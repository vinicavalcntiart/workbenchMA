import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("c2"); src_geo = t.geo
def branch(L, out, lado, tras, grav):
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": out, "Para o lado da risca": lado, "Para trás": tras, "Gravidade": grav}.items(): x.inputs[kk].default_value = v
    t.link(src_geo, x.inputs[0])
    d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 300000.0; t.link(x.outputs['Guias'], d.inputs[0])
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.link(d.outputs[0], rs.inputs['Curve'])
    return rs.outputs['Curve']
A = branch(0.12, 0.8, 0.3, 0.8, 0.4)           # curto penteado para tras
B = branch(0.05, 0.2, 0.0, 0.0, 3.0)            # costeleta: curta e vertical
mk = t.add('GeometryNodeGroup', group=GR["GR Máscara por Posição"])
for k,v in {"Frente máx (Y)": 0.03, "Frente mín (Y)": -0.06, "Altura máx": 0.02, "Lateral mín (|X|)": 0.075, "Borda suave": 0.01}.items(): mk.inputs[k].default_value = v
tr = t.add('GeometryNodeGroup', group=GR["GR Transição"]); t.link(A, tr.inputs[0]); t.link(B, tr.inputs[1]); t.link(mk.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
m = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); m.inputs["Tamanho da mecha"].default_value = 0.012
t.chain(m, m.inputs[0].name, m.outputs[0].name)
c = t.add('GeometryNodeGroup', group=GR["GR Cor por Mecha"]); t.chain(c, c.inputs[0].name, c.outputs[0].name)
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.8, redness=0.4)); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'))
me2 = head.data.copy(); bm2 = bmesh.new(); bm2.from_mesh(me2)
bmesh.ops.delete(bm2, geom=[f for f in bm2.faces if not (abs(f.calc_center_median().x) > 0.08 and -0.045 < f.calc_center_median().z < 0.03 and -0.05 < f.calc_center_median().y < -0.015)], context='FACES')
bm2.to_mesh(me2); bm2.free(); reg = link(bpy.data.objects.new("costeleta", me2)); reg.scale = (1.003,)*3; reg.hide_render = True
cc = bpy.data.hair_curves.new("cost"); gc = link(bpy.data.objects.new("costeleta_pelo", cc)); cc.surface = reg; cc.surface_uv_map = "UVMap"
tc = Tree("cost"); x = tc.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.035, "Para fora": 0.3, "Para o lado da risca": 0.0, "Para trás": 0.0, "Gravidade": 3.0, "Guias por m2": 700000.0}.items(): x.inputs[kk].default_value = v
tc.chain(x, 'Geometry', 'Guias')
tc.eg(EG['Clump Hair Curves'], Factor=0.8, Shape=0.3, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.005, Existing_Guide_Map=False, Seed=1)
profile(tc, EG, radius=0.0004); set_mat(tc, hair_mat("c", melanin=0.8, redness=0.4)); apply_tree(gc, tc.finish())
print("COST2 fios", stats(gc).get('curves'))
shot("109_costeleta", res=420, samples=16, cam_loc=(0.62,-0.30,0.0), target=(0,0,0.0), lens=46)
