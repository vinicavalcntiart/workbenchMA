import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import numpy as np
V = sys.argv[-1]   # sem | gradiente | faixas
EG, head, scalp, g = base_scene(length=0.26, gravity=4.0, spread=0.3, outward=0.3, n_guides=220)
N = 128; px = np.zeros((N,N,4), np.float32); px[:,:,3] = 1
u = np.linspace(0,1,N)[None,:].repeat(N,0)
if V == "gradiente": val = u                                     # "pintura": curto num lado, longo no outro
else: val = (np.sin(u*2*np.pi*6) > 0).astype(np.float32)         # faixas: camadas alternadas
px[:,:,0] = px[:,:,1] = px[:,:,2] = val
im = bpy.data.images.new("comprimento", N, N, alpha=False); im.pixels.foreach_set(px.ravel())
t = Tree("cp"); interp(t, EG, density=250000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
if V != "sem":
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}); na.inputs['Name'].default_value = 'surface_uv_coordinate'
    tx = t.add('GeometryNodeImageTexture'); tx.inputs['Image'].default_value = im; t.link(na.outputs['Attribute'], tx.inputs['Vector'])
    mr = t.add('ShaderNodeMapRange'); mr.clamp = True; t.link(tx.outputs['Color'], mr.inputs['Value']); mr.inputs['To Min'].default_value = 0.35; mr.inputs['To Max'].default_value = 1.1
    ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(mr.outputs['Result'], ev.inputs[0])
    tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=False); t.link(ev.outputs[0], tr.inputs['Length Factor'])
profile(t, EG, radius=0.0005); set_mat(t, hair_mat("h", melanin=0.3, redness=0.9)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"78_{V}", res=420, samples=16, cam_loc=(0.0,0.72,-0.02), target=(0,0,-0.08), lens=42)
