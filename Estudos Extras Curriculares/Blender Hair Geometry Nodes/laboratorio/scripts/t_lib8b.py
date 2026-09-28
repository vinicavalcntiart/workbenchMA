import sys; sys.path.insert(0,'.')
exec(open('t_lib8.py').read().split('shot("t_lib8_cards"')[0])
dg = bpy.context.evaluated_depsgraph_get(); ev = g.evaluated_get(dg)

bpy.ops.object.select_all(action='DESELECT'); g.select_set(True); bpy.context.view_layer.objects.active = g
try:
    r = bpy.ops.object.convert(target='MESH'); ob = bpy.context.view_layer.objects.active
    print("CONV", r, ob.type, len(ob.data.polygons) if ob.type=='MESH' else None, [u.name for u in ob.data.uv_layers] if ob.type=='MESH' else None)
except Exception as e: print("CONV erro", e); ob=None
if ob is not None and ob.type=='MESH':
    fbx = os.path.join(OUT, "cards_teste.fbx"); r = bpy.ops.export_scene.fbx(filepath=fbx, use_selection=True); print("FBX", r, os.path.getsize(fbx))
