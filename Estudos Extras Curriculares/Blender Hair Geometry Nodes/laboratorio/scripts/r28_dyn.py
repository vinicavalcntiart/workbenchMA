import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
import numpy as np
DYN = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','geometry_nodes_dynamics_assets.blend')
G = dict(spread=0.5, gravity=1.8, outward=0.6, length=0.24, n_guides=260)
FR = dict(cam_loc=(0.42,-0.62,0.02), target=(0,0,-0.08), lens=48)
def guide_tips(g):
    dg = bpy.context.evaluated_depsgraph_get(); d = g.evaluated_get(dg).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    idx = np.array([c.first_point_index+c.points_length-1 for c in d.curves]); return P[idx], len(d.curves)
def run(label, bend=0.5, rootb=0.2, sim=True, frames=48, render_it=True, attach=True):
    EG, head, scalp, g = base_scene(**dict(G))
    if attach: attach_uv(g, scalp)
    with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics']
    HD = bpy.data.node_groups['Hair Dynamics']
    # 1) modificador de simulacao so nas guias
    t1 = Tree("sim")
    if sim:
        hd = t1.add('GeometryNodeGroup', group=HD)
        t1.ng.links.new(t1.geo, hd.inputs['Hair']); t1.geo = hd.outputs['Hair']
        hd.inputs['Mode'].default_value = 'Physics (Experimental)'
        hd.inputs['Bendiness'].default_value = bend; hd.inputs['Root Bendiness'].default_value = rootb
        hd.inputs['Surface Collision'].default_value = True; hd.inputs['Deforming'].default_value = False
    apply_tree(g, t1.finish())
    sc = bpy.context.scene; sc.frame_start = 1; sc.frame_end = frames
    sc.frame_set(1); T0, n = guide_tips(g)
    for f in range(2, frames+1): sc.frame_set(f)
    T1, _ = guide_tips(g)
    drop = (T0[:,2]-T1[:,2]).mean()*100; outw = (np.linalg.norm(T1[:,:2],axis=1)-np.linalg.norm(T0[:,:2],axis=1)).mean()*100
    print(f"DYN {label:34s} guias {n}  ponta desce {drop:.1f} cm, abre {outw:+.1f} cm (quadro {frames})")
    if not render_it: return None
    # 2) groom depois da simulacao
    t2 = Tree("groom"); interp(t2, EG, density=250000.0)
    t2.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    profile(t2, EG, radius=0.0005); set_mat(t2, hair_mat("c", melanin=0.45, redness=0.8))
    apply_tree(g, t2.finish())
    return shot("28b_"+label.split()[0], res=420, samples=14, **FR)
V = [("sem_sim (forma penteada)", dict(sim=False)), ("padrao Bend 0.5 Root 0.2", dict()),
     ("duro Bend 0.05 Root 0.02", dict(bend=0.05, rootb=0.02)), ("mole Bend 1.0 Root 0.5", dict(bend=1.0, rootb=0.5))]
paths=[]; labels=[]
for lb, kw in V:
    p = run(lb, **kw); paths.append(p); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"28b_dyn_sheet.png"), cols=4))
