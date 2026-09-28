import sys; sys.path.insert(0,'.')
exec(open('r16_chunky.py').read().split("BACK = dict")[0])
import numpy as np
EG, head, scalp, g = base_scene(**G)
t = Tree("dbg"); build(t, EG, flat=0.35); apply_tree(g, t.finish())
dg = bpy.context.evaluated_depsgraph_get()
for inst in dg.object_instances:
    o = inst.object
    if o.type == 'MESH' and o.original == g or (inst.is_instance and inst.parent and inst.parent.original == g):
        m = o.data; P = np.zeros(len(m.vertices)*3); m.vertices.foreach_get('co', P); P = P.reshape(-1,3)
        print("MESH", o.name, "verts", len(m.vertices), "faces", len(m.polygons), "bbox", P.min(0).round(3), P.max(0).round(3), "nan", np.isnan(P).any())
    if o.original == g: print("INST", o.name, o.type, inst.is_instance)
