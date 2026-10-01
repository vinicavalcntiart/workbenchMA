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
        self.__dict__.update(kw)


def tri_count(bm):
    return sum(len(f.verts) - 2 for f in bm.faces)


def _opposite_edge(v, e):
    """Proxima aresta do loop ao passar por v; None se v e polo, borda ou toca n-gon/tri."""
    if v.is_boundary or len(v.link_edges) != 4:
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
    __slots__ = ("edges", "ends", "cyclic", "verts", "interior", "key", "cost", "pole_end")

    def __init__(self, edges, ends, cyclic):
        self.edges = edges
        self.ends = ends
        self.cyclic = cyclic
        self.verts = {v for e in edges for v in e.verts}
        self.interior = self.verts if cyclic else self.verts - set(ends)
        self.key = frozenset(v.index for v in self.verts)
        self.pole_end = any(not v.is_boundary for v in ends)
        self.cost = INF


def collect_loops(bm):
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
                nxt = _opposite_edge(v, cur)
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
        loops.append(Loop(edges, ends, cyclic))
    return loops


def _point_seg_dist(p, a, b):
    ab = b - a
    L2 = ab.length_squared
    if L2 < 1e-20:
        return (p - a).length
    t = max(0.0, min(1.0, (p - a).dot(ab) / L2))
    return (p - (a + ab * t)).length


class _Ctx:
    """Dados por passada: pesos, espelho, juntas."""
    def __init__(self, bm, obj, s):
        bm.verts.index_update(); bm.edges.index_update(); bm.faces.index_update()
        bm.verts.ensure_lookup_table()
        bm.normal_update()
        self.s = s
        dl = bm.verts.layers.deform.active
        self.dl = dl
        gp = obj.vertex_groups.get(s.protect_group) if obj else None
        self.gp = gp.index if gp else None
        self.deform_groups = [g.index for g in obj.vertex_groups if g.index != self.gp] if obj else []
        self._jf = {}
        # espelho X
        self.mirror = None
        if s.symmetry:
            kd = kdtree.KDTree(len(bm.verts))
            for v in bm.verts:
                kd.insert(v.co, v.index)
            kd.balance()
            tol = s.symmetry_tolerance_mm * 0.001
            self.mirror = {}
            for v in bm.verts:
                co, i, d = kd.find(Vector((-v.co.x, v.co.y, v.co.z)))
                if i is not None and d <= tol:
                    self.mirror[v.index] = i

    def protect_w(self, v):
        if self.dl is None or self.gp is None:
            return 0.0
        return v[self.dl].get(self.gp, 0.0)

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


def _edge_blocked(e, c):
    s = c.s
    if len(e.link_faces) != 2:
        return True
    if s.protect_seams and e.seam:
        return True
    if s.protect_sharp and not e.smooth:
        return True
    if s.protect_materials and e.link_faces[0].material_index != e.link_faces[1].material_index:
        return True
    if c.protect_w(e.verts[0]) >= 0.5 and c.protect_w(e.verts[1]) >= 0.5:
        return True   # aresta de loop de deformacao: o loop fica
    for f in e.link_faces:
        if len(f.verts) != 4:
            return True
    return False


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
        return INF
    for e in loop.edges:
        if _edge_blocked(e, c):
            return INF
    # esparsidade: as duas faixas viram uma so; a nova face nao pode ficar comprida demais
    for e in loop.edges:
        L = e.calc_length()
        w = sum(_face_width(f, e) for f in e.link_faces)
        if L < 1e-9 or w < 1e-9:
            return INF
        if max(w / L, L / w) > s.max_sparsity:
            return INF
    edge_set = set(loop.edges)
    total = 0.0
    for v in loop.interior:
        others = [x.other_vert(v) for x in v.link_edges if x not in edge_set]
        if len(others) != 2:
            continue
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
            err = _point_seg_dist(v.co, bn[0].co, bn[1].co)
            total += err * (5.0 if s.protect_boundary else 1.0) * (1.0 + s.silhouette_pressure)
    return total / max(1, 2 * len(loop.edges))


def _faces_of(loop):
    return {f for e in loop.edges for f in e.link_faces}


def reduce_mesh(bm, obj, target_tris, s, log=None):
    """Remove loops ate tri_count(bm) <= target_tris. Devolve o numero de passadas."""
    allow_poles = False
    passes = 0
    while tri_count(bm) > target_tris:
        passes += 1
        c = _Ctx(bm, obj, s)
        loops = collect_loops(bm)
        by_key = {l.key: l for l in loops}
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
                    continue                    # sem par espelhado: fica, para manter a simetria
                if m is not l:
                    if m.cost == INF:
                        continue
                    group.append(m)
            for g in group:
                done.add(id(g))
            groups.append((sum(g.cost for g in group), group))
        groups.sort(key=lambda t: t[0])
        need = tri_count(bm) - target_tris
        used_v, used_f, batch, est = set(), set(), [], 0
        for cost, group in groups:
            vs = set().union(*(g.verts for g in group))
            fs = set().union(*(_faces_of(g) for g in group))
            if vs & used_v or fs & used_f:
                continue
            used_v |= vs
            used_f |= fs
            batch.extend(group)
            est += sum(2 * len(g.edges) for g in group)
            if est >= need:
                break
        if not batch:
            if s.pole_fallback and not allow_poles:
                allow_poles = True
                continue
            break
        edges = [e for l in batch for e in l.edges]
        cand = set()
        for l in batch:
            cand |= l.interior
            cand |= {v for v in l.ends if v.is_boundary}
        bmesh.ops.dissolve_edges(bm, edges=edges, use_verts=False, use_face_split=False)
        rem = [v for v in cand if v.is_valid and len(v.link_edges) == 2]
        if rem:
            bmesh.ops.dissolve_verts(bm, verts=rem, use_face_split=False, use_boundary_tear=False)
        if log:
            log(f"passada {passes}: {len(batch)} loops, {tri_count(bm)} tris")
        if passes > 400:
            break
    return passes


# ----------------------------------------------------------------------------
# Interface
# ----------------------------------------------------------------------------

class LOOPLOD_LodItem(PropertyGroup):
    ratio: FloatProperty(name="Ratio", default=0.5, min=0.01, max=1.0,
                         description="Fracao dos triangulos do original")


def _settings_from(p):
    return Settings(
        protect_group=p.protect_group, weight_aware=p.weight_aware,
        weight_influence=p.weight_influence, silhouette_pressure=p.silhouette_pressure,
        max_sparsity=p.max_sparsity, protect_seams=p.protect_seams,
        protect_sharp=p.protect_sharp, protect_boundary=p.protect_boundary,
        protect_materials=p.protect_materials, pole_fallback=p.pole_fallback,
        symmetry=p.symmetry, symmetry_tolerance_mm=p.symmetry_tolerance)


class LOOPLOD_Settings(PropertyGroup):
    protect_group: StringProperty(name="Deformation Loops", default="LOD_Protect",
        description="Grupo de vertices com os loops de deformacao. O loop fica no lugar; os loops que cruzam ele podem sair")
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
    symmetry: BoolProperty(name="X Symmetry", default=True)
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

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH' and context.mode == 'EDIT_MESH'

    def execute(self, context):
        ob = context.object
        p = context.scene.loop_lod
        g = ob.vertex_groups.get(p.protect_group) or ob.vertex_groups.new(name=p.protect_group)
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
        for r in (0.5, 0.25, 0.125):
            p.lods.add().ratio = r
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
    for i, it in enumerate(p.lods, start=1):
        me = base.copy()
        bm = bmesh.new()
        bm.from_mesh(me)
        target = max(1, int(round(src_tris * it.ratio)))
        reduce_mesh(bm, ob, target, s, log=log)
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
        r.operator("looplod.mark_protected", text="Mark Selected as Protected", icon='ADD').clear = False
        r.operator("looplod.mark_protected", text="", icon='REMOVE').clear = True
        b.prop(p, "weight_aware")
        sub = b.row(); sub.active = p.weight_aware; sub.prop(p, "weight_influence")
        b = lay.box()
        b.label(text="Silhouette", icon='MOD_OUTLINE')
        b.prop(p, "silhouette_pressure")
        b.prop(p, "max_sparsity")
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
        b.prop(p, "name_mode", text="")
        b.prop(p, "collection")
        b.prop(p, "use_evaluated")
        b.prop(p, "triangulate")
        lay.operator("looplod.generate", icon='PLAY')
        if ob and ob.type == 'MESH':
            tris = sum(len(f.vertices) - 2 for f in ob.data.polygons)
            lay.label(text=f"Active: {tris:,} tris", icon='INFO')


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
