import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("agua")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
# gravidade negativa leve: o cabelo sobe e abre (flutua)
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.34, "Para fora": 0.6, "Para o lado da risca": 0.5, "Para trás": 0.9, "Gravidade": 0.15, "Guias por m2": 4000.0}.items(): x.inputs[kk].default_value = v
t.chain(x, 'Geometry', 'Guias')
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
# ondulacao: offset = (Noise4D(pos*4, W=t*0.4) - 0.5) * 0.12 * s^1.5
st = t.add('GeometryNodeInputSceneTime'); wt = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(st.outputs['Seconds'], wt.inputs[0]); wt.inputs[1].default_value = 0.4
ps = t.add('GeometryNodeInputPosition')
nz = t.add('ShaderNodeTexNoise'); nz.noise_dimensions='4D'; nz.inputs['Scale'].default_value = 7.0; nz.inputs['Detail'].default_value = 0.0
t.link(ps.outputs[0], nz.inputs['Vector']); t.link(wt.outputs[0], nz.inputs['W'])
ce = t.add('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); t.link(nz.outputs['Color'], ce.inputs[0]); ce.inputs[1].default_value = (0.5,0.5,0.5)
sp = t.add('GeometryNodeSplineParameter'); pw = t.add('ShaderNodeMath', props={'operation':'POWER'}); t.link(sp.outputs['Factor'], pw.inputs[0]); pw.inputs[1].default_value = 1.5
am = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(pw.outputs[0], am.inputs[0]); am.inputs[1].default_value = 0.2
of = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(ce.outputs[0], of.inputs[0]); t.link(am.outputs[0], of.inputs['Scale'])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(of.outputs[0], s.inputs['Offset'])
for n in ("GR Densidade Livre","GR Mecha Estilizada","GR Cor por Mecha"):
    nd = t.add('GeometryNodeGroup', group=GR[n]); t.chain(nd, nd.inputs[0].name, nd.outputs[0].name)
    if n=="GR Densidade Livre": nd.inputs["Viewport"].default_value = 1.0; nd.inputs["Fios por m2"].default_value = 220000.0
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("h", melanin=0.12, redness=1.0, roughness=0.3)); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'))
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=72
stage(res=320, samples=8, cam_loc=(0.75,-0.85,0.10), target=(0,0.10,0.0), lens=38)
sc.world.node_tree.nodes['Background'].inputs[0].default_value = (0.02,0.08,0.12,1)
fr=[]; tt=time.time()
for f in range(1,73,3):
    sc.frame_set(f); p=os.path.join(OUT, f"64_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); fr.append(p)
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in fr]
ims[0].save(os.path.join(OUT,"64_agua.gif"), save_all=True, append_images=ims[1:], duration=125, loop=0)
print("TIME", round(time.time()-tt,1))
print("SHEET", sheet([fr[i] for i in (0,6,12,18)], ["q1","q19","q37","q55"], os.path.join(OUT,"64_agua_sheet.png"), cols=4, w=320))
