import sys; sys.path.insert(0,'.')
exec(open('r22b_roll.py').read().split("run_variants(")[0])
import numpy as np
def tips(g):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    idx = np.array([c.first_point_index+c.points_length-1 for c in d.curves]); T=P[idx]
    rad = np.linalg.norm(T[:,:2],axis=1)   # distancia horizontal do eixo da cabeca
    return rad.mean()*100, T[:,2].mean()*100
res={}
for lb, kw in [("sem roll", None), ("radial +", dict(sign=1.0, radial=True)), ("radial -", dict(sign=-1.0, radial=True))]:
    EG, head, scalp, g = base_scene(**dict(G))
    t = Tree("r")
    if kw is None:
        interp(t, EG, density=100000.0)
        t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
        t.chain(t.add('GeometryNodeSubdivideCurve', Cuts=3), 'Curve', 'Curve')
    else:
        build(t, EG, **kw)
    apply_tree(g, t.finish()); r, z = tips(g); print(f"ROLL {lb:8s}: ponta a {r:.1f} cm do eixo vertical, altura media {z:.1f} cm")
