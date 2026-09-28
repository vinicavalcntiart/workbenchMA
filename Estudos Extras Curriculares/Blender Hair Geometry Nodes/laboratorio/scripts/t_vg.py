import sys; sys.path.insert(0,'.')
exec(open('r20_regions.py').read().split("EG0=None")[0])
import numpy as np
for mode in ("none","undercut"):
    EG, head, scalp, g = base_scene(**dict(G))
    t = Tree("x"); build(t, EG, g=g, scalp=scalp, mode=mode); apply_tree(g, t.finish())
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    names = [a.name for a in d.attributes]
    a = d.attributes.get("topo")
    info = f"topo: dominio {a.domain} tipo {a.data_type}" if a else "topo AUSENTE"
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    L=[]
    for c in d.curves:
        s=c.first_point_index; e=s+c.points_length; L.append(np.linalg.norm(np.diff(P[s:e],axis=0),axis=1).sum())
    L=np.array(L)
    print(f"VG {mode}: {info}; fios {len(L)}; < 4 cm: {(L<0.04).sum()}  mediana {np.median(L)*100:.1f} cm")
