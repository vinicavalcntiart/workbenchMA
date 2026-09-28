import bpy, os
p = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','geometry_nodes_dynamics_assets.blend')
with bpy.data.libraries.load(p, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics']
ng = bpy.data.node_groups['Hair Dynamics']
print("DESC", ng.description)
for i in ng.interface.items_tree:
    if i.item_type=='PANEL': print("P  [", i.name, "]"); continue
    d = getattr(i,'default_value',None)
    try: d = tuple(round(x,3) for x in d) if hasattr(d,'__len__') and not isinstance(d,str) else (round(d,4) if isinstance(d,float) else d)
    except Exception: pass
    print(" ", i.in_out, i.name, i.socket_type.replace('NodeSocket',''), d, "|", (i.description or "")[:110])
