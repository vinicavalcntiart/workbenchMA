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
# fluxo: tangente da curva mais proxima da raiz, projetada no plano da pele
oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = flow
c2p0 = t.add('GeometryNodeCurveToPoints', props={'mode':'EVALUATED'}); t.link(oi.outputs['Geometry'], c2p0.inputs['Curve'])
cap = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}); cap.inputs['Name'].default_value='fx'; t.link(c2p0.outputs['Points'], cap.inputs['Geometry']); t.link(c2p0.outputs['Tangent'], cap.inputs['Value'])
class _W: pass
c2p = _W(); c2p.outputs = {'Points': cap.outputs[0]}
cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
sn = t.add('GeometryNodeSampleNearest', props={'domain':'POINT'}); t.link(c2p.outputs['Points'], sn.inputs['Geometry']); t.link(cr.outputs['Root Position'], sn.inputs['Sample Position'])
fx = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); fx.inputs['Name'].default_value='fx'
si = t.add('GeometryNodeSampleIndex', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}); t.link(c2p.outputs['Points'], si.inputs['Geometry']); t.link(fx.outputs['Attribute'], si.inputs['Value']); t.link(sn.outputs['Index'], si.inputs['Index'])
nrm = gen.outputs['Surface Normal']
dt = t.add('ShaderNodeVectorMath', props={'operation':'DOT_PRODUCT'}); t.link(si.outputs[0], dt.inputs[0]); t.link(nrm, dt.inputs[1])
sc1 = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nrm, sc1.inputs[0]); t.link(dt.outputs['Value'], sc1.inputs['Scale'])
pj = t.add('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); t.link(si.outputs[0], pj.inputs[0]); t.link(sc1.outputs[0], pj.inputs[1])
nd = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(pj.outputs[0], nd.inputs[0])
# direcao = normal*0.35 + fluxo*0.65 ; posicao = raiz + dir * t * L  (fio reto; o Clump e a gravidade fazem o resto)
a1 = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nrm, a1.inputs[0]); a1.inputs['Scale'].default_value = 0.35
a2 = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nd.outputs[0], a2.inputs[0]); a2.inputs['Scale'].default_value = 0.65
ad = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a1.outputs[0], ad.inputs[0]); t.link(a2.outputs[0], ad.inputs[1])
spp = t.add('GeometryNodeSplineParameter'); ln = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(spp.outputs['Length'], ln.inputs[0]); ln.inputs[1].default_value = 1.0
nd2 = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(ad.outputs[0], nd2.inputs[0])
of = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nd2.outputs[0], of.inputs[0]); t.link(spp.outputs['Length'], of.inputs['Scale'])
pos = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(cr.outputs['Root Position'], pos.inputs[0]); t.link(of.outputs[0], pos.inputs[1])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(pos.outputs[0], s.inputs['Position'])
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=2)
profile(t, EG, radius=0.0004)
set_mat(t, hair_mat("f", melanin=0.3, redness=0.9, roughness=0.35)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"60_{V}", res=420, samples=16, cam_loc=(0.45,-0.35,0.30), target=(0,0,0), lens=40)
