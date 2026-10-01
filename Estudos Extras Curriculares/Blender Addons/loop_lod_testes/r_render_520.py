import bpy, bmesh, sys, math
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.open_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lodtest.blend")
sc = bpy.context.scene
names = ["Boneco_LOD0", "Boneco_LOD1", "Boneco_LOD2", "Boneco_LOD3"]
def mat(name, rgb, emit=0):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*rgb, 1)
    if emit: b.inputs['Emission Color'].default_value = (*rgb, 1); b.inputs['Emission Strength'].default_value = emit
    return m
M_body, M_wire, M_red, M_blue = mat("body", (0.75,0.75,0.75)), mat("wire", (0.02,0.02,0.02)), mat("red", (1,0.08,0.05), 2), mat("blue", (0.1,0.45,1), 2)
def make_tube(m):
    tube = bpy.data.node_groups.new("tubo_" + m.name, 'GeometryNodeTree')
    tube.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'); tube.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    N = tube.nodes; Lk = tube.links.new
    gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput'); m2c = N.new('GeometryNodeMeshToCurve'); cc = N.new('GeometryNodeCurvePrimitiveCircle'); cc.inputs['Radius'].default_value = 0.0045
    c2m = N.new('GeometryNodeCurveToMesh'); sm = N.new('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m
    Lk(gi.outputs[0], m2c.inputs['Mesh']); Lk(m2c.outputs[0], c2m.inputs['Curve']); Lk(cc.outputs['Curve'], c2m.inputs['Profile Curve']); Lk(c2m.outputs[0], sm.inputs['Geometry']); Lk(sm.outputs[0], go.inputs[0])
    return tube
def edges_obj(o, pick, m, name):
    me = o.data; vs = {}; verts = []; edges = []
    for e in me.edges:
        if pick(me, e):
            ids = []
            for i in e.vertices:
                if i not in vs: vs[i] = len(verts); verts.append(me.vertices[i].co.copy())
                ids.append(vs[i])
            edges.append(tuple(ids))
    nm = bpy.data.meshes.new(name); nm.from_pydata(verts, edges, []); nm.materials.append(m)
    ob = bpy.data.objects.new(name, nm); sc.collection.objects.link(ob); ob.modifiers.new("t", 'NODES').node_group = make_tube(m)
    ob.location = o.location; return ob
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.location = (0.62, -0.55, -0.32); cam.data.lens = 40
import mathutils
d = mathutils.Vector((0.52, 0, 0)) - cam.location; cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
sun = bpy.data.objects.new("sun", bpy.data.lights.new("sun", 'SUN')); sun.data.energy = 3.5; sun.rotation_euler = (0.9, 0.2, 0.6); sc.collection.objects.link(sun)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (0.16,0.16,0.18,1)
sc.render.engine = 'CYCLES'; sc.cycles.samples = 24; sc.render.resolution_x = 640; sc.render.resolution_y = 420
for n in names:
    for o in list(sc.objects):
        if o.type == 'MESH': o.hide_render = True
    o = bpy.data.objects[n]; o.hide_render = False
    if not o.data.materials: o.data.materials.append(M_body)
    else: o.data.materials[0] = M_body
    wf = o.copy(); wf.data = o.data.copy(); sc.collection.objects.link(wf); wf.data.materials.clear(); wf.data.materials.append(M_wire)
    wm = wf.modifiers.new("w", 'WIREFRAME'); wm.thickness = 0.0025; wf.hide_render = False
    gi_ = o.vertex_groups["LOD_Protect"].index
    def prot(me, e): return all(any(g.group == gi_ and g.weight >= 0.5 for g in me.vertices[i].groups) for i in e.vertices)
    r = edges_obj(o, prot, M_red, n + "_anel"); r.hide_render = False
    b = edges_obj(o, lambda me, e: e.use_seam, M_blue, n + "_seam"); b.hide_render = False
    tris = sum(len(f.vertices) - 2 for f in o.data.polygons)
    sc.render.filepath = f"/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lodimg/{n}.png"
    bpy.ops.render.render(write_still=True); P("RESULT", n, tris)
    for x in (wf, r, b): x.hide_render = True
