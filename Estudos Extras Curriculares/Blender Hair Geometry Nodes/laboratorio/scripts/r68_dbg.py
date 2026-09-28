import sys; sys.path.insert(0,'.')
exec(open('r68_elsa.py').read().split('print("INFO"')[0])
import numpy as np
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
r = np.linalg.norm(P, axis=1)
first = np.array([c.first_point_index for c in d.curves]); n = np.array([c.points_length for c in d.curves])
# pontos na primeira terca de cada fio
idx = np.concatenate([np.arange(f, f+max(1,k//3)) for f,k in zip(first, n)])
print("DBG pontos", len(P), "dentro da cabeca (r<0.1):", round(float((r<0.1).mean())*100,1), "%  | no 1/3 inicial:", round(float((r[idx]<0.1).mean())*100,1), "%  r medio 1/3:", round(float(r[idx].mean()),4))
