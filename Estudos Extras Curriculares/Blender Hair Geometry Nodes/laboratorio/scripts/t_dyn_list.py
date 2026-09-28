import bpy, os
p = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','geometry_nodes_dynamics_assets.blend')
with bpy.data.libraries.load(p, link=False) as (src, dst):
    print("NGS", len(src.node_groups)); names = list(src.node_groups); dst.node_groups = names
for ng in bpy.data.node_groups:
    ins = [f"{i.name}({i.socket_type.replace('NodeSocket','')})" for i in ng.interface.items_tree if i.item_type=='SOCKET' and i.in_out=='INPUT']
    if not ng.name.startswith('.'): print("NG", ng.name, "| asset" if ng.asset_data else "", "|", ", ".join(ins)[:400])
