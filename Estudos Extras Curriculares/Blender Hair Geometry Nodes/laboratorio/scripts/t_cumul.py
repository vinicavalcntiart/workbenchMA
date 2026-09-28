import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
def tips(ob):
    dg = bpy.context.evaluated_depsgraph_get(); d = ob.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P = P.reshape(-1,3)
    off = np.array([c.first_point_index + c.points_length - 1 for c in d.curves]); return P[off], len(d.points)//len(d.curves)
NODE='Frizz Hair Curves'
res = []
for cuts in (0, 2, 6):
    for cum in (True, False):
        EG, head, scalp, g = base_scene(n_guides=120)
        t = Tree("c"); interp(t, EG, density=50000.0)
        if cuts: t.chain(t.add('GeometryNodeSubdivideCurve', Cuts=cuts), 'Curve', 'Curve')
        ng0 = None
        n = t.eg(EG[NODE], Factor=1.0, Distance=0.02, Shape=0.5, Cumulative_Offset=cum, Preserve_Length=False, Seed=6)
        m = apply_tree(g, t.finish())
        # referencia sem noise
        n.inputs['Factor'].default_value = 0.0; bpy.context.view_layer.update(); A, ppc = tips(g)
        n.inputs['Factor'].default_value = 1.0; g.data.update_tag(); bpy.context.view_layer.update(); B, _ = tips(g)
        dd = np.linalg.norm(B-A, axis=1)
        print(f"CUM pontos/fio={ppc:3d} cumulative={cum}  deslocamento da ponta: medio {dd.mean()*100:.1f} cm  max {dd.max()*100:.1f} cm")
