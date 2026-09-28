import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
FR = dict(cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
def build(t, EG, g=None, scalp=None, fix=None):
    interp(t, EG, density=250000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Hair Curves Noise'], Factor=1.0, Distance=0.012, Shape=0.5, Scale=20.0, Scale_along_Curve=10.0, Offset_per_Curve=0.5, Cumulative_Offset=True, Preserve_Length=True, Seed=2)
    if fix == "smooth":   t.eg(EG['Smooth Hair Curves'], Amount=1.0, Iterations=10, Weight=0.5, Preserve_Length=True)
    if fix and fix.startswith("sshape"): t.eg(EG['Smooth Hair Curves'], Amount=1.0, Shape=float(fix[6:]), Iterations=20, Weight=0.5, Preserve_Length=True)
    if fix == "smooth30": t.eg(EG['Smooth Hair Curves'], Amount=1.0, Iterations=30, Weight=0.5, Preserve_Length=True)
    if fix == "blend":    t.eg(EG['Blend Hair Curves'], Factor=1.0, Blend_Radius=0.01, Blend_Neighbors=10, Preserve_Length=True)
    if fix == "straight": t.eg(EG['Straighten Hair Curves'], Amount=0.5, Shape=0.0, Preserve_Length=True)
    if fix == "rotate":   t.eg(EG['Rotate Hair Curves'], Factor=1.0, Angle=0.0, Random_Offset=0.6, Seed=3)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.55, redness=0.55))
run_variants("38b_smooth", [
    ("Smooth 20 iter Shape 0", dict(fix="sshape0.0", _guides=dict(G))),
    ("Smooth 20 iter Shape 0.5", dict(fix="sshape0.5", _guides=dict(G))),
    ("Smooth 20 iter Shape 0.8", dict(fix="sshape0.8", _guides=dict(G))),
], build, cols=3, **FR)
