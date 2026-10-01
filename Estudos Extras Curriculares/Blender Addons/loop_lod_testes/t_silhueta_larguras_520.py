import bpy, bmesh
base = None
for n in ['Robe_LOD0','Robe_LOD1','Robe_LOD2','Robe_LOD3']:
    m=bpy.data.objects[n].data; out=[]
    for z in (0.1,0.3,0.5,0.6,0.7,1.1,1.3):
        bm=bmesh.new(); bm.from_mesh(m)
        r=bmesh.ops.bisect_plane(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], plane_co=(0,0,z), plane_no=(0,0,1))
        xs=[g.co.x for g in r['geom_cut'] if isinstance(g,bmesh.types.BMVert) and abs(g.co.x)<0.5]
        ys=[g.co.y for g in r['geom_cut'] if isinstance(g,bmesh.types.BMVert) and abs(g.co.x)<0.5]
        out.append((max(xs)-min(xs), max(ys)-min(ys))); bm.free()
    if base is None: base = out
    print('RESULT', n, [(round((b[0]-o[0])*1000), round((b[1]-o[1])*1000)) for o,b in zip(out,base)])
    print('RESULT', n, 'perda maxima de largura (frente, lado) mm:', round(max((b[0]-o[0])*1000 for o,b in zip(out,base)),1), round(max((b[1]-o[1])*1000 for o,b in zip(out,base)),1))
