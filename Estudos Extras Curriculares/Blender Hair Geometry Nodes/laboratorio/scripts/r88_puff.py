import sys; sys.path.insert(0,'.')
V = sys.argv[-1]
sys.argv = [sys.argv[0], 'afro']
src = open('r47_styl.py').read()
src = src.replace("    sh = shell_mesh((0.17,0.175,0.16), (0,0.015,0.02), zcut=-0.11)",
"""    import bmesh as _bm
    if V == "puffs":
        sh = shell_mesh((0.075,0.075,0.075), (0.085,0.05,0.10), cut_face=False, zcut=0.04)
        s2 = shell_mesh((0.075,0.075,0.075), (-0.085,0.05,0.10), cut_face=False, zcut=0.04)
        import bpy as _b; _b.ops.object.select_all(action='DESELECT'); sh.select_set(True); s2.select_set(True); _b.context.view_layer.objects.active = sh; _b.ops.object.join()
        bpy.data.hair_curves  # noop
    elif V == "alto":
        sh = shell_mesh((0.15,0.16,0.22), (0,0.02,0.07), zcut=-0.08)
    else:
        sh = shell_mesh((0.20,0.19,0.13), (0,0.015,0.01), zcut=-0.10)""")
src = src.replace('shot(f"47_{V}"', 'shot(f"88_{_V88}"').replace("print(\"INFO\", V,", "print(\"INFO\", _V88,")
src = "V_ = None\n" + src
exec("_V88 = '%s'\n" % V + src.replace("if V.startswith(\"afro\"):", "V = _V88\nif True:").replace('if V == "puffs"', 'if _V88 == "puffs"').replace('elif V == "alto"', 'elif _V88 == "alto"'))
