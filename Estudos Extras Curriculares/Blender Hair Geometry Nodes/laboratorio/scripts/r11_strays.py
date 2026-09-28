import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.30, gravity=4.0, spread=0.25, outward=0.3, n_guides=200)
FR = dict(cam_loc=(0.45,-0.55,0.0), target=(0,0,-0.08), lens=50)
def curve_info_random(t, EG):
    n = t.add('GeometryNodeGroup', group=EG['Curve Info']); return n.outputs['Random']
def build(t, EG, g=None, scalp=None, mode="none", frac=0.12, fz=0.02, lf=1.25):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    if mode in ("strays", "strays+trim"):
        cmp = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}, B=frac)
        t.link(curve_info_random(t, EG), cmp.inputs['A'])
        fzn = t.eg(EG['Frizz Hair Curves'], Distance=fz, Shape=0.5, Cumulative_Offset=True, Preserve_Length=True, Seed=4)
        t.link(cmp.outputs['Result'], fzn.inputs['Factor'])
        if mode == "strays+trim":
            tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=lf, Scale_Uniform=False)
            t.link(cmp.outputs['Result'], tr.inputs['Mask'])
    if mode == "tipfrizz":
        t.eg(EG['Frizz Hair Curves'], Factor=1.0, Distance=0.004, Shape=0.9, Cumulative_Offset=True, Preserve_Length=True, Seed=4)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("castanho", melanin=0.6, redness=0.45, roughness=0.3))
run_variants("11_strays", [
    ("sem strays", dict(_guides=dict(G))),
    ("12% Frizz 2cm (Compare<0.12)", dict(mode="strays", _guides=dict(G))),
    ("12% Frizz + Trim x1.25", dict(mode="strays+trim", _guides=dict(G))),
    ("Frizz so ponta (Shape 0.9, 4mm)", dict(mode="tipfrizz", _guides=dict(G))),
], build, cols=4, **FR)
