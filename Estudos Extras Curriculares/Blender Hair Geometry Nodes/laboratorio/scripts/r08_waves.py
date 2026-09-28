import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.34, gravity=4.5, spread=0.25, outward=0.3, n_guides=200)
def build(t, EG, g=None, scalp=None, kind="noise", sc=1.0, sal=1.0, dist=0.015, opc=0.0, freq=3.0, rad=0.015):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    if kind == "noise":
        t.eg(EG['Hair Curves Noise'], Factor=1.0, Distance=dist, Shape=0.5, Scale=sc, Scale_along_Curve=sal,
             Offset_per_Curve=opc, Preserve_Length=True, Cumulative_Offset=False, Seed=2)
    else:
        t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=2, Curl_Start=0.15, Radius=rad, Frequency=freq,
             Random_Offset=0.25, Guide_Distance=0.02, Existing_Guide_Map=True, Seed=3)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("loiro", melanin=0.18, redness=0.35, roughness=0.25))
FR = dict(cam_loc=(0.30,-0.62,-0.02), target=(0,0,-0.12), lens=45)
run_variants("08_waves", [
    ("Noise Scale 1 SaC 1", dict(sc=1.0, sal=1.0, _guides=dict(G))),
    ("Noise Scale 10 SaC 3", dict(sc=10.0, sal=3.0, _guides=dict(G))),
    ("Noise Scale 10 SaC 8", dict(sc=10.0, sal=8.0, _guides=dict(G))),
    ("Noise Scale 30 SaC 8", dict(sc=30.0, sal=8.0, _guides=dict(G))),
    ("Curl f3 r1.5cm (onda)", dict(kind="curl", _guides=dict(G))),
    ("Curl f5 r1cm", dict(kind="curl", freq=5.0, rad=0.01, _guides=dict(G))),
], build, cols=3, **FR)
