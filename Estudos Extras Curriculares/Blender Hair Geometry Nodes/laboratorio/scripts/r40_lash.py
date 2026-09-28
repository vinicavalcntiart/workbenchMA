import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1)
EC = (0.034,-0.088,0.012); ER = 0.016
eyes=[]
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=ER, location=(sx*EC[0],EC[1],EC[2]), segments=48, ring_count=24); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth(); eyes.append(e)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.012)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
# palpebra = faixa da esfera do olho (acima do centro, na frente), 5% maior
def lid(e, zmin, zmax, name, xout=None):
    me = e.data.copy(); me.name=name; bm=bmesh.new(); bm.from_mesh(me)
    if not bm.loops.layers.uv: pass
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (zmin < f.calc_center_median().z < zmax and f.calc_center_median().y < -0.009 and (xout is None or f.calc_center_median().x*xout > 0.004))], context='FACES')
    bm.to_mesh(me); bm.free()
    o = link(bpy.data.objects.new(name, me)); o.location=e.location; o.scale=(1.06,)*3; o.hide_render=True
    bpy.context.view_layer.update(); return o
V = sys.argv[-1]
def groom(surf, name, L, outw, grav, dens, mecha, rad, tip, shp=0.5):
    cd = bpy.data.hair_curves.new(name); g = link(bpy.data.objects.new(name, cd)); cd.surface = surf; cd.surface_uv_map = "UVMap"
    t = Tree(name)
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": outw, "Para o lado da risca": 0.0, "Para trás": 0.0, "Gravidade": grav, "Guias por m2": dens}.items(): x.inputs[kk].default_value = v
    t.chain(x, 'Geometry', 'Guias')
    if mecha: t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.0, Tip_Spread=tip, Preserve_Length=True, Guide_Distance=mecha, Existing_Guide_Map=False, Seed=1)
    t.eg(EG['Set Hair Curve Profile'], Radius=rad, Shape=shp, Factor_Min=0.0, Factor_Max=1.0)
    set_mat(t, hair_mat("lash", melanin=1.0, redness=0.2, roughness=0.3)); apply_tree(g, t.finish()); print("INFO", name, stats(g).get('curves'))
    return g
for i,e in enumerate(eyes):
    sx = -1 if i==0 else 1
    s = lid(e, 0.005, 0.0135, f"lid{i}") if V in "abc" else lid(e, 0.001, 0.006, f"lid{i}", xout=(sx if V=="e" else None))
    if V=="a": groom(s, f"c{i}", 0.010, 1.0, -1.6, 300000.0, 0.0, 0.0004, 0)
    if V=="b": groom(s, f"c{i}", 0.012, 1.4, -2.5, 400000.0, 0.0, 0.0004, 0)
    if V=="c": groom(s, f"c{i}", 0.012, 1.4, -2.5, 900000.0, 0.0025, 0.00045, 0.0003)
    if V=="d": groom(s, f"c{i}", 0.009, 1.0, -1.3, 250000.0, 0.0, 0.0005, 0, 0.8)
    if V=="e": groom(s, f"c{i}", 0.011, 1.2, -1.8, 60000.0, 0.0, 0.0009, 0, 0.8)
p1 = shot(f"40_cilio_{V}", res=560, samples=24, cam_loc=(0.10,-0.34,0.03), target=(0.02,-0.09,0.012), lens=85)
