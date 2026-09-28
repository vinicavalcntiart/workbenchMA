import sys; sys.path.insert(0,'.')
from lab import *
BACK = dict(cam_loc=(-0.38,0.55,0.02), target=(0,0,-0.08), lens=55)
def build(t, EG, g=None, scalp=None, shape=0.5, ramp=None, fall=0.0, tip=0.0, radius=0.0005, gd=0.02):
    interp(t, EG, density=300000.0)
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=shape, Tip_Spread=tip, Distance_Falloff=fall,
             Preserve_Length=True, Guide_Distance=gd, Existing_Guide_Map=False, Seed=1)
    if ramp is not None:
        sp = t.add('GeometryNodeSplineParameter')
        mr = t.add('ShaderNodeMapRange', From_Min=0.0, From_Max=ramp, To_Min=0.0, To_Max=1.0)
        mr.clamp = True
        t.link(sp.outputs['Factor'], mr.inputs['Value']); t.link(mr.outputs['Result'], c.inputs['Factor'])
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4))
run_variants("04_ribbon", [
    ("Shape 0.25", dict(shape=0.25)),
    ("Shape 1.0", dict(shape=1.0)),
    ("Shape 0 + Factor rampa 0-0.3", dict(shape=0.0, ramp=0.3)),
    ("Shape 0 + rampa 0.3 + Tip 0.004", dict(shape=0.0, ramp=0.3, tip=0.004)),
    ("Shape 0 + rampa 0.15", dict(shape=0.0, ramp=0.15)),
    ("Shape 0 + rampa 0.3 + Falloff 0.006", dict(shape=0.0, ramp=0.3, fall=0.006)),
], build, cols=3, **BACK)
