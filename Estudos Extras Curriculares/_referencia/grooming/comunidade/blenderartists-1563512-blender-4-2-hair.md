---
titulo: Blender 4.2: Hair
autor: CocoKozzy
url: https://blenderartists.org/t/blender-4-2-hair/1563512
data: 2024-12-18
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — CocoKozzy — 2024-12-18T22:46:51.394Z

Hello, is it possible to get this kind of hair in Blender 4.2 without any Add-ons?
image
556×511 48.6 KB

---

### Post #2 — thorn — 2024-12-18T23:04:04.984Z

Blender has a variety of tools for hair built in.
https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/hair/index.html

---

### Post #3 — thetony20 — 2024-12-19T09:58:54.832Z

For a still, or you want to animate/simulation of it as well?

---

### Post #4 — zeauro — 2024-12-19T12:13:12.769Z

You can give hair curves desired radius. But the more their radius is thin, tha more the amount of curves is important.
Hair rendering is costly.
Numerous hair curves corresponds to a lot of geometry.
And transmission in a lot of geometry corresponds to a lot of computations.
And because of hair particles being thin details, de-noising techniques may not be helpful.
That is why we are using tricks, like hair cards, Strand or Ribbons primitives, curves thicker at root, and default hair shader skipping ray bounces, transmission steps.
EEVEE does not support Hair shaders. It is limited to tweaking of available shaders. But Cycles should be able to do it with non-default hair shader model or dedicated hair shaders.
So, the question is rather : Do you have enough memory ? Are you ready to wait for a long rendertime ?

---

### Post #5 — CocoKozzy — 2024-12-19T16:19:04.811Z

For a still image.  I’m hoping default Blender 4.2 tool can make a similar hair render.

---

### Post #6 — thetony20 — 2024-12-20T08:39:58.943Z

Then yeah, for a still image, the Geometry Nodes hair curves and the various included hair node groups should totally be able to do that.
Just going to be a matter of time and playing around with it a bit.

---

### Post #7 — CocoKozzy — 2024-12-20T15:34:43.986Z

Thank you, very much.

---