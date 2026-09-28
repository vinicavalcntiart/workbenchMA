import sys; sys.path.insert(0,'.')
exec(open('r24b_proc.py').read().split("run_variants(")[0])
import numpy as np
def meas(g):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    mid = np.array([c.first_point_index + c.points_length//3 for c in d.curves])
    tip = np.array([c.first_point_index + c.points_length-1 for c in d.curves])
    root = np.array([c.first_point_index for c in d.curves])
    return np.linalg.norm(P[mid],axis=1).mean()*100, np.linalg.norm(P[tip][:,:2],axis=1).mean()*100, np.linalg.norm(P[root],axis=1).mean()*100
for lb, kw in [("base",{}),("volume -0.5 1.5cm",dict(lift=0.015)),("volume 3cm r0.15",dict(lift=0.03, lift_ramp=0.15))]:
    EG, head, scalp, g = base_scene(**dict(G)); t = Tree("x"); build(t, EG, g=g, scalp=scalp, **kw); apply_tree(g, t.finish())
    m, tp, rt = meas(g); print(f"PROC {lb:20s} raiz {rt:.2f} cm do centro | 1/3 do fio {m:.2f} cm | ponta {tp:.2f} cm do eixo")
