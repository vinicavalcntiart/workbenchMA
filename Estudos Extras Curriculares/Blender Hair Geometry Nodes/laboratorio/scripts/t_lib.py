import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
# checagem de sockets do Map Range vetorial
mr = bpy.data.node_groups["GR Ver em Cores"] if "GR Ver em Cores" in bpy.data.node_groups else None
def load():
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    return {n.name: n for n in bpy.data.node_groups}, {m.name: m for m in bpy.data.materials}
def scene(**gk):
    reset(); GR, M = load()
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    n = gk.pop("n_guides", 160); g = comb_guides(scalp, n=n, **gk); return GR, M, g, scalp
BACK = dict(cam_loc=(-0.40,0.55,0.05), target=(0,0,-0.07), lens=55)
cfgs = {
 "A pixar fita": dict(g=dict(length=0.30, gravity=4.0, spread=0.25, outward=0.3, n_guides=200), chain=["dens","mecha","cor","strays"], mat="GR Cabelo Cor por Mecha"),
 "B merida": dict(g=dict(length=0.24, gravity=1.8, spread=0.5, outward=0.6, n_guides=220), chain=["dens","mecha","strays","cacho","cor"], mat="GR Cabelo Cor por Mecha", red=True),
 "C onda S toon": dict(g=dict(length=0.34, gravity=4.5, spread=0.25, outward=0.3, n_guides=200), chain=["dens","mecha","onda"], mat="GR Cabelo Toon"),
 "D chunky": dict(g=dict(length=0.26, gravity=3.5, spread=0.3, outward=0.35, n_guides=200), chain=["dens_low","chunky"], mat="GR Cabelo Toon"),
}
paths=[]; labels=[]
for lb, c in cfgs.items():
    GR, M, g, scalp = scene(**c["g"])
    t = Tree("demo")
    def grp(name, **kw):
        n = t.add('GeometryNodeGroup', group=GR[name])
        for k,v in kw.items(): n.inputs[k].default_value = v
        return n
    for step in c["chain"]:
        if step=="dens": t.chain(grp("GR Densidade Livre", **{"Viewport":1.0}), 'Geometry', 'Geometry')
        if step=="dens_low": t.chain(grp("GR Densidade Livre", **{"Fios por m2":4000.0, "Viewport":1.0}), 'Geometry', 'Geometry')
        if step=="mecha":
            n = t.chain(grp("GR Mecha Estilizada"), 'Geometry', 'Geometry')
            side = grp("GR Lado da Risca"); t.link(side.outputs['Lado'], n.inputs['Group ID'])
        if step=="cor": t.chain(grp("GR Cor por Mecha"), 'Geometry', 'Geometry')
        if step=="strays": t.chain(grp("GR Strays em Arco"), 'Geometry', 'Geometry')
        if step=="cacho": t.chain(grp("GR Cacho por Mecha"), 'Geometry', 'Geometry')
        if step=="onda": t.chain(grp("GR Onda S"), 'Geometry', 'Geometry')
        if step=="chunky": t.chain(grp("GR Mecha Chunky"), 'Geometry', 'Mesh')
    if "chunky" not in c["chain"]:
        pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
    m = M[c["mat"]]
    if c.get("red"):
        m = m.copy(); m.node_tree.nodes['Principled Hair BSDF'].inputs['Melanin Redness'].default_value = 1.0
    sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m; t.chain(sm)
    apply_tree(g, t.finish())
    print("INFO", lb, stats(g))
    paths.append(shot("21_lib_"+lb.split()[0], res=480, samples=16, **BACK)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT, "21_lib_sheet.png"), cols=4))
