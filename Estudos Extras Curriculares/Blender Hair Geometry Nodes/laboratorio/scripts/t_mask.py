import sys; sys.path.insert(0,'.')
from lab import *
import numpy as np
# imagem: metade esquerda do UV preta (u<0.5), direita branca
img = None
def make_img():
    im = bpy.data.images.new("mask", 64, 64, alpha=False)
    px = np.zeros((64,64,4), np.float32); px[:,:,3]=1
    px[:, 32:, :3] = 1.0   # u >= 0.5 branco
    im.pixels.foreach_set(px.ravel()); return im
def run(label, how):
    EG, head, scalp, g = base_scene(n_guides=200); attach_uv(g, scalp)
    im = make_img()
    t = Tree("m"); it = interp(t, EG, density=300000.0)
    if how == "slot":
        it.inputs['Mask Texture'].default_value = im
    elif how == "chain":
        na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="surface_uv_coordinate")
        tx = t.add('GeometryNodeImageTexture'); tx.inputs['Image'].default_value = im; tx.interpolation = 'Closest'
        t.link(na.outputs['Attribute'], tx.inputs['Vector'])
        rv = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); t.link(tx.outputs['Color'], rv.inputs['Probability'])
        nt = t.add('FunctionNodeBooleanMath', props={'operation':'NOT'}); t.link(rv.outputs[3] if len(rv.outputs)>3 else rv.outputs[0], nt.inputs[0])
        dl = t.add('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); t.chain(dl); t.link(nt.outputs[0], dl.inputs['Selection'])
    apply_tree(g, t.finish())
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    uv = np.zeros(len(d.curves)*2, np.float32); d.attributes['surface_uv_coordinate'].data.foreach_get('vector', uv); uv = uv.reshape(-1,2)
    print(f"MASK {label:28s} fios {len(uv)}  com u<0.5 (preto): {(uv[:,0]<0.5).sum()}  u>=0.5 (branco): {(uv[:,0]>=0.5).sum()}  uv unicos {len(np.unique(uv.round(4),axis=0))}")
run("sem mascara", "none")
run("slot Mask Texture", "slot")
run("cadeia surface_uv_coordinate", "chain")
