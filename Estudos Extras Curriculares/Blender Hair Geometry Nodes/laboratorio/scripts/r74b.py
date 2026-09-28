import sys; sys.path.insert(0,'.')
import numpy as np
V = sys.argv[-1]
src = open('r74_chapeu.py').read().split('if V == "sem": hat.hide_render')[0]
exec(src)
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
rxy = np.hypot(P[:,0], P[:,1]); z = P[:,2]
# atravessa a parede da copa: fora do raio 10,8 cm dentro da altura da copa
fora = ((rxy > 0.108) & (z > 0.035) & (z < 0.13)).sum()
print("CH", V, "pontos atravessando a parede da copa:", int(fora), "de", len(P))
