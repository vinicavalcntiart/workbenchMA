import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
dens = float(sys.argv[-2]); pint = sys.argv[-1]=="1"
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
if pint:
    scalp.hide_render = False
    m = bpy.data.materials.new("scalp_raiz"); nt = m.node_tree; b = nt.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (0.06,0.028,0.014,1); b.inputs['Roughness'].default_value = 0.6
    scalp.data.materials.append(m)
t = Tree("s"); interp(t, EG, density=dens)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("c", melanin=0.6, redness=0.5)); apply_tree(g, t.finish())
print("INFO", dens, pint, stats(g).get('curves'))
shot(f"48_{int(dens)}_{int(pint)}", res=420, samples=24, cam_loc=(0.25,-0.35,0.55), target=(0,0,0.03), lens=45)
