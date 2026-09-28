import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # topete | lado
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.1,0.06,0.04,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("uc")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
gp = grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.12, "Para fora": 0.9 if V=="topete" else 0.6, "Para o lado da risca": 0.2 if V=="topete" else 1.0, "Para trás": 0.8 if V=="topete" else 0.3, "Gravidade": 0.4, "Guias por m2": 5000.0})
t.chain(gp, 'Geometry', 'Guias')
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 350000.0}); t.chain(d)
v = grp("GR Volume na Raiz"); t.chain(v, v.inputs[0].name, v.outputs[0].name)
mc = grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.018}); t.chain(mc, mc.inputs[0].name, mc.outputs[0].name)
base = t.geo
# laterais e nuca raspadas: Trim 1 cm fora da mascara do topo
mk = grp("GR Máscara por Posição", **{"Altura mín": 0.075, "Borda suave": 0.006, "Lateral máx (|X|)": 0.05, "Inverter": True})
mr = t.add('ShaderNodeMapRange'); t.link(mk.outputs[0], mr.inputs['Value']); mr.inputs['To Min'].default_value = 1.0; mr.inputs["To Max"].default_value = 0.05
tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); tr.inputs['Replace Length'].default_value = False; t.link(base, tr.inputs['Geometry']); t.link(mr.outputs['Result'], tr.inputs['Length Factor'])
t.geo = tr.outputs[0]
c = grp("GR Cor por Mecha"); t.chain(c, c.inputs[0].name, c.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.75, redness=0.5)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"94_{V}", res=420, samples=16, cam_loc=(0.55,-0.45,0.08), target=(0,0,0.0), lens=46)
