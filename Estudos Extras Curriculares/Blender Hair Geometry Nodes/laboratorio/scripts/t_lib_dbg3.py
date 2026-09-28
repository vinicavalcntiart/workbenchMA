import sys; sys.path.insert(0,'.')
exec(open('t_lib_dbg.py').read().split("chains = ")[0])
def info(g):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    gi = d.attributes.get('guide_curve_index'); G_=None
    if gi:
        G_ = np.zeros(len(d.curves), np.int32); gi.data.foreach_get('value', G_)
    bad = np.isnan(P).any(1).sum()
    far = (np.linalg.norm(P,axis=1) > 1.0).sum()
    s = f"pontos NaN {bad}, pontos a >1m {far} de {len(P)}"
    if G_ is not None: s += f"; guide_curve_index min {G_.min()} max {G_.max()} unicos {len(np.unique(G_))} (fios {len(G_)}) dominio {gi.domain}"
    return s
for ch in (["dens","mecha"],["dens","mecha","cacho"],["dens","cacho_direto"]):
    GR, M, g, scalp = scene(**dict(length=0.24, gravity=1.8, spread=0.5, outward=0.6, n_guides=220))
    t = Tree("d")
    def grp(name, **kw):
        n = t.add('GeometryNodeGroup', group=GR[name]); [setattr(n.inputs[k],'default_value',v) for k,v in kw.items()]; return n
    for s in ch:
        if s=="dens": t.chain(grp("GR Densidade Livre", **{"Viewport":1.0}))
        if s=="mecha": n=t.chain(grp("GR Mecha Estilizada")); side=grp("GR Lado da Risca"); t.link(side.outputs['Lado'], n.inputs['Group ID'])
        if s=="cacho": t.chain(grp("GR Cacho por Mecha"))
        if s=="cacho_direto":
            t.eg(bpy.data.node_groups['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=0.02, Existing_Guide_Map=False, Preserve_Length=True); t.chain(grp("GR Cacho por Mecha"))
    apply_tree(g, t.finish()); print("DBG3", "+".join(ch), info(g))
