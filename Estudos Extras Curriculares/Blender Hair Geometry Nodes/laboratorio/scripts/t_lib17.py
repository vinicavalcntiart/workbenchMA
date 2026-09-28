import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
e = link(bpy.data.objects.new("MAO", None)); e.location = (0.125,-0.01,0.0)
t = Tree("x")
for name, kw in (("GR Densidade Livre", {"Viewport": 1.0}), ("GR Mecha Estilizada", {}), ("GR Desviar de Objeto", {"Objeto": e})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
apply_tree(g, t.finish())
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
print("INFO lib dentro de 4,4 cm:", int((np.linalg.norm(P-np.array(e.location[:]),axis=1)<0.044).sum()))
