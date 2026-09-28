import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # fino | grosso | regiao
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, spread=0.3, outward=0.35, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("cr")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 250000.0; t.chain(d)
base = t.geo
def mecha(sz):
    n = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); n.inputs["Tamanho da mecha"].default_value = sz; t.link(base, n.inputs[0]); return n.outputs[0]
if V == "fino": t.geo = mecha(0.008)
elif V == "grosso": t.geo = mecha(0.035)
else:
    a = mecha(0.008); b = mecha(0.035)
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx.inputs[0])
    fa = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); fa.clamp=True; t.link(sx.outputs['Z'], fa.inputs['Value']); fa.inputs['From Min'].default_value = 0.03; fa.inputs['From Max'].default_value = 0.07
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(fa.outputs['Result'], ev.inputs[0])
    tr = t.add('GeometryNodeGroup', group=GR["GR Transição"]); t.link(a, tr.inputs[0]); t.link(b, tr.inputs[1]); t.link(ev.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5, redness=0.8)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"79_{V}", res=420, samples=16, cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.05), lens=46)
