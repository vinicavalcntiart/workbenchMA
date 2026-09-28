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
def grp(n, out='Geometry', **kw):
    x = t.add('GeometryNodeGroup', group=GR[n])
    for k,v in kw.items(): x.inputs[k].default_value = v
    return t.chain(x, 'Geometry', out)
TURNS=2.2; RMIN=0.004; RMAX=0.03; ROPE=0.006; LB='coque corda: 2.2 voltas, corda 6mm'
# 3) coque: cauda em espiral ao redor do eixo do elastico
EG, GR, M, head, g = base(); t = Tree("bun")
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head}); grp("GR Densidade Livre", Viewport=1.0)
tie = (0.0, 0.07, 0.085)
grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Amarração":tie, "Até a amarração":0.45, "Comprimento da cauda":0.0, "Abertura":0.0})
sp = t.add('GeometryNodeSplineParameter')
b = t.add('ShaderNodeMapRange', From_Min=0.45, From_Max=1.0); b.clamp=True; t.link(sp.outputs['Factor'], b.inputs['Value'])
ph = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=2*math.pi, Seed=4)
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(ph.outputs['Value'], ev.inputs[0])
ang = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], ang.inputs[0]); ang.inputs[1].default_value = 2*math.pi*TURNS
co = t.add('ShaderNodeMath', props={'operation':'COSINE'}); t.link(ang.outputs[0], co.inputs[0]); si = t.add('ShaderNodeMath', props={'operation':'SINE'}); t.link(ang.outputs[0], si.inputs[0])
rr = t.add('ShaderNodeMapRange', To_Min=RMIN, To_Max=RMAX); t.link(b.outputs['Result'], rr.inputs['Value'])
rm = rr
xx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(co.outputs[0], xx.inputs[0]); t.link(rm.outputs['Result'], xx.inputs[1])
yy = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(si.outputs[0], yy.inputs[0]); t.link(rm.outputs['Result'], yy.inputs[1])
zz = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], zz.inputs[0]); zz.inputs[1].default_value = 0.018
# espiral no plano perpendicular a normal do cranio no tie (aprox. eixo = tie normalizado)
axis = Vector(tie).normalized(); u = axis.cross(Vector((1,0,0))).normalized(); v = axis.cross(u)
def vec(sock_scalar, vv):
    s = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); s.inputs[0].default_value = tuple(vv); t.link(sock_scalar, s.inputs['Scale']); return s.outputs[0]
a1 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(vec(xx.outputs[0], u), a1.inputs[0]); t.link(vec(yy.outputs[0], v), a1.inputs[1])
a2 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a1.outputs[0], a2.inputs[0]); t.link(vec(zz.outputs[0], axis), a2.inputs[1])
# espessura da corda: offset aleatorio por fio, pequeno, crescendo depois do tie
rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT_VECTOR'}, Min=(-1,-1,-1), Max=(1,1,1), Seed=6)
evv = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT_VECTOR'}); t.link(rv.outputs['Value'], evv.inputs[0])
bb = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], bb.inputs[0]); bb.inputs[1].default_value = ROPE
rope = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(evv.outputs[0], rope.inputs[0]); t.link(bb.outputs[0], rope.inputs['Scale'])
a3 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a2.outputs[0], a3.inputs[0]); t.link(rope.outputs[0], a3.inputs[1])
spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(a3.outputs[0], spn.inputs['Offset'])
grp("GR Mecha Estilizada", **{"Tamanho da mecha":0.01}); grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm); apply_tree(g, t.finish())
paths.append(shot("35b_"+str(len(paths)), res=420, samples=16, cam_loc=(-0.45,0.45,0.25), target=(0,0.03,0.03), lens=45)); labels.append(LB)
TURNS=3.0; RMIN=0.003; RMAX=0.022; ROPE=0.008; LB='coque apertado: 3 voltas, corda 8mm'
# 3) coque: cauda em espiral ao redor do eixo do elastico
EG, GR, M, head, g = base(); t = Tree("bun")
grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head}); grp("GR Densidade Livre", Viewport=1.0)
tie = (0.0, 0.07, 0.085)
grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Amarração":tie, "Até a amarração":0.45, "Comprimento da cauda":0.0, "Abertura":0.0})
sp = t.add('GeometryNodeSplineParameter')
b = t.add('ShaderNodeMapRange', From_Min=0.45, From_Max=1.0); b.clamp=True; t.link(sp.outputs['Factor'], b.inputs['Value'])
ph = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=2*math.pi, Seed=4)
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(ph.outputs['Value'], ev.inputs[0])
ang = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], ang.inputs[0]); ang.inputs[1].default_value = 2*math.pi*TURNS
co = t.add('ShaderNodeMath', props={'operation':'COSINE'}); t.link(ang.outputs[0], co.inputs[0]); si = t.add('ShaderNodeMath', props={'operation':'SINE'}); t.link(ang.outputs[0], si.inputs[0])
rr = t.add('ShaderNodeMapRange', To_Min=RMIN, To_Max=RMAX); t.link(b.outputs['Result'], rr.inputs['Value'])
rm = rr
xx = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(co.outputs[0], xx.inputs[0]); t.link(rm.outputs['Result'], xx.inputs[1])
yy = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(si.outputs[0], yy.inputs[0]); t.link(rm.outputs['Result'], yy.inputs[1])
zz = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], zz.inputs[0]); zz.inputs[1].default_value = 0.018
# espiral no plano perpendicular a normal do cranio no tie (aprox. eixo = tie normalizado)
axis = Vector(tie).normalized(); u = axis.cross(Vector((1,0,0))).normalized(); v = axis.cross(u)
def vec(sock_scalar, vv):
    s = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); s.inputs[0].default_value = tuple(vv); t.link(sock_scalar, s.inputs['Scale']); return s.outputs[0]
a1 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(vec(xx.outputs[0], u), a1.inputs[0]); t.link(vec(yy.outputs[0], v), a1.inputs[1])
a2 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a1.outputs[0], a2.inputs[0]); t.link(vec(zz.outputs[0], axis), a2.inputs[1])
# espessura da corda: offset aleatorio por fio, pequeno, crescendo depois do tie
rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT_VECTOR'}, Min=(-1,-1,-1), Max=(1,1,1), Seed=6)
evv = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT_VECTOR'}); t.link(rv.outputs['Value'], evv.inputs[0])
bb = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(b.outputs['Result'], bb.inputs[0]); bb.inputs[1].default_value = ROPE
rope = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(evv.outputs[0], rope.inputs[0]); t.link(bb.outputs[0], rope.inputs['Scale'])
a3 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a2.outputs[0], a3.inputs[0]); t.link(rope.outputs[0], a3.inputs[1])
spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(a3.outputs[0], spn.inputs['Offset'])
grp("GR Mecha Estilizada", **{"Tamanho da mecha":0.01}); grp("GR Cor por Mecha")
pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = M["GR Cabelo Cor por Mecha"]; t.chain(sm); apply_tree(g, t.finish())
paths.append(shot("35b_"+str(len(paths)), res=420, samples=16, cam_loc=(-0.45,0.45,0.25), target=(0,0.03,0.03), lens=45)); labels.append(LB)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"35b_bun_sheet.png"), cols=2))
