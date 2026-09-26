---
titulo: Geometry Nodes Assets Blender 5.0
autor: SimonThommes
url: https://devtalk.blender.org/t/geometry-nodes-assets-blender-5-0/42334
data: 2025-09-12
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — SimonThommes — 2025-09-12T16:57:21.557Z

Hello!
The time has come to ship more Geometry Nodes assets with Blender 5.0.
The goal is to bring the power of Geometry Nodes to more users, especially those that don’t necessarily want to interface with the node editor. At the same time we also want to add a few node-groups targeting those that do already use nodes and make a few things, that were already possible, more convenient by wrapping them in a pre-existing node asset.
I’m breaking these things down as
High-Level Nodes/Modifiers
Array
Scatter on Surface
Instance on Elements
Randomize Transforms
Geometry Input
Medium-Level Nodes
Smooth Geometry
Displace Geometry
Low-Level Nodes/Building Blocks
Edge Length
Is Edge Boundary
Is Edge Loose
Is Edge Manifold
Sphere Selection
Box Selection
Normal Selection
Random Rotation
Combine/Separate Cylindrical Vector
Combine/Separate Spherical Vector
The preliminary version can be found in this PR here:
#145645
A downloadable build can be found at the end of that PR.
A few disclaimers:
This is not the ultimate list of all node-groups that will ever be shipped with Blender, we’re hoping for many more, that will make Geometry Nodes more accessible from the start.
We are currently not looking for more suggestions of additional nodes. We have our own long list of wishes that we want to add, but there is only so much time and many things cannot be implemented yet with sufficient efficiency, so let’s compromise and add more assets in the future.
Keeping everything (screenshots etc.) up-to-date at all times is a lot of work, so in the interest of time, forgive me, when some things are outdated. The file in the PR itself is always the latest reference point.
descriptions are still missing
thumbnails are still missing
documentation is still missing
Examples
More details can be found in the PR itself, here are two of the high-level examples:
Array
A comprehensive new Array modifier, with shape modes for Line, Circle, Curve and Transform, and Gizmos, and Randomization.
(not meant as an exact replacement for now, but in 95% of use-cases, plus a few new ones, it should be a sufficient replacement)
[video in PR]
Scatter on Surface
Basic scattering modifier to make this essential use-case for Geometry Nodes a matter of a few clicks instead of building it from scratch.
[video in PR]
…
Others can be found in the PR (
#145645
).
We are still working to include a few more, as time allows.
But feedback is of course welcome and wanted!
Please do consider the constraints, fantasizing about future additions to this list can be done separately.

---

### Post #2 — LazyDodo — 2025-09-12T17:53:30.449Z

I’m not as much concerned about
what
we ship as the compatibility story we have, if any. For any nodes we ship out of the box, there’s a fair bit of time spend in versioning so users are able to load older files when changes are made. Whats the story like in asset land if lets say in 5.1 we add some features to the asset nodes we ship? or god forbid we remove a socket somewhere since there’s now a different/better way to do things. How would that manifest in end users existing files?

---

### Post #3 — SimonThommes — 2025-09-12T17:57:58.620Z

I’m glad you ask! The nice thing with these assets is that nothing will break, since the assets are going to be locally packed in the file. So any updates will only actually propagate to existing uses if the user explicitly replaces the node-group.
Hopefully we’ll have a proper version system for that in place for 5.1, but regardless, out-of-the-box there is no versioning code required, since the user can indefinitely continue using the old version of the asset in the file, from when it was initially added.

---

### Post #4 — LazyDodo — 2025-09-12T18:00:16.363Z

I like hearing nothing will break, less enthusiastic about the “they’ll be forever stuck in time” part, but it’s a good base to build on!

---

### Post #5 — SimonThommes — 2025-09-12T18:01:43.318Z

Well, emphasis on CAN. I definitely think we need to be able to tell users about outdated assets in their file and make it easy to upgrade. But we don’t need to force compatibility as much as for builtin feature, since upgrading is a choice.

---

### Post #6 — JoelR_VC — 2025-09-12T18:38:05.812Z

Perhaps include a versioning naming system somewhere in the UI, perhaps within the group node? This way you explicitly show the version of the packed asset to the user without it appearing to warn them that the version is oudated.

---

### Post #7 — SimonThommes — 2025-09-12T18:43:31.704Z

The design for this has been discussed in the
most recent Geometry Nodes workshop
.
This thread is meant for feedback on the assets themselves, so let’s please keep it on topic.

---

### Post #8 — JoelR_VC — 2025-09-12T18:46:32.878Z

I understand, sorry for repeating what was discussed, feel free to delete my answers so the thread stays focused.

---

### Post #9 — SimonThommes — 2025-09-12T18:53:26.102Z

No worries! I didn’t mean to sound harsh. It’s good input, just not the exactly right place.

---

### Post #10 — JoelR_VC — 2025-09-12T18:57:01.250Z

One question, I see that the amount mode in the scatter instances on surfaces node only has the amount value but not the distribution type. I don’t know if it’s possible to add those modes as well, or if it’s not possible to do so using the method used to determine the exact number of instances?
Perhaps in this mode, a relaxation property could be added to the points across the surface, with an iteration slider (0 by default) to control de effect. It would be a good way to have the exact number of points that don’t overlap much.
something like the answer to this
blender.stackexchange.com
Uniform distribution of points
geometry-nodes
asked by
Robert Hintz
on
02:07PM - 01 Feb 23 UTC

---

### Post #11 — SimonThommes — 2025-09-12T19:12:35.704Z

Unifying the exact number and poisson disk distribution method with nodes didn’t give satisfying results, so I dropped it.
Relaxation seems like potentially a good thing to add in the future. Right now I don’t see a great, efficient and convenient way of doing it while considering geodesic distance. For a flat plane it’s easy, for a general 3D surface it’s a bit more involved. For a v1, I think, it’s fine to skip this.

---

### Post #12 — BD3D — 2025-09-12T20:16:24.823Z

Hello
For the scatter node, I would suggest to rename the term ‘
align rotation
’ to ‘
align to surface normal
’ which is clearer

---

### Post #13 — NizarAmous — 2025-09-12T20:21:31.394Z

don’t we need tetrahedralize node before doing the relaxation?

---

### Post #14 — Bobo_The_Imp — 2025-09-12T20:24:35.326Z

Slightly unrelated sorry, but I was very curious seeing the “amount” mode in the scatter instances on surface node. I remember Jacques Lucke talking about potentially making that for the Distribute Points on Faces node, so it’s very cool to have that in this nodegroup. Would there still be any interest in doing that for for the Distribute Points on Faces node natively?
SimonThommes:
Relaxation seems like potentially a good thing to add in the future
mega thumbs up for this!

---

### Post #15 — Huang_Gao — 2025-09-13T02:55:08.992Z

Hello, I have been learning about geometric nodes recently and feel it is necessary to implement the geometric node asset function module. However, users are still concerned about the stability of the performance of geometric node modeling. Occasionally, I find that things implemented with geometric nodes have extremely poor performance or are not as good as destructive modeling.

---

### Post #16 — Gerstmann_Bradley — 2025-09-13T05:38:31.953Z

Besides Align Rotation, I hope we have an extra options for “rotation” on Local axis.
We can definitely tweak it in edit mode, but it will be less procedural and parametric.
One use case for such kind of rotation controls are commonly seen in Phone Ads where phone spanning out in Arc and rotating locally.
Or we need “Transform” Modifier, which then seems a bit overdoing? no strong idea yet.
for now I think have an extra rotation control is the simplest method and it probably doesn’t hurt anything to add.
(Note I think we should also add it in curve mode.)
image
413×463 23.8 KB
I also want to emphasize a huge issue of rate of float slider.
In short, in Node Editor it’s easy to slide a rotation value from 0 to 400 degrees, but the same action in Modifier only slide a rotation value from 0 to 50 degrees. I hope to call awareness of this issue, so that it can be really investigated and resolved to improve UX.
Blender Projects
Nodes: Different mouse drag effect for float properties
**System Information**
Operating system: Windows-10-10.0.19041-SP0 64 Bits
Graphics card: NVIDIA GeForce GTX 980 Ti/PCIe/SSE2 NVIDIA Corporation 4.5.0 NVIDIA 522.25

**Blender Version**
Broken: version: 3.5.0 Alpha, branch: master, commit date:...

---

### Post #17 — 1112 — 2025-09-14T02:50:41.312Z

Perhaps the issue should be reported in the UI or node-related section, but it is indeed related to the current topic: when the parameters under the transformation panel of this asset are adjusted and then Ctrl+Z is used to return to the previous state, the entire panel will fold up, which greatly affects the experience (the panel needs to be opened again).
Editor: The ideal situation should be that only the previous operation is rolled back, and the panel is in an expanded state at this time and should not be affected (as shown in the additional foldable interface operation in the second video).

---

### Post #18 — tolkfan — 2025-09-14T14:16:37.273Z

It’s great to see Array and Instance on Elements nodes/modifers coming soon. Those two things are what I see people asking for (or being confused about) the most.
I see that there are plans to add a
Face Corner
option for the
Instance on Element
node, with an optional offset towards the face center (median). I want to suggest adding an option for the offset to be down the “middle” of the corner (bisector).
Here’s an example of the two offset methods. The difference is really apparent on elongated faces.
bisector_vs_median
625×876 61.8 KB
The corner bisector node setup was taken from a
thread on Blender Artists
.

---

### Post #19 — SimonThommes — 2025-09-15T06:58:00.215Z

Please go to
Help > Report a Bug
and report this properly, so that the right people can take a look at it. This has nothing to do with the assets themselves.

---

### Post #20 — SimonThommes — 2025-09-15T07:02:29.602Z

Bobo_The_Imp:
I remember Jacques Lucke talking about potentially making that for the Distribute Points on Faces node, so it’s very cool to have that in this nodegroup. Would there still be any interest in doing that for for the Distribute Points on Faces node natively?
Yes, it could be more efficiently done builtin currently. So there’s still the option to either implement it natively, or breaking down the builtin node into more building blocks.

---

### Post #21 — SimonThommes — 2025-09-15T07:05:37.871Z

Destructive modeling will always be more performant, since instead of computing the result, it simply needs to be read from memory. In the future we will hopefully have features like caching in place to mitigate that to a degree.
If you have a concrete example that seems to obviously perform slower than it should you can report it as a bug and see what the triagers think. But please know that the developers are already doing their utmost to make Geometry Nodes fast, but it’s always possible as a user to build a setup that will be slow.

---

### Post #22 — SimonThommes — 2025-09-15T07:29:43.667Z

A
Transform
modifier sounds more reasonable to me here tbh, since this is really a separate operation, if all of them are supposed to be transformed the same.
One easy way to accomplish what you’re describing is to use the
Geometry Input
modifier, that is also implemented in this PR, to use a separate target object for the array, which can be animated however you want. And more advanced things, of course, can always be done in the node-editor.

---

### Post #23 — SimonThommes — 2025-09-15T08:33:04.404Z

tolkfan:
I want to suggest adding an option for the offset to be down the “middle” of the corner (bisector).
That seems reasonable to add to me

---

### Post #24 — SimonThommes — 2025-09-15T13:14:42.778Z

Hm, I see the point, but details like that are what the description is for imo.
Align Rotation
is something we are using in other places too and effectively that’s what it’s doing. The tangent alignment depends on the exact case and that is specified in the description.
That the surface normal is being used for alignment is implied on first glance in favor for shorter and consistent naming.

---

### Post #25 — tolkfan — 2025-09-17T11:39:00.791Z

Some feedback on the
Istance on Elements
node, specifically the way the instances are aligned to the element.
The “On Edge” option doesn’t align the way I think a user would expect an object to be aligned to an edge.
If I take a cross and instance it on edges, this is what the current node will do:
essentials_on_edge
837×842 45.7 KB
I think this is what a user would expect:
expected_on_edge
847×838 41.6 KB
This is the node setup for the alignment. The two vectors used to align are the
normal
and the
edge as a vector
(not sure if there’s a proper name for that :P). It’s also done in reverse order than usual: first the edge-as-vector, then the normal, otherwise it doesn’t align properly sometimes.
instance_on_edges
1828×783 77.6 KB
Overall I think the
Instance on Element
node should have a separate capture node for each element type, because right now it only has one capture node that captures the face normal and face tangent on faces. While points, edges and corners need different vectors for alignment.

---

### Post #26 — jamestomk — 2025-09-18T15:40:57.168Z

Perhaps this is off-topic but as a GN amateur, I’m thinking this is an area where AI could be very helpful, similar to AI writing your python script.  Is there any discussion topics on such approaches?

---

### Post #27 — And-Woo — 2025-09-19T07:52:40.266Z

Hi, I don’t know if it’s just my case, but working with Blender together with other softwares I always end up making a modifier that removes all (deletable) attributes, since exporting and importing generates a lot of useless attributes. Now that most (if not all) attributes are generic this could be achieved by adding a “remove attribute node” > “wildcrad” > “”
Edit:
maybe an operator would do as well

---

### Post #28 — 1D_Inc — 2025-09-21T10:10:19.127Z

Yes, looks more practical.
Exactness, CAD precisions are always more practical though.

---

### Post #29 — SimonThommes — 2025-09-22T08:29:05.921Z

Seems reasonable as well

---

### Post #30 — tolkfan — 2025-09-24T21:23:58.342Z

I think it could be useful for
Curve to Tube
to have a resample option to make the quads of the resulting mesh more evenly spaced.
resample_comp
1528×915 86.9 KB
There could also be a sub-option to specify one of 3 resample methods:
Count
and
Length
where the user manually inputs the values, like in the built-in node
Auto
, which is just the
Length
option, but calculated based on the (round) profile resolution
I like the
Auto
option particularly, because it produces very even quad topology, without the user having to input or change values all the time.
This is the
Auto
option node setup. I stuck it at the start of the chain in
Curve to Tube
, replacing the original resample node:
resample_nodes
1536×923 60 KB

---

### Post #31 — SimonThommes — 2025-09-25T08:50:00.109Z

Added this too.
It was quite a bit more involved, since this needs to take into account spline resolution to give useful results, so I’m estimating how much the resolution needs to be adjusted.
Also the Auto setting, doesn’t work great for custom profiles. I settled with using the lowest segment length for all splines in the custom profile.
Additionally there’s a scale setting to adjust this.
Seemed good enough to have this as the default.

---

### Post #32 — SimonThommes — 2025-09-25T08:52:47.816Z

Since there is less than a week left before the beta stage of Blender 5.0, please don’t post any more feature requests for these assets.
If there are concerns with how things work, those can still be addressed, especially bugs. But I’ll consider the feature set complete for this version.
Next steps are to create thumbnails, write descriptions and documentation and clean up the file to finish the PR.
Hopefully we can still merge this this week, to have a few days left before beta.

---

### Post #33 — tolkfan — 2025-09-25T17:23:31.933Z

Scale by Face Area
doesn’t keep the instanced elements… well, scaled. Putting a Square Root after it seems to fix it:
I have an overall question about Instance on Elements: will it support curves in the future? Yeah, you can put it on curves right now and it does instance the object, but not much more.
Instancing on curves would require different inputs and options, and I don’t think a node can tell if it’s being used on a mesh or curve object. So there would be no way to create those curve-specific inputs and have them be separate from the mesh ones.
Maybe the node should be renamed to
Instance on Mesh
, and at some point later a separate
Instance on Curve
node could be added?

---

### Post #34 — SimonThommes — 2025-09-26T11:33:24.601Z

The square root should be there, thanks for catching that.
About instancing on curves:
The modifier instances on the
control points
of curves perfectly fine. Other functionality can be found in the curve mode of the array modifier. Also, using Geometry nodes will always be available for additional functionality.

---

### Post #35 — nickberckley — 2025-09-26T11:39:14.784Z

One idea I have for curves is that when “Edge” mode is chosen, treat curve segments as edges and place an instance in the center of it. They’re not technically edges, and maybe we can rename it to “Edge/Segment”, but I’d rather use that than add new entry in the menu.
Points mode already works on all geometry types that can have points, including curves, so would be good to generalize Edge mode like that as well.

---

### Post #36 — tolkfan — 2025-09-27T08:45:11.335Z

In
Instance on Elements
the Random Value node that decides the Instance Index is set to a max of
100
, which means that a collection with 101 objects wont ever instance the last one. I think
Clipboard_09-27-2025_01
862×477 32.3 KB

---

### Post #37 — 3dioot — 2025-09-27T13:43:06.185Z

I encountered a bug with the “Curve to Tube” asset. It seems the “Extrapolate Radius” option only works correctly on one end of the curve. This happened to me when testing the daily build:
Broken: version: 5.0.0 Alpha, branch: main, commit date: 2025-09-26 23:58, hash:
db88381e7533
image
1702×1192 129 KB
I wanted to add the blend file but that file format is not allowed here for some reason so instead here is a link to my google drive.
drive.google.com
curve_to_tube_asset_bug.blend
Google Drive file.
Its great to see some GN groups being added as core assets. I am certain this will delight a lot of users.

---

### Post #38 — deadpin — 2025-09-27T19:23:59.316Z

Now that the assets are part of the official build (since last night),  bugs can be filed like normal rather than posting them here.

---

### Post #39 — SimonThommes — 2025-09-29T15:23:35.757Z

Thanks for noticing. This was an issue specifically with the round profile, costum profile worked fine.
I have a fix and will merge it soon. For the future, indeed please treat this as any other bud report on
projects.blender.org

---

### Post #40 — etti — 2025-09-29T23:55:07.389Z

There should probably be some clear distinction in the UI between the old array modifier and the new geometry node asset, since currently the only one is that the old one has an icon while the new one doesn’t.
Calling the old modifier something like “Array (Legacy)” could work.

---

### Post #41 — deadpin — 2025-09-30T00:01:19.300Z

A change made earlier today did just that with the names (and the new one gets the icon while the old one is empty).

---

### Post #42 — EvertonSchneider — 2025-09-30T17:16:00.738Z

Great work on these assets! I love the array.
I was testing it and want to ask if it’s possible to have an extra option to distribute copies based on their bounding boxes or something like that. Not an advanced user here, but I think that the accumulate field would do this job? Similar to that pizza boxes demo file from Blender 4.2 that you made
@SimonThommes
I konw that it’s maybe not the target here…

---

### Post #43 — EvertonSchneider — 2025-09-30T17:28:48.011Z

Another idea to make Curve to Tube more “animation-friendly” is to add a trim curve node or something similar. I tried here and it worked for this simple case, but I’m not sure if I did it right. Probably it’s not the way to implement this, but I’m not smart enough to do it properly.

---

### Post #44 — Middlericc — 2025-09-30T17:49:34.168Z

I guess at that point you could have the same thing by creating a really simple node setup to put before on the modifier stack. Also, that would give the user way more control over the logic on objects with multiple curves. To to that with the trim inside the group, you would need to remove the node (and inputs) from the group every time, or modify the group wich is not ideal.
I can see why that would be good tho, new users may not know how to trim the curves before intuitively.

---

### Post #45 — MasterOfNone — 2025-10-01T01:46:06.631Z

I love the geometry nodes assets! I’m testing it now. Just a question, Is there a way to change the array graph in the graph editor to be more smooth in motion and not in a stepped interpolation?

---

### Post #46 — SimonThommes — 2025-10-01T07:08:56.684Z

@EvertonSchneider
No more features will be added to these assets for 5.0, as I mentioned in a previous post.
The bounding box is used for the Line/Relative mode. If this is about stacking multiple elements, that would be a separate asset, which we might add in the future.
Trimming a curve is something I see as out of scope for this modifier. That can easily be done in a separate operation before and regards the curve itself, not the way it is meshed. These assets are all usable as nodes themselves, so it should be easy for users to wrap them in a simple node-tree that just chains operations.

---

### Post #47 — SimonThommes — 2025-10-01T07:11:46.637Z

Here you are animating an integer property, which cannot take fractional values. So it will always be stepped. There is no logical definition for a count of 5.4 steps.
If you want things to move smoothly you will need to create a custom setup for this. You could use the output of the array modifier though, turn off
Realize Instances
and delete/move instances procedurally with nodes afterwards.

---

### Post #48 — deadpin — 2025-10-02T21:22:37.202Z

For Scatter on Surface, was there a reason in particular to not enable the Object Info → As Instance box? Either by default or as another input.
Without that enabled we can’t say scatter Volumes on meshes. Nor can we make use of USD’s current point instancing export support; it currently needs an instance in the input unfortunately.
image
847×500 60.4 KB

---

### Post #49 — SimonThommes — 2025-10-03T15:36:43.429Z

Hm, interesting. I wasn’t aware of those limitations.
Generally it seems a bit weird to me to add an additional layer of instancing that isn’t generally necessary. But I suppose that’s also how it’s set up for the
Instance on Elements
modifier.
I just did some testing and this is the same also for instancing other things, like lights and cameras. Especially in combination with the
Visual Geometry to Objects
operator this would be nice to support. Then we can use this to actually scatter instances of objects and collections around.
I’m putting it on my list to always enable this
Seems like the better option than exposing yet another setting that most users don’t need tbh.

---

### Post #50 — Roggii — 2025-10-04T16:00:03.313Z

Hello,
UV offset for the new array modifier will be great to have for 5.0.

---

### Post #51 — Baardaap — 2025-10-04T21:41:31.254Z

I was playing around a bit with these and I was wondering how the documentation was planned to work. Are these kind of bundled  asset supposed to have documentation in the main manual? Or should the be more of a standard way to add documentation/help to any node tree? I think that would be very useful to have anyway. Especially for GN trees now accessed through the modifier interface it feels a bit weird to have some of the modifiers be documented in the online manuals and others missing from it, but I could imagine a default help button on the modifier menu and node group opening some sort of inline help/documentation would be very useful, also for people creating reusable node trees.

---

### Post #52 — SimonThommes — 2025-10-06T07:01:52.291Z

Since there is currently no way yet to iterate over specific types of attributes, this will not be included for 5.0

---

### Post #53 — SimonThommes — 2025-10-06T07:03:29.210Z

The assets will be documented just like any other Blender feature. This still needs to be done.
The node-trees themselves also still need a pass of cleanup and some commentary.

---

### Post #54 — Roggii — 2025-10-06T12:02:18.221Z

That’s a shame. Thanks again.

---

### Post #55 — SimonThommes — 2025-10-06T13:21:57.926Z

This modifier does output an
instance_index
attribute, which you can access in the shader to achieve essentially the same thing for shading though. This just needs a little bit of math and shader nodes.

---

### Post #56 — Charles — 2025-10-09T13:41:37.425Z

Hi, first of all great job and all that.
Secondly, would you consider to add some of the new volume grids  nodes to the assets? Something basic like to have the boolean operations with laplacian would be nice, I know they are not that hard to setup but it would be easier for the new users to have them exposed.

---

### Post #57 — SimonThommes — 2025-10-09T13:52:43.062Z

Blender 5.0 has entered beta yesterday, so no more features/nodes will be added. Only bug fixing from now.
Blender Projects
blender
The official Blender project repository.
The grid nodes are going to be quite fundamental for now. We will likely add more assets in coming releases.

---

### Post #58 — EvertonSchneider — 2025-10-09T14:29:53.873Z

Thanks
@SimonThommes
, this is huge! Thanks for the hard work on this! I spread my gratitude to all involved! Blender experience will be greatly improved with these tools.

---

### Post #59 — Luca — 2025-10-31T12:44:39.575Z

While experimenting with the new Array modifier, I noticed that in Edit Mode the gizmos can get in the way. In the screenshot below, when I try to move the selected edge, I accidentally activate the rotation gizmo. It would be really useful to have an option to toggle the gizmos on and off in each geometry node modifier, rather than having to disable the active modifier gizmos for the entire scene.
Definitely not a bug, maybe a feature request for 5.1?
image
782×560 57.1 KB

---

### Post #60 — SimonThommes — 2025-10-31T13:05:30.270Z

Yea, more of a feature request. That’s the kind of thing we need to see once 5.0 is released and people are using the assets.
For now:
Only active AND selected objects have their modifier gizmos drawn. if you deselect the object before entering edit mode, the gizmos are gone.
I agree though, that the current behavior feels a bit strange.

---

### Post #61 — FreeMind — 2025-11-01T14:00:09.463Z

How about some basic non-destructive shape primitives with gizmos to adjust them?
Like… Shift+A > ND primitives > Cube/Sphere/Cylinder/Grid

---

### Post #62 — And-Woo — 2025-11-19T21:04:57.001Z

For the new array modifier, it would be handy to add the “object” option to the “circle” mode, to use as array pivot. So the array would be around another obect instead of itself.

---

### Post #63 — dimitar — 2025-11-20T07:41:19.056Z

Agreed! That’s the first thing I looked for after adjusting the basics of the new array modifier

---

### Post #64 — SimonThommes — 2025-11-20T08:53:01.643Z

I’m not convinced this would be better than simply using a copy location constraint. That way you would avoid the object origin from being potentially far away from the data.
What’s the use-case you have in mind?

---

### Post #67 — And-Woo — 2025-11-20T09:20:59.994Z

I work in a manufacturing company, and our products are often circular, so the details and additional elements are often radial
Let’s say if you place an object in the scene and its transforms are intentional, and you just want to make a circular array around the center of the scene, at the moment you have to apply all the transforms in order to use the new array modifier.
My expected workflow is: you put an object in the scene, you rotate it and place it however you like, in order to keep things non-destructive you don’t apply the transforms because they make sense as they are, then you use an empty just to define the axis of the circular array

---

### Post #68 — SimonThommes — 2025-11-20T09:29:42.736Z

I see, thanks for being more specific!

---

### Post #69 — And-Woo — 2025-11-20T09:33:10.220Z

Iexpect this

---

### Post #70 — Abraham_S — 2025-11-20T12:19:39.749Z

Just to second this
@SimonThommes
I’ve been following this thread for a while,  as I’ve found these new modifiers to be the most exciting aspect of the 5.0 release, especially as a motion designer used to the
Cloner
tools in Cinema 4D.
As
@And-Woo
(and others) might have pointed out, it’d be
amazing
to be able to control (and animate) the rotations, scale and position of the individual instances, that’s something I, and countless others used to Cinema 4D, would love to have, as the current implementation just doesn’t really allow for that (easily).
(I’ve got no Geo nodes knowledge, so unsure how possible it even is, but again, it’d be a
big
deal for so many of us🙏🏾)

---

### Post #71 — SimonThommes — 2025-11-20T12:35:25.499Z

Not to dismiss what you’re saying, but try also using the
Geometry Input
modifier in conjunction with the array. That way you can disconnect the transform of the array and the source object and that might help with what you’re trying to do. Besides that, it should be relatively simple animating the instance transforms procedurally afterwards with Geometry Nodes.
Advanced use-cases will always have most flexibility using the node system itself.

---

### Post #72 — Abraham_S — 2025-11-20T13:14:52.889Z

Thanks for the swift reply on this
@SimonThommes
, you’re a godsend.
Again, as someone with very little geo nodes knowledge, a screenshot for how to set this up could be helpful.
But more importantly, this is, again, something that could benefit
everyone
if it was built-in in an artist-friendly UI and didn’t need extra tinkering to set up.
Appreciate every use case will always require tinkering the nodes, but as some have already pointed out, this is an expected behaviour/feature many artists would expect from other DCC programs. As someone who often jumps between C4D and Blender, it’d just speed things up drastically and make the learning curve lower if built-in.

---

### Post #73 — Hadriscus — 2025-11-21T09:43:21.555Z

Abraham_S:
As
@And-Woo
(and others) might have pointed out, it’d be
amazing
to be able to control (and animate) the rotations, scale and position of the individual instances, that’s something I, and countless others used to Cinema 4D, would love to have, as the current implementation just doesn’t really allow for that (easily).
If you mean animate individually and by hand, geonodes doesn’t make this very easy. You’d essentially need a transform node, a separate geometry node and an associated gizmo output for each individual instance.
If you mean procedural animation, then it’s easier but it depends on what you want to do

---

### Post #74 — Abraham_S — 2025-11-21T10:19:56.584Z

I was more meaning the same animation/transformations (of the instanced object) across the the array, like so:
Anything more advanced like what you and
@SimonThommes
are hinting at, I imagine one would have to really fork the nodes, but for the above, I think having a somewhere in the new Array modifier, with those transform options, built-in, would be terrific - many of us don’t have the knowledge (or time) to set this up.
(First time feedbacking on here, so thanks for bearing w/ me guys
)

---

### Post #75 — filedescriptor — 2025-11-21T10:37:06.128Z

I removed the GIF since it contained copyrighted material. See
Copyright guidelines for devtalk
.

---

### Post #76 — SimonThommes — 2025-11-21T10:38:26.549Z

@Abraham_S
Please
no screenshots/screenrecordings from other software
.
As mentioned before, you can achieve this exact behavior by combining the Array with the Geometry Input modifier.
I think adding a pivot/center object input to the circular array in the future is reasonable though.

---

### Post #77 — Abraham_S — 2025-11-21T10:49:41.549Z

My apologies, I wasn’t aware of that rule, I’ve now replaced the GIF with one demonstrating the desired behaviour within Blender, hope that’s ok.
I’ll be looking into trying that on the current Array modifier on my end, thanks again
@SimonThommes
, but yeah, however possible it’d be to add those (keyframable) options (scale, rotation and position) to the next iteration of this new Array would be
extremely
valuable, and can see this being helpful to the other modes (e.g Transform) too, where not already possible.
(Thanks again for being so receptive of this🙌🏾)

---

### Post #78 — And-Woo — 2025-11-21T13:23:53.969Z

I think it would be ideal if the object defines even the rotation, not only the location of the pivot (the object defines the entire axis)

---

### Post #79 — MartinZ — 2026-01-18T12:57:40.097Z

I am missing the ability to use multiple offset modes at the same time with the new array modifier. There are situations where I might want to keep the gap fixed size, but maybe edit the dimensions of the arrayed object, so with new one that’s a regression while with the original one, I can set relative offset to what it needs to be and then add some fixed offset to that with offset mode and I am free to change my object any way I want not having to adjust the modifier every time. Also the endpoint mode is awesome, but in reality since gizmo transforms don’t support snapping, I find it pretty much useless in day to day tasks so it doesn’t add much for me.  End caps are missing… Those can be used for a lot of things… So, I just avoid using the new array modifier altogether and use the legacy one all the time and if I needed some specific behavior, I would just construct my own modifier, but since the current array node group is so complex(and messy! especially for an asset) it’s not very useful for a starting point either. So my personal experience is that default array modifier could be improved. I don’t think it matches the original yet.

---

### Post #80 — slowk1d — 2026-03-05T11:33:51.018Z

Hello! First of all, thanks for the work on these assets, especially the array modifier!
Regarding this modifier, sometimes I wish there was a switch directly in the modfier UI for turning off the gizmos.
I don’t use them, and they get in the way many times when I want to translate the object: more than one time I confused the modifier gizmo for the regular move gizmo. Is this addition something that can be considered for future releases? Thanks

---

### Post #81 — SimonThommes — 2026-03-05T11:47:38.470Z

The new Array was not meant as a full replacement just yet, that’s why there’s no feature parity. The ability to use constant and relative offset together seems definitely reasonable to support, same for end caps

---

### Post #82 — SimonThommes — 2026-03-05T11:50:06.188Z

This is a feature request for Blender, not something I would bake into the implementation of the asset. It’s been discussed before to give the user control over what gizmos of a modifier are shown, but it hasn’t been prioritized yet.
Right now you can disable the gizmos of the active modifier in general for the viewport in the gizmo settings:
image
402×332 31.7 KB

---

### Post #83 — slowk1d — 2026-03-05T23:30:21.572Z

Oh, I didn’t imagine it would have been considered a feature request. My idea, as I envisioned it, would have been a couple of switch nodes+join geometry so their visibility could have been turned off, I wasn’t thinking of a specific new feature just for it, but maybe I’m missing something.
Anyway, thank you for the tip, I forgot about it!

---

### Post #84 — Abraham_S — 2026-05-05T10:21:56.830Z

@SimonThommes
just seen the
improved rotation alignment
in the 5.2 Alpha and seems to work great! Thank you so much for taking the time to implement this with everything you had going on!
Though, while quickly testing it, I noticde how in the
Line
shape mode, none of the the rotation options work anymore (in none of the Offset modes), as shown below:
Appreciate this might still be a work-in-progress, but figured I’d flag it now, in case it hadn’t already.
Again,
thank you
for all the work on these Simon

---

### Post #85 — SimonThommes — 2026-05-05T11:02:55.900Z

Thank you for the kind words, I’m glad the change is working well for you!
The issue you found doesn’t have anything to do with the change in the asset and is a bug in Blender. Thank you for pointing it out! I created a report here:
Blender Projects
Geometry Nodes: Rotation in `Instance on Points` node not respected in Array...
**System Information**
Operating system: Linux-6.18.26-gentoo-dist-x86_64-AMD_Ryzen_9_9950X3D_16-Core_Processor-with-glibc2.42 64 Bits, WAYLAND UI
Graphics card: NVIDIA RTX 6000 Ada Generation NVIDIA Corporation NVIDIA 595.58.03 Vulkan...
In the future, when you find an issue like this (even in the alpha version), feel free to report it as a bug. Issues like this shouldn’t occur, not even in the alpha build!

---

### Post #86 — Abraham_S — 2026-05-05T11:22:58.251Z

(Least I could do, these new modifiers are my
fav
additions as of late - hope they keep being worked on!)
Thanks for creating the report, I’ve admittedly never reported a bug, but will learn how to do so for future issues. Will keep an eye for any updates on the issue. In the mean time:

---

### Post #87 — Abraham_S — 2026-08-26T08:46:02.975Z

Hello
@SimonThommes
, hope you’ve all been well at the HQ
,
Someone might have mentioned this before, but while the current
Curve to Tube
modifier (with rounded caps
) has been a great addition, I just can’t help but need/expect trimming options along the curve.
Below is a very crude demo given my 0 knowledge of Geo Nodes.
When applying it to a curve, being able to trim its Start, End
and
Offset its results, along the curve would be
extremely
useful, especially for animation (akin to After Effect’s
Trim Path
function for any familiar with that).
Appreciate you must be heads down on other projects/modules, especially w/ Bcon looming, but how feasible do you think it’d be to implement (for 5.3)?

---

### Post #88 — JulianPerez — 2026-08-26T20:19:49.075Z

DISCLAIMER: I’m not an expert by any means and there’s probably a better way to do it, but I modified the node group for myself just by adding the Trim Curve node just before the whole resampling thing, here:
imagen
1531×408 120 KB
And a close up of that section of the node tree, with the 3 new nodes added (Trim Curve and an input for Start and End):
imagen
1080×471 92 KB
Be aware that if you have a curve object with several disconnected curves, it will affect them all at the same time, to be able to trim them in different order the solution is probably a lot more convoluted, but that’s far from my current GN knowledge hehe

---

### Post #89 — SimonThommes — 2026-08-27T08:54:35.631Z

To be honest, I don’t really see this as desirable functionality for the
Curve to Tube
node-group.
Trimming the curve is an operation that can easily be done beforehand. It doesn’t need to be integrated into the meshing.
The point of modifier assets is that they can be arbitrarily modularly combined. These high-level node-group assets are a bit of an exception in that they bundle a lot of functionality together, but adding this would imo cross the line towards bloating the modifier with unrelated operations.
There could definitely be a separate
Trim Curves
modifier, but I don’t see this as very high priority, since it is trivial to build with existing Geometry Nodes.
The fact that you say you have 0 knowledge of Geometry Nodes and still managed to get exactly the behavior you are describing, proves to me that this is a valid approach. Maybe we just need to make it more convenient/less scary for users to get started with Geometry Nodes.
I do want to also point out that there is already the `Trim Hair Curves` node-group asset, but this has some specialized behavior for hair, so it might not be what you’re looking for.

---

### Post #90 — Abraham_S — 2026-08-27T09:25:33.395Z

Thanks for taking a look at this post Simon , always appreciated.
While it definitely doesn’t need a separate Trim modifier just for that, as someone (like many here) jumping between other 3D and 2D tools, I don’t see trimmable option as bloat, but
very
useful and expected. Every time I come back to this modifier, I instinctively look for it as it’s one of the behaviours/features inherent with curves.
GN in general could defo be less intimidating and more approachable, especially for people looking for specific behaviours, but as a motion designer, animating a spline/curve should be an out of-the box thing to be done
quickly
, even for this modifier.
I was able to recreate
@JulianPerez
’s suggestion (thank you!), but again, for animators/motion designers this feels essential enough to add imo.
And the 2/3 extra options (including an offset) in the modifier panel to allow for something
so
powerful, would be worthwhile.
image
850×744 73.9 KB
I know these assets have guidelines to avoid scope creep, but strongly believe it’s worth implementing
(if others agree ofc)

---

### Post #91 — aalmaluar — 2026-08-27T11:35:36.066Z

Hey hey amazing humans!
I ran into a strange behavior when trying to replicate a standard curve-deformation setup after the new Array modifier.
But first, I am still a beginner with Geometry Nodes, so I apologize if this is an intended limitation rather than a bug.
The Setup:
I want to array an object to fit the length of a curve, and then deform that arrayed geometry along the exact same curve.
Expected Behavior (Legacy Workflow):
Using the legacy Array Modifier set to Fit Curve, followed by a Curve Modifier targeting the same curve, the mesh duplicates and deforms perfectly along the path.
Actual Behavior (New Geo Nodes Array):
Using the new Geometry Nodes Array modifier set to fit the curve, followed by the same Curve Modifier, the geometry deforms strange.
I have attached a video demonstrating the issue side-by-side (Legacy Array vs. New Array).
Is there a different workflow intended for deforming curve-fitted arrays in Geometry Nodes, or is this a bug with how the new Array asset interacts with the legacy Curve Modifier?
Thank you for being amazing!

---

### Post #92 — etti — 2026-08-27T16:00:23.274Z

There could definitely be a separate
Trim Curves
modifier, but I don’t see this as very high priority, since it is trivial to build with existing Geometry Nodes.
I feel like this is the way to go, but a potential issue is that Curve to Tube integrates Resampling in it, and I think ideally you’d want to do trimming after resampling. So resampling may also have to be split into a separate modifier for that.

---

### Post #93 — RonanDucluzeau — 2026-08-28T14:57:53.845Z

aalmaluar:
Is there a different workflow intended for deforming curve-fitted arrays in Geometry Nodes, or is this a bug with how the new Array asset interacts with the legacy Curve Modifier?
The new Curve Mode of new Array is already supporting the deformation. It should not be followed by another Curve modifier. You are applying curve deformation, 2 times.
Abraham_S:
I was able to recreate
@JulianPerez
’s suggestion (thank you!), but again, for animators/motion designers this feels essential enough to add imo.
Grease Pencil object has several modifiers to animate curves length.
Length modifier, with Start and End settings and Absolute/Relative modes for the values.
Build modifier, based on a timing ( set from a factor or number of frames), proposing 3 different transitions ( Grow, Shrink, Vanish) and 3 different modes to handle several splines ( Sequential, Concurrent, Additive ).
Older Build modifier of Curve and Mesh objects has not so many settings. It make mesh faces or curve polygons disappearing.
For animation of curves generated through geometry nodes, from a mesh, that would make sense to create a Trim Curves modifier, combining those GP modifiers, providing modes that are not handled by old Build modifier, acting differently on geometry.

---

### Post #94 — aalmaluar — 2026-08-28T15:05:45.455Z

RonanDucluzeau:
The new Curve Mode of new Array is already supporting the deformation. It should not be followed by another Curve modifier. You are applying curve deformation, 2 times.
It doesn’t deform based on the radius of the points like the legacy Curve Deform modifier does.
Or am I missing some settings?

---

### Post #95 — RonanDucluzeau — 2026-08-28T15:14:54.776Z

Indeed, it does not. That is a limitation of the modifier.
Other geometry nodes would be necessary to scale instances from radius of spline.

---

### Post #96 — aalmaluar — 2026-08-28T15:24:50.035Z

so as a non-geometry-node-familiar-person it is just better to use the legacy modifiers or there are any plans on reworking the new array modifier?
thank you for your reply and time

---

### Post #97 — RonanDucluzeau — 2026-08-28T15:34:47.286Z

Well. This thread is about feedback.
Maybe, new modifier could be updated to handle that.
Maybe, Instances on Elements modifier could be rethought to handle curve geometry and its attribute, too.
Maybe, a Transform from Attributes modifier would be welcomed.
For the moment, if Legacy modifiers are still present, it is to be used  for what is still unsupported by new ones.
Ideal solution is to build yourself, perfect custom Geometry Nodes modifier for wanted result.

---

### Post #98 — Abraham_S — 2026-08-29T10:21:35.079Z

Thanks for feedbacking on this​
. I’ll be honest, I have no idea what ‘resampling’ means in this context, why would this make adding a the trimming options less feasible
@etti
?
I guess from my experience, I don’t see trimming just as something to be done to the mesh beforehand and keep static, but literally as something I’d want to animate if there’s a curve, and I’m sure I’m not the only one, even if that messes the UVs (could always use a procedural material).
This Curve to Tube is one of those modifiers that while built for a certain use case, in real use cases, it’ll probably be used in many, non-static, ways too and trimming just seems like an obvious thing to have in there out of the box, in one way or another. (Anything more specific/niche then, sure, dig into GN, but ideally not for this…
)

---

### Post #99 — etti — 2026-08-29T19:53:40.112Z

I’ll be honest, I have no idea what ‘resampling’ means in this context, why would this make adding a the trimming options less feasible
@etti
?
Resampling essentially “recreates” the curve, so if the curve is trimmed before resampling, it may give different results than if it was trimmed after resampling. It’s especially noticable if using the count and length modes.
See:

---

### Post #100 — Abraham_S — 2026-08-31T10:25:32.859Z

Thanks for the explanation, based on that demo, it seems like having a resampling node after the trim curve could be the way to go for most use cases then(?). I might be missing something here, but can’t this not be brought forward to the Curve to Tube modifier then?
Again, this might still mess up UVs, which I’m personally ok with, if I’ve got trimming options out of the box…

---