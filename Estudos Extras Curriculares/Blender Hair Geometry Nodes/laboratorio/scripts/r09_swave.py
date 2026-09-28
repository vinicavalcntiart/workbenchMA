import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.34, gravity=4.5, spread=0.25, outward=0.3, n_guides=200)
def swave(t, EG, amp=0.012, per=0.08, start=0.2, axis="normal", phase_by_guide=True):
    """Onda plana: offset = eixo * sin(2pi*comprimento/periodo + fase) * amp * rampa(spline param)."""
    sub = t.add('GeometryNodeSubdivideCurve', Cuts=2); t.chain(sub, 'Curve', 'Curve')
    sp = t.add('GeometryNodeSplineParameter')
    k = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); k.inputs[1].default_value = 2*math.pi/per
    t.link(sp.outputs['Length'], k.inputs[0])
    if phase_by_guide:
        na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
        r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=2*math.pi, Seed=5)
        t.link(na.outputs['Attribute'], r.inputs['ID'])
        add = t.add('ShaderNodeMath', props={'operation':'ADD'}); t.link(k.outputs[0], add.inputs[0]); t.link(r.outputs['Value'], add.inputs[1]); k = add
    s = t.add('ShaderNodeMath', props={'operation':'SINE'}); t.link(k.outputs[0], s.inputs[0])
    ramp = t.add('ShaderNodeMapRange', From_Min=0.0, From_Max=start, To_Min=0.0, To_Max=amp); ramp.clamp = True
    t.link(sp.outputs['Factor'], ramp.inputs['Value'])
    m = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(s.outputs[0], m.inputs[0]); t.link(ramp.outputs['Result'], m.inputs[1])
    if axis == "normal": ax = t.add('GeometryNodeInputNormal').outputs[0]
    else:
        # eixo lateral fixo por fio: cross(tangente, Z)
        tg = t.add('GeometryNodeInputTangent')
        cr = t.add('ShaderNodeVectorMath', props={'operation':'CROSS_PRODUCT'}); cr.inputs[1].default_value = (0,0,1)
        t.link(tg.outputs[0], cr.inputs[0])
        nm = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(cr.outputs[0], nm.inputs[0]); ax = nm.outputs[0]
    sc = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(ax, sc.inputs[0]); t.link(m.outputs[0], sc.inputs['Scale'])
    sp_ = t.add('GeometryNodeSetPosition'); t.chain(sp_)
    t.link(sc.outputs[0], sp_.inputs['Offset'])
def build(t, EG, g=None, scalp=None, amp=0.012, per=0.08, axis="normal", ph=True, clump_after=False):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    swave(t, EG, amp=amp, per=per, axis=axis, phase_by_guide=ph)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("loiro", melanin=0.18, redness=0.35, roughness=0.25))
FR = dict(cam_loc=(0.30,-0.62,-0.02), target=(0,0,-0.12), lens=45)
run_variants("09_swave", [
    ("S lateral amp1.2cm per8cm fase/mecha", dict(axis="lateral", _guides=dict(G))),
    ("S normal amp1.2cm per8cm fase/mecha", dict(axis="normal", _guides=dict(G))),
    ("S lateral sem fase (tudo igual)", dict(axis="lateral", ph=False, _guides=dict(G))),
    ("S lateral amp2cm per12cm", dict(axis="lateral", amp=0.02, per=0.12, _guides=dict(G))),
], build, cols=4, **FR)
