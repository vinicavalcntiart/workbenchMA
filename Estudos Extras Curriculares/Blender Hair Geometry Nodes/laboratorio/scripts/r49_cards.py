import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
import numpy as np
MODE = sys.argv[-2]; DENS = float(sys.argv[-1])   # MODE: twist | nraiz | cross
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("cards")
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = DENS; d.inputs["Viewport"].default_value = 1.0; t.chain(d)
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 10; t.chain(rs, 'Curve', 'Curve')
pr = t.eg(EG['Set Hair Curve Profile'], Radius=0.009, Shape=0.4, Factor_Min=0.0, Factor_Max=1.0)   # meia largura do card
if MODE != "twist":
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); na.inputs['Name'].default_value = 'n_raiz'
    nv = na.outputs['Attribute']
    if MODE == "cross":
        tg = t.add('GeometryNodeInputTangent'); cx = t.add('ShaderNodeVectorMath', props={'operation':'CROSS_PRODUCT'}); t.link(tg.outputs[0], cx.inputs[0]); t.link(nv, cx.inputs[1]); nv = cx.outputs[0]
    sn = t.add('GeometryNodeSetCurveNormal'); t.chain(sn, 'Curve', 'Curve'); sn.inputs['Mode'].default_value = 'Free'; t.link(nv, sn.inputs['Normal'])
sp = t.add('GeometryNodeSplineParameter')
sv = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'POINT'}); sv.inputs['Name'].default_value='v'; t.chain(sv); t.link(sp.outputs['Factor'], sv.inputs['Value'])
ln = t.add('GeometryNodeCurvePrimitiveLine'); ln.inputs['Start'].default_value=(-1,0,0); ln.inputs['End'].default_value=(1,0,0)
sp2 = t.add('GeometryNodeSplineParameter')
su = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'POINT'}); su.inputs['Name'].default_value='u'; t.link(ln.outputs[0], su.inputs['Geometry']); t.link(sp2.outputs['Factor'], su.inputs['Value'])
cm = t.add('GeometryNodeCurveToMesh'); t.chain(cm, 'Curve', 'Mesh'); t.link(su.outputs['Geometry'], cm.inputs['Profile Curve'])
rr = t.add('GeometryNodeInputRadius'); t.link(rr.outputs[0], cm.inputs['Scale'])
au = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}); au.inputs['Name'].default_value='u'
av = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}); av.inputs['Name'].default_value='v'
cb = t.add('ShaderNodeCombineXYZ'); t.link(au.outputs['Attribute'], cb.inputs['X']); t.link(av.outputs['Attribute'], cb.inputs['Y'])
uv = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT2','domain':'CORNER'}); uv.inputs['Name'].default_value='UVMap'; t.chain(uv); t.link(cb.outputs[0], uv.inputs['Value'])
ss = t.add('GeometryNodeSetShadeSmooth'); t.chain(ss)
# material de card: faixas de fio no U, ponta some no V
m = bpy.data.materials.new("card"); nt = m.node_tree; b = nt.nodes['Principled BSDF']
b.inputs['Base Color'].default_value=(0.16,0.07,0.03,1); b.inputs['Roughness'].default_value=0.45
uvn = nt.nodes.new('ShaderNodeUVMap'); uvn.uv_map='UVMap'
sep = nt.nodes.new('ShaderNodeSeparateXYZ'); nt.links.new(uvn.outputs[0], sep.inputs[0])
nz = nt.nodes.new('ShaderNodeTexNoise'); nz.noise_dimensions='2D'
mp = nt.nodes.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value=(40,1.5,1); nt.links.new(uvn.outputs[0], mp.inputs[0]); nt.links.new(mp.outputs[0], nz.inputs['Vector']); nz.inputs['Scale'].default_value=1.0; nz.inputs['Detail'].default_value=2
cr = nt.nodes.new('ShaderNodeMapRange'); cr.inputs['From Min'].default_value=0.45; cr.inputs['From Max'].default_value=0.55; nt.links.new(nz.outputs['Fac'], cr.inputs['Value'])
# borda: 1 - |2u-1|^4 ; ponta: 1 - v^3
e1 = nt.nodes.new('ShaderNodeMath'); e1.operation='MULTIPLY_ADD'; e1.inputs[1].default_value=2; e1.inputs[2].default_value=-1; nt.links.new(sep.outputs['X'], e1.inputs[0])
e2 = nt.nodes.new('ShaderNodeMath'); e2.operation='ABSOLUTE'; nt.links.new(e1.outputs[0], e2.inputs[0])
e3 = nt.nodes.new('ShaderNodeMath'); e3.operation='POWER'; e3.inputs[1].default_value=4; nt.links.new(e2.outputs[0], e3.inputs[0])
e4 = nt.nodes.new('ShaderNodeMath'); e4.operation='SUBTRACT'; e4.inputs[0].default_value=1; nt.links.new(e3.outputs[0], e4.inputs[1])
p1 = nt.nodes.new('ShaderNodeMath'); p1.operation='POWER'; p1.inputs[1].default_value=3; nt.links.new(sep.outputs['Y'], p1.inputs[0])
p2 = nt.nodes.new('ShaderNodeMath'); p2.operation='SUBTRACT'; p2.inputs[0].default_value=1; nt.links.new(p1.outputs[0], p2.inputs[1])
a1 = nt.nodes.new('ShaderNodeMath'); a1.operation='MULTIPLY'; nt.links.new(cr.outputs['Result'], a1.inputs[0]); nt.links.new(e4.outputs[0], a1.inputs[1])
a2 = nt.nodes.new('ShaderNodeMath'); a2.operation='MULTIPLY'; nt.links.new(a1.outputs[0], a2.inputs[0]); nt.links.new(p2.outputs[0], a2.inputs[1])
nt.links.new(a2.outputs[0], b.inputs['Alpha'])
# raiz mais escura
cr2 = nt.nodes.new('ShaderNodeMix'); cr2.data_type='RGBA'; cr2.inputs[6].default_value=(0.05,0.02,0.01,1); cr2.inputs[7].default_value=(0.22,0.10,0.045,1)
nt.links.new(sep.outputs['Y'], cr2.inputs[0]); nt.links.new(cr2.outputs[2], b.inputs['Base Color'])
set_mat(t, m); apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ev = g.evaluated_get(dg); gs = ev.evaluated_geometry(); me = gs.mesh
N = np.array([p.normal[:] for p in me.polygons]); C = np.array([p.center[:] for p in me.polygons])
rad = C/np.linalg.norm(C,axis=1)[:,None]; dots = np.abs((N*rad).sum(1))
print("INFO", MODE, int(DENS), "cards", len(me.polygons)//9, "tris", len(me.polygons)*2, "deitado(|n.radial|) medio", round(float(dots.mean()),2), "uv", 'UVMap' in [a.name for a in me.attributes])
shot(f"49_{MODE}_{int(DENS)}", res=420, samples=24, cam_loc=(0.45,-0.60,0.08), target=(0,0,-0.04), lens=45)
