import sys; sys.path.insert(0,'.')
from lab import *
G = dict(length=0.26, gravity=3.5, spread=0.3, outward=0.35, n_guides=200)
def toon_mat():
    m = bpy.data.materials.new("chunky"); nt=m.node_tree; b = nt.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value=(0.35,0.12,0.04,1); b.inputs['Roughness'].default_value=0.35
    b.inputs['Coat Weight'].default_value = 0.4
    return m
def build(t, EG, g=None, scalp=None, flat=0.35, twist=0.0, per_lock=False, dens=3000.0, rad=0.006, clump=False):
    interp(t, EG, density=dens)
    if clump:
        t.eg(EG['Clump Hair Curves'], Factor=0.6, Shape=0.25, Preserve_Length=True, Guide_Distance=0.03, Existing_Guide_Map=False, Seed=1)
    t.chain(t.add('GeometryNodeResampleCurve', Count=24), 'Curve', 'Curve')
    # raio afilado: Set Hair Curve Profile (Shape 0.5, Factor Min 0 na ponta)
    t.eg(EG['Set Hair Curve Profile'], Radius=rad, Shape=0.3, Factor_Min=0.0, Factor_Max=1.0)
    if twist:
        sp = t.add('GeometryNodeSplineParameter')
        mul = t.add('ShaderNodeMath', props={'operation':'MULTIPLY'}); t.link(sp.outputs['Factor'], mul.inputs[0])
        if per_lock:
            r = t.add('FunctionNodeRandomValue', props={'data_type':'FLOAT'}, Min=-twist, Max=twist, Seed=8)
            # ID vazio = por curva (cada mecha e uma curva aqui)
            t.link(r.outputs['Value'], mul.inputs[1])
        else: mul.inputs[1].default_value = twist
        st = t.add('GeometryNodeSetCurveTilt'); t.chain(st, 'Curve', 'Curve'); t.link(mul.outputs[0], st.inputs['Tilt'])
    circ = t.add('GeometryNodeCurvePrimitiveCircle', Resolution=10, Radius=1.0)
    tr = t.add('GeometryNodeTransform', Scale=(1.0, flat, 1.0)); t.link(circ.outputs['Curve'], tr.inputs['Geometry'])
    c2m = t.add('GeometryNodeCurveToMesh', Fill_Caps=True); t.chain(c2m, 'Curve', 'Mesh'); t.link(tr.outputs['Geometry'], c2m.inputs['Profile Curve'])
    rad_in = t.add('GeometryNodeInputRadius'); t.link(rad_in.outputs[0], c2m.inputs['Scale'])
    t.chain(t.add('GeometryNodeSetShadeSmooth'), 'Geometry', 'Geometry')
    set_mat(t, toon_mat())
BACK = dict(cam_loc=(-0.40,0.55,0.05), target=(0,0,-0.07), lens=55)
run_variants("16_chunky", [
    ("tubo redondo (flat 1)", dict(flat=1.0, _guides=dict(G))),
    ("fita achatada (Y 0.35)", dict(flat=0.35, _guides=dict(G))),
    ("fita + torcao global pi", dict(flat=0.35, twist=math.pi, _guides=dict(G))),
    ("fita + torcao por mecha +-pi", dict(flat=0.35, twist=math.pi, per_lock=True, _guides=dict(G))),
    ("idem + Clump 0.6", dict(flat=0.35, twist=math.pi, per_lock=True, clump=True, _guides=dict(G))),
    ("mais fina e densa (r4mm, 6000/m2)", dict(flat=0.3, twist=math.pi, per_lock=True, rad=0.004, dens=6000.0, _guides=dict(G))),
], build, cols=3, **BACK)
