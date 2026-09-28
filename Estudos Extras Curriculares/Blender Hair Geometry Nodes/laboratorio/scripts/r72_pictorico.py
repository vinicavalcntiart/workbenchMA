import sys; sys.path.insert(0,'.')
V = sys.argv[-1]   # fio | normal | pictorico
src = open('r62_criatura.py').read()
pre = src.split("cd = bpy.data.hair_curves.new")[0]
exec(pre)
cd = bpy.data.hair_curves.new("pelo"); g = link(bpy.data.objects.new("pelo", cd)); cd.surface = body; cd.surface_uv_map = "UVMap"
t = Tree("pic")
gen = t.add('GeometryNodeGroup', group=EG['Generate Hair Curves']); t.link(t.geo, gen.inputs['Hair Surface']); t.link(value(t, 90000.0), gen.inputs['Density'])
gen.inputs['Hair Length'].default_value = 0.04; gen.inputs['Control Points'].default_value = 8; gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
t.geo = gen.outputs['Geometry']
sn_ = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT_VECTOR','domain':'CURVE'}); sn_.inputs['Name'].default_value='nsurf'; t.chain(sn_); t.link(gen.outputs['Surface Normal'], sn_.inputs['Value'])
pc = t.add('GeometryNodeGroup', group=GR["GR Pentear por Curva"]); t.chain(pc); pc.inputs["Curva de fluxo"].default_value = flow; pc.inputs["Levanta"].default_value = 0.4
# clump grande + sub-clump
c1 = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=2)
na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}); na.inputs['Name'].default_value='guide_curve_index'
r1 = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); t.link(na.outputs['Attribute'], r1.inputs['ID'])
e1 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(r1.outputs['Value'], e1.inputs[0])
s1 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s1.inputs['Name'].default_value='clump_a'; t.chain(s1); t.link(e1.outputs[0], s1.inputs['Value'])
if V == "pictorico":   # buracos: apaga 12% dos clumps grandes
    rb = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); rb.inputs['Probability'].default_value = 0.12; rb.inputs['Seed'].default_value = 9; t.link(na.outputs['Attribute'], rb.inputs['ID'])
    dl = t.add('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); t.chain(dl); t.link([o for o in rb.outputs if o.type=='BOOLEAN'][0], dl.inputs['Selection'])
c2 = t.eg(EG['Clump Hair Curves'], Factor=0.8, Shape=0.3, Tip_Spread=0.0005, Preserve_Length=True, Guide_Distance=0.006, Existing_Guide_Map=False, Seed=5)
na2 = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}); na2.inputs['Name'].default_value='guide_curve_index'
r2 = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); r2.inputs['Seed'].default_value = 3; t.link(na2.outputs['Attribute'], r2.inputs['ID'])
e2 = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(r2.outputs['Value'], e2.inputs[0])
s2 = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); s2.inputs['Name'].default_value='clump_b'; t.chain(s2); t.link(e2.outputs[0], s2.inputs['Value'])
profile(t, EG, radius=0.0005 if V!="fio" else 0.0004)
main = t.geo
if V == "pictorico":   # pelos de guarda: 1,5% dos fios, 1,5x mais longos, grossos
    cr_ = t.add('GeometryNodeGroup', group=EG['Curve Info']) if 'Curve Info' in EG else None
    rg = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); rg.inputs['Probability'].default_value = 0.985; rg.inputs['Seed'].default_value = 11
    ix = t.add('GeometryNodeInputIndex'); t.link(ix.outputs[0], rg.inputs['ID'])
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'BOOLEAN'}); t.link([o for o in rg.outputs if o.type=='BOOLEAN'][0], ev.inputs[0])
    dg_ = t.add('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); t.link(main, dg_.inputs['Geometry']); t.link(ev.outputs[0], dg_.inputs['Selection'])
    tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); tr.inputs['Replace Length'].default_value = False; tr.inputs['Length Factor'].default_value = 1.5; t.link(dg_.outputs[0], tr.inputs['Geometry'])
    pr = t.add('GeometryNodeGroup', group=EG['Set Hair Curve Profile']); pr.inputs['Radius'].default_value = 0.0012; pr.inputs['Shape'].default_value = 0.6; pr.inputs['Factor Min'].default_value = 0.0; pr.inputs['Factor Max'].default_value = 1.0; t.link(tr.outputs[0], pr.inputs['Geometry'])
    sg = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'}); sg.inputs['Name'].default_value='guarda'; sg.inputs['Value'].default_value = 1.0; t.link(pr.outputs[0], sg.inputs['Geometry'])
    j = t.add('GeometryNodeJoinGeometry'); t.link(main, j.inputs[0]); t.link(sg.outputs[0], j.inputs[0]); t.geo = j.outputs[0]
# material
m = bpy.data.materials.new("pic"); nt = m.node_tree; nt.nodes.clear(); out = nt.nodes.new('ShaderNodeOutputMaterial')
a1 = nt.nodes.new('ShaderNodeAttribute'); a1.attribute_name='clump_a'; a2 = nt.nodes.new('ShaderNodeAttribute'); a2.attribute_name='clump_b'
if V == "fio":
    h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization='MELANIN'; h.inputs['Melanin Redness'].default_value = 1.0; h.inputs['Roughness'].default_value = 0.35
    mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 0.3; mr.inputs['To Max'].default_value = 0.55; nt.links.new(a1.outputs['Fac'], mr.inputs['Value']); nt.links.new(mr.outputs['Result'], h.inputs['Melanin'])
    nt.links.new(h.outputs[0], out.inputs['Surface'])
else:
    # cor: matiz por clump grande (laranja -> ocre), valor por sub-clump
    ramp = nt.nodes.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].color = (0.55,0.22,0.06,1); ramp.color_ramp.elements[1].color = (0.85,0.55,0.22,1)
    nt.links.new(a1.outputs['Fac'], ramp.inputs['Fac'])
    vm = nt.nodes.new('ShaderNodeMapRange'); vm.inputs['To Min'].default_value = 0.75; vm.inputs['To Max'].default_value = 1.15; nt.links.new(a2.outputs['Fac'], vm.inputs['Value'])
    mul = nt.nodes.new('ShaderNodeMix'); mul.data_type='RGBA'; mul.blend_type='MULTIPLY'; mul.inputs[0].default_value = 1.0; nt.links.new(ramp.outputs['Color'], mul.inputs[6])
    cv = nt.nodes.new('ShaderNodeCombineColor'); nt.links.new(vm.outputs['Result'], cv.inputs[0]); nt.links.new(vm.outputs['Result'], cv.inputs[1]); nt.links.new(vm.outputs['Result'], cv.inputs[2]); nt.links.new(cv.outputs[0], mul.inputs[7])
    col = mul.outputs[2]
    if V == "pictorico":   # guarda escura como linha de acento
        ag = nt.nodes.new('ShaderNodeAttribute'); ag.attribute_name='guarda'
        mg = nt.nodes.new('ShaderNodeMix'); mg.data_type='RGBA'; nt.links.new(ag.outputs['Fac'], mg.inputs[0]); nt.links.new(col, mg.inputs[6]); mg.inputs[7].default_value = (0.12,0.05,0.02,1); col = mg.outputs[2]
    d = nt.nodes.new('ShaderNodeBsdfToon'); d.component='DIFFUSE'; d.inputs['Size'].default_value = 0.55; d.inputs['Smooth'].default_value = 0.25
    nt.links.new(col, d.inputs['Color'])
    an = nt.nodes.new('ShaderNodeAttribute'); an.attribute_name='nsurf'
    vt = nt.nodes.new('ShaderNodeVectorTransform'); vt.vector_type='NORMAL'; vt.convert_from='OBJECT'; vt.convert_to='WORLD'; nt.links.new(an.outputs['Vector'], vt.inputs[0])
    nt.links.new(vt.outputs[0], d.inputs['Normal'])
    nt.links.new(d.outputs[0], out.inputs['Surface'])
set_mat(t, m); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"72_{V}", res=560, samples=32, cam_loc=(0.42,-0.62,0.20), target=(0,-0.03,0.0), lens=45)
