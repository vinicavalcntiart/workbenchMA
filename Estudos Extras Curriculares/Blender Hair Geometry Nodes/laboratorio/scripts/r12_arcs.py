import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.30, gravity=4.0, spread=0.25, outward=0.3, n_guides=200)
FR = dict(cam_loc=(0.45,-0.55,0.0), target=(0,0,-0.08), lens=50)
def build(t, EG, g=None, scalp=None, frac=0.04, kind="noise", dist=0.04, sc=3.0):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    ci = t.add('GeometryNodeGroup', group=EG['Curve Info'])
    cmp = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}, B=frac)
    t.link(ci.outputs['Random'], cmp.inputs['A'])
    if kind == "noise":
        n = t.eg(EG['Hair Curves Noise'], Distance=dist, Shape=0.7, Scale=sc, Scale_along_Curve=1.0, Offset_per_Curve=1.0,
                 Cumulative_Offset=True, Preserve_Length=True, Seed=6)
    else:
        n = t.eg(EG['Frizz Hair Curves'], Distance=0.02, Shape=0.5, Cumulative_Offset=True, Preserve_Length=True, Seed=4)
    t.link(cmp.outputs['Result'], n.inputs['Factor'])
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("castanho", melanin=0.6, redness=0.45, roughness=0.3))
run_variants("12_arcs", [
    ("4% Frizz 2cm", dict(kind="frizz", _guides=dict(G))),
    ("4% Noise arco 4cm Offset/fio 1", dict(_guides=dict(G))),
    ("4% Noise arco 7cm", dict(dist=0.07, _guides=dict(G))),
    ("8% Noise arco 4cm Scale 8", dict(frac=0.08, sc=8.0, _guides=dict(G))),
], build, cols=4, **FR)
