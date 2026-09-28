import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.22, gravity=4.0, spread=0.3, outward=0.35, n_guides=200)
FR = dict(cam_loc=(0.42,-0.62,0.02), target=(0,0,-0.08), lens=50)
def build(t, EG, g=None, scalp=None, rl=0.06, rr=0.02, rd=(0,0,0), ro=0.5, taper=0.0, keep=0.0):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Roll Hair Curves'], Factor=1.0, Subdivision=2, Roll_Length=rl, Roll_Radius=rr, Roll_Direction=rd, Random_Orientation=ro,
         Roll_Taper=taper, Retain_Overall_Shape=keep, Preserve_Length=True, Seed=2)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.75, redness=0.5))
run_variants("22_roll", [
    ("Roll 6cm r2cm (padrao dir)", dict(_guides=dict(G))),
    ("Random Orientation 0", dict(ro=0.0, _guides=dict(G))),
    ("Roll Direction Z (0,0,1)", dict(rd=(0,0,1), ro=0.0, _guides=dict(G))),
    ("Roll Direction X (1,0,0)", dict(rd=(1,0,0), ro=0.0, _guides=dict(G))),
    ("Roll 10cm r1.5cm Taper 0.5", dict(rl=0.10, rr=0.015, taper=0.5, _guides=dict(G))),
    ("Retain Overall Shape 1", dict(keep=1.0, _guides=dict(G))),
], build, cols=3, **FR)
