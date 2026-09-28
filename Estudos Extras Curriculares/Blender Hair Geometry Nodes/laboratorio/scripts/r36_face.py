import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; M = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
# olhos
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1)
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.016, location=(sx*0.034,-0.088,0.012)); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.012)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
def region(name, keep):
    me = head.data.copy(); me.name = name
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if not keep(f.calc_center_median())], context='FACES')
    bm.to_mesh(me); bm.free()
    o = link(bpy.data.objects.new(name, me)); o.scale=(1.003,)*3; o.hide_render = True; return o
brow = region("sobrancelha", lambda c: c.y < -0.07 and 0.028 < c.z < 0.040 and 0.012 < abs(c.x) < 0.058)
beard = region("barba", lambda c: c.y < -0.04 and c.z < -0.045 and abs(c.x) < 0.075)
must = region("bigode", lambda c: c.y < -0.085 and -0.045 < c.z < -0.03 and abs(c.x) < 0.03)
lash = region("cilio", lambda c: c.y < -0.085 and 0.018 < c.z < 0.026 and 0.02 < abs(c.x) < 0.05)
def groom(surf, name, L, outw, lado, tras, grav, dens, mecha, rad, mat, shape=0.25):
    cd = bpy.data.hair_curves.new(name); g = link(bpy.data.objects.new(name, cd)); cd.surface = surf; cd.surface_uv_map = "UVMap"
    t = Tree(name)
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": outw, "Para o lado da risca": lado, "Para trás": tras, "Gravidade": grav, "Guias por m2": dens}.items(): x.inputs[kk].default_value = v
    t.chain(x, 'Geometry', 'Guias')
    if mecha:
        c = t.eg(EG['Clump Hair Curves'], Factor=0.9, Shape=shape, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=mecha, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Set Hair Curve Profile'], Radius=rad, Shape=0.3, Factor_Min=0.0, Factor_Max=1.0)
    set_mat(t, mat); apply_tree(g, t.finish()); print("INFO", name, stats(g).get('curves'))
    return g
hm = hair_mat("pelo", melanin=0.9, redness=0.35, roughness=0.35)
groom(brow, "sobrancelha", 0.014, 0.25, 1.2, 0.0, -0.4, 600000.0, 0.004, 0.00035, hm)
groom(lash, "cilio", 0.010, 0.9, 0.3, 0.0, -1.6, 120000.0, 0.0, 0.0004, hm)
groom(beard, "barba", 0.018, 0.5, 0.15, 0.0, 1.0, 900000.0, 0.005, 0.00035, hm)
groom(must, "bigode", 0.02, 0.4, 1.4, 0.0, 0.6, 900000.0, 0.005, 0.0004, hm)
p1 = shot("36_rosto_frente", res=640, samples=24, cam_loc=(0.12,-0.40,0.0), target=(0,-0.05,-0.01), lens=55)
lab_cam = bpy.context.scene.camera; lab_cam.location = (0.30,-0.30,0.02); d = Vector((0,-0.05,-0.01))-lab_cam.location; lab_cam.rotation_euler = d.to_track_quat('-Z','Y').to_euler()
p2 = os.path.join(OUT, "36_rosto_34.png"); render(p2)
print("SHEET", sheet([p1,p2], ["frente", "3/4"], os.path.join(OUT,"36_face_sheet.png"), cols=2))
