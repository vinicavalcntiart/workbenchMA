import sys; sys.path.insert(0,'.')
exec(open('r48_scalp.py').read().split('shot(f"48_')[0])
import numpy as np
from PIL import Image
def emis(name, col):
    m = bpy.data.materials.new(name); nt = m.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); e = nt.nodes.new('ShaderNodeEmission'); e.inputs['Color'].default_value = (*col,1); e.inputs['Strength'].default_value = 1
    nt.links.new(e.outputs[0], o.inputs['Surface']); return m
head.data.materials[0] = emis("verde", (0,1,0))
scalp.hide_render = False
if pint: scalp.data.materials[0] = emis("azul", (0,0,1))
else: scalp.hide_render = True
hm = emis("preto", (0,0,0))
for n in g.modifiers[-1].node_group.nodes:
    if n.bl_idname == 'GeometryNodeSetMaterial': n.inputs['Material'].default_value = hm
stage(res=420, samples=4, cam_loc=(0.25,-0.35,0.55), target=(0,0,0.03), lens=45)
sc = bpy.context.scene; sc.cycles.use_denoising = False; sc.view_settings.view_transform = 'Standard'
p = os.path.join(OUT, "48_mask.png"); render(p)
a = np.asarray(Image.open(p).convert('RGB')).astype(float)/255
# area de cabelo+couro: tudo que nao e fundo cinza, acima do meio da cabeca
top = a[:230]
green = (top[...,1]>0.5)&(top[...,0]<0.3)&(top[...,2]<0.3)
print("MASK", int(dens), int(pint), "pele no topo px", int(green.sum()))
