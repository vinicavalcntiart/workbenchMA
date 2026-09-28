import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]   # sem | contorno | contorno_grosso | contorno_64
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("toon")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for k,v in {"Cabeça (colisão)": head, "Comprimento": 0.20, "Para fora": 0.5, "Para o lado da risca": 0.4, "Para trás": 0.2, "Gravidade": 1.0, "Guias por m2": 4000.0}.items(): x.inputs[k].default_value = v
t.chain(x, 'Geometry', 'Guias')
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = 3000.0; d.inputs["Viewport"].default_value = 1.0; t.chain(d)
ch = t.add('GeometryNodeGroup', group=GR["GR Mecha Chunky"]); ch.inputs["Raio"].default_value = 0.009; ch.inputs["Achatamento"].default_value = 0.4; t.chain(ch, 'Geometry', 'Mesh')
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = MAT["GR Cabelo Toon"]; t.chain(sm)
if V != "sem":
    base = t.geo
    fl = t.add('GeometryNodeFlipFaces'); t.link(base, fl.inputs['Mesh'])
    nn = t.add('GeometryNodeInputNormal'); sc_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nn.outputs[0], sc_.inputs[0]); sc_.inputs['Scale'].default_value = -(0.0025 if "grosso" in V else 0.0012)
    sp = t.add('GeometryNodeSetPosition'); t.link(fl.outputs[0], sp.inputs['Geometry']); t.link(sc_.outputs[0], sp.inputs['Offset'])
    om = bpy.data.materials.new("contorno"); nt = om.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); gm = nt.nodes.new('ShaderNodeNewGeometry'); tr = nt.nodes.new('ShaderNodeBsdfTransparent'); em = nt.nodes.new('ShaderNodeEmission'); em.inputs['Color'].default_value=(0.02,0.01,0.005,1)
    mx = nt.nodes.new('ShaderNodeMixShader')
    lp = nt.nodes.new('ShaderNodeLightPath'); inv = nt.nodes.new('ShaderNodeMath'); inv.operation='SUBTRACT'; inv.inputs[0].default_value=1.0; nt.links.new(lp.outputs['Is Camera Ray'], inv.inputs[1])
    mxm = nt.nodes.new('ShaderNodeMath'); mxm.operation='MAXIMUM'; nt.links.new(gm.outputs['Backfacing'], mxm.inputs[0]); nt.links.new(inv.outputs[0], mxm.inputs[1])
    nt.links.new(mxm.outputs[0] if "cam" in V else gm.outputs['Backfacing'], mx.inputs[0])
    nt.links.new(em.outputs[0], mx.inputs[1]); nt.links.new(tr.outputs[0], mx.inputs[2])
    nt.links.new(mx.outputs[0], o.inputs['Surface'])

    sm2 = t.add('GeometryNodeSetMaterial'); sm2.inputs['Material'].default_value = om; t.link(sp.outputs[0], sm2.inputs['Geometry'])
    j = t.add('GeometryNodeJoinGeometry'); t.link(base, j.inputs[0]); t.link(sm2.outputs[0], j.inputs[0]); t.geo = j.outputs[0]
apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ev = g.evaluated_get(dg); gs = ev.evaluated_geometry(); me = gs.mesh
import numpy as np
print("INFO", V, "faces", len(me.polygons) if me else None)
import lab as _l
_orig = _l.render
def _r(path, **kw):
    if V.endswith("_64") or "inv" in V or "cam" in V: bpy.context.scene.cycles.transparent_max_bounces = 64
    print("TB", bpy.context.scene.cycles.transparent_max_bounces); return _orig(path, **kw)
_l.render = _r
shot(f"53_{V}", res=440, samples=24, cam_loc=(0.50,-0.66,0.10), target=(0,0,-0.03), lens=45)
