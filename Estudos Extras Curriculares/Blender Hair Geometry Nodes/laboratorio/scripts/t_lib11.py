import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
V = sys.argv[-1]   # normal | espiral | onda
reset(); EG = essentials()
# corpo: elipsoide deitado (bicho)
me = bpy.data.meshes.new("body"); bm = bmesh.new(); bm.loops.layers.uv.new("UVMap")
bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=32, radius=1.0, calc_uvs=True)
bmesh.ops.scale(bm, vec=(0.12,0.22,0.12), verts=bm.verts); bm.to_mesh(me); bm.free()
for p in me.polygons: p.use_smooth = True
body = link(bpy.data.objects.new("body", me)); body.data.materials.append(skin_mat())
# curva de fluxo
cu = bpy.data.curves.new("fluxo", 'CURVE'); cu.dimensions = '3D'; sp = cu.splines.new('POLY')
import math
if V == "espiral":
    pts = [(0.14*math.cos(a), -0.24 + 0.48*a/(6*math.pi), 0.14*math.sin(a)) for a in [i*6*math.pi/120 for i in range(121)]]
elif V == "onda":
    pts = [(0.03*math.sin(y*30), y, 0.13) for y in [-0.24 + i*0.48/120 for i in range(121)]]
else:
    pts = [(0, -0.24 + i*0.48/120, 0.0) for i in range(121)]   # da frente para tras
sp.points.add(len(pts)-1)
for p_, c in zip(sp.points, pts): p_.co = (*c, 1)
flow = link(bpy.data.objects.new("fluxo", cu)); flow.hide_render = True
cd = bpy.data.hair_curves.new("pelo"); g = link(bpy.data.objects.new("pelo", cd)); cd.surface = body; cd.surface_uv_map = "UVMap"
t = Tree("fl")
gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves']); t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, 60000.0), gen.inputs['Density'])
gen.inputs['Hair Length'].default_value = 0.035; gen.inputs['Control Points'].default_value = 6; gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
t.geo = gen.outputs['Geometry']
with bpy.data.libraries.load(os.path.join(LAB,"receitas_grooming.blend"), link=False, assets_only=True) as (src, dst): dst.node_groups = ["GR Pentear por Curva"]
pc = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Pentear por Curva"]); t.chain(pc); pc.inputs["Curva de fluxo"].default_value = flow
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=2)
profile(t, EG, radius=0.0004)
set_mat(t, hair_mat("f", melanin=0.3, redness=0.9, roughness=0.35)); apply_tree(g, t.finish())
print("INFO lib", V, stats(g).get('curves'))
shot(f"t_lib11_{V}", res=420, samples=16, cam_loc=(0.45,-0.35,0.30), target=(0,0,0), lens=40)
