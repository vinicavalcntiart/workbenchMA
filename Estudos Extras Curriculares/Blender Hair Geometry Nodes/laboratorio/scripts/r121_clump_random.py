"""Clump Factor variando por fio (padrao Blender Studio), 5.2:
Curve Info (Essentials) -> Random -> Map Range (0..1 -> min..max) -> Factor do Clump Hair Curves."""
import sys; sys.path.insert(0,'.')
from lab import *
def build(t, EG, g=None, scalp=None, lo=None, hi=None):
    interp(t, EG, density=300000.0)
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.5, Tip_Spread=0.0,
             Preserve_Length=True, Guide_Distance=0.03, Existing_Guide_Map=False, Seed=1)
    if lo is not None:
        ci = t.add('GeometryNodeGroup', group=EG['Curve Info'])
        mr = t.add('ShaderNodeMapRange'); mr.clamp = True
        mr.inputs['To Min'].default_value = lo; mr.inputs['To Max'].default_value = hi
        t.link(ci.outputs['Random'], mr.inputs['Value']); t.link(mr.outputs['Result'], c.inputs['Factor'])
    profile(t, EG, radius=0.0003)
    set_mat(t, hair_mat("c", melanin=0.7, redness=0.4))
run_variants("121_clump_random", [
    ("Factor fixo 1,0", dict()),
    ("Random -> Map Range 0,4 a 1,0", dict(lo=0.4, hi=1.0)),
    ("Random -> Map Range 0,0 a 1,0", dict(lo=0.0, hi=1.0)),
], build, cols=3, cam_loc=(0.30,-0.40,0.02), target=(0.02,0.0,-0.10), lens=60)
