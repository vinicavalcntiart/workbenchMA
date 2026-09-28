import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
ctrl = link(bpy.data.objects.new("MAO", None)); ctrl.empty_display_type = 'SPHERE'; ctrl.empty_display_size = 0.04
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035); mao = bpy.context.object; mao.parent = ctrl
mm = bpy.data.materials.new("mao"); mm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.9,0.6,0.5,1); mao.data.materials.append(mm)
t = Tree("pe")
for name, kw in (("GR Densidade Livre", {"Viewport": 1.0, "Fios por m2": 220000.0}), ("GR Mecha Estilizada", {})):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name)
# pente: empurra cada ponto para fora da esfera do controle (raio R + margem), suave
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = ctrl
ps = t.add('GeometryNodeInputPosition')
dv = t.add('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); t.link(ps.outputs[0], dv.inputs[0]); t.link(oi.outputs['Location'], dv.inputs[1])
ln = t.add('ShaderNodeVectorMath', props={'operation':'LENGTH'}); t.link(dv.outputs[0], ln.inputs[0])
nd = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(dv.outputs[0], nd.inputs[0])
R = 0.045
pen = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); pen.inputs[0].default_value = R; t.link(ln.outputs['Value'], pen.inputs[1])
mx = t.add('ShaderNodeMath', props={'operation':'MAXIMUM'}); t.link(pen.outputs[0], mx.inputs[0]); mx.inputs[1].default_value = 0.0
sc_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nd.outputs[0], sc_.inputs[0]); t.link(mx.outputs[0], sc_.inputs['Scale'])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(sc_.outputs[0], s.inputs['Offset'])
w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.003, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
for q in w.inputs:
    if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.35, redness=0.8)); apply_tree(g, t.finish())
# mao passando pelo lado da cabeca, de cima para baixo
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=36
for f,z in ((1,0.12),(36,-0.2)):
    ctrl.location = (0.125, -0.01, z); ctrl.keyframe_insert("location", frame=f)
import numpy as np
for f in (13, 25):
    sc.frame_set(f); bpy.context.view_layer.update()
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    c = np.array(ctrl.matrix_world.translation[:]); dist = np.linalg.norm(P-c, axis=1)
    print("PEN", "desvio" if s.mute==False else "sem", "q", f, "pontos dentro da esfera (r<3,5cm):", int((dist<0.035).sum()), "entre 3,5 e 4,5:", int(((dist>=0.035)&(dist<0.045)).sum()))
s.mute = True
for f in (13, 25):
    sc.frame_set(f); bpy.context.view_layer.update()
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    c = np.array(ctrl.matrix_world.translation[:]); dist = np.linalg.norm(P-c, axis=1)
    print("PEN sem q", f, "pontos dentro:", int((dist<0.035).sum()))
