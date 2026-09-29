import bpy, sys, statistics as S
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.read_homefile(use_empty=True)
me = bpy.data.meshes.new("V"); vs = [(-1.6,0.35,0),(0,-0.25,0),(1.3,0.15,0),(1.8,1.0,0)]
me.from_pydata(vs, [(0,1),(1,2),(2,3)], []); ob = bpy.data.objects.new("V", me); bpy.context.scene.collection.objects.link(ob)
def run(kind):
    ng = bpy.data.node_groups.new(kind, 'GeometryNodeTree')
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'); ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    N = ng.nodes; L = ng.links.new; gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput'); m2c = N.new('GeometryNodeMeshToCurve')
    L(gi.outputs[0], m2c.inputs['Mesh']); cur = m2c.outputs[0]
    if kind.startswith("catmull") or kind.startswith("bezier"):
        st = N.new('GeometryNodeCurveSplineType'); st.spline_type = 'CATMULL_ROM' if kind.startswith("catmull") else 'BEZIER'
        L(cur, st.inputs['Curve']); cur = st.outputs[0]
        if kind.startswith("bezier"):
            ht = N.new('GeometryNodeCurveSetHandles'); ht.handle_type = 'AUTO'; L(cur, ht.inputs['Curve']); cur = ht.outputs[0]
    if kind.endswith("sub"):   # subdivide: segue o tamanho de cada trecho original
        sd = N.new('GeometryNodeSubdivideCurve'); sd.inputs['Cuts'].default_value = 3; L(cur, sd.inputs['Curve']); cur = sd.outputs[0]
    if kind.endswith("len"):
        rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.15; L(cur, rs.inputs['Curve']); cur = rs.outputs[0]
    if kind.endswith("res"):   # resolucao da propria spline (Set Spline Resolution) -> Curve to Points Evaluated
        sr = N.new('GeometryNodeSetSplineResolution'); sr.inputs['Resolution'].default_value = 4; L(cur, sr.inputs['Geometry']); cur = sr.outputs[0]
        c2p = N.new('GeometryNodeCurveToPoints'); c2p.mode = 'EVALUATED'; L(cur, c2p.inputs['Curve']); cur = c2p.outputs['Points']
    L(cur, go.inputs[0])
    m = ob.modifiers.new(kind, 'NODES'); m.node_group = ng
    dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg)
    gs = ev.evaluated_geometry()
    if kind.endswith("res"):
        pc = gs.pointcloud; pts = [pc.points[i].co.copy() for i in range(len(pc.points))]
    else:
        cd = gs.curves; pts = [cd.points[i].position.copy() for i in range(len(cd.points))]
    d = [(pts[i+1]-pts[i]).length for i in range(len(pts)-1)]
    P("RESULT", kind.ljust(16), "pontos", len(pts), "espacamento min", round(min(d),3), "max", round(max(d),3), "variacao max/min", round(max(d)/min(d),2))
    ob.modifiers.remove(m)
for k in ("bezier_res", "catmull_sub", "catmull_len", "bezier_len"): run(k)
