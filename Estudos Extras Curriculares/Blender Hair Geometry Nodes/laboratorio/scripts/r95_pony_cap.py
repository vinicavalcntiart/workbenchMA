import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
CAP = sys.argv[-1] == "cap"
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(nape=(-0.7 if CAP else None)); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.12,0.06,0.03,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("p")
def grp(name, out=None, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, out or n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 300000.0})
grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Abertura": 0.02})
grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.012}); grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, MAT["GR Cabelo Cor por Mecha"]); apply_tree(g, t.finish())
print("INFO", CAP, stats(g).get('curves'))
shot(f"95_pony_{'cap' if CAP else 'teste'}", res=440, samples=20, cam_loc=(0.45,0.55,-0.02), target=(0,0.02,-0.05), lens=42)
