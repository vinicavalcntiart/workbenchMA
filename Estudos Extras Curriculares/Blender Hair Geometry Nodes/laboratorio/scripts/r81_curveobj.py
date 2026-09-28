import sys; sys.path.insert(0,'.')
from lab import *
import math
SET = sys.argv[-1] == "set"
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g0 = base_scene(n_guides=12, length=0.24)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
# copia as 12 guias para um objeto Curve comum (POLY)
cu = bpy.data.curves.new("guias_curve", 'CURVE'); cu.dimensions = '3D'
for c in g0.data.curves:
    sp = cu.splines.new('POLY'); pts = [g0.data.points[i].position for i in range(c.first_point_index, c.first_point_index+c.points_length)]
    sp.points.add(len(pts)-1)
    for p_, v in zip(sp.points, pts): p_.co = (*v, 1)
co = link(bpy.data.objects.new("guias_curve", cu)); bpy.data.objects.remove(g0)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("cabelo", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("co")
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = co
ga = t.add('GeometryNodeGroup', group=EG['Get Attachment Surface']); t.link(t.gi.outputs[0], ga.inputs[0])
t.geo = oi.outputs['Geometry']
if SET:
    sa = t.add('GeometryNodeGroup', group=EG['Set Attachment Surface']); t.chain(sa); sa.inputs['Mode'].default_value = 'Geometry'
    t.link(ga.outputs['Surface Geometry'], sa.inputs['Surface Geometry']); t.link(ga.outputs['Surface UV Map'], sa.inputs['Surface UV Map'])
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 200000.0; t.chain(d)
apply_tree(g, t.finish())
print("CO set" if SET else "CO sem", stats(g).get('curves'))
