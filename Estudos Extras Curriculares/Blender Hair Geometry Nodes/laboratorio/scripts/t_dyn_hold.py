import sys; sys.path.insert(0,'.')
exec(open('r28_dyn.py').read().split("def run(")[0])
G.update(dict(spread=0.35, gravity=0.8, outward=0.8, length=0.22))
def hold(label, bend=0.05, rootb=0.02, mass=0.01, grav=-9.81, iters=15, frames=36, sub=10):
    EG, head, scalp, g = base_scene(**dict(G)); attach_uv(g, scalp)
    with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics']
    t1 = Tree("sim"); hd = t1.add('GeometryNodeGroup', group=bpy.data.node_groups['Hair Dynamics'])
    t1.ng.links.new(t1.geo, hd.inputs['Hair']); t1.geo = hd.outputs['Hair']
    hd.inputs['Mode'].default_value = 'Physics (Experimental)'
    for k,v in (('Bendiness',bend),('Root Bendiness',rootb),('Mass',mass),('Constraint Steps',iters),('Substeps',sub)): hd.inputs[k].default_value = v
    for s in hd.inputs:
        if s.name=='Gravity' and s.type=='VECTOR': s.default_value = (0,0,grav)
    apply_tree(g, t1.finish())
    sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=frames; sc.frame_set(1); T0,_ = guide_tips(g)
    t0=time.perf_counter()
    for f in range(2, frames+1): sc.frame_set(f)
    dt=(time.perf_counter()-t0)/(frames-1)*1000
    T1,_ = guide_tips(g); print(f"HOLD {label:36s} ponta desce {(T0[:,2]-T1[:,2]).mean()*100:5.1f} cm   {dt:.0f} ms/quadro (260 guias)")
hold("padrao (Steps 15, Sub 10)", bend=0.0, rootb=0.0)
hold("Steps 60", bend=0.0, rootb=0.0, iters=60)
hold("Steps 120", bend=0.0, rootb=0.0, iters=120)
hold("Substeps 40, Steps 15", bend=0.0, rootb=0.0, sub=40)
hold("Steps 60 + gravidade 1/4", bend=0.0, rootb=0.0, iters=60, grav=-2.45)
