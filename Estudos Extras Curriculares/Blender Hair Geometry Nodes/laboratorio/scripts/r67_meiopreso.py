import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
V = sys.argv[-1]   # solto | preso | meio
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.30, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("mp")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for kk,v in kw.items(): n.inputs[kk].default_value = v
    return n
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 220000.0}); t.chain(d)
m = grp("GR Mecha Estilizada"); t.chain(m, m.inputs[0].name, m.outputs[0].name)
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
base = t.geo
rb = grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Amarração": (0.0, 0.095, 0.045), "Até a amarração": 0.35, "Comprimento da cauda": 0.22, "Abertura": 0.02, "Para trás": 0.2})
t.link(base, rb.inputs[0])
if V == "solto": pass
elif V == "preso": t.geo = rb.outputs[0]
else:
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx.inputs[0])
    fa = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); fa.clamp=True; t.link(sx.outputs['Z'], fa.inputs['Value']); fa.inputs['From Min'].default_value = 0.035; fa.inputs['From Max'].default_value = 0.055
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(fa.outputs['Result'], ev.inputs[0])
    tr = grp("GR Transição"); t.link(base, tr.inputs[0]); t.link(rb.outputs[0], tr.inputs[1]); t.link(ev.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
c = grp("GR Cor por Mecha"); t.chain(c, c.inputs[0].name, c.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.2, redness=0.9)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"67_{V}{sys.argv[-2] if len(sys.argv)>2 and sys.argv[-2]=="lado" else ""}", res=420, samples=16, cam_loc=((0.75,0.05,0.12) if "lado" in sys.argv else (0.45,0.55,0.10)), target=(0,0,-0.06), lens=46)
