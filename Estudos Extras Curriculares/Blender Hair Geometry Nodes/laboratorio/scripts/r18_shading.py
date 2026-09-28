import sys; sys.path.insert(0,'.')
from lab import *
import lab; lab.LIGHT_K = 0.4
G = dict(length=0.30, gravity=4.0, spread=0.25, outward=0.3, n_guides=200)
BACK = dict(cam_loc=(-0.40,0.55,0.05), target=(0,0,-0.07), lens=55)
def mk(kind):
    m = bpy.data.materials.new(kind); nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); base=(0.30,0.11,0.04,1)
    if kind in ("CHIANG","HUANG"):
        h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model = kind; h.parametrization='COLOR'
        h.inputs['Color'].default_value = base; h.inputs['Roughness'].default_value = 0.3
        nt.links.new(h.outputs[0], out.inputs['Surface'])
    elif kind == "PRINCIPLED":
        b = nt.nodes.new('ShaderNodeBsdfPrincipled'); b.inputs['Base Color'].default_value=base; b.inputs['Roughness'].default_value=0.4
        b.inputs['Coat Weight'].default_value=0.3; nt.links.new(b.outputs[0], out.inputs['Surface'])
    elif kind == "TOON":
        d = nt.nodes.new('ShaderNodeBsdfToon'); d.component='DIFFUSE'; d.inputs['Color'].default_value=base; d.inputs['Size'].default_value=0.6; d.inputs['Smooth'].default_value=0.05
        g = nt.nodes.new('ShaderNodeBsdfToon'); g.component='GLOSSY'; g.inputs['Color'].default_value=(1,0.85,0.7,1); g.inputs['Size'].default_value=0.15; g.inputs['Smooth'].default_value=0.02
        a = nt.nodes.new('ShaderNodeAddShader'); nt.links.new(d.outputs[0], a.inputs[0]); nt.links.new(g.outputs[0], a.inputs[1])
        nt.links.new(a.outputs[0], out.inputs['Surface'])
    elif kind == "GRADIENTE":
        hi = nt.nodes.new('ShaderNodeHairInfo'); cr = nt.nodes.new('ShaderNodeValToRGB')
        cr.color_ramp.elements[0].color=(0.08,0.03,0.015,1); cr.color_ramp.elements[1].color=(0.55,0.25,0.08,1)
        nt.links.new(hi.outputs['Intercept'], cr.inputs['Fac'])
        b = nt.nodes.new('ShaderNodeBsdfPrincipled'); b.inputs['Roughness'].default_value=0.45
        nt.links.new(cr.outputs['Color'], b.inputs['Base Color']); nt.links.new(b.outputs[0], out.inputs['Surface'])
    return m
def build(t, EG, g=None, scalp=None, kind="CHIANG"):
    interp(t, EG, density=300000.0)
    c = t.eg(EG['Clump Hair Curves'], Factor=1.0, Shape=0.0, Tip_Spread=0.004, Preserve_Length=True, Guide_Distance=0.02, Existing_Guide_Map=False, Seed=1)
    sp = t.add('GeometryNodeSplineParameter'); mr = t.add('ShaderNodeMapRange', From_Max=0.3); mr.clamp=True
    t.link(sp.outputs['Factor'], mr.inputs['Value']); t.link(mr.outputs['Result'], c.inputs['Factor'])
    profile(t, EG, radius=0.0006)
    set_mat(t, mk(kind))
run_variants("18b_shading", [(k, dict(kind=k, _guides=dict(G))) for k in ("CHIANG","HUANG","PRINCIPLED","TOON","GRADIENTE")], build, cols=5, res=420, **BACK)
