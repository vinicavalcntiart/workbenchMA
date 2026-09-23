# Groom Hide — esconde guias de hair curves enquanto voce faz grooming.
#
# Como funciona por dentro:
#   O modo Sculpt Curves desenha as guias originais como "cage" por cima do
#   resultado avaliado, e nenhum modificador consegue filtrar esse cage. Entao
#   esconder de verdade significa tirar as curvas do objeto. Este addon move as
#   guias escondidas para um objeto irmao oculto ("estacionamento") e, para o
#   cabelo nao mudar de forma, um modificador de Geometry Nodes no topo da stack
#   injeta essas guias de volta na avaliacao, na ordem original. O Interpolate
#   continua vendo todas as guias, os filhos ficam identicos, e o cage so mostra
#   o que voce quer pentear.
#
#   Ao revelar, as guias voltam para o objeto e a ordem original das curvas e
#   restaurada, para nao mudar seeds que dependem de indice.

import bpy
import numpy as np
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty
from bpy.types import Operator, Panel, PropertyGroup

ATTR_ORDER = "groom_hide_order"          # indice original de cada curva (curve domain, int)
MOD_NAME = "Groom Hide (guias ocultas)"
NODEGROUP_NAME = "GroomHide.FeedHiddenGuides"
FEED_INPUT = "Alimentar interpolacao"


# ----------------------------------------------------------------------------
# Estado guardado nos objetos
# ----------------------------------------------------------------------------

class GroomHideObjectState(PropertyGroup):
    owner: PointerProperty(type=bpy.types.Object, name="Dono")
    order: IntProperty(name="Ordem", default=0)
    collection: PointerProperty(type=bpy.types.Collection, name="Colecao de guias ocultas")
    feed: BoolProperty(
        name=FEED_INPUT,
        description=(
            "Injeta as guias ocultas de volta na avaliacao (antes do Interpolate), "
            "para os filhos nao mudarem. Desligue se o objeto nao gera filhos, "
            "senao as guias ocultas continuam aparecendo no resultado avaliado"
        ),
        default=True,
        update=lambda self, ctx: _sync_feed(self.id_data),
    )


def _is_owner(obj):
    return obj is not None and obj.type == 'CURVES' and obj.groom_hide.owner is None


def _parked_sets(owner):
    """Objetos de estacionamento deste dono, do mais antigo ao mais recente."""
    col = owner.groom_hide.collection
    if col is None:
        return []
    sets = [o for o in col.objects if o.groom_hide.owner == owner]
    sets.sort(key=lambda o: o.groom_hide.order)
    return sets


# ----------------------------------------------------------------------------
# Selecao
# ----------------------------------------------------------------------------

def _curve_offsets(cd):
    n = len(cd.curves)
    first = np.empty(n, dtype=np.int32)
    cd.curves.foreach_get("first_point_index", first)
    return first


def _selected_curves_mask(cd):
    """Mascara booleana por curva. None se nao ha atributo de selecao."""
    attr = cd.attributes.get(".selection")
    if attr is None:
        return None
    n_curves = len(cd.curves)
    n_points = len(cd.points)
    if attr.data_type == 'BOOLEAN':
        raw = np.empty(len(attr.data), dtype=bool)
        attr.data.foreach_get("value", raw)
        sel = raw
    else:  # FLOAT (modo sculpt usa selecao suave 0..1)
        raw = np.empty(len(attr.data), dtype=np.float32)
        attr.data.foreach_get("value", raw)
        sel = raw > 0.0
    if attr.domain == 'CURVE':
        return sel[:n_curves]
    # ponto -> curva: uma curva conta como selecionada se qualquer ponto estiver
    first = _curve_offsets(cd)
    ends = np.append(first[1:], n_points)
    out = np.zeros(n_curves, dtype=bool)
    for i in range(n_curves):
        if sel[first[i]:ends[i]].any():
            out[i] = True
    return out


# ----------------------------------------------------------------------------
# Ordem original
# ----------------------------------------------------------------------------

def _ensure_order_attr(cd):
    attr = cd.attributes.get(ATTR_ORDER)
    if attr is None:
        attr = cd.attributes.new(ATTR_ORDER, 'INT', 'CURVE')
        attr.data.foreach_set("value", np.arange(len(cd.curves), dtype=np.int32))
    return attr


def _restore_order(cd):
    attr = cd.attributes.get(ATTR_ORDER)
    if attr is None:
        return
    order = np.empty(len(cd.curves), dtype=np.int32)
    attr.data.foreach_get("value", order)
    new_indices = np.argsort(order, kind="stable").astype(np.int32)
    if not np.array_equal(new_indices, np.arange(len(new_indices))):
        cd.reorder_curves(new_indices=new_indices.tolist())


# ----------------------------------------------------------------------------
# Colecao de estacionamento e modificador
# ----------------------------------------------------------------------------

def _find_layer_collection(layer_col, col):
    if layer_col.collection == col:
        return layer_col
    for child in layer_col.children:
        found = _find_layer_collection(child, col)
        if found:
            return found
    return None


def _ensure_collection(context, owner):
    st = owner.groom_hide
    if st.collection is not None:
        return st.collection
    col = bpy.data.collections.new(f"{owner.name} · guias ocultas")
    col.hide_render = True
    context.scene.collection.children.link(col)
    lc = _find_layer_collection(context.view_layer.layer_collection, col)
    if lc:
        lc.hide_viewport = True
    st.collection = col
    return col


def _build_nodegroup():
    ng = bpy.data.node_groups.get(NODEGROUP_NAME)
    if ng is not None:
        return ng
    ng = bpy.data.node_groups.new(NODEGROUP_NAME, 'GeometryNodeTree')
    ng.is_modifier = True
    iface = ng.interface
    iface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    iface.new_socket("Colecao", in_out='INPUT', socket_type='NodeSocketCollection')
    feed = iface.new_socket(FEED_INPUT, in_out='INPUT', socket_type='NodeSocketBool')
    feed.default_value = True
    iface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')

    n_in = ng.nodes.new('NodeGroupInput')
    n_out = ng.nodes.new('NodeGroupOutput')
    n_col = ng.nodes.new('GeometryNodeCollectionInfo')
    n_col.transform_space = 'RELATIVE'
    n_col.inputs["Separate Children"].default_value = False
    n_real = ng.nodes.new('GeometryNodeRealizeInstances')
    n_join = ng.nodes.new('GeometryNodeJoinGeometry')
    n_attr = ng.nodes.new('GeometryNodeInputNamedAttribute')
    n_attr.data_type = 'INT'
    n_attr.inputs["Name"].default_value = ATTR_ORDER
    n_sort = ng.nodes.new('GeometryNodeSortElements')
    n_sort.domain = 'CURVE'
    n_switch = ng.nodes.new('GeometryNodeSwitch')
    n_switch.input_type = 'GEOMETRY'

    n_in.location = (-800, 0)
    n_col.location = (-600, -200)
    n_real.location = (-400, -200)
    n_join.location = (-200, 0)
    n_attr.location = (-200, -250)
    n_sort.location = (50, 0)
    n_switch.location = (300, 0)
    n_out.location = (500, 0)

    links = ng.links
    links.new(n_in.outputs["Colecao"], n_col.inputs["Collection"])
    links.new(n_col.outputs["Instances"], n_real.inputs["Geometry"])
    # Join Geometry: o primeiro link e o primeiro na ordem de saida.
    links.new(n_in.outputs["Geometry"], n_join.inputs[0])
    links.new(n_real.outputs["Geometry"], n_join.inputs[0])
    # Reordena pelo indice original para a avaliacao ficar identica a de antes.
    links.new(n_join.outputs["Geometry"], n_sort.inputs["Geometry"])
    links.new(n_attr.outputs["Attribute"], n_sort.inputs["Sort Weight"])
    links.new(n_in.outputs[FEED_INPUT], n_switch.inputs["Switch"])
    links.new(n_in.outputs["Geometry"], n_switch.inputs["False"])
    links.new(n_sort.outputs["Geometry"], n_switch.inputs["True"])
    links.new(n_switch.outputs["Output"], n_out.inputs["Geometry"])
    return ng


def _socket_id(ng, name):
    for item in ng.interface.items_tree:
        if item.item_type == 'SOCKET' and item.in_out == 'INPUT' and item.name == name:
            return item.identifier
    return None


def _ensure_modifier(owner, col):
    mod = owner.modifiers.get(MOD_NAME)
    ng = _build_nodegroup()
    if mod is None:
        mod = owner.modifiers.new(MOD_NAME, 'NODES')
        mod.node_group = ng
        mod.show_expanded = False
    mod[_socket_id(ng, "Colecao")] = col
    mod[_socket_id(ng, FEED_INPUT)] = owner.groom_hide.feed
    idx = list(owner.modifiers).index(mod)
    if idx != 0:
        with bpy.context.temp_override(object=owner):
            bpy.ops.object.modifier_move_to_index(modifier=mod.name, index=0)
    return mod


def _sync_feed(owner):
    mod = owner.modifiers.get(MOD_NAME) if owner else None
    if mod and mod.node_group:
        mod[_socket_id(mod.node_group, FEED_INPUT)] = owner.groom_hide.feed
        owner.update_tag()


def _remove_modifier(owner):
    mod = owner.modifiers.get(MOD_NAME)
    if mod:
        owner.modifiers.remove(mod)


def _generates_children(context, owner):
    """Heuristica: se a avaliacao tem mais curvas que o original, ha filhos."""
    dg = context.evaluated_depsgraph_get()
    ev = owner.evaluated_get(dg)
    try:
        return len(ev.data.curves) > len(owner.data.curves)
    except Exception:
        return True


# ----------------------------------------------------------------------------
# Troca de modo
# ----------------------------------------------------------------------------

class _ObjectModeScope:
    """Entra em modo objeto para mexer nos dados e volta ao modo anterior."""

    def __init__(self, context, obj):
        self.context = context
        self.obj = obj
        self.mode = context.mode

    def __enter__(self):
        if self.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        return self

    def __exit__(self, *exc):
        vl = self.context.view_layer
        vl.objects.active = self.obj
        self.obj.select_set(True)
        if self.mode == 'SCULPT_CURVES':
            bpy.ops.object.mode_set(mode='SCULPT_CURVES')
        elif self.mode == 'EDIT_CURVES':
            bpy.ops.object.mode_set(mode='EDIT')
        return False


# ----------------------------------------------------------------------------
# Operacoes de fundo
# ----------------------------------------------------------------------------

def _park_curves(context, owner, hide_mask):
    """Move as curvas marcadas em hide_mask para um novo objeto estacionado."""
    cd = owner.data
    _ensure_order_attr(cd)
    hide_idx = np.nonzero(hide_mask)[0].tolist()
    keep_idx = np.nonzero(~hide_mask)[0].tolist()

    col = _ensure_collection(context, owner)
    order = 1 + max((o.groom_hide.order for o in _parked_sets(owner)), default=0)

    park = owner.copy()
    park.data = cd.copy()
    park.name = f"{owner.name}.oculto.{order:03d}"
    park.data.name = park.name
    for m in list(park.modifiers):
        park.modifiers.remove(m)
    park.groom_hide.owner = owner
    park.groom_hide.order = order
    park.groom_hide.collection = None
    for c in list(park.users_collection):
        c.objects.unlink(park)
    col.objects.link(park)
    park.hide_render = True
    park.hide_select = True
    park.hide_set(True)

    park.data.remove_curves(indices=keep_idx)
    cd.remove_curves(indices=hide_idx)

    if owner.modifiers.get(MOD_NAME) is None:
        owner.groom_hide.feed = _generates_children(context, owner)
    _ensure_modifier(owner, col)
    return park, len(hide_idx)


def _unpark(context, owner, sets):
    """Junta os objetos estacionados de volta ao dono e limpa o que sobrou."""
    if not sets:
        return 0
    count = sum(len(o.data.curves) for o in sets)
    col = owner.groom_hide.collection

    # Objetos numa colecao escondida nao podem ser selecionados, entao eles
    # voltam para a colecao do dono antes do join.
    home = owner.users_collection[0] if owner.users_collection else context.scene.collection
    for o in context.view_layer.objects:
        o.select_set(False)
    for o in sets:
        for c in list(o.users_collection):
            c.objects.unlink(o)
        home.objects.link(o)
        o.hide_set(False)
        o.hide_select = False
        o.select_set(True)
    owner.select_set(True)
    context.view_layer.objects.active = owner
    names = [o.name for o in sets]
    bpy.ops.object.join()
    leftovers = [n for n in names if n in bpy.data.objects]
    if leftovers:
        raise RuntimeError("join nao juntou: " + ", ".join(leftovers))

    # join apaga os objetos, mas as curves datablocks ficam orfas
    prefix = owner.name + ".oculto."
    for cdb in [c for c in bpy.data.hair_curves if c.users == 0 and c.name.startswith(prefix)]:
        bpy.data.hair_curves.remove(cdb)

    _restore_order(owner.data)
    if not _parked_sets(owner):
        attr = owner.data.attributes.get(ATTR_ORDER)
        if attr:
            owner.data.attributes.remove(attr)
        _remove_modifier(owner)
        if col is not None:
            bpy.data.collections.remove(col)
        owner.groom_hide.collection = None
    return count


# ----------------------------------------------------------------------------
# Operadores
# ----------------------------------------------------------------------------

class GROOMHIDE_OT_hide(Operator):
    bl_idname = "groom_hide.hide"
    bl_label = "Esconder guias"
    bl_description = "Esconde as guias selecionadas (ou as nao selecionadas) sem mudar o cabelo gerado"
    bl_options = {'REGISTER', 'UNDO'}

    unselected: BoolProperty(name="Esconder as nao selecionadas", default=False)

    @classmethod
    def poll(cls, context):
        return _is_owner(context.active_object) and context.mode in {'SCULPT_CURVES', 'EDIT_CURVES', 'OBJECT'}

    def execute(self, context):
        owner = context.active_object
        mask = _selected_curves_mask(owner.data)
        if mask is None:
            self.report({'WARNING'}, "Nada selecionado" if not self.unselected else "Nao ha guias nao selecionadas")
            return {'CANCELLED'}
        if self.unselected:
            mask = ~mask
        if not mask.any():
            self.report({'WARNING'}, "Nenhuma guia para esconder")
            return {'CANCELLED'}
        if mask.all():
            self.report({'WARNING'}, "Isso esconderia todas as guias. Deixe pelo menos uma")
            return {'CANCELLED'}
        with _ObjectModeScope(context, owner):
            _, n = _park_curves(context, owner, mask)
        self.report({'INFO'}, f"{n} guia(s) escondida(s)")
        return {'FINISHED'}


class GROOMHIDE_OT_reveal(Operator):
    bl_idname = "groom_hide.reveal"
    bl_label = "Revelar guias"
    bl_description = "Traz as guias escondidas de volta"
    bl_options = {'REGISTER', 'UNDO'}

    mode: EnumProperty(
        name="Modo",
        items=[
            ('ALL', "Todas", "Revela todas as guias escondidas"),
            ('LAST', "Ultimo conjunto", "Revela so o ultimo conjunto escondido"),
            ('INDEX', "Conjunto", "Revela o conjunto de indice dado"),
        ],
        default='ALL',
    )
    index: IntProperty(name="Conjunto", default=0)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return _is_owner(obj) and bool(_parked_sets(obj)) and context.mode in {'SCULPT_CURVES', 'EDIT_CURVES', 'OBJECT'}

    def execute(self, context):
        owner = context.active_object
        sets = _parked_sets(owner)
        if self.mode == 'LAST':
            sets = sets[-1:]
        elif self.mode == 'INDEX':
            sets = [o for o in sets if o.groom_hide.order == self.index]
        if not sets:
            self.report({'WARNING'}, "Nenhum conjunto para revelar")
            return {'CANCELLED'}
        with _ObjectModeScope(context, owner):
            n = _unpark(context, owner, sets)
        self.report({'INFO'}, f"{n} guia(s) revelada(s)")
        return {'FINISHED'}


# ----------------------------------------------------------------------------
# Interface
# ----------------------------------------------------------------------------

class GROOMHIDE_PT_panel(Panel):
    bl_label = "Groom Hide"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Groom"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj is not None and obj.type == 'CURVES'

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        if obj.groom_hide.owner is not None:
            layout.label(text="Este e um conjunto de guias ocultas.", icon='HIDE_ON')
            layout.label(text=f"Dono: {obj.groom_hide.owner.name}")
            return

        col = layout.column(align=True)
        col.operator("groom_hide.hide", text="Esconder selecionadas", icon='HIDE_ON').unselected = False
        col.operator("groom_hide.hide", text="Esconder nao selecionadas", icon='HIDE_ON').unselected = True

        sets = _parked_sets(obj)
        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("groom_hide.reveal", text="Revelar ultimo", icon='HIDE_OFF').mode = 'LAST'
        row.operator("groom_hide.reveal", text="Revelar todas", icon='HIDE_OFF').mode = 'ALL'

        if sets:
            box = layout.box()
            total = 0
            for o in sets:
                n = len(o.data.curves)
                total += n
                row = box.row(align=True)
                row.label(text=f"Conjunto {o.groom_hide.order}: {n} guia(s)")
                op = row.operator("groom_hide.reveal", text="", icon='HIDE_OFF')
                op.mode = 'INDEX'
                op.index = o.groom_hide.order
            box.label(text=f"{total} guia(s) escondida(s), {len(obj.data.curves)} visiveis")
            layout.prop(obj.groom_hide, "feed")
        else:
            layout.label(text=f"{len(obj.data.curves)} guia(s), nenhuma escondida")

        layout.separator()
        layout.label(text="Atalhos: H, Shift+H, Alt+H", icon='EVENT_H')


# ----------------------------------------------------------------------------
# Atalhos
# ----------------------------------------------------------------------------

_keymaps = []


def _register_keymaps():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc is None:
        return
    for km_name in ("Sculpt Curves", "Curves"):
        km = kc.keymaps.new(name=km_name, space_type='EMPTY')
        kmi = km.keymap_items.new("groom_hide.hide", 'H', 'PRESS')
        kmi.properties.unselected = False
        _keymaps.append((km, kmi))
        kmi = km.keymap_items.new("groom_hide.hide", 'H', 'PRESS', shift=True)
        kmi.properties.unselected = True
        _keymaps.append((km, kmi))
        kmi = km.keymap_items.new("groom_hide.reveal", 'H', 'PRESS', alt=True)
        kmi.properties.mode = 'ALL'
        _keymaps.append((km, kmi))


def _unregister_keymaps():
    for km, kmi in _keymaps:
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    _keymaps.clear()


# ----------------------------------------------------------------------------
# Registro
# ----------------------------------------------------------------------------

classes = (
    GroomHideObjectState,
    GROOMHIDE_OT_hide,
    GROOMHIDE_OT_reveal,
    GROOMHIDE_PT_panel,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Object.groom_hide = PointerProperty(type=GroomHideObjectState)
    _register_keymaps()


def unregister():
    _unregister_keymaps()
    del bpy.types.Object.groom_hide
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
