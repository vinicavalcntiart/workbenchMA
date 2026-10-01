import bpy, mathutils, sys
out = sys.argv[sys.argv.index("--")+1]
sc = bpy.context.scene
names = ["Robe_LOD0", "Robe_LOD1", "Robe_LOD2", "Robe_LOD3"]
sc.render.engine = 'CYCLES'; sc.cycles.samples = 24
sc.render.resolution_x = 1800; sc.render.resolution_y = 760
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (.18,.18,.2,1)
def mat(n, c):
    m = bpy.data.materials.new(n); m.use_nodes = True; m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*c, 1); return m
mb, mk = mat("b", (.75,.75,.75)), mat("k", (.01,.01,.01))
for o in list(sc.objects):
    if o.type == 'MESH' and o.name not in names: o.hide_render = True
for k, n in enumerate(names):
    o = bpy.data.objects[n]; o.location.x = k * 2.0; o.hide_render = False
    o.data.materials.clear(); o.data.materials.append(mb); o.data.materials.append(mk)
    wf = o.modifiers.new("w", 'WIREFRAME'); wf.use_replace = False; wf.thickness = 0.004; wf.material_offset = 1
sun = bpy.data.objects.new("s", bpy.data.lights.new("s", 'SUN')); sun.data.energy = 3; sun.rotation_euler = (0.8, 0.2, 0.4); sc.collection.objects.link(sun)
cam = bpy.data.objects.new("c", bpy.data.cameras.new("c")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.type = 'ORTHO'; cam.data.ortho_scale = 8.2
cam.location = (3.0, -8, 0.75); cam.rotation_euler = (1.5708, 0, 0)
sc.render.filepath = out
bpy.ops.render.render(write_still=True)
