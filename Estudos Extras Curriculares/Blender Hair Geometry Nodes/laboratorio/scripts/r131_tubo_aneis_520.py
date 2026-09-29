import bpy, sys, math
def P(*a): print(*a); sys.stdout.flush()
V = sys.argv[-1]; OUT = "/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/fillet/" + V + ".png"
bpy.ops.wm.read_homefile(use_empty=True)
sc = bpy.context.scene
me = bpy.data.meshes.new("V"); vs = [(-1.6,0.35,0),(0,-0.25,0),(1.3,0.15,0),(1.8,1.0,0)]
me.from_pydata(vs, [(0,1),(1,2),(2,3)], []); ob = bpy.data.objects.new("V", me); sc.collection.objects.link(ob)
ng = bpy.data.node_groups.new("tubo", 'GeometryNodeTree')
ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'); ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
N = ng.nodes; L = ng.links.new
gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput'); m2c = N.new('GeometryNodeMeshToCurve')
cc = N.new('GeometryNodeCurvePrimitiveCircle'); cc.inputs['Radius'].default_value = 0.1; cc.inputs['Resolution'].default_value = 6
c2m = N.new('GeometryNodeCurveToMesh'); c2m.inputs['Fill Caps'].default_value = True
L(gi.outputs[0], m2c.inputs['Mesh']); cur = m2c.outputs[0]
if V == "fillet":
    f = N.new('GeometryNodeFilletCurve'); f.inputs['Radius'].default_value = 0.35
    try: f.mode = 'POLY'
    except Exception: pass
    for s in f.inputs:
        if s.name == 'Count': s.default_value = 12
        if s.name == 'Mode':
            try: s.default_value = 'Poly'
            except Exception as e: P("mode", e)
    P("INFO fillet inputs", [(s.name, getattr(s,'default_value',None)) for s in f.inputs if s.name!='Curve'])
    L(cur, f.inputs['Curve']); cur = f.outputs[0]
    rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.08
    L(cur, rs.inputs['Curve']); cur = rs.outputs[0]
elif V == "bezier":
    st = N.new('GeometryNodeCurveSplineType'); st.spline_type = 'BEZIER'; ht = N.new('GeometryNodeCurveSetHandles'); ht.handle_type = 'AUTO'
    rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.08
    L(cur, st.inputs['Curve']); L(st.outputs[0], ht.inputs['Curve']); L(ht.outputs[0], rs.inputs['Curve']); cur = rs.outputs[0]
elif V in ("cat_sub", "cat_len"):
    st = N.new('GeometryNodeCurveSplineType'); st.spline_type = 'CATMULL_ROM'; L(cur, st.inputs['Curve']); cur = st.outputs[0]
    if V == "cat_sub":
        sd = N.new('GeometryNodeSubdivideCurve'); sd.inputs['Cuts'].default_value = 3; L(cur, sd.inputs['Curve']); cur = sd.outputs[0]
    else:
        rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.15; L(cur, rs.inputs['Curve']); cur = rs.outputs[0]
elif V == "blur":
    rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.08
    L(cur, rs.inputs['Curve']); cur = rs.outputs[0]
    pos = N.new('GeometryNodeInputPosition'); bl = N.new('GeometryNodeBlurAttribute'); bl.data_type = 'FLOAT_VECTOR'; bl.inputs['Iterations'].default_value = 8
    ends = N.new('GeometryNodeCurveEndpointSelection'); nt = N.new('FunctionNodeBooleanMath'); nt.operation = 'NOT'
    L(pos.outputs[0], [s for s in bl.inputs if s.name=='Value' and s.type=='VECTOR'][0])
    sp = N.new('GeometryNodeSetPosition'); L(cur, sp.inputs['Geometry']); L([o for o in bl.outputs if o.type=='VECTOR'][0], sp.inputs['Position'])
    L(ends.outputs[0], nt.inputs[0]); L(nt.outputs[0], sp.inputs['Selection']); cur = sp.outputs[0]
L(cur, c2m.inputs['Curve']); L(cc.outputs['Curve'], c2m.inputs['Profile Curve'])
sh = N.new('GeometryNodeSetShadeSmooth'); sh.inputs['Shade Smooth'].default_value = False
L(c2m.outputs[0], sh.inputs['Geometry']); L(sh.outputs[0], go.inputs[0])
ob.modifiers.new("GN", 'NODES').node_group = ng
mat = bpy.data.materials.new("m"); mat.diffuse_color = (0.8,0.8,0.8,1); ob.data.materials.append(mat)
wf = ob.copy(); sc.collection.objects.link(wf); wm = wf.modifiers.new("W", 'WIREFRAME'); wm.thickness = 0.012
mk = bpy.data.materials.new("k"); mk.use_nodes = True; mk.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.02,0.02,0.02,1); wf.data = ob.data.copy(); wf.data.materials.clear(); wf.data.materials.append(mk)
dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg).data; P("RESULT", V, "verts", len(ev.vertices))
# render Cycles CPU, camera de cima, luz + wire por Freestyle desligado
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.location = (0.1, -1.6, 4.2); cam.rotation_euler = (math.radians(22), 0, 0); cam.data.lens = 38
sun = bpy.data.objects.new("sun", bpy.data.lights.new("sun", 'SUN')); sun.data.energy = 3; sun.rotation_euler = (0.6, 0.3, 0.4); sc.collection.objects.link(sun)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (0.18,0.18,0.2,1)
sc.render.engine = 'CYCLES'; sc.cycles.samples = 16; sc.render.resolution_x = 700; sc.render.resolution_y = 420
sc.render.use_freestyle = False; sc.render.line_thickness = 0.8
sc.view_layers[0].freestyle_settings.linesets.new("l") if not sc.view_layers[0].freestyle_settings.linesets else None
ls = sc.view_layers[0].freestyle_settings.linesets[0]; ls.select_by_visibility = True; ls.select_crease = True; ls.select_silhouette = True; ls.select_border = True
sc.view_layers[0].freestyle_settings.crease_angle = math.radians(179)
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True); P("RESULT render", OUT)
