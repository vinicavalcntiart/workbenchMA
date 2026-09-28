import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
from mathutils import Matrix
V = sys.argv[-1]
S = {"redonda":(1,1,1), "ovo":(0.9,1.0,1.25), "larga":(1.25,1.1,0.88), "crianca":(0.7,0.7,0.7), "crianca_L":(0.7,0.7,0.7), "crianca_obj":(1,1,1)}[V]
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
M = Matrix.Diagonal((*S,1)); head.data.transform(M); scalp.data.transform(M); head.data.update(); scalp.data.update()
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("grm")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
L = 0.22*(0.7 if V=="crianca_L" else 1.0)
for k,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": 0.4, "Para o lado da risca": 0.35, "Para trás": 0.2, "Gravidade": 1.2, "Guias por m2": 4000.0}.items(): x.inputs[k].default_value = v
t.chain(x, 'Geometry', 'Guias')
for n in ("GR Densidade Livre","GR Mecha Estilizada","GR Onda S","GR Cor por Mecha"):
    nd = t.add('GeometryNodeGroup', group=GR[n]); t.chain(nd, nd.inputs[0].name, nd.outputs[0].name)
    if n=="GR Densidade Livre": nd.inputs["Viewport"].default_value = 1.0
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("h", melanin=0.5, redness=0.6)); apply_tree(g, t.finish())
if V=="crianca_obj":
    for o in (head, scalp, g): o.scale = (0.7,0.7,0.7)
    bpy.context.view_layer.update()
print("INFO", V, stats(g).get('curves'))
shot(f"51_{V}", res=420, samples=16, cam_loc=(0.50,-0.72,0.10), target=(0,0,-0.03), lens=45)
