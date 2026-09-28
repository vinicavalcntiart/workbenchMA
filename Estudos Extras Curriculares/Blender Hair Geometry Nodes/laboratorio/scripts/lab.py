"""Laboratorio de grooming headless, bpy 5.2.2."""
import bpy, bmesh, math, os, random, time
from mathutils import Vector, Matrix
import addon_utils
LAB = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(bpy.utils.system_resource('DATAFILES'),'assets','nodes','procedural_hair_node_assets.blend')

def reset():
    bpy.ops.wm.read_homefile(use_empty=True)
    addon_utils.enable("cycles", default_set=True)

def essentials():
    with bpy.data.libraries.load(ASSETS, link=False) as (src, dst):
        dst.node_groups = [n for n in src.node_groups]
    return {ng.name: ng for ng in bpy.data.node_groups}

def link(ob, coll=None):
    (coll or bpy.context.scene.collection).objects.link(ob); return ob

# ---------- cabeca e scalp ----------
def make_head(radius=0.1, scalp_cut=-0.15, front_cut=0.55, subdiv=64):
    """Cabeca = esfera. Scalp = calota superior (z > scalp_cut*R), sem a testa/rosto (y < -front_cut*R e z<0.55R)."""
    me = bpy.data.meshes.new("head")
    bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=subdiv, v_segments=subdiv//2, radius=radius, calc_uvs=True)
    bm.to_mesh(me); bm.free()
    head = link(bpy.data.objects.new("head", me))
    for p in me.polygons: p.use_smooth = True
    # scalp
    sm = me.copy(); sm.name = "scalp"
    bm = bmesh.new(); bm.from_mesh(sm)
    kill = []
    for f in bm.faces:
        c = f.calc_center_median()
        face = (c.y < -front_cut*radius and c.z < 0.62*radius)   # rosto/testa
        low = c.z < scalp_cut*radius
        sides = (abs(c.x) > 0.8*radius and c.z < 0.25*radius and c.y < 0.2*radius)  # orelhas
        if face or low or sides: kill.append(f)
    bmesh.ops.delete(bm, geom=kill, context='FACES')
    bm.to_mesh(sm); bm.free()
    scalp = link(bpy.data.objects.new("scalp", sm))
    scalp.scale = (1.004,1.004,1.004)
    bpy.context.view_layer.update()
    return head, scalp

# ---------- guias ----------
def comb_guides(scalp, n=180, pts=12, length=0.28, gravity=4.0, R=0.1, spread=0.25, outward=0.3, part_x=0.0, seed=1, back_bias=0.0):
    """Guias penteadas: sai pela normal, divide na risca (x=part_x), cai com gravidade e nao entra na cabeca."""
    rnd = random.Random(seed)
    me = scalp.data; mw = scalp.matrix_world
    # amostragem por area
    tris = []
    me.calc_loop_triangles()
    for t in me.loop_triangles:
        a,b,c = [mw @ me.vertices[i].co for i in t.vertices]
        tris.append((a,b,c,((b-a).cross(c-a)).length/2))
    tot = sum(t[3] for t in tris)
    roots = []
    for _ in range(n):
        r = rnd.uniform(0,tot); acc=0
        for a,b,c,ar in tris:
            acc += ar
            if acc >= r: break
        u,v = rnd.random(), rnd.random()
        if u+v>1: u,v=1-u,1-v
        roots.append(a + (b-a)*u + (c-a)*v)
    curves = []
    for p0 in roots:
        nrm = p0.normalized()
        side = 1 if p0.x >= part_x else -1
        d = (nrm*outward + Vector((side*spread, 0.35+back_bias, -0.3))).normalized()
        p = p0.copy(); seg = length/(pts-1); cur=[p.copy()]
        for i in range(1,pts):
            d = (d + Vector((0,0,-gravity/(pts-1)))).normalized()
            p = p + d*seg
            if p.length < R*1.06: p = p.normalized()*R*1.06   # colisao simples
            cur.append(p.copy())
        curves.append(cur)
    cd = bpy.data.hair_curves.new("guides")
    cd.add_curves([pts]*len(curves))
    flat = [c for cur in curves for v in cur for c in v]
    cd.attributes['position'].data.foreach_set('vector', flat)
    ob = link(bpy.data.objects.new("guides", cd))
    cd.surface = scalp
    cd.surface_uv_map = "UVMap"
    return ob

# ---------- modificador de GN ----------
class Tree:
    """Mini construtor: t = Tree('nome'); n = t.add('GeometryNodeGroup', group=EG['Clump Hair Curves'], Factor=0.5)"""
    def __init__(self, name):
        self.ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
        self.ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
        self.ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        self.gi = self.ng.nodes.new('NodeGroupInput'); self.go = self.ng.nodes.new('NodeGroupOutput')
        self.x = 0; self.geo = self.gi.outputs[0]
    def add(self, idname, group=None, props=None, **inputs):
        n = self.ng.nodes.new(idname)
        if group is not None: n.node_tree = group
        for k,v in (props or {}).items(): setattr(n, k, v)
        for k,v in inputs.items():
            s = n.inputs[k.replace('_',' ')] if k.replace('_',' ') in n.inputs else n.inputs[k]
            s.default_value = v
        self.x += 250; n.location = (self.x, 0)
        return n
    def chain(self, n, sock_in='Geometry', sock_out='Geometry'):
        """Liga a geometria corrente em n e avanca."""
        self.ng.links.new(self.geo, n.inputs[sock_in]); self.geo = n.outputs[sock_out]; return n
    def eg(self, group, **inputs):
        return self.chain(self.add('GeometryNodeGroup', group=group, **inputs))
    def link(self, a, b):
        self.ng.links.new(a, b)
    def finish(self):
        self.ng.links.new(self.geo, self.go.inputs[0]); return self.ng

def apply_tree(ob, ng):
    m = ob.modifiers.new(ng.name, 'NODES'); m.node_group = ng; return m

def stats(ob):
    dg = bpy.context.evaluated_depsgraph_get(); ev = ob.evaluated_get(dg)
    d = ev.data
    try: return dict(curves=len(d.curves), points=len(d.points), attrs=sorted(a.name for a in d.attributes if not a.name.startswith('.')))
    except Exception as e: return dict(err=str(e))

# ---------- material ----------
def hair_mat(name="hair", melanin=0.8, redness=0.3, roughness=0.3, coat=0.0, tint=None, model='CHIANG', rand_color=0.1):
    m = bpy.data.materials.new(name)
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    h = nt.nodes.new('ShaderNodeBsdfHairPrincipled'); h.model = model; h.parametrization = 'MELANIN'
    h.inputs['Melanin'].default_value = melanin
    h.inputs['Melanin Redness'].default_value = redness
    h.inputs['Roughness'].default_value = roughness
    if 'Random Color' in h.inputs: h.inputs['Random Color'].default_value = rand_color
    if tint: h.inputs['Tint'].default_value = (*tint,1)
    nt.links.new(h.outputs[0], out.inputs['Surface'])
    return m

def skin_mat():
    m = bpy.data.materials.new("skin"); nt=m.node_tree
    b = nt.nodes.get('Principled BSDF')
    if b: b.inputs['Base Color'].default_value=(0.8,0.55,0.45,1); b.inputs['Roughness'].default_value=0.6
    return m

# ---------- cena e render ----------
def stage(cam_loc=(0.42,-0.62,0.10), target=(0,0,-0.06), lens=50, res=640, samples=24, bg=0.08):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=samples
    sc.cycles.use_denoising = True
    try: sc.cycles.denoiser = 'OPENIMAGEDENOISE'
    except Exception: pass
    sc.render.resolution_x = sc.render.resolution_y = res
    sc.render.film_transparent = False
    cam = link(bpy.data.objects.new("cam", bpy.data.cameras.new("cam"))); cam.data.lens = lens
    cam.location = cam_loc
    d = Vector(target) - Vector(cam_loc); cam.rotation_euler = d.to_track_quat('-Z','Y').to_euler()
    sc.camera = cam
    def light(name, typ, loc, energy, size=2, color=(1,1,1)):
        L = bpy.data.lights.new(name, typ); L.energy = energy; L.color=color
        if typ=='AREA': L.size = size
        o = link(bpy.data.objects.new(name, L)); o.location = loc
        dd = Vector(target)-Vector(loc); o.rotation_euler = dd.to_track_quat('-Z','Y').to_euler(); return o
    light("key",'AREA',(0.35,-0.35,0.45),LIGHT_K*14,0.3,(1,0.95,0.9))
    light("rim",'AREA',(-0.3,0.4,0.3),LIGHT_K*16,0.2,(0.8,0.9,1))
    light("fill",'AREA',(-0.45,-0.25,0.0),LIGHT_K*4,0.4)
    w = bpy.data.worlds.new("w"); sc.world = w
    w.node_tree.nodes['Background'].inputs[0].default_value=(bg,bg,bg*1.1,1)
    return cam

def render(path, **kw):
    sc = bpy.context.scene
    sc.render.filepath = path
    t = time.time(); bpy.ops.render.render(write_still=True)
    return round(time.time()-t,1)

# ---------- base comum ----------
def base_scene(n_guides=160, seed=1, **guide_kw):
    n_guides = guide_kw.pop("n_guides", n_guides)
    reset(); EG = essentials()
    head, scalp = make_head()
    head.data.materials.append(skin_mat())
    scalp.hide_render = True
    g = comb_guides(scalp, n=n_guides, seed=seed, **guide_kw)
    return EG, head, scalp, g

def value(t, v):
    n = t.add('ShaderNodeValue'); n.outputs[0].default_value = v; return n.outputs[0]

def interp(t, EG, density=300000.0, **kw):
    n = t.eg(EG['Interpolate Hair Curves'], **kw)
    t.link(value(t, density), n.inputs['Density'])
    return n

def profile(t, EG, radius=0.0004, shape=0.5, fmin=0.0, fmax=1.0):
    return t.eg(EG['Set Hair Curve Profile'], Radius=radius, Shape=shape, Factor_Min=fmin, Factor_Max=fmax)

def set_mat(t, mat):
    n = t.add('GeometryNodeSetMaterial'); n.inputs['Material'].default_value = mat
    return t.chain(n)

LIGHT_K = 1.0
OUT = os.path.join(LAB, "out"); os.makedirs(OUT, exist_ok=True)
def shot(name, **stage_kw):
    stage(**stage_kw)
    p = os.path.join(OUT, name + ".png")
    s = render(p); print(f"RENDER {name}: {s}s -> {p}"); return p

def sheet(paths, labels, out, cols=3, w=512):
    from PIL import Image, ImageDraw, ImageFont
    ims = [Image.open(p).convert("RGB").resize((w,w)) for p in paths]
    rows = (len(ims)+cols-1)//cols
    S = Image.new("RGB", (cols*w, rows*(w+34)), (24,24,26)); d = ImageDraw.Draw(S)
    try: f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception: f = ImageFont.load_default()
    for i,(im,lb) in enumerate(zip(ims,labels)):
        x,y = (i%cols)*w, (i//cols)*(w+34)
        S.paste(im,(x,y+34)); d.text((x+10,y+6), lb, fill=(235,235,235), font=f)
    S.save(out); return out

def run_variants(tag, variants, build, res=480, samples=16, cols=None, **shot_kw):
    """variants: lista de (rotulo, kwargs). build(t, EG, **kwargs) monta a cadeia depois do Interpolate."""
    paths, labels, info = [], [], []
    for i,(lb,kw) in enumerate(variants):
        EG, head, scalp, g = base_scene(**kw.pop('_guides', {}))
        t = Tree(tag)
        build(t, EG, g=g, scalp=scalp, **kw)
        apply_tree(g, t.finish())
        st = stats(g)
        tt = time.time(); p = shot(f"{tag}_{i}", res=res, samples=samples, **shot_kw)
        paths.append(p); labels.append(lb); info.append((lb, st.get('curves'), st.get('points')))
    sp = sheet(paths, labels, os.path.join(OUT, f"{tag}_sheet.png"), cols=cols or len(paths))
    for x in info: print("INFO", tag, x)
    print("SHEET", sp); return sp

# ---------- pelo ----------
def make_body(radius=0.15, subdiv=64):
    me = bpy.data.meshes.new("body")
    bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=subdiv, v_segments=subdiv//2, radius=radius, calc_uvs=True)
    bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    return link(bpy.data.objects.new("body", me))

def fur_guides(surf, n=500, pts=6, length=0.03, lift=0.45, seed=2, R=0.15):
    """Guias curtas: saem pela normal e deitam para baixo ao longo da superficie."""
    rnd = random.Random(seed); me = surf.data; me.calc_loop_triangles()
    tris=[]; tot=0
    for t in me.loop_triangles:
        a,b,c = [me.vertices[i].co.copy() for i in t.vertices]; ar=((b-a).cross(c-a)).length/2; tris.append((a,b,c,ar)); tot+=ar
    curves=[]
    for _ in range(n):
        r=rnd.uniform(0,tot); acc=0
        for a,b,c,ar in tris:
            acc+=ar
            if acc>=r: break
        u,v=rnd.random(),rnd.random()
        if u+v>1: u,v=1-u,1-v
        p0=a+(b-a)*u+(c-a)*v; nrm=p0.normalized()
        down=(Vector((0,0,-1)) - nrm*nrm.dot(Vector((0,0,-1))))
        if down.length<1e-4: down=Vector((1,0,0))
        down.normalize()
        cur=[]; seg=length/(pts-1)
        for i in range(pts):
            tt=i/(pts-1)
            d=(nrm*lift*(1-tt)+down*(1-lift*(1-tt))).normalized()
            p = p0 if i==0 else cur[-1]+d*seg
            if p.length<R*1.01: p=p.normalized()*R*1.01
            cur.append(p.copy())
        curves.append(cur)
    cd=bpy.data.hair_curves.new("fur"); cd.add_curves([pts]*len(curves))
    cd.attributes['position'].data.foreach_set('vector',[c for cur in curves for v in cur for c in v])
    ob=link(bpy.data.objects.new("fur",cd)); cd.surface=surf; cd.surface_uv_map="UVMap"; return ob

def fur_scene(**kw):
    reset(); EG = essentials()
    body = make_body(); body.data.materials.append(skin_mat())
    g = fur_guides(body, **kw); return EG, body, g

def vgroup(scalp, name, fn):
    """Cria vertex group no scalp com peso fn(co) em coordenadas de mundo."""
    vg = scalp.vertex_groups.new(name=name); mw = scalp.matrix_world
    for v in scalp.data.vertices:
        w = max(0.0, min(1.0, fn(mw @ v.co)))
        vg.add([v.index], w, 'REPLACE')
    return vg
