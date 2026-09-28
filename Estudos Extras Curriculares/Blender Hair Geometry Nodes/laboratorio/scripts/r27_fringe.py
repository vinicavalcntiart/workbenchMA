import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.24, gravity=4.0, spread=0.3, outward=0.35, n_guides=240)
FRONT = dict(cam_loc=(0.12,-0.62,0.05), target=(0,0,-0.02), lens=50)
def franja(co):   # frente do topo: y negativo e z alto
    return min(1.0, max(0.0, (-co.y - 0.02)/0.03)) * min(1.0, max(0.0, (co.z - 0.03)/0.02))
def build(t, EG, g=None, scalp=None, push=0.0, cut=0.0, down=0.0):
    vgroup(scalp, "franja", franja)
    interp(t, EG, density=300000.0)
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}, Name="franja")
    if push:
        d = t.eg(EG['Displace Hair Curves'], Shape=0.5, Displace_Vector=(0.0, -push, -down))
        t.link(na.outputs['Attribute'], d.inputs['Factor'])
    if cut:
        tr = t.eg(EG['Trim Hair Curves'], Replace_Length=True, Length=cut, Scale_Uniform=False, Random_Offset=0.006)
        t.link(na.outputs['Attribute'], tr.inputs['Mask'])
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.8, redness=0.4))
run_variants("27_fringe", [
    ("sem franja", dict(_guides=dict(G))),
    ("Displace (0,-8cm,0) Factor=franja", dict(push=0.08, _guides=dict(G))),
    ("+ Trim 9cm Mask=franja", dict(push=0.08, cut=0.09, _guides=dict(G))),
    ("+ desce 4cm (franja reta)", dict(push=0.08, cut=0.09, down=0.04, _guides=dict(G))),
], build, cols=4, **FRONT)
