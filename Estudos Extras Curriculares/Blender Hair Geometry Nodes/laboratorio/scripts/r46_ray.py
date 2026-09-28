import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
def sphere(bm, sc, c, seg=32):
    r = bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg//2, radius=1.0)
    vs = r['verts']; bmesh.ops.scale(bm, vec=sc, verts=vs); bmesh.ops.translate(bm, vec=c, verts=vs); return vs
me = bpy.data.meshes.new("shell"); bm = bmesh.new()
if V.startswith("afro"):
    sphere(bm, (0.19,0.19,0.17), (0,0.01,0.02))
elif V.startswith("nuvem"):
    vs = sphere(bm,(0.13,0.14,0.13),(0,0.02,0.04)) + sphere(bm,(0.09,0.09,0.09),(0.12,0.03,0.11)) + sphere(bm,(0.09,0.09,0.09),(-0.12,0.03,0.11))
    hull = bmesh.ops.convex_hull(bm, input=bm.verts[:])
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f not in set(hull['geom']) ] + [v for v in hull.get('geom_interior',[]) if isinstance(v, bmesh.types.BMVert)], context='FACES')
else:  # bob fechado embaixo? aberto: sem rosto e sem fundo
    sphere(bm, (0.145,0.15,0.13), (0,0.012,-0.03))
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < -0.13 or (f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.05)], context='FACES')
bm.to_mesh(me); bm.free(); shell = link(bpy.data.objects.new("shell", me)); shell.hide_render = True
t = Tree("ray")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = (600000.0 if ("gordo" in V or "medio" in V) else 250000.0); d.inputs["Viewport"].default_value = 1.0; t.chain(d)
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = shell
if V.startswith(("afro","nuvem")):
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 160; t.chain(rs, 'Curve', 'Curve')
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); na.inputs['Name'].default_value = 'n_raiz'
    rc = t.add('GeometryNodeRaycast'); t.link(oi.outputs['Geometry'], rc.inputs['Target Geometry']); t.link(cr.outputs['Root Position'], rc.inputs['Source Position']); t.link(na.outputs['Attribute'], rc.inputs['Ray Direction']); rc.inputs['Ray Length'].default_value = 1.0
    sp = t.add('GeometryNodeSplineParameter')
    k = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], k.inputs[0]); t.link(rc.outputs['Hit Distance'], k.inputs[1])
    sc_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(na.outputs['Attribute'], sc_.inputs[0]); t.link(k.outputs[0], sc_.inputs['Scale'])
    ad = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(cr.outputs['Root Position'], ad.inputs[0]); t.link(sc_.outputs[0], ad.inputs[1])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(ad.outputs[0], s.inputs['Position'])
    A = dict(gd=0.015, sh=0.25, cr=0.004, cf=45.0)
    if "gordo" in V: A = dict(gd=0.025, sh=0.1, cr=0.010, cf=20.0)
    if "medio" in V: A = dict(gd=0.02, sh=0.15, cr=0.007, cf=30.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=A['sh'], Tip_Spread=0.003, Preserve_Length=True, Guide_Distance=A['gd'], Existing_Guide_Map=False, Seed=1)
    if not V.endswith("_liso"):
        t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=A['cr'], Frequency=A['cf'], Existing_Guide_Map=True, Subdivision=0, Random_Offset=0.3)
else:
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    if V == "bob_corte":
        ps = t.add('GeometryNodeInputPosition'); nr = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(ps.outputs[0], nr.inputs[0])
        rc = t.add('GeometryNodeRaycast'); t.link(oi.outputs['Geometry'], rc.inputs['Target Geometry']); t.link(ps.outputs[0], rc.inputs['Source Position']); t.link(nr.outputs[0], rc.inputs['Ray Direction']); rc.inputs['Ray Length'].default_value = 1.0
        nt = t.add('FunctionNodeBooleanMath', props={'operation':'NOT'}); t.link(rc.outputs['Is Hit'], nt.inputs[0])
        dl = t.add('GeometryNodeDeleteGeometry', props={'domain':'POINT'}); t.chain(dl); t.link(nt.outputs[0], dl.inputs['Selection'])
profile(t, EG, radius=(0.0007 if ('gordo' in V or 'medio' in V) else 0.0005))
set_mat(t, hair_mat("c", melanin=0.75 if V.startswith(("afro","nuvem")) else 0.6, redness=0.4)); apply_tree(g, t.finish())
st = stats(g); print("INFO", V, st.get('curves'), st.get('points'))
shot(f"46_{V}", res=420, samples=16, cam_loc=(0.50,-0.66,0.10), target=(0,0,-0.02), lens=42)
