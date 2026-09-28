import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # tangente | raiz | proxy
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.22, gravity=3.0, spread=0.3, outward=0.5, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}
me = bpy.data.meshes.new("shell"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=1.0)
bmesh.ops.scale(bm, vec=(0.145,0.15,0.13), verts=bm.verts); bmesh.ops.translate(bm, vec=(0,0.012,-0.03), verts=bm.verts)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < -0.13 or (f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.05)], context='FACES')
bm.to_mesh(me); bm.free(); sh = link(bpy.data.objects.new("shell", me)); sh.hide_render = True
for p in me.polygons: p.use_smooth = True
t = Tree("np")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Forma por Malha", **{"Malha da forma": sh})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 250000.0})
grp("GR Mecha Estilizada")
grp("GR Normal da Malha", **{"Malha": sh})
profile(t, EG, radius=0.0006)
set_mat(t, bpy.data.materials["GR Cabelo Cel"]); apply_tree(g, t.finish())
print("INFO lib", stats(g).get('curves'))
shot("t_lib14_cel", res=460, samples=24, cam_loc=(0.45,-0.60,0.12), target=(0,0,-0.04), lens=45)
