import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
MODE = sys.argv[-1]  # still | gif
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("scalp_raiz"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.10,0.035,0.012,1); scalp.data.materials.append(sm_)
# olhos
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1)
eyes=[]
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.016, location=(sx*0.034,-0.088,0.012), segments=48, ring_count=24); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth(); eyes.append(e)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.012)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
def curves_on(surf, name):
    cd = bpy.data.hair_curves.new(name); o = link(bpy.data.objects.new(name, cd)); cd.surface = surf; cd.surface_uv_map = "UVMap"; return o
def proc(t, colis, L, out, lado, tras, grav, dens):
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": colis, "Comprimento": L, "Para fora": out, "Para o lado da risca": lado, "Para trás": tras, "Gravidade": grav, "Guias por m2": dens}.items(): x.inputs[kk].default_value = v
    t.chain(x, 'Geometry', 'Guias')
def grp(t, name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for kk,v in kw.items(): n.inputs[kk].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
hm = hair_mat("pelo", melanin=0.75, redness=0.9, roughness=0.35)
# cabelo
g = curves_on(scalp, "cabelo"); t = Tree("cabelo")
proc(t, head, 0.26, 0.45, 0.35, 0.6, 1.5, 4000.0)
grp(t, "GR Física Estilizada", **{"Vento": 0.06, "Movimento": 0.3, "Raiz solta": 0.05, "Substeps": 20})
w_ = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
for q in w_.inputs:
    if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
grp(t, "GR Densidade Livre", **{"Fios por m2": 220000.0, "Viewport": 1.0})
grp(t, "GR Mecha Estilizada")
grp(t, "GR Strays em Arco")
grp(t, "GR Cacho por Mecha", **{"Voltas por metro mín": 18.0, "Voltas por metro máx": 30.0, "Raio mín": 0.009, "Raio máx": 0.014, "Começa em": 0.35})
grp(t, "GR Cor por Mecha")
profile(t, EG, radius=0.0005); set_mat(t, MAT["GR Cabelo Cor por Mecha"]); apply_tree(g, t.finish())
# palpebras e cilios
def lid(e, name):
    me = e.data.copy(); me.name=name; bm=bmesh.new(); bm.from_mesh(me)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (0.001 < f.calc_center_median().z < 0.006 and f.calc_center_median().y < -0.009)], context='FACES')
    bm.to_mesh(me); bm.free(); o = link(bpy.data.objects.new(name, me)); o.location=e.location; o.scale=(1.06,)*3; o.hide_render=True; return o
for i,e in enumerate(eyes):
    s = lid(e, f"lid{i}"); c = curves_on(s, f"cil{i}"); tc = Tree(f"cil{i}")
    proc(tc, head, 0.009, 1.0, 0.0, 0.0, -1.3, 250000.0); profile(tc, EG, radius=0.0005, shape=0.8); set_mat(tc, hm); apply_tree(c, tc.finish())
# sobrancelha
me = head.data.copy(); bm = bmesh.new(); bm.from_mesh(me)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (f.calc_center_median().y < -0.07 and 0.028 < f.calc_center_median().z < 0.040 and 0.012 < abs(f.calc_center_median().x) < 0.058)], context='FACES')
bm.to_mesh(me); bm.free(); brow = link(bpy.data.objects.new("brow", me)); brow.scale=(1.003,)*3; brow.hide_render=True
b = curves_on(brow, "sobrancelha"); tb = Tree("sob")
proc(tb, head, 0.014, 0.25, 1.2, 0.0, -0.4, 600000.0)
tb.eg(EG['Clump Hair Curves'], Factor=0.9, Shape=0.25, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.004, Existing_Guide_Map=False, Seed=1)
profile(tb, EG, radius=0.00035); set_mat(tb, hm); apply_tree(b, tb.finish())
sc = bpy.context.scene; sc.frame_start = 1; sc.frame_end = 48
if MODE == "still":
    for f in range(1, 37): sc.frame_set(f)
    print("INFO", stats(g).get('curves'), stats(g).get('points'))
    shot("56_hero", res=900, samples=48, cam_loc=(0.30,-0.52,0.06), target=(0.0,-0.02,-0.03), lens=50)
else:
    stage(res=360, samples=10, cam_loc=(0.30,-0.52,0.06), target=(0.0,-0.02,-0.03), lens=50)
    fr=[]; tt=time.time()
    for f in range(1,49):
        sc.frame_set(f)
        if f % 2 == 1:
            p=os.path.join(OUT, f"56_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); fr.append(p)
    from PIL import Image
    ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in fr]
    ims[0].save(os.path.join(OUT,"56_hero.gif"), save_all=True, append_images=ims[1:], duration=83, loop=0)
    print("TIME", round(time.time()-tt,1))
