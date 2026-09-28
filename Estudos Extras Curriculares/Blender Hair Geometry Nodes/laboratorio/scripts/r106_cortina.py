import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7, front_cut=0.75); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("ct")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
x = grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.30, "Para fora": 0.35, "Para o lado da risca": 0.25, "Para trás": 0.2, "Gravidade": 2.2}); t.chain(x, 'Geometry', 'Guias')
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 300000.0}); t.chain(d)
m = grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.014}); t.chain(m, m.inputs[0].name, m.outputs[0].name)
base = t.geo
if V == "cortina":
    mk = grp("GR Máscara por Posição", **{"Frente máx (Y)": -0.045, "Altura mín": 0.03, "Borda suave": 0.012})
    mr = t.add('ShaderNodeMapRange'); t.link(mk.outputs[0], mr.inputs['Value']); mr.inputs['To Min'].default_value = 1.0; mr.inputs['To Max'].default_value = 0.42
    tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); tr.inputs['Replace Length'].default_value = False; t.link(base, tr.inputs['Geometry']); t.link(mr.outputs['Result'], tr.inputs['Length Factor'])
    # abre para os lados: offset lateral = sign(x raiz) * s^2 * 5 cm * mascara, e um pouco para tras
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx.inputs[0])
    sg = t.add('ShaderNodeMath', props={'operation':'SIGN'}); t.link(sx.outputs['X'], sg.inputs[0])
    sp = t.add('GeometryNodeSplineParameter'); s2 = t.add('ShaderNodeMath', props={'operation':'POWER'}); t.link(sp.outputs['Factor'], s2.inputs[0]); s2.inputs[1].default_value = 0.6
    k = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(s2.outputs[0], k.inputs[0]); t.link(mk.outputs[0], k.inputs[1])
    vx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sg.outputs[0], vx.inputs[0]); vx.inputs[1].default_value = 0.09
    cb = t.add('ShaderNodeCombineXYZ'); t.link(vx.outputs[0], cb.inputs['X']); cb.inputs['Y'].default_value = 0.015
    of = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(cb.outputs[0], of.inputs[0]); t.link(k.outputs[0], of.inputs['Scale'])
    stp = t.add('GeometryNodeSetPosition'); t.link(tr.outputs[0], stp.inputs['Geometry']); t.link(of.outputs[0], stp.inputs['Offset'])
    w = t.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves']); w.inputs['Offset Distance'].default_value = 0.004; w.inputs['Above Surface'].default_value = 0.0; w.inputs['Lock Roots'].default_value = True; t.link(stp.outputs[0], w.inputs['Geometry'])
    for q in w.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
    t.geo = w.outputs[0]
c = grp("GR Cor por Mecha"); t.chain(c, c.inputs[0].name, c.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.45, redness=0.6)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"106_{V}", res=420, samples=16, cam_loc=(0.12,-0.62,0.02), target=(0,0,-0.03), lens=46)
