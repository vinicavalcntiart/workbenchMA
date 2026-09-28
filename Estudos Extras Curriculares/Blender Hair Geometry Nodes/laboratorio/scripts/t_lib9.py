import sys; sys.path.insert(0,'.')
sys.argv = sys.argv[:-1] + ['sem']
exec(open('r53_toon.py').read().split("apply_tree(g, t.finish())")[0])
c = t.add('GeometryNodeGroup', group=bpy.data.node_groups["GR Contorno"]); t.chain(c, 'Mesh', 'Mesh')
bpy.context.scene.cycles.transparent_max_bounces = 64
apply_tree(g, t.finish())
print("INFO mat default", c.inputs['Material'].default_value.name if c.inputs['Material'].default_value else None)
shot("t_lib9_contorno", res=440, samples=24, cam_loc=(0.50,-0.66,0.10), target=(0,0,-0.03), lens=45)
