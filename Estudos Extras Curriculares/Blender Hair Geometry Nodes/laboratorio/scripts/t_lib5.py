import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.5
LIB = os.path.join(LAB, "receitas_grooming.blend")
paths=[]; labels=[]
for lb, extra in [("rabo baixo", dict()), ("rabo alto + Onda S", dict(tie=(0,0.085,0.07), tf=0.3, onda=True)), ("rabo baixo + Cacho", dict(cacho=True))]:
    reset()
    with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if n.startswith("GR ")]; dst.materials = list(src.materials)
    GR = {n.name:n for n in bpy.data.node_groups}; M = {m.name:m for m in bpy.data.materials}
    head, scalp = make_head(); head.data.materials.append(skin_mat()); scalp.hide_render=True
    cd = bpy.data.hair_curves.new("vazio"); g = link(bpy.data.objects.new("groom", cd)); cd.surface = scalp; cd.surface_uv_map = "UVMap"
    t = Tree("pony")
    def grp(n, out='Geometry', **kw):
        x = t.add('GeometryNodeGroup', group=GR[n])
        for k,v in kw.items(): x.inputs[k].default_value = v
        return t.chain(x, 'Geometry', out)
    grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head})
    grp("GR Densidade Livre", Viewport=1.0)
    kw = {"Cabeça (colisão)": head}
    if 'tie' in extra: kw["Amarração"] = extra['tie']; kw["Até a amarração"] = extra['tf']
    grp("GR Rabo de Cavalo", **kw)
    grp("GR Mecha Estilizada", **{"Tamanho da mecha":0.012})
    if extra.get('onda'): grp("GR Onda S", Amplitude=0.01, **{"Período":0.08, "Começa em":0.5})
    if extra.get('cacho'): grp("GR Cacho por Mecha", **{"Começa em":0.45})
    grp("GR Cor por Mecha")
    pr = t.add('GeometryNodeGroup', group=bpy.data.node_groups['Set Hair Curve Profile']); pr.inputs['Radius'].default_value=0.0005; t.chain(pr)
    m = M["GR Cabelo Cor por Mecha"]; sm = t.add('GeometryNodeSetMaterial'); sm.inputs['Material'].default_value = m; t.chain(sm)
    apply_tree(g, t.finish())
    tiep = extra.get('tie', (0,0.105,-0.01))
    bpy.ops.mesh.primitive_torus_add(major_radius=0.013, minor_radius=0.0045, location=tiep, rotation=(math.radians(70),0,0))
    em = bpy.data.materials.new("el"); em.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.75,0.1,0.12,1); bpy.context.object.data.materials.append(em)
    print("INFO", lb, stats(g).get('curves'))
    paths.append(shot("34_"+str(len(paths)), res=420, samples=16, cam_loc=(-0.5,0.5,0.0), target=(0,0.05,-0.1), lens=40)); labels.append(lb)
print("SHEET", sheet(paths, labels, os.path.join(OUT,"34_pony_lib_sheet.png"), cols=3))
