import bpy, bmesh, sys, math, time
sys.path.insert(0, "/home/user/workbenchMA/Estudos Extras Curriculares/Blender Addons")
import loop_lod
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.read_homefile(use_empty=True)
loop_lod.register()
bm = bmesh.new(); uv = bm.loops.layers.uv.new("UVMap")
def tube(axis, start, end, rings, segs, radius, x0=0.0):
    rows = []
    for i in range(rings + 1):
        t = i / rings; p = start + (end - start) * t
        r = radius * (1.0 - 0.25 * math.sin(t * math.pi * 2) ** 2)   # forma com variacao (silhueta)
        row = []
        for j in range(segs):
            a = 2 * math.pi * j / segs
            if axis == 'X': co = (p, r * math.cos(a), r * math.sin(a))
            else: co = (r * math.cos(a), r * math.sin(a), p)
            row.append(bm.verts.new(co))
        rows.append(row)
    faces = []
    for i in range(rings):
        for j in range(segs):
            q = (rows[i][j], rows[i][(j+1)%segs], rows[i+1][(j+1)%segs], rows[i+1][j])
            f = bm.faces.new(q); faces.append((f, i, j))
            for k, l in enumerate(f.loops):
                ii = i + (1 if k >= 2 else 0); jj = j + (1 if k in (1, 2) else 0)
                l[uv].uv = (jj / segs, ii / rings)
    return rows
torso = tube('Z', -0.4, 0.4, 20, 24, 0.18)
armR = tube('X', 0.25, 0.85, 24, 16, 0.06)
armL = tube('X', -0.25, -0.85, 24, 16, 0.06)
bm.edges.ensure_lookup_table()
me = bpy.data.meshes.new("Boneco_LOD0"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("Boneco_LOD0", me); bpy.context.scene.collection.objects.link(ob)
bpy.context.view_layer.objects.active = ob; ob.select_set(True)
gp = ob.vertex_groups.new(name="LOD_Protect"); gu = ob.vertex_groups.new(name="upper"); gf = ob.vertex_groups.new(name="fore")
bm = bmesh.new(); bm.from_mesh(me); dl = bm.verts.layers.deform.verify()
for v in bm.verts:
    x = abs(v.co.x)
    if abs(x - 0.55) < 1e-4 and abs(v.co.x) > 0.2: v[dl][gp.index] = 1.0          # anel do cotovelo (i = 12)
    if x > 0.24:
        w = min(1, max(0, (x - 0.45) / 0.2)); v[dl][gf.index] = w; v[dl][gu.index] = 1 - w
for e in bm.edges:
    a, b = e.verts
    if abs(a.co.x) > 0.24 and abs(b.co.x) > 0.24:
        if a.co.z < 0 and b.co.z < 0 and abs(a.co.y) < 1e-6 and abs(b.co.y) < 1e-6: e.seam = True     # seam embaixo do braco
        if abs(abs(a.co.x) - 0.775) < 1e-4 and abs(abs(b.co.x) - 0.775) < 1e-4: e.smooth = False                 # punho sharp (i = 21)
bm.to_mesh(me); bm.free()
p = bpy.context.scene.loop_lod
for r in (0.5, 0.25, 0.125): p.lods.add().ratio = r
p.use_evaluated = False
t0 = time.time()
src, out = loop_lod.generate_lods(bpy.context, ob, p)
P("RESULT original tris", src, "tempo", round(time.time()-t0, 2), "s")
def analisa(o):
    m = o.data; gi = o.vertex_groups["LOD_Protect"].index
    prot = [v for v in m.vertices if any(g.group == gi and g.weight >= 0.5 for g in v.groups)]
    xs = sorted({round(abs(v.co.x), 4) for v in prot})
    R = [v for v in prot if v.co.x > 0]
    import mathutils
    kd = mathutils.kdtree.KDTree(len(m.vertices))
    for v in m.vertices: kd.insert(v.co, v.index)
    kd.balance()
    sem_par = sum(1 for v in m.vertices if kd.find(mathutils.Vector((-v.co.x, v.co.y, v.co.z)))[2] > 1e-4)
    seams = [e for e in m.edges if e.use_seam]
    sx = [m.vertices[i].co.x for e in seams for i in e.vertices if m.vertices[i].co.x > 0]
    sharp = [e for e in m.edges if e.use_edge_sharp]
    shx = sorted({round(abs(m.vertices[i].co.x), 3) for e in sharp for i in e.vertices})
    ngons = sum(1 for f in m.polygons if len(f.vertices) > 4); tris = sum(1 for f in m.polygons if len(f.vertices) == 3)
    return dict(anel_cotovelo_vertices_lado_direito=len(R), anel_x=xs, verts_sem_espelho=sem_par,
                seam_x=(round(min(sx),3), round(max(sx),3)) if sx else None, sharp_x=shx,
                ngons=ngons, triangulos=tris, faces=len(m.polygons))
P("RESULT LOD0", analisa(ob))
for n, t, g in out:
    P("RESULT", n, "alvo", t, "obtido", g, analisa(bpy.data.objects[n]))
bpy.ops.wm.save_as_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lodtest.blend")
