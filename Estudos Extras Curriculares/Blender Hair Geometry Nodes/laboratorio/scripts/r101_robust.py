import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
from mathutils import Matrix
import math
V = sys.argv[-1]   # base | deslocada | girada
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("rb")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head})
grp("GR Densidade Livre", **{"Viewport": 1.0})
grp("GR Mecha Estilizada"); grp("GR Volume na Raiz"); grp("GR Ponta Virada", **{"Para fora": True, "Subdivisão": 0}); grp("GR Onda S"); grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.4, redness=0.8)); apply_tree(g, t.finish())
# move o conjunto (objetos, nao a malha): cabeca, scalp e cabelo juntos
if V != "base":
    root = link(bpy.data.objects.new("rig", None))
    for o in (head, scalp, g): o.parent = root
    if V == "deslocada": root.location = (0.6, 0.3, 1.5)
    if V == "girada": root.rotation_euler = (math.radians(25), 0, math.radians(60))
    bpy.context.view_layer.update()
import numpy as np
dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
print("ROB", V, "fios", len(d.curves), "pos local soma", round(float(P.sum()),2))
tgt = head.matrix_world.translation
cam_loc = tgt + head.matrix_world.to_3x3() @ Vector((0.42,-0.62,0.06))
shot(f"101_{V}", res=360, samples=12, cam_loc=tuple(cam_loc), target=tuple(tgt + head.matrix_world.to_3x3() @ Vector((0,0,-0.06))), lens=46)
