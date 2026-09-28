import sys; sys.path.insert(0,'.')
exec(open('r31_procguides.py').read().split("def build(")[0])
BACK = dict(cam_loc=(-0.45,0.55,0.0), target=(0,0.05,-0.08), lens=42)
def build(t, EG, head, tie=(0,0.105,0.03), tfrac=0.35, L=0.40, spread=0.012, grav_drop=1.0, clump=True):
    GR = bpy.data.node_groups
    gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves'])
    t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, 300000.0), gen.inputs['Density'])
    gen.inputs['Hair Length'].default_value = L; gen.inputs['Control Points'].default_value = 24
    gen.inputs['Distribution Method'].default_value = 'Poisson Disk'; t.geo = gen.outputs['Geometry']
    sp = t.add('GeometryNodeSplineParameter'); root = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    # a = t/tfrac (0..1 ate a amarracao), b = (t - tfrac)/(1-tfrac) (0..1 depois)
    a = t.add('ShaderNodeMapRange', From_Min=0.0, From_Max=tfrac); a.clamp=True; t.link(sp.outputs['Factor'], a.inputs['Value'])
    b = t.add('ShaderNodeMapRange', From_Min=tfrac, From_Max=1.0); b.clamp=True; t.link(sp.outputs['Factor'], b.inputs['Value'])
    # ate a amarracao: lerp(raiz, tie, a) com leve arco para fora
    lerp = t.add('ShaderNodeMix', props={'data_type':'VECTOR'}); t.link(a.outputs['Result'], lerp.inputs['Factor'])
    t.link(root.outputs['Root Position'], lerp.inputs[4]); lerp.inputs[5].default_value = tie
    # depois: cai a partir do tie, espalhando um pouco em volta (offset por fio, ao redor)
    r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT_VECTOR'}, Min=(-1,-1,0), Max=(1,1,0), Seed=3)
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT_VECTOR'}); t.link(r.outputs['Value'], ev.inputs[0])
    sprd = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); sprd.inputs['Scale'].default_value = spread; t.link(ev.outputs[0], sprd.inputs[0])
    fall_len = (1-tfrac)*L
    drop = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); drop.inputs[0].default_value = (0, 0.25, -grav_drop); t.link(b.outputs['Result'], drop.inputs['Scale'])
    dropL = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(drop.outputs[0], dropL.inputs[0]); dropL.inputs['Scale'].default_value = fall_len
    # espalhamento cresce depois do tie: spread * b
    sb = t.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t.link(sprd.outputs[0], sb.inputs[0]); t.link(b.outputs['Result'], sb.inputs['Scale'])
    tail = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(dropL.outputs[0], tail.inputs[0]); t.link(sb.outputs[0], tail.inputs[1])
    pos = t.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t.link(lerp.outputs[1], pos.inputs[0]); t.link(tail.outputs[0], pos.inputs[1])
    spn = t.add('GeometryNodeSetPosition'); t.chain(spn); t.link(pos.outputs[0], spn.inputs['Position'])
    w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
    for x in w.inputs:
        if x.name == 'Surface' and x.type == 'OBJECT': x.default_value = head
    if clump:
        t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.003, Preserve_Length=True, Guide_Distance=0.012, Existing_Guide_Map=False, Seed=2)
    # elastico: toro no tie
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("p", melanin=0.8, redness=0.5))
def tie_ring(tie):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.012, minor_radius=0.004, location=tie, rotation=(math.radians(70),0,0))
    m = bpy.data.materials.new("elastico"); m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.7,0.08,0.1,1); bpy.context.object.data.materials.append(m)
V=[("rabo baixo (nuca), sem clump", dict(tie=(0,0.105,-0.01), clump=False)),
   ("rabo baixo + clump", dict(tie=(0,0.105,-0.01))),
   ("rabo alto (topo de tras)", dict(tie=(0,0.085,0.07), tfrac=0.3))]
paths=[]; labels=[]
for lb, kw in V:
    EG, head, scalp, g = scene(); t = Tree("pony"); build(t, EG, head, **kw); apply_tree(g, t.finish()); tie_ring(kw.get('tie'))
    print("INFO", lb, stats(g).get('curves'))
    paths.append(shot("33_"+str(len(paths)), res=420, samples=16, **BACK)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"33_pony_sheet.png"), cols=3))
