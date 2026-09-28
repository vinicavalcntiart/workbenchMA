import sys; sys.path.insert(0,'.')
from lab import *
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
CH = [("GR Densidade Livre", {"Fios por m2": 300000.0, "Viewport": 1.0}), ("GR Mecha Estilizada", {}), ("GR Volume na Raiz", {}), ("GR Strays em Arco", {}),
      ("GR Onda S", {}), ("GR Cacho por Mecha", {}), ("GR Ponta Virada", {"Subdivisão": int([a for a in sys.argv if a.isdigit()][-1])}), ("GR Cor por Mecha", {})]
if "antes" in sys.argv: CH = [CH[0],CH[1],CH[2],CH[3],CH[6],CH[4],CH[5],CH[7]]
t = Tree("c"); nodes = []
for name, kw in CH:
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name); nodes.append(n)
pr = profile(t, EG, radius=0.0005)
m = apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get()
def ev():
    ts=[]
    for i in range(3):
        m.show_viewport=False; dg.update(); m.show_viewport=True; t0=time.time(); dg.update(); g.evaluated_get(dg).data.points; ts.append(time.time()-t0)
    return min(ts)*1000
# mede acumulado: muta tudo depois do grupo k
prev = 0
for k in range(len(nodes)):
    for j,n in enumerate(nodes): n.mute = j > k
    ms = ev(); st = stats(g)
    print(f"COST {CH[k][0]:24s} acumulado {ms:7.0f} ms  (+{ms-prev:5.0f})  fios {st.get('curves')}  pontos {st.get('points')}")
    prev = ms
for n in nodes: n.mute = False
nodes[0].inputs["Viewport"].default_value = 0.25
print(f"COST viewport 0,25: {ev():.0f} ms", stats(g).get('curves'))
