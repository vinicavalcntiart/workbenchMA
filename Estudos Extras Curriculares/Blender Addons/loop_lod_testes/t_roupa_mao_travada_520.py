import bpy, bmesh, sys, math, time, mathutils
sys.path.insert(0, "/home/user/workbenchMA/Estudos Extras Curriculares/Blender Addons")
import loop_lod
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.read_homefile(use_empty=True); loop_lod.register()
SEG, RINGS, R = 24, 20, 0.18
bm = bmesh.new(); uv = bm.loops.layers.uv.new("UVMap")
rows = []
for i in range(RINGS + 1):
    z = -0.8 + 1.2 * i / RINGS; r = R * (1.25 - 0.25 * i / RINGS)
    rows.append([bm.verts.new((r * math.cos(2*math.pi*j/SEG), r * math.sin(2*math.pi*j/SEG), z)) for j in range(SEG)])
for i in range(RINGS):
    for j in range(SEG):
        f = bm.faces.new((rows[i][j], rows[i][(j+1)%SEG], rows[i+1][(j+1)%SEG], rows[i+1][j]))
        for k, l in enumerate(f.loops):
            l[uv].uv = ((j + (1 if k in (1,2) else 0)) / SEG, (i + (1 if k >= 2 else 0)) / RINGS)
bm.faces.ensure_lookup_table()
def patch(js, is_):
    return [f for f in bm.faces if any(True for _ in [0]) and
            (lambda c: True)(0) and
            round(((math.atan2(f.calc_center_median().y, f.calc_center_median().x) * SEG / (2*math.pi)) - 0.5)) % SEG in js and
            int((f.calc_center_median().z + 0.8) / (1.2 / RINGS)) in is_]
arm_rows = {14, 15, 16, 17}
dlb = bm.verts.layers.deform.verify()
PROT_STEPS = {5, 6, 7, 10, 11}          # cotovelo (3 aneis) e punho (2 aneis)
for side, js in ((1, {22, 23, 0, 1}), (-1, {10, 11, 12, 13})):
    faces = patch(js, arm_rows)
    for step in range(12):
        res = bmesh.ops.extrude_face_region(bm, geom=faces)
        newv = [g for g in res['geom'] if isinstance(g, bmesh.types.BMVert)]
        bmesh.ops.delete(bm, geom=faces, context='FACES')
        faces = [g for g in res['geom'] if isinstance(g, bmesh.types.BMFace)]
        for v in newv: v.co.x += side * 0.06
        for v in newv:
            if step in PROT_STEPS: v[dlb][0] = 1.0
            elif 0 in v[dlb]: del v[dlb][0]
        if step == 0:
            for v in newv: v.co.z -= 0.0
    # mao: escala a ponta
bm.normal_update()
# pescoco: tampa em leque (polo cheio de triangulos), como no personagem
top = [e for e in bm.edges if e.is_boundary and all(v.co.z > 0.39 for v in e.verts)]
res = bmesh.ops.holes_fill(bm, edges=top, sides=0)
bmesh.ops.poke(bm, faces=res['faces'])
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
me = bpy.data.meshes.new("Roupa_LOD0"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("Roupa_LOD0", me); bpy.context.scene.collection.objects.link(ob); bpy.context.view_layer.objects.active = ob
gp = ob.vertex_groups.new(name="LOD_Protect")   # indice 0 = o marcado no bmesh
bm = bmesh.new(); bm.from_mesh(me); dl = bm.verts.layers.deform.verify()
XS = sorted({round(abs(v.co.x), 4) for v in bm.verts if abs(v.co.x) > R * 1.3})
cot = XS[5:8]; pul = XS[9:11]
for v in bm.verts:
    ax = round(abs(v.co.x), 4)
    if v.co.z > 0.36: v[dl][gp.index] = 1.0          # anel do pescoco
for e in bm.edges:
    a, b = e.verts
    if all(abs(v.co.x) < 1e-4 and abs(v.co.y) > 0.1 for v in (a, b)) and all(v.co.z < 0.1 for v in (a, b)): e.seam = True   # laterais do robe
bm.to_mesh(me); bm.free()
def stats(o):
    m = o.data; bmx = bmesh.new(); bmx.from_mesh(m)
    nm = loop_lod.nonmanifold_count(bmx); ng = sum(1 for f in bmx.faces if len(f.verts) > 4); tr = loop_lod.tri_count(bmx)
    kd = mathutils.kdtree.KDTree(len(m.vertices))
    for v in m.vertices: kd.insert(v.co, v.index)
    kd.balance()
    sem = sum(1 for v in m.vertices if kd.find(mathutils.Vector((-v.co.x, v.co.y, v.co.z)))[2] > 1e-4)
    gi = o.vertex_groups["LOD_Protect"].index
    ring = {}
    for v in m.vertices:
        if v.co.x > 0.25 and any(g.group == gi and g.weight >= .5 for g in v.groups):
            k = round(v.co.x / 0.06) * 0.06
            ring[round(k, 2)] = ring.get(round(k, 2), 0) + 1
    sz = [m.vertices[i].co.z for e in m.edges if e.use_seam for i in e.vertices]
    seams = (sum(1 for e in m.edges if e.use_seam), round(min(sz),2) if sz else None, round(max(sz),2) if sz else None)
    bmx.free()
    return dict(tris=tr, ngons=ng, nonmanifold=nm, sem_espelho=sem, aneis_protegidos_braco_dir=dict(sorted(ring.items())), seams=seams)
P("RESULT LOD0", stats(ob))
gl = ob.vertex_groups.new(name="LOD_Lock")
gl.add([v.index for v in ob.data.vertices if abs(v.co.x) > 0.8], 1.0, 'REPLACE')
NL = sum(1 for v in ob.data.vertices if abs(v.co.x) > 0.8)
p = bpy.context.scene.loop_lod
for r in (0.5, 0.25, 0.125): p.lods.add().ratio = r
p.use_evaluated = False
t0 = time.time(); src, out = loop_lod.generate_lods(bpy.context, ob, p)
P("RESULT tempo", round(time.time() - t0, 1), "s")
for n, t, g in out: P("RESULT", n, "alvo", t, "mao travada", NL, "->", sum(1 for v in bpy.data.objects[n].data.vertices if abs(v.co.x) > 0.8), stats(bpy.data.objects[n]))
bpy.ops.wm.save_as_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lodtest3.blend")
