import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("d"); x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for k,v in {"Cabeça (colisão)": head, "Comprimento": 0.22, "Para fora": 0.4, "Para o lado da risca": 0.35, "Para trás": 0.45, "Gravidade": 1.3, "Guias por m2": 4000.0}.items(): x.inputs[k].default_value = v
t.chain(x, 'Geometry', 'Guias')
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; t.chain(d)
mc = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); t.chain(mc)
if V == "molhado": mc.inputs["Fecha a partir de"].default_value = 0.12; mc.inputs["Abertura da ponta"].default_value = 0.0; mc.inputs["Tamanho da mecha"].default_value = 0.012
sel = None
na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}); na.inputs['Name'].default_value='guide_curve_index'
if V == "destaque":   # 3% das mechas
    rb = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); rb.inputs['Probability'].default_value = 0.10; t.link(na.outputs['Attribute'], rb.inputs['ID']); rb.inputs['Seed'].default_value = 4
    sel = [o for o in rb.outputs if o.type=='BOOLEAN'][0]
if V == "vampira":    # raizes na frente perto da risca
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    sx = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx.inputs[0])
    c1 = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}); t.link(sx.outputs['Y'], c1.inputs[0]); c1.inputs[1].default_value = -0.035
    ax = t.add('ShaderNodeMath', props={'operation':'ABSOLUTE'}); t.link(sx.outputs['X'], ax.inputs[0])
    c2 = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}); t.link(ax.outputs[0], c2.inputs[0]); c2.inputs[1].default_value = 0.03
    an = t.add('FunctionNodeBooleanMath', props={'operation':'AND'}); t.link(c1.outputs[0], an.inputs[0]); t.link(c2.outputs[0], an.inputs[1]); sel = an.outputs[0]
if V == "ahoge":      # a mecha cuja raiz esta mais perto da coroa: arco para cima
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    di = t.add('ShaderNodeVectorMath', props={'operation':'DISTANCE'}); t.link(cr.outputs['Root Position'], di.inputs[0]); di.inputs[1].default_value = (0.0,-0.02,0.1)
    c1 = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}); t.link(di.outputs['Value'], c1.inputs[0]); c1.inputs[1].default_value = 0.006
    sel = c1.outputs[0]
    sp = t.add('GeometryNodeSplineParameter')
    # offset: sobe e faz arco para frente: (0, -0.06 t^2, 0.10 t - 0.05 t^2) relativo, substitui a forma
    t2 = t.add('ShaderNodeMath', props={'operation':'POWER'}); t.link(sp.outputs['Factor'], t2.inputs[0]); t2.inputs[1].default_value = 2.0
    yy = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(t2.outputs[0], yy.inputs[0]); yy.inputs[1].default_value = -0.07
    z1 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], z1.inputs[0]); z1.inputs[1].default_value = 0.09
    z2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(t2.outputs[0], z2.inputs[0]); z2.inputs[1].default_value = -0.05
    zz = t.add('ShaderNodeMath', props={'operation':'ADD'}); t.link(z1.outputs[0], zz.inputs[0]); t.link(z2.outputs[0], zz.inputs[1])
    cb = t.add('ShaderNodeCombineXYZ'); t.link(yy.outputs[0], cb.inputs['Y']); t.link(zz.outputs[0], cb.inputs['Z'])
    ad = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(cr.outputs['Root Position'], ad.inputs[0]); t.link(cb.outputs[0], ad.inputs[1])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(sel, s.inputs['Selection']); t.link(ad.outputs[0], s.inputs['Position'])
if sel is not None:
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'BOOLEAN'}); t.link(sel, ev.inputs[0])
    st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='destaque'; t.chain(st); t.link(ev.outputs[0], st.inputs['Value'])
    if V == "destaque":
        tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=1.25, Scale_Uniform=False); t.link(ev.outputs[0], tr.inputs['Mask'])
        cu = t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=0.006, Frequency=6.0, Existing_Guide_Map=True, Subdivision=2); t.link(ev.outputs[0], cu.inputs['Factor'])
profile(t, EG, radius=0.0005)
m = bpy.data.materials.new("h"); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial')
h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization='MELANIN'; h.inputs['Melanin Redness'].default_value = 0.6
h.inputs['Roughness'].default_value = 0.15 if V=="molhado" else 0.3
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='destaque'
if V == "vampira":   # destaque = quase sem melanina (branco)
    mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value=0.8; mr.inputs['To Max'].default_value=0.03; nt.links.new(a.outputs['Fac'], mr.inputs['Value']); nt.links.new(mr.outputs['Result'], h.inputs['Melanin'])
else:
    h.inputs['Melanin'].default_value = 0.95 if V=="molhado" else 0.6
if V == "destaque":  # tinta azul na mecha
    h.parametrization = 'MELANIN'
    mx = nt.nodes.new('ShaderNodeMix'); mx.data_type='RGBA'; mx.inputs[6].default_value=(1,1,1,1); mx.inputs[7].default_value=(0.1,0.35,1.0,1); nt.links.new(a.outputs['Fac'], mx.inputs[0]); nt.links.new(mx.outputs[2], h.inputs['Tint'])
    mr2 = nt.nodes.new('ShaderNodeMapRange'); mr2.inputs['To Min'].default_value=0.6; mr2.inputs['To Max'].default_value=0.05; nt.links.new(a.outputs['Fac'], mr2.inputs['Value']); nt.links.new(mr2.outputs['Result'], h.inputs['Melanin'])
nt.links.new(h.outputs[0], o.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
import numpy as np
dd = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
if 'destaque' in dd.attributes:
    a_ = np.zeros(len(dd.curves), np.float32); dd.attributes['destaque'].data.foreach_get('value', a_); print("SEL", V, int((a_>0.5).sum()), "de", len(dd.curves))
print("INFO", V, stats(g).get('curves'))
shot(f"58_{V}", res=420, samples=20, cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.04), lens=46)
