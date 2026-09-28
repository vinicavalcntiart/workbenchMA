import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.6
import numpy as np
V = sys.argv[-1]   # dura | suave
reset(); EG = essentials()
head, scalp = make_head(nape=-0.7); head.data.materials.append(skin_mat()); scalp.hide_render = True
g = comb_guides(scalp, n=220, length=0.16, gravity=1.0, spread=0.25, outward=0.8, back_bias=0.9)
t = Tree("hl"); it = interp(t, EG, density=450000.0)
if V == "suave":
    # distancia ate a borda da frente do scalp: usa a normal/posicao; borda da testa ~ y=-0.055 z<0.062
    ps = t.add('GeometryNodeInputPosition'); sx = t.add('ShaderNodeSeparateXYZ'); t.link(ps.outputs[0], sx.inputs[0])
    # 1 atras, afina nos ultimos 2,5 cm antes da testa: combina Y (frente) e Z (altura) numa "distancia" aproximada
    d_ = t.add('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); t.link(sx.outputs['Z'], d_.inputs[0]); d_.inputs[1].default_value = 1.0
    ny = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sx.outputs['Y'], ny.inputs[0]); ny.inputs[1].default_value = -1.0
    t.link(ny.outputs[0], d_.inputs[2])   # d = z - y  (grande na frente-baixo)
    mr = t.add('ShaderNodeMapRange'); mr.clamp = True; t.link(d_.outputs[0], mr.inputs['Value'])
    mr.inputs['From Min'].default_value = 0.09; mr.inputs['From Max'].default_value = 0.125; mr.inputs['To Min'].default_value = 1.0; mr.inputs['To Max'].default_value = 0.08
    t.link(mr.outputs['Result'], it.inputs['Density Mask'])
t.eg(EG['Clump Hair Curves'], Factor=0.8, Shape=0.3, Tip_Spread=0.002, Preserve_Length=True, Guide_Distance=0.012, Existing_Guide_Map=False, Seed=1)
main = t.geo
if "baby" in sys.argv:
    # ramo baby: Interpolate so na faixa da borda (mascara invertida), curtos, ondulados
    it2 = t.add('GeometryNodeGroup', group=EG['Interpolate Hair Curves']); t.link(t.gi.outputs[0], it2.inputs['Geometry']); t.link(value(t, 150000.0), it2.inputs['Density'])
    b1 = t.add('ShaderNodeMapRange'); b1.clamp=True; t.link(d_.outputs[0], b1.inputs['Value']); b1.inputs['From Min'].default_value=0.112; b1.inputs['From Max'].default_value=0.124; b1.inputs['To Min'].default_value=0.0; b1.inputs['To Max'].default_value=1.0
    t.link(b1.outputs['Result'], it2.inputs['Density Mask'])
    tr = t.add('GeometryNodeGroup', group=EG['Trim Hair Curves']); tr.inputs['Replace Length'].default_value = True; tr.inputs['Length'].default_value = 0.025; tr.inputs['Random Offset'].default_value = 0.01; t.link(it2.outputs[0], tr.inputs['Geometry'])
    nz = t.add('GeometryNodeGroup', group=EG['Hair Curves Noise']); nz.inputs['Distance'].default_value = 0.004; nz.inputs['Scale'].default_value = 40.0; nz.inputs['Offset per Curve'].default_value = 1.0; nz.inputs['Preserve Length'].default_value = True; t.link(tr.outputs[0], nz.inputs['Geometry'])
    j = t.add('GeometryNodeJoinGeometry'); t.link(main, j.inputs[0]); t.link(nz.outputs[0], j.inputs[0]); t.geo = j.outputs[0]
profile(t, EG, radius=0.0004); set_mat(t, hair_mat("h", melanin=0.9, redness=0.3)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"104_{V}{'_baby' if 'baby' in sys.argv else ''}", res=420, samples=20, cam_loc=(0.05,-0.36,0.06), target=(0,-0.06,0.05), lens=50)
