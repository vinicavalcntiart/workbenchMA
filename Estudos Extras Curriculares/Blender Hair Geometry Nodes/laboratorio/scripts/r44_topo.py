import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np, bmesh
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
t = Tree("d"); interp(t, EG, density=250000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
m = apply_tree(g, t.finish())
def snap():
    bpy.context.view_layer.update(); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    R = P[[c.first_point_index for c in d.curves]]; T = P[[c.first_point_index+c.points_length-1 for c in d.curves]]
    return len(d.curves), R, T
def cmp(tag, a, b):
    from mathutils.kdtree import KDTree
    def q(X,Y):
        k=KDTree(len(X))
        for i,p in enumerate(X): k.insert(p.tolist(), i)
        k.balance(); return np.array([k.find(p.tolist())[2] for p in Y])
    dd = q(a[1],b[1]); dt = q(a[2],b[2])
    print("TOPO", tag, a[0], "->", b[0], "raiz desloc. media mm", round(dd.mean()*1000,2), "ponta mm", round(dt.mean()*1000,2))
A = snap()
# 1) mesma malha, ordem das faces embaralhada
bm = bmesh.new(); bm.from_mesh(scalp.data); import random; rr = random.Random(5)
bm.faces.ensure_lookup_table(); idx = list(range(len(bm.faces))); rr.shuffle(idx)
for i,f in enumerate(bm.faces): f.index = idx[i]
bm.faces.sort(); bm.to_mesh(scalp.data); bm.free(); scalp.data.update()
B = snap(); cmp("faces embaralhadas", A, B)
# 2) Triangulate (forma identica)
bm = bmesh.new(); bm.from_mesh(scalp.data); bmesh.ops.triangulate(bm, faces=bm.faces[:]); bm.to_mesh(scalp.data); bm.free(); scalp.data.update()
C = snap(); cmp("triangulado", A, C)
cmp("embaralhado vs triangulado", B, C); cmp("controle A vs A", A, snap())
