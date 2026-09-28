import sys; sys.path.insert(0,'.')
exec(open('t_cgim.py').read().split("for gd in")[0])
cases = [
 ("CGIM 0.02 -> Clump(GI ligado, Existing OFF, GD 0.1)", dict(link=True, ex=False, gd=0.1)),
 ("CGIM 0.02 -> Clump(GI ligado, Existing ON,  GD 0.1)", dict(link=True, ex=True, gd=0.1)),
 ("CGIM 0.02 -> Clump(sem GI,    Existing ON,  GD 0.1)", dict(link=False, ex=True, gd=0.1)),
 ("Clump sozinho GD 0.02 Existing OFF", dict(link=False, ex=False, gd=0.02, nocg=True)),
]
for lb, c in cases:
    EG, head, scalp, g = base_scene(n_guides=220)
    t = Tree("c"); interp(t, EG, density=300000.0)
    if not c.get("nocg"): cg = t.eg(EG['Create Guide Index Map'], Guide_Distance=0.02)
    cl = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=c['gd'], Existing_Guide_Map=c['ex'], Preserve_Length=True)
    if c['link']: t.link(cg.outputs['Guide Index'], cl.inputs['Guide Index'])
    st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type':'INT','domain':'CURVE'}, Name="gi_clump"); t.chain(st)
    t.link(cl.outputs['Guide Index'], st.inputs['Value'])
    apply_tree(g, t.finish())
    print(f"CL {lb}: Guide Index usado pelo Clump unicos {uniq(g,'gi_clump')[0]}, atributo guide_curve_index {uniq(g,'guide_curve_index')[0]}")
