import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); scalp.hide_render = True
def toon(name, col, size=0.5):
    m = bpy.data.materials.new(name); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial')
    d = nt.nodes.new('ShaderNodeBsdfToon'); d.component='DIFFUSE'; d.inputs['Color'].default_value=(*col,1); d.inputs['Size'].default_value=size; d.inputs['Smooth'].default_value=0.03
    nt.links.new(d.outputs[0], o.inputs['Surface']); return m
head.data.materials.append(toon("pele", (0.95,0.72,0.58), 0.7))
# cabelo toon azul
hm = MAT["GR Cabelo Toon"].copy(); hm.name = "cabelo_toon"
for n in hm.node_tree.nodes:
    if n.bl_idname=='ShaderNodeBsdfToon' and n.component=='DIFFUSE': n.inputs['Color'].default_value=(0.05,0.12,0.45,1)
    if n.bl_idname=='ShaderNodeBsdfToon' and n.component=='GLOSSY': n.inputs['Color'].default_value=(0.35,0.55,0.9,1)
w = toon("olho", (0.97,0.97,0.97), 0.9); k = toon("iris", (0.02,0.02,0.05), 0.9)
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02, location=(sx*0.036,-0.086,0.0)); e=bpy.context.object; e.scale=(0.8,0.5,1.2); e.data.materials.append(w); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(sx*0.034,-0.096,-0.002)); p=bpy.context.object; p.scale=(0.8,0.5,1.3); p.data.materials.append(k); bpy.ops.object.shade_smooth()
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("npr")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.20, "Para fora": 0.7, "Para o lado da risca": 0.5, "Para trás": 0.35, "Gravidade": 1.3, "Guias por m2": 4000.0}.items(): x.inputs[kk].default_value = v
t.chain(x, 'Geometry', 'Guias')
d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Fios por m2"].default_value = 3000.0; d.inputs["Viewport"].default_value = 1.0; t.chain(d)
# ahoge: fio mais proximo da coroa em arco (17.52)
cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
di = t.add('ShaderNodeVectorMath', props={'operation':'DISTANCE'}); t.link(cr.outputs['Root Position'], di.inputs[0]); di.inputs[1].default_value = (0.0,-0.02,0.1)
c1 = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}); t.link(di.outputs['Value'], c1.inputs[0]); c1.inputs[1].default_value = 0.012
sp = t.add('GeometryNodeSplineParameter'); t2 = t.add('ShaderNodeMath', props={'operation':'POWER'}); t.link(sp.outputs['Factor'], t2.inputs[0]); t2.inputs[1].default_value = 2.0
yy = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(t2.outputs[0], yy.inputs[0]); yy.inputs[1].default_value = -0.08
z1 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], z1.inputs[0]); z1.inputs[1].default_value = 0.11
z2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(t2.outputs[0], z2.inputs[0]); z2.inputs[1].default_value = -0.06
zz = t.add('ShaderNodeMath', props={'operation':'ADD'}); t.link(z1.outputs[0], zz.inputs[0]); t.link(z2.outputs[0], zz.inputs[1])
cb = t.add('ShaderNodeCombineXYZ'); t.link(yy.outputs[0], cb.inputs['Y']); t.link(zz.outputs[0], cb.inputs['Z'])
ad = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(cr.outputs['Root Position'], ad.inputs[0]); t.link(cb.outputs[0], ad.inputs[1])
s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(c1.outputs[0], s.inputs['Selection']); t.link(ad.outputs[0], s.inputs['Position'])
ch = t.add('GeometryNodeGroup', group=GR["GR Mecha Chunky"]); ch.inputs["Raio"].default_value = 0.018; ch.inputs["Achatamento"].default_value = 0.3; ch.inputs["Torção máx (voltas)"].default_value = 0.0; t.chain(ch, 'Geometry', 'Mesh')
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = hm; t.chain(sm)
c = t.add('GeometryNodeGroup', group=GR["GR Contorno"]); t.chain(c, 'Mesh', 'Mesh'); c.inputs["Espessura"].default_value = 0.0022
apply_tree(g, t.finish())
# contorno da cabeca tambem (mesma receita, num modificador de GN na cabeca)
th = Tree("cont_head"); ch2 = th.add('GeometryNodeGroup', group=GR["GR Contorno"]); th.chain(ch2, 'Mesh', 'Mesh'); ch2.inputs["Espessura"].default_value = 0.0018; apply_tree(head, th.finish())
bpy.context.scene.cycles.transparent_max_bounces = 64
lab_render = lab.render
def r2(path, **kw):
    bpy.context.scene.cycles.transparent_max_bounces = 64; wn = bpy.context.scene.world.node_tree; bgn = wn.nodes['Background']; bgn.inputs[0].default_value=(0.08,0.08,0.09,1)
    if 'camfundo' not in wn.nodes:
        b2 = wn.nodes.new('ShaderNodeBackground'); b2.name='camfundo'; b2.inputs[0].default_value=(0.86,0.88,0.92,1)
        lp = wn.nodes.new('ShaderNodeLightPath'); mx = wn.nodes.new('ShaderNodeMixShader'); out = wn.nodes['World Output']
        wn.links.new(lp.outputs['Is Camera Ray'], mx.inputs[0]); wn.links.new(bgn.outputs[0], mx.inputs[1]); wn.links.new(b2.outputs[0], mx.inputs[2]); wn.links.new(mx.outputs[0], out.inputs['Surface'])
    return lab_render(path, **kw)
lab.render = r2
shot("63_npr", res=900, samples=32, cam_loc=(0.30,-0.55,0.08), target=(0,-0.02,0.0), lens=50)
