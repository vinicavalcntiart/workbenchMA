import bpy, sys
def P(*a): print(*a); sys.stdout.flush()
bpy.ops.wm.read_homefile(use_empty=True)
me = bpy.data.meshes.new("linha"); vs = [(0,0,0),(1,-0.5,0),(2.5,-0.2,0),(3,1,0)]
me.from_pydata(vs, [(0,1),(1,2),(2,3)], []); ob = bpy.data.objects.new("linha", me); bpy.context.scene.collection.objects.link(ob)
ng = bpy.data.node_groups.new("Edge para Cilindro", 'GeometryNodeTree')
ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
r = ng.interface.new_socket("Raio", in_out='INPUT', socket_type='NodeSocketFloat'); r.default_value = 0.05
rs = ng.interface.new_socket("Lados", in_out='INPUT', socket_type='NodeSocketInt'); rs.default_value = 12
ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
N = ng.nodes; L = ng.links.new
gi = N.new('NodeGroupInput'); go = N.new('NodeGroupOutput')
m2c = N.new('GeometryNodeMeshToCurve')
cc = N.new('GeometryNodeCurvePrimitiveCircle')
c2m = N.new('GeometryNodeCurveToMesh')
ss = N.new('GeometryNodeSetShadeSmooth')
L(gi.outputs[0], m2c.inputs['Mesh']); L(m2c.outputs[0], c2m.inputs['Curve'])
L(gi.outputs[1], cc.inputs['Radius']); L(gi.outputs[2], cc.inputs['Resolution']); L(cc.outputs['Curve'], c2m.inputs['Profile Curve'])
c2m.inputs['Fill Caps'].default_value = True
L(c2m.outputs[0], ss.inputs['Geometry']); L(ss.outputs[0], go.inputs[0])
m = ob.modifiers.new("GN", 'NODES'); m.node_group = ng
dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg).data
P("RESULT verts", len(ev.vertices), "faces", len(ev.polygons), "inputs c2m", [s.name for s in c2m.inputs])
# variacao: cantos suaves (Bezier + Auto + Resample) e afinar com Scale
st = N.new('GeometryNodeCurveSplineType'); st.spline_type = 'BEZIER'
ht = N.new('GeometryNodeCurveSetHandles'); ht.handle_type = 'AUTO'
rs2 = N.new('GeometryNodeResampleCurve'); rs2.inputs['Count'].default_value = 40
L(m2c.outputs[0], st.inputs['Curve']); L(st.outputs[0], ht.inputs['Curve']); L(ht.outputs[0], rs2.inputs['Curve']); L(rs2.outputs[0], c2m.inputs['Curve'])
sp = N.new('GeometryNodeSplineParameter'); mr = N.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 1.0; mr.inputs['To Max'].default_value = 0.2
L(sp.outputs['Factor'], mr.inputs['Value']); L(mr.outputs['Result'], c2m.inputs['Scale'])
ob.data.update(); dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg).data
import mathutils
vs = [v.co for v in ev.vertices]
P("RESULT suave verts", len(ev.vertices), "faces", len(ev.polygons))
# raio no inicio x no fim: distancia dos vertices do primeiro e do ultimo anel ao centro do anel
ring = 12
def rad(k):
    pts = vs[k*ring:(k+1)*ring]; c = sum(pts, mathutils.Vector()) / ring; return max((p - c).length for p in pts)
P("RESULT raio inicio", round(rad(0),3), "fim", round(rad(39),3))
