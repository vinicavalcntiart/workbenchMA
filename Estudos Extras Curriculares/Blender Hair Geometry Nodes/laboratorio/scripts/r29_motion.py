import sys; sys.path.insert(0,'.')
exec(open('r28_dyn.py').read().split("def run(")[0])
import numpy as np
mode = sys.argv[-1]   # "local" ou "world"
FR = dict(cam_loc=(0.0,-0.75,0.05), target=(0,0,-0.06), lens=45)
G2 = dict(spread=0.3, gravity=4.0, outward=0.35, length=0.26, n_guides=220)
EG, head, scalp, g = base_scene(**G2); attach_uv(g, scalp)
# rig: empty gira; cabeca, scalp e guias filhos dele
rig = bpy.data.objects.new("rig", None); link(rig)
for o in (head, scalp, g): o.parent = rig
rig.rotation_mode = 'XYZ'
for f, a in ((1,0),(12,60),(24,-40),(36,0),(60,0)):
    rig.rotation_euler = (0,0,math.radians(a)); rig.keyframe_insert("rotation_euler", frame=f)
with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics']
t1 = Tree("sim"); hd = t1.add('GeometryNodeGroup', group=bpy.data.node_groups['Hair Dynamics'])
t1.ng.links.new(t1.geo, hd.inputs['Hair']); t1.geo = hd.outputs['Hair']
hd.inputs['Mode'].default_value = 'Physics (Experimental)'
for k,v in (('Bendiness',0.5),('Root Bendiness',0.1),('Substeps',20)): hd.inputs[k].default_value = v
if mode == "world":
    so = t1.add('GeometryNodeSelfObject'); oi = t1.add('GeometryNodeObjectInfo'); oi.transform_space = 'ORIGINAL'
    t1.link(so.outputs[0], oi.inputs['Object']); t1.link(oi.outputs['Transform'], hd.inputs['Simulation to World'])
apply_tree(g, t1.finish())
t2 = Tree("groom"); interp(t2, EG, density=200000.0, Viewport_Amount=1.0)
t2.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
profile(t2, EG, radius=0.0005); set_mat(t2, hair_mat("c", melanin=0.6, redness=0.6)); apply_tree(g, t2.finish())
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=48
stage(res=320, samples=8, **FR)
frames=[]; lag=[]
for f in range(1, 49):
    sc.frame_set(f)
    if f % 2 == 1:
        p = os.path.join(OUT, f"29_{mode}_{f:03d}.png"); sc.render.filepath = p; bpy.ops.render.render(write_still=True); frames.append(p)
from PIL import Image
ims = [Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in frames]
gif = os.path.join(OUT, f"29_motion_{mode}.gif"); ims[0].save(gif, save_all=True, append_images=ims[1:], duration=83, loop=0)
print("GIF", gif, len(ims))
