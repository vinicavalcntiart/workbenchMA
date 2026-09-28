import sys; sys.path.insert(0,'.')
from lab import *
CAM = dict(cam_loc=(0.42,-0.55,0.16), target=(0,0,0.0), lens=55)
def fur_mat(mel=0.25, red=0.9):
    return hair_mat("fur", melanin=mel, redness=red, roughness=0.35)
def branch(t, EG, geo_in, dens, gd, factor, shape, tip, length_factor, radius, seed):
    """Um ramo: Interpolate -> Clump -> Trim -> Profile, a partir de geo_in; devolve socket de saida."""
    it = t.add('GeometryNodeGroup', group=EG['Interpolate Hair Curves'], Seed=seed)
    t.link(geo_in, it.inputs['Geometry']); t.link(value(t, dens), it.inputs['Density']); out = it.outputs['Geometry']
    if factor > 0:
        c = t.add('GeometryNodeGroup', group=EG['Clump Hair Curves'], Factor=factor, Shape=shape, Tip_Spread=tip,
                  Preserve_Length=True, Guide_Distance=gd, Existing_Guide_Map=False, Seed=seed+1)
        t.link(out, c.inputs['Geometry']); out = c.outputs['Geometry']
    if length_factor != 1.0:
        tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=length_factor, Scale_Uniform=True, Random_Offset=0.2)
        t.link(out, tr.inputs['Geometry']); out = tr.outputs['Geometry']
    pr = t.add('GeometryNodeGroup', group=EG['Set Hair Curve Profile'], Radius=radius, Shape=0.5, Factor_Min=0.0, Factor_Max=1.0)
    t.link(out, pr.inputs['Geometry']); return pr.outputs['Geometry']
def build_fur(mode):
    EG, body, g = fur_scene(n=600, length=0.035)
    t = Tree("fur")
    if mode == "fino":
        o = branch(t, EG, t.gi.outputs[0], 3e6, 0.0, 0.0, 0.5, 0.0, 1.0, 0.00015, 1)
    elif mode == "tufos":
        o = branch(t, EG, t.gi.outputs[0], 1.5e6, 0.008, 1.0, 0.25, 0.001, 1.0, 0.0003, 1)
    elif mode == "tufos_pontudos":
        o = branch(t, EG, t.gi.outputs[0], 1.5e6, 0.012, 1.0, 0.0, 0.0, 1.0, 0.0004, 1)
    elif mode == "duas_camadas":
        under = branch(t, EG, t.gi.outputs[0], 3e6, 0.0, 0.0, 0.5, 0.0, 0.45, 0.00015, 1)
        top = branch(t, EG, t.gi.outputs[0], 6e5, 0.01, 1.0, 0.25, 0.001, 1.15, 0.00035, 5)
        j = t.add('GeometryNodeJoinGeometry'); t.link(top, j.inputs[0]); t.link(under, j.inputs[0]); o = j.outputs[0]
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = fur_mat()
    t.link(o, sm.inputs['Geometry']); t.geo = sm.outputs['Geometry']
    apply_tree(g, t.finish()); return g
paths=[]; labels=[]
for mode, lb in [("fino","fino sem clump, 3M/m2"),("tufos","tufos GD 8mm Shape .25"),("tufos_pontudos","tufos pontudos GD 12mm Shape 0"),("duas_camadas","subpelo 45% + topo clump x1.15")]:
    g = build_fur(mode); st = stats(g); print("INFO", mode, st.get('curves'))
    paths.append(shot(f"14_fur_{mode}", res=480, samples=16, **CAM)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT, "14_fur_sheet.png"), cols=4))
