import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
def load():
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    return {n.name: n for n in bpy.data.node_groups}, {m.name: m for m in bpy.data.materials}
def grp(t, GR, name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
def finish(t, GR, M, g, mat="GR Cabelo Cor por Mecha", rad=0.0005):
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=rad; t.chain(pr)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M[mat]; t.chain(sm); apply_tree(g, t.finish())
paths=[]; labels=[]
# 1 ponta virada p/ fora
reset(); GR, M = load(); head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
g = comb_guides(scalp, n=200, length=0.22, gravity=4.0, spread=0.3, outward=0.35)
t = Tree("a"); t.chain(grp(t,GR,"GR Densidade Livre", Viewport=1.0)); t.chain(grp(t,GR,"GR Mecha Estilizada")); t.chain(grp(t,GR,"GR Cor por Mecha"))
t.chain(grp(t,GR,"GR Ponta Virada", **{"Para fora":True})); finish(t,GR,M,g)
paths.append(shot("23_a", res=420, samples=16, cam_loc=(0.55,-0.45,-0.10), target=(0,0,-0.11), lens=50)); labels.append("GR Ponta Virada (fora)")
# 2 corte por regiao
reset(); GR, M = load(); head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
vgroup(scalp, "topo", lambda co: (co.z-0.02)/0.03)
g = comb_guides(scalp, n=220, length=0.12, gravity=1.5, spread=0.3, outward=0.6)
t = Tree("b"); t.chain(grp(t,GR,"GR Densidade Livre", Viewport=1.0)); t.chain(grp(t,GR,"GR Corte por Região")); finish(t,GR,M,g)
paths.append(shot("23_b", res=420, samples=16, cam_loc=(-0.25,0.45,-0.30), target=(0,0.02,0.0), lens=50)); labels.append("GR Corte por Regiao")
# 3 tranca
reset(); GR, M = load(); head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
p0 = Vector((0, 0.094, 0.035)).normalized()*0.1004; pts=[p0 + Vector((0, 0.045*math.sin(min(i/15*4,1.0)*1.57), -0.42*i/15)) for i in range(16)]
cd = bpy.data.hair_curves.new("g"); cd.add_curves([16]); cd.attributes['position'].data.foreach_set('vector', [c for v in pts for c in v])
g = link(bpy.data.objects.new("g", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("c"); t.chain(grp(t,GR,"GR Densidade Livre", Viewport=1.0, **{"Fios por m2":4e6, "Distância das guias":0.02})); t.chain(grp(t,GR,"GR Trança Grossa")); finish(t,GR,M,g,rad=0.0004)
paths.append(shot("23_c", res=420, samples=16, cam_loc=(-0.30,0.55,-0.15), target=(0,0.08,-0.2), lens=40)); labels.append("GR Tranca Grossa")
# 4 pelo
reset(); GR, M = load(); EG = essentials(); body = make_body(); body.data.materials.append(skin_mat()); g = fur_guides(body, n=600, length=0.035)
t = Tree("d"); t.chain(grp(t,GR,"GR Pelo em Tufos", Viewport=1.0, Subpelo=True, **{"Pelo de guarda":True}))
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = hair_mat("fur", melanin=0.25, redness=0.9, roughness=0.35); t.chain(sm); apply_tree(g, t.finish())
print("INFO pelo", stats(g).get('curves'))
paths.append(shot("23_d", res=420, samples=16, cam_loc=(0.42,-0.55,0.16), target=(0,0,0.0), lens=55)); labels.append("GR Pelo em Tufos (sub+guarda)")
print("SHEET", sheet(paths, labels, os.path.join(OUT,"23_lib2_sheet.png"), cols=4))
