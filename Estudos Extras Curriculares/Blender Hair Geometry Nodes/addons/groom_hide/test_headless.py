import bpy, os, sys, importlib.util, numpy as np
import pathlib
ADDON = str(pathlib.Path(__file__).with_name("__init__.py"))
spec = importlib.util.spec_from_file_location("groom_hide", ADDON); gh = importlib.util.module_from_spec(spec); spec.loader.exec_module(gh); gh.register()

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.mesh.primitive_plane_add(size=2)
surf = bpy.context.active_object
bpy.ops.object.curves_empty_hair_add()
hair = bpy.context.active_object
cd = hair.data
N = 40
cd.add_curves([5]*N)
# positions: guides standing up on a grid, tips leaning by index
pos = np.zeros((N*5,3), dtype=np.float32)
rng = np.random.default_rng(1)
for i in range(N):
    x, y = rng.uniform(-0.9,0.9,2)
    for k in range(5):
        pos[i*5+k] = (x + 0.05*k*i/N, y, 0.1*k)
cd.attributes['position'].data.foreach_set('vector', pos.ravel())
uv = cd.attributes.new('surface_uv_coordinate','FLOAT2','CURVE')
uv.data.foreach_set('vector', ((pos[::5,:2]+1)/2).ravel())
rad = cd.attributes.new('radius','FLOAT','POINT'); rad.data.foreach_set('value', np.linspace(0.001,0.01,N*5))
tag = cd.attributes.new('my_tag','INT','CURVE'); tag.data.foreach_set('value', np.arange(N)*7)
# Interpolate Hair Curves from essentials
assets = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','procedural_hair_node_assets.blend')
with bpy.data.libraries.load(assets, link=False) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n == 'Interpolate Hair Curves']
ng = bpy.data.node_groups['Interpolate Hair Curves']
mod = hair.modifiers.new('Interpolate', 'NODES'); mod.node_group = ng
# set surface + amount
mod['Input_2'] = surf
mod['Input_15'] = 300.0
mod['Input_18_use_attribute'] = True
mod['Input_18_attribute_name'] = 'UVMap'

def ev_count():
    dg = bpy.context.evaluated_depsgraph_get(); return len(hair.evaluated_get(dg).data.curves)
def ev_tip_hash():
    dg = bpy.context.evaluated_depsgraph_get(); e = hair.evaluated_get(dg).data
    p = np.empty(len(e.points)*3, dtype=np.float32); e.attributes['position'].data.foreach_get('vector', p)
    return round(float(np.abs(p).sum()), 3)

before_count, before_hash = ev_count(), ev_tip_hash()
print("children before:", before_count, "orig:", len(cd.curves), "hash:", before_hash)
assert before_count > N, "Interpolate nao gerou filhos"

# select curves 0..9 via point-domain float selection, in sculpt mode
bpy.ops.object.mode_set(mode='SCULPT_CURVES')
sel = cd.attributes.new('.selection','FLOAT','POINT')
v = np.zeros(N*5, dtype=np.float32); v[:10*5] = 1.0; sel.data.foreach_set('value', v)
print("mode:", bpy.context.mode)
r = bpy.ops.groom_hide.hide(unselected=False); print("hide:", r, "mode after:", bpy.context.mode, "orig now:", len(cd.curves))
assert len(cd.curves) == N-10
assert hair.modifiers[0].name == gh.MOD_NAME, [m.name for m in hair.modifiers]
after_count, after_hash = ev_count(), ev_tip_hash()
print("children after hide:", after_count, "hash:", after_hash, "feed:", hair.groom_hide.feed)
assert after_count == before_count, "quantidade de filhos mudou"
assert abs(after_hash - before_hash) < 1e-2, "forma do cabelo mudou"
sets = gh._parked_sets(hair); print("sets:", [(o.name, len(o.data.curves), o.hide_get()) for o in sets])

# hide unselected of the remaining: select curves 0..4 of remaining (curve domain bool via edit mode style)
cd.attributes.remove(cd.attributes['.selection'])
sel = cd.attributes.new('.selection','BOOLEAN','CURVE')
b = np.zeros(len(cd.curves), dtype=bool); b[:5] = True; sel.data.foreach_set('value', b)
r = bpy.ops.groom_hide.hide(unselected=True); print("hide unselected:", r, "orig now:", len(cd.curves))
assert len(cd.curves) == 5
print("children after 2nd hide:", ev_count(), "hash:", ev_tip_hash())
assert ev_count() == before_count and abs(ev_tip_hash()-before_hash) < 1e-2

# feed off -> hidden guides not fed
hair.groom_hide.feed = False
print("feed off children:", ev_count(), "hash:", ev_tip_hash())
assert abs(ev_tip_hash()-before_hash) > 1e-2, "com feed off a forma deveria mudar"
hair.groom_hide.feed = True

# reveal last
r = bpy.ops.groom_hide.reveal(mode='LAST'); print("reveal last:", r, "orig:", len(cd.curves), "sets:", len(gh._parked_sets(hair)))
assert len(cd.curves) == N-10
# reveal all
r = bpy.ops.groom_hide.reveal(mode='ALL'); print("reveal all:", r, "orig:", len(cd.curves), "mode:", bpy.context.mode)
assert len(cd.curves) == N
assert gh.MOD_NAME not in [m.name for m in hair.modifiers]
assert hair.groom_hide.collection is None
assert gh.ATTR_ORDER not in cd.attributes
# check order + attributes restored
t = np.empty(N, dtype=np.int32); cd.attributes['my_tag'].data.foreach_get('value', t)
assert np.array_equal(t, np.arange(N)*7), t
p2 = np.empty(N*5*3, dtype=np.float32); cd.attributes['position'].data.foreach_get('vector', p2)
assert np.allclose(p2.reshape(-1,3), pos), "posicoes mudaram"
r2 = np.empty(N*5, dtype=np.float32); cd.attributes['radius'].data.foreach_get('value', r2)
assert np.allclose(r2, np.linspace(0.001,0.01,N*5))
print("final children:", ev_count(), "hash:", ev_tip_hash())
assert ev_count()==before_count and abs(ev_tip_hash()-before_hash)<1e-2
print("orphans:", [c.name for c in bpy.data.hair_curves], "objects:", [o.name for o in bpy.data.objects])
bpy.ops.object.mode_set(mode='OBJECT')
print("ALL OK")
