import bpy, sys
OUTP = sys.argv[-1]
def log(*a): print("LOG", *a); sys.stdout.flush()
ob = bpy.data.objects['Cabelo']; main = ob.modifiers['Groom inicial']; tree = main.node_group
gp = [n for n in tree.nodes if getattr(n, 'node_tree', None) and n.node_tree.name == 'GR Guias Procedurais'][0]
# 1. guias procedurais viram curvas reais: modificador temporario so com a GR Guias Procedurais, aplicado
tmp = bpy.data.node_groups.new("tmp_guias", 'GeometryNodeTree')
tmp.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
tmp.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
gi = tmp.nodes.new('NodeGroupInput'); go = tmp.nodes.new('NodeGroupOutput')
g2 = tmp.nodes.new('GeometryNodeGroup'); g2.node_tree = gp.node_tree
for s in gp.inputs:
    if hasattr(s, 'default_value') and not s.is_linked:
        try: g2.inputs[s.identifier].default_value = s.default_value
        except Exception: pass
tmp.links.new(gi.outputs[0], g2.inputs[0]); tmp.links.new(g2.outputs[0], go.inputs[0])
m = ob.modifiers.new("tmp", 'NODES'); m.node_group = tmp
bpy.ops.object.modifier_move_to_index({'object': ob}, modifier="tmp", index=0) if False else None
main.show_viewport = False; main.show_render = False
while ob.modifiers[0].name != "tmp":
    with bpy.context.temp_override(object=ob, active_object=ob): bpy.ops.object.modifier_move_up(modifier="tmp")
with bpy.context.temp_override(object=ob, active_object=ob): bpy.ops.object.modifier_apply(modifier="tmp")
main.show_viewport = True; main.show_render = True
bpy.data.node_groups.remove(tmp)
cd = ob.data; n = len(cd.curves)
for a in list(cd.attributes):
    if a.name == "UVMap" or a.name.startswith(".uv_select"):
        log("REMOVE", a.name, a.domain, a.data_type); cd.attributes.remove(cd.attributes[a.name])
log("GUIAS reais", n, [a.name for a in cd.attributes])
# 2. groom passa a usar as guias reais: tira a GR Guias Procedurais da cadeia
gin = [x for x in tree.nodes if x.type == 'GROUP_INPUT'][0]
nxt = [l.to_socket for l in tree.links if l.from_node == gp][0]
tree.nodes.remove(gp); tree.links.new(gin.outputs[0], nxt)
# 2b. Deform Curves on Surface sai do fim da cadeia e vira modificador proprio antes do groom
#     (ultimo na stack; botao Edit Mode do modificador desligado)
dc = tree.nodes['Deform Curves on Surface']
up = [l.from_socket for l in tree.links if l.to_node == dc][0]; down = [l.to_socket for l in tree.links if l.from_node == dc][0]
tree.nodes.remove(dc); tree.links.new(up, down)
sd = bpy.data.node_groups.new("Surface Deform", 'GeometryNodeTree')
sd.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'); sd.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
a = sd.nodes.new('NodeGroupInput'); b = sd.nodes.new('NodeGroupOutput'); d = sd.nodes.new('GeometryNodeDeformCurvesOnSurface')
a.location = (-300, 0); d.location = (0, 0); b.location = (300, 0)
sd.links.new(a.outputs[0], d.inputs['Curves']); sd.links.new(d.outputs['Curves'], b.inputs[0])
msd = ob.modifiers.new("Surface Deform", 'NODES'); msd.node_group = sd
# fica por ultimo (regra 8: raiz nao descola na animacao), mas desligado no Edit Mode:
# com guias reais, Deform depois do Interpolate derruba o Edit Mode na 5.2.0/5.2.2
msd.show_in_editmode = False
# arruma a cadeia do groom em linha
order = []; cur = gin
while True:
    nx = [l.to_node for l in tree.links if l.from_node == cur]
    if not nx: break
    cur = nx[0]; order.append(cur)
gin.location = (-300, 0)
for i, nd in enumerate(order): nd.location = (i * 260, 0)
log("MODS", [m.name for m in ob.modifiers], "cadeia", [n.name for n in order])
# 3. conjuntos por posicao da raiz (rosto em -Y)
ys = [cd.points[c.first_point_index].position.y for c in cd.curves]
zs = [cd.points[c.first_point_index].position.z for c in cd.curves]
front = [y < -0.02 for y in ys]; back = [y > 0.03 for y in ys]
cd.attributes.new("Front_Guides_02_R", 'BOOLEAN', 'CURVE').data.foreach_set("value", front)
cd.attributes.new("Back_Guides_01_R", 'BOOLEAN', 'CURVE').data.foreach_set("value", back)
log("CONJUNTOS front", sum(front), "back", sum(back))
# 4. tres node tools, cada um com Identifier proprio
def tool(name, idname, default, kind):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.is_tool = True; ng.is_modifier = False; ng.is_mode_edit = True; ng.is_mode_sculpt = True
    ng.is_type_curve = True; ng.is_type_mesh = False; ng.node_tool_idname = idname
    ng.use_fake_user = True   # sem usuario o grupo nao e salvo no .blend
    ng.description = {"store": "Grava as guias selecionadas num atributo booleano (dominio Spline)",
                      "sel": "Seleciona so as guias do conjunto",
                      "del": "Apaga as guias do conjunto; os atributos ficam"}[kind]
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    s = ng.interface.new_socket("Nome", in_out='INPUT', socket_type='NodeSocketString'); s.default_value = default
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    N = ng.nodes; L = ng.links.new
    gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput'); gi.location = (-520, 0); go.location = (360, 0)
    fr = N.new('NodeFrame'); fr.label = name + "  ·  Identifier: " + idname; fr.label_size = 16; fr.shrink = True
    ng["_frame"] = fr.name
    if kind == "store":
        se = N.new('GeometryNodeToolSelection'); se.location = (-260, -180); se.label = 'Guias selecionadas'
        st = N.new('GeometryNodeStoreNamedAttribute'); st.data_type = 'BOOLEAN'; st.domain = 'CURVE'; st.location = (100, 0)
        L(gi.outputs[0], st.inputs['Geometry']); L(gi.outputs[1], st.inputs['Name'])
        L([o for o in se.outputs if o.type == 'BOOLEAN'][0], st.inputs['Value']); L(st.outputs[0], go.inputs[0])
    else:
        na = N.new('GeometryNodeInputNamedAttribute'); na.data_type = 'BOOLEAN'; na.location = (-260, -180); na.label = 'Conjunto (atributo)'
        L(gi.outputs[1], na.inputs['Name']); attr = [o for o in na.outputs if o.type == 'BOOLEAN'][0]
        if kind == "sel":
            ss = N.new('GeometryNodeToolSetSelection'); ss.domain = 'CURVE'; ss.location = (100, 0)
            L(gi.outputs[0], ss.inputs['Geometry']); L(attr, ss.inputs['Selection']); L(ss.outputs[0], go.inputs[0])
        else:
            sp = N.new('GeometryNodeSeparateGeometry'); sp.domain = 'CURVE'; sp.location = (100, 0)
            L(gi.outputs[0], sp.inputs['Geometry']); L(attr, sp.inputs['Selection']); L(sp.outputs['Inverted'], go.inputs[0]); sp.label = 'Separa: Inverted = o que fica'
def tidy(ng):
    fr = ng.nodes[ng["_frame"]]
    for nd in ng.nodes:
        if nd != fr: nd.parent = fr
    del ng["_frame"]
tool("Salvar Seleção", "curves.salvar_selecao", "Novo_Conjunto", "store")
tool("Selecionar Conjunto", "curves.selecionar_conjunto", "Front_Guides_02_R", "sel")
tool("Apagar Conjunto", "curves.apagar_conjunto", "Front_Guides_02_R", "del")
for nm in ("Salvar Seleção", "Selecionar Conjunto", "Apagar Conjunto"): tidy(bpy.data.node_groups[nm])
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg).data
log("FILHOS avaliados", len(ev.curves))
for o in bpy.context.view_layer.objects: o.select_set(False)
ob.select_set(True); bpy.context.view_layer.objects.active = ob
bpy.ops.wm.save_as_mainfile(filepath=OUTP, compress=True)
log("SALVO", OUTP)
