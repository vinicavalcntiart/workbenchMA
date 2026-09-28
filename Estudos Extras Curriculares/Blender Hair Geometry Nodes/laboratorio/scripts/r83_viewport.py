import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
from PIL import Image
VA = float(sys.argv[-1])
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = ["GR Densidade Livre"]
t = Tree("v"); d = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Densidade Livre"]); d.inputs["Viewport"].default_value = VA; d.inputs["Fios por m2"].default_value = 60000.0; t.chain(d)
profile(t, EG, radius=0.0004); set_mat(t, hair_mat("h", melanin=0.9)); apply_tree(g, t.finish())
head.hide_render = True
print("VP viewport eval fios", stats(g).get('curves'))
stage(res=300, samples=4, bg=1.0); sc = bpy.context.scene; sc.cycles.use_denoising = False
p = os.path.join(OUT, f"83_{VA}.png"); render(p)
a = np.asarray(Image.open(p).convert('L')).astype(float)/255
print("VP", VA, "cobertura de cabelo no render %.1f%%" % ((a < 0.6).mean()*100))
