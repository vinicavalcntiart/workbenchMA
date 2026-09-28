"""Cilios em camadas: palpebra = tubo em volta do olho; scalp = quadrante da margem do tubo.
A normal do tubo varia em dois eixos (ao longo da margem e na espessura), entao as raizes
formam fileiras em profundidade em vez de uma linha. Variante via argv: a b c d e."""
import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(os.path.dirname(LAB), "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); skin = skin_mat(); head.data.materials.append(skin); scalp.hide_render = True
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1)
EC = (0.034,-0.088,0.012); ER = 0.016
V = sys.argv[-1]
PSI0, PSI1 = [float(x) for x in os.environ.get("PSI","-10,90").split(",")]
COL = os.environ.get("COL","none")
GRAV = os.environ.get("GRAV")
SIDE = os.environ.get("SIDE")
RG = os.environ.get("RG")   # "min,max": gravidade aleatoria por cilio
ROFF = float(os.environ.get("ROFF","0"))
DENS = os.environ.get("DENS")
BETA = math.radians(30)            # abertura: margem 30 graus acima do centro do olho, na frente
UP = Vector((0, math.sin(BETA), math.cos(BETA)))      # lado "palpebra" do plano
FW = Vector((0, -math.cos(BETA), math.sin(BETA)))     # direcao da margem no meio do arco

def mk(name, verts, faces, uvs=None, mat=None, hide=False):
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); me.update()
    if uvs:
        uv = me.uv_layers.new(name="UVMap")
        for p in me.polygons:
            for li in p.loop_indices: uv.data[li].uv = uvs[me.loops[li].vertex_index]
    for p in me.polygons: p.use_smooth = True
    if mat: me.materials.append(mat)
    o = link(bpy.data.objects.new(name, me)); o.hide_render = hide; return o

def tube(c0, psi0, psi1, r=0.0016, th=(0.04, 0.96), nt=64, nc=16, closed=False):
    """Centro da margem: grande circulo do olho no plano da palpebra, raio ER*1.02."""
    c0 = Vector(c0); X = Vector((1,0,0)); verts, uvs = [], []
    for i in range(nt+1):
        t = math.pi*(th[0] + (th[1]-th[0])*i/nt)
        d = (X*math.cos(t) + FW*math.sin(t)).normalized()
        T = (-X*math.sin(t) + FW*math.cos(t)).normalized()
        n2 = T.cross(d)
        if n2.dot(-UP) < 0: n2 = -n2            # n2 aponta para a abertura do olho
        for j in range(nc + (0 if closed else 1)):
            s = psi0 + (psi1-psi0)*j/nc
            verts.append(c0 + d*ER*1.02 + r*(d*math.cos(s) + n2*math.sin(s))); uvs.append((i/nt, j/nc))
    m = nc if closed else nc+1; faces = []
    for i in range(nt):
        for j in range(nc):
            a, b = i*m + j, i*m + (j+1) % m
            faces.append((a, a+m, b+m, b))   # normal para fora do tubo
    return verts, faces, uvs

eyes, lids = [], []
for sx in (-1, 1):
    c = (sx*EC[0], EC[1], EC[2])
    bpy.ops.mesh.primitive_uv_sphere_add(radius=ER, location=c, segments=48, ring_count=24); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth(); eyes.append(e)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.012)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
    if V != "a":
        # casca da palpebra: esfera 1.02 acima do plano + tubo da margem (visiveis, pele)
        bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=32, radius=ER*1.02)
        bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().dot(UP) < 0.0], context='FACES')
        me = bpy.data.meshes.new("shell"); bm.to_mesh(me); bm.free()
        for pp in me.polygons: pp.use_smooth = True
        me.materials.append(skin); sh = link(bpy.data.objects.new("shell", me)); sh.location = c
        v_, f_, u_ = tube(c, 0, 2*math.pi, closed=True); mk("lidrim", v_, f_, mat=skin)
        # scalp dos cilios: quadrante externo-frontal da margem (psi -35 a 65 graus)
        v_, f_, u_ = tube(c, math.radians(PSI0), math.radians(PSI1), nc=8)
        lids.append(mk(f"lashscalp{sx}", v_, f_, uvs=u_, hide=True))
bpy.context.view_layer.update()

def lid_old(e):   # referencia: faixa da esfera do olho (17.36)
    me = e.data.copy(); bm=bmesh.new(); bm.from_mesh(me)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (0.001 < f.calc_center_median().z < 0.006 and f.calc_center_median().y < -0.009)], context='FACES')
    bm.to_mesh(me); bm.free(); o = link(bpy.data.objects.new("lidold", me)); o.location=e.location; o.scale=(1.06,)*3; o.hide_render=True
    bpy.context.view_layer.update(); return o

def groom(surf, name, sx, L, grav, dens, rad, shp, corner=None, clump=None, ctip=0.0, cshape=0.3):
    cd = bpy.data.hair_curves.new(name); g = link(bpy.data.objects.new(name, cd)); cd.surface = surf; cd.surface_uv_map = "UVMap"
    t = Tree(name)
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": (head if COL=="head" else None), "Comprimento": L, "Para fora": 1.0, "Para o lado da risca": 0.0, "Para trás": 0.0, "Gravidade": (float(GRAV) if GRAV else grav), "Guias por m2": (float(DENS) if DENS else dens)}.items(): x.inputs[kk].default_value = v
    t.chain(x, 'Geometry', 'Guias')
    if RG:   # gravidade por cilio: Index -> Evaluate on Domain (Curve) -> Random Value -> Gravidade
        lo, hi = [float(v) for v in RG.split(",")]
        ix = t.add('GeometryNodeInputIndex'); ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'INT'})
        t.link(ix.outputs[0], ev.inputs[0])
        rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'})
        mn = [i for i in rv.inputs if i.name=='Min' and i.type=='VALUE'][0]; mx_ = [i for i in rv.inputs if i.name=='Max' and i.type=='VALUE'][0]
        mn.default_value, mx_.default_value = lo, hi; rv.inputs['Seed'].default_value = 7
        t.link(ev.outputs[0], rv.inputs['ID'])
        t.link([o for o in rv.outputs if o.type=='VALUE'][0], x.inputs['Gravidade'])
    if corner:   # canto externo mais longo: Trim por X da raiz (interno->externo)
        rt = t.add('GeometryNodeGroup', group=EG['Curve Root']); sp = t.add('ShaderNodeSeparateXYZ'); t.link(rt.outputs['Root Position'], sp.inputs[0])
        mr = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); mr.clamp = True
        t.link(sp.outputs['X'], mr.inputs['Value'])
        mr.inputs['From Min'].default_value = sx*(EC[0]-ER); mr.inputs['From Max'].default_value = sx*(EC[0]+ER)
        mr.inputs['To Min'].default_value = corner; mr.inputs['To Max'].default_value = 1.0
        tr = t.eg(EG['Trim Hair Curves'], Scale_Uniform=False, Replace_Length=False, Random_Offset=ROFF)
        t.link(mr.outputs['Result'], tr.inputs['Length Factor'])
    if clump:
        t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=cshape, Tip_Spread=ctip, Preserve_Length=True, Guide_Distance=clump, Existing_Guide_Map=False, Seed=3)
    t.eg(EG['Set Hair Curve Profile'], Radius=rad, Shape=shp, Factor_Min=0.0, Factor_Max=1.0)
    set_mat(t, hair_mat("lash", melanin=1.0, redness=0.2, roughness=0.3)); apply_tree(g, t.finish())
    st = stats(g); print("INFO", V, name, st.get('curves'), st.get('points'), st.get('err',''))
    if name=="c1":
        ev_=g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data; import statistics as S_
        zs=[ev_.points[i].position.z for i in range(len(ev_.points)) if i%12==11]; print("TIPZ_SD_mm", round(S_.pstdev(zs)*1000,2))
    for md in g.modifiers:
        pass
    return g

for i, sx in enumerate((-1, 1)):
    if V == "a": groom(lid_old(eyes[i]), f"c{i}", sx, 0.009, -1.3, 250000.0, 0.0005, 0.8)
    if V == "b": groom(lids[i], f"c{i}", sx, 0.009, -1.3, 1200000.0, 0.0003, 0.8)
    if V in "ce": groom(lids[i], f"c{i}", sx, 0.012, -1.6, 2000000.0, 0.0003, 0.8, corner=0.5, clump=0.0018, ctip=0.0002)
    if V == "d": groom(lids[i], f"c{i}", sx, 0.013, -1.8, 1500000.0, 0.0005, 0.9, corner=0.45, clump=0.003, ctip=0.0, cshape=0.5)
if V == "e" or SIDE: shot("115_cilio_e"+os.environ.get("TAG",""), res=560, samples=24, cam_loc=(0.26,-0.20,0.02), target=(0.034,-0.10,0.016), lens=100)
elif False: shot("115_cilio_e", res=560, samples=24, cam_loc=(0.26,-0.20,0.02), target=(0.034,-0.10,0.016), lens=100)
else: shot(f"115_cilio_{V}"+os.environ.get("TAG",""), res=560, samples=24, cam_loc=(0.10,-0.34,0.03), target=(0.02,-0.09,0.012), lens=85)
