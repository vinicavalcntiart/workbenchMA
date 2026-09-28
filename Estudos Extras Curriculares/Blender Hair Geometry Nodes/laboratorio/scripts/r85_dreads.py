import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # liso | textura
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("scalp"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.03,0.015,0.01,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("dr")
def grp(name, out=None, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, out or n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.30, "Para fora": 0.6, "Para o lado da risca": 0.35, "Para trás": 0.25, "Gravidade": 1.6, "Guias por m2": 4000.0})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 2200.0})
grp("GR Onda S", **{"Período": 0.25, "Amplitude": 0.01})
ch = grp("GR Mecha Chunky", out='Mesh', **{"Raio": 0.007, "Achatamento": 1.0, "Torção máx (voltas)": 0.0, "Pontos por mecha": 48})
if V == "textura":   # nos: engrossa e afina ao longo (seno no raio) + deslocamento por Noise
    ps = t.add('GeometryNodeInputPosition'); nz = t.add('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 180.0; nz.inputs['Detail'].default_value = 3.0; t.link(ps.outputs[0], nz.inputs['Vector'])
    mr = t.add('ShaderNodeMapRange'); t.link(nz.outputs['Fac'], mr.inputs['Value']); mr.inputs['To Min'].default_value = -0.0012; mr.inputs['To Max'].default_value = 0.0012
    nn = t.add('GeometryNodeInputNormal'); sc_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(nn.outputs[0], sc_.inputs[0]); t.link(mr.outputs['Result'], sc_.inputs['Scale'])
    sp = t.add('GeometryNodeSetPosition'); t.chain(sp); t.link(sc_.outputs[0], sp.inputs['Offset'])
m = bpy.data.materials.new("dread"); b = m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value = (0.06,0.03,0.015,1); b.inputs['Roughness'].default_value = 0.75
pass
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m; t.chain(sm)
apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ev = g.evaluated_get(dg); gs = ev.evaluated_geometry(); me = gs.mesh
print("INFO", V, "faces", len(me.polygons) if me else None)
shot(f"85_{V}", res=440, samples=24, cam_loc=(0.45,-0.62,0.05), target=(0,0,-0.08), lens=42)
