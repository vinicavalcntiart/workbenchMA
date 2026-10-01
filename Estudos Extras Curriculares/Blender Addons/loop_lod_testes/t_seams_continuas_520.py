import bpy
for o in bpy.data.objects:
    if o.type!='MESH': continue
    m=o.data; ed=[e for e in m.edges if e.use_seam]
    adj={}
    for e in ed:
        a,b=e.vertices; adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
    seen=set(); comps=0
    for v in adj:
        if v in seen: continue
        comps+=1; st=[v]
        while st:
            x=st.pop()
            if x in seen: continue
            seen.add(x); st+=adj[x]
    print("RESULT",o.name,"seam edges",len(ed),"cadeias",comps)
