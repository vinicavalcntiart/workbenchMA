import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
import numpy as np
from mathutils.bvhtree import BVHTree
V = sys.argv[-1]   # sem | inicio | fim
EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
attach_uv(g, scalp)
def add_key(o):
    o.shape_key_add(name="Basis"); k = o.shape_key_add(name="torto")
    for v in k.data:
        z = (v.co.z + 0.1)/0.2
        v.co.x += 0.05*z*z; v.co.z += 0.02*z
    return k
ks = add_key(scalp); kh = add_key(head); scalp.add_rest_position_attribute = True
t = Tree("d")
if V == "inicio": t.chain(t.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
interp(t, EG, density=150000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
if V == "fim": t.chain(t.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
w1 = t.add('ShaderNodeTexWave'); w1.inputs['Scale'].default_value = 8.0; t.link(cr.outputs['Root Position'], w1.inputs['Vector'])
e1 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(w1.outputs['Fac'], e1.inputs[0])
s1 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s1.inputs['Name'].default_value='pad_pos'; t.chain(s1); t.link(e1.outputs[0], s1.inputs['Value'])
uvn = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); uvn.inputs['Name'].default_value='surface_uv_coordinate'
w2 = t.add('ShaderNodeTexWave'); w2.inputs['Scale'].default_value = 8.0; t.link(uvn.outputs['Attribute'], w2.inputs['Vector'])
e2 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(w2.outputs['Fac'], e2.inputs[0])
s2 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s2.inputs['Name'].default_value='pad_uv'; t.chain(s2); t.link(e2.outputs[0], s2.inputs['Value'])
if V == "fim_depois": t.chain(t.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
profile(t, EG, radius=0.0005)
m = bpy.data.materials.new("p"); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial'); h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization='MELANIN'
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='pad_pos'; mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['From Min'].default_value=0.45; mr.inputs['From Max'].default_value=0.55; mr.inputs['To Min'].default_value=0.1; mr.inputs['To Max'].default_value=0.95; mr.clamp=True
nt.links.new(a.outputs['Fac'], mr.inputs['Value']); nt.links.new(mr.outputs['Result'], h.inputs['Melanin']); nt.links.new(h.outputs[0], o.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
def read():
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    R = P[[c.first_point_index for c in d.curves]]
    pp = np.zeros(len(d.curves), np.float32); d.attributes['pad_pos'].data.foreach_get('value', pp)
    pu = np.zeros(len(d.curves), np.float32); d.attributes['pad_uv'].data.foreach_get('value', pu)
    se = scalp.evaluated_get(dg); me = se.to_mesh(); bvh = BVHTree.FromPolygons([v.co.copy() for v in me.vertices], [p.vertices[:] for p in me.polygons]); se.to_mesh_clear()
    dist = np.array([ (Vector(r) - bvh.find_nearest(Vector(r))[0]).length for r in R[::10]])
    return len(d.curves), R, pp>0.5, pu>0.5, dist
ks.value = kh.value = 0.0; n0,R0,p0,u0,d0 = read()
ks.value = kh.value = 1.0; bpy.context.view_layer.update(); n1,R1,p1,u1,d1 = read()
same = n0==n1
print("INFO", V, "fios", n0, n1, "raiz ate scalp deformado: media mm", round(float(d1.mean()*1000),2), "max mm", round(float(d1.max()*1000),1),
      "| padrao por posicao troca", (f"{(p0!=p1).mean()*100:.1f}%" if same else "n/a"), "| por UV troca", (f"{(u0!=u1).mean()*100:.1f}%" if same else "n/a"))
shot(f"52_{V}", res=420, samples=16, cam_loc=(0.50,-0.66,0.10), target=(0.02,0,-0.02), lens=45)
