import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np, math
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("rb"); nodes=[]
CH = [("GR Guias Procedurais", {"Cabeça (colisão)": head}), ("GR Densidade Livre", {"Viewport": 1.0, "Seed": 0}), ("GR Mecha Estilizada", {}), ("GR Volume na Raiz", {}), ("GR Ponta Virada", {"Para fora": True, "Subdivisão": 0}), ("GR Onda S", {})]
for name, kw in CH:
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name); nodes.append(n)
apply_tree(g, t.finish())
root = link(bpy.data.objects.new("rig", None))
for o in (head, scalp, g): o.parent = root
def snap():
    bpy.context.view_layer.update(); d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); return len(d.curves), P
for k in range(len(nodes)):
    for j,n in enumerate(nodes): n.mute = j > k
    root.location = (0,0,0); root.rotation_euler = (0,0,0); n0,A = snap()
    root.location = (0.6,0.3,1.5); n1,B = snap()
    root.location = (0,0,0); root.rotation_euler = (math.radians(25),0,math.radians(60)); n2,C = snap()
    dB = float(np.abs(A-B).max()) if n0==n1 else None; dC = float(np.abs(A-C).max()) if n0==n2 else None
    print(f"ROB2 {CH[k][0]:24s} fios {n0}/{n1}/{n2}  dif max deslocado {dB}  girado {dC}")
