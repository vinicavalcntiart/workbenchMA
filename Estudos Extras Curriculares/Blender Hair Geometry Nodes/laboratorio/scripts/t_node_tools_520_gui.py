import bpy, sys, os
OUT = "/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/toolgui"
os.makedirs(OUT, exist_ok=True)
def log(*a):
    print("LOG", *a); sys.stdout.flush()
def attrs(cd):
    return sorted((a.name, a.domain, a.data_type) for a in cd.attributes if not a.name.startswith('.'))
def setup():
    for o in list(bpy.data.objects): bpy.data.objects.remove(o)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1); head = bpy.context.object; head.name = "head"
    bpy.ops.object.curves_empty_hair_add()   # objeto Curves de cabelo com surface = head (ativo antes)
    ob = bpy.context.object
    if ob.type != 'CURVES':
        cd = bpy.data.hair_curves.new("guias"); ob = bpy.data.objects.new("guias", cd); bpy.context.scene.collection.objects.link(ob)
    cd = ob.data
    cd.add_curves([4]*8)
    for i,p in enumerate(cd.points): p.position = ((i//4)*0.02-0.07, 0, 0.1+(i%4)*0.02)
    a = cd.attributes.new("Front_Guides_02_R", 'BOOLEAN', 'CURVE'); a.data.foreach_set("value", [i<4 for i in range(8)])
    f = cd.attributes.new("peso", 'FLOAT', 'CURVE'); f.data.foreach_set("value", [i*0.1 for i in range(8)])
    c = cd.attributes.new("cor", 'FLOAT_COLOR', 'POINT')
    u = cd.attributes.get("surface_uv_coordinate") or cd.attributes.new("surface_uv_coordinate", 'FLOAT2', 'CURVE')
    ob.select_set(True); bpy.context.view_layer.objects.active = ob
    return ob
def mk_tool(name, idname, kind):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.is_tool = True; ng.is_modifier = False; ng.is_mode_edit = True; ng.is_mode_sculpt = True; ng.is_type_curve = True
    ng.is_type_mesh = False
    ng.node_tool_idname = idname
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    s = ng.interface.new_socket("Nome", in_out='INPUT', socket_type='NodeSocketString'); s.default_value = "Front_Guides_02_R" if kind=="sel" else "Novo_Set"
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    gi = ng.nodes.new('NodeGroupInput'); go = ng.nodes.new('NodeGroupOutput'); L = ng.links.new
    if kind == "store":
        sel = ng.nodes.new('GeometryNodeToolSelection')
        st = ng.nodes.new('GeometryNodeStoreNamedAttribute'); st.data_type='BOOLEAN'; st.domain='CURVE'
        L(gi.outputs[0], st.inputs['Geometry']); L(gi.outputs[1], st.inputs['Name'])
        L([o for o in sel.outputs if o.type=='BOOLEAN'][0], st.inputs['Value']); L(st.outputs[0], go.inputs[0])
    else:
        na = ng.nodes.new('GeometryNodeInputNamedAttribute'); na.data_type='BOOLEAN'
        ss = ng.nodes.new('GeometryNodeToolSetSelection'); ss.domain='CURVE'
        L(gi.outputs[1], na.inputs['Name']); L(gi.outputs[0], ss.inputs['Geometry'])
        L([o for o in na.outputs if o.type=='BOOLEAN'][0], ss.inputs['Selection']); L(ss.outputs[0], go.inputs[0])
    return ng
def ctx():
    w = bpy.context.window_manager.windows[0]
    for ar in w.screen.areas:
        if ar.type == 'VIEW_3D':
            return dict(window=w, area=ar, region=[r for r in ar.regions if r.type=='WINDOW'][0])
STATE = {"step": 0}
import os as _o
_o.path.exists(OUT+'/PRONTO') and _o.remove(OUT+'/PRONTO')
def step():
    s = STATE["step"]; STATE["step"] += 1
    try:
        if s == 0:
            ob = setup(); STATE["ob"] = ob
            mk_tool("Salvar Selecao", "curves.salvar_selecao", "store"); mk_tool("Selecionar Conjunto", "curves.selecionar_conjunto", "sel")
            log("ANTES", attrs(ob.data), "surface", ob.data.surface.name if ob.data.surface else None)
            return 1.0
        if s == 1:
            log("OPS curves tem salvar/selecionar:", hasattr(bpy.ops.curves, "salvar_selecao"), hasattr(bpy.ops.curves, "selecionar_conjunto"))
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='EDIT')
            return 1.0
        if s == 2:
            ob = STATE["ob"]
            with bpy.context.temp_override(**ctx()):
                r = bpy.ops.curves.selecionar_conjunto('EXEC_DEFAULT')
            log("RUN selecionar", r)
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='OBJECT')
            sel = ob.data.attributes.get(".selection")
            log("SELECAO", None if sel is None else [bool(d.value) for d in sel.data][:8] if sel.domain=='CURVE' else (sel.domain, len(sel.data)))
            log("DEPOIS selecionar", attrs(ob.data))
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='EDIT')
            return 1.0
        if s == 3:
            ob = STATE["ob"]
            with bpy.context.temp_override(**ctx()):
                r = bpy.ops.curves.salvar_selecao('EXEC_DEFAULT')
            log("RUN salvar", r)
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='OBJECT')
            log("DEPOIS salvar", attrs(ob.data))
            ns = ob.data.attributes.get("Novo_Set"); log("Novo_Set", None if ns is None else [bool(d.value) for d in ns.data])
            return 1.0
        if s == 4:
            ob = STATE["ob"]
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='OBJECT'); bpy.ops.object.mode_set(mode='SCULPT_CURVES')
                r = bpy.ops.curves.selecionar_conjunto('EXEC_DEFAULT')
            log("RUN selecionar SCULPT", r)
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='OBJECT')
            log("DEPOIS sculpt", attrs(ob.data))
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='EDIT')
            w = bpy.context.window_manager.windows[0]
            for ar in w.screen.areas:
                if ar.type == 'PROPERTIES': ar.spaces[0].context = 'DATA'
                if ar.type == 'VIEW_3D':
                    r3 = ar.spaces[0].region_3d; r3.view_distance = 0.32; r3.view_location = (0,0,0.13)
            return 1.5
        if s == 5:
            w = bpy.context.window_manager.windows[0]
            v3 = [a for a in w.screen.areas if a.type == 'VIEW_3D'][0]
            with bpy.context.temp_override(window=w, area=v3, region=[r for r in v3.regions if r.type=='WINDOW'][0]):
                bpy.ops.screen.area_split(direction='VERTICAL', factor=0.45)
            return 1.0
        if s == 6:
            w = bpy.context.window_manager.windows[0]
            v3s = [a for a in w.screen.areas if a.type == 'VIEW_3D']
            ne = sorted(v3s, key=lambda a: a.x)[-1]
            ne.type = 'NODE_EDITOR'; ne.ui_type = 'GeometryNodeTree'
            sp = ne.spaces.active; sp.node_tree_sub_type = 'TOOL'
            STATE["ne"] = ne
            return 1.0
        if s == 7:
            ne = STATE["ne"]; w = bpy.context.window_manager.windows[0]
            sp = ne.spaces.active; sp.node_tree = bpy.data.node_groups["Selecionar Conjunto"]
            log("NE tree", sp.node_tree.name if sp.node_tree else None, sp.node_tree_sub_type)
            return 1.0
        if s == 8:
            ne = STATE["ne"]; w = bpy.context.window_manager.windows[0]
            with bpy.context.temp_override(window=w, area=ne, region=[r for r in ne.regions if r.type=='WINDOW'][0]):
                bpy.ops.node.view_all()
            open(OUT + "/PRONTO", "w").write("1"); log("PRONTO")
            return 8.0
        bpy.ops.wm.quit_blender(); return None
    except Exception as e:
        import traceback; log("ERR", repr(e)); traceback.print_exc(); bpy.ops.wm.quit_blender(); return None
bpy.app.timers.register(step, first_interval=2.0)
