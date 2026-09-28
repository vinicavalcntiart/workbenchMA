import bpy
ng = bpy.data.node_groups.new("x",'GeometryNodeTree')
r = ng.nodes.new('FunctionNodeRandomValue'); r.data_type='FLOAT'
for i,s in enumerate(r.inputs): print("RV", i, s.name, s.identifier, s.type, "enabled" if s.enabled else "-", "avail" if getattr(s,'is_available',True) else "")
print("RV inputs['Min'] ->", r.inputs['Min'].identifier, r.inputs['Min'].type)
m = ng.nodes.new('ShaderNodeMapRange'); m.data_type='FLOAT_VECTOR'
for i,s in enumerate(m.inputs): print("MR", i, s.name, s.identifier, s.type, "enabled" if s.enabled else "-")
