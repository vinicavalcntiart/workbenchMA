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
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = ["GR Guias Desenhadas"]
gd = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Guias Desenhadas"]); gd.inputs["Grease Pencil"].default_value = gpo; t.chain(gd, 'Geometry', 'Guias')
for name, kw in (("GR Densidade Livre", {"Viewport": 1.0, "Fios por m2": 220000.0}), ("GR Mecha Estilizada", {})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.35, redness=0.9)); apply_tree(g, t.finish())
print("INFO lib", stats(g).get('curves'), stats(g).get('points'))
