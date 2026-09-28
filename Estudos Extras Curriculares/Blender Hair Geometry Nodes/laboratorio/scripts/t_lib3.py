import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
def load():
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
    return {n.name: n for n in bpy.data.node_groups}
exec(open('t_mask.py').read().split("def run(")[0].split("img = None")[1])
# mascara
reset(); GR = load(); head, scalp = make_head(); g = comb_guides(scalp, n=200); attach_uv(g, scalp)
t = Tree("m"); d_ = t.add('GeometryNodeGroup', group=GR['GR Densidade Livre']); d_.inputs['Viewport'].default_value = 1.0; t.chain(d_)
m = t.add('GeometryNodeGroup', group=GR['GR Máscara por Imagem']); m.inputs['Imagem'].default_value = make_img(); t.chain(m)
apply_tree(g, t.finish()); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
uv = np.zeros(len(d.curves)*2, np.float32); d.attributes['surface_uv_coordinate'].data.foreach_get('vector', uv); uv = uv.reshape(-1,2)
print(f"LIB3 GR Mascara por Imagem: fios {len(uv)}, no preto {(uv[:,0]<0.5).sum()}")
# fisica
reset(); GR = load(); head, scalp = make_head(); g = comb_guides(scalp, n=260, spread=0.35, gravity=0.8, outward=0.8, length=0.22); attach_uv(g, scalp)
t = Tree("f"); fz = t.add('GeometryNodeGroup', group=GR['GR Física Estilizada']); t.chain(fz, 'Guias', 'Guias'); apply_tree(g, t.finish())
def tips():
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    return P[[c.first_point_index+c.points_length-1 for c in d.curves]]
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=36; sc.frame_set(1); T0 = tips()
for f in range(2,37): sc.frame_set(f)
print(f"LIB3 GR Fisica Estilizada: ponta desce {(T0[:,2]-tips()[:,2]).mean()*100:.1f} cm em 36 quadros")
