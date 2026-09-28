import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.28, gravity=3.0, spread=0.35, outward=0.45, n_guides=200)
def build(t, EG, g=None, scalp=None, seed=0, style="curly"):
    # Seed mestre: um Integer que soma um deslocamento fixo em cada node
    S = t.add('FunctionNodeInputInt'); S.integer = seed
    def sd(off):
        m = t.add('FunctionNodeIntegerMath', props={'operation':'ADD'}); t.link(S.outputs[0], m.inputs[0]); m.inputs[1].default_value = off
        return m.outputs[0]
    it = interp(t, EG, density=300000.0); t.link(sd(0), it.inputs['Seed'])
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
             Guide_Distance=0.02, Existing_Guide_Map=False); t.link(sd(1), c.inputs['Seed'])
    if style != "liso":
        cu = t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=3, Curl_Start=0.1, Radius=0.011, Frequency=9.0 if style=="curly" else 3.0,
                  Random_Offset=0.25, Existing_Guide_Map=True); t.link(sd(2), cu.inputs['Seed'])
        na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
        r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.7, Max=1.4)
        t.link(na.outputs['Attribute'], r.inputs['ID']); t.link(sd(3), r.inputs['Seed'])
        mul = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); mul.inputs[1].default_value = 0.011
        t.link(r.outputs['Value'], mul.inputs[0]); t.link(mul.outputs[0], cu.inputs['Radius'])
    ci = t.add('GeometryNodeGroup', group=EG['Curve Info'])
    cmp = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}, B=0.04)
    t.link(ci.outputs['Random'], cmp.inputs['A'])
    n = t.eg(EG['Hair Curves Noise'], Distance=0.04, Shape=0.7, Scale=3.0, Offset_per_Curve=1.0, Cumulative_Offset=True, Preserve_Length=True)
    t.link(cmp.outputs['Result'], n.inputs['Factor']); t.link(sd(4), n.inputs['Seed'])
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("h", melanin=0.45 if style!="curly" else 0.3, redness=0.6 if style!="curly" else 1.0, roughness=0.3))
V = []
for s in (0, 17, 42): V.append((f"cacheado seed {s}", dict(seed=s, style="curly", _guides=dict(G))))
for st in ("liso", "ondulado"): V.append((f"{st} seed 0 (mesma arvore)", dict(seed=0, style=st, _guides=dict(G))))
V.append(("cacheado seed 0, guias seed 5", dict(seed=0, style="curly", _guides=dict(G, seed=5))))
run_variants("13_seed", V, build, cols=3)
