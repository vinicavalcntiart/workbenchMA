import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
FR = dict(cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.07), lens=48)
def gid(t):
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index"); return na.outputs['Attribute']
def build(t, EG, g=None, scalp=None, length=False, lift=0.0, lift_shape=-0.5, breakup=False):
    interp(t, EG, density=300000.0)
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
        d = t.eg(EG['Displace Hair Curves'], Factor=1.0, Shape=lift_shape, Surface_Normal=True, Surface_Normal_Distance=lift)
        d.inputs[8].default_value = scalp if d.inputs[8].type=='OBJECT' else None
        for s in d.inputs:
            if s.type=='OBJECT' and s.name=='Surface': s.default_value = scalp
        uv = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="UVMap")
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.6, redness=0.55))
run_variants("24_proc", [
    ("base", dict(_guides=dict(G))),
    ("comprimento por mecha 70-100%", dict(length=True, _guides=dict(G))),
    ("volume: Displace normal 1.5cm Shape -0.5", dict(lift=0.015, _guides=dict(G))),
    ("clump quebrado por Noise 3D (15-100%)", dict(breakup=True, _guides=dict(G))),
    ("os tres juntos", dict(length=True, lift=0.015, breakup=True, _guides=dict(G))),
    ("volume Shape 0.5 (so pontas)", dict(lift=0.02, lift_shape=0.5, _guides=dict(G))),
], build, cols=3, **FR)
