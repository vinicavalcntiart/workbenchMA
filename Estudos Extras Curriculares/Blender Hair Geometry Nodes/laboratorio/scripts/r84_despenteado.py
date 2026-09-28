import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # 0 | 1 | 2 | 3
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("dp")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.13, "Para fora": 0.7, "Para o lado da risca": 0.3, "Para trás": 0.3, "Gravidade": 0.8})
lv = int(V)
if lv >= 1:   # bagunca nas GUIAS: gira cada guia em volta da propria raiz (poucos pontos, barato)
    t.eg(EG['Rotate Hair Curves'], Factor=1.0, Angle=0.0, Random_Offset=0.5*lv, Seed=3)
if lv >= 2:
    t.eg(EG['Hair Curves Noise'], Factor=1.0, Distance=0.01*lv, Shape=0.5, Scale=6.0, Scale_along_Curve=3.0, Offset_per_Curve=1.0, Cumulative_Offset=False, Preserve_Length=True, Seed=4)
w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
for q in w.inputs:
    if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 250000.0})
grp("GR Mecha Estilizada")
if lv >= 3: grp("GR Strays em Arco", **{"Fração": 0.06})
grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5, redness=0.8)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"84_{V}", res=400, samples=16, cam_loc=(0.40,-0.58,0.14), target=(0,0,0.0), lens=46)
