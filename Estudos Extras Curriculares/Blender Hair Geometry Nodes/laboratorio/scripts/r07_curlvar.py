import sys; sys.path.insert(0,'.')
from lab import *
G = dict(spread=0.5, gravity=1.8, outward=0.6, length=0.24, n_guides=220)
def rnd_by_guide(t, lo, hi, seed):
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
    r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=lo, Max=hi, Seed=seed)
    t.link(na.outputs['Attribute'], r.inputs['ID']); return r.outputs['Value']
def rnd_per_curve(t, lo, hi, seed):
    r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=lo, Max=hi, Seed=seed); return r.outputs['Value']
def build(t, EG, g=None, scalp=None, var=None, dens=400000.0, radius=0.0006):
    interp(t, EG, density=dens)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
         Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    c = t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=3, Curl_Start=0.08, Radius=0.011, Frequency=9.0,
             Random_Offset=0.25, Guide_Distance=0.02, Existing_Guide_Map=True, Seed=3)
    if var == "mecha":
        t.link(rnd_by_guide(t, 0.007, 0.016, 11), c.inputs['Radius'])
        t.link(rnd_by_guide(t, 6.0, 13.0, 12), c.inputs['Frequency'])
    elif var == "fio":
        t.link(rnd_per_curve(t, 0.007, 0.016, 11), c.inputs['Radius'])
        t.link(rnd_per_curve(t, 6.0, 13.0, 12), c.inputs['Frequency'])
    profile(t, EG, radius=radius)
    set_mat(t, hair_mat("ruivo", melanin=0.3, redness=1.0, roughness=0.28))
run_variants("07_curlvar", [
    ("Curl fixo r1.1cm f9", dict(_guides=dict(G))),
    ("Random por MECHA (ID=guia)", dict(var="mecha", _guides=dict(G))),
    ("Random por FIO", dict(var="fio", _guides=dict(G))),
], build, cols=3, res=560, samples=20)
