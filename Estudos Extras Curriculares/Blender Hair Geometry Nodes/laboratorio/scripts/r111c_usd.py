import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("abc")
for name, kw in (("GR Densidade Livre", {"Viewport": 1.0, "Fios por m2": 150000.0}), ("GR Mecha Estilizada", {}), ("GR Onda S", {})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
for nm, dt, dom in (("cor_mecha","FLOAT_COLOR","POINT"), ("cor_curva","FLOAT_COLOR","CURVE"), ("uv_teste","FLOAT2","CURVE"), ("peso","FLOAT","POINT")):
    stn = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':dt,'domain':dom}); stn.inputs['Name'].default_value = nm; t.chain(stn)
    [x for x in stn.inputs if x.name=='Value' and x.enabled][0].default_value = ((0.8,0.2,0.1,1) if dt=='FLOAT_COLOR' else (0.3,0.7,0.0) if dt=="FLOAT2" else 0.5)
profile(t, EG, radius=0.0005, shape=0.5); apply_tree(g, t.finish())
st = stats(g); _d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data; print("ABC antes", st.get("curves"), st.get("points"), "raio medio mm", round(float(np.mean([pt.radius for pt in list(_d.points)[:5000]]))*1000,3), "attrs", st.get("attrs"))
p = os.path.join(OUT, "groom_teste.usdc")
bpy.ops.object.select_all(action='DESELECT'); g.select_set(True); bpy.context.view_layer.objects.active = g
t0 = time.time(); r = bpy.ops.wm.usd_export(filepath=p, selected_objects_only=True, evaluation_mode='RENDER'); print("ABC export", r, round(time.time()-t0,2), "s", round(os.path.getsize(p)/1e6,1), "MB")
n0 = set(bpy.data.objects.keys()); bpy.ops.wm.usd_import(filepath=p); new = [bpy.data.objects[k] for k in set(bpy.data.objects.keys())-n0]
for o in new:
    print("ABC importado", o.name, o.type, end=" ")
    d = o.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    print("ATTR", sorted(a.name for a in o.data.attributes if not a.name.startswith('.')))
    try:
        print(len(d.curves), len(d.points), "raio medio mm", round(float(np.mean([pt.radius for pt in list(d.points)[:5000]]))*1000,3))
    except Exception as e:
        try: print(len(d.splines))
        except Exception as e2: print(e, e2)
