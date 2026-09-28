import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
V = sys.argv[-1]
SH = {  # (escala xyz, centro, corte z abaixo, comprimento guia, gravidade)
 "bob":   ((0.145,0.15,0.13), (0,0.012,-0.03), -0.13, 0.22, 3.0),
 "topete":((0.12,0.16,0.14), (0,-0.02,0.03), -0.06, 0.16, 1.0),
 "afro":  ((0.19,0.19,0.17), (0,0.01,0.02), -0.10, 0.20, 0.5),
}
sc_, c_, zcut, L, grav = SH[V.split("_")[0]]
EG, head, scalp, g = base_scene(length=L, gravity=grav, spread=0.3, outward=0.5, n_guides=220)
me = bpy.data.meshes.new("shell"); bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=1.0)
bmesh.ops.scale(bm, vec=sc_, verts=bm.verts); bmesh.ops.translate(bm, vec=c_, verts=bm.verts)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < zcut or (f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.05)], context='FACES')
bm.to_mesh(me); bm.free(); shell = link(bpy.data.objects.new("shell", me)); shell.hide_render = True
t = Tree("shell")
if not V.endswith("_sem"):
    oi = t.add('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); oi.inputs['Object'].default_value = shell
    gp = t.add('GeometryNodeProximity', props={'target_element':'FACES'}); t.link(oi.outputs['Geometry'], gp.inputs[0])
    sp = t.add('GeometryNodeSplineParameter')
    mr = t.add('ShaderNodeMapRange'); mr.clamp=True; t.link(sp.outputs['Factor'], mr.inputs['Value']); mr.inputs['From Max'].default_value=0.35
    ps = t.add('GeometryNodeInputPosition')
    mx = t.add('ShaderNodeMix', props={'data_type':'VECTOR'}); t.link(mr.outputs['Result'], mx.inputs['Factor']); t.link(ps.outputs[0], mx.inputs[4]); t.link(gp.outputs['Position'], mx.inputs[5])
    s = t.add('GeometryNodeSetPosition'); t.chain(s); t.link(mx.outputs[1], s.inputs['Position'])
interp(t, EG, density=250000.0)
t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
if V.startswith("afro"): t.eg(EG['Curl Hair Curves'], Factor=1.0, Radius=0.004, Frequency=25.0, Existing_Guide_Map=True, Subdivision=2)
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("c", melanin=0.6, redness=0.5)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"45_{V}", res=420, samples=16, cam_loc=(0.45,-0.60,0.08), target=(0,0,-0.04), lens=45)
if V.endswith("_sem"):
    g.hide_render=True; shell.hide_render=False
    m = bpy.data.materials.new("sh"); m.diffuse_color=(0.3,0.6,1,1); m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.3,0.6,1,1); m.node_tree.nodes['Principled BSDF'].inputs['Alpha'].default_value=0.45
    shell.data.materials.append(m); render(os.path.join(OUT, f"45_{V}_malha.png"))
