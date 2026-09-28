import sys; sys.path.insert(0,'.')
from lab import *
V = sys.argv[-1]
CAM = dict(cam_loc=(0.42,-0.55,0.16), target=(0,0,0.0), lens=55)
EG, body, g = fur_scene(n=600, length=0.035)
t = Tree("pad")
it = t.eg(EG['Interpolate Hair Curves'], Seed=1); t.link(value(t, 1.5e6), it.inputs['Density'])
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=2)
cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
if V.startswith("listra"):
    tx = t.add('ShaderNodeTexWave'); tx.wave_type='BANDS'; tx.bands_direction='Z'
    tx.inputs['Scale'].default_value = 7.0; tx.inputs['Distortion'].default_value = 8.0; tx.inputs['Detail'].default_value = 1.0
    t.link(cr.outputs['Root Position'], tx.inputs['Vector']); f = tx.outputs['Fac']
    mr = t.add('ShaderNodeMapRange'); mr.clamp=True; mr.inputs['From Min'].default_value=0.62; mr.inputs['From Max'].default_value=0.68; t.link(f, mr.inputs['Value'])
else:
    tx = t.add('ShaderNodeTexVoronoi'); tx.inputs['Scale'].default_value = 12.0
    t.link(cr.outputs['Root Position'], tx.inputs['Vector']); f = tx.outputs['Distance']
    if V.startswith("roseta"):   # anel: 1 entre 0,28 e 0,42 de distancia
        a1 = t.add('ShaderNodeMapRange'); a1.clamp=True; a1.inputs['From Min'].default_value=0.26; a1.inputs['From Max'].default_value=0.30; t.link(f, a1.inputs['Value'])
        a2 = t.add('ShaderNodeMapRange'); a2.clamp=True; a2.inputs['From Min'].default_value=0.44; a2.inputs['From Max'].default_value=0.40; t.link(f, a2.inputs['Value'])
        mr = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(a1.outputs['Result'], mr.inputs[0]); t.link(a2.outputs['Result'], mr.inputs[1])
        mr.outputs[0].name
    else:
        mr = t.add('ShaderNodeMapRange'); mr.clamp=True; mr.inputs['From Min'].default_value=0.40; mr.inputs['From Max'].default_value=0.34; t.link(f, mr.inputs['Value'])
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(mr.outputs[0], ev.inputs[0])
st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='padrao'; t.chain(st); t.link(ev.outputs[0], st.inputs['Value'])
if V.endswith("_relevo"):
    lf = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(ev.outputs[0], lf.inputs[0]); lf.inputs[1].default_value = -0.4; lf.inputs[2].default_value = 1.0
    tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=True); t.link(lf.outputs[0], tr.inputs['Length Factor'])
profile(t, EG, radius=0.0003)
m = bpy.data.materials.new("fur"); nt = m.node_tree; nt.nodes.clear()
out = nt.nodes.new('ShaderNodeOutputMaterial'); h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model='CHIANG'; h.parametrization='MELANIN'
h.inputs['Roughness'].default_value=0.35; h.inputs['Melanin Redness'].default_value=1.0
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='padrao'
mm = nt.nodes.new('ShaderNodeMapRange'); mm.inputs['To Min'].default_value=0.3; mm.inputs['To Max'].default_value=1.0; nt.links.new(a.outputs['Fac'], mm.inputs['Value'])
nt.links.new(mm.outputs['Result'], h.inputs['Melanin']); nt.links.new(h.outputs[0], out.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"50_{V}", res=420, samples=16, **CAM)
