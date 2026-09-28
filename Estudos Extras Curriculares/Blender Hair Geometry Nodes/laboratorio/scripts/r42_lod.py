import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
from PIL import Image
D = 1.0; LOD = True
EG, head, scalp, g = base_scene(length=0.28, gravity=4.0, spread=0.3, outward=0.3, n_guides=200)
dirv = Vector((0.42,-0.62,0.06)); tgt = Vector((0,0,-0.07)); cam_loc = tgt + (dirv-tgt).normalized()*D
cam = stage(res=480, samples=16, cam_loc=tuple(cam_loc), target=tuple(tgt), lens=50)
t = Tree("lod"); interp(t, EG, density=250000.0)
keep = None
if LOD:
    oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = cam
    cr = t.add('GeometryNodeGroup', group=EG['Curve Root'])
    dist = t.add('ShaderNodeVectorMath', props={'operation':'DISTANCE'}); t.link(cr.outputs['Root Position'], dist.inputs[0]); t.link(oi.outputs['Location'], dist.inputs[1])
    mr = t.add('ShaderNodeMapRange'); mr.clamp=True; t.link(dist.outputs['Value'], mr.inputs['Value'])
    mr.inputs['From Min'].default_value=1.0; mr.inputs['From Max'].default_value=8.0; mr.inputs['To Min'].default_value=1.0; mr.inputs['To Max'].default_value=0.04
    keep = mr.outputs['Result']
    rb = t.add('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); t.link(keep, rb.inputs['Probability'])
    nt = t.add('FunctionNodeBooleanMath', props={'operation':'NOT'}); t.link(rb.outputs[3] if len(rb.outputs)>3 else rb.outputs['Value'], nt.inputs[0])
    dl = t.add('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); t.chain(dl); t.link(nt.outputs[0], dl.inputs['Selection'])
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
profile(t, EG, radius=0.0005)
if LOD:
    sq = t.add('ShaderNodeMath', props={'operation':'INVERSE_SQRT'}); t.link(keep, sq.inputs[0])
    rn = t.add('GeometryNodeInputRadius'); mu = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(rn.outputs[0], mu.inputs[0]); t.link(sq.outputs[0], mu.inputs[1])
    sr = t.add('GeometryNodeSetCurveRadius'); t.chain(sr, 'Curve', 'Curve'); t.link(mu.outputs[0], sr.inputs['Radius'])
set_mat(t, hair_mat("c", melanin=0.5, redness=0.6)); m = apply_tree(g, t.finish())

res=480
for D in (0.75, 2.5, 6.0):
    cam.location = tgt + (dirv-tgt).normalized()*D
    for on in (0,1):
        mr.inputs['To Max'].default_value = 0.04 if on else 1.0
        bpy.context.view_layer.update(); dg = bpy.context.evaluated_depsgraph_get(); dg.update(); st = stats(g)
        ts=[]
        for i in range(3):
            m.show_viewport=False; dg.update(); m.show_viewport=True; t0=time.time(); dg.update(); g.evaluated_get(dg).data.points; ts.append(time.time()-t0)
        p = os.path.join(OUT, f"42_d{D}_{on}.png"); rt = render(p)
        frac = min(1.0, 0.42/(0.72*D)); c = int(res*frac); x0=(res-c)//2
        Image.open(p).crop((x0,x0,x0+c,x0+c)).resize((400,400), Image.LANCZOS).save(p.replace('.png','_crop.png'))
        print("INFO", D, on, st.get('curves'), st.get('points'), "eval ms", round(min(ts)*1000), "render s", rt)
