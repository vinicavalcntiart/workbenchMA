import sys; sys.path.insert(0,'.')
src = open('r55_morph.py').read()
src = src.split("pB = t.add('GeometryNodeInputPosition')")[0]
exec(src)
tr = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Transição"]); t.link(base, tr.inputs[0]); t.link(cb.outputs[0], tr.inputs[1]); tr.inputs["Fator"].default_value = 0.5
t.geo = tr.outputs[0]
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.3, redness=1.0)); apply_tree(g, t.finish())
print("INFO", stats(g).get('curves'), stats(g).get('points'))
shot("t_lib10_transicao", res=380, samples=16, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
