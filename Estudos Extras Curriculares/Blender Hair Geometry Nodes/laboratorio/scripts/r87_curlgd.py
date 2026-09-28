import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("c")
for name in ("GR Densidade Livre","GR Mecha Estilizada","GR Cacho por Mecha"):
    n = t.add('GeometryNodeGroup', group=GR[name]); t.chain(n, n.inputs[0].name, n.outputs[0].name)
apply_tree(g, t.finish())
curl = [n for n in GR['GR Cacho por Mecha'].nodes if n.bl_idname=='GeometryNodeGroup' and n.node_tree and n.node_tree.name.startswith('Curl Hair Curves')][0]
print("existing", curl.inputs['Existing Guide Map'].default_value, "linked?", curl.inputs['Existing Guide Map'].is_linked)
def snap():
    bpy.context.view_layer.update(); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); return P
a = snap(); curl.inputs['Guide Distance'].default_value = 0.01; b = snap()
print("CURLGD diferenca maxima ao trocar 0,1 -> 0,01:", float(np.abs(a-b).max()))
