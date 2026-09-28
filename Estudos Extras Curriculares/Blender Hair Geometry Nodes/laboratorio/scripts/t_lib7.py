import sys; sys.path.insert(0,'.')
exec(open('t_lib6.py').read().split('t = Tree("v")')[0])
W2 = sys.argv[-1]
def shell(sc,c,zcut=-1,face=False):
    me = bpy.data.meshes.new("shell"); bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=1.0)
    bmesh.ops.scale(bm, vec=sc, verts=bm.verts); bmesh.ops.translate(bm, vec=c, verts=bm.verts)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().z < zcut or (face and f.calc_center_median().y < -0.09 and f.calc_center_median().z < 0.05)], context='FACES')
    bm.to_mesh(me); bm.free(); o = link(bpy.data.objects.new("shell", me)); o.hide_render=True; return o
t = Tree("v")
grp(t, "GR Densidade Livre", **{"Fios por m2": 250000.0, "Viewport": 1.0})
if W2 == "trolls":
    grp(t, "GR Comprimento até a Malha", **{"Malha da forma": shell((0.16,0.16,0.35),(0,0.02,0.15))})
    t.eg(EG['Clump Hair Curves'], Factor=0.45, Shape=0.3, Tip_Spread=0.003, Preserve_Length=True, Guide_Distance=0.04, Existing_Guide_Map=False, Seed=1)
else:
    grp(t, "GR Mecha Estilizada")
    grp(t, "GR Corte pela Malha", **{"Malha do corte": shell((0.145,0.15,0.13),(0,0.012,-0.03),zcut=-0.13,face=True)})
profile(t, EG, radius=0.0005)
set_mat(t, hair_mat("c", melanin=0.6, redness=0.5)); apply_tree(g, t.finish())
n,T = tips(); print("INFO", W2, "fios", n, "ponta z min cm", round(float(T[:,2].min())*100,1))
shot(f"t_lib7_{W2}", res=420, samples=16, cam_loc=(0.8,-1.1,0.35) if W2=="trolls" else (0.45,-0.60,0.08), target=(0,0,0.18) if W2=="trolls" else (0,0,-0.04), lens=38 if W2=="trolls" else 45)
