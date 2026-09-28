import sys; sys.path.insert(0,'.')
from lab import *
BACK = dict(cam_loc=(-0.38,0.55,0.02), target=(0,0,-0.08), lens=55)
def build(t, EG, g=None, scalp=None, shape=0.5, tip=0.0, off=0.0, fall=0.0, radius=0.0005, gd=0.02):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=shape, Tip_Spread=tip, Clump_Offset=off,
         Distance_Falloff=fall, Preserve_Length=True, Guide_Distance=gd, Existing_Guide_Map=False, Seed=1)
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4))
run_variants("03_shape", [
    ("Shape 0.5 (padrao)", dict(shape=0.5)),
    ("Shape 0", dict(shape=0.0)),
    ("Shape -0.5", dict(shape=-0.5)),
    ("Shape 0 + Tip Spread 0.005", dict(shape=0.0, tip=0.005)),
    ("Shape 0 + Offset 0.004", dict(shape=0.0, off=0.004)),
    ("Shape 0 + Falloff 0.01", dict(shape=0.0, fall=0.01)),
], build, cols=3, **BACK)
