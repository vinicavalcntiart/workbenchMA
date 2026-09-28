import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
MODE = sys.argv[-1]   # cut | uniform | fio
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
t = Tree("grow"); interp(t, EG, density=200000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=0.008, Frequency=5.0, Existing_Guide_Map=True, Subdivision=2)
# Length Factor = clamp(Seconds*0.8 - atraso, 0.02, 1); atraso = Random 0..0.4 por mecha (ou por fio)
st = t.add('GeometryNodeInputSceneTime')
rv = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=0.4)
if MODE != "fio":
    na = t.add('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}); na.inputs['Name'].default_value='guide_curve_index'
    t.link(na.outputs['Attribute'], rv.inputs['ID'])
ev = t.add('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); t.link(rv.outputs['Value'], ev.inputs[0])
ma = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(st.outputs['Seconds'], ma.inputs[0]); ma.inputs[1].default_value=0.8
neg = t.add('ShaderNodeMath', props={'operation':'SUBTRACT'}); t.link(ma.outputs[0], neg.inputs[0]); t.link(ev.outputs[0], neg.inputs[1]); ma.inputs[2].default_value=0.0
cl = t.add('ShaderNodeClamp'); t.link(neg.outputs[0], cl.inputs['Value']); cl.inputs['Min'].default_value=0.02
tr = t.eg(EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=(MODE=="uniform"))
t.link(cl.outputs[0], tr.inputs['Length Factor'])
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("c", melanin=0.45, redness=0.9)); apply_tree(g, t.finish())
sc = bpy.context.scene; sc.frame_start=1; sc.frame_end=48
stage(res=320, samples=8, cam_loc=(0.42,-0.62,0.06), target=(0,0,-0.07), lens=48)
tt=time.time(); frames=[]
for f in range(1,49,2):
    sc.frame_set(f); p=os.path.join(OUT, f"41_{MODE}_{f:03d}.png"); sc.render.filepath=p; bpy.ops.render.render(write_still=True); frames.append(p)
    if f==25: print("INFO", MODE, stats(g).get('curves'), stats(g).get('points'))
from PIL import Image
ims=[Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in frames]
ims[0].save(os.path.join(OUT,f"41_crescer_{MODE}.gif"), save_all=True, append_images=ims[1:]+[ims[-1]]*6, duration=83, loop=0)
print("TIME", MODE, round(time.time()-tt,1))
