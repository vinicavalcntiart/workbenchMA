import sys, os
_W, _S, _OUTF = sys.argv[-3], sys.argv[-2], sys.argv[-1]; which = _W
sys.argv = [sys.argv[0]] + (["still"] if which=="cacheada" else ["pictorico"] if which=="criatura" else ["x"])
src = open(_S).read()
# roda tudo menos o render final
cut = {"cacheada": "sc = bpy.context.scene; sc.frame_start = 1", "criatura": "shot(f\"72_", "anime": "shot(\"63_npr\""}[which]
code = src.split(cut)[0]
exec(code)
import bpy
if _W == "cacheada":
    bpy.context.scene.frame_start = 1; bpy.context.scene.frame_end = 72
if _W == "anime":
    bpy.context.scene.cycles.transparent_max_bounces = 64
from lab import stage
cam = stage(res=1080, samples=64, cam_loc=(0.42,-0.62,0.12), target=(0,-0.02,-0.03), lens=48)
bpy.context.scene.render.resolution_y = 1080
from lab import localize; localize()
bpy.ops.wm.save_as_mainfile(filepath=_OUTF, compress=True)
print("SALVO", _OUTF, os.path.getsize(_OUTF)//1024, "KB")
