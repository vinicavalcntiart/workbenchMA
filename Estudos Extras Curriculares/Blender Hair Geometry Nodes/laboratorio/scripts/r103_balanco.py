import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LAG = float(sys.argv[-1])   # atraso ao longo do fio (rad): 0 = pendulo rigido
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("bl")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.34, "Gravidade": 2.2})
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
# balanco: gira cada ponto em volta da raiz, eixo Y (lado a lado), angulo = A * s * sin(2pi t/T - LAG*s)
cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sp = t.add('GeometryNodeSplineParameter'); st = t.add('GeometryNodeInputSceneTime')
w = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(st.outputs['Seconds'], w.inputs[0]); w.inputs[1].default_value = 2*math.pi/1.0
lg = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], lg.inputs[0]); lg.inputs[1].default_value = LAG
ph = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); t.link(w.outputs[0], ph.inputs[0]); t.link(lg.outputs[0], ph.inputs[1])
sn = t.add('ShaderNodeMath', props={'operation':'SINE'}); t.link(ph.outputs[0], sn.inputs[0])
a1 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sn.outputs[0], a1.inputs[0]); t.link(sp.outputs['Factor'], a1.inputs[1])
a2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(a1.outputs[0], a2.inputs[0]); a2.inputs[1].default_value = 0.35
ps = t.add('GeometryNodeInputPosition')
vr = t.add('ShaderNodeVectorRotate', props={'rotation_type':'Y_AXIS'}); t.link(ps.outputs[0], vr.inputs['Vector']); t.link(cr.outputs['Root Position'], vr.inputs['Center']); t.link(a2.outputs[0], vr.inputs['Angle'])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(vr.outputs[0], s.inputs['Position'])
w_ = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=1, Lock_Roots=True)
for q in w_.inputs:
    if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 200000.0})
grp("GR Mecha Estilizada"); grp("GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.35, redness=0.9)); apply_tree(g, t.finish())
sc = bpy.context.scene; sc.render.fps = 24; sc.frame_start=1; sc.frame_end=24
stage(res=300, samples=8, cam_loc=(0.0,0.75,-0.05), target=(0,0,-0.12), lens=40)
fr=[]
for f in range(1,25,2):
    sc.frame_set(f); p=os.path.join(OUT, f"103_{LAG}_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); fr.append(p)
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in fr]
ims[0].save(os.path.join(OUT,f"103_balanco_{LAG}.gif"), save_all=True, append_images=ims[1:], duration=83, loop=0)
print("OK", LAG, stats(g).get('curves'))
