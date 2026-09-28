import bpy, sys, os
f = sys.argv[-1]
bpy.ops.wm.open_mainfile(filepath=f)
sc = bpy.context.scene
libs = [l.filepath for l in bpy.data.libraries]
imgs_missing = [i.name for i in bpy.data.images if i.source=='FILE' and not os.path.exists(bpy.path.abspath(i.filepath))]
for fr in range(1, 13): sc.frame_set(fr)
dg = bpy.context.evaluated_depsgraph_get()
tot = 0
for o in sc.objects:
    if o.type == 'CURVES':
        ev = o.evaluated_get(dg); d = ev.data
        try: tot += len(d.curves)
        except Exception: pass
sc.render.resolution_x = sc.render.resolution_y = 300; sc.cycles.samples = 8
out = "/tmp/claude-0/-home-user-workbenchMA/f47732b7-f570-5d7c-a0c7-06fcea6d4438/scratchpad/lab/out/chk_" + os.path.basename(f).replace(".blend",".png")
sc.render.filepath = out; bpy.ops.render.render(write_still=True)
print("CHK", os.path.basename(f), "libs externas:", libs, "imagens faltando:", imgs_missing, "curvas avaliadas:", tot, "render ok:", os.path.exists(out))
