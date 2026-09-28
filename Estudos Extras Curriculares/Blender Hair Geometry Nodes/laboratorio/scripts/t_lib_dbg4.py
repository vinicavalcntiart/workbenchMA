import sys; sys.path.insert(0,'.')
exec(open('t_lib_dbg3.py').read().split("for ch in")[0])
GR, M, g, scalp = scene(**dict(length=0.24, gravity=1.8, spread=0.5, outward=0.6, n_guides=220))
ng = GR["GR Mecha Estilizada"]
for it in ng.interface.items_tree:
    if it.item_type=='SOCKET' and it.in_out=='INPUT': print("IF", it.name, getattr(it,'default_value',None), getattr(it,'subtype',None))
n = ng.nodes
cg = [x for x in n if x.bl_idname=='GeometryNodeGroup' and x.node_tree and x.node_tree.name.startswith('Create Guide')][0]
print("CG links:", [(l.from_socket.name, l.to_socket.name) for l in ng.links if l.to_node==cg])
for gid in (True, False):
    t = Tree("d"); t.chain(t.add('GeometryNodeGroup', group=GR["GR Densidade Livre"]))
    m = t.chain(t.add('GeometryNodeGroup', group=GR["GR Mecha Estilizada"]))
    print("node input Tamanho:", m.inputs['Tamanho da mecha'].default_value)
    if gid: side = t.add('GeometryNodeGroup', group=GR["GR Lado da Risca"]); t.link(side.outputs['Lado'], m.inputs['Group ID'])
    for mm in list(g.modifiers): g.modifiers.remove(mm)
    apply_tree(g, t.finish()); print("DBG4 groupID", gid, info(g))
