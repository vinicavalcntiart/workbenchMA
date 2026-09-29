import bpy, sys
def log(*a): print("LOG", *a); sys.stdout.flush()
def setup():
    for o in list(bpy.data.objects): bpy.data.objects.remove(o)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1)
    bpy.ops.object.curves_empty_hair_add(); ob = bpy.context.object; cd = ob.data
    cd.add_curves([4]*8)
    for i,p in enumerate(cd.points): p.position = ((i//4)*0.02-0.07, 0, 0.1+(i%4)*0.02)
    cd.attributes.new("Front_Guides_02_R", 'BOOLEAN', 'CURVE').data.foreach_set("value", [i<4 for i in range(8)])
    return ob
def base(name):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.is_tool = True; ng.is_modifier = False; ng.is_mode_edit = True; ng.is_type_curve = True; ng.is_type_mesh = False
    ng.node_tool_idname = "curves.tool"
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    return ng, ng.nodes.new('NodeGroupInput'), ng.nodes.new('NodeGroupOutput')
def ctx():
    w = bpy.context.window_manager.windows[0]; a = [x for x in w.screen.areas if x.type == 'VIEW_3D'][0]
    return dict(window=w, area=a, region=[r for r in a.regions if r.type=='WINDOW'][0])
ST = {"s": 0}
def step():
    s = ST["s"]; ST["s"] += 1
    try:
        if s == 0:
            # "Tool" antigo: passa a geometria direto (nao apaga nada)
            ng, gi, go = base("Tool"); ng.links.new(gi.outputs[0], go.inputs[0])
            # "Tool.001" corrigido: apaga o conjunto
            ng2, gi2, go2 = base("Tool.001")
            na = ng2.nodes.new('GeometryNodeInputNamedAttribute'); na.data_type='BOOLEAN'; na.inputs['Name'].default_value = "Front_Guides_02_R"
            sp = ng2.nodes.new('GeometryNodeSeparateGeometry'); sp.domain='CURVE'
            ng2.links.new(gi2.outputs[0], sp.inputs['Geometry']); ng2.links.new([o for o in na.outputs if o.type=='BOOLEAN'][0], sp.inputs['Selection'])
            ng2.links.new(sp.outputs['Inverted'], go2.inputs[0])
            ST["ob"] = setup()
            return 1.0
        if s == 1:
            ob = ST["ob"]
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='EDIT')
            log("ANTES curvas", len(ob.data.curves))
            with bpy.context.temp_override(**ctx()): r = bpy.ops.curves.tool('EXEC_DEFAULT')
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='OBJECT')
            log("RUN curves.tool", r, "DEPOIS curvas", len(ob.data.curves), "(4 = rodou Tool.001; 8 = rodou o Tool antigo)")
            return 1.0
        bpy.ops.wm.quit_blender(); return None
    except Exception as e:
        import traceback; log("ERR", repr(e)); traceback.print_exc(); bpy.ops.wm.quit_blender(); return None
bpy.app.timers.register(step, first_interval=2.0)
