import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("s")
for name, kw in (("GR Densidade Livre", {"Viewport": 1.0, "Fios por m2": 220000.0}), ("GR Mecha Estilizada", {}), ("GR Cacho por Mecha", {})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
profile(t, EG, radius=0.0008); set_mat(t, hair_mat("h", melanin=0.4, redness=0.9)); apply_tree(g, t.finish())
paths=[]; labs=[]
stage(res=420, samples=24, cam_loc=(0.20,-0.22,-0.12), target=(0.07,0,-0.14), lens=50)
for shp in ('RIBBONS','THICK','THICK_LINEAR'):
    bpy.context.scene.cycles_curves.shape = shp
    p = os.path.join(OUT, f"77_{shp}.png"); tt = render(p); paths.append(p); labs.append(f"{shp}: {tt} s"); print("SHAPE", shp, tt)
print(sheet(paths, labs, os.path.join(OUT,"77_shape_sheet.png"), cols=3, w=420))
