import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
import numpy as np
LIB = os.path.join(LAB, "receitas_grooming.blend")
W = sys.argv[-1]
EG, head, scalp, g = base_scene(length=0.22, gravity=3.0, spread=0.3, outward=0.5, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
def grp(t, name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
def tips():
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    return len(d.curves), P[[c.first_point_index+c.points_length-1 for c in d.curves]]
t = Tree("v")
if W == "vento":
    attach_uv(g, scalp)
    col = bpy.data.collections.new("Colisores"); bpy.context.scene.collection.children.link(col)
    grp(t, "GR Física Estilizada", **{"Vento": 0.12, "Movimento": 0.3, "Raiz solta": 0.05, "Substeps": 20, "Colisores": col})
    apply_tree(g, t.finish()); sc = bpy.context.scene
    for f in range(1, 37):
        sc.frame_set(f)
        if f in (1, 12, 24, 36): n,T = tips(); print("INFO vento q", f, "ponta x media cm", round(float(T[:,0].mean())*100, 1))
    sys.exit()
if W == "malha":
    me = bpy.data.meshes.new("shell"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=1.0)
    bmesh.ops.scale(bm, vec=(0.145,0.15,0.13), verts=bm.verts); bmesh.ops.translate(bm, vec=(0,0.012,-0.03), verts=bm.verts)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < -0.13 or (f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.05)], context='FACES')
    bm.to_mesh(me); bm.free(); sh = link(bpy.data.objects.new("shell", me)); sh.hide_render = True
    grp(t, "GR Forma por Malha", **{"Malha da forma": sh})
grp(t, "GR Densidade Livre", **{"Fios por m2": 250000.0, "Viewport": 1.0})
grp(t, "GR Mecha Estilizada")
if W == "crescer": grp(t, "GR Crescer")
profile(t, EG, radius=0.0005)
if W == "lod":
    cam = stage(res=420, samples=16, cam_loc=(0.45*8,-0.60*8,0.08*8), target=(0,0,-0.04), lens=45)
    grp(t, "GR LOD por Câmera", **{"Câmera": cam})
set_mat(t, hair_mat("c", melanin=0.6, redness=0.5)); apply_tree(g, t.finish())
if W == "crescer": bpy.context.scene.frame_set(20)
n,T = tips(); print("INFO", W, "fios", n)
if W != "lod": shot(f"t_lib6_{W}", res=420, samples=16, cam_loc=(0.45,-0.60,0.08), target=(0,0,-0.04), lens=45)
