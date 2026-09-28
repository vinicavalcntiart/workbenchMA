import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]   # sem | leve | forte | curto
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
    dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
GR = {n.name:n for n in bpy.data.node_groups}
head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("wh")
x = t.add('GeometryNodeGroup', group=GR["GR Guias Procedurais"])
L = 0.07 if V=="curto" else 0.16
for k,v in {"Cabeça (colisão)": head, "Comprimento": L, "Para fora": 0.3, "Para o lado da risca": 0.0, "Para trás": 0.4, "Gravidade": 0.8, "Guias por m2": 5000.0}.items(): x.inputs[k].default_value = v
t.chain(x, 'Geometry', 'Guias')
if V != "sem":
    # redemoinho: gira cada ponto em volta do eixo (centro -> coroa) com angulo = forca * t * falloff(dist raiz-coroa)
    C = Vector((0.0, 0.035, 0.094)).normalized()*0.1
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    di = t.add('ShaderNodeVectorMath', props={'operation':'DISTANCE'}); t.link(cr.outputs['Root Position'], di.inputs[0]); di.inputs[1].default_value = C
    fo = t.add('ShaderNodeMapRange'); fo.clamp = True; t.link(di.outputs['Value'], fo.inputs['Value']); fo.inputs['From Min'].default_value = 0.0; fo.inputs['From Max'].default_value = 0.07; fo.inputs['To Min'].default_value = 1.0; fo.inputs['To Max'].default_value = 0.0
    sp = t.add('GeometryNodeSplineParameter')
    an = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], an.inputs[0]); t.link(fo.outputs['Result'], an.inputs[1])
    an2 = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(an.outputs[0], an2.inputs[0]); an2.inputs[1].default_value = {"leve":1.5,"forte":3.5,"curto":3.5}[V]
    ps = t.add('GeometryNodeInputPosition')
    vr = t.add('ShaderNodeVectorRotate', props={'rotation_type':'AXIS_ANGLE'}); t.link(ps.outputs[0], vr.inputs['Vector']); vr.inputs['Center'].default_value = C; vr.inputs['Axis'].default_value = C.normalized(); t.link(an2.outputs[0], vr.inputs['Angle'])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(vr.outputs[0], s.inputs['Position'])
    w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
    for q in w.inputs:
        if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
for n in ("GR Densidade Livre","GR Mecha Estilizada","GR Cor por Mecha"):
    nd = t.add('GeometryNodeGroup', group=GR[n]); t.chain(nd, nd.inputs[0].name, nd.outputs[0].name)
    if n=="GR Densidade Livre": nd.inputs["Viewport"].default_value = 1.0
    if n=="GR Mecha Estilizada": nd.inputs["Tamanho da mecha"].default_value = 0.015
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("h", melanin=0.35, redness=0.8)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"54_{V}", res=420, samples=16, cam_loc=(0.10,0.25,0.50), target=(0,0.03,0.07), lens=45)
