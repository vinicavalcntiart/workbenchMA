import sys; sys.path.insert(0,'.')
exec(open('r28_dyn.py').read().split("def run(")[0])
def trial(label, coll=False, guides=None, substeps=10, iters=15, frames=24, rootb=0.2, bend=0.5, head_collider=False, margin=0.002):
    EG, head, scalp, g = base_scene(**(guides or dict(G)))
    attach_uv(g, scalp)
    with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics', 'Collider']
    coll_col = None
    if head_collider:
        coll_col = bpy.data.collections.new("colisores"); bpy.context.scene.collection.children.link(coll_col)
        bpy.context.scene.collection.objects.unlink(head); coll_col.objects.link(head)
        tc = Tree("col"); cn = tc.add('GeometryNodeGroup', group=bpy.data.node_groups['Collider']); tc.chain(cn)
        cn.inputs['Deforming'].default_value = False; cn.inputs['Margin'].default_value = margin
        apply_tree(head, tc.finish())
    t1 = Tree("sim"); hd = t1.add('GeometryNodeGroup', group=bpy.data.node_groups['Hair Dynamics'])
    t1.ng.links.new(t1.geo, hd.inputs['Hair']); t1.geo = hd.outputs['Hair']
    hd.inputs['Mode'].default_value = 'Physics (Experimental)'; hd.inputs['Surface Collision'].default_value = coll; hd.inputs['Deforming'].default_value = False
    hd.inputs['Substeps'].default_value = substeps; hd.inputs['Constraint Steps'].default_value = iters
    hd.inputs['Root Bendiness'].default_value = rootb; hd.inputs['Bendiness'].default_value = bend
    if coll_col: hd.inputs['Effectors Collection'].default_value = coll_col
    apply_tree(g, t1.finish())
    sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=frames; sc.frame_set(1)
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P0 = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P0); P0=P0.reshape(-1,3)
    roots0 = np.array([c.first_point_index for c in d.curves]); tips0 = np.array([c.first_point_index+c.points_length-1 for c in d.curves])
    line=[]
    for f in range(2, frames+1):
        sc.frame_set(f)
        if f in (3,5,10,frames):
            d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
            P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
            line.append(f"f{f}: raiz {np.linalg.norm(P[roots0]-P0[roots0],axis=1).max()*100:.1f} ponta dz {(P[tips0,2]-P0[tips0,2]).mean()*100:+.1f}")
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    inside = (np.linalg.norm(P,axis=1) < 0.0985).sum()
    print("DD", label, "|", "; ".join(line), f"| pontos dentro da cabeca: {inside} de {len(P)}")
G2 = dict(spread=0.1, gravity=0.3, outward=0.9, length=0.24, n_guides=260)   # guias apontando p/ fora: vao cair em cima da cabeca
trial("sem colisao, guias p/ fora", guides=G2, frames=36)
trial("Collider na cabeca, guias p/ fora", guides=G2, head_collider=True, frames=36)
