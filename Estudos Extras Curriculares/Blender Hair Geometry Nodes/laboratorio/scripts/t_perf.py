import sys; sys.path.insert(0,'.')
from lab import *
def timed(g, reps=3):
    ts=[]
    for i in range(reps):
        g.data.update_tag(); t0=time.perf_counter(); dg=bpy.context.evaluated_depsgraph_get(); dg.update(); ts.append(time.perf_counter()-t0)
    return sorted(ts)[len(ts)//2]
STEPS = [
 ("Interpolate", lambda t,EG: None),
 ("+ Clump", lambda t,EG: t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=0.02, Existing_Guide_Map=False, Preserve_Length=True)),
 ("+ Noise", lambda t,EG: t.eg(EG['Hair Curves Noise'], Distance=0.01, Scale=10.0, Scale_along_Curve=8.0)),
 ("+ Frizz", lambda t,EG: t.eg(EG['Frizz Hair Curves'], Distance=0.003)),
 ("+ Curl Sub 2", lambda t,EG: t.eg(EG['Curl Hair Curves'], Subdivision=2, Radius=0.01, Frequency=9.0)),
 ("+ Trim", lambda t,EG: t.eg(EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=0.9)),
 ("+ Profile", lambda t,EG: t.eg(EG['Set Hair Curve Profile'], Radius=0.0005)),
]
for dens in (300000.0, 1200000.0):
    prev=0
    for k in range(len(STEPS)):
        EG, head, scalp, g = base_scene()
        t = Tree("p"); interp(t, EG, density=dens)
        for name, f in STEPS[1:k+1]: f(t, EG)
        apply_tree(g, t.finish()); bpy.context.evaluated_depsgraph_get()
        tt = timed(g); st = stats(g)
        print(f"PERF dens={int(dens)} {STEPS[k][0]:14s} total {tt*1000:7.0f} ms  (+{(tt-prev)*1000:6.0f})  fios {st.get('curves')} pontos {st.get('points')}")
        prev = tt
