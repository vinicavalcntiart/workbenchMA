import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
def meas(g):
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    if len(d.curves)==0: return (0, 0.0, 0.0)
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    L = [np.linalg.norm(np.diff(P[c.first_point_index:c.first_point_index+c.points_length],axis=0),axis=1).sum() for c in list(d.curves)[:2000]]
    T = P[[c.first_point_index+c.points_length-1 for c in list(d.curves)[:2000]]]
    return (len(d.curves), round(float(np.mean(L))*100,1), round(float(np.linalg.norm(T,axis=1).mean())*100,1))
for name in ("(nenhum)", "GR Forma por Malha", "GR Comprimento até a Malha", "GR Pentear por Curva", "GR Rabo de Cavalo", "GR LOD por Câmera", "GR Corte pela Malha", "GR Trança Grossa"):
    EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, n_guides=150)
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
    t = Tree("s"); d = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 60000.0; t.chain(d)
    if name != "(nenhum)":
        n = t.add('GeometryNodeGroup', group=bpy.data.node_groups[name]); t.chain(n, n.inputs[0].name, n.outputs[0].name)
    apply_tree(g, t.finish())
    print(f"SEM {name:28s} fios, comprimento medio cm, dist. media da ponta ao centro cm:", meas(g))
