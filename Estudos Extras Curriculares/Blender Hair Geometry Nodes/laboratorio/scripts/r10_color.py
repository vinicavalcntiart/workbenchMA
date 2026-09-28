import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.30, gravity=4.0, spread=0.25, outward=0.3, n_guides=200)
BACK = dict(cam_loc=(-0.38,0.55,0.02), target=(0,0,-0.08), lens=55)
def color_mat(mode):
    m = bpy.data.materials.new("hcol"); nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model='CHIANG'; h.parametrization='MELANIN'
    h.inputs['Roughness'].default_value = 0.3; h.inputs['Melanin Redness'].default_value = 0.5
    h.inputs['Melanin'].default_value = 0.45
    nt.links.new(h.outputs[0], out.inputs['Surface'])
    mel = None
    if mode in ("mecha", "mecha+raiz"):
        a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name = "mecha_rand"
        mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 0.3; mr.inputs['To Max'].default_value = 0.65
        nt.links.new(a.outputs['Fac'], mr.inputs['Value']); mel = mr.outputs['Result']
    if mode == "fio":
        hi = nt.nodes.new('ShaderNodeHairInfo')
        mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 0.3; mr.inputs['To Max'].default_value = 0.65
        nt.links.new(hi.outputs['Random'], mr.inputs['Value']); mel = mr.outputs['Result']
    if mode == "mecha+raiz":
        hi = nt.nodes.new('ShaderNodeHairInfo')
        rr = nt.nodes.new('ShaderNodeMapRange'); rr.inputs['From Max'].default_value = 0.25
        rr.inputs['To Min'].default_value = 0.45; rr.inputs['To Max'].default_value = 0.0; rr.clamp = True
        nt.links.new(hi.outputs['Intercept'], rr.inputs['Value'])
        add = nt.nodes.new('ShaderNodeMath'); add.operation='ADD'
        nt.links.new(mel, add.inputs[0]); nt.links.new(rr.outputs['Result'], add.inputs[1]); mel = add.outputs[0]
    if mel is not None: nt.links.new(mel, h.inputs['Melanin'])
    return m
def build(t, EG, g=None, scalp=None, mode="none"):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    # atributo por mecha para o shader
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
    r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Seed=9); t.link(na.outputs['Attribute'], r.inputs['ID'])
    st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}, Name="mecha_rand")
    t.chain(st); t.link(r.outputs['Value'], st.inputs['Value'])
    profile(t, EG, radius=0.0005)
    set_mat(t, color_mat(mode))
run_variants("10_color", [
    ("cor unica", dict(mode="none", _guides=dict(G))),
    ("melanina por MECHA (atributo)", dict(mode="mecha", _guides=dict(G))),
    ("melanina por FIO (Hair Info Random)", dict(mode="fio", _guides=dict(G))),
    ("por mecha + raiz escura (Intercept)", dict(mode="mecha+raiz", _guides=dict(G))),
], build, cols=4, **BACK)
