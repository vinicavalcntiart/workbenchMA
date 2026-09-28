import sys; sys.path.insert(0,'.')
exec(open('t_lib6.py').read().split('t = Tree("v")')[0])
with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst): dst.materials = [m for m in src.materials if m == "GR Card Alpha"]
t = Tree("v")
grp(t, "GR Densidade Livre", **{"Fios por m2": 20000.0, "Viewport": 1.0})
grp(t, "GR Hair Cards")
set_mat(t, bpy.data.materials["GR Card Alpha"]); apply_tree(g, t.finish())
gs = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).evaluated_geometry(); me = gs.mesh
print("INFO cards tris", len(me.polygons)*2, "uv", [a.name for a in me.attributes if a.name=="UVMap"])
shot("t_lib8_cards", res=420, samples=24, cam_loc=(0.45,-0.60,0.08), target=(0,0,-0.04), lens=45)
