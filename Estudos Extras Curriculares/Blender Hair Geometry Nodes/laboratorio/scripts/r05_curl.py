import sys; sys.path.insert(0,'.')
from lab import *
G = dict(spread=0.45, gravity=2.2, outward=0.45, length=0.24)
def build(t, EG, g=None, scalp=None, order="clump>curl", rad=0.012, freq=1.0, roff=0.25, sub=2, radius=0.0005):
    interp(t, EG, density=250000.0)
    def clump(): t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
                      Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    def curl(): t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=sub, Curl_Start=0.1, Radius=rad, Frequency=freq,
                     Random_Offset=roff, Guide_Distance=0.02, Existing_Guide_Map=True, Seed=3)
    if order=="clump>curl": clump(); curl()
    elif order=="curl>clump": curl(); clump()
    else: curl()
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("ruivo", melanin=0.35, redness=0.95, roughness=0.3))
run_variants("05_curl", [
    ("so Curl r1.2cm f1", dict(order="curl", _guides=G)),
    ("Clump > Curl", dict(order="clump>curl", _guides=G)),
    ("Curl > Clump", dict(order="curl>clump", _guides=G)),
    ("Clump > Curl f3", dict(order="clump>curl", freq=3.0, _guides=G)),
    ("Clump > Curl f3 RandOff 0", dict(order="clump>curl", freq=3.0, roff=0.0, _guides=G)),
    ("Clump > Curl f3 r0.6cm", dict(order="clump>curl", freq=3.0, rad=0.006, _guides=G)),
], build, cols=3)
