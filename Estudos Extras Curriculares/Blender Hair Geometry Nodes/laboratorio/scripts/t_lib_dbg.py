import sys; sys.path.insert(0,'.')
exec(open('t_lib.py').read().split("BACK = dict")[0])
import numpy as np
def measure(g):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    tips = np.array([c.first_point_index+c.points_length-1 for c in d.curves])
    r = np.linalg.norm(P[tips],axis=1); return f"fios {len(tips)} pts/fio {len(P)//max(1,len(tips))} ponta: dist centro mediana {np.median(r)*100:.1f} cm, z mediana {np.median(P[tips][:,2])*100:.1f} cm"
chains = [["dens"],["dens","mecha"],["dens","mecha","strays"],["dens","mecha","strays","cacho"],["dens","cacho_direto"]]
for ch in chains:
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
            c = t.eg(bpy.data.node_groups['Clump Hair Curves'], Factor=1.0, Shape=0.25, Guide_Distance=0.02, Existing_Guide_Map=False, Preserve_Length=True)
            t.chain(grp("GR Cacho por Mecha"))
    apply_tree(g, t.finish()); print("DBG", "+".join(ch), measure(g))
