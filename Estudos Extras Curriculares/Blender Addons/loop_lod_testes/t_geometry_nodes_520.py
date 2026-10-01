import bpy, sys, math
sys.path.insert(0, "/home/user/workbenchMA/Estudos Extras Curriculares/Blender Addons")
import loop_lod
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.read_homefile(use_empty=True); loop_lod.register()
# objeto so com edges + Geometry Nodes que faz o tubo (como o seu)
me = bpy.data.meshes.new("Linha_LOD0"); vs = [(-1,0,0),(0,0.3,0),(1,0,0),(1.5,0.8,0)]
me.from_pydata(vs, [(0,1),(1,2),(2,3)], []); ob = bpy.data.objects.new("Linha_LOD0", me); bpy.context.scene.collection.objects.link(ob)
ng = bpy.data.node_groups.new("tubo", 'GeometryNodeTree')
ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'); ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
N = ng.nodes; L = ng.links.new; gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput')
m2c = N.new('GeometryNodeMeshToCurve'); st = N.new('GeometryNodeCurveSplineType'); st.spline_type = 'CATMULL_ROM'
rs = N.new('GeometryNodeResampleCurve'); rs.inputs['Mode'].default_value = 'Length'; rs.inputs['Length'].default_value = 0.05
cc = N.new('GeometryNodeCurvePrimitiveCircle'); cc.inputs['Radius'].default_value = 0.08; cc.inputs['Resolution'].default_value = 16
c2m = N.new('GeometryNodeCurveToMesh')
L(gi.outputs[0], m2c.inputs['Mesh']); L(m2c.outputs[0], st.inputs['Curve']); L(st.outputs[0], rs.inputs['Curve']); L(rs.outputs[0], c2m.inputs['Curve']); L(cc.outputs['Curve'], c2m.inputs['Profile Curve']); L(c2m.outputs[0], go.inputs[0])
ob.modifiers.new("GN", 'NODES').node_group = ng
arm = bpy.data.objects.new("Rig", bpy.data.armatures.new("Rig")); bpy.context.scene.collection.objects.link(arm)
am = ob.modifiers.new("Armature", 'ARMATURE'); am.object = arm
bpy.context.view_layer.objects.active = ob
p = bpy.context.scene.loop_lod
for r in (0.5, 0.25): p.lods.add().ratio = r
p.use_evaluated = True; p.symmetry = False
src, out = loop_lod.generate_lods(bpy.context, ob, p)
P("RESULT original (avaliado com GN)", src, "tris; malha original tem", len(ob.data.polygons), "faces")
for n, t, g in out:
    o = bpy.data.objects[n]
    P("RESULT", n, "alvo", t, "obtido", g, "modificadores", [m.type for m in o.modifiers], "colecao", [c.name for c in o.users_collection])
