import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import math, numpy as np
MUNDO = sys.argv[-1] == "1"
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("gm")
n = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"]); n.inputs["Cabeça (colisão)"].default_value = head; n.inputs["Comprimento"].default_value = 0.3; n.inputs["Gravidade"].default_value = 2.0; n.inputs["Gravidade do mundo"].default_value = MUNDO; t.chain(n, 'Geometry', 'Guias')
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; t.chain(d)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.4)); apply_tree(g, t.finish())
for o in (head, scalp, g): o.rotation_euler = (0, math.radians(50), 0)   # cabeca inclinada de lado
bpy.context.view_layer.update()
dd = g.evaluated_get(bpy.context.evaluated_depsgraph_get())
P = np.zeros(len(dd.data.points)*3, np.float32); dd.data.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
W = np.array([ (g.matrix_world @ Vector(p))[:] for p in P[::50]])
R = np.array([ (g.matrix_world @ Vector(P[c.first_point_index]))[:] for c in list(dd.data.curves)[::50]])
T = np.array([ (g.matrix_world @ Vector(P[c.first_point_index+c.points_length-1]))[:] for c in list(dd.data.curves)[::50]])
print("GM mundo" if MUNDO else "GM objeto", "ponta - raiz (mundo) media: x %.3f z %.3f" % tuple((T-R).mean(0)[[0,2]]))
shot(f"t_lib18_{int(MUNDO)}", res=360, samples=12, cam_loc=(0.0,-0.8,0.0), target=(0,0,-0.08), lens=42)
