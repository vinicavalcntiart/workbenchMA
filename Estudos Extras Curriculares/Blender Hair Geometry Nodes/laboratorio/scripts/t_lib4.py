import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; M = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("so_grupos")
def grp(n, out='Geometry', **kw):
    x = t.add('GeometryNodeGroup', group=GR[n])
    for k,v in kw.items(): x.inputs[k].default_value = v
    return t.chain(x, 'Geometry', out)
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head, "Comprimento":0.2, "Gravidade":1.0, "Para fora":0.55})
grp("GR Densidade Livre", Viewport=1.0)
grp("GR Mecha Estilizada")
grp("GR Volume na Raiz")
grp("GR Ponta Virada", **{"Para fora":True})
grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm)
apply_tree(g, t.finish()); print("INFO", stats(g).get('curves'), "nodes no tree:", len(t.ng.nodes))
p = shot("32_zero_sculpt", res=640, samples=24, cam_loc=(0.42,-0.62,0.02), target=(0,0,-0.06), lens=48); print("OK", p)
