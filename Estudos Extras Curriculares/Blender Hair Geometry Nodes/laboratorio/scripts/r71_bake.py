import sys; sys.path.insert(0,'.')
from lab import *
LIB = os.path.join(LAB, "receitas_grooming.blend")
MODE = sys.argv[-1]   # sem | bake
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("bk")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
grp("GR Flutuar", Amplitude=0.08)
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 300000.0})
grp("GR Mecha Estilizada"); grp("GR Cacho por Mecha"); grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005)
if MODE == "bake":
    bk = t.add('GeometryNodeBake'); bk.bake_items.new('GEOMETRY', 'Geometry'); t.chain(bk, 'Geometry', 'Geometry')
m = apply_tree(g, t.finish())
sc = bpy.context.scene; sc.frame_start = 1; sc.frame_end = 12
if MODE == "bake":
    m.bake_directory = os.path.join(OUT, "bake_cache"); m.bake_target = 'DISK'
    b = m.bakes[0]; b.bake_mode = 'ANIMATION'; b.use_custom_simulation_frame_range = True; b.frame_start = 1; b.frame_end = 12
    bpy.context.view_layer.objects.active = g; g.select_set(True)
    t0 = time.time()
    with bpy.context.temp_override(object=g, active_object=g, selected_objects=[g]):
        r = bpy.ops.object.geometry_node_bake_single(session_uid=g.session_uid, modifier_name=m.name, bake_id=b.bake_id)
    print("BAKE", r, round(time.time()-t0,1), "s para", sc.frame_end, "quadros")
    sz = sum(os.path.getsize(os.path.join(dp,f)) for dp,_,fs in os.walk(m.bake_directory) for f in fs); print("BAKE tamanho MB", round(sz/1e6,1))
ts=[]
for f in range(1, 13):
    t0 = time.time(); sc.frame_set(f); d_ = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    import numpy as np; P_ = np.zeros(len(d_.points)*3, np.float32); d_.attributes['position'].data.foreach_get('vector', P_); ts.append(time.time()-t0)
    if f in (2, 11): print("POS", MODE, f, round(float(P_[::997].sum()),3))
print("PLAY", MODE, "ms por quadro (media 2..12):", round(sum(ts[1:])/len(ts[1:])*1000), "pontos", stats(g).get('points'))
