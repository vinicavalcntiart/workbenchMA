import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("morph")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = 200000.0; d.inputs["Viewport"].default_value = 1.0; t.chain(d)
m = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); t.chain(m)
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 64; t.chain(rs, 'Curve', 'Curve')
base = t.geo
# B: cacho por mecha, Subdivisao 0 (mesma contagem de pontos)
cb = t.add('GeometryNodeGroup', group=GR["GR Cacho por Mecha"]); t.link(base, cb.inputs[0])
for s in cb.inputs:
    if s.name.startswith("Subdivis"): s.default_value = 0
pB = t.add('GeometryNodeInputPosition'); ix = t.add('GeometryNodeInputIndex')
si = t.add('GeometryNodeSampleIndex', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}); t.link(cb.outputs[0], si.inputs['Geometry']); t.link(pB.outputs[0], si.inputs['Value']); t.link(ix.outputs[0], si.inputs['Index'])
# fator: suave 0..1 entre 0,3 s e 1,5 s, com atraso por mecha
st = t.add('GeometryNodeInputSceneTime')
na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}); na.inputs['Name'].default_value='guide_curve_index'
rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=0.5); t.link(na.outputs['Attribute'], rv.inputs['ID'])
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(rv.outputs['Value'], ev.inputs[0])
sb = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); t.link(st.outputs['Seconds'], sb.inputs[0]); t.link(ev.outputs[0], sb.inputs[1])
mr = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); mr.clamp=True; t.link(sb.outputs[0], mr.inputs['Value']); mr.inputs['From Min'].default_value=0.3; mr.inputs['From Max'].default_value=1.2
pA = t.add('GeometryNodeInputPosition')
mx = t.add('ShaderNodeMix', props={'data_type':'VECTOR'}); t.link(mr.outputs['Result'], mx.inputs[0]); t.link(pA.outputs[0], mx.inputs[4]); t.link(si.outputs[0], mx.inputs[5])
sp = t.add('GeometryNodeSetPosition'); t.link(base, sp.inputs['Geometry']); t.link(mx.outputs[1], sp.inputs['Position']); t.geo = sp.outputs[0]
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("h", melanin=0.3, redness=1.0)); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=48
stage(res=320, samples=8, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
frames=[]; tt=time.time()
for f in range(1,49,2):
    sc.frame_set(f); p=os.path.join(OUT, f"55_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); frames.append(p)
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in frames]
ims[0].save(os.path.join(OUT,"55_morph.gif"), save_all=True, append_images=ims[1:]+[ims[-1]]*6, duration=83, loop=0)
print("TIME", round(time.time()-tt,1))
print("SHEET", sheet([frames[i] for i in (0,8,12,16,23)], ["q1 liso","q17","q25","q33","q47 cacheado"], os.path.join(OUT,"55_morph_sheet.png"), cols=5, w=320))
