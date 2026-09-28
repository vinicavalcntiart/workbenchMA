import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
t = Tree("multidao")
# semente pela posicao do proprio objeto
so = t.add('GeometryNodeSelfObject'); oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'ORIGINAL'}); t.link(so.outputs[0], oi.inputs['Object'])
hv = t.add('FunctionNodeHashValue'); hv.data_type = 'VECTOR'; t.link(oi.outputs['Location'], hv.inputs['Value'])
seed = hv.outputs[0]
def rnd(lo, hi, k):
    r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=lo, Max=hi); t.link(seed, r.inputs['ID']); r.inputs['Seed'].default_value = k; return r.outputs['Value']
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for kk,v in kw.items():
        if isinstance(v, bpy.types.NodeSocket): t.link(v, n.inputs[kk])
        else: n.inputs[kk].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Densidade Livre", **{"Fios por m2": 200000.0, "Viewport": 1.0, "Seed": seed})
grp("GR Mecha Estilizada", **{"Seed": seed, "Tamanho da mecha": rnd(0.012, 0.028, 1)})
vmin = rnd(4.0, 40.0, 2); vmax = t.add('ShaderNodeMath', props={'operation':'ADD'}); t.link(vmin, vmax.inputs[0]); vmax.inputs[1].default_value = 8.0
grp("GR Cacho por Mecha", **{"Seed": seed, "Voltas por metro mín": vmin, "Voltas por metro máx": vmax.outputs[0], "Começa em": 0.3})
tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=False); t.link(rnd(0.55, 1.05, 3), tr.inputs['Length Factor'])
grp("GR Cor por Mecha", **{"Seed": seed})
st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); st.inputs['Name'].default_value='obj_rand'; t.chain(st); t.link(rnd(0.0, 1.0, 4), st.inputs['Value'])
profile(t, EG, radius=0.0005)
m = bpy.data.materials.new("h"); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial')
h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization='MELANIN'; h.inputs['Roughness'].default_value = 0.3
a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name='obj_rand'; b = nt.nodes.new('ShaderNodeAttribute'); b.attribute_name='mecha_rand'
m1 = nt.nodes.new('ShaderNodeMapRange'); m1.inputs['To Min'].default_value=0.08; m1.inputs['To Max'].default_value=0.95; nt.links.new(a.outputs['Fac'], m1.inputs['Value'])
m2 = nt.nodes.new('ShaderNodeMath'); m2.operation='MULTIPLY_ADD'; nt.links.new(b.outputs['Fac'], m2.inputs[0]); m2.inputs[1].default_value=0.12; nt.links.new(m1.outputs['Result'], m2.inputs[2])
nt.links.new(m2.outputs[0], h.inputs['Melanin'])
rr = nt.nodes.new('ShaderNodeMapRange'); rr.inputs['To Min'].default_value=0.2; rr.inputs['To Max'].default_value=1.0; nt.links.new(a.outputs['Fac'], rr.inputs['Value']); nt.links.new(rr.outputs['Result'], h.inputs['Melanin Redness'])
nt.links.new(h.outputs[0], o.inputs['Surface'])
set_mat(t, m); ng = t.finish(); apply_tree(g, ng)
col = bpy.data.collections.new("personagem")
for o_ in (head, scalp, g):
    for c_ in list(o_.users_collection): c_.objects.unlink(o_)
    col.objects.link(o_)
bpy.context.scene.collection.children.link(col); bpy.context.view_layer.layer_collection.children[col.name].exclude = True
for i in range(4):
    inst = bpy.data.objects.new(f"inst{i}", None); inst.instance_type = 'COLLECTION'; inst.instance_collection = col; inst.location = (i*0.34 - 0.51, 0, 0); link(inst)
bpy.context.view_layer.update()
shot("110_instancias", res=900, samples=20, cam_loc=(0.0,-1.55,0.12), target=(0,0,-0.08), lens=42)
