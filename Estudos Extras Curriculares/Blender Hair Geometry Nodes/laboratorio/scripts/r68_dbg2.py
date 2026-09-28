import sys; sys.path.insert(0,'.')
exec(open('r35_updos.py').read().split("paths=[]; labels=[]")[0])
import numpy as np
def run(tie, tras, tranca=False, shrink=False):
    EG, GR, M, head, g = base(); t = Tree("x")
    def grp(n, out='Geometry', **kw):
        x = t.add('GeometryNodeGroup', group=GR[n])
        for k,v in kw.items(): x.inputs[k].default_value = v
        return t.chain(x, 'Geometry', out)
    grp("GR Guias Procedurais", out='Guias', **{"Cabeça (colisão)": head, "Comprimento": 0.45, "Para trás": 0.4})
    grp("GR Densidade Livre", Viewport=1.0)
    rb = grp("GR Rabo de Cavalo", **{"Cabeça (colisão)": head, "Amarração": tie, "Até a amarração": 0.35, "Comprimento da cauda": 0.30, "Para trás": tras})
    if tranca: grp("GR Trança Grossa", Raio=0.022, **{"Começa em": 0.38, "Cruzamentos": 1.0, "Espessura na ponta": 0.5, **({"Cabeça (colisão)": head} if tranca=="cab" else {})})
    if shrink:
        w = t.eg(EG['Shrinkwrap Hair Curves'], Factor=1.0, Offset_Distance=0.004, Above_Surface=0.0, Smoothing_Steps=2, Lock_Roots=True)
        for q in w.inputs:
            if q.name == 'Surface' and q.type == 'OBJECT': q.default_value = head
    apply_tree(g, t.finish())
    d = g.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    P = np.zeros(len(d.points)*3, np.float32); d.attributes['position'].data.foreach_get('vector', P); P=P.reshape(-1,3)
    r = np.linalg.norm(P, axis=1)
    first = np.array([c.first_point_index for c in d.curves]); n = np.array([c.points_length for c in d.curves])
    idx = np.concatenate([np.arange(f, f+max(1,k//3)) for f,k in zip(first, n)])
    print("DBG tranca", tranca, "shrink", shrink, "dentro 1/3:", round(float((r[idx]<0.1).mean())*100,1), "%  dentro total:", round(float((r<0.1).mean())*100,1))
run((0.075, 0.06, -0.07), -0.5, True, False)
run((0.075, 0.06, -0.07), -0.5, "cab", False)
