import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
SUB = int(sys.argv[-1])
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.2, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("r")
for name, kw in (("GR Densidade Livre", {"Fios por m2": 250000.0, "Viewport": 1.0}), ("GR Mecha Estilizada", {}), ("GR Ponta Virada", {"Subdivisão": SUB, "Para fora": True})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5, redness=0.6)); apply_tree(g, t.finish())
print("INFO", SUB, stats(g).get('points'))
shot(f"61_roll_sub{SUB}", res=420, samples=16, cam_loc=(0.55,-0.45,-0.05), target=(0,0,-0.12), lens=55)
