import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
def shell_mesh(sc, c, cut_face=True, zcut=-1):
    me = bpy.data.meshes.new("shell"); bm = bmesh.new(); bm.loops.layers.uv.new("UVMap")
    r = bmesh.ops.create_uvsphere(bm, u_segments=(128 if 'borda' in sys.argv else 48), v_segments=(64 if 'borda' in sys.argv else 24), radius=1.0, calc_uvs=True)
    bmesh.ops.scale(bm, vec=sc, verts=bm.verts); bmesh.ops.translate(bm, vec=c, verts=bm.verts)
    if "borda" in sys.argv:
        # recorte do rosto por elipse no plano XZ, em malha densa (sem degrau)
        def dentro(c): return c.y < -0.02 and (c.x/0.11)**2 + ((c.z+0.035)/0.095)**2 < 1.0
        kill = [f for f in bm.faces if f.calc_center_median().z < zcut or (cut_face and dentro(f.calc_center_median()))]
    else:
        kill = [f for f in bm.faces if f.calc_center_median().z < zcut or (cut_face and f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.04)]
    bmesh.ops.delete(bm, geom=kill, context='FACES'); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    return link(bpy.data.objects.new("shell", me))
if V.startswith("afro"):
    g.hide_render = True; g.hide_viewport = True
    sh = shell_mesh((0.17,0.175,0.16), (0,0.015,0.02), zcut=-0.11)
    m = bpy.data.materials.new("massa"); b = m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value = (0.03,0.016,0.009,1); b.inputs['Roughness'].default_value = 0.9
    sh.data.materials.append(m)
    if "borda" in sys.argv:
        so = sh.modifiers.new("esp", 'SOLIDIFY'); so.thickness = 0.02; so.offset = -1.0
    cd = bpy.data.hair_curves.new("fur"); fur = link(bpy.data.objects.new("fur", cd)); cd.surface = sh; cd.surface_uv_map = "UVMap"
    t = Tree("afro")
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    L = 0.035 if V=="afro" else 0.02
    for k,v in {"Cabeça (colisão)": sh, "Comprimento": L, "Para fora": 1.0, "Para o lado da risca": 0.0, "Para trás": 0.0, "Gravidade": 0.0, "Guias por m2": 150000.0}.items(): x.inputs[k].default_value = v
    t.chain(x, 'Geometry', 'Guias')
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 40; t.chain(rs, 'Curve', 'Curve')
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.2, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=0.003, Frequency=45.0, Existing_Guide_Map=True, Subdivision=0, Random_Offset=0.3)
    profile(t, EG, radius=0.0006)
    set_mat(t, hair_mat("c", melanin=0.85, redness=0.4, roughness=0.4)); apply_tree(fur, t.finish())
    print("INFO", V, stats(fur).get('curves'), stats(fur).get('points'))
elif V.startswith("trolls"):
    sh = shell_mesh((0.16,0.16,0.35), (0,0.02,0.15), cut_face=False); sh.hide_render = True
    t = Tree("trolls")
    d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = 300000.0; d.inputs["Viewport"].default_value = 1.0; t.chain(d)
    oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = sh
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); na.inputs['Name'].default_value = 'n_raiz'
    up = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(na.outputs['Attribute'], up.inputs[0]); up.inputs[1].default_value = (0,0,1.5)
    nd = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(up.outputs[0], nd.inputs[0])
    rc = t.add('GeometryNodeRaycast'); t.link(oi.outputs['Geometry'], rc.inputs['Target Geometry']); t.link(cr.outputs['Root Position'], rc.inputs['Source Position']); t.link(nd.outputs[0], rc.inputs['Ray Direction']); rc.inputs['Ray Length'].default_value = 2.0
    sp = t.add('GeometryNodeSplineParameter')
    k = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], k.inputs[0]); t.link(rc.outputs['Hit Distance'], k.inputs[1])
    sc_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nd.outputs[0], sc_.inputs[0]); t.link(k.outputs[0], sc_.inputs['Scale'])
    ad = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(cr.outputs['Root Position'], ad.inputs[0]); t.link(sc_.outputs[0], ad.inputs[1])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(ad.outputs[0], s.inputs['Position'])
    t.eg(EG['Clump Hair Curves'], Factor=(0.45 if V=='trolls_macio' else 1.0), Shape=0.3, Tip_Spread=0.003, Preserve_Length=True, Guide_Distance=0.04, Existing_Guide_Map=False, Seed=1)
    if V.startswith("trolls"):
        t.eg(EG['Hair Curves Noise'], Factor=1.0, Distance=0.004, Shape=0.5, Scale=12.0, Scale_along_Curve=5.0, Offset_per_Curve=0.3, Cumulative_Offset=False, Preserve_Length=True, Seed=2)
    profile(t, EG, radius=0.0006, shape=0.1)
    set_mat(t, hair_mat("c", melanin=0.0, redness=0.0, roughness=0.5, tint=(0.95,0.22,0.55))); apply_tree(g, t.finish())
    print("INFO", V, stats(g).get('curves'), stats(g).get('points'))
shot(f"47_{V}{'_borda' if 'borda' in sys.argv else ''}", res=420, samples=16, cam_loc=(0.8,-1.1,0.35) if V.startswith("trolls") else (0.50,-0.66,0.10), target=(0,0,0.18) if V.startswith("trolls") else (0,0,-0.02), lens=38 if V.startswith("trolls") else 42)
