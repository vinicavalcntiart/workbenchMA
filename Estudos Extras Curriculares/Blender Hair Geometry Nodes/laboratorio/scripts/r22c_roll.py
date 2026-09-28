import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.22, gravity=4.0, spread=0.3, outward=0.35, n_guides=200)
FR = dict(cam_loc=(0.10,-0.72,-0.06), target=(0,0,-0.10), lens=50)
def build(t, EG, g=None, scalp=None, sign=1.0, rl=0.06, rr=0.02, per_lock=False, radial=False):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    ro = t.eg(EG['Roll Hair Curves'], Factor=1.0, Subdivision=2, Roll_Length=rl, Roll_Radius=rr, Random_Orientation=0.0, Preserve_Length=True, Seed=2)
    root = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    if radial:
        cr = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); cr.inputs['Scale'].default_value = sign
    else:
        cr = t.add('ShaderNodeVectorMath', props={'operation':'CROSS_PRODUCT'}); cr.inputs[1].default_value=(0,0,sign)
    t.link(root.outputs['Root Position'], cr.inputs[0])
    nm = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(cr.outputs[0], nm.inputs[0])
    t.link(nm.outputs[0], ro.inputs['Roll Direction'])
    if per_lock:
        na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
        rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.6, Max=1.4, Seed=4); t.link(na.outputs['Attribute'], rv.inputs['ID'])
        m = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); m.inputs[1].default_value = rl; t.link(rv.outputs['Value'], m.inputs[0]); t.link(m.outputs[0], ro.inputs['Roll Length'])
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.75, redness=0.5))
run_variants("22c_roll", [
    ("sem Roll", dict(rl=0.0001, _guides=dict(G))),
    ("Roll Dir = raiz (flip p/ fora)", dict(sign=1.0, radial=True, _guides=dict(G))),
    ("Roll Dir = -raiz (p/ dentro)", dict(sign=-1.0, radial=True, _guides=dict(G))),
    ("p/ dentro + comprimento por mecha", dict(sign=-1.0, radial=True, per_lock=True, _guides=dict(G))),
], build, cols=4, cam_loc=(0.55,-0.45,-0.10), target=(0,0,-0.11), lens=50)
