import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
def uniq(g, name):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    a = d.attributes.get(name); v = np.zeros(len(a.data), np.int32); a.data.foreach_get('value', v); return len(np.unique(v)), len(v)
for gd in (0.005, 0.02, 0.05):
    for src in ("guias originais", "depois do Interpolate"):
        EG, head, scalp, g = base_scene(n_guides=220)
        t = Tree("c")
        if src != "guias originais": interp(t, EG, density=300000.0)
        cg = t.eg(EG['Create Guide Index Map'], Guide_Distance=gd)
        st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'INT','domain':'CURVE'}, Name="gi_out"); t.chain(st)
        t.link(cg.outputs['Guide Index'], st.inputs['Value'])
        apply_tree(g, t.finish())
        print(f"CGIM GD {gd} {src:22s}: saida Guide Index unicos {uniq(g,'gi_out')}, atributo guide_curve_index unicos {uniq(g,'guide_curve_index')}")
