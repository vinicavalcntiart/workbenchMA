import sys; sys.path.insert(0,'.')
exec(open('r28_dyn.py').read().split("def run(")[0])
DYN = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','geometry_nodes_dynamics_assets.blend')
F = float(sys.argv[-1])
G2 = dict(spread=0.3, gravity=4.0, outward=0.35, length=0.30, n_guides=240)
EG, head, scalp, g = base_scene(**G2); attach_uv(g, scalp)
with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics','Custom Force']
t1 = Tree("sim"); hd = t1.add('GeometryNodeGroup', group=bpy.data.node_groups['Hair Dynamics'])
t1.ng.links.new(t1.geo, hd.inputs['Hair']); t1.geo = hd.outputs['Hair']
hd.inputs['Mode'].default_value = 'Physics (Experimental)'
for k,v in (('Bendiness',0.3),('Root Bendiness',0.05),('Substeps',20)): hd.inputs[k].default_value = v
cf = t1.add('GeometryNodeGroup', group=bpy.data.node_groups['Custom Force'])
# vento: F * (0.6 + 0.4*sin(2pi*t/1.5s)) em X + turbulencia 3D
st = t1.add('GeometryNodeInputSceneTime')
w = t1.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t1.link(st.outputs['Seconds'], w.inputs[0]); w.inputs[1].default_value = 2*math.pi/1.5
sn = t1.add('ShaderNodeMath', props={'operation':'SINE'}); t1.link(w.outputs[0], sn.inputs[0])
gust = t1.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t1.link(sn.outputs[0], gust.inputs[0]); gust.inputs[1].default_value = 0.4; gust.inputs[2].default_value = 0.6
fx = t1.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t1.link(gust.outputs[0], fx.inputs[0]); fx.inputs[1].default_value = F
base = t1.add('ShaderNodeCombineXYZ'); t1.link(fx.outputs[0], base.inputs['X'])
pos = t1.add('GeometryNodeInputPosition')
nz = t1.add('ShaderNodeTexNoise', Scale=15.0, Detail=1.0); nz.noise_dimensions = '4D'
t1.link(pos.outputs[0], nz.inputs['Vector']); t1.link(st.outputs['Seconds'], nz.inputs['W'])
cen = t1.add('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); t1.link(nz.outputs['Color'], cen.inputs[0]); cen.inputs[1].default_value = (0.5,0.5,0.5)
tb = t1.add('ShaderNodeVectorMath', props={'operation':'SCALE'}); t1.link(cen.outputs[0], tb.inputs[0]); tb.inputs['Scale'].default_value = F*1.2
fv = t1.add('ShaderNodeVectorMath', props={'operation':'ADD'}); t1.link(base.outputs[0], fv.inputs[0]); t1.link(tb.outputs[0], fv.inputs[1])
t1.link(fv.outputs[0], cf.inputs['Force'])
t1.link(cf.outputs['Force'], [s for s in hd.inputs if s.name=='Effectors' and s.type=='BUNDLE'][0])
apply_tree(g, t1.finish())
t2 = Tree("groom"); interp(t2, EG, density=200000.0, Viewport_Amount=1.0)
t2.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
profile(t2, EG, radius=0.0005); set_mat(t2, hair_mat("c", melanin=0.4, redness=0.8)); apply_tree(g, t2.finish())
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=48
stage(res=320, samples=8, cam_loc=(0.0,-0.75,0.0), target=(0.04,0,-0.08), lens=42)
frames=[]; tipx=[]
import numpy as np
for f in range(1,49):
    sc.frame_set(f)
    if f % 2 == 1:
        p = os.path.join(OUT, f"39_{F}_{f:03d}.png"); sc.render.filepath = p; bpy.ops.render.render(write_still=True); frames.append(p)
    if f in (1,12,24,36,48):
        d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
        P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
        T = P[[c.first_point_index+c.points_length-1 for c in d.curves]]; tipx.append(f"q{f}: ponta x media {T[:,0].mean()*100:+.1f} cm")
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in frames]
gif=os.path.join(OUT, f"39_vento_{F}.gif"); ims[0].save(gif, save_all=True, append_images=ims[1:], duration=83, loop=0)
print("WIND", F, " | ".join(tipx)); print("GIF", gif)
