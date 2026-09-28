import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7, front_cut=0.75); head.data.materials.append(skin_mat()); scalp.hide_render = True
exec('def split_scalp' + open('r17_part.py').read().split("def build(")[0].split("def split_scalp")[1]); split_scalp(scalp)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("c2"); src_geo = t.geo
def branch(L, out, lado, tras, grav):
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": out, "Para o lado da risca": lado, "Para trás": tras, "Gravidade": grav}.items(): x.inputs[kk].default_value = v
    t.link(src_geo, x.inputs[0])
    d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 300000.0; t.link(x.outputs['Guias'], d.inputs[0])
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.link(d.outputs[0], rs.inputs['Curve'])
    return rs.outputs['Curve']
A = branch(0.30, 0.35, 0.6, 0.2, 2.2)          # cabelo normal
B = branch(0.14, 0.5, 1.1, -0.9, 1.4)           # franja: para frente e para o lado, cai na testa
import numpy as np
def roots(sock):
    tt = Tree("chk"); tt.link(sock, tt.go.inputs[0]) if False else None
    return sock
res=[]
for sock in (A,B):
    t.ng.links.new(sock, t.go.inputs[0])
    if not g.modifiers: apply_tree(g, t.ng)
    bpy.context.view_layer.update(); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    res.append((len(d.curves), len(d.points), P[[c.first_point_index for c in d.curves]]))
print("RAIZ contagens A/B:", res[0][:2], res[1][:2], "raiz dif max mm:", round(float(np.abs(res[0][2]-res[1][2]).max())*1000,4) if res[0][0]==res[1][0] else "n/a")
