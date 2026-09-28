import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.20, gravity=3.0, spread=0.3, outward=0.4, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
scalp.hide_render = False; sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.12,0.05,0.03,1); scalp.data.materials.append(sm_)
# malha da crista: elipsoide fino e alto
me = bpy.data.meshes.new("crista"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=1.0)
bmesh.ops.scale(bm, vec=(0.03,0.16,0.20), verts=bm.verts); bmesh.ops.translate(bm, vec=(0,0.02,0.10), verts=bm.verts); bm.to_mesh(me); bm.free()
cr_ = link(bpy.data.objects.new("crista", me)); cr_.hide_render = True
t = Tree("mo")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 350000.0}); t.chain(d); base = t.geo
mk = grp("GR Máscara por Posição", **{"Lateral máx (|X|)": 0.018, "Altura mín": 0.02, "Borda suave": 0.006})
# A: raspado (4 mm)
tA = grp("GR Corte por Região") if False else None
trA = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); trA.inputs['Replace Length'].default_value = True; trA.inputs['Length'].default_value = 0.006; t.link(base, trA.inputs['Geometry'])
wA = t.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves']); wA.inputs['Offset Distance'].default_value = 0.002; wA.inputs['Above Surface'].default_value = 0.0; wA.inputs['Lock Roots'].default_value = True; t.link(trA.outputs[0], wA.inputs['Geometry'])
for q in wA.inputs:
    if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
# B: crista ate a malha
cb = grp("GR Comprimento até a Malha", **{"Malha da forma": cr_, "Viés": (0,0,0.8), "Pontos": 12}); t.link(base, cb.inputs[0])
rsA = t.add('GeometryNodeResampleCurve'); rsA.inputs['Count'].default_value = 12; t.link(wA.outputs[0], rsA.inputs['Curve'])
ms = grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.015}); t.link(cb.outputs[0], ms.inputs[0])
tr = grp("GR Transição"); t.link(rsA.outputs[0], tr.inputs[0]); t.link(ms.outputs[0], tr.inputs[1]); t.link(mk.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
profile(t, EG, radius=0.0005)
m = bpy.data.materials.new("m"); b = m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value = (0.02,0.25,0.06,1); b.inputs['Roughness'].default_value = 0.4
set_mat(t, m); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
shot("93_moicano", res=460, samples=20, cam_loc=(0.55,-0.45,0.12), target=(0,0,0.04), lens=42)
