import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.3, n_guides=100)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = ["GR Balanço"]
t = Tree("b"); rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs,'Curve','Curve')
n = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Balanço"]); t.chain(n); apply_tree(g, t.finish())
sc = bpy.context.scene; sc.render.fps = 24; xs=[]
for f in (1,7,13,19):
    sc.frame_set(f); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    T = P[[c.first_point_index+c.points_length-1 for c in d.curves]]; xs.append(round(float(T[:,0].mean())*100,1))
print("INFO ponta x media cm nos quadros 1,7,13,19:", xs)
