import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.28, gravity=4.0, spread=0.35, outward=0.3, n_guides=200)
TOP = dict(cam_loc=(0.0,-0.25,0.42), target=(0,0.0,0.02), lens=50)
def split_scalp(scalp):
    """Rasga o scalp em x=0: vira duas ilhas."""
    bm = bmesh.new(); bm.from_mesh(scalp.data)
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], plane_co=(0,0,0), plane_no=(1,0,0))
    edges = [e for e in bm.edges if all(abs(v.co.x) < 1e-6 for v in e.verts)]
    bmesh.ops.split_edges(bm, edges=edges)
    bm.to_mesh(scalp.data); bm.free()
def build(t, EG, g=None, scalp=None, islands=False, groupid=False):
    if islands: split_scalp(scalp)
    it = interp(t, EG, density=300000.0, Part_by_Mesh_Islands=True)
    if groupid:
        cg = t.add('GeometryNodeGroup', group=EG['Create Guide Index Map'], Guide_Distance=0.02)
        t.chain(cg)
        pos = t.add('GeometryNodeInputPosition'); sep = t.add('ShaderNodeSeparateXYZ'); t.link(pos.outputs[0], sep.inputs[0])
        cmp = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'GREATER_THAN'}, B=0.0)
        t.link(sep.outputs['X'], cmp.inputs['A'])
        # posicao da RAIZ: Curve Root essentials
        root = t.add('GeometryNodeGroup', group=EG['Curve Root'])
        sep2 = t.add('ShaderNodeSeparateXYZ'); t.link(root.outputs['Root Position'], sep2.inputs[0]); t.link(sep2.outputs['X'], cmp.inputs['A'])
        b2i = t.add('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'GREATER_THAN'}, B=0.0)
        t.link(cmp.outputs['Result'], cg.inputs['Group ID'])
        c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Existing_Guide_Map=False, Seed=1)
        t.link(cg.outputs['Guide Index'], c.inputs['Guide Index'])
    else:
        t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True,
             Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    profile(t, EG, radius=0.0005)
    set_mat(t, hair_mat("c", melanin=0.75, redness=0.35))
run_variants("17_part", [
    ("scalp inteiro, Clump normal", dict()),
    ("scalp em 2 ilhas (Part by Mesh Islands)", dict(islands=True)),
    ("2 ilhas + Clump com Group ID = raiz.x>0", dict(islands=True, groupid=True)),
], build, cols=3, **TOP)
