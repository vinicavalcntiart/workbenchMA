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
g = G("GR Densidade Livre", "Interpolate Hair Curves sem a trava de 10.000 fios/m2 do painel. Testado bpy 5.2.2.")
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
g.l(it.outputs['Geometry'], o); g.l(it.outputs['Guide Index'], gi_o); libs.append(g.ng)

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
sub = g.inp("Subdivisão", 'NodeSocketInt', 3, 0, 6, "3 = 12 pontos viram 89")
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
mats = [mat_mecha(), mat_toon()]

for ng in libs:
    ng.asset_mark(); ng.asset_data.description = ng.description
    ng.asset_data.tags.new("grooming"); ng.asset_data.tags.new("laboratorio")
for m in mats:
    m.use_fake_user = True; m.asset_mark(); m.asset_data.tags.new("grooming")
for ng in libs: ng.use_fake_user = True
OUTF = sys.argv[-1]
bpy.ops.wm.save_as_mainfile(filepath=OUTF, compress=True)
print("SALVO", OUTF, [n.name for n in libs], [m.name for m in mats])
