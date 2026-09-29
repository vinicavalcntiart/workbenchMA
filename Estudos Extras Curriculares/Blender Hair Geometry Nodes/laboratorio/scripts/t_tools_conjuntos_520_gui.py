import bpy, sys, os
OUT = "/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/toolgui"
def log(*a): print("LOG", *a); sys.stdout.flush()
def attrs(cd): return sorted(a.name for a in cd.attributes if not a.name.startswith('.'))
def ctx():
    w = bpy.context.window_manager.windows[0]; a = [x for x in w.screen.areas if x.type == 'VIEW_3D'][0]
    return dict(window=w, area=a, region=[r for r in a.regions if r.type=='WINDOW'][0])
def sel_mask(cd):
    s = cd.attributes.get(".selection")
    return [bool(d.value) for d in s.data] if s is not None and s.domain == 'CURVE' else None
ST = {"s": 0}
def step():
    s = ST["s"]; ST["s"] += 1
    try:
        ob = bpy.data.objects['Cabelo']; cd = ob.data
        if s == 0:
            log("OPS", [hasattr(bpy.ops.curves, n) for n in ("salvar_selecao", "selecionar_conjunto", "apagar_conjunto")])
            log("ANTES curvas", len(cd.curves), attrs(cd))
            with bpy.context.temp_override(**ctx()):
                bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.curves.set_selection_domain(domain='CURVE')
            return 1.5
        if s == 1:
            try:
                with bpy.context.temp_override(**ctx()):
                    r = bpy.ops.curves.selecionar_conjunto('EXEC_DEFAULT')
            except AttributeError as e:
                ST["retry"] = ST.get("retry", 0) + 1; log("retry", ST["retry"], e)
                if ST["retry"] > 10: raise
                ST["s"] = 1; return 1.0
            front = [bool(d.value) for d in cd.attributes["Front_Guides_02_R"].data]
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='OBJECT')
            m = sel_mask(cd); log("SELECIONAR", r, "selecionadas", sum(m) if m else None, "igual ao conjunto", m == front)
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='EDIT')
            # tela: viewport de frente para o rosto, node editor com o Apagar Conjunto
            w = bpy.context.window_manager.windows[0]
            v3 = [a for a in w.screen.areas if a.type == 'VIEW_3D'][0]
            with bpy.context.temp_override(window=w, area=v3, region=[r for r in v3.regions if r.type=='WINDOW'][0]):
                bpy.ops.view3d.view_axis(type='FRONT'); bpy.ops.view3d.view_selected()
            return 1.0
        if s == 2:
            w = bpy.context.window_manager.windows[0]
            for a in w.screen.areas:
                if a.type == 'PROPERTIES': a.spaces.active.context = 'DATA'
            return 1.0
        if s == 3:
            return 1.0
        if s == 4:
            open(OUT + "/PRONTO", "w").write("1"); log("PRONTO"); return 6.0
        if s == 5:
            with bpy.context.temp_override(**ctx()): r = bpy.ops.curves.salvar_selecao('EXEC_DEFAULT')
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='OBJECT')
            nv = [bool(d.value) for d in cd.attributes["Novo_Conjunto"].data]
            log("SALVAR", r, "Novo_Conjunto", sum(nv), "attrs", attrs(cd))
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='EDIT'); r = bpy.ops.curves.apagar_conjunto('EXEC_DEFAULT')
            with bpy.context.temp_override(**ctx()): bpy.ops.object.mode_set(mode='OBJECT')
            back = sum(bool(d.value) for d in cd.attributes["Back_Guides_01_R"].data)
            log("APAGAR", r, "curvas", len(cd.curves), "back restantes", back, "attrs", attrs(cd))
            dg = bpy.context.evaluated_depsgraph_get(); log("FILHOS depois", len(ob.evaluated_get(dg).data.curves))
            return 1.0
        bpy.ops.wm.quit_blender(); return None
    except Exception as e:
        import traceback; log("ERR", repr(e)); traceback.print_exc(); bpy.ops.wm.quit_blender(); return None
bpy.app.timers.register(step, first_interval=3.0)
