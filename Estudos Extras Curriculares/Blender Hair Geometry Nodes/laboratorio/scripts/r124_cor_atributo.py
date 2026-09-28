"""Atributo de cor no GN (5.2): Store Named Attribute tipo Color -> Attribute no shader."""
import sys; sys.path.insert(0,'.')
from lab import *
def cor_mat(name, attr):
    m = bpy.data.materials.new(name); nt = m.node_tree
    for n in list(nt.nodes):
        if n.type != 'OUTPUT_MATERIAL': nt.nodes.remove(n)
    out = [n for n in nt.nodes if n.type == 'OUTPUT_MATERIAL'][0]
    h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.parametrization = 'COLOR'
    a = nt.nodes.new('ShaderNodeAttribute'); a.attribute_type = 'GEOMETRY'; a.attribute_name = attr
    nt.links.new(a.outputs['Color'], h.inputs['Color']); nt.links.new(h.outputs[0], out.inputs['Surface'])
    return m
def ramp(t, stops):
    cr = t.add('ShaderNodeValToRGB'); el = cr.color_ramp.elements
    el[0].position, el[0].color = stops[0]; el[1].position, el[1].color = stops[-1]
    for p, c in stops[1:-1]: e = el.new(p); e.color = c
    return cr
def build(t, EG, g=None, scalp=None, mode="fio"):
    interp(t, EG, density=300000.0)
    t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.5, Preserve_Length=True, Guide_Distance=0.03, Existing_Guide_Map=False, Seed=1)
    st = t.add('GeometryNodeStoreNamedAttribute', props={'data_type': 'FLOAT_COLOR', 'domain': 'CURVE' if mode == "fio" else 'POINT'})
    st.inputs['Name'].default_value = "cor"; t.chain(st)
    if mode == "fio":    # uma cor por fio: Curve Info Random -> Color Ramp
        ci = t.add('GeometryNodeGroup', group=EG['Curve Info'])
        cr = ramp(t, [(0.0, (0.35,0.12,0.04,1)), (0.5, (0.75,0.35,0.10,1)), (1.0, (0.95,0.75,0.35,1))])
        t.link(ci.outputs['Random'], cr.inputs['Fac'])
    else:                # raiz -> ponta: Spline Parameter -> Color Ramp (dominio Point)
        sp = t.add('GeometryNodeSplineParameter')
        cr = ramp(t, [(0.0, (0.05,0.03,0.02,1)), (0.55, (0.45,0.18,0.06,1)), (1.0, (0.95,0.55,0.75,1))])
        t.link(sp.outputs['Factor'], cr.inputs['Fac'])
    t.link(cr.outputs['Color'], st.inputs['Value'])
    profile(t, EG, radius=0.0003)
    set_mat(t, cor_mat("cor_" + mode, "cor"))
run_variants("124_cor_atributo", [
    ("Cor por fio (Curve, Curve Info Random)", dict(mode="fio")),
    ("Raiz -> ponta (Point, Spline Parameter)", dict(mode="ponta")),
], build, cols=2)
