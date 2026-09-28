import sys; sys.path.insert(0,'.')
from lab import *
import lab
LIB = os.path.join(LAB, "receitas_grooming.blend")
which = sys.argv[-1]
def load():
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    return {n.name: n for n in bpy.data.node_groups}, {m.name: m for m in bpy.data.materials}
def grp(t, GR, name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return n
def backdrop(col=(0.18,0.2,0.24)):
    bpy.ops.mesh.primitive_plane_add(size=4, location=(0,1.2,0)); p = bpy.context.object; p.rotation_euler=(math.radians(90),0,0)
    m = bpy.data.materials.new("bd"); m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*col,1); m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=0.9
    p.data.materials.append(m)
def neck(head_mat):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.18, location=(0,0.01,-0.15)); n = bpy.context.object
    n.data.materials.append(head_mat); bpy.ops.object.shade_smooth()
def eyes(z=0.01, y=-0.085, x=0.035, r=0.017):
    w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1); w.node_tree.nodes['Principled BSDF'].inputs['Coat Weight'].default_value=1.0
    k = bpy.data.materials.new("pupil"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.01,0.01,0.01,1); k.node_tree.nodes['Principled BSDF'].inputs['Coat Weight'].default_value=1.0
    for sx in (-1,1):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(sx*x, y, z)); e = bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r*0.45, location=(sx*x*0.97, y-r*0.75, z)); p = bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
def mat_melanin(base, mel_lo, mel_hi, red):
    m = base.copy(); nt = m.node_tree
    nt.nodes['Principled Hair BSDF'].inputs['Melanin Redness'].default_value = red
    mr = [n for n in nt.nodes if n.bl_idname=='ShaderNodeMapRange' and n.inputs['To Max'].default_value > 0.5][0]
    mr.inputs['To Min'].default_value = mel_lo; mr.inputs['To Max'].default_value = mel_hi
    return m
RES = 1024; SAMPLES = 64
if which == "pixar":
    reset(); GR, M = load(); lab.LIGHT_K = 0.55
    head, scalp = make_head(); sk = skin_mat(); head.data.materials.append(sk); scalp.hide_render=True; neck(sk); eyes(); backdrop()
    g = comb_guides(scalp, n=240, length=0.20, gravity=4.0, spread=0.3, outward=0.35, seed=3)
    t = Tree("pixar")
    t.chain(grp(t,GR,"GR Densidade Livre", Viewport=1.0, **{"Fios por m2": 450000.0}))
    m = t.chain(grp(t,GR,"GR Mecha Estilizada", **{"Tamanho da mecha":0.022})); side = grp(t,GR,"GR Lado da Risca", **{"Posição da risca X":0.02}); t.link(side.outputs['Lado'], m.inputs['Group ID'])
    t.chain(grp(t,GR,"GR Volume na Raiz", Volume=0.02, **{"Sobe até":0.2}))
    t.chain(grp(t,GR,"GR Strays em Arco", **{"Fração":0.03}))
    t.chain(grp(t,GR,"GR Ponta Virada", **{"Para fora":False, "Comprimento do rolo":0.05}))
    t.chain(grp(t,GR,"GR Cor por Mecha"))
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = mat_melanin(M["GR Cabelo Cor por Mecha"], 0.55, 0.85, 0.45); t.chain(sm)
    apply_tree(g, t.finish()); print("INFO", which, stats(g).get('curves'))
    lab.stage(cam_loc=(0.36,-0.52,0.06), target=(0,0,-0.04), lens=55, res=RES, samples=SAMPLES)
elif which == "merida":
    reset(); GR, M = load(); lab.LIGHT_K = 0.55
    head, scalp = make_head(); sk = skin_mat(); head.data.materials.append(sk); scalp.hide_render=True; neck(sk); eyes(); backdrop((0.12,0.16,0.14))
    g = comb_guides(scalp, n=260, length=0.26, gravity=2.0, spread=0.5, outward=0.6, seed=4)
    t = Tree("merida")
    t.chain(grp(t,GR,"GR Densidade Livre", Viewport=1.0, **{"Fios por m2": 350000.0}))
    t.chain(grp(t,GR,"GR Mecha Estilizada", **{"Tamanho da mecha":0.018}))
    t.chain(grp(t,GR,"GR Volume na Raiz", Volume=0.025, **{"Sobe até":0.25}))
    t.chain(grp(t,GR,"GR Strays em Arco", **{"Fração":0.03}))
    t.chain(grp(t,GR,"GR Cacho por Mecha", **{"Raio mín":0.009, "Raio máx":0.016, "Voltas por metro mín":22.0, "Voltas por metro máx":38.0}))
    t.chain(grp(t,GR,"GR Cor por Mecha"))
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0006; t.chain(pr)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = mat_melanin(M["GR Cabelo Cor por Mecha"], 0.25, 0.5, 1.0); t.chain(sm)
    apply_tree(g, t.finish()); print("INFO", which, stats(g).get('curves'))
    lab.stage(cam_loc=(0.40,-0.62,0.02), target=(0,0,-0.07), lens=50, res=RES, samples=SAMPLES)
elif which == "dreamworks":
    reset(); GR, M = load(); lab.LIGHT_K = 0.5
    body = make_body(); sk = skin_mat(); body.data.materials.append(sk); backdrop((0.2,0.17,0.22))
    eyes(z=0.05, y=-0.155, x=0.05, r=0.028)
    g = fur_guides(body, n=700, length=0.035, seed=5)
    t = Tree("dw")
    t.chain(grp(t,GR,"GR Pelo em Tufos", Viewport=1.0, Subpelo=True, **{"Pelo de guarda":True, "Tamanho do tufo":0.009}))
    t.chain(grp(t,GR,"GR Cor por Mecha"))
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = mat_melanin(M["GR Cabelo Cor por Mecha"], 0.15, 0.4, 0.95); t.chain(sm)
    apply_tree(g, t.finish()); print("INFO", which, stats(g).get('curves'))
    lab.stage(cam_loc=(0.30,-0.62,0.14), target=(0,0,0.0), lens=50, res=RES, samples=SAMPLES)
p = os.path.join(OUT, f"25_hero_{which}.png"); tt = render(p); print("RENDER", which, tt, "s")
