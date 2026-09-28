import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import numpy as np
V = sys.argv[-1]   # sem | guias | fim
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.40, gravity=5.0, spread=0.35, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
# tronco: elipsoide largo abaixo da cabeca + pescoco
bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0,0.01,-0.30), segments=48, ring_count=24); torso = bpy.context.object; torso.scale = (0.22,0.12,0.16); bpy.ops.object.transform_apply(scale=True); bpy.ops.object.shade_smooth()
bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.16, location=(0,0.01,-0.13)); neck = bpy.context.object
bpy.ops.object.select_all(action='DESELECT'); torso.select_set(True); neck.select_set(True); bpy.context.view_layer.objects.active = torso; bpy.ops.object.join(); body = torso
body.data.materials.append(skin_mat())
def shrink(t_, obj):
    w = t_.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves']); w.inputs['Offset Distance'].default_value = 0.004; w.inputs['Above Surface'].default_value = 0.0; w.inputs['Smoothing Steps'].default_value = 3; w.inputs['Lock Roots'].default_value = True
    for q in w.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = obj
    return t_.chain(w)
t = Tree("om")
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
if V == "guias": shrink(t, body)
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 220000.0; t.chain(d)
m = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); t.chain(m, m.inputs[0].name, m.outputs[0].name)
if V in ("guias", "fim"): shrink(t, body)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.8, redness=0.4)); apply_tree(g, t.finish())
dd = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(dd.points)*3, np.float32); dd.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
q = (P - np.array([0,0.01,-0.30])) / np.array([0.22,0.12,0.16]); inside = (np.linalg.norm(q,axis=1) < 0.995).mean()
print("INFO", V, "pontos dentro do tronco %.2f%%" % (inside*100))
shot(f"75_{V}", res=440, samples=16, cam_loc=(0.55,-0.75,0.05), target=(0,0,-0.15), lens=38)
