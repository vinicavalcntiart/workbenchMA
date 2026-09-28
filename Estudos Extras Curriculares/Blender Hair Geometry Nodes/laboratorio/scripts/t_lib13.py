import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.7
import numpy as np
FZ = -0.55
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
bpy.ops.mesh.primitive_plane_add(size=3, location=(0,0,FZ))
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("c")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for kk,v in kw.items(): n.inputs[kk].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
x = grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 1.1, "Para fora": 0.3, "Para o lado da risca": 0.25, "Para trás": 0.35, "Gravidade": 3.0})
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 60; t.chain(rs, 'Curve', 'Curve')
grp("GR Chão", **{"Altura do chão": FZ})
grp("GR Flutuar", **{"Amplitude": 0.05})
grp("GR Densidade Livre", **{"Fios por m2": 200000.0, "Viewport": 1.0})
grp("GR Mecha Estilizada")
grp("GR Chão", **{"Altura do chão": FZ, "Espalhar": False})
profile(t, EG, radius=0.0006); set_mat(t, hair_mat("h", melanin=0.1, redness=0.9)); apply_tree(g, t.finish())
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
print("INFO fios", len(d.curves), "z min", round(float(P[:,2].min()),4), "pontos no chao", int((P[:,2] < FZ+0.01).sum()))
shot("t_lib13_chao", res=420, samples=16, cam_loc=(1.1,-1.3,0.25), target=(0,0.1,-0.35), lens=40)
