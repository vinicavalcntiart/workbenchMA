import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("mp")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; t.chain(d)
mk = t.add('GeometryNodeGroup', group=GR["GR Máscara por Posição"]); mk.inputs["Altura mín"].default_value = 0.05
mr = t.add('ShaderNodeMapRange'); t.link(mk.outputs[0], mr.inputs['Value']); mr.inputs['To Min'].default_value = 1.0; mr.inputs['To Max'].default_value = 0.4
tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False); t.link(mr.outputs['Result'], tr.inputs['Length Factor'])
st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='m'; t.chain(st); t.link(mk.outputs[0], st.inputs['Value'])
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5)); apply_tree(g, t.finish())
dd = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
a = np.zeros(len(dd.curves), np.float32); dd.attributes['m'].data.foreach_get('value', a)
print("INFO mascara: fios =1:", int((a>0.99).sum()), "=0:", int((a<0.01).sum()), "transicao:", int(((a>0.01)&(a<0.99)).sum()), "de", len(a))
shot("t_lib16_mascara", res=380, samples=16, cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.05), lens=46)
