import sys; sys.path.insert(0,'.')
from lab import *
V = [dict(spread=0.35, gravity=2.6, outward=0.25, length=0.22),
     dict(spread=0.25, gravity=4.0, outward=0.3, length=0.28),
     dict(spread=0.45, gravity=2.0, outward=0.45, length=0.18)]
paths=[]
for i,kw in enumerate(V):
    EG, head, scalp, g = base_scene(**kw)
    t = Tree("base"); interp(t, EG, density=300000.0); profile(t, EG, radius=0.0003)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4)); apply_tree(g, t.finish())
    paths.append(shot(f"01_guias_{i}", res=512, samples=16))
print(sheet(paths, [str(v) for v in V], os.path.join(OUT,"01_guias_sheet.png"), cols=3))
