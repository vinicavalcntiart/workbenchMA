---
titulo: Rig and simulate Hair Curves on Blender 3.3
autor: SSBB210
url: https://blenderartists.org/t/rig-and-simulate-hair-curves-on-blender-3-3/1407111
data: 2022-09-16
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — SSBB210 — 2022-09-16T22:32:22.648Z

(copy/paste of what I have posted on reddit)
The required geonodes to make rigging and dynamics hair(with cloth sim) possible are in this file
https://studio.blender.org/films/heist/gallery/?asset=6072
Hair_deform & generate_proxy
Create any mesh and add generate_proxy then select the haircurves & apply it
Put Hair_deform on the haircurves and select the proxy you just generated
(If you do any modification to any of those objects, you must re-generate another proxy, you can still add additional genodes that can modify or add additional curves, but it must be under hair_deform)
Also the generated mesh will have a lot of vertices, so you need to optimize your hair curves and use geonode to generate more children
https://www.youtube.com/watch?v=dUuRmcUQK_s
by Johnny Matthews
It’s the same concept as this tutorial
https://www.youtube.com/watch?v=W97e8xIVoqE
by Nick Burkard
But using geonodes
To Simulate hair with cloth physic
You need to create another proxy for the proxy and extrude faces, otherwise you won’t have any collision. Also it easier to weight paint faces than invisible vertices
Update: Surface Deform need to be the last modifier for interpolated hair curves to work, you will also need to activate the checkbox for: ‘Surface Rest Position’ in the interpolated hair node
nvm doesnt work with hair_deform, sorry for the bump
Only if the body or scalp is using armature modifier. This doesnt apply if you are using Child of constraint/Armature Constraint, you wont have hair shifting/moving issue with constraints.

---

### Post #2 — SSBB210 — 2022-09-25T06:48:58.936Z

Step 0. this guide assumes you have surface deform geometry node already
image
1591×1016 285 KB
Step 1. append the geometry nodes from
https://studio.blender.org/films/heist/gallery/?asset=6072
image
1945×1144 233 KB
append these nodes too:
https://johnnygizmo.gumroad.com/l/habif
by
Johnny Matthews
image
1337×862 122 KB
Step 2. Make a backup of your hair curves. Optimize your curve hair, if you want to have dynamics hair(w/ cloth sim). Use the density brush. Separate the hair into multiple section if you have to.
If you choose to skip this step, you can still rig it, but your proxy mesh will have way too many vertices and your viewport performance won’t be great
image
1503×1037 236 KB
Use the geometry nodes that you just appended to generates children(if you know how to create interpolated children, it would be even better, I don’t know how to do that.)
image
2001×1196 417 KB
Step 3.  Turn off any geometry nodes that can generate children, apply them if you have to(resample can be applied), because the Generate_proxy will create an exact copy of your hair curves with its visible nodes.
Add a hair deform geometry node and move it above. Geometry nodes that can generate or move the curve need to be under hair_deform
image
1476×995 205 KB
The Hair_deform requires a proxy to work correctly
Turn the visibility off for the hair_deform for now otherwise you cannot use the generate proxy.
image
1329×887 152 KB
Step 4. Create any mesh(Suzanne, Plane, Grid…) and add a geometry node then select the generate_proxy
image
724×371 60.8 KB
select the hair curves
apply it

---

### Post #3 — SSBB210 — 2022-09-25T07:23:20.829Z

Step 5. name your proxy
image
1431×715 191 KB
Do not edit the mesh! You can add an armature modifier, but you won’t be able to see your weight paint, because there is no face. you can assign it to the hair_deform and turn back on every nodes that aren’t visible
image
1357×944 186 KB
Step 6. Duplicate your proxy and name it
image
1515×811 235 KB
Select the mesh you just duplicated and go in edit mode select everything and extrude by 0.001
image
699×664 81.8 KB
(OPTIONAL for the cloth modifier)Do not let go of your selection. Create a vertex group and assign them, it’s for the cloth modifier
image
2122×623 318 KB
image
1403×678 256 KB
Add another vertex group and call it whatever you want. I named it “pin” though.
Weight paint it
image
1570×729 149 KB
Set the cloth modifier, I am no expert in blender sim, I find it most of the time buggy. maybe someone has a good preset that they can share.
image
1390×929 173 KB
Step 7.Add Surface deform to the original proxy and select the proxy with the cloth modifier.
image
1414×527 140 KB
Make sure to bind it with no deformation, so go back to frame 0 or 1 and bind it. (because of the cloth modifier)

---

### Post #4 — SSBB210 — 2022-09-25T07:36:06.577Z

Step 8. TURN OFF ray visibility for cycles and set the viewport display(EEVEE & Cycles) as wire  for the the proxies
image
430×775 50.8 KB
Step 9. Make sure turn back the hair curves and its geometry nodes. if you follow correctly and I didn’t mess up you should at least have something like this, when you add an object with the collision modifer
image
1718×925 149 KB

---

### Post #5 — SSBB210 — 2022-09-25T07:50:26.370Z

Step 10. If you do not want clipping hair, you can add this geonode:“Curves Aboves” by Johnny Matthews and add these nodes to the geometry node(I have no idea if this is the best way to edit it, Geometry node is still too complicated for me)
image
2379×1345 444 KB
you can add a “resample” to make the hair a bit smoother again and reduce hair clipping through mesh.
image
1521×1219 260 KB
Sorry I did not cover the rigging part, but it should be like this
https://www.youtube.com/watch?v=gTdRGZA4TXA
DON’T FORGET to parent the proxies to the “head” bone or Data transfer the vertex group from the body mesh and then assign an armature

---

### Post #6 — SSBB210 — 2022-09-25T13:33:21.992Z



---

### Post #7 — SSBB210 — 2022-09-25T13:53:29.329Z

If the hair are flying around, then select the vertices from the denser area in edit mode and add some of them into the no_self_collision vertex group or don’t use self collision
Or redo it from Step 2.

---

### Post #8 — spiotrx — 2022-10-20T13:53:24.744Z

This post is underrated. Not many Blender 3.3 hair guides out there. Thank you!

---

### Post #9 — JBJ — 2023-02-04T21:27:08.820Z

This is pure gem for GN hair simulation. advanced skill. Thank you for your detailed explanation.

---

### Post #10 — SSBB210 — 2023-03-29T18:54:23.726Z

Better method here by munorr:
https://munorr.gumroad.com/l/bgen
edit:
no longer free
but not that expensive
https://munorr.gumroad.com/

---

### Post #11 — loic_bramoulle — 2023-04-08T23:42:55.399Z

B-gen is amazing but it only works for hair & braids, not for a piece of fur or beard, as it should deform with the body (facial animation/shapekey anim, armature/surface deform modifier ect…) For this the Hair_deform & generate_proxy method from the Einar demo file is supposed to work, but in my test the Hair_deform node setup makes the curves disapear when doing anything in the scene. (rendering, hiding any collection ect…) it works when turning the hair_deform off and on again, but as rendering a frame makes it disapear again, you’ll only see it in viewport.
In my case it’s for example a piece of fur on the clothes, the proxy generated with the node setup is driven with surface deform by another proxy of a portion of the body.
So in viewport I can see it seems to work, but the fur vanishes when doing anything includidng rendering, until turned off and on again.
hair_test_002
1377×848 172 KB

---

### Post #12 — ZenYS — 2023-05-01T14:21:43.035Z

Does this problem appears in 3.5.1 version?

---

### Post #13 — loic_bramoulle — 2023-06-19T22:21:05.836Z

ah nice it seems to work in 3.5.1, but only if we move frame by frame, jumping on a frame in the timeline doesn’t synch the hair_deform on the right frame. Or maybe it just takes some time to snap into place.

---