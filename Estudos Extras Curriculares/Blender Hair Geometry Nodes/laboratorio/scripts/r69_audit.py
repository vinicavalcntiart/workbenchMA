import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head()
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
CH = [("GR Guias Procedurais", {"Cabeça (colisão)": head}), ("GR Densidade Livre", {"Viewport": 1.0}), ("GR Mecha Estilizada", {}), ("GR Volume na Raiz", {}),
      ("GR Strays em Arco", {}), ("GR Ponta Virada", {}), ("GR Onda S", {}), ("GR Cacho por Mecha", {}), ("GR Corte pela Malha", {}), ("GR Flutuar", {})]
t = Tree("a"); nodes=[]
for name, kw in CH:
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name); nodes.append(n)
m = apply_tree(g, t.finish())
for k in range(len(nodes)):
    for j,n in enumerate(nodes): n.mute = j > k
    if CH[k][0] == "GR Corte pela Malha": continue
    bpy.context.view_layer.update()
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    r = np.linalg.norm(P, axis=1)
    print(f"AUD {CH[k][0]:22s} dentro da cabeca {100*(r<0.0995).mean():5.2f}%   (pontos {len(P)})")
