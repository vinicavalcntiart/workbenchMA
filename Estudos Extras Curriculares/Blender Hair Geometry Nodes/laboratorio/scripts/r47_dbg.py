import sys; sys.argv=['x','trolls']
exec(open('r47_styl.py').read().split("shot(f\"47_")[0])
import numpy as np
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
R = P[[c.first_point_index for c in d.curves]]; T = P[[c.first_point_index+c.points_length-1 for c in d.curves]]
down = T[:,2] < R[:,2]; L = np.linalg.norm(T-R,axis=1)
print("DBG curvas", len(R), "descem", int(down.sum()), "raiz z media das que descem", float(R[down,2].mean()) if down.any() else None, "comp medio", float(L.mean()), "zero", int((L<0.001).sum()))
