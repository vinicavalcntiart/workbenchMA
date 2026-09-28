import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
G = dict(spread=0.5, gravity=1.8, outward=0.6, length=0.24, n_guides=220)
FR = dict(cam_loc=(0.30,-0.45,0.0), target=(0.02,0,-0.06), lens=60)
def build(t, EG, g=None, scalp=None, sub=3, resample=0):
    interp(t, EG, density=250000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    if resample: t.chain(t.add('GeometryNodeResampleCurve', Count=resample), 'Curve', 'Curve')
    t.eg(EG['Curl Hair Curves'], Factor=1.0, Subdivision=sub, Curl_Start=0.08, Radius=0.011, Frequency=10.0, Random_Offset=0.25, Existing_Guide_Map=True, Seed=3)
    profile(t, EG, radius=0.0006)
    set_mat(t, hair_mat("r", melanin=0.3, redness=1.0))
V=[("Sub 1", dict(sub=1)),("Sub 2", dict(sub=2)),("Sub 3", dict(sub=3)),("Resample 30 + Sub 0", dict(sub=0, resample=30)),("Resample 40 + Sub 0", dict(sub=0, resample=40)),("Resample 24 + Sub 1", dict(sub=1, resample=24))]
paths=[]; labels=[]
for lb, kw in V:
    EG, head, scalp, g = base_scene(**dict(G)); t = Tree("p"); build(t, EG, g=g, scalp=scalp, **kw); apply_tree(g, t.finish())
    t0=time.perf_counter(); g.data.update_tag(); bpy.context.evaluated_depsgraph_get().update(); ev=(time.perf_counter()-t0)*1000
    st = stats(g); ppc = st['points']//st['curves']
    p = shot("26_"+str(len(paths)), res=400, samples=12, **FR)
    rt = render(p)
    print(f"PTS {lb:22s} pontos/fio {ppc:3d} total {st['points']/1e6:.2f} M  avaliacao {ev:.0f} ms  render {rt}s")
    paths.append(p); labels.append(f"{lb}: {ppc} pts/fio, render {rt}s")
print("SHEET", sheet(paths, labels, os.path.join(OUT,"26_pts_sheet.png"), cols=3))
