"""Gera receitas_grooming.blend: node groups testados no laboratorio, marcados como asset."""
import sys, os; sys.path.insert(0,'.')
from lab import *
reset(); EG = essentials()

class G:
    """Construtor de node group com interface nomeada."""
    def __init__(self, name, desc):
        self.ng = bpy.data.node_groups.new(name, 'GeometryNodeTree'); self.ng.description = desc
        self.ng.is_modifier = True
        self.gi = self.ng.nodes.new('NodeGroupInput'); self.go = self.ng.nodes.new('NodeGroupOutput')
        self.gi.location=(-600,0); self.go.location=(900,0); self.x=-350; self.y=0
    def inp(self, name, typ, default=None, mn=None, mx=None, desc="", subtype=None):
        s = self.ng.interface.new_socket(name, in_out='INPUT', socket_type=typ)
        if default is not None: s.default_value = default
        if mn is not None: s.min_value = mn
        if mx is not None: s.max_value = mx
        if subtype: s.subtype = subtype
        s.description = desc; return self.gi.outputs[name]
    def out(self, name, typ, desc=""):
        s = self.ng.interface.new_socket(name, in_out='OUTPUT', socket_type=typ); s.description = desc; return self.go.inputs[name]
    def n(self, idname, group=None, props=None, **inputs):
        nd = self.ng.nodes.new(idname)
        if group is not None: nd.node_tree = group
        for k,v in (props or {}).items(): setattr(nd, k, v)
        for k,v in inputs.items(): nd.inputs[k.replace('_',' ')].default_value = v
        nd.location = (self.x, self.y); self.x += 200; return nd
    def l(self, a, b): self.ng.links.new(a, b)

def guide_id(g):
    na = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'INT'}, Name="guide_curve_index"); return na.outputs['Attribute']

libs = []

# 1. Densidade Livre
g = G("GR Densidade Livre", "Interpolate Hair Curves sem a trava de 10.000 fios/m2 do painel. Grava n_raiz (normal do scalp) para GR Volume na Raiz. Testado bpy 5.2.2.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
den = g.inp("Fios por m2", 'NodeSocketFloat', 300000.0, 0.0, 1e8, "Cabeça real (~0,05 m2): 300.000 = ~15 mil fios")
va = g.inp("Viewport", 'NodeSocketFloat', 0.25, 0.0, 1.0, "Fração na viewport. Render usa 100%", 'FACTOR')
ng_ = g.inp("Guias por fio", 'NodeSocketInt', 4, 1, 8)
dg = g.inp("Distância das guias", 'NodeSocketFloat', 0.0, 0.0, 10.0, "0 = cabeça toda. >0 só nasce fio perto da guia", 'DISTANCE')
pm = g.inp("Risca por ilhas", 'NodeSocketBool', True, desc="Part by Mesh Islands")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry'); gi_o = g.out("Guide Index", 'NodeSocketInt')
it = g.n('GeometryNodeGroup', group=EG['Interpolate Hair Curves'])
for a,b in ((geo,'Geometry'),(den,'Density'),(va,'Viewport Amount'),(ng_,'Interpolation Guides'),(dg,'Distance to Guides'),(pm,'Part by Mesh Islands'),(sd,'Seed')): g.l(a, it.inputs[b])
# guarda a normal da raiz para GR Volume na Raiz
stn = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT_VECTOR','domain':'CURVE'}, Name="n_raiz")
g.l(it.outputs['Geometry'], stn.inputs['Geometry']); g.l(it.outputs['Surface Normal'], stn.inputs['Value'])
g.l(stn.outputs['Geometry'], o); g.l(it.outputs['Guide Index'], gi_o); libs.append(g.ng)

# 2. Mecha Estilizada
g = G("GR Mecha Estilizada", "Clump com Factor em rampa ao longo do fio: mecha em fita sem careca na raiz. Shape 0 interno.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
gd = g.inp("Tamanho da mecha", 'NodeSocketFloat', 0.02, 0.0, 1.0, "Guide Distance. 0,02 = mecha de 2 cm", 'DISTANCE')
fo = g.inp("Força", 'NodeSocketFloat', 1.0, 0.0, 1.0, "", 'FACTOR')
ini = g.inp("Fecha a partir de", 'NodeSocketFloat', 0.3, 0.01, 1.0, "Fração do fio onde a mecha já está fechada. 0,15 abre buraco", 'FACTOR')
ts = g.inp("Abertura da ponta", 'NodeSocketFloat', 0.004, 0.0, 1.0, "Tip Spread", 'DISTANCE')
gid = g.inp("Group ID", 'NodeSocketInt', 0, desc="Ligue o lado da risca para a mecha nunca atravessar")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
cg = g.n('GeometryNodeGroup', group=EG['Create Guide Index Map'])
g.l(geo, cg.inputs['Geometry']); g.l(gd, cg.inputs['Guide Distance']); g.l(gid, cg.inputs['Group ID'])
sp = g.n('GeometryNodeSplineParameter'); mr = g.n('ShaderNodeMapRange'); mr.clamp = True
g.l(sp.outputs['Factor'], mr.inputs['Value']); g.l(ini, mr.inputs['From Max'])
mul = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(mr.outputs['Result'], mul.inputs[0]); g.l(fo, mul.inputs[1])
# NAO ligar Guide Index: o Clump usaria o mapa, mas gravaria guide_curve_index com o mapa proprio (Guide Distance interno).
# Existing Guide Map ligado le o atributo gravado pelo Create Guide Index Map (que respeita o Group ID).
c = g.n('GeometryNodeGroup', group=EG['Clump Hair Curves'], Shape=0.0, Preserve_Length=True, Existing_Guide_Map=True)
g.l(cg.outputs['Geometry'], c.inputs['Geometry']); g.l(gd, c.inputs['Guide Distance'])
g.l(mul.outputs[0], c.inputs['Factor']); g.l(ts, c.inputs['Tip Spread']); g.l(sd, c.inputs['Seed'])
g.l(c.outputs['Geometry'], o); libs.append(g.ng)

# 3. Cacho por Mecha
g = G("GR Cacho por Mecha", "Curl com raio e voltas sorteados por mecha (ID = guide_curve_index). Frequency interna = voltas/m / 3. Use depois do Clump.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
rmin = g.inp("Raio mín", 'NodeSocketFloat', 0.008, 0.0, 1.0, "", 'DISTANCE'); rmax = g.inp("Raio máx", 'NodeSocketFloat', 0.014, 0.0, 1.0, "", 'DISTANCE')
vmin = g.inp("Voltas por metro mín", 'NodeSocketFloat', 20.0, 0.0, 1000.0, "Merida ~30. Onda ~9"); vmax = g.inp("Voltas por metro máx", 'NodeSocketFloat', 36.0, 0.0, 1000.0)
cs = g.inp("Começa em", 'NodeSocketFloat', 0.08, 0.0, 1.0, "", 'FACTOR')
sub = g.inp("Subdivisão", "NodeSocketInt", 2, 0, 6, "2 = 45 pontos por fio, igual a 3 no render com metade da memoria. 1 quebra o cacho")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
gid_ = guide_id(g)
r1 = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(gid_, r1.inputs['ID']); g.l(rmin, r1.inputs['Min']); g.l(rmax, r1.inputs['Max']); g.l(sd, r1.inputs['Seed'])
r2 = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(gid_, r2.inputs['ID']); g.l(vmin, r2.inputs['Min']); g.l(vmax, r2.inputs['Max'])
s2 = g.n('FunctionNodeIntegerMath', props={'operation':'ADD'}); g.l(sd, s2.inputs[0]); s2.inputs[1].default_value = 7; g.l(s2.outputs[0], r2.inputs['Seed'])
d3 = g.n('ShaderNodeMath', props={'operation':'DIVIDE'}); g.l(r2.outputs['Value'], d3.inputs[0]); d3.inputs[1].default_value = 3.0
cu = g.n('GeometryNodeGroup', group=EG['Curl Hair Curves'], Factor=1.0, Random_Offset=0.25, Existing_Guide_Map=True)
g.l(geo, cu.inputs['Geometry']); g.l(r1.outputs['Value'], cu.inputs['Radius']); g.l(d3.outputs[0], cu.inputs['Frequency'])
g.l(cs, cu.inputs['Curl Start']); g.l(sub, cu.inputs['Subdivision']); g.l(sd, cu.inputs['Seed'])
g.l(cu.outputs['Geometry'], o); libs.append(g.ng)

# 4. Onda S
g = G("GR Onda S", "Onda plana de desenho: seno do comprimento, empurra na lateral do fio, fase sorteada por mecha.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
amp = g.inp("Amplitude", "NodeSocketFloat", 0.015, 0.0, 1.0, "Mantenha menor que o tamanho da mecha: acima disso mechas vizinhas se cruzam em X", "DISTANCE")
per = g.inp("Período", "NodeSocketFloat", 0.10, 0.001, 10.0, "Comprimento de uma onda", 'DISTANCE')
ini = g.inp("Começa em", 'NodeSocketFloat', 0.2, 0.001, 1.0, "", 'FACTOR')
cuts = g.inp("Subdivisão", 'NodeSocketInt', 2, 0, 10)
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
sb = g.n('GeometryNodeSubdivideCurve'); g.l(geo, sb.inputs['Curve']); g.l(cuts, sb.inputs['Cuts'])
sp = g.n('GeometryNodeSplineParameter')
tau = g.n('ShaderNodeMath', props={'operation':'DIVIDE'}); tau.inputs[0].default_value = 2*math.pi; g.l(per, tau.inputs[1])
k = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sp.outputs['Length'], k.inputs[0]); g.l(tau.outputs[0], k.inputs[1])
r = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=0.0, Max=2*math.pi); g.l(guide_id(g), r.inputs['ID']); g.l(sd, r.inputs['Seed'])
ad = g.n('ShaderNodeMath', props={'operation':'ADD'}); g.l(k.outputs[0], ad.inputs[0]); g.l(r.outputs['Value'], ad.inputs[1])
sn = g.n('ShaderNodeMath', props={'operation':'SINE'}); g.l(ad.outputs[0], sn.inputs[0])
mr = g.n('ShaderNodeMapRange'); mr.clamp=True; g.l(sp.outputs['Factor'], mr.inputs['Value']); g.l(ini, mr.inputs['From Max']); g.l(amp, mr.inputs['To Max'])
m = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sn.outputs[0], m.inputs[0]); g.l(mr.outputs['Result'], m.inputs[1])
tg = g.n('GeometryNodeInputTangent'); cr = g.n('ShaderNodeVectorMath', props={'operation':'CROSS_PRODUCT'}); cr.inputs[1].default_value=(0,0,1)
g.l(tg.outputs[0], cr.inputs[0]); nm = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(cr.outputs[0], nm.inputs[0])
sc = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nm.outputs[0], sc.inputs[0]); g.l(m.outputs[0], sc.inputs['Scale'])
spn = g.n('GeometryNodeSetPosition'); g.l(sb.outputs['Curve'], spn.inputs['Geometry']); g.l(sc.outputs[0], spn.inputs['Offset'])
g.l(spn.outputs['Geometry'], o); libs.append(g.ng)

# 5. Strays em Arco
g = G("GR Strays em Arco", "Uma fração dos fios vira arco limpo (Noise cumulativo). Coloque ANTES de Curl/Braid/Subdivide: Cumulative cresce com o número de pontos.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
fr = g.inp("Fração", 'NodeSocketFloat', 0.04, 0.0, 1.0, "0,04 estilizado. 0,12 realista", 'FACTOR')
di = g.inp("Distância", 'NodeSocketFloat', 0.04, 0.0, 10.0, "0,07 dramático", 'DISTANCE')
zz = g.inp("Zigue-zague (Frizz)", 'NodeSocketBool', False, desc="Liga Frizz em vez de arco: visual realista")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
ci = g.n('GeometryNodeGroup', group=EG['Curve Info'])
ad = g.n('ShaderNodeMath', props={'operation':'ADD'}); g.l(ci.outputs['Random'], ad.inputs[0])
# seed: desloca o random e pega a parte fracionaria
i2f = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sd, i2f.inputs[0]); i2f.inputs[1].default_value = 0.618034
g.l(i2f.outputs[0], ad.inputs[1]); fc = g.n('ShaderNodeMath', props={'operation':'FRACT'}); g.l(ad.outputs[0], fc.inputs[0])
cmp = g.n('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'LESS_THAN'}); g.l(fc.outputs[0], cmp.inputs['A']); g.l(fr, cmp.inputs['B'])
notz = g.n('FunctionNodeBooleanMath', props={'operation':'NOT'}); g.l(zz, notz.inputs[0])
a1 = g.n('FunctionNodeBooleanMath', props={'operation':'AND'}); g.l(cmp.outputs['Result'], a1.inputs[0]); g.l(notz.outputs[0], a1.inputs[1])
a2 = g.n('FunctionNodeBooleanMath', props={'operation':'AND'}); g.l(cmp.outputs['Result'], a2.inputs[0]); g.l(zz, a2.inputs[1])
nz = g.n('GeometryNodeGroup', group=EG['Hair Curves Noise'], Shape=0.7, Scale=3.0, Offset_per_Curve=1.0, Cumulative_Offset=True, Preserve_Length=True)
g.l(geo, nz.inputs['Geometry']); g.l(a1.outputs[0], nz.inputs['Factor']); g.l(di, nz.inputs['Distance']); g.l(sd, nz.inputs['Seed'])
fz = g.n('GeometryNodeGroup', group=EG['Frizz Hair Curves'], Shape=0.5, Cumulative_Offset=True, Preserve_Length=True)
g.l(nz.outputs['Geometry'], fz.inputs['Geometry']); g.l(a2.outputs[0], fz.inputs['Factor']); g.l(sd, fz.inputs['Seed'])
half = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(di, half.inputs[0]); half.inputs[1].default_value = 0.5; g.l(half.outputs[0], fz.inputs['Distance'])
g.l(fz.outputs['Geometry'], o); libs.append(g.ng)

# 6. Cor por Mecha
g = G("GR Cor por Mecha", "Grava 'mecha_rand' (0-1 por mecha, dominio Curve) para o shader. Use um Attribute 'mecha_rand' no material.")
geo = g.inp("Geometry", 'NodeSocketGeometry'); sd = g.inp("Seed", 'NodeSocketInt', 0)
nm_ = g.inp("Nome do atributo", 'NodeSocketString', "mecha_rand")
o = g.out("Geometry", 'NodeSocketGeometry')
r = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(guide_id(g), r.inputs['ID']); g.l(sd, r.inputs['Seed'])
st = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'CURVE'})
g.l(geo, st.inputs['Geometry']); g.l(nm_, st.inputs['Name']); g.l(r.outputs['Value'], st.inputs['Value'])
g.l(st.outputs['Geometry'], o); libs.append(g.ng)

# 7. Lado da Risca
g = G("GR Lado da Risca", "Inteiro 0/1 pelo lado da raiz em X. Ligue no Group ID da GR Mecha Estilizada para a risca ficar seca.")
off = g.inp("Posição da risca X", 'NodeSocketFloat', 0.0, -10.0, 10.0, "", 'DISTANCE')
o = g.out("Lado", 'NodeSocketInt')
rt = g.n('GeometryNodeGroup', group=EG['Curve Root']); sx = g.n('ShaderNodeSeparateXYZ'); g.l(rt.outputs['Root Position'], sx.inputs[0])
cmp = g.n('FunctionNodeCompare', props={'data_type':'FLOAT','operation':'GREATER_THAN'}); g.l(sx.outputs['X'], cmp.inputs['A']); g.l(off, cmp.inputs['B'])
g.l(cmp.outputs['Result'], o); libs.append(g.ng)

# 8. Mecha Chunky
g = G("GR Mecha Chunky", "Fios viram malha de fita achatada e torcida por mecha. Raio do fio ligado no Scale do Curve to Mesh (5.2).")
geo = g.inp("Geometry", 'NodeSocketGeometry')
rad = g.inp("Raio", 'NodeSocketFloat', 0.005, 0.0, 1.0, "", 'DISTANCE')
fl = g.inp("Achatamento", 'NodeSocketFloat', 0.35, 0.01, 1.0, "1 = tubo redondo", 'FACTOR')
tw = g.inp("Torção máx (voltas)", 'NodeSocketFloat', 0.5, 0.0, 10.0)
res = g.inp("Pontos por mecha", 'NodeSocketInt', 24, 2, 500)
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Mesh", 'NodeSocketGeometry')
rs = g.n('GeometryNodeResampleCurve'); g.l(geo, rs.inputs['Curve']); g.l(res, rs.inputs['Count'])
pr = g.n('GeometryNodeGroup', group=EG['Set Hair Curve Profile'], Shape=0.3, Factor_Min=0.0, Factor_Max=1.0)
g.l(rs.outputs['Curve'], pr.inputs['Geometry']); g.l(rad, pr.inputs['Radius'])
spp = g.n('GeometryNodeSplineParameter')
tv = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(tw, tv.inputs[0]); tv.inputs[1].default_value = 2*math.pi
ng2 = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(tv.outputs[0], ng2.inputs[0]); ng2.inputs[1].default_value = -1.0
r = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(ng2.outputs[0], r.inputs['Min']); g.l(tv.outputs[0], r.inputs['Max']); g.l(sd, r.inputs['Seed'])
ev = g.n('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); g.l(r.outputs['Value'], ev.inputs[0])
mm = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(spp.outputs['Factor'], mm.inputs[0]); g.l(ev.outputs[0], mm.inputs[1])
tl = g.n('GeometryNodeSetCurveTilt'); g.l(pr.outputs['Geometry'], tl.inputs['Curve']); g.l(mm.outputs[0], tl.inputs['Tilt'])
ci = g.n('GeometryNodeCurvePrimitiveCircle', Resolution=10, Radius=1.0)
cx = g.n('ShaderNodeCombineXYZ', X=1.0, Z=1.0); g.l(fl, cx.inputs['Y'])
tr = g.n('GeometryNodeTransform'); g.l(ci.outputs['Curve'], tr.inputs['Geometry']); g.l(cx.outputs[0], tr.inputs['Scale'])
cm = g.n('GeometryNodeCurveToMesh', Fill_Caps=True); g.l(tl.outputs['Curve'], cm.inputs['Curve']); g.l(tr.outputs['Geometry'], cm.inputs['Profile Curve'])
rr = g.n('GeometryNodeInputRadius'); g.l(rr.outputs[0], cm.inputs['Scale'])
ss = g.n('GeometryNodeSetShadeSmooth'); g.l(cm.outputs['Mesh'], ss.inputs['Geometry'])
g.l(ss.outputs['Geometry'], o); libs.append(g.ng)

# 9. Ver em Cores
g = G("GR Ver em Cores", "Float 0-1 vira cor azul->vermelho para o Viewer (Ctrl+Shift+clique).")
g.ng.is_modifier = False
v = g.inp("Valor", 'NodeSocketFloat', 0.0, -1e9, 1e9); mn = g.inp("Mín", 'NodeSocketFloat', 0.0); mx = g.inp("Máx", 'NodeSocketFloat', 1.0)
o = g.out("Cor", 'NodeSocketColor')
mr = g.n('ShaderNodeMapRange', props={'data_type':'FLOAT_VECTOR'}); mr.clamp = True
g.l(v, mr.inputs['Vector']); 
mr.inputs[9].default_value = (0,0,1)  # To Min vetor
mr.inputs[10].default_value = (1,0,0) # To Max vetor
cmn = g.n('ShaderNodeCombineXYZ'); g.l(mn, cmn.inputs['X']); g.l(mn, cmn.inputs['Y']); g.l(mn, cmn.inputs['Z'])
cmx = g.n('ShaderNodeCombineXYZ'); g.l(mx, cmx.inputs['X']); g.l(mx, cmx.inputs['Y']); g.l(mx, cmx.inputs['Z'])
g.l(cmn.outputs[0], mr.inputs[7]); g.l(cmx.outputs[0], mr.inputs[8])
g.l(mr.outputs['Vector'], o); libs.append(g.ng)


# 10. Ponta Virada
g = G("GR Ponta Virada", "Roll com a direcao radial: ponta vira para fora (flip) ou para dentro. Roll Direction do Essentials e 'para onde enrola', nao eixo.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
fora = g.inp("Para fora", 'NodeSocketBool', False, desc="Ligado = flip anos 60. Desligado = ponta para dentro")
rl = g.inp("Comprimento do rolo", 'NodeSocketFloat', 0.06, 0.0, 10.0, "", 'DISTANCE')
rr = g.inp("Raio do rolo", 'NodeSocketFloat', 0.02, 0.0, 10.0, "", 'DISTANCE')
var = g.inp("Variação por mecha", 'NodeSocketFloat', 0.4, 0.0, 1.0, "0,4 = comprimento entre 60% e 140%", 'FACTOR')
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
rt = g.n('GeometryNodeGroup', group=EG['Curve Root'])
sw = g.n('GeometryNodeSwitch', props={'input_type':'FLOAT'}); sw.inputs['False'].default_value = -1.0; sw.inputs['True'].default_value = 1.0; g.l(fora, sw.inputs['Switch'])
sc = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(rt.outputs['Root Position'], sc.inputs[0]); g.l(sw.outputs[0], sc.inputs['Scale'])
lo = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); lo.inputs[0].default_value = 1.0; g.l(var, lo.inputs[1])
hi = g.n('ShaderNodeMath', props={'operation':'ADD'}); hi.inputs[0].default_value = 1.0; g.l(var, hi.inputs[1])
r = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(guide_id(g), r.inputs['ID']); g.l(lo.outputs[0], r.inputs['Min']); g.l(hi.outputs[0], r.inputs['Max']); g.l(sd, r.inputs['Seed'])
ml = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(r.outputs['Value'], ml.inputs[0]); g.l(rl, ml.inputs[1])
ro = g.n('GeometryNodeGroup', group=EG['Roll Hair Curves'], Factor=1.0, Subdivision=2, Random_Orientation=0.0, Preserve_Length=True)
g.l(geo, ro.inputs['Geometry']); g.l(sc.outputs[0], ro.inputs['Roll Direction']); g.l(ml.outputs[0], ro.inputs['Roll Length']); g.l(rr, ro.inputs['Roll Radius']); g.l(sd, ro.inputs['Seed'])
g.l(ro.outputs['Geometry'], o); libs.append(g.ng)

# 11. Tranca Grossa
g = G("GR Trança Grossa", "Braid com raio constante (Shape 0, Factor Min 0,7). Use depois de um Interpolate com Distance to Guides ~0,02: uma tranca por guia.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
rad = g.inp("Raio", 'NodeSocketFloat', 0.016, 0.0, 1.0, "", 'DISTANCE')
fq = g.inp("Cruzamentos", 'NodeSocketFloat', 1.0, 0.0, 100.0, "Frequency: 2 = fechada, 0,5 = solta")
ini = g.inp("Começa em", 'NodeSocketFloat', 0.12, 0.0, 1.0, "", 'FACTOR')
fmin = g.inp("Espessura na ponta", 'NodeSocketFloat', 0.7, 0.0, 10.0, "Factor Min. 0 afina ate sumir")
o = g.out("Geometry", 'NodeSocketGeometry')
br = g.n('GeometryNodeGroup', group=EG['Braid Hair Curves'], Factor=1.0, Subdivision=2, Shape=0.0, Factor_Max=1.0, Guide_Distance=0.3, Existing_Guide_Map=False)
g.l(geo, br.inputs['Geometry']); g.l(rad, br.inputs['Radius']); g.l(fq, br.inputs['Frequency']); g.l(ini, br.inputs['Braid Start']); g.l(fmin, br.inputs['Factor Min'])
g.l(br.outputs['Geometry'], o); libs.append(g.ng)

# 12. Corte por Regiao
g = G("GR Corte por Região", "Encurta onde o vertex group do scalp vale 0 e desliga o clump ali. Vertex group chega nos fios como atributo de Curve.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
vg = g.inp("Vertex group (1 = longo)", 'NodeSocketString', "topo")
ln = g.inp("Comprimento curto", 'NodeSocketFloat', 0.025, 0.0, 10.0, "", 'DISTANCE')
gd = g.inp("Tamanho da mecha", 'NodeSocketFloat', 0.02, 0.0, 1.0, "", 'DISTANCE')
sh = g.inp("Shape do clump", 'NodeSocketFloat', 0.25, -1.0, 1.0)
o = g.out("Geometry", 'NodeSocketGeometry')
na = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}); g.l(vg, na.inputs['Name'])
inv = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); inv.inputs[0].default_value = 1.0; g.l(na.outputs['Attribute'], inv.inputs[1])
tr = g.n('GeometryNodeGroup', group=EG['Trim Hair Curves'], Replace_Length=True, Scale_Uniform=False, Random_Offset=0.004)
g.l(geo, tr.inputs['Geometry']); g.l(ln, tr.inputs['Length']); g.l(inv.outputs[0], tr.inputs['Mask'])
cl = g.n('GeometryNodeGroup', group=EG['Clump Hair Curves'], Tip_Spread=0.002, Preserve_Length=True, Existing_Guide_Map=False)
g.l(tr.outputs['Geometry'], cl.inputs['Geometry']); g.l(na.outputs['Attribute'], cl.inputs['Factor']); g.l(gd, cl.inputs['Guide Distance']); g.l(sh, cl.inputs['Shape'])
g.l(cl.outputs['Geometry'], o); libs.append(g.ng)

# 13. Pelo em Tufos
g = G("GR Pelo em Tufos", "Pelo estilizado de personagem: Interpolate denso + Clump pequeno Shape 0,25. Opcional subpelo e pelo de guarda.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
den = g.inp("Fios por m2", 'NodeSocketFloat', 1.5e6, 0.0, 1e9)
va = g.inp("Viewport", 'NodeSocketFloat', 0.2, 0.0, 1.0, "", 'FACTOR')
td = g.inp("Tamanho do tufo", 'NodeSocketFloat', 0.008, 0.0, 1.0, "", 'DISTANCE')
rad = g.inp("Raio do fio", 'NodeSocketFloat', 0.0003, 0.0, 1.0, "", 'DISTANCE')
sub = g.inp("Subpelo", 'NodeSocketBool', False, desc="Camada curta (45%) sem clump, 2x densidade")
gua = g.inp("Pelo de guarda", 'NodeSocketBool', False, desc="Poucos fios 1,4x mais longos e 3x mais grossos")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
def interp_node(dmul, seed_off):
    it = g.n('GeometryNodeGroup', group=EG['Interpolate Hair Curves']); g.l(geo, it.inputs['Geometry']); g.l(va, it.inputs['Viewport Amount'])
    m = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(den, m.inputs[0]); m.inputs[1].default_value = dmul; g.l(m.outputs[0], it.inputs['Density'])
    a = g.n('FunctionNodeIntegerMath', props={'operation':'ADD'}); g.l(sd, a.inputs[0]); a.inputs[1].default_value = seed_off; g.l(a.outputs[0], it.inputs['Seed'])
    return it
def prof(src, rmul):
    p = g.n('GeometryNodeGroup', group=EG['Set Hair Curve Profile'], Shape=0.5, Factor_Min=0.0, Factor_Max=1.0); g.l(src, p.inputs['Geometry'])
    m = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(rad, m.inputs[0]); m.inputs[1].default_value = rmul; g.l(m.outputs[0], p.inputs['Radius']); return p.outputs['Geometry']
top = interp_node(1.0, 0)
cl = g.n('GeometryNodeGroup', group=EG['Clump Hair Curves'], Factor=1.0, Shape=0.25, Tip_Spread=0.001, Preserve_Length=True, Existing_Guide_Map=False)
g.l(top.outputs['Geometry'], cl.inputs['Geometry']); g.l(td, cl.inputs['Guide Distance']); g.l(sd, cl.inputs['Seed'])
top_o = prof(cl.outputs['Geometry'], 1.0)
un = interp_node(2.0, 11)
ut = g.n('GeometryNodeGroup', group=EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=0.45, Scale_Uniform=True, Random_Offset=0.2); g.l(un.outputs['Geometry'], ut.inputs['Geometry'])
un_o = prof(ut.outputs['Geometry'], 0.5)
gu = interp_node(0.02, 23)
gt = g.n('GeometryNodeGroup', group=EG['Trim Hair Curves'], Replace_Length=False, Length_Factor=1.4, Scale_Uniform=True); g.l(gu.outputs['Geometry'], gt.inputs['Geometry'])
gu_o = prof(gt.outputs['Geometry'], 3.0)
e = g.n('GeometryNodeGeometryToInstance')  # placeholder removido abaixo
g.ng.nodes.remove(e)
s1 = g.n('GeometryNodeSwitch', props={'input_type':'GEOMETRY'}); g.l(sub, s1.inputs['Switch']); g.l(un_o, s1.inputs['True'])
s2 = g.n('GeometryNodeSwitch', props={'input_type':'GEOMETRY'}); g.l(gua, s2.inputs['Switch']); g.l(gu_o, s2.inputs['True'])
j = g.n('GeometryNodeJoinGeometry'); g.l(s2.outputs[0], j.inputs[0]); g.l(top_o, j.inputs[0]); g.l(s1.outputs[0], j.inputs[0])
g.l(j.outputs[0], o); libs.append(g.ng)


# 14. Volume na Raiz
g = G("GR Volume na Raiz", "Empurra o fio pela normal do scalp (atributo n_raiz da GR Densidade Livre), raiz parada. 3 cm + rampa 0,15 = topete.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
vol = g.inp("Volume", 'NodeSocketFloat', 0.015, -1.0, 1.0, "Distancia maxima do empurrao", 'DISTANCE')
rp = g.inp("Sobe até", 'NodeSocketFloat', 0.3, 0.001, 1.0, "Fracao do fio onde o volume ja e total. Menor = mais topete", 'FACTOR')
o = g.out("Geometry", 'NodeSocketGeometry')
n = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="n_raiz")
sp = g.n('GeometryNodeSplineParameter'); mr = g.n('ShaderNodeMapRange'); mr.clamp = True
g.l(sp.outputs['Factor'], mr.inputs['Value']); g.l(rp, mr.inputs['From Max']); g.l(vol, mr.inputs['To Max'])
sc = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(n.outputs['Attribute'], sc.inputs[0]); g.l(mr.outputs['Result'], sc.inputs['Scale'])
spn = g.n('GeometryNodeSetPosition'); g.l(geo, spn.inputs['Geometry']); g.l(sc.outputs[0], spn.inputs['Offset'])
g.l(spn.outputs['Geometry'], o); libs.append(g.ng)


# 15. Mascara por Imagem
g = G("GR Máscara por Imagem", "Apaga fios onde a imagem e preta, lendo o UV da raiz (surface_uv_coordinate). Depois do Interpolate; a cor pode passar por qualquer cadeia antes.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
img = g.inp("Imagem", 'NodeSocketImage')
inv = g.inp("Inverter", 'NodeSocketBool', False, desc="Ligado: apaga onde e branco")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry'); vo = g.out("Valor da imagem", 'NodeSocketFloat', "Cinza da imagem na raiz de cada fio: reuse em Trim, Clump, Curl")
na = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="surface_uv_coordinate")
tx = g.n('GeometryNodeImageTexture'); g.l(img, tx.inputs['Image']); g.l(na.outputs['Attribute'], tx.inputs['Vector'])
sw = g.n('GeometryNodeSwitch', props={'input_type':'FLOAT'}); g.l(inv, sw.inputs['Switch']); g.l(tx.outputs['Color'], sw.inputs['False'])
one = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); one.inputs[0].default_value = 1.0; g.l(tx.outputs['Color'], one.inputs[1]); g.l(one.outputs[0], sw.inputs['True'])
rv = g.n('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); g.l(sw.outputs[0], rv.inputs['Probability']); g.l(sd, rv.inputs['Seed'])
nt = g.n('FunctionNodeBooleanMath', props={'operation':'NOT'}); g.l(rv.outputs[3] if len(rv.outputs)>3 else rv.outputs[0], nt.inputs[0])
dl = g.n('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); g.l(geo, dl.inputs['Geometry']); g.l(nt.outputs[0], dl.inputs['Selection'])
g.l(dl.outputs['Geometry'], o); g.l(sw.outputs[0], vo); libs.append(g.ng)

# 16. Fisica Estilizada
DYN = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','geometry_nodes_dynamics_assets.blend')
with bpy.data.libraries.load(DYN, link=False) as (src, dst): dst.node_groups = ['Hair Dynamics','Custom Force']
HD = bpy.data.node_groups['Hair Dynamics']
g = G("GR Física Estilizada", "Hair Dynamics nas GUIAS com valores que seguram penteado estilizado (Bendiness 0, Root 0, Substeps 40). Guias precisam de Snap to Nearest Surface. Coloque ANTES do Interpolate.")
geo = g.inp("Guias", 'NodeSocketGeometry')
mov = g.inp("Movimento", 'NodeSocketFloat', 0.0, 0.0, 1.0, "Bendiness. 0 segura a forma; 0,5 balanca", 'FACTOR')
raiz = g.inp("Raiz solta", 'NodeSocketFloat', 0.0, 0.0, 1.0, "Root Bendiness", 'FACTOR')
sub = g.inp("Substeps", 'NodeSocketInt', 40, 1, 200, "40 segura o penteado (queda 1,5 cm). 10 = padrao, desaba")
grav = g.inp("Gravidade", 'NodeSocketFloat', 1.0, 0.0, 2.0, "Multiplica 9,81 m/s2", 'FACTOR')
col = g.inp("Colisores", 'NodeSocketCollection', desc="Colecao com objetos que tem o modificador Collider (ex.: a cabeca inteira). Nao use Surface Collision no scalp: explode.")
vf = g.inp("Vento", 'NodeSocketFloat', 0.0, 0.0, 2.0, "Forca do vento. 0,04 brisa; 0,12 vento de cena (fio 30 cm)")
vd = g.inp("Direção do vento", 'NodeSocketVector', (1.0,0.0,0.0), desc="Para onde o vento sopra")
o = g.out("Guias", 'NodeSocketGeometry')
hd = g.n('GeometryNodeGroup', group=HD)
hd.inputs['Mode'].default_value = 'Physics (Experimental)'
g.l(geo, hd.inputs['Hair']); g.l(mov, hd.inputs['Bendiness']); g.l(raiz, hd.inputs['Root Bendiness']); g.l(sub, hd.inputs['Substeps']); g.l(col, hd.inputs['Effectors Collection'])
gm = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); gm.inputs[0].default_value = (0,0,-9.81); g.l(grav, gm.inputs['Scale'])
for s_ in hd.inputs:
    if s_.name == 'Gravity' and s_.type == 'VECTOR': g.l(gm.outputs[0], s_)
# vento: rajada seno 1,5 s (20-100%) + turbulencia Noise 4D -> Custom Force -> Effectors
stt = g.n('GeometryNodeInputSceneTime')
w1 = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(stt.outputs['Seconds'], w1.inputs[0]); w1.inputs[1].default_value = 2*math.pi/1.5
sn = g.n('ShaderNodeMath', props={'operation':'SINE'}); g.l(w1.outputs[0], sn.inputs[0])
gu = g.n('ShaderNodeMath', props={'operation':'MULTIPLY_ADD'}); g.l(sn.outputs[0], gu.inputs[0]); gu.inputs[1].default_value = 0.4; gu.inputs[2].default_value = 0.6
fz = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(gu.outputs[0], fz.inputs[0]); g.l(vf, fz.inputs[1])
nd = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(vd, nd.inputs[0])
bs = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nd.outputs[0], bs.inputs[0]); g.l(fz.outputs[0], bs.inputs['Scale'])
ps = g.n('GeometryNodeInputPosition')
nz = g.n('ShaderNodeTexNoise'); nz.noise_dimensions = '4D'; nz.inputs['Scale'].default_value = 15.0; nz.inputs['Detail'].default_value = 1.0
g.l(ps.outputs[0], nz.inputs['Vector']); g.l(stt.outputs['Seconds'], nz.inputs['W'])
ce = g.n('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); g.l(nz.outputs['Color'], ce.inputs[0]); ce.inputs[1].default_value = (0.5,0.5,0.5)
tk = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(vf, tk.inputs[0]); tk.inputs[1].default_value = 1.2
tb = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(ce.outputs[0], tb.inputs[0]); g.l(tk.outputs[0], tb.inputs['Scale'])
fv = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(bs.outputs[0], fv.inputs[0]); g.l(tb.outputs[0], fv.inputs[1])
cf = g.n('GeometryNodeGroup', group=bpy.data.node_groups['Custom Force']); g.l(fv.outputs[0], cf.inputs['Force'])
g.l(cf.outputs['Force'], [x for x in hd.inputs if x.name=='Effectors' and x.type=='BUNDLE'][0])
g.l(hd.outputs['Hair'], o); libs.append(g.ng)


# 17. Guias Procedurais
g = G("GR Guias Procedurais", "Gera guias penteadas sem esculpir: Generate Hair Curves + parabola (para fora, lado da risca, para tras, gravidade) + Shrinkwrap. Use num objeto Curves vazio com Surface; depois ligue a cadeia normal.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
cab = g.inp("Cabeça (colisão)", 'NodeSocketObject', desc="Objeto da cabeca inteira para o Shrinkwrap")
L = g.inp("Comprimento", 'NodeSocketFloat', 0.22, 0.0, 10.0, "", 'DISTANCE')
outw = g.inp("Para fora", 'NodeSocketFloat', 0.4, 0.0, 3.0, "0,4 cai rente; 0,8 volume; 1,2 espetado")
lado = g.inp("Para o lado da risca", 'NodeSocketFloat', 0.35, -2.0, 2.0)
tras = g.inp("Para trás", 'NodeSocketFloat', 0.2, -2.0, 2.0)
grav = g.inp("Gravidade", 'NodeSocketFloat', 1.2, 0.0, 10.0, "1,2 bob; 2,2 longo caido; 0 espetado")
risca = g.inp("Risca X", 'NodeSocketFloat', 0.0, -10.0, 10.0, "", 'DISTANCE')
dens = g.inp("Guias por m2", 'NodeSocketFloat', 4000.0, 0.0, 1e6, "4000 ~ 200 guias numa cabeca real")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Guias", 'NodeSocketGeometry')
gen = g.n('GeometryNodeGroup', group=EG['Generate Hair Curves'])
gen.inputs['Control Points'].default_value = 12; gen.inputs['Distribution Method'].default_value = 'Poisson Disk'
g.l(geo, gen.inputs['Hair Surface']); g.l(L, gen.inputs['Hair Length']); g.l(dens, gen.inputs['Density']); g.l(sd, gen.inputs['Seed'])
sp = g.n('GeometryNodeSplineParameter'); rt = g.n('GeometryNodeGroup', group=EG['Curve Root'])
sx = g.n('ShaderNodeSeparateXYZ'); g.l(rt.outputs['Root Position'], sx.inputs[0])
dx = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); g.l(sx.outputs['X'], dx.inputs[0]); g.l(risca, dx.inputs[1])
sg = g.n('ShaderNodeMath', props={'operation':'SIGN'}); g.l(dx.outputs[0], sg.inputs[0])
sl = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sg.outputs[0], sl.inputs[0]); g.l(lado, sl.inputs[1])
dirv = g.n('ShaderNodeCombineXYZ'); g.l(sl.outputs[0], dirv.inputs['X']); g.l(tras, dirv.inputs['Y'])
om1 = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); g.l(outw, om1.inputs[0]); om1.inputs[1].default_value = 1.0
nn = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(gen.outputs['Surface Normal'], nn.inputs[0]); g.l(om1.outputs[0], nn.inputs['Scale'])
a1 = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(nn.outputs[0], a1.inputs[0]); g.l(dirv.outputs[0], a1.inputs[1])
lt = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sp.outputs['Factor'], lt.inputs[0]); g.l(L, lt.inputs[1])
lin = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(a1.outputs[0], lin.inputs[0]); g.l(lt.outputs[0], lin.inputs['Scale'])
t2 = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sp.outputs['Factor'], t2.inputs[0]); g.l(sp.outputs['Factor'], t2.inputs[1])
gl_ = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(grav, gl_.inputs[0]); g.l(L, gl_.inputs[1])
gz = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(t2.outputs[0], gz.inputs[0]); g.l(gl_.outputs[0], gz.inputs[1])
ng_ = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(gz.outputs[0], ng_.inputs[0]); ng_.inputs[1].default_value = -1.0
gv = g.n('ShaderNodeCombineXYZ'); g.l(ng_.outputs[0], gv.inputs['Z'])
off = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(lin.outputs[0], off.inputs[0]); g.l(gv.outputs[0], off.inputs[1])
spn = g.n('GeometryNodeSetPosition'); g.l(gen.outputs['Geometry'], spn.inputs['Geometry']); g.l(off.outputs[0], spn.inputs['Offset'])
w = g.n('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.006, Above_Surface=0.0, Smoothing_Steps=3, Lock_Roots=True)
g.l(spn.outputs['Geometry'], w.inputs['Geometry'])
for x in w.inputs:
    if x.name == 'Surface' and x.type == 'OBJECT': g.l(cab, x)
g.l(w.outputs['Geometry'], o); libs.append(g.ng)


# 18. Rabo de Cavalo
g = G("GR Rabo de Cavalo", "Reposiciona cada fio: da raiz ate o ponto de amarracao (colado no cranio pelo Shrinkwrap) e dali cai abrindo. Use depois da GR Densidade Livre; a forma das guias nao importa.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
cab = g.inp("Cabeça (colisão)", 'NodeSocketObject')
tie = g.inp("Amarração", 'NodeSocketVector', (0.0, 0.105, -0.01), desc="Ponto do elastico, em coordenadas do objeto", subtype='TRANSLATION')
tf = g.inp("Até a amarração", 'NodeSocketFloat', 0.35, 0.05, 0.95, "Fracao do fio gasta ate o elastico", 'FACTOR')
cl = g.inp("Comprimento da cauda", 'NodeSocketFloat', 0.26, 0.0, 10.0, "", 'DISTANCE')
ab = g.inp("Abertura", 'NodeSocketFloat', 0.03, 0.0, 1.0, "Quanto a cauda abre na ponta", 'DISTANCE')
tr = g.inp("Para trás", 'NodeSocketFloat', 0.25, -2.0, 2.0)
pts = g.inp("Pontos por fio", 'NodeSocketInt', 24, 4, 500)
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
rs = g.n('GeometryNodeResampleCurve'); g.l(geo, rs.inputs['Curve']); g.l(pts, rs.inputs['Count'])
sp = g.n('GeometryNodeSplineParameter'); rt = g.n('GeometryNodeGroup', group=EG['Curve Root'])
a = g.n('ShaderNodeMapRange'); a.clamp=True; g.l(sp.outputs['Factor'], a.inputs['Value']); g.l(tf, a.inputs['From Max'])
b = g.n('ShaderNodeMapRange'); b.clamp=True; g.l(sp.outputs['Factor'], b.inputs['Value']); g.l(tf, b.inputs['From Min'])
mx = g.n('ShaderNodeMix', props={'data_type':'VECTOR'}); g.l(a.outputs['Result'], mx.inputs['Factor']); g.l(rt.outputs['Root Position'], mx.inputs[4]); g.l(tie, mx.inputs[5])
dv = g.n('ShaderNodeCombineXYZ'); dv.inputs['Z'].default_value = -1.0; g.l(tr, dv.inputs['Y'])
dn = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(dv.outputs[0], dn.inputs[0])
bl = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(b.outputs['Result'], bl.inputs[0]); g.l(cl, bl.inputs[1])
drop = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(dn.outputs[0], drop.inputs[0]); g.l(bl.outputs[0], drop.inputs['Scale'])
r = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT_VECTOR'}, Min=(-1,-1,-0.3), Max=(1,1,0.3)); g.l(sd, r.inputs['Seed'])
ev = g.n('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT_VECTOR'}); g.l(r.outputs['Value'], ev.inputs[0])
ab2 = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(b.outputs['Result'], ab2.inputs[0]); g.l(ab, ab2.inputs[1])
sprd = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(ev.outputs[0], sprd.inputs[0]); g.l(ab2.outputs[0], sprd.inputs['Scale'])
t1 = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(mx.outputs[1], t1.inputs[0]); g.l(drop.outputs[0], t1.inputs[1])
t2 = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(t1.outputs[0], t2.inputs[0]); g.l(sprd.outputs[0], t2.inputs[1])
spn = g.n('GeometryNodeSetPosition'); g.l(rs.outputs['Curve'], spn.inputs['Geometry']); g.l(t2.outputs[0], spn.inputs['Position'])
w = g.n('GeometryNodeGroup', group=EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
g.l(spn.outputs['Geometry'], w.inputs['Geometry'])
for x in w.inputs:
    if x.name == 'Surface' and x.type == 'OBJECT': g.l(cab, x)
g.l(w.outputs['Geometry'], o); libs.append(g.ng)

# 19. Forma por Malha
g = G("GR Forma por Malha", "Puxa as guias para a superficie de uma malha simples (o 'capacete' da silhueta). A partir de 'Cola a partir de' o fio fica na malha. Use nas GUIAS, antes do Interpolate.")
geo = g.inp("Guias", 'NodeSocketGeometry')
mal = g.inp("Malha da forma", 'NodeSocketObject', desc="Malha aberta em volta da cabeca (esfera deformada, sem a parte do rosto)")
fo = g.inp("Força", 'NodeSocketFloat', 1.0, 0.0, 1.0, "", 'FACTOR')
cl = g.inp("Cola a partir de", 'NodeSocketFloat', 0.35, 0.01, 1.0, "Fracao do fio onde ele ja esta colado na malha", 'FACTOR')
o = g.out("Guias", 'NodeSocketGeometry')
oi = g.n('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); g.l(mal, oi.inputs['Object'])
gp = g.n('GeometryNodeProximity', props={'target_element':'FACES'}); g.l(oi.outputs['Geometry'], gp.inputs[0])
sp = g.n('GeometryNodeSplineParameter')
mr = g.n('ShaderNodeMapRange'); mr.clamp = True; g.l(sp.outputs['Factor'], mr.inputs['Value']); g.l(cl, mr.inputs['From Max']); g.l(fo, mr.inputs['To Max'])
ps = g.n('GeometryNodeInputPosition')
mx = g.n('ShaderNodeMix', props={'data_type':'VECTOR'}); g.l(mr.outputs['Result'], mx.inputs[0]); g.l(ps.outputs[0], mx.inputs[4]); g.l(gp.outputs['Position'], mx.inputs[5])
st = g.n('GeometryNodeSetPosition'); g.l(geo, st.inputs['Geometry']); g.l(mx.outputs[1], st.inputs['Position'])
g.l(st.outputs['Geometry'], o); libs.append(g.ng)

# 20. Crescer
g = G("GR Crescer", "Animacao: cada mecha cresce pelo caminho final com atraso sorteado. Coloque no fim, antes do Set Hair Curve Profile. Precisa de guide_curve_index (Clump antes).")
geo = g.inp("Geometry", 'NodeSocketGeometry')
vel = g.inp("Velocidade", 'NodeSocketFloat', 0.8, 0.0, 100.0, "Comprimento por segundo (1 = fio inteiro em 1 s)")
at = g.inp("Atraso por mecha", 'NodeSocketFloat', 0.4, 0.0, 10.0, "Segundos x velocidade de diferenca entre mechas")
sd = g.inp("Seed", 'NodeSocketInt', 0)
o = g.out("Geometry", 'NodeSocketGeometry')
stt = g.n('GeometryNodeInputSceneTime')
rv = g.n('FunctionNodeRandomValue', props={'data_type':'FLOAT'}); g.l(guide_id(g), rv.inputs['ID']); g.l(at, rv.inputs['Max']); g.l(sd, rv.inputs['Seed'])
ev = g.n('GeometryNodeFieldOnDomain', props={'domain':'CURVE','data_type':'FLOAT'}); g.l(rv.outputs['Value'], ev.inputs[0])
mu = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(stt.outputs['Seconds'], mu.inputs[0]); g.l(vel, mu.inputs[1])
su = g.n('ShaderNodeMath', props={'operation':'SUBTRACT'}); g.l(mu.outputs[0], su.inputs[0]); g.l(ev.outputs[0], su.inputs[1])
cp = g.n('ShaderNodeClamp'); g.l(su.outputs[0], cp.inputs['Value']); cp.inputs['Min'].default_value = 0.02
tr = g.n('GeometryNodeGroup', group=EG['Trim Hair Curves'], Replace_Length=False, Scale_Uniform=False)
g.l(geo, tr.inputs['Geometry']); g.l(cp.outputs[0], tr.inputs['Length Factor'])
g.l(tr.outputs['Geometry'], o); libs.append(g.ng)

# 21. LOD por Camera
g = G("GR LOD por Câmera", "Multidao: apaga fios longe da camera e engrossa os que ficam (raio x 1/raiz da fracao). Coloque no fim, depois do Set Hair Curve Profile.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
cam = g.inp("Câmera", 'NodeSocketObject')
pe = g.inp("Perto", 'NodeSocketFloat', 1.0, 0.0, 1e4, "Ate aqui, 100% dos fios", 'DISTANCE')
lo = g.inp("Longe", 'NodeSocketFloat', 8.0, 0.0, 1e4, "Daqui em diante, o minimo", 'DISTANCE')
mi = g.inp("Mínimo", 'NodeSocketFloat', 0.04, 0.001, 1.0, "Fracao que fica longe", 'FACTOR')
o = g.out("Geometry", 'NodeSocketGeometry')
oi = g.n('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); g.l(cam, oi.inputs['Object'])
cr = g.n('GeometryNodeGroup', group=EG['Curve Root'])
di = g.n('ShaderNodeVectorMath', props={'operation':'DISTANCE'}); g.l(cr.outputs['Root Position'], di.inputs[0]); g.l(oi.outputs['Location'], di.inputs[1])
mr = g.n('ShaderNodeMapRange'); mr.clamp = True; g.l(di.outputs['Value'], mr.inputs['Value']); g.l(pe, mr.inputs['From Min']); g.l(lo, mr.inputs['From Max']); mr.inputs['To Min'].default_value = 1.0; g.l(mi, mr.inputs['To Max'])
rb = g.n('FunctionNodeRandomValue', props={'data_type':'BOOLEAN'}); g.l(mr.outputs['Result'], rb.inputs['Probability'])
nt_ = g.n('FunctionNodeBooleanMath', props={'operation':'NOT'}); g.l([x for x in rb.outputs if x.type=='BOOLEAN'][0], nt_.inputs[0])
dl = g.n('GeometryNodeDeleteGeometry', props={'domain':'CURVE'}); g.l(geo, dl.inputs['Geometry']); g.l(nt_.outputs[0], dl.inputs['Selection'])
iq = g.n('ShaderNodeMath', props={'operation':'INVERSE_SQRT'}); g.l(mr.outputs['Result'], iq.inputs[0])
rn = g.n('GeometryNodeInputRadius'); mu = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(rn.outputs[0], mu.inputs[0]); g.l(iq.outputs[0], mu.inputs[1])
sr = g.n('GeometryNodeSetCurveRadius'); g.l(dl.outputs['Geometry'], sr.inputs['Curve']); g.l(mu.outputs[0], sr.inputs['Radius'])
g.l(sr.outputs['Curve'], o); libs.append(g.ng)

# 22. Corte pela Malha
g = G("GR Corte pela Malha", "Apaga os pontos do fio que passam da malha (raio do centro do objeto para fora). Corte reto: o fio cai natural e para na malha. Depois do Clump/Onda.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
mal = g.inp("Malha do corte", 'NodeSocketObject', desc="Malha em volta da cabeca; precisa conter todo o scalp")
o = g.out("Geometry", 'NodeSocketGeometry')
oi = g.n('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); g.l(mal, oi.inputs['Object'])
ps = g.n('GeometryNodeInputPosition'); nr = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(ps.outputs[0], nr.inputs[0])
rc = g.n('GeometryNodeRaycast'); g.l(oi.outputs['Geometry'], rc.inputs['Target Geometry']); g.l(ps.outputs[0], rc.inputs['Source Position']); g.l(nr.outputs[0], rc.inputs['Ray Direction']); rc.inputs['Ray Length'].default_value = 10.0
nt_ = g.n('FunctionNodeBooleanMath', props={'operation':'NOT'}); g.l(rc.outputs['Is Hit'], nt_.inputs[0])
dl = g.n('GeometryNodeDeleteGeometry', props={'domain':'POINT'}); g.l(geo, dl.inputs['Geometry']); g.l(nt_.outputs[0], dl.inputs['Selection'])
g.l(dl.outputs['Geometry'], o); libs.append(g.ng)

# 23. Comprimento ate a Malha
g = G("GR Comprimento até a Malha", "Cada fio vira reta da raiz ate onde bate na malha (normal do scalp + vies). Trolls, espetado, moicano. Depois da GR Densidade Livre (usa n_raiz); depois ligue Clump.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
mal = g.inp("Malha da forma", 'NodeSocketObject', desc="Precisa conter todo o scalp, senao o fio nasce fora e desce")
vi = g.inp("Viés", 'NodeSocketVector', (0.0,0.0,1.5), desc="Somado a normal do scalp. (0,0,1,5) = sobe (Trolls)")
pts = g.inp("Pontos", 'NodeSocketInt', 24, 2, 1000)
o = g.out("Geometry", 'NodeSocketGeometry')
rs = g.n('GeometryNodeResampleCurve'); g.l(geo, rs.inputs['Curve']); g.l(pts, rs.inputs['Count'])
oi = g.n('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); g.l(mal, oi.inputs['Object'])
cr = g.n('GeometryNodeGroup', group=EG['Curve Root'])
na = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="n_raiz")
ad0 = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(na.outputs['Attribute'], ad0.inputs[0]); g.l(vi, ad0.inputs[1])
nd = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(ad0.outputs[0], nd.inputs[0])
rc = g.n('GeometryNodeRaycast'); g.l(oi.outputs['Geometry'], rc.inputs['Target Geometry']); g.l(cr.outputs['Root Position'], rc.inputs['Source Position']); g.l(nd.outputs[0], rc.inputs['Ray Direction']); rc.inputs['Ray Length'].default_value = 10.0
sp = g.n('GeometryNodeSplineParameter')
k = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(sp.outputs['Factor'], k.inputs[0]); g.l(rc.outputs['Hit Distance'], k.inputs[1])
sc_ = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nd.outputs[0], sc_.inputs[0]); g.l(k.outputs[0], sc_.inputs['Scale'])
ad = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(cr.outputs['Root Position'], ad.inputs[0]); g.l(sc_.outputs[0], ad.inputs[1])
st = g.n('GeometryNodeSetPosition'); g.l(rs.outputs['Curve'], st.inputs['Geometry']); g.l(ad.outputs[0], st.inputs['Position'])
g.l(st.outputs['Geometry'], o); libs.append(g.ng)

# 24. Hair Cards
g = G("GR Hair Cards", "Cada fio vira um card (fita plana com UV) deitado no cranio: normal da curva = Tangent x n_raiz. Use depois da GR Densidade Livre com densidade baixa (8.000-20.000/m2). Material: GR Card Alpha.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
lw = g.inp("Meia largura", 'NodeSocketFloat', 0.009, 0.0, 1.0, "Metade da largura do card na raiz", 'DISTANCE')
afi = g.inp("Afinar", 'NodeSocketFloat', 0.4, 0.0, 1.0, "Shape do Set Hair Curve Profile", 'FACTOR')
pts = g.inp("Pontos", 'NodeSocketInt', 10, 2, 200, "Segmentos ao longo do card")
o = g.out("Mesh", 'NodeSocketGeometry')
rs = g.n('GeometryNodeResampleCurve'); g.l(geo, rs.inputs['Curve']); g.l(pts, rs.inputs['Count'])
pr = g.n('GeometryNodeGroup', group=EG['Set Hair Curve Profile'], Factor_Min=0.0, Factor_Max=1.0); g.l(rs.outputs['Curve'], pr.inputs['Geometry']); g.l(lw, pr.inputs['Radius']); g.l(afi, pr.inputs['Shape'])
na = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="n_raiz")
tg = g.n('GeometryNodeInputTangent'); cx = g.n('ShaderNodeVectorMath', props={'operation':'CROSS_PRODUCT'}); g.l(tg.outputs[0], cx.inputs[0]); g.l(na.outputs['Attribute'], cx.inputs[1])
sn = g.n('GeometryNodeSetCurveNormal'); g.l(pr.outputs['Geometry'], sn.inputs['Curve']); sn.inputs['Mode'].default_value = 'Free'; g.l(cx.outputs[0], sn.inputs['Normal'])
sp = g.n('GeometryNodeSplineParameter')
sv = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'POINT'}, Name="v"); g.l(sn.outputs['Curve'], sv.inputs['Geometry']); g.l(sp.outputs['Factor'], sv.inputs['Value'])
ln = g.n('GeometryNodeCurvePrimitiveLine', Start=(-1.0,0.0,0.0), End=(1.0,0.0,0.0))
sp2 = g.n('GeometryNodeSplineParameter')
su = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT','domain':'POINT'}, Name="u"); g.l(ln.outputs[0], su.inputs['Geometry']); g.l(sp2.outputs['Factor'], su.inputs['Value'])
cm = g.n('GeometryNodeCurveToMesh'); g.l(sv.outputs['Geometry'], cm.inputs['Curve']); g.l(su.outputs['Geometry'], cm.inputs['Profile Curve'])
rr = g.n('GeometryNodeInputRadius'); g.l(rr.outputs[0], cm.inputs['Scale'])
au = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}, Name="u"); av = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT'}, Name="v")
cb = g.n('ShaderNodeCombineXYZ'); g.l(au.outputs['Attribute'], cb.inputs['X']); g.l(av.outputs['Attribute'], cb.inputs['Y'])
uv = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT2','domain':'CORNER'}, Name="UVMap"); g.l(cm.outputs['Mesh'], uv.inputs['Geometry']); g.l(cb.outputs[0], uv.inputs['Value'])
ss = g.n('GeometryNodeSetShadeSmooth'); g.l(uv.outputs['Geometry'], ss.inputs['Geometry'])
g.l(ss.outputs['Geometry'], o); libs.append(g.ng)

# 25. Contorno
def mat_contorno():
    m = bpy.data.materials.new("GR Contorno"); nt = m.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); gm = nt.nodes.new('ShaderNodeNewGeometry'); tr = nt.nodes.new('ShaderNodeBsdfTransparent')
    em = nt.nodes.new('ShaderNodeEmission'); em.inputs['Color'].default_value=(0.02,0.01,0.005,1)
    lp = nt.nodes.new('ShaderNodeLightPath'); inv = nt.nodes.new('ShaderNodeMath'); inv.operation='SUBTRACT'; inv.inputs[0].default_value=1.0; nt.links.new(lp.outputs['Is Camera Ray'], inv.inputs[1])
    mxm = nt.nodes.new('ShaderNodeMath'); mxm.operation='MAXIMUM'; nt.links.new(gm.outputs['Backfacing'], mxm.inputs[0]); nt.links.new(inv.outputs[0], mxm.inputs[1])
    mx = nt.nodes.new('ShaderNodeMixShader'); nt.links.new(mxm.outputs[0], mx.inputs[0]); nt.links.new(em.outputs[0], mx.inputs[1]); nt.links.new(tr.outputs[0], mx.inputs[2]); nt.links.new(mx.outputs[0], o.inputs['Surface'])
    return m
MCONT = mat_contorno()
g = G("GR Contorno", "Contorno de nanquim por casca invertida, feito no GN (sem modificador). Para malha (GR Mecha Chunky). Material GR Contorno: so raios de camera veem a casca, senao ela bloqueia a luz. Cycles: Transparent bounces >= 32.")
geo = g.inp("Mesh", 'NodeSocketGeometry')
es = g.inp("Espessura", 'NodeSocketFloat', 0.0025, 0.0, 1.0, "2,5 mm le como traco de desenho a 70 cm", 'DISTANCE')
mt = g.inp("Material", 'NodeSocketMaterial')
o = g.out("Mesh", 'NodeSocketGeometry')
fl = g.n('GeometryNodeFlipFaces'); g.l(geo, fl.inputs['Mesh'])
nn = g.n('GeometryNodeInputNormal'); ng_ = g.n('ShaderNodeMath', props={'operation':'MULTIPLY'}); g.l(es, ng_.inputs[0]); ng_.inputs[1].default_value = -1.0
sc_ = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nn.outputs[0], sc_.inputs[0]); g.l(ng_.outputs[0], sc_.inputs['Scale'])
sp = g.n('GeometryNodeSetPosition'); g.l(fl.outputs[0], sp.inputs['Geometry']); g.l(sc_.outputs[0], sp.inputs['Offset'])
sm = g.n('GeometryNodeSetMaterial'); g.l(sp.outputs[0], sm.inputs['Geometry']); g.l(mt, sm.inputs['Material'])
j = g.n('GeometryNodeJoinGeometry'); g.l(geo, j.inputs[0]); g.l(sm.outputs[0], j.inputs[0])
g.l(j.outputs[0], o); libs.append(g.ng)
for it in g.ng.interface.items_tree:
    if getattr(it, 'name', '') == "Material" and it.in_out == 'INPUT': it.default_value = MCONT

# 26. Transicao
g = G("GR Transição", "Anima de um penteado para outro: cada ponto de A vai ate o ponto de mesmo indice em B. A e B precisam da mesma contagem de pontos (Resample antes de separar; Curl com Subdivisao 0).")
ga = g.inp("Penteado A", 'NodeSocketGeometry')
gb = g.inp("Penteado B", 'NodeSocketGeometry')
fa = g.inp("Fator", 'NodeSocketFloat', 0.0, 0.0, 1.0, "0 = A, 1 = B. Aceita campo: Scene Time - atraso por mecha", 'FACTOR')
o = g.out("Geometry", 'NodeSocketGeometry')
pB = g.n('GeometryNodeInputPosition'); ix = g.n('GeometryNodeInputIndex')
si = g.n('GeometryNodeSampleIndex', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}); g.l(gb, si.inputs['Geometry']); g.l(pB.outputs[0], si.inputs['Value']); g.l(ix.outputs[0], si.inputs['Index'])
pA = g.n('GeometryNodeInputPosition')
mx = g.n('ShaderNodeMix', props={'data_type':'VECTOR'}); g.l(fa, mx.inputs[0]); g.l(pA.outputs[0], mx.inputs[4]); g.l(si.outputs[0], mx.inputs[5])
sp = g.n('GeometryNodeSetPosition'); g.l(ga, sp.inputs['Geometry']); g.l(mx.outputs[1], sp.inputs['Position'])
g.l(sp.outputs[0], o); libs.append(g.ng)
for it in g.ng.interface.items_tree:
    if getattr(it, 'name', '') == "Fator" and it.in_out == 'INPUT': it.hide_value = False

# 27. Pentear por Curva
g = G("GR Pentear por Curva", "Deita cada fio na direcao da curva de fluxo mais proxima, projetada na pele. Para pelo curto de criatura. Use logo depois de gerar os fios (Generate Hair Curves ou guias); a normal vem da direcao da raiz.")
geo = g.inp("Geometry", 'NodeSocketGeometry')
cv = g.inp("Curva de fluxo", 'NodeSocketObject', desc="Objeto Curve desenhado sobre o corpo, no sentido do pelo")
lv = g.inp("Levanta", 'NodeSocketFloat', 0.35, 0.0, 1.0, "0 = deitado na pele, 1 = em pe", 'FACTOR')
o = g.out("Geometry", 'NodeSocketGeometry')
oi = g.n('GeometryNodeObjectInfo', props={'transform_space':'RELATIVE'}); g.l(cv, oi.inputs['Object'])
c2p = g.n('GeometryNodeCurveToPoints', props={'mode':'EVALUATED'}); g.l(oi.outputs['Geometry'], c2p.inputs['Curve'])
cap = g.n('GeometryNodeStoreNamedAttribute', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}, Name="fluxo_t"); g.l(c2p.outputs['Points'], cap.inputs['Geometry']); g.l(c2p.outputs['Tangent'], cap.inputs['Value'])
cr = g.n('GeometryNodeGroup', group=EG['Curve Root'])
sn = g.n('GeometryNodeSampleNearest', props={'domain':'POINT'}); g.l(cap.outputs[0], sn.inputs['Geometry']); g.l(cr.outputs['Root Position'], sn.inputs['Sample Position'])
fx = g.n('GeometryNodeInputNamedAttribute', props={'data_type':'FLOAT_VECTOR'}, Name="fluxo_t")
si = g.n('GeometryNodeSampleIndex', props={'data_type':'FLOAT_VECTOR','domain':'POINT'}); g.l(cap.outputs[0], si.inputs['Geometry']); g.l(fx.outputs['Attribute'], si.inputs['Value']); g.l(sn.outputs['Index'], si.inputs['Index'])
nrm = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(cr.outputs['Root Direction'], nrm.inputs[0])
dt = g.n('ShaderNodeVectorMath', props={'operation':'DOT_PRODUCT'}); g.l(si.outputs[0], dt.inputs[0]); g.l(nrm.outputs[0], dt.inputs[1])
s1 = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nrm.outputs[0], s1.inputs[0]); g.l(dt.outputs['Value'], s1.inputs['Scale'])
pj = g.n('ShaderNodeVectorMath', props={'operation':'SUBTRACT'}); g.l(si.outputs[0], pj.inputs[0]); g.l(s1.outputs[0], pj.inputs[1])
nd = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(pj.outputs[0], nd.inputs[0])
mx = g.n('ShaderNodeMix', props={'data_type':'VECTOR'}); g.l(lv, mx.inputs[0]); g.l(nd.outputs[0], mx.inputs[4]); g.l(nrm.outputs[0], mx.inputs[5])
nd2 = g.n('ShaderNodeVectorMath', props={'operation':'NORMALIZE'}); g.l(mx.outputs[1], nd2.inputs[0])
spp = g.n('GeometryNodeSplineParameter')
of = g.n('ShaderNodeVectorMath', props={'operation':'SCALE'}); g.l(nd2.outputs[0], of.inputs[0]); g.l(spp.outputs['Length'], of.inputs['Scale'])
ps = g.n('ShaderNodeVectorMath', props={'operation':'ADD'}); g.l(cr.outputs['Root Position'], ps.inputs[0]); g.l(of.outputs[0], ps.inputs[1])
st = g.n('GeometryNodeSetPosition'); g.l(geo, st.inputs['Geometry']); g.l(ps.outputs[0], st.inputs['Position'])
g.l(st.outputs[0], o); libs.append(g.ng)

# materiais
def mat_mecha():
    m = bpy.data.materials.new("GR Cabelo Cor por Mecha"); nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); out.location=(600,0)
    h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model='CHIANG'; h.parametrization='MELANIN'; h.location=(300,0)
    h.inputs['Roughness'].default_value=0.3; h.inputs['Melanin Redness'].default_value=0.5
    a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_name="mecha_rand"; a.location=(-400,100)
    mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value=0.3; mr.inputs['To Max'].default_value=0.65; mr.location=(-200,100)
    hi = nt.nodes.new('ShaderNodeHairInfo'); hi.location=(-400,-150)
    rr = nt.nodes.new('ShaderNodeMapRange'); rr.inputs['From Max'].default_value=0.25; rr.inputs['To Min'].default_value=0.45; rr.inputs['To Max'].default_value=0.0; rr.clamp=True; rr.location=(-200,-150)
    ad = nt.nodes.new('ShaderNodeMath'); ad.operation='ADD'; ad.location=(50,0)
    nt.links.new(a.outputs['Fac'], mr.inputs['Value']); nt.links.new(hi.outputs['Intercept'], rr.inputs['Value'])
    nt.links.new(mr.outputs['Result'], ad.inputs[0]); nt.links.new(rr.outputs['Result'], ad.inputs[1]); nt.links.new(ad.outputs[0], h.inputs['Melanin'])
    nt.links.new(h.outputs[0], out.inputs['Surface']); return m
def mat_toon():
    m = bpy.data.materials.new("GR Cabelo Toon"); nt=m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); out.location=(500,0)
    d = nt.nodes.new('ShaderNodeBsdfToon'); d.component='DIFFUSE'; d.inputs['Color'].default_value=(0.12,0.045,0.02,1); d.inputs['Size'].default_value=0.6; d.inputs['Smooth'].default_value=0.05; d.location=(0,100)
    gl = nt.nodes.new('ShaderNodeBsdfToon'); gl.component='GLOSSY'; gl.inputs['Color'].default_value=(1,0.85,0.7,1); gl.inputs['Size'].default_value=0.08; gl.inputs['Smooth'].default_value=0.1; gl.location=(0,-100)
    a = nt.nodes.new('ShaderNodeAddShader'); a.location=(250,0)
    nt.links.new(d.outputs[0], a.inputs[0]); nt.links.new(gl.outputs[0], a.inputs[1]); nt.links.new(a.outputs[0], out.inputs['Surface']); return m

def mat_card():
    m = bpy.data.materials.new("GR Card Alpha"); nt = m.node_tree; b = nt.nodes['Principled BSDF']; b.inputs['Roughness'].default_value=0.45
    uvn = nt.nodes.new('ShaderNodeUVMap'); uvn.uv_map='UVMap'
    sep = nt.nodes.new('ShaderNodeSeparateXYZ'); nt.links.new(uvn.outputs[0], sep.inputs[0])
    mp = nt.nodes.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value=(40,1.5,1); nt.links.new(uvn.outputs[0], mp.inputs[0])
    nz = nt.nodes.new('ShaderNodeTexNoise'); nz.noise_dimensions='2D'; nz.inputs['Scale'].default_value=1.0; nz.inputs['Detail'].default_value=2; nt.links.new(mp.outputs[0], nz.inputs['Vector'])
    cr = nt.nodes.new('ShaderNodeMapRange'); cr.inputs['From Min'].default_value=0.45; cr.inputs['From Max'].default_value=0.55; nt.links.new(nz.outputs['Fac'], cr.inputs['Value'])
    e1 = nt.nodes.new('ShaderNodeMath'); e1.operation='MULTIPLY_ADD'; e1.inputs[1].default_value=2; e1.inputs[2].default_value=-1; nt.links.new(sep.outputs['X'], e1.inputs[0])
    e2 = nt.nodes.new('ShaderNodeMath'); e2.operation='ABSOLUTE'; nt.links.new(e1.outputs[0], e2.inputs[0])
    e3 = nt.nodes.new('ShaderNodeMath'); e3.operation='POWER'; e3.inputs[1].default_value=4; nt.links.new(e2.outputs[0], e3.inputs[0])
    e4 = nt.nodes.new('ShaderNodeMath'); e4.operation='SUBTRACT'; e4.inputs[0].default_value=1; nt.links.new(e3.outputs[0], e4.inputs[1])
    p1 = nt.nodes.new('ShaderNodeMath'); p1.operation='POWER'; p1.inputs[1].default_value=3; nt.links.new(sep.outputs['Y'], p1.inputs[0])
    p2 = nt.nodes.new('ShaderNodeMath'); p2.operation='SUBTRACT'; p2.inputs[0].default_value=1; nt.links.new(p1.outputs[0], p2.inputs[1])
    a1 = nt.nodes.new('ShaderNodeMath'); a1.operation='MULTIPLY'; nt.links.new(cr.outputs['Result'], a1.inputs[0]); nt.links.new(e4.outputs[0], a1.inputs[1])
    a2 = nt.nodes.new('ShaderNodeMath'); a2.operation='MULTIPLY'; nt.links.new(a1.outputs[0], a2.inputs[0]); nt.links.new(p2.outputs[0], a2.inputs[1])
    nt.links.new(a2.outputs[0], b.inputs['Alpha'])
    cr2 = nt.nodes.new('ShaderNodeMix'); cr2.data_type='RGBA'; cr2.inputs[6].default_value=(0.05,0.02,0.01,1); cr2.inputs[7].default_value=(0.22,0.10,0.045,1)
    nt.links.new(sep.outputs['Y'], cr2.inputs[0]); nt.links.new(cr2.outputs[2], b.inputs['Base Color'])
    return m
mats = [mat_mecha(), mat_toon(), mat_card(), MCONT]

for ng in libs:
    ng.asset_mark(); ng.asset_data.description = ng.description
    ng.asset_data.tags.new("grooming"); ng.asset_data.tags.new("laboratorio")
for m in mats:
    m.use_fake_user = True; m.asset_mark(); m.asset_data.tags.new("grooming")
for ng in libs: ng.use_fake_user = True
OUTF = sys.argv[-1]
bpy.ops.wm.save_as_mainfile(filepath=OUTF, compress=True)
print("SALVO", OUTF, [n.name for n in libs], [m.name for m in mats])
