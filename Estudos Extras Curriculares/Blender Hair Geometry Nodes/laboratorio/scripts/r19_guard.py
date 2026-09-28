import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
exec(open('r14_fur.py').read().split("def build_fur")[0].split("from lab import *",1)[1])
def build(mode):
    EG, body, g = fur_scene(n=600, length=0.035)
    t = Tree("fur")
    base = branch(t, EG, t.gi.outputs[0], 1.5e6, 0.008, 1.0, 0.25, 0.001, 1.0, 0.0003, 1)
    outs = [base]
    if mode in ("guarda", "guarda+buracos"):
        # guard hairs: pouca densidade, 40% mais longos, 3x mais grossos, sem clump
        guard = branch(t, EG, t.gi.outputs[0], 3e4, 0.0, 0.0, 0.5, 0.0, 1.4, 0.0009, 9)
        outs.append(guard)
    if mode in ("buracos", "guarda+buracos"):
        # buracos: apaga tufos inteiros por mecha (Random por guia < 0.18)
        na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index")
        r = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}, Probability=0.18, Seed=3)
        t.link(na.outputs['Attribute'], r.inputs['ID'])
        dl = t.add('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); t.link(base, dl.inputs['Geometry']); t.link(r.outputs[3] if len(r.outputs)>3 else r.outputs['Value'], dl.inputs['Selection'])
        outs[0] = dl.outputs['Geometry']
    j = t.add('GeometryNodeJoinGeometry')
    for o in outs: t.link(o, j.inputs[0])
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = fur_mat(); t.link(j.outputs[0], sm.inputs['Geometry']); t.geo = sm.outputs['Geometry']
    apply_tree(g, t.finish()); return g
paths=[]; labels=[]
for mode, lb in [("base","tufos (base)"),("guarda","+ pelo de guarda (3x grosso, 1.4x longo)"),("buracos","+ buracos: 18% dos tufos apagados"),("guarda+buracos","guarda + buracos")]:
    g = build(mode); print("INFO", mode, stats(g).get('curves'))
    paths.append(shot(f"19_guard_{mode}", res=480, samples=16, **CAM)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT, "19_guard_sheet.png"), cols=4))
