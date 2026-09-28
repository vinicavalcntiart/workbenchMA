import sys; sys.path.insert(0,'.')
from lab import *
OUTF = sys.argv[-1]
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(nape=-0.7); head.name = "Cabeca"; scalp.name = "HairCap"; head.data.materials.append(skin_mat())
sm_ = bpy.data.materials.new("HairCap cor da raiz"); sm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.08,0.035,0.015,1); scalp.data.materials.append(sm_)
scalp.add_rest_position_attribute = True
cd = bpy.data.hair_curves.new("Cabelo"); g = link(bpy.data.objects.new("Cabelo", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("Groom inicial")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    t.chain(n, n.inputs[0].name, n.outputs[0].name); return n
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head})
grp("GR Densidade Livre")
grp("GR Mecha Estilizada")
grp("GR Cor por Mecha")
t.chain(t.add('GeometryNodeDeformCurvesOnSurface'), 'Curves', 'Curves')
profile(t, EG, radius=0.0005)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = MAT["GR Cabelo Cor por Mecha"]; t.chain(sm)
for i,n in enumerate(t.ng.nodes): n.location = (i*220, 0) if n.bl_idname != 'NodeGroupOutput' else n.location
apply_tree(g, t.finish())
stage(res=1080, samples=48, cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.04), lens=48)
bpy.context.scene.render.resolution_y = 1080
print("INFO", stats(g).get('curves'))
from lab import localize; localize()
bpy.ops.wm.save_as_mainfile(filepath=OUTF, compress=True); print("SALVO", OUTF)
