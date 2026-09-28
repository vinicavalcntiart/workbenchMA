import sys; sys.path.insert(0,'.')
from lab import *
reset(); EG = essentials()
head, scalp = make_head()
area = sum(p.area for p in scalp.data.polygons)*1.004**2
print("area scalp m2:", round(area,4))
g = comb_guides(scalp, n=150)
for mode in ("default_value","Value node"):
    for dens in (10000.0, 100000.0):
        t = Tree(f"d{dens}")
        n = t.eg(EG['Interpolate Hair Curves'])
        if mode=="default_value":
            n.inputs['Density'].default_value = dens; shown = n.inputs['Density'].default_value
        else:
            v = t.add('ShaderNodeValue'); v.outputs[0].default_value = dens; t.link(v.outputs[0], n.inputs['Density']); shown = dens
        ng = t.finish(); m = apply_tree(g, ng)
        st = stats(g); print(mode, dens, "-> socket", shown, "curves", st.get('curves'), "por m2", round(st.get('curves',0)/area))
        g.modifiers.remove(m)
