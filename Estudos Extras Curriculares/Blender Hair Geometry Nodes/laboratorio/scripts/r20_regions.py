import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(length=0.26, gravity=3.0, spread=0.35, outward=0.4, n_guides=220)
SIDE = dict(cam_loc=(0.55,-0.35,0.03), target=(0,0,-0.03), lens=55)
def top(co):  # 1 no topo, 0 nas laterais/nuca: suave entre z 0.02 e 0.05
    return (co.z - 0.02)/0.03
def build(t, EG, g=None, scalp=None, mode="none"):
    vgroup(scalp, "topo", top)
    interp(t, EG, density=300000.0)
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}, Name="topo")
    if mode in ("undercut", "undercut+clump"):
        # laterais curtas: Length = 0.03 + topo*... usando Trim com Replace Length e Mask = 1-topo
        inv = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); inv.inputs[0].default_value = 1.0; t.link(na.outputs['Attribute'], inv.inputs[1])
        tr = t.eg(EG['Trim Hair Curves'], Replace_Length=True, Length=0.025, Scale_Uniform=False, Random_Offset=0.004)
        t.link(inv.outputs[0], tr.inputs['Mask'])
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    if mode == "undercut+clump":
        t.link(na.outputs['Attribute'], c.inputs['Factor'])
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.8, redness=0.3))
EG0=None
run_variants("20_regions", [
    ("sem regiao", dict(mode="none", _guides=dict(G))),
    ("undercut: Trim Mask = 1-topo", dict(mode="undercut", _guides=dict(G))),
    ("undercut + Clump Factor = topo", dict(mode="undercut+clump", _guides=dict(G))),
], build, cols=3, **SIDE)
