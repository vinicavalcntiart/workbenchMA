import bpy, bmesh, math
for n in ["Roupa_LOD0","Roupa_LOD1","Roupa_LOD2","Roupa_LOD3"]:
    o=bpy.data.objects[n]; bm=bmesh.new(); bm.from_mesh(o.data); bm.normal_update()
    bad=[]
    for f in bm.faces:
        if len(f.verts)!=4: continue
        a,b,c,d=[v.co for v in f.verts]
        n1=(b-a).cross(c-a); n2=(c-a).cross(d-a); n3=(b-a).cross(d-a); n4=(c-b).cross(d-b)
        if min(x.length for x in (n1,n2,n3,n4))<1e-12: bad.append(("degenerada",)); continue
        fold=max(math.degrees(n1.angle(n2)), math.degrees(n3.angle(n4)))
        # concavo: algum canto com angulo > 180 (n das sub-tri invertidas)
        conc = n3.dot(n4)<0 or n1.dot(n2)<0
        if fold>25 or conc: bad.append((round(fold),conc,tuple(round(x,2) for x in f.calc_center_median())))
    # dobra entre faces vizinhas
    sharp=sum(1 for e in bm.edges if len(e.link_faces)==2 and math.degrees(e.calc_face_angle())>100)
    print("RESULT",n,"quads ruins",len(bad),bad[:8],"arestas dobradas >100graus",sharp)
    bm.free()
