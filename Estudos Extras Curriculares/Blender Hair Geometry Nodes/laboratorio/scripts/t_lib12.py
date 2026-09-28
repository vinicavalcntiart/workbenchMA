import sys; sys.path.insert(0,'.')
from lab import *
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(n_guides=60)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = ["GR Semente do Objeto"]
t = Tree("s"); sn = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Semente do Objeto"])
st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='r'; t.chain(st); t.link(sn.outputs['Aleatório A'], st.inputs['Value'])
apply_tree(g, t.finish())
import numpy as np
vals=[]
for x in (0.0, 0.34, 0.68):
    for o in (head, scalp, g): o.location = (x,0,0)
    bpy.context.view_layer.update(); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    a = np.zeros(len(d.curves), np.float32); d.attributes['r'].data.foreach_get('value', a); vals.append(round(float(a[0]),3))
print("INFO semente por posicao", vals)
