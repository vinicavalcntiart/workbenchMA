"""Variar so as pontas do Clump. Base: Factor 1 (mechas em cone)."""
import sys; sys.path.insert(0,'.')
from lab import *
def fsock(n, name, io='in'):
    socks = n.inputs if io=='in' else n.outputs
    return [s for s in socks if s.name == name and s.type == 'VALUE'][0]
def build(t, EG, g=None, scalp=None, mode="base", spread=0.0):
    interp(t, EG, density=300000.0)
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.5, Tip_Spread=spread,
             Preserve_Length=True, Guide_Distance=0.03, Existing_Guide_Map=False, Seed=1)
    if mode in ("mix", "tip"):
        ci = t.add('GeometryNodeGroup', group=EG['Curve Info'])
        rr = t.add('ShaderNodeMapRange'); rr.clamp = True
        rr.inputs['To Min'].default_value = 0.3; rr.inputs['To Max'].default_value = 1.0
        t.link(ci.outputs['Random'], rr.inputs['Value'])
        mx = t.add('ShaderNodeMix', props={'data_type': 'FLOAT'})
        fsock(mx, 'A').default_value = 1.0
        t.link(rr.outputs['Result'], fsock(mx, 'B'))
        if mode == "mix":   # mascara da regiao da ponta: Spline Parameter 0,6 -> 1,0
            sp = t.add('GeometryNodeSplineParameter')
            mm = t.add('ShaderNodeMapRange'); mm.clamp = True
            mm.inputs['From Min'].default_value = 0.6; mm.inputs['From Max'].default_value = 1.0
            t.link(sp.outputs['Factor'], mm.inputs['Value']); t.link(mm.outputs['Result'], fsock(mx, 'Factor'))
        else:               # Curve Tip: Tip Selection so marca o ultimo ponto
            ct = t.add('GeometryNodeGroup', group=EG['Curve Tip'])
            t.link(ct.outputs['Tip Selection'], fsock(mx, 'Factor'))
        t.link(fsock(mx, 'Result', 'out'), c.inputs['Factor'])
    profile(t, EG, radius=0.0003)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4))
run_variants("122_clump_pontas", [
    ("Base: Factor 1 (cones)", dict()),
    ("Tip Spread 6 mm (0 nodes)", dict(spread=0.006)),
    ("Spline Param + Random: so a ponta", dict(mode="mix")),
    ("Curve Tip: so o ultimo ponto", dict(mode="tip")),
], build, cols=4, cam_loc=(0.24,-0.33,-0.12), target=(0.03,0.0,-0.19), lens=95)
