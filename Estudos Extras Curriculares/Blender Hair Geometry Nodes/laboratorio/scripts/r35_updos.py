import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
def base():
    reset(); EG = essentials()
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    GR = {n.name:n for n in bpy.data.node_groups}; M = {m.name:m for m in bpy.data.materials}
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
    return EG, GR, M, head, g
def ring(loc, rot=(70,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.013, minor_radius=0.0045, location=loc, rotation=tuple(math.radians(a) for a in rot))
    em = bpy.data.materials.new("el"); em.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.75,0.1,0.12,1); bpy.context.object.data.materials.append(em)
paths=[]; labels=[]
# 1) maria-chiquinha: amarracao com X espelhado pelo lado da raiz -> precisa de campo no socket Amarracao
EG, GR, M, head, g = base(); t = Tree("pig")
def grp(n, out='Geometry', **kw):
    x = t.add('GeometryNodeGroup', group=GR[n])
    for k,v in kw.items(): x.inputs[k].default_value = v
    return t.chain(x, 'Geometry', out)
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head}); grp("GR Densidade Livre", Viewport=1.0)
rb = grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Até a amarração":0.3, "Comprimento da cauda":0.2, "Abertura":0.025})
root = t.add('GeometryNodeGroup', group=EG['Curve Root']); sx = t.add('ShaderNodeSeparateXYZ'); t.link(root.outputs['Root Position'], sx.inputs[0])
sg = t.add('ShaderNodeMath', props={'operation':'SIGN'}); t.link(sx.outputs['X'], sg.inputs[0])
mx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sg.outputs[0], mx.inputs[0]); mx.inputs[1].default_value = 0.085
tv = t.add('ShaderNodeCombineXYZ'); t.link(mx.outputs[0], tv.inputs['X']); tv.inputs['Y'].default_value = 0.035; tv.inputs['Z'].default_value = 0.03
t.link(tv.outputs[0], rb.inputs['Amarração'])
grp("GR Mecha Estilizada", **{"Tamanho da mecha":0.012}); grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm); apply_tree(g, t.finish())
ring((0.085,0.035,0.03),(0,90,0)); ring((-0.085,0.035,0.03),(0,90,0))
paths.append(shot("35_0", res=420, samples=16, cam_loc=(0.0,0.62,0.05), target=(0,0.02,-0.05), lens=40)); labels.append("maria-chiquinha: Amarracao X = sinal(raiz.x)*8.5cm")
# 2) rabo tranc,ado
EG, GR, M, head, g = base(); t = Tree("br")
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head}); grp("GR Densidade Livre", Viewport=1.0)
grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Abertura":0.015})
grp("GR Trança Grossa", Raio=0.014, **{"Começa em":0.4, "Cruzamentos":1.2})
grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm); apply_tree(g, t.finish())
ring((0,0.105,-0.01))
paths.append(shot("35_1", res=420, samples=16, cam_loc=(-0.5,0.5,0.0), target=(0,0.05,-0.1), lens=40)); labels.append("rabo + GR Tranca Grossa (Comeca em .4)")
# 3) coque: cauda em espiral ao redor do eixo do elastico
EG, GR, M, head, g = base(); t = Tree("bun")
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head}); grp("GR Densidade Livre", Viewport=1.0)
tie = (0.0, 0.07, 0.085)
grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Amarração":tie, "Até a amarração":0.45, "Comprimento da cauda":0.0, "Abertura":0.0})
sp = t.add('GeometryNodeSplineParameter')
b = t.add('ShaderNodeMapRange', From_Min=0.45, From_Max=1.0); b.clamp=True; t.link(sp.outputs['Factor'], b.inputs['Value'])
ph = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=2*math.pi, Seed=4)
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(ph.outputs['Value'], ev.inputs[0])
ang = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(b.outputs['Result'], ang.inputs[0]); ang.inputs[1].default_value = 2*math.pi*2.2; t.link(ev.outputs[0], ang.inputs[2])
co = t.add('ShaderNodeMath', props={'operation':'COSINE'}); t.link(ang.outputs[0], co.inputs[0]); si = t.add('ShaderNodeMath', props={'operation':'SINE'}); t.link(ang.outputs[0], si.inputs[0])
rr = t.add('ShaderNodeMapRange', To_Min=0.004, To_Max=0.03); t.link(b.outputs['Result'], rr.inputs['Value'])
rj = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.6, Max=1.2, Seed=5); evr = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(rj.outputs['Value'], evr.inputs[0])
rm = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(rr.outputs['Result'], rm.inputs[0]); t.link(evr.outputs[0], rm.inputs[1])
xx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(co.outputs[0], xx.inputs[0]); t.link(rm.outputs[0], xx.inputs[1])
yy = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(si.outputs[0], yy.inputs[0]); t.link(rm.outputs[0], yy.inputs[1])
zz = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], zz.inputs[0]); zz.inputs[1].default_value = 0.018
# espiral no plano perpendicular a normal do cranio no tie (aprox. eixo = tie normalizado)
axis = Vector(tie).normalized(); u = axis.cross(Vector((1,0,0))).normalized(); v = axis.cross(u)
def vec(sock_scalar, vv):
    s = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); s.inputs[0].default_value = tuple(vv); t.link(sock_scalar, s.inputs['Scale']); return s.outputs[0]
a1 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(vec(xx.outputs[0], u), a1.inputs[0]); t.link(vec(yy.outputs[0], v), a1.inputs[1])
a2 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a1.outputs[0], a2.inputs[0]); t.link(vec(zz.outputs[0], axis), a2.inputs[1])
spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(a2.outputs[0], spn.inputs['Offset'])
grp("GR Mecha Estilizada", **{"Tamanho da mecha":0.01}); grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm); apply_tree(g, t.finish())
paths.append(shot("35_2", res=420, samples=16, cam_loc=(-0.45,0.45,0.25), target=(0,0.03,0.03), lens=45)); labels.append("coque: espiral 2.2 voltas, raio 4mm->3cm")
print("SHEET", sheet(paths, labels, os.path.join(OUT,"35_updos_sheet.png"), cols=3))
