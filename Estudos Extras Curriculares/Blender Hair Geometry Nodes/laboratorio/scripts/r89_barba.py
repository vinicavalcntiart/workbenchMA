import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.55
V = sys.argv[-1]   # fio | bloco
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
me = head.data.copy(); bm = bmesh.new(); bm.from_mesh(me)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (f.calc_center_median().y < -0.03 and f.calc_center_median().z < -0.035 and abs(f.calc_center_median().x) < 0.08)], context='FACES')
bm.to_mesh(me); bm.free(); beard = link(bpy.data.objects.new("barba_reg", me)); beard.scale=(1.003,)*3; beard.hide_render = True
cd = bpy.data.hair_curves.new("barba"); g = link(bpy.data.objects.new("barba", cd)); cd.surface = beard; cd.surface_uv_map = "UVMap"
t = Tree("br")
def grp(name, out=None, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, out or n.outputs[0].name)
if V == "fio":
    grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.07, "Para fora": 0.6, "Para o lado da risca": 0.0, "Para trás": -0.3, "Gravidade": 1.5, "Guias por m2": 600000.0})
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.008, Existing_Guide_Map=False, Seed=1)
    profile(t, EG, radius=0.0004); set_mat(t, hair_mat("b", melanin=0.7, redness=0.8))
else:
    grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.08, "Para fora": 0.7, "Para o lado da risca": 0.0, "Para trás": -0.3, "Gravidade": 1.4, "Guias por m2": 4000.0})
    grp("GR Mecha Chunky", out='Mesh', **{"Raio": 0.012, "Achatamento": 0.35, "Torção máx (voltas)": 0.15, "Pontos por mecha": 16})
    grp("GR Normal da Malha", **{"Malha": head})
    m = MAT["GR Cabelo Cel"].copy()
    for n in m.node_tree.nodes:
        if n.bl_idname=='ShaderNodeBsdfToon' and n.component=='DIFFUSE': n.inputs['Color'].default_value=(0.45,0.15,0.05,1)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m; t.chain(sm)
    c = t.add('GeometryNodeGroup', group=GR["GR Contorno"]); t.chain(c, 'Mesh', 'Mesh'); c.inputs["Espessura"].default_value = 0.002
    bpy.context.scene.cycles.transparent_max_bounces = 64
apply_tree(g, t.finish())
print("INFO", V)
import lab as _l
_o = _l.render
def _r(p, **kw): bpy.context.scene.cycles.transparent_max_bounces = 64; return _o(p, **kw)
_l.render = _r
shot(f"89_{V}", res=440, samples=24, cam_loc=(0.30,-0.50,-0.06), target=(0,-0.04,-0.06), lens=48)
