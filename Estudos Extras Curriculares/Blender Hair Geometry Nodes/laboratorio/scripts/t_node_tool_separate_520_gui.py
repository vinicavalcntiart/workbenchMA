import bpy, sys
def log(*a): print("LOG", *a); sys.stdout.flush()
def attrs(cd): return sorted((a.name, a.domain) for a in cd.attributes if not a.name.startswith('.'))
def setup():
    for o in list(bpy.data.objects): bpy.data.objects.remove(o)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1)
    bpy.ops.object.curves_empty_hair_add(); ob = bpy.context.object; cd = ob.data
    cd.add_curves([4]*8)
    for i,p in enumerate(cd.points): p.position = ((i//4)*0.02-0.07, 0, 0.1+(i%4)*0.02)
    cd.attributes.new("Front_Guides_02_R", 'BOOLEAN', 'CURVE').data.foreach_set("value", [i<4 for i in range(8)])
    cd.attributes.new("Back_Guides_01_R", 'BOOLEAN', 'CURVE').data.foreach_set("value", [i>=6 for i in range(8)])
    cd.attributes.new("peso", 'FLOAT', 'CURVE').data.foreach_set("value", [i*0.1 for i in range(8)])
    return ob
def mk(name, idname, attrname, sep_link):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.is_tool = True; ng.is_modifier = False; ng.is_mode_edit = True; ng.is_type_curve = True; ng.is_type_mesh = False
    ng.node_tool_idname = idname
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    gi = ng.nodes.new('NodeGroupInput'); go = ng.nodes.new('NodeGroupOutput'); L = ng.links.new
    na = ng.nodes.new('GeometryNodeInputNamedAttribute'); na.data_type = 'BOOLEAN'; na.inputs['Name'].default_value = attrname
    ss = ng.nodes.new('GeometryNodeToolSetSelection'); ss.domain = 'CURVE'
    sp = ng.nodes.new('GeometryNodeSeparateGeometry'); sp.domain = 'CURVE'
    L(gi.outputs[0], ss.inputs['Geometry']); L([o for o in na.outputs if o.type=='BOOLEAN'][0], ss.inputs['Selection'])
    L(ss.outputs[0], sp.inputs['Geometry'])
    if sep_link: L([o for o in na.outputs if o.type=='BOOLEAN'][0], sp.inputs['Selection'])
    L(sp.outputs['Inverted'], go.inputs[0])
def ctx():
    w = bpy.context.window_manager.windows[0]; a = [x for x in w.screen.areas if x.type == 'VIEW_3D'][0]
    return dict(window=w, area=a, region=[r for r in a.regions if r.type=='WINDOW'][0])
CASES = [("Grafo do Vini", "curves.grafo_vini", "Front_Guides_02_R", False), ("Vini nome errado", "curves.grafo_vini_nome", "Front_Guides_02", False), ("Corrigido", "curves.grafo_corrigido", "Front_Guides_02_R", True)]
ST = {"s": 0}
def step():
    s = ST["s"]; ST["s"] += 1
    try:
        if s == 0:
            for c in CASES: mk(*c)
            return 1.0
        if 1 <= s <= len(CASES):
            name, idn, an, lk = CASES[s-1]
            ob = setup()
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='EDIT')
            log(name, "ANTES curvas", len(ob.data.curves), attrs(ob.data))
            op = getattr(bpy.ops.curves, idn.split('.')[1])
            with bpy.context.temp_override(**ctx()): r = op('EXEC_DEFAULT')
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='OBJECT')
            log(name, "RUN", r, "DEPOIS curvas", len(ob.data.curves), attrs(ob.data), "surface", ob.data.surface.name if ob.data.surface else None)
            return 1.0
        bpy.ops.wm.quit_blender(); return None
    except Exception as e:
        import traceback; log("ERR", repr(e)); traceback.print_exc(); bpy.ops.wm.quit_blender(); return None
bpy.app.timers.register(step, first_interval=2.0)
