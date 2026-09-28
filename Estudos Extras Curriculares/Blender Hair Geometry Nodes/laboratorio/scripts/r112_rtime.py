import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("rt")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; t.chain(d)
m = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); t.chain(m, m.inputs[0].name, m.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5)); apply_tree(g, t.finish())
stage(res=540, samples=32, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
for dens in (50000.0, 150000.0, 450000.0, 1350000.0):
    d.inputs["Fios por m2"].default_value = dens; bpy.context.view_layer.update()
    n = stats(g).get('curves'); p = os.path.join(OUT, f"112_{int(dens)}.png"); tt = render(p)
    print("RT", int(dens), "fios", n, "render s", tt)
