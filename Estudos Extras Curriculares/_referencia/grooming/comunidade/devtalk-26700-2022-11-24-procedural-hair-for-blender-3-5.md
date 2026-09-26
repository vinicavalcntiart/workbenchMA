---
titulo: 2022-11-24 Procedural Hair for Blender 3.5
autor: dfelinto
url: https://devtalk.blender.org/t/2022-11-24-procedural-hair-for-blender-3-5/26700
data: 2022-11-25
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — dfelinto — 2022-11-25T14:20:05.544Z

Procedural Hair
November 24, 2022
As a follow up of the
last module meeting
Daniel Bystedt organized a meeting to find the priorities (nodes and node groups) for procedural hair for Blender 3.5.
Present:
Andy Goralczyk
Dalai Felinto
Daniel Bystedt
Jacques Lucke
Lukas Tonne
The topics are in order of priority (from higher to lower):
Distribute child splines on faces
Hair info
Clump splines
Hair frizz
Curl hair
Smooth hair
Braids
Push hair outside surface
Rotate hair
Bend hair
Straighten hair
Shrinkwrap hair
Interpolate shape
Feedback:
Distribute child curves on faces
This is the basic interpolation needed for working with parent/child hair workflow.
Hair info
Should be a node group if possible, before becoming a built-in node
Clump splines
Parting should be doable via attributes within a data-set.
The clump criteria (e.g., distance) should be an option for the node.
Geodesic distance node would help, ahtough slow
Hair frizz
Keeping the distance between segments is needed regardless.
It can be one of the building blocks for the hair frizz group.
Curl hair
The frequency, amplitude and length should be inputs that can be mapped.
The total length of the curly hair is important in some cases (to preserve the hair length).
Smooth hair
It doesn’t try to align the hair tip with the surface.
Preserve the overall length or;
Lock the being/end of the curves.
Use case/example:
If you have a lot of frizz, Daniel would randomly select hair and smooth them out, so it gets a less uniform look.
It helps for final tweaks without having to do changes on the begin of a node-tree (before the frizz is applied).
Braids
Braids and corn rows can use the same system.
Push hair outside surface
This is one of the most complicated and important topics.
This can be computational expensive.
A generic solution may be tricky, but a simple system may be possible for some use cases.
Rotate hair
Spin the hair around the root around the surface normal.
Useful to get random overlaps.
Bend hair
The simple case is to bend long hair tips.
Nice for moustaches (not french mustaches).
For long hair the root point is not relevant.
It may be better to pick a few of the last control points, but it is also dependent of the control point density.
Shrinkwrap hair
Useful for some animals, where the hair gets really close to the legs.
Interpolate shape
Useful for animating art-directed hair poses.
Straighten hair
Same as the puff brush.

---

### Post #2 — Metamesh — 2023-01-11T00:18:18.115Z

excited to see the development on this, can’t wait to see what else is cooking for grooming!

---

### Post #3 — fr002 — 2023-01-11T17:51:46.969Z

See
@DanielBystedt
posts on Twitter. He did some interesting node groups / proof of concept
https://twitter.com/3DBystedt/status/1612235936334581761?s=20&t=_LIyMEq9l0TjNT9_5RfHcQ

---

### Post #4 — DamianWinnichenko — 2023-05-10T15:04:51.984Z

I didn’t find any better place to ask, sorry if this is the wrong place.
I’d like to know if there are plans to add an operator to increase\decrease hair resolution (number of control points of a single strand). For now, it is only possible to delete a strand(strands) and create a new one with the specified number of control points.
At least, I didn’t find a more optimal solution if exists.
image
1149×617 135 KB
image
1072×680 114 KB

---

### Post #5 — modmoderVAAAA — 2023-05-10T15:16:44.444Z

Hello, yes, this tool is still being developed right now, so it will be added sometime.
EDIT: When I talk about a tool, I mean the hair editor itself and its editing tools*

---

### Post #6 — DamianWinnichenko — 2023-05-10T15:22:12.549Z

Aaah! Good to know! Thanks a lot!

---

### Post #7 — HooglyBoogly — 2023-05-10T15:45:57.771Z

In the meantime, you can use the resample curve node in a geometry nodes modifier and apply it.

---

### Post #8 — DamianWinnichenko — 2023-05-10T15:54:44.486Z

Confirm! The method works perfectly, thanks for the advice!

---