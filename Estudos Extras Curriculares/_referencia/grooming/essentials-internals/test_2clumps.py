import bpy, os, random, math
import numpy as np
assets = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','procedural_hair_node_assets.blend')
with bpy.data.libraries.load(assets, link=False) as (src, dst):
    dst.node_groups = ['Clump Hair Curves','Create Guide Index Map']
bpy.ops.wm.read_homefile(use_empty=True)
with bpy.data.libraries.load(assets, link=False) as (src, dst):
    dst.node_groups = ['Clump Hair Curves','Create Guide Index Map']
CL = bpy.data.node_groups['Clump Hair Curves']; CG = bpy.data.node_groups['Create Guide Index Map']

# 40x40 fios retos, 8 pontos, altura 0.2, sem surface
N=40; P=8; random.seed(1)
cd = bpy.data.hair_curves.new("hair")
cd.add_curves([P]*(N*N))

pts=[]
for i in range(N):
    for j in range(N):
        x=i/N+random.uniform(-0.01,0.01); y=j/N+random.uniform(-0.01,0.01)
        for k in range(P):
            t=k/(P-1); pts.append((x+0.05*t, y, 0.2*t))
import itertools
flat=list(itertools.chain.from_iterable(pts))
cd.attributes['position'].data.foreach_set('vector', flat)
ob = bpy.data.objects.new("hair", cd); bpy.context.scene.collection.objects.link(ob)

def sid(ng,name):
    for it in ng.interface.items_tree:
        if it.item_type=='SOCKET' and it.in_out=='INPUT' and it.name==name: return it.identifier

def build(chain):
    """chain: lista de (grupo, {input: valor}) em fila"""
    ng = bpy.data.node_groups.new("t", 'GeometryNodeTree')
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    gi = ng.nodes.new('NodeGroupInput'); go = ng.nodes.new('NodeGroupOutput')
    prev = gi.outputs[0]; last=None
    for grp, vals in chain:
        n = ng.nodes.new('GeometryNodeGroup'); n.node_tree = grp
        ng.links.new(prev, n.inputs['Geometry'])
        for k,v in vals.items(): n.inputs[k].default_value = v
        if last is not None and grp is CL and 'Guide Index' in vals: pass
        prev = n.outputs['Geometry']; last=n
    ng.links.new(prev, go.inputs[0])
    return ng

def evalpos(ng):
    for m in list(ob.modifiers): ob.modifiers.remove(m)
    m = ob.modifiers.new("gn",'NODES'); m.node_group = ng
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    c = ev.data
    arr = np.zeros(len(c.attributes['position'].data)*3, dtype=np.float32)
    c.attributes['position'].data.foreach_get('vector', arr)
    arr = arr.reshape(-1,3)
    names = [a.name for a in c.attributes]
    return arr.reshape(N*N,P,3)[:, -1, :].copy(), names   # pontas

def nclumps(tips, r=0.005):
    # agrupa pontas proximas: numero aproximado de mechas
    q = np.round(tips/ r).astype(int)
    return len({tuple(x) for x in q})

S = {}
S['A_0.08'] = build([(CL, {'Guide Distance':0.08})])
S['B_0.02'] = build([(CL, {'Guide Distance':0.02})])
S['A>B_existON'] = build([(CL, {'Guide Distance':0.08}), (CL, {'Guide Distance':0.02,'Seed':7,'Existing Guide Map':True})])
S['A>B_existOFF'] = build([(CL, {'Guide Distance':0.08}), (CL, {'Guide Distance':0.02,'Seed':7,'Existing Guide Map':False})])
S['CGIM0.08>Clump_existON'] = build([(CG, {'Guide Distance':0.08}), (CL, {'Guide Distance':0.02,'Existing Guide Map':True})])
S['CGIM0.08>Clump_existOFF'] = build([(CG, {'Guide Distance':0.08}), (CL, {'Guide Distance':0.02,'Existing Guide Map':False})])
R = {}
for k,ng in S.items():
    tips, names = evalpos(ng); R[k]=tips
    print(f"{k:28s} mechas~{nclumps(tips):5d}  attrs={[n for n in names if 'guide' in n]}")
def d(a,b): return float(np.abs(R[a]-R[b]).max())
print("\nA>B existON  vs A>B existOFF : max diff", round(d('A>B_existON','A>B_existOFF'),5))
print("A>B existON  vs A alone      : max diff", round(d('A>B_existON','A_0.08'),5))
print("A>B existOFF vs A alone      : max diff", round(d('A>B_existOFF','A_0.08'),5))
print("CGIM>Clump ON vs OFF         : max diff", round(d('CGIM0.08>Clump_existON','CGIM0.08>Clump_existOFF'),5))
print("CGIM>Clump ON vs A alone     : max diff", round(d('CGIM0.08>Clump_existON','A_0.08'),5))
