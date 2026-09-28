import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.24, gravity=4.0, spread=0.3, outward=0.35, n_guides=240)
FRONT = dict(cam_loc=(0.12,-0.62,0.05), target=(0,0,-0.02), lens=50)
def franja(co):   # frente do topo: y negativo e z alto
    return min(1.0, max(0.0, (-co.y - 0.02)/0.03)) * min(1.0, max(0.0, (co.z - 0.03)/0.02))
def build(t, EG, g=None, scalp=None, push=0.0, cut=0.0, down=0.0, wrap=False, above=0.0, smooth=2, order='trim_first'):
    vgroup(scalp, "franja", franja)
    interp(t, EG, density=300000.0)
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}, Name="franja")
    def do_trim():
        if cut:
            tr = t.eg(EG['Trim Hair Curves'], Replace_Length=True, Length=cut, Scale_Uniform=False, Random_Offset=0.006)
            t.link(na.outputs['Attribute'], tr.inputs['Mask'])
    def do_push():
        if push:
            d = t.eg(EG['Displace Hair Curves'], Shape=0.5, Displace_Vector=(0.0, -push, -down))
            t.link(na.outputs['Attribute'], d.inputs['Factor'])
    if order == 'trim_first': do_trim(); do_push()
    else: do_push(); do_trim()
    if wrap:
        w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=above, Smoothing_Steps=smooth, Lock_Roots=True)
        for x in w.inputs:
            if x.name == 'Surface' and x.type == 'OBJECT': x.default_value = bpy.data.objects['head']
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.8, redness=0.4))
run_variants("27b_fringe", [
    ("Trim 9cm > Displace (0,-6,-3cm)", dict(push=0.06, down=0.03, cut=0.09, _guides=dict(G))),
    ("+ Shrinkwrap cabeca (Above 0)", dict(push=0.06, down=0.03, cut=0.09, wrap=True, _guides=dict(G))),
    ("+ Shrinkwrap Above 0.5 (padrao)", dict(push=0.06, down=0.03, cut=0.09, wrap=True, above=0.5, _guides=dict(G))),
    ("Displace > Trim (ordem inversa) + wrap", dict(push=0.06, down=0.03, cut=0.09, wrap=True, order='push_first', _guides=dict(G))),
], build, cols=4, **FRONT)
