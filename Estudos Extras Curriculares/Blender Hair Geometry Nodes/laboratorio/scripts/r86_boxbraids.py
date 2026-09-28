import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("scalp"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.03,0.015,0.01,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("bb")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
gd = {"poucas": 1500.0, "muitas": 3000.0}[V]
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.34, "Para fora": 0.5, "Para o lado da risca": 0.35, "Para trás": 0.3, "Gravidade": 2.0, "Guias por m2": gd})
dl = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 400000.0, "Guias por fio": 1})
grp("GR Trança Grossa", **{"Raio": 0.004, "Cruzamentos": 6.0, "Começa em": 0.03, "Espessura na ponta": 0.8, "Cabeça (colisão)": head, "Tamanho da trança": 0.015})
profile(t, EG, radius=0.00035)
set_mat(t, hair_mat("h", melanin=0.95, redness=0.3, roughness=0.35)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'), stats(g).get('points'))
shot(f"86_{V}", res=440, samples=20, cam_loc=(0.45,-0.62,0.02), target=(0,0,-0.10), lens=40)
