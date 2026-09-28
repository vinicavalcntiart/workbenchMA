import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.7
V = sys.argv[-1]   # atravessa | dobra
FZ = -0.55
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
bpy.ops.mesh.primitive_plane_add(size=3, location=(0,0,FZ)); fl = bpy.context.object
fm = bpy.data.materials.new("chao"); fm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.35,0.3,0.25,1); fl.data.materials.append(fm)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("chao")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 1.1, "Para fora": 0.3, "Para o lado da risca": 0.25, "Para trás": 0.35, "Gravidade": 3.0, "Guias por m2": 4000.0}.items(): x.inputs[kk].default_value = v
t.chain(x, 'Geometry', 'Guias')
rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 60; t.chain(rs, 'Curve', 'Curve')
if V == "dobra":
    ps = t.add('GeometryNodeInputPosition'); sx = t.add('ShaderNodeSeparateXYZ'); t.link(ps.outputs[0], sx.inputs[0])
    dp = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); dp.inputs[0].default_value = FZ + 0.003; t.link(sx.outputs['Z'], dp.inputs[1])
    mx = t.add('ShaderNodeMath', props={'operation':'MAXIMUM'}); t.link(dp.outputs[0], mx.inputs[0]); mx.inputs[1].default_value = 0.0
    hz = t.add('ShaderNodeCombineXYZ'); t.link(sx.outputs['X'], hz.inputs['X']); t.link(sx.outputs['Y'], hz.inputs['Y'])
    ad0 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(hz.outputs[0], ad0.inputs[0]); ad0.inputs[1].default_value = (0, 0.05, 0)
    nd = t.add('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); t.link(ad0.outputs[0], nd.inputs[0])
    sp1 = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nd.outputs[0], sp1.inputs[0]); t.link(mx.outputs[0], sp1.inputs['Scale'])
    up = t.add('ShaderNodeCombineXYZ'); t.link(mx.outputs[0], up.inputs['Z'])
    of = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(sp1.outputs[0], of.inputs[0]); t.link(up.outputs[0], of.inputs[1])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(of.outputs[0], s.inputs['Offset'])
for n in ("GR Densidade Livre","GR Mecha Estilizada","GR Cor por Mecha"):
    nd_ = t.add('GeometryNodeGroup', group=GR[n]); t.chain(nd_, nd_.inputs[0].name, nd_.outputs[0].name)
    if n=="GR Densidade Livre": nd_.inputs["Viewport"].default_value = 1.0; nd_.inputs["Fios por m2"].default_value = 200000.0
if V == "dobra":   # de novo nos filhos (a interpolacao pode furar o chao)
    ps2 = t.add('GeometryNodeInputPosition'); sx2 = t.add('ShaderNodeSeparateXYZ'); t.link(ps2.outputs[0], sx2.inputs[0])
    mz = t.add('ShaderNodeMath', props={'operation':'MAXIMUM'}); t.link(sx2.outputs['Z'], mz.inputs[0]); mz.inputs[1].default_value = FZ + 0.002
    cz = t.add('ShaderNodeCombineXYZ'); t.link(sx2.outputs['X'], cz.inputs['X']); t.link(sx2.outputs['Y'], cz.inputs['Y']); t.link(mz.outputs[0], cz.inputs['Z'])
    s2 = t.add('GeometryNodeSetPosition'); t.chain(s2); t.link(cz.outputs[0], s2.inputs['Position'])
profile(t, EG, radius=0.0006)
set_mat(t, hair_mat("h", melanin=0.1, redness=0.9, roughness=0.3)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'), stats(g).get('points'))
shot(f"65_{V}", res=480, samples=20, cam_loc=(1.1,-1.3,0.25), target=(0,0.1,-0.35), lens=40)
