import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
res = []
for lf, su in ((1.0,False),(0.5,False),(1.5,False),(1.5,True),(2.0,False)):
    EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, n_guides=120)
    t = Tree("t"); tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=lf, Scale_Uniform=su); apply_tree(g, t.finish())
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    L = [np.linalg.norm(np.diff(P[c.first_point_index:c.first_point_index+c.points_length],axis=0),axis=1).sum() for c in d.curves]
    res.append((lf, su, round(float(np.mean(L))*100,1)))
for r in res: print("TRIM LF", r[0], "Scale Uniform", r[1], "comprimento medio cm", r[2])
