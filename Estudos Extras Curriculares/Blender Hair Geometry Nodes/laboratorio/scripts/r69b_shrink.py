import sys; sys.path.insert(0,'.')
exec(open('r69_audit.py').read().split("m = apply_tree")[0].replace('("GR Corte pela Malha", {}), ("GR Flutuar", {})', '("GR Corte pela Malha", {})'))
import numpy as np
pos = sys.argv[-1]   # nenhum | antes_cacho | fim
def shrink():
    w = t.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.003, Above_Surface=0.0, Smoothing_Steps=0, Lock_Roots=True)
    for q in w.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
    return w
# reconstroi a arvore com o shrink na posicao pedida
t = Tree("b"); prev = None
for name, kw in CH:
    if name == "GR Onda S" and pos == "antes_cacho": t.chain(shrink())
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
if pos == "fim": t.chain(shrink())
m = apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ts=[]
for i in range(3):
    m.show_viewport=False; dg.update(); m.show_viewport=True; t0=time.time(); dg.update(); d = g.evaluated_get(dg).data; ts.append(time.time()-t0)
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3); r = np.linalg.norm(P, axis=1)
print(f"SHR {pos:12s} dentro {100*(r<0.0995).mean():5.2f}%  avaliacao {min(ts)*1000:6.0f} ms  pontos {len(P)}")
