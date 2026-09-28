import sys; sys.path.insert(0,'.')
exec(open('t_perf.py').read().split("for dens in")[0])
D = {n:f for n,f in STEPS}
orders = {
 "ingenua: Clump Noise Frizz Curl Trim Profile": ["+ Clump","+ Noise","+ Frizz","+ Curl Sub 2","+ Trim","+ Profile"],
 "otimizada: Clump Trim Noise Frizz Profile Curl": ["+ Clump","+ Trim","+ Noise","+ Frizz","+ Profile","+ Curl Sub 2"],
}
for dens in (1200000.0,):
    for lb, seq in orders.items():
        EG, head, scalp, g = base_scene()
        t = Tree("p"); interp(t, EG, density=dens)
        for n in seq: D[n](t, EG)
        apply_tree(g, t.finish()); bpy.context.evaluated_depsgraph_get()
        print(f"PERF2 {lb:48s} {timed(g)*1000:6.0f} ms")
    # viewport amount
    for va in (1.0, 0.25):
        EG, head, scalp, g = base_scene()
        t = Tree("p"); it = interp(t, EG, density=dens, Viewport_Amount=va)
        for n in orders["otimizada: Clump Trim Noise Frizz Profile Curl"]: D[n](t, EG)
        apply_tree(g, t.finish()); bpy.context.evaluated_depsgraph_get()
        print(f"PERF2 viewport amount {va}: {timed(g)*1000:6.0f} ms  fios {stats(g).get('curves')}")
