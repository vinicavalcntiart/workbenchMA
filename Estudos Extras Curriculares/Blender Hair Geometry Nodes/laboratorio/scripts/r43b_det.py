import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
G = np.zeros(len(g.data.points)*3, np.float32); g.data.attributes['position'].data.foreach_get('vector', G)
sv = np.zeros(len(scalp.data.vertices)*3, np.float32); scalp.data.vertices.foreach_get('co', sv)
t = Tree("d"); interp(t, EG, density=250000.0); m = apply_tree(g, t.finish())
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P)
print("DET guides", round(float(G.sum()),5), "scalp", len(scalp.data.vertices), round(float(sv.sum()),5), "interp", len(d.curves), round(float(P.sum()),4))
