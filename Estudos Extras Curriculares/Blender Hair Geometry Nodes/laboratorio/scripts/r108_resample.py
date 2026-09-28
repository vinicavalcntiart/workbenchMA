import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # count | length
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("rs")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
x = grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.30}); t.chain(x, 'Geometry', 'Guias')
d = grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 300000.0}); t.chain(d)
m = grp("GR Mecha Estilizada"); t.chain(m, m.inputs[0].name, m.outputs[0].name)
# corte em camadas: topo curto (10%), laterais medias, nuca longa
mk = grp("GR Máscara por Posição", **{"Altura mín": 0.06, "Borda suave": 0.01})
mr = t.add('ShaderNodeMapRange'); t.link(mk.outputs[0], mr.inputs['Value']); mr.inputs['To Min'].default_value = 1.0; mr.inputs['To Max'].default_value = 0.12
tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); tr.inputs['Replace Length'].default_value = False; t.chain(tr); t.link(mr.outputs['Result'], tr.inputs['Length Factor'])
rs = t.add('GeometryNodeResampleCurve'); t.chain(rs, 'Curve', 'Curve')
if V == "count": rs.inputs['Mode'].default_value = 'Count'; rs.inputs['Count'].default_value = 24
else: rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.0125
o = grp("GR Onda S"); t.chain(o, o.inputs[0].name, o.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.5, redness=0.6)); m_ = apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get(); ts=[]
for i in range(3):
    m_.show_viewport=False; dg.update(); m_.show_viewport=True; t0=time.time(); dg.update(); g.evaluated_get(dg).data.points; ts.append(time.time()-t0)
print("RS", V, "fios", stats(g).get('curves'), "pontos", stats(g).get('points'), "ms", round(min(ts)*1000))
shot(f"108_{V}", res=380, samples=16, cam_loc=(0.42,-0.62,0.08), target=(0,0,-0.06), lens=46)
