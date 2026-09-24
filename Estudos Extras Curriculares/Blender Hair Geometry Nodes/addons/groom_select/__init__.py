# Groom Select — seleciona guias de hair curves por atributo, e salva a
# selecao como atributo. So escreve no atributo ".selection" (e no atributo
# que voce mandar salvar). Nunca move, apaga ou reordena curva.

import bpy
import numpy as np
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty, StringProperty
from bpy.types import Operator, Panel, PropertyGroup

_enum_cache = []   # o Blender exige que as strings do enum continuem vivas


# ----------------------------------------------------------------------------
# Leitura de atributos
# ----------------------------------------------------------------------------

def _curves_obj(context):
    o = context.active_object
    return o if o is not None and o.type == 'CURVES' else None


def _first_points(cd):
    n = len(cd.curves)
    first = np.empty(n, dtype=np.int32)
    cd.curves.foreach_get("first_point_index", first)
    return first


def _point_to_curve_any(cd, point_mask):
    """Curva conta como marcada se qualquer ponto dela estiver marcado."""
    first = _first_points(cd)
    ends = np.append(first[1:], len(cd.points))
    out = np.zeros(len(cd.curves), dtype=bool)
    for i in range(len(cd.curves)):
        if point_mask[first[i]:ends[i]].any():
            out[i] = True
    return out


def _curve_to_point(cd, curve_mask):
    first = _first_points(cd)
    ends = np.append(first[1:], len(cd.points))
    out = np.zeros(len(cd.points), dtype=bool)
    for i in np.nonzero(curve_mask)[0]:
        out[first[i]:ends[i]] = True
    return out


def _read_attr_as_curve_mask(cd, attr, int_value, float_min, float_max):
    """Converte um atributo bool/int/float em mascara por curva."""
    n = len(attr.data)
    if attr.data_type == 'BOOLEAN':
        raw = np.empty(n, dtype=bool)
        attr.data.foreach_get("value", raw)
        mask = raw
    elif attr.data_type in {'INT', 'INT8'}:
        raw = np.empty(n, dtype=np.int32)
        attr.data.foreach_get("value", raw)
        mask = raw == int_value
    elif attr.data_type == 'FLOAT':
        raw = np.empty(n, dtype=np.float32)
        attr.data.foreach_get("value", raw)
        mask = (raw >= float_min) & (raw <= float_max)
    else:
        return None
    if attr.domain == 'CURVE':
        return mask
    if attr.domain == 'POINT':
        return _point_to_curve_any(cd, mask)
    return None


def _current_selection_curve_mask(cd):
    attr = cd.attributes.get(".selection")
    if attr is None:
        # sem atributo, o Blender trata tudo como selecionado
        return np.ones(len(cd.curves), dtype=bool)
    n = len(attr.data)
    if attr.data_type == 'BOOLEAN':
        raw = np.empty(n, dtype=bool)
        attr.data.foreach_get("value", raw)
        mask = raw
    else:
        raw = np.empty(n, dtype=np.float32)
        attr.data.foreach_get("value", raw)
        mask = raw > 0.0
    if attr.domain == 'CURVE':
        return mask
    return _point_to_curve_any(cd, mask)


def _write_selection(context, cd, curve_mask):
    """Escreve a mascara por curva no atributo .selection, no tipo e dominio
    certos para o modo atual (sculpt usa float, edit usa bool)."""
    attr = cd.attributes.get(".selection")
    if attr is None:
        want_type = 'BOOLEAN' if context.mode == 'EDIT_CURVES' else 'FLOAT'
        domain = cd.selection_domain if cd.selection_domain in {'POINT', 'CURVE'} else 'POINT'
        attr = cd.attributes.new(".selection", want_type, domain)
    mask = curve_mask if attr.domain == 'CURVE' else _curve_to_point(cd, curve_mask)
    if attr.data_type == 'BOOLEAN':
        attr.data.foreach_set("value", mask.astype(bool))
    else:
        attr.data.foreach_set("value", mask.astype(np.float32))
    cd.update_tag()
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()


# ----------------------------------------------------------------------------
# Estado do painel
# ----------------------------------------------------------------------------

def _attr_items(self, context):
    _enum_cache.clear()
    obj = _curves_obj(context)
    if obj is None:
        _enum_cache.append(("NONE", "(sem objeto de curvas)", ""))
        return _enum_cache
    for a in obj.data.attributes:
        if a.name.startswith(".") or a.name in {"position", "radius", "surface_uv_coordinate"}:
            continue
        if a.data_type not in {'BOOLEAN', 'INT', 'INT8', 'FLOAT'}:
            continue
        if a.domain not in {'CURVE', 'POINT'}:
            continue
        dom = "curva" if a.domain == 'CURVE' else "ponto"
        typ = {'BOOLEAN': "bool", 'INT': "int", 'INT8': "int", 'FLOAT': "float"}[a.data_type]
        _enum_cache.append((a.name, f"{a.name}  ({typ}, {dom})", ""))
    if not _enum_cache:
        _enum_cache.append(("NONE", "(nenhum atributo bool/int/float)", ""))
    return _enum_cache


class GroomSelectSettings(PropertyGroup):
    attribute: EnumProperty(name="Atributo", items=_attr_items)
    int_value: IntProperty(name="Valor", default=1, description="Para atributo inteiro: seleciona curvas com este valor")
    float_min: FloatProperty(name="Min", default=0.5, soft_min=0.0, soft_max=1.0, description="Para atributo float: valor minimo")
    float_max: FloatProperty(name="Max", default=1.0, soft_min=0.0, soft_max=1.0, description="Para atributo float: valor maximo")
    save_name: StringProperty(name="Nome", default="Guias_01", description="Nome do atributo booleano a criar ou atualizar")


# ----------------------------------------------------------------------------
# Operadores
# ----------------------------------------------------------------------------

_MODES = [
    ('SET', "Selecionar", "Substitui a selecao atual"),
    ('ADD', "Adicionar", "Une com a selecao atual"),
    ('SUB', "Remover", "Tira da selecao atual"),
    ('AND', "Só nesses", "Mantem so o que esta nos dois"),
]


class GROOMSELECT_OT_select_by_attribute(Operator):
    bl_idname = "groom_select.by_attribute"
    bl_label = "Selecionar por atributo"
    bl_description = "Seleciona as guias marcadas no atributo escolhido"
    bl_options = {'REGISTER', 'UNDO'}

    mode: EnumProperty(name="Modo", items=_MODES, default='SET')

    @classmethod
    def poll(cls, context):
        return _curves_obj(context) is not None

    def execute(self, context):
        obj = _curves_obj(context)
        cd = obj.data
        st = context.scene.groom_select
        attr = cd.attributes.get(st.attribute)
        if attr is None:
            self.report({'WARNING'}, "Escolha um atributo")
            return {'CANCELLED'}
        mask = _read_attr_as_curve_mask(cd, attr, st.int_value, st.float_min, st.float_max)
        if mask is None:
            self.report({'WARNING'}, f"Atributo {attr.name} nao e bool, int ou float por curva/ponto")
            return {'CANCELLED'}
        if self.mode == 'ADD':
            mask = _current_selection_curve_mask(cd) | mask
        elif self.mode == 'SUB':
            mask = _current_selection_curve_mask(cd) & ~mask
        elif self.mode == 'AND':
            mask = _current_selection_curve_mask(cd) & mask
        _write_selection(context, cd, mask)
        self.report({'INFO'}, f"{int(mask.sum())} de {len(cd.curves)} guia(s) selecionada(s)")
        return {'FINISHED'}


class GROOMSELECT_OT_save_selection(Operator):
    bl_idname = "groom_select.save_selection"
    bl_label = "Salvar seleção como atributo"
    bl_description = "Grava a selecao atual num atributo booleano por curva"
    bl_options = {'REGISTER', 'UNDO'}

    mode: EnumProperty(
        name="Modo",
        items=[
            ('SET', "Substituir", "O atributo passa a ser exatamente a selecao atual"),
            ('ADD', "Adicionar", "Marca as guias selecionadas, mantendo as que ja estavam"),
            ('SUB', "Remover", "Desmarca as guias selecionadas"),
        ],
        default='SET',
    )

    @classmethod
    def poll(cls, context):
        return _curves_obj(context) is not None

    def execute(self, context):
        obj = _curves_obj(context)
        cd = obj.data
        st = context.scene.groom_select
        name = st.save_name.strip()
        if not name or name.startswith("."):
            self.report({'WARNING'}, "De um nome ao atributo")
            return {'CANCELLED'}
        sel = _current_selection_curve_mask(cd)
        if cd.attributes.get(".selection") is None:
            self.report({'WARNING'}, "Nada selecionado ainda. Selecione guias primeiro")
            return {'CANCELLED'}
        attr = cd.attributes.get(name)
        if attr is not None and (attr.domain != 'CURVE' or attr.data_type != 'BOOLEAN'):
            self.report({'WARNING'}, f"'{name}' ja existe e nao e booleano por curva. Use outro nome")
            return {'CANCELLED'}
        if attr is None:
            attr = cd.attributes.new(name, 'BOOLEAN', 'CURVE')
            old = np.zeros(len(cd.curves), dtype=bool)
        else:
            old = np.empty(len(cd.curves), dtype=bool)
            attr.data.foreach_get("value", old)
        if self.mode == 'SET':
            new = sel
        elif self.mode == 'ADD':
            new = old | sel
        else:
            new = old & ~sel
        attr.data.foreach_set("value", new)
        cd.update_tag()
        self.report({'INFO'}, f"'{name}': {int(new.sum())} guia(s) marcada(s)")
        return {'FINISHED'}


class GROOMSELECT_OT_all(Operator):
    bl_idname = "groom_select.all"
    bl_label = "Selecionar tudo / nada / inverter"
    bl_options = {'REGISTER', 'UNDO'}

    action: EnumProperty(items=[('ALL', "Tudo", ""), ('NONE', "Nada", ""), ('INVERT', "Inverter", "")], default='ALL')

    @classmethod
    def poll(cls, context):
        return _curves_obj(context) is not None

    def execute(self, context):
        cd = _curves_obj(context).data
        if self.action == 'ALL':
            mask = np.ones(len(cd.curves), dtype=bool)
        elif self.action == 'NONE':
            mask = np.zeros(len(cd.curves), dtype=bool)
        else:
            mask = ~_current_selection_curve_mask(cd)
        _write_selection(context, cd, mask)
        return {'FINISHED'}


# ----------------------------------------------------------------------------
# Painel
# ----------------------------------------------------------------------------

class GROOMSELECT_PT_panel(Panel):
    bl_label = "Groom Select"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Groom"

    @classmethod
    def poll(cls, context):
        return _curves_obj(context) is not None

    def draw(self, context):
        layout = self.layout
        st = context.scene.groom_select
        cd = _curves_obj(context).data

        box = layout.box()
        box.label(text="Selecionar por atributo", icon='RESTRICT_SELECT_OFF')
        box.prop(st, "attribute", text="")
        attr = cd.attributes.get(st.attribute)
        if attr is not None:
            if attr.data_type in {'INT', 'INT8'}:
                box.prop(st, "int_value")
            elif attr.data_type == 'FLOAT':
                row = box.row(align=True)
                row.prop(st, "float_min")
                row.prop(st, "float_max")
        col = box.column(align=True)
        col.operator("groom_select.by_attribute", text="Selecionar").mode = 'SET'
        row = col.row(align=True)
        row.operator("groom_select.by_attribute", text="Adicionar").mode = 'ADD'
        row.operator("groom_select.by_attribute", text="Remover").mode = 'SUB'
        row.operator("groom_select.by_attribute", text="Só nesses").mode = 'AND'

        box = layout.box()
        box.label(text="Salvar seleção como atributo", icon='FILE_TICK')
        box.prop(st, "save_name", text="")
        col = box.column(align=True)
        col.operator("groom_select.save_selection", text="Substituir").mode = 'SET'
        row = col.row(align=True)
        row.operator("groom_select.save_selection", text="Adicionar").mode = 'ADD'
        row.operator("groom_select.save_selection", text="Remover").mode = 'SUB'

        row = layout.row(align=True)
        row.operator("groom_select.all", text="Tudo").action = 'ALL'
        row.operator("groom_select.all", text="Nada").action = 'NONE'
        row.operator("groom_select.all", text="Inverter").action = 'INVERT'

        sel = _current_selection_curve_mask(cd)
        layout.label(text=f"{int(sel.sum())} de {len(cd.curves)} guias selecionadas")


# ----------------------------------------------------------------------------
# Registro
# ----------------------------------------------------------------------------

classes = (
    GroomSelectSettings,
    GROOMSELECT_OT_select_by_attribute,
    GROOMSELECT_OT_save_selection,
    GROOMSELECT_OT_all,
    GROOMSELECT_PT_panel,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.groom_select = bpy.props.PointerProperty(type=GroomSelectSettings)


def unregister():
    del bpy.types.Scene.groom_select
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
