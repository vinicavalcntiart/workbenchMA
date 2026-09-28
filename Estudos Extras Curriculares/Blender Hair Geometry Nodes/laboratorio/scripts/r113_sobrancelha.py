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
ctrl = link(bpy.data.objects.new("CTRL_sobrancelha", None)); ctrl.empty_display_type = 'CUBE'; ctrl.empty_display_size = 0.01; ctrl.location = (0, -0.15, 0.04)
cd = bpy.data.hair_curves.new("sob"); g = link(bpy.data.objects.new("sobrancelha", cd)); cd.surface = brow; cd.surface_uv_map = "UVMap"
t = Tree("sob"); x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.014, "Para fora": 0.25, "Para o lado da risca": 1.2, "Para trás": 0.0, "Gravidade": -0.4, "Guias por m2": 900000.0}.items(): x.inputs[kk].default_value = v
t.chain(x, 'Geometry', 'Guias')
t.eg(EG['Clump Hair Curves'], Factor=0.9, Shape=0.25, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.004, Existing_Guide_Map=False, Seed=1)
# controle: escala Z do Empty = levantar (cm); escala X = franzir (ponta interna desce)
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'ORIGINAL'}); oi.inputs['Object'].default_value = ctrl
sc_ = t.add('ShaderNodeSeparateXYZ'); t.link(oi.outputs['Scale'], sc_.inputs[0])
up = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); t.link(sc_.outputs['Z'], up.inputs[0]); up.inputs[1].default_value = 1.0
upm = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(up.outputs[0], upm.inputs[0]); upm.inputs[1].default_value = 0.012
fr = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); t.link(sc_.outputs['X'], fr.inputs[0]); fr.inputs[1].default_value = 1.0
ps = t.add('GeometryNodeInputPosition'); sp = t.add('ShaderNodeSeparateXYZ'); t.link(ps.outputs[0], sp.inputs[0])
ax = t.add('ShaderNodeMath', props={'operation':'ABSOLUTE'}); t.link(sp.outputs['X'], ax.inputs[0])
inn = t.add('ShaderNodeMapRange'); inn.clamp = True; t.link(ax.outputs[0], inn.inputs['Value']); inn.inputs['From Min'].default_value = 0.012; inn.inputs['From Max'].default_value = 0.05; inn.inputs['To Min'].default_value = 1.0; inn.inputs['To Max'].default_value = 0.0
frm = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(fr.outputs[0], frm.inputs[0]); t.link(inn.outputs['Result'], frm.inputs[1])
frm2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(frm.outputs[0], frm2.inputs[0]); frm2.inputs[1].default_value = -0.01
dz = t.add('ShaderNodeMath', props={'operation':'ADD'}); t.link(upm.outputs[0], dz.inputs[0]); t.link(frm2.outputs[0], dz.inputs[1])
cb = t.add('ShaderNodeCombineXYZ'); t.link(dz.outputs[0], cb.inputs['Z'])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(cb.outputs[0], s.inputs['Offset'])
profile(t, EG, radius=0.00045); set_mat(t, hair_mat("h", melanin=0.9, redness=0.35)); apply_tree(g, t.finish())
paths=[]; labs=[]
for nm, scl in (("neutro",(1,1,1)),("surpresa",(1,1,2)),("bravo",(2,1,1))):
    ctrl.scale = scl; bpy.context.view_layer.update()
    paths.append(shot(f"113_{nm}", res=360, samples=16, cam_loc=(0.0,-0.36,0.02), target=(0,-0.05,0.02), lens=55)); labs.append(f"{nm}: escala {scl}")
print("SHEET", sheet(paths, labs, os.path.join(OUT,"113_sobrancelha_sheet.png"), cols=3, w=360))
