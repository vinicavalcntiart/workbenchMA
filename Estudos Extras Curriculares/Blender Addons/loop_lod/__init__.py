# Loop LOD — LODs por remocao de edge loops (Blender 5.2).
#
# Como funciona:
#   1. Acha todos os edge loops da malha (caminhos que atravessam vertices de
#      valencia 4 cercados de quads).
#   2. Da a cada loop um custo: quanto a forma muda se ele sair (distancia de
#      cada vertice removido ate a reta entre os vizinhos), pesado por
#      silhueta e por pesos de deformacao.
#   3. Remove os loops mais baratos primeiro, sempre junto com o loop
#      espelhado em X, ate chegar no numero de triangulos do LOD.
#
# Loops de deformacao: a protecao vale para as ARESTAS do loop marcado (as duas
# pontas no grupo LOD_Protect). O loop nunca sai e fica no mesmo lugar, mas os
# loops que cruzam ele podem sair, entao o anel perde vertices em volta
# ("otimiza o raio, mantem a posicao").
#
# Seams, sharp, bordas e trocas de material nunca saem; os vertices em cima
# deles podem sair, e o Blender junta as duas arestas numa so, mantendo a
# marcacao (testado no 5.2.0).

import math

import bpy
import bmesh
from mathutils import Vector, kdtree
from bpy.props import (BoolProperty, CollectionProperty, EnumProperty,
                       FloatProperty, IntProperty, PointerProperty, StringProperty)
from bpy.types import Operator, Panel, PropertyGroup, UIList

INF = float("inf")


# ----------------------------------------------------------------------------
# Nucleo (sem interface; usado pelo operador e pelos testes)
# ----------------------------------------------------------------------------

class Settings:
    """Copia simples das opcoes, para o nucleo nao depender do bpy.props."""
    def __init__(self, **kw):
        self.protect_group = "LOD_Protect"
        self.lock_group = "LOD_Lock"
        self.weight_aware = True
        self.weight_influence = 1.0
        self.silhouette_pressure = 1.5
        self.max_sparsity = 6.0
        self.protect_seams = True
        self.protect_sharp = True
        self.protect_boundary = True
        self.protect_materials = True
        self.pole_fallback = True
        self.symmetry = True
        self.symmetry_tolerance_mm = 1.0
        self.optimize_protected_radius = True
        self.shape_balance = 1.0
        self.min_ring_verts = 8
        self.silhouette_tolerance_mm = 5.0
        self.__dict__.update(kw)


def tri_count(bm):
    return sum(len(f.verts) - 2 for f in bm.faces)


def _opposite_edge(v, e, stop=()):
    """Proxima aresta do loop ao passar por v; None se v e polo, borda, area travada ou toca n-gon/tri."""
    if v in stop or v.is_boundary or len(v.link_edges) != 4:
        return None
    for f in v.link_faces:
        if len(f.verts) != 4:
            return None
    fe = set(e.link_faces)
    for e2 in v.link_edges:
        if e2 is not e and not (set(e2.link_faces) & fe):
            return e2
    return None


class Loop:
    __slots__ = ("edges", "ends", "cyclic", "verts", "interior", "key", "cost", "pole_end", "simple", "bad_key", "in_lock", "ring_hits")

    def __init__(self, edges, ends, cyclic, stop=(), lock=()):
        self.edges = edges
        self.ends = ends
        self.cyclic = cyclic
        self.verts = {v for e in edges for v in e.verts}
        self.interior = self.verts if cyclic else self.verts - set(ends)
        self.key = frozenset(v.index for v in self.verts)
        # ponta na area travada nao e polo: o loop so para ali (vira um pentagono triangulado)
        self.pole_end = any(not v.is_boundary and v not in stop for v in ends)
        self.in_lock = any(e.verts[0] in lock and e.verts[1] in lock for e in edges)
        self.simple = len(self.verts) == (len(edges) if cyclic else len(edges) + 1)
        self.bad_key = frozenset(tuple(round(x, 5) for x in v.co) for v in self.verts)
        self.cost = INF
        self.ring_hits = {}


def locked_verts(bm, lock_group):
    dl = bm.verts.layers.deform.active
    if dl is None or lock_group is None:
        return set()
    return {v for v in bm.verts if v[dl].get(lock_group, 0.0) >= 0.5}


def collect_loops(bm, stop=(), lock=None):
    """stop: vertices onde o loop corta em vez de atravessar (area travada, anel no minimo)."""
    lock = stop if lock is None else lock
    seen = set()
    loops = []
    for e in bm.edges:
        if e.index in seen:
            continue
        seen.add(e.index)
        if len(e.link_faces) != 2:
            continue
        edges = [e]
        ends = []
        cyclic = False
        for d in (0, 1):
            cur, v = e, e.verts[d]
            while True:
                nxt = _opposite_edge(v, cur, stop)
                if nxt is None:
                    ends.append(v)
                    break
                if nxt is e:
                    cyclic = True
                    break
                if nxt.index in seen:
                    ends.append(v)
                    break
                seen.add(nxt.index)
                edges.append(nxt)
                v = nxt.other_vert(v)
                cur = nxt
            if cyclic:
                break
        loops.append(Loop(edges, ends, cyclic, stop, lock))
    return loops


def _ring_size(l, prot):
    """Vertices do anel, ou None se o loop nao e anel. Anel protegido conta mesmo aberto
    (um triangulo encostado quebra o loop, mas o anel continua sendo o do cotovelo)."""
    if l.cyclic:
        return len(l.edges)
    if prot and sum(1 for v in l.verts if v in prot) >= 0.85 * len(l.verts):
        return len(l.verts)
    return None


def protected_verts(bm, protect_group):
    return locked_verts(bm, protect_group)


def gather_loops(bm, lock, min_ring, prot=()):
    """Loops candidatos. Um anel fechado que ja esta no minimo (dedo, punho, braco no LOD
    baixo) vira barreira: o loop que vem do torso ou do braco para ali, em vez de ser
    recusado inteiro por atravessar ele."""
    base = collect_loops(bm, lock, lock)
    if min_ring <= 0:
        return base
    small = [l for l in base if (_ring_size(l, prot) or 10 ** 9) <= min_ring]
    if not small:
        return base
    ring_vs = set().union(*(l.verts for l in small))
    stop = set(lock) | ring_vs
    out = list(small)
    for l in collect_loops(bm, stop, lock):
        if all(e.verts[0] in ring_vs and e.verts[1] in ring_vs for e in l.edges):
            continue            # trecho entre dois aneis no minimo (ou o proprio anel)
        out.append(l)
    return out


def _boundary_cycles(bm):
    """vertice de borda -> (id do ciclo, numero de vertices do ciclo)."""
    out = {}
    cid = 0
    for v0 in bm.verts:
        if not v0.is_boundary or v0 in out:
            continue
        cyc, st = [], [v0]
        seen = {v0}
        while st:
            v = st.pop()
            cyc.append(v)
            for e in v.link_edges:
                if e.is_boundary:
                    u = e.other_vert(v)
                    if u not in seen:
                        seen.add(u)
                        st.append(u)
        for v in cyc:
            out[v] = (cid, len(cyc))
        cid += 1
    return out


def _silhouette_loss(v, a, b):
    """Quanto o contorno encolhe se v sair e a e b se ligarem. Mede na vista de frente
    (projeta em XZ) quando v esta no contorno de frente, e na de lado (YZ) quando esta no
    de lado. Ombro curvo, cintura e barra entram aqui mesmo sem ser o ponto mais externo."""
    n = v.normal
    loss = 0.0
    for drop, nc in ((1, n.y), (0, n.x)):
        if abs(nc) > 0.4:
            continue                    # vertice de frente para essa camera: nao e contorno
        keep = [i for i in range(3) if i != drop]
        p2 = Vector([v.co[i] for i in keep])
        a2 = Vector([a.co[i] for i in keep])
        b2 = Vector([b.co[i] for i in keep])
        loss = max(loss, _point_seg_dist(p2, a2, b2))
    return loss


def _point_seg_dist(p, a, b):
    ab = b - a
    L2 = ab.length_squared
    if L2 < 1e-20:
        return (p - a).length
    t = max(0.0, min(1.0, (p - a).dot(ab) / L2))
    return (p - (a + ab * t)).length


def _propagate_mirror(bm, m):
    """Topology mirror: a partir dos pares certos, pareia os vizinhos pela topologia.
    Pega o que a distancia nao pega (mao, dedo, dobra esculpida com assimetria maior
    que a aresta). So aceita par mutuo e com a mesma valencia."""
    # so pares mutuos valem como semente
    for i in [i for i, j in m.items() if m.get(j) != i]:
        del m[i]
    vs = bm.verts
    for _ in range(64):
        new = {}
        taken = set(m.values())
        for i, j in m.items():
            v, w = vs[i], vs[j]
            free_v = [e.other_vert(v) for e in v.link_edges if e.other_vert(v).index not in m]
            if not free_v:
                continue
            free_w = [e.other_vert(w) for e in w.link_edges
                      if e.other_vert(w).index not in taken and e.other_vert(w).index not in new.values()]
            if not free_w:
                continue
            for b in free_v:
                if b.index in new:
                    continue
                mb = Vector((-b.co.x, b.co.y, b.co.z))
                cands = [c for c in free_w if len(c.link_edges) == len(b.link_edges)]
                if not cands:
                    continue
                c = min(cands, key=lambda c: (c.co - mb).length_squared)
                # mutuo: b tambem e o mais perto de c entre os livres de v
                mc = Vector((-c.co.x, c.co.y, c.co.z))
                if min(free_v, key=lambda x: (x.co - mc).length_squared) is not b:
                    continue
                if c.index in new.values() or (c.index in new and new[c.index] != b.index):
                    continue
                new[b.index] = c.index
                new[c.index] = b.index
        if not new:
            break
        m.update(new)


class _Ctx:
    """Dados por passada: pesos, espelho, juntas."""
    def __init__(self, bm, obj, s):
        bm.verts.index_update(); bm.edges.index_update(); bm.faces.index_update()
        bm.verts.ensure_lookup_table()
        bm.normal_update()
        self.s = s
        self.bad = set()
        dl = bm.verts.layers.deform.active
        self.dl = dl
        gp = obj.vertex_groups.get(s.protect_group) if obj else None
        self.gp = gp.index if gp else None
        gl = obj.vertex_groups.get(s.lock_group) if obj else None
        self.gl = gl.index if gl else None
        self.deform_groups = [g.index for g in obj.vertex_groups if g.index not in (self.gp, self.gl)] if obj else []
        self._jf = {}
        self.why = None
        sc = max((abs(x) for x in obj.matrix_world.to_scale()), default=1.0) if obj else 1.0
        self.sil_tol = s.silhouette_tolerance_mm * 0.001 / max(sc, 1e-9)
        self.prot = set()
        self.edge_loop = {}
        self.bcycle = _boundary_cycles(bm)
        # espelho X
        self.mirror = None
        if s.symmetry:
            kd = kdtree.KDTree(len(bm.verts))
            for v in bm.verts:
                kd.insert(v.co, v.index)
            kd.balance()
            sc = max((abs(x) for x in obj.matrix_world.to_scale()), default=1.0) if obj else 1.0
            tol = s.symmetry_tolerance_mm * 0.001 / max(sc, 1e-9)    # mm no mundo -> unidade local
            self.mirror = {}
            for v in bm.verts:
                co, i, d = kd.find(Vector((-v.co.x, v.co.y, v.co.z)))
                if i is None:
                    continue
                # malha esculpida (pano, dobras) nunca e simetrica ao milimetro: aceita o par
                # se ele esta a menos de 40% da menor aresta do vertice. O par so vale se o
                # loop espelhado inteiro existir, entao a topologia continua conferida.
                lim = tol
                if v.link_edges:
                    lim = max(tol, 0.4 * min(e.calc_length() for e in v.link_edges))
                if d <= lim:
                    self.mirror[v.index] = i
            _propagate_mirror(bm, self.mirror)

    def protect_w(self, v):
        if self.dl is None or self.gp is None:
            return 0.0
        return v[self.dl].get(self.gp, 0.0)

    def lock_w(self, v):
        if self.dl is None or self.gl is None:
            return 0.0
        return v[self.dl].get(self.gl, 0.0)

    def joint_factor(self, v):
        """Maior variacao de peso de deformacao entre v e os vizinhos (0 a 1)."""
        if v.index in self._jf:
            return self._jf[v.index]
        r = 0.0
        if self.dl is not None and self.deform_groups:
            wv = v[self.dl]
            for e in v.link_edges:
                wu = e.other_vert(v)[self.dl]
                for g in self.deform_groups:
                    d = abs(wv.get(g, 0.0) - wu.get(g, 0.0))
                    if d > r:
                        r = d
        self._jf[v.index] = min(r, 1.0)
        return self._jf[v.index]


def _edge_protected(e, c):
    return c.protect_w(e.verts[0]) >= 0.5 and c.protect_w(e.verts[1]) >= 0.5


def _edge_blocked(e, c):
    """Motivo do bloqueio da aresta, ou None."""
    s = c.s
    if len(e.link_faces) != 2:
        return "aresta de borda"
    if s.protect_seams and e.seam:
        return "UV seam"
    if s.protect_sharp and not e.smooth:
        return "sharp edge"
    if s.protect_materials and e.link_faces[0].material_index != e.link_faces[1].material_index:
        return "borda de material"
    if not c.s.optimize_protected_radius and _edge_protected(e, c):
        return "area protegida"
    for f in e.link_faces:
        if len(f.verts) != 4:
            return "vizinho de triangulo/n-gon"
    return None


def _rej(c, why, loop=None):
    if c.why is not None and (loop is None or len(loop.edges) > 1):
        c.why[why] = c.why.get(why, 0) + 1
    return INF


def _face_width(f, e):
    """Distancia do meio de e ate o meio da aresta oposta no quad f."""
    a, b = e.verts
    opp = [x for x in f.edges if a not in x.verts and b not in x.verts]
    if not opp:
        return e.calc_length()
    m1 = (a.co + b.co) * 0.5
    o = opp[0]
    m2 = (o.verts[0].co + o.verts[1].co) * 0.5
    return (m1 - m2).length


def loop_cost(loop, c, allow_poles):
    s = c.s
    if loop.pole_end and not allow_poles:
        return _rej(c, "termina em polo (so no Pole Fallback)")
    if not loop.simple:
        return _rej(c, "loop cruza a si mesmo")
    if loop.bad_key in c.bad:
        return _rej(c, "desfeito: criava dobra, lasca, non-manifold ou nao reduzia")
    if loop.in_lock or any(c.lock_w(v) >= 0.5 for v in loop.interior):
        return _rej(c, "area travada")      # maos, rosto: nada dentro dela sai
    prot = 0
    for e in loop.edges:
        why = _edge_blocked(e, c)
        if why:
            return _rej(c, why, loop)
        if _edge_protected(e, c):
            prot += 1
    if prot >= 0.85 * len(loop.edges):
        return _rej(c, "anel protegido")    # loop de deformacao: fica no lugar
    # esparsidade: as duas faixas viram uma so; a nova face nao pode ficar comprida demais
    shape = 0.0
    for e in loop.edges:
        L = e.calc_length()
        w = sum(_face_width(f, e) for f in e.link_faces)
        if L < 1e-9 or w < 1e-9:
            return _rej(c, "aresta degenerada")
        a = max(w / L, L / w)
        if a > s.max_sparsity:
            return _rej(c, "face ficaria comprida (Max Sparsity)")
        # equilibrio de forma: tirar o loop que deixa a face mais quadrada vem antes.
        # Sem isso, num cilindro reto os aneis no comprimento (erro zero) saem todos
        # antes do raio diminuir.
        shape += (a - 1.0) ** 2 * min(L, w)
    edge_set = set(loop.edges)
    # resolucao minima: cada anel que este loop cruza perde 1 vertice por cruzamento.
    # Braco, perna e dedo nao podem cair abaixo de min_ring_verts (deformacao e volume).
    hits = {}
    if s.min_ring_verts > 0:
        for v in loop.interior:
            for x in v.link_edges:
                if x in edge_set:
                    continue
                r = c.edge_loop.get(x)
                if r is not None and r is not loop:
                    size = _ring_size(r, c.prot)
                    if size is not None:
                        k = ('r', id(r))
                        n, h = hits.get(k, (size, 0))
                        hits[k] = (n, h + 1)
                break
        if not loop.cyclic:
            for v in loop.ends:
                if v.is_boundary and v in c.bcycle:
                    cid, n = c.bcycle[v]
                    k = ('b', cid)
                    hits[k] = (n, hits.get(k, (n, 0))[1] + 1)
        for n, h in hits.values():
            if n - h < s.min_ring_verts:
                return _rej(c, "anel ficaria abaixo de Min Ring Verts")
    loop.ring_hits = hits
    total = 0.0
    for v in loop.interior:
        others = [x.other_vert(v) for x in v.link_edges if x not in edge_set]
        if len(others) != 2:
            continue
        if _silhouette_loss(v, others[0], others[1]) > c.sil_tol:
            return _rej(c, "silhueta (Silhouette Tolerance)", loop)
        err = _point_seg_dist(v.co, others[0].co, others[1].co)
        n = v.normal
        sil = max(1.0 - abs(n.y), 1.0 - abs(n.x)) ** 4      # perfil de frente e de lado
        k = 1.0 + s.silhouette_pressure * sil
        if s.weight_aware:
            k *= 1.0 + s.weight_influence * 4.0 * c.joint_factor(v)
        pw = c.protect_w(v)
        if 0.0 < pw < 0.5:                                  # protecao suave
            k *= 1.0 + 10.0 * pw
        total += err * k
    # pontas na borda: o vertice sai e a abertura perde um ponto (como o anel protegido)
    if not loop.cyclic:
        for v in loop.ends:
            if not v.is_boundary:
                continue
            bn = [x.other_vert(v) for x in v.link_edges if x.is_boundary]
            if len(bn) != 2:
                continue
            if _silhouette_loss(v, bn[0], bn[1]) > c.sil_tol:
                return _rej(c, "silhueta (Silhouette Tolerance)", loop)
            err = _point_seg_dist(v.co, bn[0].co, bn[1].co)
            total += err * (5.0 if s.protect_boundary else 1.0) * (1.0 + s.silhouette_pressure)
    total += s.shape_balance * 0.05 * shape
    return total / max(1, 2 * len(loop.edges))


def _faces_of(loop):
    return {f for e in loop.edges for f in e.link_faces}


def fold_count(bm, max_angle=1.75):
    """Arestas dobradas (faces vizinhas quase viradas uma contra a outra, > ~100 graus)."""
    n = 0
    for e in bm.edges:
        if len(e.link_faces) == 2:
            try:
                if e.calc_face_angle() > max_angle:
                    n += 1
            except ValueError:
                n += 1
    return n


def _min_angle(f):
    vs = [v.co for v in f.verts]
    n = len(vs)
    m = math.pi
    for i in range(n):
        a = vs[i - 1] - vs[i]
        b = vs[(i + 1) % n] - vs[i]
        if a.length_squared < 1e-20 or b.length_squared < 1e-20:
            return 0.0
        m = min(m, a.angle(b))
    return m


def sliver_count(bm, min_angle=math.radians(14)):
    """Faces com algum canto muito fechado (triangulo-lasca). Deformam mal e sombreiam mal."""
    return sum(1 for f in bm.faces if _min_angle(f) < min_angle)


def health(bm):
    """(non-manifold + vertice solto, dobras, lascas). Nenhum pode aumentar."""
    return (nonmanifold_count(bm), fold_count(bm), sliver_count(bm))


def _healthy(bm, before):
    return all(a <= b for a, b in zip(health(bm), before))


def _fail_reason(bm, before, t_before):
    h = health(bm)
    for name, a, b in zip(("non-manifold", "dobra", "lasca"), h, before):
        if a > b:
            return name
    if tri_count(bm) >= t_before:
        return "nao reduzia"
    return None


def nonmanifold_count(bm):
    return sum(1 for e in bm.edges if not e.is_manifold and not e.is_boundary) + \
           sum(1 for v in bm.verts if not v.link_edges)


def _dissolve(bm, loops):
    edges = [e for l in loops for e in l.edges]
    cand = set()
    for l in loops:
        cand |= l.interior
        cand |= {v for v in l.ends if v.is_boundary}
    near = {f for l in loops for e in l.edges for f in e.link_faces}
    bmesh.ops.dissolve_edges(bm, edges=edges, use_verts=False, use_face_split=False)
    rem = [v for v in cand if v.is_valid and len(v.link_edges) == 2]
    if rem:
        bmesh.ops.dissolve_verts(bm, verts=rem, use_face_split=False, use_boundary_tear=False)
    # n-gons (pontas em polo): triangula e junta de volta o que der em quad
    # (pentagono vira quad + triangulo, hexagono vira 2 quads). Triangulo solto trava os
    # loops em volta, entao quanto menos sobrar, mais o LOD reduz.
    ngons = [f for f in bm.faces if len(f.verts) > 4]
    if ngons:
        tris = bmesh.ops.triangulate(bm, faces=ngons, quad_method='BEAUTY', ngon_method='BEAUTY')['faces']
        tris = [f for f in tris if f.is_valid and len(f.verts) == 3]
        if tris:
            bmesh.ops.join_triangles(bm, faces=tris, cmp_seam=True, cmp_sharp=True, cmp_materials=True,
                                     angle_face_threshold=math.radians(40), angle_shape_threshold=math.radians(60))


def _snapshot(bm):
    me = bpy.data.meshes.new("_looplod_tmp")
    bm.to_mesh(me)
    return me


def _restore(bm, me):
    bm.clear()
    bm.from_mesh(me)
    bpy.data.meshes.remove(me)


def _apply_checked(bm, groups, before_nm, bad, lock_group=None, min_ring=0, protect_group=None, why=None):
    """Aplica o lote; se criar non-manifold ou dobra, ou nao reduzir, desfaz e tenta grupo por
    grupo (loop + espelho juntos, para nao quebrar a simetria), marcando os ruins."""
    key_groups = [[l.bad_key for l in g] for g in groups]
    t0 = tri_count(bm)
    snap = _snapshot(bm)
    _dissolve(bm, [l for g in groups for l in g])
    # cada grupo tem que tirar triangulo: loop que so troca 2 quads por 2 quads entra em ciclo
    if _healthy(bm, before_nm) and t0 - tri_count(bm) >= 2 * len(groups):
        bpy.data.meshes.remove(snap)
        return len(groups)
    _restore(bm, snap)
    applied = 0
    for keys in key_groups:
        bm.verts.ensure_lookup_table()
        current = {l.bad_key: l for l in gather_loops(bm, locked_verts(bm, lock_group), min_ring,
                                                       protected_verts(bm, protect_group))}
        loops = [current[k] for k in keys if k in current]
        if len(loops) != len(keys):
            continue
        t1 = tri_count(bm)
        snap = _snapshot(bm)
        _dissolve(bm, loops)
        fr = _fail_reason(bm, before_nm, t1)
        if fr is None:
            bpy.data.meshes.remove(snap)
            applied += 1
        else:
            _restore(bm, snap)
            bad.update(keys)
            if why is not None:
                k = "desfeito na hora: " + fr
                why[k] = why.get(k, 0) + 1
    return applied


def reduce_mesh(bm, obj, target_tris, s, log=None, report=None):
    """Remove loops ate tri_count(bm) <= target_tris. Devolve o numero de passadas.
    report (dict): recebe os motivos de recusa da ultima passada e o motivo da parada."""
    allow_poles = False
    passes = 0
    bad = set()
    why = {}
    undo_why = {}
    stop = "alvo atingido"
    while tri_count(bm) > target_tris and passes < 400:
        passes += 1
        c = _Ctx(bm, obj, s)
        c.bad = bad
        c.why = why = {}
        if report is not None and passes == 1 and c.mirror is not None:
            report["espelho"] = len(c.mirror) / max(1, len(bm.verts))
        c.prot = protected_verts(bm, c.gp)
        loops = gather_loops(bm, locked_verts(bm, c.gl), s.min_ring_verts, c.prot)
        by_key = {l.key: l for l in loops}
        c.edge_loop = {e: l for l in loops for e in l.edges}
        groups = []
        for l in loops:
            l.cost = loop_cost(l, c, allow_poles)
        done = set()
        for l in loops:
            if l.cost == INF or id(l) in done:
                continue
            group = [l]
            if c.mirror is not None:
                mk = frozenset(c.mirror.get(i, -1) for i in l.key)
                m = by_key.get(mk)
                if m is None:
                    _rej(c, "sem par espelhado (X Symmetry)")
                    continue                    # fica, para manter a simetria
                if m is not l:
                    if m.cost == INF:
                        _rej(c, "par espelhado recusado")
                        continue
                    group.append(m)
            for g in group:
                done.add(id(g))
            groups.append((sum(g.cost for g in group), group))
        groups.sort(key=lambda t: t[0])
        need = tri_count(bm) - target_tris
        used_v, used_f, batch, est = set(), set(), [], 0
        ring_used = {}
        chosen = []
        for cost, group in groups:
            vs = set().union(*(g.verts for g in group))
            fs = set().union(*(_faces_of(g) for g in group))
            if vs & used_v or fs & used_f:
                continue
            rh = {}
            for g in group:
                for k, (n, h) in g.ring_hits.items():
                    rh[k] = (n, rh.get(k, (n, 0))[1] + h)
            if any(n - h - ring_used.get(k, 0) < s.min_ring_verts for k, (n, h) in rh.items()):
                continue
            for k, (n, h) in rh.items():
                ring_used[k] = ring_used.get(k, 0) + h
            used_v |= vs
            used_f |= fs
            batch.extend(group)
            chosen.append(group)
            est += sum(2 * len(g.edges) for g in group)
            if est >= need:
                break
        if not batch:
            if s.pole_fallback and not allow_poles:
                allow_poles = True
                continue
            stop = "acabaram os loops que podem sair"
            break
        before_nm = health(bm)
        applied = _apply_checked(bm, chosen, before_nm, bad, c.gl, s.min_ring_verts, c.gp, undo_why)
        if log:
            log(f"passada {passes}: {applied}/{len(chosen)} grupos, {tri_count(bm)} tris")
    if passes >= 400 and tri_count(bm) > target_tris:
        stop = "limite de passadas"
    if report is not None:
        report["parada"] = stop
        allw = dict(why)
        allw.pop("desfeito: criava dobra, lasca, non-manifold ou nao reduzia", None)
        allw.update(undo_why)
        report["motivos"] = dict(sorted(allw.items(), key=lambda t: -t[1]))
    return passes


# ----------------------------------------------------------------------------
# Interface
# ----------------------------------------------------------------------------

class LOOPLOD_LodItem(PropertyGroup):
    ratio: FloatProperty(name="Ratio", default=0.5, min=0.01, max=1.0,
                         description="Fracao dos triangulos do original")
    min_ring: IntProperty(name="Min Ring", default=0, min=0, max=64,
                          description="Anel minimo so deste LOD. 0 = usa o Min Ring Verts geral. "
                                      "LOD baixo costuma ir a 6")
    max_sparsity: FloatProperty(name="Max Sparsity", default=0.0, min=0.0, max=50.0,
                                description="Max Sparsity so deste LOD. 0 = usa o geral. "
                                            "Mais alto aceita faces mais compridas e reduz mais")
    silhouette: FloatProperty(name="Silhouette Tolerance", default=0.0, min=0.0, max=1000.0,
                              description="Tolerancia de silhueta (mm) so deste LOD. 0 = a geral dobrada a cada "
                                          "LOD (5, 10, 20 mm...), porque o LOD de longe aguenta mais erro")


def _settings_from(p):
    return Settings(
        protect_group=p.protect_group, lock_group=p.lock_group, weight_aware=p.weight_aware,
        weight_influence=p.weight_influence, silhouette_pressure=p.silhouette_pressure,
        max_sparsity=p.max_sparsity, protect_seams=p.protect_seams,
        protect_sharp=p.protect_sharp, protect_boundary=p.protect_boundary,
        protect_materials=p.protect_materials, pole_fallback=p.pole_fallback,
        symmetry=p.symmetry, symmetry_tolerance_mm=p.symmetry_tolerance,
        optimize_protected_radius=p.optimize_protected_radius,
        shape_balance=p.shape_balance, min_ring_verts=p.min_ring_verts,
        silhouette_tolerance_mm=p.silhouette_tolerance)


class LOOPLOD_Settings(PropertyGroup):
    protect_group: StringProperty(name="Deformation Loops", default="LOD_Protect",
        description="Grupo de vertices com os loops de deformacao. O loop fica no lugar; os loops que cruzam ele podem sair")
    lock_group: StringProperty(name="Locked Areas", default="LOD_Lock",
        description="Grupo de vertices que nao muda em nenhum LOD (maos, rosto). Os loops que chegam nela param na borda (vira triangulo ali)")
    weight_aware: BoolProperty(name="Weight-Aware Cost", default=True,
        description="Encarece remover loops onde os pesos de deformacao mudam (juntas)")
    weight_influence: FloatProperty(name="Weight Influence", default=1.0, min=0.0, max=10.0)
    silhouette_pressure: FloatProperty(name="Silhouette Pressure", default=1.5, min=0.0, max=20.0,
        description="Quanto mais alto, mais o contorno de frente e de lado e preservado")
    max_sparsity: FloatProperty(name="Max Sparsity", default=6.0, min=1.5, max=50.0,
        description="Proporcao maxima (comprimento / largura) de uma face depois de remover um loop")
    protect_seams: BoolProperty(name="Protect UV Seams", default=True)
    protect_sharp: BoolProperty(name="Protect Sharp Edges", default=True)
    protect_boundary: BoolProperty(name="Protect Boundaries", default=True,
        description="Aberturas (pescoco, punhos) ficam no lugar e so perdem vertices onde quase nao mudam a forma")
    protect_materials: BoolProperty(name="Protect Material Borders", default=True)
    pole_fallback: BoolProperty(name="Pole Fallback", default=True,
        description="Quando acabam os loops limpos, aceita loops que terminam em polos (gera alguns n-gons)")
    optimize_protected_radius: BoolProperty(name="Optimize Protected Radius", default=True,
        description="Os aneis protegidos ficam no lugar, mas os loops que cruzam eles podem sair (o anel perde vertices em volta). Desligado: nada que toca a area protegida sai")
    silhouette_tolerance: FloatProperty(name="Silhouette Tolerance", default=5.0, min=0.0, max=1000.0,
        description="Quanto (mm) o contorno de frente, de lado ou de cima pode encolher num ponto. "
                    "Vertice que forma o contorno e passaria disso fica")
    min_ring_verts: IntProperty(name="Min Ring Verts", default=8, min=0, max=64,
        description="Nenhum anel fechado (braco, perna, dedo) nem abertura (barra, gola) fica com menos vertices que isso. 8 segura volume e deformacao de cotovelo e joelho; 0 desliga")
    shape_balance: FloatProperty(name="Shape Balance", default=1.0, min=0.0, max=10.0,
        description="Mantem as faces perto de quadradas: alterna entre tirar aneis no comprimento e reduzir o raio. 0 = so o erro de forma decide")
    symmetry: BoolProperty(name="X Symmetry", default=True)
    last_report: StringProperty(default="")
    symmetry_tolerance: FloatProperty(name="Symmetry Tolerance", default=1.0, min=0.0, max=100.0,
        description="Distancia maxima, em mm, entre um vertice e o espelho dele")
    use_evaluated: BoolProperty(name="Use Modifiers (Geometry Nodes)", default=True,
        description="Usa a malha com os modificadores aplicados (Geometry Nodes, Mirror...). Armature fica desligado e e mantido nos LODs")
    triangulate: BoolProperty(name="Triangulate Result", default=False)
    lods: CollectionProperty(type=LOOPLOD_LodItem)
    lod_index: IntProperty(default=0)
    name_mode: EnumProperty(name="Naming", items=[
        ('REPLACE', "Replace LOD0 token", "Troca LOD0 no nome por LOD1, LOD2..."),
        ('SUFFIX', "Add _LODn suffix", "Acrescenta _LOD1, _LOD2...")], default='REPLACE')
    collection: StringProperty(name="Collection", default="LODs")


class LOOPLOD_UL_lods(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row(align=True)
        row.label(text=f"LOD{index + 1}")
        row.prop(item, "ratio", text="")


class LOOPLOD_OT_lod_add(Operator):
    bl_idname = "looplod.lod_add"
    bl_label = "Adicionar LOD"
    bl_options = {'UNDO'}

    def execute(self, context):
        p = context.scene.loop_lod
        it = p.lods.add()
        it.ratio = p.lods[-2].ratio * 0.5 if len(p.lods) > 1 else 0.5
        p.lod_index = len(p.lods) - 1
        return {'FINISHED'}


class LOOPLOD_OT_lod_remove(Operator):
    bl_idname = "looplod.lod_remove"
    bl_label = "Remover LOD"
    bl_options = {'UNDO'}

    def execute(self, context):
        p = context.scene.loop_lod
        if p.lods:
            p.lods.remove(p.lod_index)
            p.lod_index = max(0, p.lod_index - 1)
        return {'FINISHED'}


class LOOPLOD_OT_mark(Operator):
    bl_idname = "looplod.mark_protected"
    bl_label = "Mark Selected as Protected"
    bl_description = "No Edit Mode: poe os vertices selecionados no grupo dos loops de deformacao (peso 1)"
    bl_options = {'REGISTER', 'UNDO'}
    clear: BoolProperty(default=False)
    target: EnumProperty(items=[('PROTECT', "Protect", ""), ('LOCK', "Lock", "")], default='PROTECT')

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH' and context.mode == 'EDIT_MESH'

    def execute(self, context):
        ob = context.object
        p = context.scene.loop_lod
        name = p.protect_group if self.target == 'PROTECT' else p.lock_group
        g = ob.vertex_groups.get(name) or ob.vertex_groups.new(name=name)
        bm = bmesh.from_edit_mesh(ob.data)
        dl = bm.verts.layers.deform.verify()
        n = 0
        for v in bm.verts:
            if v.select:
                if self.clear:
                    if g.index in v[dl]:
                        del v[dl][g.index]
                else:
                    v[dl][g.index] = 1.0
                n += 1
        bmesh.update_edit_mesh(ob.data)
        self.report({'INFO'}, f"{n} vertices {'tirados do' if self.clear else 'no'} grupo {g.name}")
        return {'FINISHED'}


def _lod_name(name, n, mode):
    if mode == 'REPLACE' and "LOD0" in name:
        return name.replace("LOD0", f"LOD{n}")
    return f"{name}_LOD{n}"


def _source_mesh(context, ob, use_evaluated):
    if not use_evaluated:
        return ob.data.copy()
    arm = [m for m in ob.modifiers if m.type == 'ARMATURE' and m.show_viewport]
    for m in arm:
        m.show_viewport = False
    try:
        dg = context.evaluated_depsgraph_get()
        dg.update()
        me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg), preserve_all_data_layers=True, depsgraph=dg)
    finally:
        for m in arm:
            m.show_viewport = True
    return me


def generate_lods(context, ob, p, log=None):
    if not p.lods:
        for r, ring, sp in ((0.5, 0, 0.0), (0.25, 0, 0.0), (0.125, 6, 12.0)):
            it = p.lods.add()
            it.ratio, it.min_ring, it.max_sparsity = r, ring, sp
    s = _settings_from(p)
    col = bpy.data.collections.get(p.collection)
    if col is None:
        col = bpy.data.collections.new(p.collection)
        context.scene.collection.children.link(col)
    base = _source_mesh(context, ob, p.use_evaluated)
    bm0 = bmesh.new()
    bm0.from_mesh(base)
    src_tris = tri_count(bm0)
    bm0.free()
    out = []
    reports = []
    for i, it in enumerate(p.lods, start=1):
        me = base.copy()
        bm = bmesh.new()
        bm.from_mesh(me)
        target = max(1, int(round(src_tris * it.ratio)))
        rep = {}
        over = {}
        if it.min_ring > 0:
            over["min_ring_verts"] = it.min_ring
        if it.max_sparsity > 0:
            over["max_sparsity"] = it.max_sparsity
        over["silhouette_tolerance_mm"] = it.silhouette if it.silhouette > 0 else \
            s.silhouette_tolerance_mm * 2 ** (i - 1)
        si = Settings(**dict(s.__dict__, **over)) if over else s
        reduce_mesh(bm, ob, target, si, log=log, report=rep)
        reports.append((i, target, rep))
        if p.triangulate:
            bmesh.ops.triangulate(bm, faces=bm.faces[:])
        got = tri_count(bm)
        bm.to_mesh(me)
        bm.free()
        name = _lod_name(ob.name, i, p.name_mode)
        old = bpy.data.objects.get(name)
        if old is not None:
            bpy.data.objects.remove(old)
        new = ob.copy()
        new.data = me
        new.name = name
        me.name = name
        if p.use_evaluated:
            for m in list(new.modifiers):
                if m.type != 'ARMATURE':
                    new.modifiers.remove(m)
        for c in list(new.users_collection):
            c.objects.unlink(new)
        col.objects.link(new)
        out.append((name, target, got))
    bpy.data.meshes.remove(base)
    lines = []
    prev = None
    for (i, target, rep), (name, _t, got) in zip(reports, out):
        lines.append(f"LOD{i}: {got} tris (alvo {target}) - {rep.get('parada', 'alvo atingido')}")
        if prev is not None and got >= prev:
            lines.append(f"   IGUAL ao LOD{i - 1}: neste LOD suba Silhouette ou Max Sparsity, ou baixe Min Ring")
        prev = got
        if got > target * 1.15:
            for k, n in list(rep.get("motivos", {}).items())[:5]:
                lines.append(f"   {n}x {k}")
    if reports and "espelho" in reports[0][2] and reports[0][2]["espelho"] < 0.98:
        lines.append(f"Simetria: so {reports[0][2]['espelho']:.0%} dos vertices tem par. "
                     "Aumente Symmetry Tolerance ou desligue X Symmetry")
    p.last_report = "\n".join(lines)
    return src_tris, out


class LOOPLOD_OT_generate(Operator):
    bl_idname = "looplod.generate"
    bl_label = "Generate LODs"
    bl_description = "Gera os LODs da lista na colecao, a partir do objeto ativo"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH' and context.mode == 'OBJECT'

    def execute(self, context):
        src, out = generate_lods(context, context.object, context.scene.loop_lod)
        msg = ", ".join(f"{n}: {g} tris" for n, t, g in out)
        self.report({'INFO'}, f"Original {src} tris. {msg}")
        return {'FINISHED'}


class LOOPLOD_PT_panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loop LOD"
    bl_label = "Loop LOD"

    def draw(self, context):
        lay = self.layout
        p = context.scene.loop_lod
        ob = context.object
        b = lay.box()
        b.label(text="Deformation Loops", icon='GROUP_VERTEX')
        if ob and ob.type == 'MESH':
            b.prop_search(p, "protect_group", ob, "vertex_groups", text="")
        else:
            b.prop(p, "protect_group", text="")
        r = b.row(align=True)
        o = r.operator("looplod.mark_protected", text="Mark Selected as Protected", icon='ADD'); o.clear = False; o.target = 'PROTECT'
        o = r.operator("looplod.mark_protected", text="", icon='REMOVE'); o.clear = True; o.target = 'PROTECT'
        b.label(text="Locked Areas (hands, face)", icon='LOCKED')
        if ob and ob.type == 'MESH':
            b.prop_search(p, "lock_group", ob, "vertex_groups", text="")
        else:
            b.prop(p, "lock_group", text="")
        r = b.row(align=True)
        o = r.operator("looplod.mark_protected", text="Mark Selected as Locked", icon='ADD'); o.clear = False; o.target = 'LOCK'
        o = r.operator("looplod.mark_protected", text="", icon='REMOVE'); o.clear = True; o.target = 'LOCK'
        b.prop(p, "optimize_protected_radius")
        b.prop(p, "weight_aware")
        sub = b.row(); sub.active = p.weight_aware; sub.prop(p, "weight_influence")
        b = lay.box()
        b.label(text="Silhouette", icon='MOD_OUTLINE')
        b.prop(p, "silhouette_pressure")
        b.prop(p, "silhouette_tolerance")
        b.prop(p, "max_sparsity")
        b.prop(p, "shape_balance")
        b.prop(p, "min_ring_verts")
        b = lay.box()
        b.label(text="Keep Intact", icon='LOCKED')
        for k in ("protect_seams", "protect_sharp", "protect_boundary", "protect_materials", "pole_fallback"):
            b.prop(p, k)
        b = lay.box()
        b.label(text="Symmetry", icon='MOD_MIRROR')
        b.prop(p, "symmetry")
        sub = b.row(); sub.active = p.symmetry; sub.prop(p, "symmetry_tolerance")
        b = lay.box()
        b.label(text="LOD Chain", icon='MOD_DECIM')
        row = b.row()
        row.template_list("LOOPLOD_UL_lods", "", p, "lods", p, "lod_index", rows=3)
        col = row.column(align=True)
        col.operator("looplod.lod_add", text="", icon='ADD')
        col.operator("looplod.lod_remove", text="", icon='REMOVE')
        if 0 <= p.lod_index < len(p.lods):
            it = p.lods[p.lod_index]
            sub = b.column(align=True)
            sub.label(text=f"So no LOD{p.lod_index + 1} (0 = geral):")
            sub.prop(it, "min_ring", text="Min Ring Verts")
            sub.prop(it, "max_sparsity", text="Max Sparsity")
            auto = p.silhouette_tolerance * 2 ** p.lod_index
            sub.prop(it, "silhouette", text=f"Silhouette (0 = {auto:g} mm)")
        b.prop(p, "name_mode", text="")
        b.prop(p, "collection")
        b.prop(p, "use_evaluated")
        b.prop(p, "triangulate")
        lay.operator("looplod.generate", icon='PLAY')
        if ob and ob.type == 'MESH':
            tris = sum(len(f.vertices) - 2 for f in ob.data.polygons)
            lay.label(text=f"Active: {tris:,} tris", icon='INFO')
        if p.last_report:
            b = lay.box()
            b.label(text="Ultima geracao", icon='TEXT')
            col = b.column(align=True)
            col.scale_y = 0.8
            for line in p.last_report.split("\n"):
                col.label(text=line)


classes = (LOOPLOD_LodItem, LOOPLOD_Settings, LOOPLOD_UL_lods, LOOPLOD_OT_lod_add,
           LOOPLOD_OT_lod_remove, LOOPLOD_OT_mark, LOOPLOD_OT_generate, LOOPLOD_PT_panel)


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.loop_lod = PointerProperty(type=LOOPLOD_Settings)


def unregister():
    del bpy.types.Scene.loop_lod
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
