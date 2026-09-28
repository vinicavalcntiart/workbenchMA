import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import math
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
# corpo = bolota (elipsoide) com "cabeca" na frente, uma malha so
me = bpy.data.meshes.new("body"); bm = bmesh.new(); bm.loops.layers.uv.new("UVMap")
bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=32, radius=1.0, calc_uvs=True)
for v in bm.verts:
    y = v.co.y
    k = 1.0 + 0.25*max(0.0, -y)   # frente mais larga (cabeca)
    v.co.x *= 0.13*k; v.co.z *= 0.12*k; v.co.y *= 0.20
bm.to_mesh(me); bm.free()
for p in me.polygons: p.use_smooth = True
body = link(bpy.data.objects.new("body", me))
sk = bpy.data.materials.new("pele"); sk.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.12,0.05,0.02,1); body.data.materials.append(sk)
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.95,0.95,0.92,1); w.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=0.1
kk = bpy.data.materials.new("pup"); kk.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.01,0.01,0.01,1); kk.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=0.05
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, location=(sx*0.055,-0.175,0.07)); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.018, location=(sx*0.052,-0.205,0.075)); p=bpy.context.object; p.data.materials.append(kk); bpy.ops.object.shade_smooth()
# curva de fluxo: do focinho para tras, pelo dorso
cu = bpy.data.curves.new("fluxo", 'CURVE'); cu.dimensions = '3D'; sp = cu.splines.new('POLY')
pts = [(0, -0.26 + i*0.52/60, 0.0) for i in range(61)]
sp.points.add(len(pts)-1)
for p_, c in zip(sp.points, pts): p_.co = (*c, 1)
flow = link(bpy.data.objects.new("fluxo", cu)); flow.hide_render = True
cd = bpy.data.hair_curves.new("pelo"); g = link(bpy.data.objects.new("pelo", cd)); cd.surface = body; cd.surface_uv_map = "UVMap"
t = Tree("cri")
gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves']); t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, 90000.0), gen.inputs['Density'])
gen.inputs['Hair Length'].default_value = 0.04; gen.inputs['Control Points'].default_value = 8; gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
t.geo = gen.outputs['Geometry']
pc = t.add('GeometryNodeGroup', group=GR["GR Pentear por Curva"]); t.chain(pc); pc.inputs["Curva de fluxo"].default_value = flow; pc.inputs["Levanta"].default_value = 0.4
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.012, Existing_Guide_Map=False, Seed=2)
t.eg(EG['Hair Curves Noise'], Factor=1.0, Distance=0.003, Shape=0.5, Scale=30.0, Scale_along_Curve=4.0, Offset_per_Curve=0.4, Cumulative_Offset=False, Preserve_Length=True, Seed=3)
# listras
cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
tx = t.add('ShaderNodeTexWave'); tx.wave_type='BANDS'; tx.bands_direction='Y'; tx.inputs['Scale'].default_value = 6.0; tx.inputs['Distortion'].default_value = 5.0; t.link(cr.outputs['Root Position'], tx.inputs['Vector'])
mr = t.add('ShaderNodeMapRange'); mr.clamp=True; mr.inputs['From Min'].default_value=0.62; mr.inputs['From Max'].default_value=0.7; t.link(tx.outputs['Fac'], mr.inputs['Value'])
sx_ = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx_.inputs[0])
dorso = t.add('ShaderNodeMapRange'); dorso.clamp=True; t.link(sx_.outputs['Z'], dorso.inputs['Value']); dorso.inputs['From Min'].default_value=0.0; dorso.inputs['From Max'].default_value=0.06
mm = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(mr.outputs['Result'], mm.inputs[0]); t.link(dorso.outputs['Result'], mm.inputs[1])
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(mm.outputs[0], ev.inputs[0])
st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='padrao'; t.chain(st); t.link(ev.outputs[0], st.inputs['Value'])
# barriga clara: store 'barriga' = 1 - dorso-ish (z<0)
bz = t.add('ShaderNodeMapRange'); bz.clamp=True; t.link(sx_.outputs['Z'], bz.inputs['Value']); bz.inputs['From Min'].default_value=-0.02; bz.inputs['From Max'].default_value=-0.08
ev2 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(bz.outputs['Result'], ev2.inputs[0])
st2 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st2.inputs['Name'].default_value='barriga'; t.chain(st2); t.link(ev2.outputs[0], st2.inputs['Value'])
lf = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(ev.outputs[0], lf.inputs[0]); lf.inputs[1].default_value = -0.35; lf.inputs[2].default_value = 1.0
tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=True); t.link(lf.outputs[0], tr.inputs['Length Factor'])
profile(t, EG, radius=0.0004)
m = bpy.data.materials.new("fur"); nt = m.node_tree; nt.nodes.clear()
out = nt.nodes.new('ShaderNodeOutputMaterial'); h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model='CHIANG'; h.parametrization='MELANIN'
h.inputs['Roughness'].default_value=0.35; h.inputs['Melanin Redness'].default_value=1.0
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='padrao'; b = nt.nodes.new('ShaderNodeAttribute'); b.attribute_name='barriga'
m1 = nt.nodes.new('ShaderNodeMapRange'); m1.inputs['To Min'].default_value=0.28; m1.inputs['To Max'].default_value=1.0; nt.links.new(a.outputs['Fac'], m1.inputs['Value'])
m2 = nt.nodes.new('ShaderNodeMath'); m2.operation='MULTIPLY_ADD'; nt.links.new(b.outputs['Fac'], m2.inputs[0]); m2.inputs[1].default_value=-0.22; nt.links.new(m1.outputs['Result'], m2.inputs[2])
nt.links.new(m2.outputs[0], h.inputs['Melanin']); nt.links.new(h.outputs[0], out.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
shot("62_criatura", res=900, samples=40, cam_loc=(0.42,-0.62,0.20), target=(0,-0.03,0.0), lens=45)
