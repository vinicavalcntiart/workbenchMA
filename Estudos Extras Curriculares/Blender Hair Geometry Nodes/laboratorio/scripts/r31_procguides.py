import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
FR = dict(cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.06), lens=48)
def scene():
    reset(); EG = essentials()
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
    return EG, head, scalp, g
def build(t, EG, head, L=0.26, out=0.4, spread=0.35, back=0.2, grav=1.2, guides_density=4000.0, mode="curls"):
    gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves'])
    t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, guides_density), gen.inputs['Density'])
    gen.inputs['Hair Length'].default_value = L; gen.inputs['Control Points'].default_value = 12
    gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
    t.geo = gen.outputs['Geometry']
    # parabola: offset = (n*(out-1) + lado*spread + tras*back)*L*t - Z*grav*L*t^2
    sp = t.add('GeometryNodeSplineParameter')
    root = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    sx = t.add('ShaderNodeSeparateXYZ'); t.link(root.outputs['Root Position'], sx.inputs[0])
    sg = t.add('ShaderNodeMath', props={'operation':'SIGN'}); t.link(sx.outputs['X'], sg.inputs[0])
    side = t.add('ShaderNodeCombineXYZ'); t.link(sg.outputs[0], side.inputs['X'])
    n_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(gen.outputs['Surface Normal'], n_.inputs[0]); n_.inputs['Scale'].default_value = out-1.0
    s_ = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(side.outputs[0], s_.inputs[0]); s_.inputs['Scale'].default_value = spread
    a1 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(n_.outputs[0], a1.inputs[0]); t.link(s_.outputs[0], a1.inputs[1])
    a2 = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(a1.outputs[0], a2.inputs[0]); a2.inputs[1].default_value = (0, back, 0)
    lt = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], lt.inputs[0]); lt.inputs[1].default_value = L
    lin = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(a2.outputs[0], lin.inputs[0]); t.link(lt.outputs[0], lin.inputs['Scale'])
    t2 = t.add('ShaderNodeMath', props={'operation':'POWER'}); t.link(sp.outputs['Factor'], t2.inputs[0]); t2.inputs[1].default_value = 2.0
    gz = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(t2.outputs[0], gz.inputs[0]); gz.inputs[1].default_value = -grav*L
    gv = t.add('ShaderNodeCombineXYZ'); t.link(gz.outputs[0], gv.inputs['Z'])
    off = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(lin.outputs[0], off.inputs[0]); t.link(gv.outputs[0], off.inputs[1])
    spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(off.outputs[0], spn.inputs['Offset'])
    w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.006, Above_Surface=0.0, Smoothing_Steps=3, Lock_Roots=True)
    for x in w.inputs:
        if x.name == 'Surface' and x.type == 'OBJECT': x.default_value = head
    GR = bpy.data.node_groups
    d = t.add('GeometryNodeGroup', group=GR['GR Densidade Livre']); d.inputs['Viewport'].default_value = 1.0; t.chain(d)
    m = t.add('GeometryNodeGroup', group=GR['GR Mecha Estilizada']); t.chain(m)
    if mode == "curls":
        c = t.add('GeometryNodeGroup', group=GR['GR Cacho por Mecha']); t.chain(c)
    if mode == "wave":
        c = t.add('GeometryNodeGroup', group=GR['GR Onda S']); t.chain(c)
    cm = t.add('GeometryNodeGroup', group=GR['GR Cor por Mecha']); t.chain(cm)
    profile(t, EG, radius=0.0005)
    mat = hair_mat("h", melanin=0.5 if mode!="curls" else 0.3, redness=0.6 if mode!="curls" else 1.0)
    set_mat(t, mat)
V = [("bob liso: out .4 lado .35 grav 1.2 L 22cm", dict(L=0.22, mode="liso")),
     ("longo ondulado: L 34cm grav 2.2", dict(L=0.34, grav=2.2, spread=0.25, mode="wave")),
     ("volume cacheado: out .8 grav .5", dict(L=0.24, out=0.8, grav=0.5, spread=0.45, mode="curls")),
     ("espetado: out 1.2 grav 0 L 12cm", dict(L=0.12, out=1.2, grav=0.0, spread=0.1, back=0.1, mode="liso"))]
paths=[]; labels=[]
for lb, kw in V:
    EG, head, scalp, g = scene(); t = Tree("proc"); build(t, EG, head, **kw); apply_tree(g, t.finish())
    st = stats(g); print("INFO", lb, st.get('curves'))
    paths.append(shot("31_"+str(len(paths)), res=420, samples=16, **FR)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"31_procguides_sheet.png"), cols=4))
