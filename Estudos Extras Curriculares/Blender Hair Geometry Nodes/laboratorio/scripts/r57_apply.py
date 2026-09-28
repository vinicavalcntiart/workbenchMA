import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("guias"); g = link(bpy.data.objects.new("guias", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("gen"); x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for k,v in {"Cabeça (colisão)": head, "Comprimento": 0.22, "Para fora": 0.4, "Para o lado da risca": 0.35, "Para trás": 0.3, "Gravidade": 1.2, "Guias por m2": 4000.0}.items(): x.inputs[k].default_value = v
t.chain(x, 'Geometry', 'Guias'); m = apply_tree(g, t.finish())
bpy.context.view_layer.objects.active = g; g.select_set(True)
r = bpy.ops.object.modifier_apply(modifier=m.name)
d = g.data
print("APPLY", r, "curvas", len(d.curves), "pontos", len(d.points), "attrs", sorted(a.name for a in d.attributes if not a.name.startswith('.')), "surface", d.surface.name if d.surface else None)
# "esculpe": puxa as guias do lado direito para cima-fora (simula um ajuste manual)
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P = P.reshape(-1,3)
for c in d.curves:
    i0 = c.first_point_index; n = c.points_length
    if P[i0,0] > 0.03:
        for j in range(1, n): P[i0+j] += np.array([0.03, 0.0, 0.02]) * (j/(n-1))**1.5
d.attributes['position'].data.foreach_set('vector', P.ravel()); d.update_tag()
# cadeia de groom nas guias editadas
t2 = Tree("groom")
for n in ("GR Densidade Livre","GR Mecha Estilizada","GR Cor por Mecha"):
    nd = t2.add('GeometryNodeGroup', group=GR[n]); t2.chain(nd, nd.inputs[0].name, nd.outputs[0].name)
    if n=="GR Densidade Livre": nd.inputs["Viewport"].default_value = 1.0
t2.chain(t2.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
profile(t2, EG, radius=0.0005); set_mat(t2, hair_mat("h", melanin=0.45, redness=0.7)); apply_tree(g, t2.finish())
print("INFO", stats(g).get('curves'))
shot("57_aplicado", res=420, samples=16, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.06), lens=48)
