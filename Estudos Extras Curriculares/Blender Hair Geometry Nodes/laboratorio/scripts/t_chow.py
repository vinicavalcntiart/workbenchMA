import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
def uniq(g):
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    a = d.attributes.get('guide_curve_index')
    if not a: return 0
    v = np.zeros(len(a.data), np.int32); a.data.foreach_get('value', v); return len(np.unique(v))
EG, head, scalp, g = base_scene(n_guides=200)
# modificador 1: interpolate + mapa esparso antigo (GD 0.1)
t1 = Tree("m1"); interp(t1, EG, density=300000.0); t1.eg(EG['Create Guide Index Map'], Guide_Distance=0.1); apply_tree(g, t1.finish())
print("CHOW apos mod1 (mapa esparso):", uniq(g))
# modificador 2: Clump Existing OFF GD 0.02
t2 = Tree("m2"); t2.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=0.02, Existing_Guide_Map=False, Preserve_Length=True); m2 = apply_tree(g, t2.finish())
print("CHOW apos mod2 (Clump Existing OFF, GD 2cm):", uniq(g))
# modificador 3: Curl Existing ON -> que mapa ele usa? medir via saida Guide Index
t3 = Tree("m3"); c = t3.eg(EG['Curl Hair Curves'], Radius=0.01, Frequency=9.0, Subdivision=1, Existing_Guide_Map=True)
st = t3.add('GeometryNodeStoreNamedAttribute', props={'data_type':'INT','domain':'CURVE'}, Name="curl_gi"); t3.chain(st); t3.link(c.outputs['Guide Index'], st.inputs['Value'])
apply_tree(g, t3.finish())
d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data; a = d.attributes['curl_gi']; v = np.zeros(len(a.data), np.int32); a.data.foreach_get('value', v)
print("CHOW Curl (Existing ON) usou mapa com", len(np.unique(v)), "guias")
