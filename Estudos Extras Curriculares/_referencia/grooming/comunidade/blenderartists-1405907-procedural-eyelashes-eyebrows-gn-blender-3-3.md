---
titulo: Procedural Eyelashes/Eyebrows with Geometry Nodes in Blender 3.3
autor: thetony20
url: https://blenderartists.org/t/procedural-eyelashes-eyebrows-with-geometry-nodes-in-blender-3-3/1405907
data: 2022-09-10
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — thetony20 — 2022-09-10T17:48:53.421Z

Hi All,
Looking for some help/advice in relation to the new Hair system in Blender 3.3 and Geometry Nodes.
First up, I totally suck at Geometry Nodes, just can’t get my head around most of it and hence the need for the help.
The Idea
Given the new hair curves in Blender 3.3, I have this ‘vision’ of maybe a Geometry Nodes driven setup of just being able to place a few ‘guide hairs’ for eyelashes or eyebrows and then being able to tweak a bunch of parameters via geometry Nodes and you can have all sorts of eyelashes or eyebrows.
Now I know you can just do it all via the grooming tools, but then you have to do that every time. It would be way more flexible to just add a few guild hairs (like the start, end, along with a few in the middle to define general shape and direction) and then adjust the length, the bending angle, how ‘bushy’ or pencil thin the eyebrows are, etc, etc all via a few Geometry Node values and maybe the odd Float Curve and the like.
So, first question, is this even possible and if so, then second question would be how?
As a starting point, consider this:
Eyelash-curve
1131×1265 90.9 KB
Four default Hair Curves added around the top eyelid of Suzanne, with the default Geometry Node group.
Reading left to right as being the starting point, is it possible to make those four hairs have their length adjusted based on the shown Float Curve. So the first hair would be fairly short, the second one a little longer, the third is the longest at the peak of that curve and then the forth is just a little shorter.
Now of course, if that’s possible, then a whole bunch of other questions come up. Like if one then adds more hairs, will they all follow the Float Curve. Can you then bend or shape the ‘eyelashes’ up/down, add some spread to one side or the other, or both. Generally increase a random number of extra hairs without them spreading out too far (like cutting into the eye). Control the thickness and some clumping, etc, etc.
So yeah, you know, all the sort of controls one would like for a whole range of possible eyelashes, but lets start with something simple and basic (I hope) and control the length.
cheers.

---

### Post #2 — thetony20 — 2022-09-13T16:24:47.654Z

So I take it there are no Geometry Node wizards out there that can help?

---

### Post #3 — zeroskilz — 2022-09-13T18:00:30.313Z

thetony20:
I take it there are no Geometry Node wizards out there
Yeah no, sorry, just us idiots here… (speaking for myself, of course)
Donno about the new hair system… just managed eyelashes in the past using regular curves; doing something like this:
image
1854×937 250 KB
… building a curve from a vertex group and adding Bezier instances and setting end positions and handles for curviness. Skipping the curve-to-mesh here for brevity (which would come at the end and would give the lashes “volume”).
Just an example - you can obviously build on this to make it as complex as you can manage.
Good luck.

---

### Post #4 — thetony20 — 2022-09-14T09:24:34.661Z

OK, thanks for that. It seems you are using some float curves to control the shape, which is somewhat there.
So in theory much of that should work on the new hair system, as one would just directly supply the curves into the node group, rather then add them first long a polygon edge.
I’ll try to play around with it a bit to see if I can get lucky hacking something together.

---

### Post #5 — thetony20 — 2022-09-14T17:22:34.812Z

Played around with things a little and had some part success.
Eyelash-curve2
1920×1080 161 KB
Can use the new hair curve to just add some ‘hairs’ and they will bend and somewhat curve based on the 2 float curves.
However, I’m somewhat stuck at what I thought would be the initial problem anyway and that is if I try to change the length of the hairs, so make them shorter, either by a trim curve node or just by direct sculpting, I lose all the bending, rather then just having smaller versions of what’s seen in the image, I quickly end up with straight lines.
And of course that doesn’t even touch on the second part of that problem, being able to easily adjust the length of the hairs as they go across the eye. So shorter (and ideally less curved) near the nose, to being longer and more curved towards the outer edge.

---

### Post #6 — DeAndre_Johnson — 2022-11-04T14:22:50.242Z

Maybe this can help. It deesn’t use the new hair system but the geometry node set up might be helpful.

---

### Post #7 — thetony20 — 2022-11-04T15:22:50.184Z

Thanks, I’ll check it out.

---