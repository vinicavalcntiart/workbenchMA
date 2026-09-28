import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # solto | atras
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.5, spread=0.45, outward=0.35, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.03, location=(sx*0.108,0.005,-0.02)); e = bpy.context.object; e.scale=(0.45,0.7,1.1); bpy.ops.object.shade_smooth(); e.data.materials.append(head.data.materials[0])
t = Tree("or")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 220000.0}); t.chain(d)
m = grp("GR Mecha Estilizada"); t.chain(m, m.inputs[0].name, m.outputs[0].name)
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.chain(rs, 'Curve', 'Curve')
base = t.geo
if V == "atras":
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx_ = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx_.inputs[0])
    sg = t.add('ShaderNodeMath', props={'operation':'SIGN'}); t.link(sx_.outputs['X'], sg.inputs[0])
    tx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sg.outputs[0], tx.inputs[0]); tx.inputs[1].default_value = 0.108
    tie = t.add('ShaderNodeCombineXYZ'); t.link(tx.outputs[0], tie.inputs['X']); tie.inputs['Y'].default_value = 0.035; tie.inputs['Z'].default_value = 0.005
    rb = grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Até a amarração": 0.3, "Comprimento da cauda": 0.18, "Abertura": 0.03, "Para trás": 0.3})
    t.link(base, rb.inputs[0]); t.link(tie.outputs[0], rb.inputs['Amarração'])
    # mascara: raiz na lateral da frente (|x| > 4 cm e y < 2 cm e z < 7 cm)
    ax = t.add('ShaderNodeMath', props={'operation':'ABSOLUTE'}); t.link(sx_.outputs['X'], ax.inputs[0])
    m1 = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); m1.clamp=True; t.link(ax.outputs[0], m1.inputs['Value']); m1.inputs['From Min'].default_value = 0.025; m1.inputs['From Max'].default_value = 0.045
    m2 = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); m2.clamp=True; t.link(sx_.outputs['Y'], m2.inputs['Value']); m2.inputs['From Min'].default_value = 0.07; m2.inputs['From Max'].default_value = 0.04
    m3 = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); m3.clamp=True; t.link(sx_.outputs['Z'], m3.inputs['Value']); m3.inputs['From Min'].default_value = 0.09; m3.inputs['From Max'].default_value = 0.07
    mu = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(m1.outputs['Result'], mu.inputs[0]); t.link(m2.outputs['Result'], mu.inputs[1])
    mu2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(mu.outputs[0], mu2.inputs[0]); t.link(m3.outputs['Result'], mu2.inputs[1])
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(mu2.outputs[0], ev.inputs[0])
    tr = grp("GR Transição"); t.link(base, tr.inputs[0]); t.link(rb.outputs[0], tr.inputs[1]); t.link(ev.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.45, redness=0.7)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"76_{V}", res=440, samples=16, cam_loc=(0.62,-0.30,0.02), target=(0.02,0,-0.04), lens=48)
