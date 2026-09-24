import bpy, pathlib, importlib.util, numpy as np
ADDON = str(pathlib.Path(__file__).with_name("__init__.py"))
spec = importlib.util.spec_from_file_location("groom_select", ADDON); gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs); gs.register()

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.mesh.primitive_plane_add()
bpy.ops.object.curves_empty_hair_add()
hair = bpy.context.active_object; cd = hair.data
N = 12
cd.add_curves([4]*N)
b = cd.attributes.new("Top_Guides_01", 'BOOLEAN', 'CURVE'); v = np.zeros(N, bool); v[:4] = True; b.data.foreach_set("value", v)
i = cd.attributes.new("region", 'INT', 'CURVE'); i.data.foreach_set("value", np.array([0,0,1,1,2,2,0,1,2,0,1,2], np.int32))
f = cd.attributes.new("weight", 'FLOAT', 'POINT'); w = np.zeros(N*4, np.float32); w[4*8:4*8+2] = 0.9; f.data.foreach_set("value", w)  # curva 8 tem pontos altos
st = bpy.context.scene.groom_select

def sel_mask(): return gs._current_selection_curve_mask(cd)

# --- modo sculpt (float selection)
bpy.ops.object.mode_set(mode='SCULPT_CURVES')
st.attribute = "Top_Guides_01"
assert bpy.ops.groom_select.by_attribute(mode='SET') == {'FINISHED'}
a = cd.attributes['.selection']; print("sculpt .selection:", a.domain, a.data_type)
assert a.data_type == 'FLOAT'
assert sel_mask().tolist() == v.tolist(), sel_mask()
st.attribute = "region"; st.int_value = 2
bpy.ops.groom_select.by_attribute(mode='ADD')
exp = v | (np.array([0,0,1,1,2,2,0,1,2,0,1,2]) == 2)
assert sel_mask().tolist() == exp.tolist(), sel_mask()
bpy.ops.groom_select.by_attribute(mode='SUB')
assert sel_mask().tolist() == v.tolist()
st.attribute = "weight"; st.float_min = 0.5; st.float_max = 1.0
bpy.ops.groom_select.by_attribute(mode='SET')
m = sel_mask(); assert m.sum() == 1 and m[8], m
# salvar selecao
st.save_name = "Novo_Grupo"
bpy.ops.groom_select.save_selection(mode='SET')
ng = np.empty(N, bool); cd.attributes["Novo_Grupo"].data.foreach_get("value", ng); assert ng.sum() == 1 and ng[8]
st.attribute = "Top_Guides_01"; bpy.ops.groom_select.by_attribute(mode='SET')
bpy.ops.groom_select.save_selection(mode='ADD')
cd.attributes["Novo_Grupo"].data.foreach_get("value", ng); assert ng.sum() == 5, ng
bpy.ops.groom_select.save_selection(mode='SUB')
cd.attributes["Novo_Grupo"].data.foreach_get("value", ng); assert ng.sum() == 1 and ng[8]
bpy.ops.groom_select.all(action='INVERT'); assert sel_mask().sum() == N-4
bpy.ops.groom_select.all(action='NONE'); assert sel_mask().sum() == 0
bpy.ops.groom_select.all(action='ALL'); assert sel_mask().sum() == N
bpy.ops.object.mode_set(mode='OBJECT')

# --- modo edit (bool selection): remove .selection e refaz
cd.attributes.remove(cd.attributes['.selection'])
bpy.ops.object.mode_set(mode='EDIT')
st.attribute = "region"; st.int_value = 1
bpy.ops.groom_select.by_attribute(mode='SET')
a = cd.attributes['.selection']; print("edit .selection:", a.domain, a.data_type)
assert a.data_type == 'BOOLEAN'
assert sel_mask().sum() == 4
bpy.ops.object.mode_set(mode='OBJECT')
# atributos originais intactos
cd.attributes["Top_Guides_01"].data.foreach_get("value", ng); assert ng.tolist() == v.tolist()
print("ALL OK")
