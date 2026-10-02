import bpy, numpy as np
def P(*a): print("RESULT", *a, flush=True)
ob = bpy.data.objects["Cabelo"]
def ev(o):
    dg = bpy.context.evaluated_depsgraph_get(); dg.update()
    e = o.evaluated_get(dg).data
    return len(e.curves), np.array([p.vector for p in e.attributes["position"].data])
n0, co0 = ev(ob)
def newtree(name):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    return ng, ng.nodes, ng.links.new, ng.nodes.new('NodeGroupInput'), ng.nodes.new('NodeGroupOutput')
def to_top(o, md):
    o.modifiers.move(len(o.modifiers)-1, 0)
bpy.context.view_layer.objects.active = ob
for o in bpy.context.selected_objects: o.select_set(False)
ob.select_set(True)
if ob.mode != "OBJECT": bpy.ops.object.mode_set(mode="OBJECT")
# 1) grava a ordem: Store Named Attribute "ordem" = Index (Spline), Apply
ng, N, L, gi, go = newtree("Gravar Ordem")
st = N.new('GeometryNodeStoreNamedAttribute'); st.data_type = 'INT'; st.domain = 'CURVE'; st.inputs["Name"].default_value = "ordem"
ix = N.new('GeometryNodeInputIndex')
L(gi.outputs[0], st.inputs["Geometry"]); L(ix.outputs[0], st.inputs["Value"]); L(st.outputs[0], go.inputs[0])
m = ob.modifiers.new("Gravar Ordem", 'NODES'); m.node_group = ng; to_top(ob, m)
bpy.ops.object.modifier_apply(modifier="Gravar Ordem")
P("ordem gravada:", "ordem" in ob.data.attributes, ob.data.attributes["ordem"].domain, [m.name for m in ob.modifiers])
# 2) separa (P)
bpy.ops.object.mode_set(mode='EDIT')
sel = [d.value for d in ob.data.attributes["Front_Guides_02_R"].data]
a = ob.data.attributes.get(".selection") or ob.data.attributes.new(".selection", 'BOOLEAN', 'CURVE')
a.data.foreach_set("value", sel)
P("users antes do separate", ob.data.users)
bpy.ops.curves.separate()
P("users depois do separate (edit)", ob.data.users)
bpy.ops.object.mode_set(mode='OBJECT')
new = [o for o in bpy.data.objects if o.type == 'CURVES' and o is not ob][0]
P("users em object mode", ob.data.users, "copia", new.data.users, new.data is ob.data)
for mm in list(new.modifiers): new.modifiers.remove(mm)
new.hide_set(True); new.hide_render = True
# 3) Object Info -> Join -> Sort Elements (Spline, ordem)
ng, N, L, gi, go = newtree("Guias Ocultas")
oi = N.new('GeometryNodeObjectInfo'); oi.transform_space = 'ORIGINAL'; oi.inputs["Object"].default_value = new
j = N.new('GeometryNodeJoinGeometry')
so = N.new('GeometryNodeSortElements'); so.domain = 'CURVE'
na = N.new('GeometryNodeInputNamedAttribute'); na.data_type = 'INT'; na.inputs["Name"].default_value = "ordem"
L(gi.outputs[0], j.inputs[0]); L(oi.outputs["Geometry"], j.inputs[0]); L(j.outputs[0], so.inputs["Geometry"])
L(na.outputs["Attribute"], so.inputs["Sort Weight"]); L(so.outputs[0], go.inputs[0])
md = ob.modifiers.new("Guias Ocultas", 'NODES'); md.node_group = ng; to_top(ob, md); md.show_in_editmode = False
n1, co1 = ev(ob)
P("escondido: guias", len(ob.data.curves), "avaliadas", n1, "de", n0, "| maior diferenca ponto a ponto:", float(np.abs(co0 - co1).max()) if len(co0)==len(co1) else "n/a")
bpy.ops.wm.save_as_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/hide_manual_escondido.blend")
bpy.ops.wm.open_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/hide_manual_escondido.blend")
ob = bpy.data.objects["Cabelo"]; new = bpy.data.objects["Cabelo.001"]
bpy.context.view_layer.objects.active = ob
P("users depois de reabrir", ob.data.users)
# 4) revelar: Apply no modificador (ja esta no topo) e apaga a copia
bpy.ops.object.modifier_apply(modifier="Guias Ocultas")
bpy.data.objects.remove(new)
n2, co2 = ev(ob)
P("revelado com Apply: guias", len(ob.data.curves), "avaliadas", n2, "| diferenca:", float(np.abs(co0 - co2).max()),
  "| atributos:", [x.name for x in ob.data.attributes if not x.name.startswith('.')], "| stack:", [m.name for m in ob.modifiers])
src = bpy.data.objects["Cabelo"].data
P("surface ok:", ob.data.surface is not None, ob.data.surface_uv_map)
