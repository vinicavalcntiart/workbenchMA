import bpy, bmesh, sys, math, time, mathutils
from mathutils import Vector
sys.path.insert(0, "/home/user/workbenchMA/Estudos Extras Curriculares/Blender Addons")
import loop_lod
def P(*a): print(*a); sys.stdout.flush()
RATIOS = [float(x) for x in sys.argv[sys.argv.index("--")+1:]] if "--" in sys.argv else [0.5, 0.25, 0.08]
bpy.ops.wm.read_homefile(use_empty=True); loop_lod.register()
SEG, ROWS = 24, 26
bm = bmesh.new()
rows = []
for i in range(ROWS + 1):
    t = i / ROWS; z = 1.35 * t; r = 0.34 - 0.14 * t
    rows.append([bm.verts.new((r*math.cos(2*math.pi*(j+.5)/SEG), r*math.sin(2*math.pi*(j+.5)/SEG), z)) for j in range(SEG)])
for k in range(3):   # ombro fechando ate o pescoco
    r = 0.2 - 0.04*(k+1); z = 1.35 + 0.035*(k+1)
    rows.append([bm.verts.new((r*math.cos(2*math.pi*(j+.5)/SEG), r*math.sin(2*math.pi*(j+.5)/SEG), z)) for j in range(SEG)])
for i in range(len(rows)-1):
    for j in range(SEG):
        bm.faces.new((rows[i][j], rows[i][(j+1)%SEG], rows[i+1][(j+1)%SEG], rows[i+1][j]))
bm.faces.ensure_lookup_table(); bm.normal_update()
def ang_idx(f):
    c = f.calc_center_median(); return int(math.floor((math.atan2(c.y, c.x) % (2*math.pi)) * SEG / (2*math.pi)))
def row_idx(f):
    return int(f.calc_center_median().z / (1.35/ROWS))
def extrude(faces, step_vec, scale=1.0, center_axis=None):
    res = bmesh.ops.extrude_face_region(bm, geom=faces)
    bmesh.ops.delete(bm, geom=faces, context='FACES')
    nv = [g for g in res['geom'] if isinstance(g, bmesh.types.BMVert)]
    nf = [g for g in res['geom'] if isinstance(g, bmesh.types.BMFace)]
    cen = sum((v.co for v in nv), Vector()) / len(nv)
    for v in nv:
        v.co = cen + (v.co - cen) * scale + step_vec
    return nf, nv
for side in (1,):
    js = {0, 1, 22, 23} if side == 1 else {10, 11, 12, 13}
    faces = [f for f in bm.faces if len(f.verts) == 4 and ang_idx(f) in js and row_idx(f) in {20, 21, 22, 23}]
    d = Vector((0.72*side, 0, -0.69)).normalized()
    for k in range(15):                                    # braco
        faces, nv = extrude(faces, d*0.045, 0.985)
    for k in range(3):                                     # mao (achata)
        faces, nv = extrude(faces, d*0.03, 1.0)
        cen = sum((v.co for v in nv), Vector())/len(nv)
        for v in nv: v.co.y = cen.y + (v.co.y - cen.y)*0.7
    # dedos: 4 quads de uma fileira da tampa, cada um com inset e 4 extrusoes (anel de 4)
    w = d.cross(Vector((0, 1, 0))).normalized()
    cen = sum((f.calc_center_median() for f in faces), Vector())/len(faces)
    rowf = sorted(faces, key=lambda f: (f.calc_center_median()-cen).dot(w))[4:8]
    ins = bmesh.ops.inset_individual(bm, faces=rowf, thickness=0.005, depth=0)
    for f in rowf:
        fs = [f]
        for k in range(4):
            fs, nv = extrude(fs, d*0.022, 0.9)
bmesh.ops.bisect_plane(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], plane_co=(0,0,0), plane_no=(1,0,0), clear_inner=True)
bmesh.ops.mirror(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], axis='X', merge_dist=1e-5)
nb = [e for e in bm.edges if e.is_boundary and all(v.co.z > 1.4 for v in e.verts)]
bmesh.ops.poke(bm, faces=bmesh.ops.holes_fill(bm, edges=nb, sides=0)['faces'])     # pescoco em leque
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
# seam nas costas, de cima a baixo
for e in bm.edges:
    a, b = e.verts
    if all(abs(v.co.x) < 1e-4 and v.co.y > 0 for v in (a, b)) and abs(a.co.z-b.co.z) > 1e-5: e.seam = True
# simetria exata
bm.verts.ensure_lookup_table()
kd = mathutils.kdtree.KDTree(len(bm.verts))
for v in bm.verts: kd.insert(v.co, v.index)
kd.balance()
for v in bm.verts:
    if v.co.x < -1e-6:
        co, i, dd = kd.find(Vector((-v.co.x, v.co.y, v.co.z)))
        if dd < 1e-3: v.co = Vector((-bm.verts[i].co.x, bm.verts[i].co.y, bm.verts[i].co.z))
import os, random
NOISE = float(os.environ.get("NOISE", "0"))
random.seed(3)
for v in bm.verts:
    v.co += Vector((random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))) * NOISE
me = bpy.data.meshes.new("Robe_LOD0"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("Robe_LOD0", me); bpy.context.scene.collection.objects.link(ob); bpy.context.view_layer.objects.active = ob
def stats(o):
    bmx = bmesh.new(); bmx.from_mesh(o.data)
    r = dict(tris=loop_lod.tri_count(bmx), quads=sum(1 for f in bmx.faces if len(f.verts)==4), ngons=sum(1 for f in bmx.faces if len(f.verts)>4),
             nonmanifold=loop_lod.nonmanifold_count(bmx), dobras=loop_lod.fold_count(bmx))
    bmx.free(); return r
P("RESULT LOD0", stats(ob))
p = bpy.context.scene.loop_lod
RINGS = [int(x) for x in os.environ.get("RINGS", "0,0,0").split(",")]
SPS = [float(x) for x in os.environ.get("SPS", "0,0,0").split(",")]
for r, mr, sp in zip(RATIOS, RINGS, SPS):
    it = p.lods.add(); it.ratio = r; it.min_ring = mr; it.max_sparsity = sp
p.use_evaluated = False
t0 = time.time(); src, out = loop_lod.generate_lods(bpy.context, ob, p)
P("RESULT tempo", round(time.time()-t0, 1), "s")
for n, t, g in out: P("RESULT", n, "alvo", t, stats(bpy.data.objects[n]))
for l in p.last_report.split("\n"): P("RESULT  |", l)
bpy.ops.wm.save_as_mainfile(filepath="/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lodrobe.blend")
