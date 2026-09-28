import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # sem | reta | bico
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.02,0.015,0.01,1); scalp.data.materials.append(sm_)
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
# malha de corte: esfera grande aparada por um "rodape" em z; na frente, a borda da franja
me = bpy.data.meshes.new("corte"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=96, v_segments=48, radius=1.0)
bmesh.ops.scale(bm, vec=(0.2,0.2,0.25), verts=bm.verts)
import math
def borda(x, y):
    if y < -0.04:   # frente: franja
        if V == "reta": return 0.035
        if V == "bico": return 0.035 - 0.015*abs(math.sin(x*140))
    return -0.35
bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < borda(f.calc_center_median().x, f.calc_center_median().y)], context='FACES')
bm.to_mesh(me); bm.free(); corte = link(bpy.data.objects.new("corte", me)); corte.hide_render = True
t = Tree("fr")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.30, "Para fora": 0.35, "Para o lado da risca": 0.0, "Para trás": 0.15, "Gravidade": 2.2})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 300000.0})
grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.012})
if V != "sem": grp("GR Corte pela Malha", **{"Malha do corte": corte})
profile(t, EG, radius=0.0005, shape=0.1)
set_mat(t, hair_mat("h", melanin=0.98, redness=0.2, roughness=0.3)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"100_{V}", res=420, samples=16, cam_loc=(0.15,-0.66,0.02), target=(0,0,-0.02), lens=46)
