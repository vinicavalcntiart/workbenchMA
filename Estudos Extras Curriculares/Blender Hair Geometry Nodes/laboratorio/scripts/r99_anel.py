import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
V = sys.argv[-1]   # toon | anel
LIB = os.path.join(LAB, "receitas_grooming.blend")
reset(); EG = essentials()
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
GR = {n.name:n for n in bpy.data.node_groups}; MAT = {m.name:m for m in bpy.data.materials}
head, scalp = make_head(nape=-0.7)
def toon(name, col, size=0.6):
    m = bpy.data.materials.new(name); nt = m.node_tree; nt.nodes.clear(); o = nt.nodes.new('ShaderNodeOutputMaterial')
    d = nt.nodes.new('ShaderNodeBsdfToon'); d.component='DIFFUSE'; d.inputs['Color'].default_value=(*col,1); d.inputs['Size'].default_value=size; d.inputs['Smooth'].default_value=0.03
    nt.links.new(d.outputs[0], o.inputs['Surface']); return m
head.data.materials.append(toon("pele", (0.95,0.72,0.58), 0.7))
sm_ = toon("sc", (0.35,0.12,0.25)); scalp.data.materials.append(sm_)
pm = bpy.data.meshes.new("proxy"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=0.13); bmesh.ops.translate(bm, vec=(0,0.015,-0.02), verts=bm.verts); bm.to_mesh(pm); bm.free()
for p_ in pm.polygons: p_.use_smooth = True
proxy = link(bpy.data.objects.new("proxy", pm)); proxy.hide_render = True
cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
t = Tree("an")
def grp(name, **kw):
    n = t.add('GeometryNodeGroup', group=GR[name])
    for k,v in kw.items(): n.inputs[k].default_value = v
    return t.chain(n, n.inputs[0].name, n.outputs[0].name)
grp("GR Guias Procedurais", **{"Cabeça (colisão)": head, "Comprimento": 0.30, "Para fora": 0.5, "Para o lado da risca": 0.4, "Para trás": 0.3, "Gravidade": 1.6})
grp("GR Densidade Livre", **{"Viewport": 1.0, "Fios por m2": 200000.0})
grp("GR Mecha Estilizada", **{"Tamanho da mecha": 0.022})
grp("GR Normal da Malha", **{"Malha": proxy})
profile(t, EG, radius=0.0007, shape=0.2)
m = MAT["GR Cabelo Cel"].copy()
nt = m.node_tree
d = [n for n in nt.nodes if n.bl_idname=='ShaderNodeBsdfToon' and n.component=='DIFFUSE'][0]; d.inputs['Color'].default_value = (0.55,0.08,0.35,1)
gl = [n for n in nt.nodes if n.bl_idname=='ShaderNodeBsdfToon' and n.component=='GLOSSY'][0]
if V == "anel":
    # anel de brilho: faixa no Intercept (altura do fio) independente da luz, somado como emissao
    tc = nt.nodes.new('ShaderNodeTexCoord'); sz = nt.nodes.new('ShaderNodeSeparateXYZ'); nt.links.new(tc.outputs['Object'], sz.inputs[0])
    # faixa em Z (metros do objeto) acompanhando a curva do cranio: z + 0,35*(x^2+y^2)/R
    x2 = nt.nodes.new('ShaderNodeVectorMath'); x2.operation='DOT_PRODUCT'; nt.links.new(tc.outputs['Object'], x2.inputs[0]); nt.links.new(tc.outputs['Object'], x2.inputs[1])
    zz = nt.nodes.new('ShaderNodeMath'); zz.operation='MULTIPLY_ADD'; nt.links.new(x2.outputs['Value'], zz.inputs[0]); zz.inputs[1].default_value = 3.0; nt.links.new(sz.outputs['Z'], zz.inputs[2])
    rp = nt.nodes.new('ShaderNodeValToRGB'); r = rp.color_ramp; r.interpolation = 'CONSTANT'
    r.elements[0].position = 0.0; r.elements[0].color = (0,0,0,1); r.elements[1].position = 0.52; r.elements[1].color = (1,1,1,1)
    e3 = r.elements.new(0.57); e3.color = (0,0,0,1)
    mr_ = nt.nodes.new('ShaderNodeMapRange'); mr_.inputs['From Min'].default_value = -0.1; mr_.inputs['From Max'].default_value = 0.2; nt.links.new(zz.outputs[0], mr_.inputs['Value'])
    nt.links.new(mr_.outputs['Result'], rp.inputs['Fac'])
    em = nt.nodes.new('ShaderNodeEmission'); em.inputs['Color'].default_value = (1.0,0.6,0.85,1); em.inputs['Strength'].default_value = 0.8
    nt.links.new(rp.outputs['Color'], em.inputs['Strength'])
    mix = nt.nodes.new('ShaderNodeAddShader'); out = [n for n in nt.nodes if n.bl_idname=='ShaderNodeOutputMaterial'][0]
    prev = out.inputs['Surface'].links[0].from_socket
    nt.links.new(prev, mix.inputs[0]); nt.links.new(em.outputs[0], mix.inputs[1]); nt.links.new(mix.outputs[0], out.inputs['Surface'])
    gl.inputs['Color'].default_value = (0.2,0.05,0.12,1)
set_mat(t, m); apply_tree(g, t.finish())
import lab as _l
_o = _l.render
def _r(p, **kw):
    wn = bpy.context.scene.world.node_tree; bgn = wn.nodes['Background']; bgn.inputs[0].default_value=(0.08,0.08,0.09,1)
    if 'cf' not in wn.nodes:
        b2 = wn.nodes.new('ShaderNodeBackground'); b2.name='cf'; b2.inputs[0].default_value=(0.86,0.88,0.92,1)
        lp = wn.nodes.new('ShaderNodeLightPath'); mx = wn.nodes.new('ShaderNodeMixShader')
        wn.links.new(lp.outputs['Is Camera Ray'], mx.inputs[0]); wn.links.new(bgn.outputs[0], mx.inputs[1]); wn.links.new(b2.outputs[0], mx.inputs[2]); wn.links.new(mx.outputs[0], wn.nodes['World Output'].inputs['Surface'])
    return _o(p, **kw)
_l.render = _r
shot(f"99_{V}", res=440, samples=24, cam_loc=(0.40,-0.62,0.06), target=(0,0,-0.08), lens=42)
