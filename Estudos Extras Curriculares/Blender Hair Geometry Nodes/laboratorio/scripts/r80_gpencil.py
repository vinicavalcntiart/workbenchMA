import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import math, random
V = sys.argv[-1]   # tracos | groom
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
# "desenho": 14 tracos com raiz no couro e onda em S (como o artista faria com Surface placement)
gp = bpy.data.grease_pencils.new("tracos"); L_ = gp.layers.new("cabelo"); fr = L_.frames.new(1); dr = fr.drawing
rnd = random.Random(3); NPT = 16; strokes = []
roots = []
for i in range(14):
    a = -math.pi*0.9 + i*(1.8*math.pi/13)         # em volta da cabeca
    el = math.radians(55 if i%2 else 35)
    r0 = Vector((math.sin(a)*math.cos(el), math.cos(a)*math.cos(el)*1.0, math.sin(el)))*0.101
    if r0.y < -0.06: r0.y = -0.06 + 0.0*r0.y
    roots.append(r0)
dr.add_strokes([NPT]*len(roots))
for s, r0 in zip(dr.strokes, roots):
    side = Vector((r0.x, r0.y, 0)).normalized()
    for j, p in enumerate(s.points):
        t = j/(NPT-1)
        pos = r0 + r0.normalized()*0.02*t + side*0.04*t + Vector((0,0.03,0))*t - Vector((0,0,0.26))*t*t
        pos += side.cross(Vector((0,0,1))).normalized()*0.015*math.sin(t*2*math.pi*1.5)*t
        if pos.length < 0.104: pos = pos.normalized()*0.104
        p.position = pos; p.radius = 0.002
gpo = link(bpy.data.objects.new("tracos", gp))
cd = bpy.data.hair_curves.new("cabelo"); g = link(bpy.data.objects.new("cabelo", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("gp")
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = gpo
g2c = t.add('GeometryNodeGreasePencilToCurves'); t.link(oi.outputs['Geometry'], g2c.inputs['Grease Pencil']); g2c.inputs['Layers as Instances'].default_value = False
rl = t.add('GeometryNodeRealizeInstances'); t.link(g2c.outputs['Curves'], rl.inputs[0])
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 16; t.link(rl.outputs[0], rs.inputs['Curve'])
t.geo = rs.outputs['Curve']
MODE = sys.argv[-2] if len(sys.argv) > 2 else "nada"
if MODE in ("set", "set_attach"):
    sa = t.add('GeometryNodeGroup', group=EG['Set Attachment Surface']); t.chain(sa)
    sa.inputs['Surface Object'].default_value = scalp
    uvn = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); uvn.inputs['Name'].default_value = 'UVMap'; t.link(uvn.outputs['Attribute'], sa.inputs['Surface UV Map'])
if MODE in ("attach", "set_attach"):
    at = t.add('GeometryNodeGroup', group=EG['Attach Hair Curves to Surface']); t.chain(at)
    for q in at.inputs:
        if q.type == 'OBJECT': q.default_value = scalp

if V == "tracos":
    profile(t, EG, radius=0.0015)
else:
    for name, kw in (("GR Densidade Livre", {"Viewport": 1.0, "Fios por m2": 220000.0}), ("GR Mecha Estilizada", {}), ("GR Cor por Mecha", {})):
        n = t.add('GeometryNodeGroup', group=GR[name])
        for k,v in kw.items(): n.inputs[k].default_value = v
        t.chain(n, n.inputs[0].name, n.outputs[0].name)
    profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("h", melanin=0.35 if V=="groom" else 0.9, redness=0.9)); apply_tree(g, t.finish())
gpo.hide_render = True
bpy.context.view_layer.objects.active = g; g.select_set(True)
for m_ in list(g.modifiers): bpy.ops.object.modifier_apply(modifier=m_.name)
bpy.data.objects.remove(gpo); bpy.data.grease_pencils.remove(gp)
print("INFO", V, MODE if V=="groom" else "", stats(g).get('curves'), stats(g).get('points'))
shot(f"80_{V}{'_'+MODE if V=='groom' else ''}", res=420, samples=16, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=46)
