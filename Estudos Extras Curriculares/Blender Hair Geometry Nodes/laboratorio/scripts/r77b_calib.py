import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import numpy as np
from PIL import Image
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
t = Tree("c"); interp(t, EG, density=220000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
profile(t, EG, radius=0.0005); mat = hair_mat("h", melanin=0.4, redness=0.6); set_mat(t, mat); apply_tree(g, t.finish())
h = [n for n in mat.node_tree.nodes if n.bl_idname=='ShaderNodeBsdfHairPrincipled'][0]
head.hide_render = True
stage(res=200, samples=16, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
def lum(shape, mel):
    bpy.context.scene.cycles_curves.shape = shape; h.inputs['Melanin'].default_value = mel
    p = os.path.join(OUT, "77c.png"); render(p)
    a = np.asarray(Image.open(p).convert('RGB')).astype(float)/255; m = np.abs(a-np.array([0.30,0.30,0.32])).sum(2)>0.08
    return float((a[m]@np.array([0.2126,0.7152,0.0722])).mean())
R = {m: lum('RIBBONS', m) for m in (0.2,0.4,0.6,0.8)}
Tm = [round(x,2) for x in np.linspace(0.02,0.8,14)]; T = {m: lum('THICK', m) for m in Tm}
for m, l in R.items():
    best = min(Tm, key=lambda k: abs(T[k]-l)); print(f"CAL ribbons mel {m}: lum {l:.3f} -> 3D Curves mel {best} (lum {T[best]:.3f})")
