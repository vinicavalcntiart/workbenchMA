import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
def ombre_mat(base, tip, rough=0.35):
    m = bpy.data.materials.new("ombre"); nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model='CHIANG'; h.parametrization='COLOR'
    h.inputs['Roughness'].default_value = rough
    hi = nt.nodes.new('ShaderNodeHairInfo'); cr = nt.nodes.new('ShaderNodeValToRGB')
    cr.color_ramp.elements[0].position = 0.45; cr.color_ramp.elements[0].color = (*base,1)
    cr.color_ramp.elements[1].position = 0.95; cr.color_ramp.elements[1].color = (*tip,1)
    a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name = "mecha_rand"
    mix = nt.nodes.new('ShaderNodeMix'); mix.data_type='RGBA'; mix.blend_type='MULTIPLY'; mix.inputs['Factor'].default_value = 0.35
    mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 0.7; mr.inputs['To Max'].default_value = 1.2
    nt.links.new(a.outputs['Fac'], mr.inputs['Value'])
    comb = nt.nodes.new('ShaderNodeCombineColor'); [nt.links.new(mr.outputs['Result'], comb.inputs[i]) for i in range(3)]
    nt.links.new(hi.outputs['Intercept'], cr.inputs['Fac']); nt.links.new(cr.outputs['Color'], mix.inputs[6]); nt.links.new(comb.outputs[0], mix.inputs[7])
    nt.links.new(mix.outputs[2], h.inputs['Color']); nt.links.new(h.outputs[0], out.inputs['Surface']); return m
STYLES = [
 ("bob castanho",          dict(L=0.2, outw=0.4, lado=0.35, grav=1.2, curl=0, onda=0, roll=-1, vol=0.015), ((0.03,0.012,0.005),(0.05,0.02,0.008))),
 ("longo ombre azul",      dict(L=0.34, outw=0.4, lado=0.25, grav=2.2, curl=0, onda=1, roll=0, vol=0.01), ((0.03,0.015,0.008),(0.05,0.2,0.6))),
 ("cacheado ruivo",        dict(L=0.24, outw=0.8, lado=0.45, grav=0.5, curl=1, onda=0, roll=0, vol=0.02), ((0.35,0.08,0.02),(0.45,0.12,0.03))),
 ("espetado loiro",        dict(L=0.12, outw=1.2, lado=0.1, grav=0.0, curl=0, onda=0, roll=0, vol=0.0), ((0.5,0.35,0.15),(0.8,0.7,0.45))),
 ("flip anos 60",          dict(L=0.18, outw=0.45, lado=0.3, grav=1.4, curl=0, onda=0, roll=1, vol=0.03), ((0.02,0.02,0.025),(0.04,0.04,0.05))),
 ("rosa ombre ondulado",   dict(L=0.28, outw=0.5, lado=0.3, grav=1.6, curl=0, onda=1, roll=0, vol=0.02), ((0.35,0.2,0.12),(0.9,0.25,0.5))),
 ("curto cacheado preto",  dict(L=0.12, outw=0.9, lado=0.2, grav=0.3, curl=2, onda=0, roll=0, vol=0.01), ((0.015,0.01,0.008),(0.02,0.012,0.01))),
 ("longo liso platinado",  dict(L=0.36, outw=0.35, lado=0.2, grav=2.6, curl=0, onda=0, roll=-1, vol=0.01), ((0.7,0.65,0.55),(0.85,0.82,0.75))),
]
paths=[]; labels=[]
for lb, p, (c0,c1) in STYLES:
    reset()
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
    GR = {n.name:n for n in bpy.data.node_groups}
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    cd = bpy.data.hair_curves.new("v"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
    t = Tree("galeria")
    def grp(n, out='Geometry', **kw):
        x = t.add('GeometryNodeGroup', group=GR[n])
        for k,v in kw.items(): x.inputs[k].default_value = v
        return t.chain(x, 'Geometry', out)
    grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head, "Comprimento":p['L'], "Para fora":p['outw'], "Para o lado da risca":p['lado'], "Gravidade":p['grav']})
    grp("GR Densidade Livre", Viewport=1.0)
    grp("GR Mecha Estilizada")
    if p['vol']: grp("GR Volume na Raiz", Volume=p['vol'], **{"Sobe até":0.2})
    grp("GR Strays em Arco", **{"Fração":0.03})
    if p['curl'] == 1: grp("GR Cacho por Mecha")
    if p['curl'] == 2: grp("GR Cacho por Mecha", **{"Raio mín":0.004, "Raio máx":0.007, "Voltas por metro mín":50.0, "Voltas por metro máx":80.0, "Começa em":0.05})
    if p['onda']: grp("GR Onda S")
    if p['roll']: grp("GR Ponta Virada", **{"Para fora": p['roll'] > 0})
    grp("GR Cor por Mecha")
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = ombre_mat(c0,c1); t.chain(sm)
    apply_tree(g, t.finish())
    paths.append(shot("37_"+str(len(paths)), res=360, samples=14, cam_loc=(0.42,-0.62,0.04), target=(0,0,-0.07), lens=45)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"37_gallery_sheet.png"), cols=4, w=400))
