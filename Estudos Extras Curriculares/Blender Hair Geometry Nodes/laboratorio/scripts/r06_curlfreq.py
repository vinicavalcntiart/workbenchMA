import sys; sys.path.insert(0,'.')
from lab import *
G = dict(spread=0.45, gravity=2.2, outward=0.45, length=0.24)
def build(t, EG, g=None, scalp=None, rad=0.01, freq=10.0, roff=0.25, sub=3, fend=1.0, clump=True, radius=0.0005):
    interp(t, EG, density=250000.0)
    if clump: t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
                    Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=sub, Curl_Start=0.1, Radius=rad, Frequency=freq,
         Factor_End=fend, Random_Offset=roff, Guide_Distance=0.02, Existing_Guide_Map=True, Seed=3)
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("ruivo", melanin=0.35, redness=0.95, roughness=0.3))
run_variants("06_curlfreq", [
    ("Freq 5 (15 voltas/m)", dict(freq=5.0, _guides=G)),
    ("Freq 10 (30 voltas/m)", dict(freq=10.0, _guides=G)),
    ("Freq 15", dict(freq=15.0, _guides=G)),
    ("Freq 20 r 0.7cm", dict(freq=20.0, rad=0.007, _guides=G)),
    ("Freq 10 FactorEnd 0.4", dict(freq=10.0, fend=0.4, _guides=G)),
    ("Freq 10 sem Clump", dict(freq=10.0, clump=False, _guides=G)),
], build, cols=3)
