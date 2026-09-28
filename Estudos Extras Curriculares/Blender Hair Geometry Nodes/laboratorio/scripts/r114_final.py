import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(nape=-0.7, front_cut=0.75); head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("sc"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.12,0.05,0.02,1); scalp.data.materials.append(sm_)
exec('def split_scalp' + open('r17_part.py').read().split("def build(")[0].split("def split_scalp")[1]); split_scalp(scalp)
w = bpy.data.materials.new("eye"); w.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.9,0.9,0.88,1)
k = bpy.data.materials.new("pup"); k.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.03,0.02,0.02,1)
for sx in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.016, location=(sx*0.034,-0.088,0.0)); e=bpy.context.object; e.data.materials.append(w); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0075, location=(sx*0.033,-0.101,0.0)); p=bpy.context.object; p.data.materials.append(k); bpy.ops.object.shade_smooth()
me = head.data.copy(); bm = bmesh.new(); bm.from_mesh(me)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if not (f.calc_center_median().y < -0.07 and 0.018 < f.calc_center_median().z < 0.030 and 0.012 < abs(f.calc_center_median().x) < 0.058)], context='FACES')
bm.to_mesh(me); bm.free(); brow = link(bpy.data.objects.new("brow", me)); brow.scale=(1.003,)*3; brow.hide_render=True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("fin"); src_geo = t.geo
def branch(L, out, lado, tras, grav):
    x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
    for kk,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": out, "Para o lado da risca": lado, "Para trás": tras, "Gravidade": grav}.items(): x.inputs[kk].default_value = v
    t.link(src_geo, x.inputs[0])
    rs0 = t.add('GeometryNodeResampleCurve'); rs0.inputs['Count'].default_value = 24; t.link(x.outputs['Guias'], rs0.inputs['Curve'])
    b = t.add('GeometryNodeGroup', group=GR["GR Balanço"]); b.inputs["Amplitude"].default_value = 0.12; t.link(rs0.outputs[0], b.inputs[0])
    w_ = t.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves']); w_.inputs['Offset Distance'].default_value = 0.004; w_.inputs['Above Surface'].default_value = 0.0; w_.inputs['Lock Roots'].default_value = True; t.link(b.outputs[0], w_.inputs['Geometry'])
    for q in w_.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
    d = t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]); d.inputs["Viewport"].default_value = 1.0; d.inputs["Fios por m2"].default_value = 260000.0; t.link(w_.outputs[0], d.inputs[0])
    rs = t.add('GeometryNodeResampleCurve'); rs.inputs['Count'].default_value = 24; t.link(d.outputs[0], rs.inputs['Curve'])
    return rs.outputs['Curve']
A = branch(0.32, 0.35, 0.6, 0.25, 2.2); B = branch(0.14, 0.5, 1.1, -0.9, 1.4)
mk = t.add('GeometryNodeGroup', group=GR["GR Máscara por Posição"])
for kk,v in {"Frente máx (Y)": -0.03, "Altura mín": 0.035, "Lateral máx (|X|)": 0.05, "Borda suave": 0.012}.items(): mk.inputs[kk].default_value = v
tr = t.add('GeometryNodeGroup', group=GR["GR Transição"]); t.link(A, tr.inputs[0]); t.link(B, tr.inputs[1]); t.link(mk.outputs[0], tr.inputs['Fator']); t.geo = tr.outputs[0]
m = t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]); m.inputs["Tamanho da mecha"].default_value = 0.014
ls_ = t.add('GeometryNodeGroup', group=GR["GR Lado da Risca"]); t.link(ls_.outputs[0], m.inputs["Group ID"]); t.chain(m, m.inputs[0].name, m.outputs[0].name)
for nm in ("GR Cor por Mecha",):
    n = t.add('GeometryNodeGroup', group=GR[nm]); t.chain(n, n.inputs[0].name, n.outputs[0].name)
profile(t, EG, radius=0.0005)
hm = MAT["GR Cabelo Cor por Mecha"].copy()
for n in hm.node_tree.nodes:
    if n.bl_idname == 'ShaderNodeBsdfHairPrincipled': n.inputs['Melanin Redness'].default_value = 0.95
set_mat(t, hm); apply_tree(g, t.finish())
bm_ = hair_mat("pelo", melanin=0.75, redness=0.9, roughness=0.35)
cb = bpy.data.hair_curves.new("sob"); gb = link(bpy.data.objects.new("sobrancelha", cb)); cb.surface = brow; cb.surface_uv_map = "UVMap"
tb = Tree("sob"); x = tb.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
for kk,v in {"Cabeça (colisão)": head, "Comprimento": 0.014, "Para fora": 0.25, "Para o lado da risca": 1.2, "Para trás": 0.0, "Gravidade": -0.4, "Guias por m2": 700000.0}.items(): x.inputs[kk].default_value = v
tb.chain(x, 'Geometry', 'Guias'); tb.eg(EG['Clump Hair Curves'], Factor=0.9, Shape=0.25, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.004, Existing_Guide_Map=False, Seed=1)
profile(tb, EG, radius=0.00035); set_mat(tb, bm_); apply_tree(gb, tb.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
sc = bpy.context.scene; sc.render.fps = 24; sc.frame_start = 1; sc.frame_end = 24
if sys.argv[-1] == "still":
    sc.frame_set(1); shot("114_final", res=900, samples=48, cam_loc=(0.26,-0.56,0.04), target=(0,-0.02,-0.05), lens=46)
else:
    stage(res=360, samples=10, cam_loc=(0.26,-0.56,0.04), target=(0,-0.02,-0.05), lens=46)
    fr=[]
    for f in range(1,25,2):
        sc.frame_set(f); p=os.path.join(OUT, f"114_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); fr.append(p)
    from PIL import Image
    ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in fr]
    ims[0].save(os.path.join(OUT,"114_final.gif"), save_all=True, append_images=ims[1:], duration=83, loop=0); print("GIF ok")
