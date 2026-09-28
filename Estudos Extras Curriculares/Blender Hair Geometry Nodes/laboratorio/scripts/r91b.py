import sys; sys.path.insert(0,'.')
exec(open('r91_raposa.py').read().split('print("INFO"')[0])
import numpy as np
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
for nm in ('branco','orelha'):
    a = np.zeros(len(d.curves), np.float32); d.attributes[nm].data.foreach_get('value', a); print("ATT", nm, "fios > 0,5:", int((a>0.5).sum()), "de", len(a))
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
R = P[[c.first_point_index for c in d.curves]]
print("ATT raiz z min/max", round(float(R[:,2].min()),3), round(float(R[:,2].max()),3), "|x| max", round(float(np.abs(R[:,0]).max()),3))
