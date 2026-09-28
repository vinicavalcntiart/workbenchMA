import sys; sys.path.insert(0,'.')
from lab import *
def braid_scene():
    reset(); EG = essentials()
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render = True
    # uma guia na nuca, caindo 40 cm
    p0 = Vector((0, 0.094, 0.035)).normalized()*0.1004; pts=[]
    for i in range(16):
        tt=i/15; pts.append(p0 + Vector((0, 0.045*math.sin(min(tt*4,1.0)*1.57), -0.42*tt)))
    cd = bpy.data.hair_curves.new("g"); cd.add_curves([16])
    cd.attributes['position'].data.foreach_set('vector', [c for v in pts for c in v])
    g = link(bpy.data.objects.new("g", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
    return EG, g
BACK = dict(cam_loc=(-0.30,0.55,-0.15), target=(0,0.08,-0.2), lens=40)
paths=[]; labels=[]
for f, rad, ff, sh, fmin in [(1.0,0.012,0.0,0.5,0.0),(1.0,0.016,0.0,0.0,0.7),(1.2,0.018,0.05,0.0,0.75),(0.8,0.02,0.05,-0.3,0.6)]:
    EG, g = braid_scene(); t = Tree("br")
    it = t.eg(EG['Interpolate Hair Curves'], Distance_to_Guides=0.02); t.link(value(t, 4e6), it.inputs['Density'])
    t.eg(EG['Braid Hair Curves'], Factor=1.0, Subdivision=2, Braid_Start=0.12, Radius=rad, Shape=sh, Factor_Min=fmin, Factor_Max=1.0, Frequency=f,
         Flare_Length=ff, Flare_Opening=ff*0.5, Guide_Distance=0.3, Existing_Guide_Map=False)
    profile(t, EG, radius=0.0004)
    set_mat(t, hair_mat("tr", melanin=0.85, redness=0.3, roughness=0.3))
    apply_tree(g, t.finish()); st = stats(g); print("INFO", f, st.get('curves'), st.get('points'))
    paths.append(shot(f"15b_braid_{len(paths)}", res=480, samples=16, **BACK)); labels.append(f"F{f} R{rad} Shape{sh} FMin{fmin}" + (f" flare{ff}" if ff else ""))
print("SHEET", sheet(paths, labels, os.path.join(OUT,"15b_braid_sheet.png"), cols=4))
