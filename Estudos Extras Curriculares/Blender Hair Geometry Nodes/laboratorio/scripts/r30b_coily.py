import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
FR = dict(cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.02), lens=45)
def load():
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    return {n.name: n for n in bpy.data.node_groups}, {m.name: m for m in bpy.data.materials}
def one(label, rmin, rmax, vmin, vmax, sub=3, vol=0.03, dens=400000.0, length=0.16, clump=0.012, resample=0):
    reset(); GR, M = load(); head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    g = comb_guides(scalp, n=260, length=length, gravity=0.3, spread=0.3, outward=0.95)
    t = Tree("c")
    def grp(n, **kw):
        x = t.add('GeometryNodeGroup', group=GR[n])
        for k,v in kw.items(): x.inputs[k].default_value = v
        return t.chain(x)
    grp("GR Densidade Livre", Viewport=1.0, **{"Fios por m2":dens})
    grp("GR Mecha Estilizada", **{"Tamanho da mecha":clump})
    grp("GR Volume na Raiz", Volume=vol, **{"Sobe até":0.2})
    if resample: t.chain(t.add('GeometryNodeResampleCurve', Count=resample), 'Curve', 'Curve')
    grp("GR Cacho por Mecha", **{"Raio mín":rmin, "Raio máx":rmax, "Voltas por metro mín":vmin, "Voltas por metro máx":vmax, "Subdivisão":sub, "Começa em":0.02})
    grp("GR Cor por Mecha")
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0004; t.chain(pr)
    m = M["GR Cabelo Cor por Mecha"].copy(); nt = m.node_tree
    [n for n in nt.nodes if n.bl_idname=='ShaderNodeMapRange' and n.inputs['To Max'].default_value > 0.5][0].inputs['To Min'].default_value = 0.8
    [n for n in nt.nodes if n.bl_idname=='ShaderNodeMapRange' and n.inputs['To Max'].default_value > 0.5][0].inputs['To Max'].default_value = 0.95
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m; t.chain(sm)
    apply_tree(g, t.finish()); st = stats(g); print("INFO", label, st.get('curves'), st.get('points'))
    return shot("30b_"+label.split()[0], res=420, samples=16, **FR)
V = [("crespo Resample 200 (8 pts/volta)", dict(a=(0.0025,0.0045,110,150), sub=0, resample=200, dens=700000.0, length=0.2, clump=0.008, vol=0.02)),
     ("crespo Resample 200 + Sub 1", dict(a=(0.0025,0.0045,110,150), sub=1, resample=200, dens=700000.0, length=0.2, clump=0.008, vol=0.02))]
paths=[]; labels=[]
for lb, kw in V:
    a = kw.pop('a'); p = one(lb, *a, **kw); paths.append(p); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"30b_coily_sheet.png"), cols=2))
