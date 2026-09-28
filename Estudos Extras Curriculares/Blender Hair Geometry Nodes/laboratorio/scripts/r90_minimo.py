import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
N = int(sys.argv[-1])
EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, spread=0.3, outward=0.35, n_guides=220)
t = Tree("min"); n_nodes = 0
interp(t, EG, density=250000.0); n_nodes += 2          # Interpolate + Value
if N >= 5:
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1); n_nodes += 1
if N >= 8:
    t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=0.008, Frequency=6.0, Existing_Guide_Map=True, Subdivision=2); n_nodes += 1
    t.eg(EG['Roll Hair Curves'], Factor=1.0, Subdivision=0, Roll_Length=0.05, Roll_Radius=0.015, Random_Orientation=0.0, Preserve_Length=True); n_nodes += 1
profile(t, EG, radius=0.0005); n_nodes += 1
set_mat(t, hair_mat("h", melanin=0.45, redness=0.7)); n_nodes += 1
m = apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ts=[]
for i in range(3):
    m.show_viewport=False; dg.update(); m.show_viewport=True; t0=time.time(); dg.update(); g.evaluated_get(dg).data.points; ts.append(time.time()-t0)
print("MIN", N, "nodes", n_nodes, "avaliacao ms", round(min(ts)*1000))
shot(f"90_{N}", res=380, samples=16, cam_loc=(0.42,-0.62,0.08), target=(0,0,-0.06), lens=46)
