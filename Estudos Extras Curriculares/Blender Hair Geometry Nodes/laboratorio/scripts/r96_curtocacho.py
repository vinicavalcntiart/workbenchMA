import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # vpm baixo | alto
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.03,0.015,0.01,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("cc")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.07, "Para fora": 0.8, "Para o lado da risca": 0.2, "Para trás": 0.2, "Gravidade": 0.3})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 450000.0})
grp("GR Mecha Estilizada", **{"Tamanho da mecha": (0.018 if V=="raio" else 0.01)})
vpm = {"baixo": (20.0, 36.0), "medio": (45.0, 60.0), "alto": (70.0, 90.0), "raio": (14.0, 20.0)}[V]
grp("GR Cacho por Mecha", **{"Voltas por metro mín": vpm[0], "Voltas por metro máx": vpm[1], "Raio mín": (0.009 if V=="raio" else 0.004), "Raio máx": (0.012 if V=="raio" else 0.006), "Começa em": 0.1})
grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.95, redness=0.3)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'), stats(g).get('points'))
shot(f"96_{V}", res=420, samples=20, cam_loc=(0.42,-0.55,0.12), target=(0,0,0.0), lens=46)
