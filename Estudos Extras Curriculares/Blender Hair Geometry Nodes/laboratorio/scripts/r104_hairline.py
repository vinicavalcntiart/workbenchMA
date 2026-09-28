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
profile(t, EG, radius=0.0004); set_mat(t, hair_mat("h", melanin=0.9, redness=0.3)); apply_tree(g, t.finish())
print("INFO", V, stats(g).get('curves'))
shot(f"104_{V}", res=420, samples=20, cam_loc=(0.05,-0.36,0.06), target=(0,-0.06,0.05), lens=50)
