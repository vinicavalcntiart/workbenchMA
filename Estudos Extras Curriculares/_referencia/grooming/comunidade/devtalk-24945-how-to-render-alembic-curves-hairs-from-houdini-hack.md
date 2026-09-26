---
titulo: How to render alembic curves/hairs from Houdini with this hack
autor: pullpullson
url: https://devtalk.blender.org/t/how-to-render-alembic-curves-hairs-from-houdini-with-this-hack/24945
data: 2022-06-30
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — pullpullson — 2022-06-30T17:09:23.582Z

Hey friends,
We are currently having a project in which we simulate hair in Houdini and want to render it in Blender.
In general the issue is importing animated alembic curves and then render them in Blender with the new curve data block.
Now many of you who already tried to get this to work might know it’s not that straightforward.
There are a couple of obstacles along the way.
Hopefully this whole process should be a lot easier once:
D11591 - Alembic: import arbitrary attributes
D11592 - Alembic/USD: use geometry sets to import data
are merged in master.
But for people who want to get something working before that, here is a little overview.
Using Blender 3.3.0 Alpha with new Curves type enabled (in Experimental settings tab)
Obstacle 01 - Importing Curves
Problem:
Importing an alembic cache that contains curves seems to work in the viewport but when starting a render the cache always jumps back to the first frame or rest pose and essentially does not get evaluated. There are a couple of reasons for this which you can read through in this task:
T58704 - Animated alembic curves dont update on render
Solution:
We know alembic curves don’t work but what works is alembic polygons. So what we need to do is somehow convert the curves in houdini to polygons, import them to Blender as a regular alembic cache and then convert them back to curves.
Convert houdini curves/polylines to polygons with the
ends
node. This node basically just connects the last curve point with the first one and creates a ngon.
convert_side_by_side
1000×500 113 KB
Import that alembic file into Blender (here you can already verify that this cache renders at any frame as expected)
Add a geometry node modifier with a node tree that does the following:
hair_blender_nodetree
868×284 14.9 KB
We convert
Mesh to Curve
and by using the
Set Spline Cyclic
node with Cyclic turned off we basically undo what we did in houdini and delete the connection between the last and first point.
Note:
It seems like in some cases it deletes the wrong edge, input is welcome on how the debug this.
As a result we now have actual curves that don’t jump back to their rest pose when trying to render them.
convert_blender_side_by_side
1000×500 60.5 KB
But how do we render them?
Obstacle 02 - Render Curves
:
Problem:
Trying to render our converted curves now does not work. They don’t show up. In the background those curves are still stored in the old data block. What we want is the new curve data block so we can use nodes like the
Set Curve Radius
node and affect how our curves are rendered.
Solution
:
In order to ‘convert’ those curves to the new curve data block we create an empty hair object, add a geometry node setup and just reference our old object with the converted curves in to the new empty hair object geo node tree. That way we use the new curve data block. You should also immediatly see a change in the viewport how the curves are displayed.
Create empty hair object
Add geometry node setup,
Object Info
converted curves object and connect to output.
Set Curve Radius
and
Set Material
.
hair_new_type_nodetree
758×284 17.6 KB
Render!
Hopefully that helps someone who has the same issue right now.
Cheers!

---

### Post #2 — hi.jprooney — 2022-07-20T08:48:10.392Z

Wow-thanks SO much for this walkthrough. I’ve just tested and it’s a hack that’s working so far. I’d been beating my head against a wall for a while on this problem, hoping that someone would crack this. Much appreciated

---

### Post #3 — pullpullson — 2022-07-20T09:18:36.120Z

No problem! Glad it helped.
Just keep an eye on the deletion of the edge with the
Set Spline Cyclic
node. I hade issues that for some ngons it would delete the wrong edge

---

### Post #4 — nikokoneko — 2022-07-20T09:28:47.891Z

Thanks SO much for this tutorial! I’ve been using this approach for a few monhs actually, but always great to hear other people still care about this problem. I did have a lot of issues with Set Spline Cyclic node deleting the wrong edge, so I think what I did instead is to export curveu attribute from Houdini (via vertex colors) and then deleting the vertices with curveu smaller (or larger) than some near-limit value such as 0.02 or 0.98 in order to force the deletion of correct edge (although in that case I lose the first or last vertex of the curve too, so it’s not perfect neither).

---

### Post #5 — pullpullson — 2022-07-20T10:51:01.211Z

Hey
@nikokoneko
,
thanks for your input on the ‘wrong edge deletion’ problem. Realy interesting approach you found there! I think at this point it would be worth contacting one of the geometry nodes devs and find out what’s wrong with the
Set Spline Cyclic
node. (winking at you
@jacqueslucke
). Maybe I’ll have time to do some tests soon and find out more.

---

### Post #6 — nikokoneko — 2022-07-20T11:53:45.693Z

To be honest I could not figure out if the problem was in the Blender”s SetSplineCyclic node or Houdini was not closing all lines correctly. Looking at the errors I couldn’t find the common thread between them to deduce where the problem could be.

---

### Post #7 — ecke101 — 2022-07-20T22:32:25.621Z

The node is only setting the “cyclic” attribute on the curve so nothing could go wrong in the node really.
This should give the same result:

---

### Post #8 — kurk — 2022-08-31T01:14:38.646Z

One can use a sequential .abc export in Blender to deal with the Alembic curve cache bug. The  workaround by the OP is not ideal, however it is a good to have solution.

---

### Post #9 — JooJ — 2022-11-22T15:09:22.157Z

Hey, really helpful explanation on how to get the hair across from houdini, however i dont understand how you managed to get the hair to stick to character and have physics like you show in the video, i also cannot manually sculpt the hair for some reason either.

---

### Post #10 — koko_ze — 2022-11-22T16:55:10.849Z

Is alembic unable to store just plain edges? Or why is that houdini curve to polygon there?

---

### Post #11 — pullpullson — 2022-11-22T17:05:14.049Z

Yes. I think if you export a plain edge from houdini it automatically gets converted to curves.
Maybe it’s also the Blender side that interprets that as a curve. Not 100% sure which one is the issue.
And then you run again in to:
Obstacle 01 - Importing Curves
(as described in the thread)

---

### Post #12 — SamuliPahaoja — 2023-01-10T20:29:16.099Z

In my case at least, the extra edge was always between the vertices with the lowest and highest indices of the face. So instead of making the curve non-cyclic, I removed that edge before converting from mesh to curves. Seems to work well.
image
1211×795 135 KB

---

### Post #13 — nikokoneko — 2023-04-17T21:29:04.636Z

Thank you
@SamuliPahaoja
this workaround is flawless!

---