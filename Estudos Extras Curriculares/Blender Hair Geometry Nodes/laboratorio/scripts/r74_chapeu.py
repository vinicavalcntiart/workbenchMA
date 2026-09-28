import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # sem | chapeu
LIB = os.path.join(LAB, "receitas_grooming.blend")
EG, head, scalp, g = base_scene(length=0.24, gravity=4.0, spread=0.3, outward=0.35, n_guides=220)
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
# chapeu: copa (cilindro) + aba (disco)
bpy.ops.mesh.primitive_cylinder_add(radius=0.108, depth=0.10, location=(0,0.0,0.08)); crown = bpy.context.object
bpy.ops.mesh.primitive_cylinder_add(radius=0.19, depth=0.006, location=(0,0,0.035)); brim = bpy.context.object
hat = crown
hm_ = bpy.data.materials.new("chapeu"); hm_.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.15,0.25,0.12,1); hat.data.materials.append(hm_); brim.data.materials.append(hm_)
t = Tree("ch")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 250000.0}); grp("GR Mecha Estilizada")
if V == "chapeu":
    oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = hat
    ps = t.add('GeometryNodeInputPosition')
    rc = t.add('GeometryNodeRaycast'); t.link(oi.outputs['Geometry'], rc.inputs['Target Geometry']); t.link(ps.outputs[0], rc.inputs['Source Position']); rc.inputs['Ray Direction'].default_value = (0,0,1); rc.inputs['Ray Length'].default_value = 1.0
    # sob o chapeu = raio para cima bate no chapeu; vira fator do Shrinkwrap na cabeca (cola no cranio)
    w = t.add('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves']); w.inputs['Offset Distance'].default_value = 0.003; w.inputs['Above Surface'].default_value = 1.0; w.inputs['Smoothing Steps'].default_value = 2; w.inputs['Lock Roots'].default_value = True
    for q in w.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
    ob = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); ob.inputs['Object'].default_value = brim
    rd = t.add('GeometryNodeRaycast'); t.link(ob.outputs['Geometry'], rd.inputs['Target Geometry']); t.link(ps.outputs[0], rd.inputs['Source Position']); rd.inputs['Ray Direction'].default_value = (0,0,-1); rd.inputs['Ray Length'].default_value = 1.0
    orr = t.add('FunctionNodeBooleanMath', props={'operation':'OR'}); t.link(rc.outputs['Is Hit'], orr.inputs[0]); t.link(rd.outputs['Is Hit'], orr.inputs[1])
    t.chain(w); t.link(orr.outputs[0], w.inputs['Factor'])
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.55, redness=0.6)); apply_tree(g, t.finish())
if V == "sem": hat.hide_render = False
print("INFO", V, stats(g).get('curves'))
shot(f"74_{V}", res=440, samples=16, cam_loc=(0.50,-0.62,0.05), target=(0,0,-0.03), lens=42)
