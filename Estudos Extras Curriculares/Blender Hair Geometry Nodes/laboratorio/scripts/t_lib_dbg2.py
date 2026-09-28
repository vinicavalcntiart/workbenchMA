import sys; sys.path.insert(0,'.')
exec(open('t_lib_dbg.py').read().split("chains = ")[0])
FR = dict(cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.06), lens=50)
paths=[]; labels=[]
for ch in [["dens","mecha"],["dens","mecha","cacho"],["dens","cacho_direto"],["dens","mecha","strays","cacho"]]:
    GR, M, g, scalp = scene(**dict(length=0.24, gravity=1.8, spread=0.5, outward=0.6, n_guides=220))
    t = Tree("d")
    def grp(name, **kw):
        n = t.add('GeometryNodeGroup', group=GR[name])
        for k,v in kw.items(): n.inputs[k].default_value = v
        return n
    for s in ch:
        if s=="dens": t.chain(grp("GR Densidade Livre", **{"Viewport":1.0}))
        if s=="mecha":
            n=t.chain(grp("GR Mecha Estilizada")); side=grp("GR Lado da Risca"); t.link(side.outputs['Lado'], n.inputs['Group ID'])
        if s=="strays": t.chain(grp("GR Strays em Arco"))
        if s=="cacho": t.chain(grp("GR Cacho por Mecha"))
        if s=="cacho_direto":
            t.eg(bpy.data.node_groups['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=0.02, Existing_Guide_Map=False, Preserve_Length=True)
            t.chain(grp("GR Cacho por Mecha"))
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = hair_mat("r", melanin=0.3, redness=1.0); t.chain(sm)
    apply_tree(g, t.finish())
    paths.append(shot("21d_"+str(len(paths)), res=400, samples=12, **FR)); labels.append("+".join(ch))
print("SHEET", sheet(paths, labels, os.path.join(OUT, "21d_sheet.png"), cols=4))
