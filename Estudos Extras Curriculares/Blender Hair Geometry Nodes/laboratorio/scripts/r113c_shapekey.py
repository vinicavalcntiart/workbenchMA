import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1)
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.016, location=(sx*0.034,-0.088,0.012)); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.012)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
me = head.data.copy(); bm = bmesh.new(); bm.from_mesh(me)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (f.calc_center_median().y < -0.07 and 0.028 < f.calc_center_median().z < 0.040 and 0.012 < abs(f.calc_center_median().x) < 0.058)], context='FACES')
bm.to_mesh(me); bm.free(); brow = link(bpy.data.objects.new("brow", me)); brow.scale=(1.003,)*3; brow.hide_render=True
brow.add_rest_position_attribute = True
brow.shape_key_add(name="Basis")
ks = brow.shape_key_add(name="surpresa")
for v in ks.data: v.co.z += 0.010; v.co.y -= 0.002
kb = brow.shape_key_add(name="bravo")
for v in kb.data:
    f = max(0.0, min(1.0, (0.05 - abs(v.co.x))/0.038)); v.co.z -= 0.009*f
cd = bpy.data.hair_curves.new("sob"); g = link(bpy.data.objects.new("sobrancelha", cd)); cd.surface = brow; cd.surface_uv_map = "UVMap"
t = Tree("sob"); x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.014, "Para fora": 0.25, "Para o lado da risca": 1.2, "Para trás": 0.0, "Gravidade": -0.4, "Guias por m2": 900000.0}.items(): x.inputs[kk].default_value = v
t.chain(x, 'Geometry', 'Guias')
t.eg(EG['Clump Hair Curves'], Factor=0.9, Shape=0.25, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.004, Existing_Guide_Map=False, Seed=1)
t.chain(t.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
profile(t, EG, radius=0.00045); set_mat(t, hair_mat("h", melanin=0.9, redness=0.35)); apply_tree(g, t.finish())
paths=[]; labs=[]
import numpy as np
from mathutils.bvhtree import BVHTree
for nm, scl in (("neutro",(0,0)),("surpresa",(1,0)),("bravo",(0,1))):
    ks.value, kb.value = scl; bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    R = P[[c.first_point_index for c in d.curves]]
    se = brow.evaluated_get(dg); me_ = se.to_mesh(); mw = brow.matrix_world
    bvh = BVHTree.FromPolygons([mw @ v.co for v in me_.vertices], [p_.vertices[:] for p_ in me_.polygons]); se.to_mesh_clear()
    gm = g.matrix_world; dist = [ (gm @ Vector(r) - bvh.find_nearest(gm @ Vector(r))[0]).length for r in R[::5] ]
    print("SK", nm, "raiz ate a pele mm media", round(float(np.mean(dist))*1000,2))
    paths.append(shot(f"113c_{nm}", res=360, samples=16, cam_loc=(0.0,-0.36,0.02), target=(0,-0.05,0.02), lens=55)); labs.append(f"{nm}: shape key {scl}")
print("SHEET", sheet(paths, labs, os.path.join(OUT,"113c_sobrancelha_sheet.png"), cols=3, w=360))
