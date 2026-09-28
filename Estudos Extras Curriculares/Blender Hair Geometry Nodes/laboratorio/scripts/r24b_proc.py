import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
FR = dict(cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.07), lens=48)
def gid(t):
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index"); return na.outputs['Attribute']
def build(t, EG, g=None, scalp=None, length=False, lift=0.0, lift_shape=-0.5, lift_ramp=0.3, breakup=False):
    it = interp(t, EG, density=300000.0)
    stn = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT_VECTOR','domain':'CURVE'}, Name="n_raiz"); t.chain(stn)
    t.link(it.outputs['Surface Normal'], stn.inputs['Value'])
    cg = t.eg(EG['Create Guide Index Map'], Guide_Distance=0.02)
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=True, Seed=1)
    if breakup:
        rt = t.add('GeometryNodeGroup', group=EG['Curve Root'])
        nz = t.add('ShaderNodeTexNoise', Scale=25.0, Detail=0.0); t.link(rt.outputs['Root Position'], nz.inputs['Vector'])
        mr = t.add('ShaderNodeMapRange', From_Min=0.4, From_Max=0.6, To_Min=0.15, To_Max=1.0); mr.clamp = True
        t.link(nz.outputs['Fac'], mr.inputs['Value']); t.link(mr.outputs['Result'], c.inputs['Factor'])
    if length:
        r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.7, Max=1.0, Seed=5); t.link(gid(t), r.inputs['ID'])
        tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=False)
        t.link(r.outputs['Value'], tr.inputs['Length Factor'])
    if lift:
        # volume: empurra pela normal da raiz; rampa 0..ramp no Spline Parameter segura a raiz no lugar
        n = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="n_raiz")
        sp = t.add('GeometryNodeSplineParameter')
        mr = t.add('ShaderNodeMapRange', From_Max=lift_ramp, To_Max=lift); mr.clamp = True; t.link(sp.outputs['Factor'], mr.inputs['Value'])
        sc = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(n.outputs['Attribute'], sc.inputs[0]); t.link(mr.outputs['Result'], sc.inputs['Scale'])
        spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(sc.outputs[0], spn.inputs['Offset'])
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.6, redness=0.55))
run_variants("24b_proc", [
    ("base", dict(_guides=dict(G))),
    ("volume 1.5cm, rampa 30%", dict(lift=0.015, _guides=dict(G))),
    ("volume 3cm, rampa 15% (topete)", dict(lift=0.03, lift_ramp=0.15, _guides=dict(G))),
    ("comprimento + volume 1.5 + noise", dict(length=True, lift=0.015, breakup=True, _guides=dict(G))),
], build, cols=4, **FR)
