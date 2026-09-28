"""Simula um traco do Texture Paint (modo Space) com as formulas do codigo do Blender:
- falloff: BKE_brush_curve_strength (brush.cc), Custom avaliado por CurveMapping do proprio bpy
- sem Accumulate: mask = acc*(1-f) + s*f (paint_image_proj.cc, 'approaches brush_alpha slowly')
- com Accumulate: mask = acc + s*f*alphafac; alphafac = 1/overlap so com Adjust Strength for Spacing
  (paint_image_ops_paint.cc + paint_stroke_integrate_overlap em paint_stroke.cc)
Mede a borda do traco: distancia entre 90% e 10% do valor do centro, em raios."""
import bpy, math, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img")

def preset(name):
    return {"SMOOTH": lambda p: 3*p*p-2*p**3, "SHARP": lambda p: p*p, "SMOOTHER": lambda p: p**3*(p*(p*6-15)+10),
            "LINEAR": lambda p: p, "POW4": lambda p: p**4, "SPHERE": lambda p: math.sqrt(max(0,2*p-p*p))}[name]

def custom(points):
    b = bpy.data.brushes.new("tmp", mode='TEXTURE_PAINT'); c = b.curve_distance_falloff
    cv = c.curves[0]
    while len(cv.points) > 2: cv.points.remove(cv.points[1])
    cv.points[0].location = points[0]; cv.points[1].location = points[-1]
    for pt in points[1:-1]: cv.points.new(*pt)
    for pt in cv.points: pt.handle_type = 'AUTO'
    c.update(); c.initialize()
    xs = np.linspace(0, 1, 1001); ys = np.array([c.evaluate(cv, x) for x in xs])
    return lambda p: float(np.interp(1.0-p, xs, ys))   # Custom: avalia em 1-p = distancia normalizada

def falloff_fn(kind):
    f = preset(kind) if isinstance(kind, str) else custom(kind)
    return lambda d: 0.0 if d >= 1 else f(1.0 - d)   # d = distancia/raio; p = 1-d

def overlap(fd, spacing):
    n = int(100/max(spacing,0.1)); h = max(spacing,0.1)/50.0; best = 0
    for i in range(10):
        x0 = i*0.1 - 1; s = sum(fd(abs(x0 + k*h)) for k in range(n) if abs(x0+k*h) < 1); best = max(best, s)
    return 1.0/best if best else 1.0

def stroke(kind, strength=1.0, spacing=10, accumulate=False, atten=False, R=40, W=560, H=150, peak=1.0):
    fd0 = falloff_fn(kind); fd = lambda d: peak*fd0(d)
    alphafac = overlap(fd, spacing) if (accumulate and atten) else 1.0
    yy, xx = np.mgrid[0:H, 0:W].astype(float); acc = np.zeros((H, W))
    step = 2*R*spacing/100.0
    lut_d = np.linspace(0, 1, 2001); lut = np.array([fd(d) for d in lut_d])
    px = np.linspace(60, W-60, 20000); py = H/2 + 18*np.sin((px-60)/(W-120)*2*np.pi)
    arc = np.concatenate([[0], np.cumsum(np.hypot(np.diff(px), np.diff(py)))])
    for a_ in np.arange(0, arc[-1], step):   # dabs espacados pelo comprimento do arco, como no Blender
        x = float(np.interp(a_, arc, px)); y = float(np.interp(a_, arc, py))
        d = np.sqrt((xx-x)**2 + (yy-y)**2)/R; f = np.where(d < 1, np.interp(np.minimum(d,1), lut_d, lut), 0.0)
        if accumulate: acc = np.minimum(acc + strength*f*alphafac, 1.0)
        else: acc = np.maximum(acc, acc*(1-f) + strength*f)   # so grava se aumenta
    return acc

def profile1d(kind, strength=1.0, spacing=10, accumulate=False, atten=False, peak=1.0, **_):
    """Traco reto: pixel no meio do traco, a distancia y (em raios) da linha. Dabs a cada 2*spacing/100 raios."""
    fd0 = falloff_fn(kind); fd = lambda d: peak*fd0(d)
    alphafac = overlap(fd, spacing) if (accumulate and atten) else 1.0
    step = 2*spacing/100.0; xs = np.arange(-1.2, 1.2+1e-9, step)
    ys = np.linspace(0, 1, 201); out = []
    for y in ys:
        acc = 0.0
        for x in xs:
            f = fd(math.hypot(x, y))
            acc = min(acc + strength*f*alphafac, 1.0) if accumulate else max(acc, acc*(1-f) + strength*f)
        out.append(acc)
    out = np.array(out); c = out[0]
    y90 = np.interp(0.9*c, out[::-1], ys[::-1]); y10 = np.interp(0.1*c, out[::-1], ys[::-1]); y50 = np.interp(0.5*c, out[::-1], ys[::-1])
    return round(y10-y90, 2), round(y50, 2), round(c, 2)

def edge_width(img, R=40):
    col = img[:, img.shape[1]//2]; c = col.max()
    if c <= 0: return 0, 0
    idx = np.arange(len(col)); top = idx[col >= 0.9*c]; low = idx[col >= 0.1*c]
    return round(((low.max()-top.max()))/R, 2), round(c, 2)

def hard(h):   # hardness como no Paint Hard do Essentials: pontos do Smooth comprimidos para [h, 1]
    return [(h + x*(1-h), y) for x,y in [(0.0,1.0),(0.25,0.94),(0.75,0.06),(1.0,0.0)]]
V = [
 ("Paint Soft padrão (Smooth, str 1)", dict(kind="SMOOTH")),
 ("Paint Hard padrão", dict(kind=[(0.0,1.0),(0.75,1.0),(0.81,0.95),(0.96,0.06),(1.0,0.0)])),
 ("Soft, Strength 0,3", dict(kind="SMOOTH", strength=0.3)),
 ("Soft, spacing 40%", dict(kind="SMOOTH", spacing=40)),
 ("Accumulate + Adjust for Spacing", dict(kind="SMOOTH", accumulate=True, atten=True)),
 ("Accumulate + Adjust, curva Sharp", dict(kind="SHARP", accumulate=True, atten=True)),
 ("Curva Custom com pico 0,15 (flow)", dict(kind="SMOOTH", peak=0.15)),
 ("Custom cauda longa, pico 0,15", dict(kind=[(0.0,1.0),(0.25,0.45),(0.6,0.1),(1.0,0.0)], peak=0.15)),
 ("Accumulate + Adjust, hardness 0,5", dict(kind=hard(0.5), accumulate=True, atten=True)),
 ("Accumulate + Adjust, cauda longa", dict(kind=[(0.0,1.0),(0.25,0.45),(0.6,0.1),(1.0,0.0)], accumulate=True, atten=True)),
 ("hardness 0,5 com spacing 5%", dict(kind=hard(0.5), accumulate=True, atten=True, spacing=5)),
 ("cauda longa com spacing 5%", dict(kind=[(0.0,1.0),(0.25,0.45),(0.6,0.1),(1.0,0.0)], accumulate=True, atten=True, spacing=5)),
]
rows = []; W=560; H=150
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17)
S = Image.new("RGB", (2*W, 6*(H+30)), (24,24,26)); dr = ImageDraw.Draw(S)
for i,(lb,kw) in enumerate(V):
    a = stroke(**kw); w, y50, c = profile1d(**kw); rows.append((lb, w, c)); print("ROW", lb, "| borda 10-90%:", w, "R | meia altura:", y50, "R | centro:", c)
    im = Image.fromarray((255*(1-a*0.92)).astype(np.uint8)).convert("RGB")
    x, y = (i%2)*W, (i//2)*(H+30); S.paste(im, (x, y+30)); dr.text((x+8, y+6), f"{lb}  | borda {w} R", fill=(235,235,235), font=f)
S.save(os.path.join(OUT, "brush_soft_sheet.jpg"), quality=90)
