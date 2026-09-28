import sys; sys.path.insert(0,'.')
from lab import *
MAT = None
def build(t, EG, g=None, scalp=None, mode=0, radius=0.0003):
    interp(t, EG, density=300000.0)
    if mode >= 1:
        t.eg(EG['Clump Hair Curves'], Factor=0.5 if mode==3 else 1.0, Shape=0.5, Tip_Spread=0.0,
             Preserve_Length=True, Guide_Distance=0.03, Existing_Guide_Map=False, Seed=1)
    if mode == 3:
        t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.5, Preserve_Length=True,
             Guide_Distance=0.008, Existing_Guide_Map=False, Seed=7)
    if mode == 2:
        pass
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4))
run_variants("02_clump", [
    ("sem clump", dict(mode=0)),
    ("1 clump GD 3cm F1", dict(mode=1)),
    ("1 clump + raio 0.8mm", dict(mode=1, radius=0.0008)),
    ("2 niveis 3cm F0.5 > 8mm F1", dict(mode=3)),
], build, cols=4)
