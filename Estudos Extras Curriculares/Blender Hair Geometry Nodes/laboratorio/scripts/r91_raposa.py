import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import math
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
# cabeca de raposa: esfera + focinho + orelhas (uma malha, com UV)
bm = bmesh.new(); bm.loops.layers.uv.new("UVMap")
bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=32, radius=0.1, calc_uvs=True)
for v in bm.verts:
    if v.co.y < 0:   # focinho: estica para frente e afina
        k = min(1.0, -v.co.y/0.1); v.co.y *= 1.0 + 0.9*k*k; v.co.x *= 1.0 - 0.45*k*k; v.co.z = v.co.z*(1.0-0.4*k*k) - 0.02*k*k
for sx in (-1,1):
    r = bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=0.045, radius2=0.004, depth=0.11, calc_uvs=True)
    vs = r['verts']
    bmesh.ops.rotate(bm, verts=vs, cent=(0,0,0), matrix=Matrix.Rotation(math.radians(-18*sx), 3, 'Y'))
    bmesh.ops.translate(bm, verts=vs, vec=(sx*0.055, 0.01, 0.125))
me = bpy.data.meshes.new("raposa"); bm.to_mesh(me); bm.free()
for p in me.polygons: p.use_smooth = True
body = link(bpy.data.objects.new("raposa", me)); sk = bpy.data.materials.new("pele"); sk.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.3,0.1,0.03,1); body.data.materials.append(sk)
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.02,0.02,1); w.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=0.05
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.014, location=(sx*0.045,-0.085,0.035)); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(0,-0.19,-0.02)); nz_=bpy.context.object; nz_.data.materials.append(w)
cd = bpy.data.hair_curves.new("pelo"); g = link(bpy.data.objects.new("pelo", cd)); cd.surface = body; cd.surface_uv_map = "UVMap"
t = Tree("rp")
gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves']); t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, 120000.0), gen.inputs['Density'])
gen.inputs['Hair Length'].default_value = 0.02; gen.inputs['Control Points'].default_value = 6; gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
t.geo = gen.outputs['Geometry']
# fluxo: da ponta do focinho para tras (curva reta)
cu = bpy.data.curves.new("fluxo", 'CURVE'); cu.dimensions='3D'; sp = cu.splines.new('POLY'); sp.points.add(30)
for i,p_ in enumerate(sp.points): p_.co = (0, -0.20 + i*0.32/30, 0.02, 1)
flow = link(bpy.data.objects.new("fluxo", cu)); flow.hide_render = True
pc = t.add('GeometryNodeGroup', group=GR["GR Pentear por Curva"]); t.chain(pc); pc.inputs["Curva de fluxo"].default_value = flow; pc.inputs["Levanta"].default_value = 0.35
# comprimento por regiao: bochechas (lateral baixa) e ponta da orelha longos
cr = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx = t.add('ShaderNodeSeparateXYZ'); t.link(cr.outputs['Root Position'], sx.inputs[0])
ax = t.add('ShaderNodeMath', props={'operation':'ABSOLUTE'}); t.link(sx.outputs['X'], ax.inputs[0])
bo = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); bo.clamp=True; t.link(ax.outputs[0], bo.inputs['Value']); bo.inputs['From Min'].default_value=0.06; bo.inputs['From Max'].default_value=0.095
bz = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); bz.clamp=True; t.link(sx.outputs['Z'], bz.inputs['Value']); bz.inputs['From Min'].default_value=0.02; bz.inputs['From Max'].default_value=-0.03
bch = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(bo.outputs['Result'], bch.inputs[0]); t.link(bz.outputs['Result'], bch.inputs[1])
oz = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); oz.clamp=True; t.link(sx.outputs['Z'], oz.inputs['Value']); oz.inputs['From Min'].default_value=0.15; oz.inputs['From Max'].default_value=0.175
mx = t.add('ShaderNodeMath', props={'operation':'MAXIMUM'}); t.link(bch.outputs[0], mx.inputs[0]); t.link(oz.outputs['Result'], mx.inputs[1])
lf = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(mx.outputs[0], lf.inputs[0]); lf.inputs[1].default_value = 2.2; lf.inputs[2].default_value = 1.0
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(lf.outputs[0], ev.inputs[0])
tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=False); t.link(ev.outputs[0], tr.inputs['Length Factor'])
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.2, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=2)
# cor: branco no peito/queixo (z baixo e frente), laranja no resto, ponta da orelha escura
wz = t.add('ShaderNodeMapRange', props={'interpolation_type':'SMOOTHSTEP'}); wz.clamp=True; t.link(sx.outputs['Z'], wz.inputs['Value']); wz.inputs['From Min'].default_value=-0.01; wz.inputs['From Max'].default_value=-0.05
e2 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(wz.outputs['Result'], e2.inputs[0])
s2 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s2.inputs['Name'].default_value='branco'; t.chain(s2); t.link(e2.outputs[0], s2.inputs['Value'])
e3 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(oz.outputs['Result'], e3.inputs[0])
s3 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s3.inputs['Name'].default_value='orelha'; t.chain(s3); t.link(e3.outputs[0], s3.inputs['Value'])
profile(t, EG, radius=0.00035)
m = bpy.data.materials.new("raposa"); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial')
h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization='MELANIN'; h.inputs['Roughness'].default_value=0.35; h.inputs['Melanin Redness'].default_value=1.0
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='branco'; b_ = nt.nodes.new('ShaderNodeAttribute'); b_.attribute_name='orelha'
m1 = nt.nodes.new('ShaderNodeMapRange'); m1.inputs['To Min'].default_value = 0.42; m1.inputs['To Max'].default_value = 0.02; nt.links.new(a.outputs['Fac'], m1.inputs['Value'])
m2 = nt.nodes.new('ShaderNodeMath'); m2.operation='MULTIPLY_ADD'; nt.links.new(b_.outputs['Fac'], m2.inputs[0]); m2.inputs[1].default_value = 0.5; nt.links.new(m1.outputs['Result'], m2.inputs[2])
nt.links.new(m2.outputs[0], h.inputs['Melanin'])
rd = nt.nodes.new('ShaderNodeMapRange'); rd.inputs['To Min'].default_value = 1.0; rd.inputs['To Max'].default_value = 0.0; nt.links.new(a.outputs['Fac'], rd.inputs['Value']); nt.links.new(rd.outputs['Result'], h.inputs['Melanin Redness'])
nt.links.new(h.outputs[0], o.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
shot("91_raposa", res=720, samples=32, cam_loc=(0.30,-0.60,0.02), target=(0,-0.04,0.04), lens=45)
