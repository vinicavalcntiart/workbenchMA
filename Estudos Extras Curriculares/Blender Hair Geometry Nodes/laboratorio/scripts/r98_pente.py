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
stage(res=320, samples=10, cam_loc=(0.55,-0.55,0.02), target=(0.02,0,-0.06), lens=44)
fr=[]
for f in range(1,37,3):
    sc.frame_set(f); p=os.path.join(OUT, f"98_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); fr.append(p)
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in fr]
ims[0].save(os.path.join(OUT,"98_pente.gif"), save_all=True, append_images=ims[1:], duration=110, loop=0)
print("SHEET", sheet([fr[0], fr[4], fr[8]], ["q1","q13","q25"], os.path.join(OUT,"98_pente_sheet.png"), cols=3, w=320))
