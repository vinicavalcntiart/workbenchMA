---
titulo: Experimental Physics Feedback for Blender 5.2 LTS
autor: jacqueslucke
url: https://devtalk.blender.org/t/experimental-physics-feedback-for-blender-5-2-lts/45449
data: 2026-06-24
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — jacqueslucke — 2026-06-24T16:42:12.346Z

This thread is used to gather user feedback on the new experimental hair and cloth physics in Blender 5.2 LTS.
See the
release notes
for an initial introduction on how to use the system. A lower level description of the
declaration simulation framework
and
xpbd solver
node are available too.
We know that there are a few missing features like cloth self collision. Also, in future releases we intend to improve existing solvers as well as new ones which will ideally be combined through substepping.
Besides general feedback, there are a few specific aspects that would be interesting to get constructive feedback on:
Hair Surface Attachment: Does the implemented method for attaching hair to a surface work for all use-cases? Does it work out of the box or does it need a lot of fiddling around? What can be improved about it?
Forces: We didn’t have time for this release to ship a bunch of new forces to use with the system. One can build custom forces though. Does setting up custom forces work well? What are limitations of the current approach? What forces should be shipped with future versions of Blender?
Hair Animation: Hair simulation can be expensive and is often not necessary for simple cases. What features should be added to the “Animated” mode to fake hair dynamics?
Cloth: Besides self-collision, what are missing high level feature from the Cloth Dynamics group?
Hackability: How difficult is it to add some basic custom behavior to the high level dynamics groups? Please share some of the stuff you did or tried to do.
Workflow: As usual, we try to have a modifier and node based workflow. How well do they work for you? How hard is it to integrate physics into larger setups?

---

### Post #3 — Volkashin3D — 2026-06-24T18:16:42.835Z

Accidentally hit enter earlier, sorry
Hair Surface Attachment: Does the implemented method for attaching hair to a surface work for all use-cases? Does it work out of the box or does it need a lot of fiddling around? What can be improved about it?
If you mean adding a Dynamic Hair node set to animation, it does seem perfect. Idk how you could improve it, it no longer requires any nodes on the scalp so if you ask me it is perfect. I assume it warns if there are unattached hairs like the old one. I didn’t test this
Forces: We didn’t have time for this release to ship a bunch of new forces to use with the system. One can build custom forces though. Does setting up custom forces work well? What are limitations of the current approach? What forces should be shipped with future versions of Blender?
I want forces and I want them now. Jokes aside, setting up custom forces works decently. The biggest limitation is GN knowledge. I seem to struggle quite a bit with that
What forces? All forces, of course. The Geo Node knowledge is potentially a huge limitation, which is why I am not really joking when I say all forces you can think of. Simple wind with noise seems pretty easy, others maybe not so much.
Hair Animation: Hair simulation can be expensive and is often not necessary for simple cases. What features should be added to the “Animated” mode to fake hair dynamics?
Honestly, I thought that was out of scope, but if you do that, this will absolutely wipe the floor with the old particles system. Some simple either faking, or control through some kind of armature would be
perfect
.
After re reading this, if it’s possible, faking with a cage for collisions would be an absolute banger feature as well, even if we have to make the cage ourselves.
Hackability: How difficult is it to add some basic custom behavior to the high level dynamics groups? Please share some of the stuff you did or tried to do.
After re reading I wasn’t sure if this refers to editing the XPBD related nodes, or using them in the more intended way of adding stuff with bundles, so I’ll separate in two:
Intended way for adding forces etc:
Very confusing at first. If it wasn’t for Falk I’d be lost during the 5.2 alpha. It didn’t seem intuitive at the time. Now, I could probably figure it out with the information in 5.2 Release Notes. I just checked to make sure, and yeah, the way effectors work by adding them through other geometry is something I couldn’t figure out without the information in 5.2 Release Notes. It’s very helpful. On this part, I suppose the only thing I could use is more examples for different kinds of forces
Doesn’t really make much sense if you add them in/before 5.3
Something hit me while writing this, having to only release node group presets during alpha versions doesn’t really make sense to me. It would be nice if they were exempt from this rule.
Unintended way of editing XPBD:
Terrible for me, Geo Node skill issue
I’ve been trying to use XPBD from the cloth sim for particles to spawn in and out mid simulation and I couldn’t figure it out on my own. I needed the help of multiple people lol. If I open these nodes, the first thing I see is these weird new bundles that I don’t know where they go, what they do, how they are accessed and how to add or remove data in them. Closures are kinda confusing too if I’m being honest. That said, there’s at least a few people out there that managed to figure out everything I couldn’t, but I think I may be the majority on this one…
Workflow: As usual, we try to have a modifier and node based workflow. How well do they work for you? How hard is it to integrate physics into larger setups?
Before beta it was complicated and annoying to figure everything out. Since beta it’s been a breeze, an absolutely amazing experience. I have no complaints
except more forces
. Maybe consider adding a preset for point cloud simulation. I managed to make some really interesting simulation with XPBD, I loved it.
For hair specifically, I already made a bunch of test animations. They came out outstanding. I think there’s only 1 thing that could be improved and that’s an easier way of handling the substeps. That’s about it, but at the same time, it’s not a huge issue. I can’t think of any complaints about integrating them.
Regarding performance
I have one pretty big concern about XPBD. Adding collisions is a significant impact on performance. I am concerned about cloth sim’s self collisions in the future. Do you have any room for optimizations in the XPBD setup? It’s very impressive, but in
real
scenes the performance specifically is between “it’s ok” and “god help me” when it comes to bake speed and Ram usage. I was forced to remove all vertex groups before baking. The data being carried over and written for each frame wasn’t obvious to me and I only noticed it after some 60 frames took 12GB of disk space
Further, albeit not limited to hair sim, we could use “DEF-*” functionality where it deletes every deform vertex group. Or even better, an inverted one where we can for example give the hair related vertex groups a prefix and delete everything except that one prefix.
I also noticed one issue tho I don’t know if it’s XPBD necessarily. Blender tends to crash when you link a heavy character with heavy hair/fur that has the simulation inside XPBD set to Packed. No crash after setting it to Disk.
That’s all I got. If you have any specific questions feel free to ask. Also if you are interested in seeing the animations I made with the hair simulation I can link them, they are on YouTube. I figured I’d ask first to not spam.
Edit: I hope you enjoy the essay. I got carried away.
Edit2: It seems I missed one pretty important detail. The Hair Dynamics node set to animation is almost twice as slow as the old Surface Deform one. That’s not ideal when it comes to making Hair Dynamics the default.
Edit3: I would like to see an option for collision offset like we have on the old physics collision settings. Right now I am forced to use shrinkwrap after a simulation if it touches the scalp too much cause it tends to clip from time to time. I don’t want to use edge contacts cause that takes the simulation bake time to “god help me” in 1 click
Edit4: Just caught this. If you bake while you have a “Bundle path not found” warning, you have to delete the bake to make it go away.

---

### Post #4 — Draise — 2026-06-24T19:30:37.744Z

UX and Assets: The Physics stack and operators and types should all have equivalent nodes out of the box, with similar or same settings.
This will allow familiar UX to existing pipelines, but allow nodal flexibility, and have familiar settings where old documentation would remain compatible. This will also make the physics in nodes feature complete out of the box with the additional flexibility of chaining.
image
344×582 16.9 KB
Chainability: In general I found the nodes hard to understand with the open string field (reminicent of the attribute named fields of  Blender 3.0) and it’s disconnect.
An alternative is to have a simulation stack, where you plug in the forces and elements into the node stack to run one into the other in a simple “chain” top to bottom.
This also poses tricky domain issues, how do you define what physical domain your are simulating? The get, read, set nodes for the physical domains should be assets out of the box instead of named attributes you write unknowningly in these field.
My first impressions was.. well.. nope, not sure how to use this, will need to read the docs - but ideally as a tech artist or artist, you want to drag, drop, plug in sequence.. and it will just work. Tooltips should suffice, no need for extra deep documentation before you get started.
Demo files showcasing each asset would be useful.

---

### Post #5 — redmser — 2026-06-24T22:25:34.008Z

Great feature, love to see how it develops. I tested a lot of this during alpha, so some later updates make some of my notes and feedback redundant.
I had a bunch of problems with mismatching (world/local/object) spaces. This was due to…
1a. If you add hair/fur to an object, the Curves object inherits the surface object’s scale. But the simulation assumes a scale of
1
and does not propagate the scale automatically → if curves are scale
0.1
then hair will be 10x as long.
1b. Because of this scale issue, colliders and forces were also in the wrong space, and had to be transformed as well. This ended up in a transform matrix mess which IMO should all be handled by the hair dynamics node group (UPD: colliders are world-space only now, thus they are fixed).
image
1170×616 76.9 KB
Set Attachment Surface
for an armature-animated surface did not work when using “Object” mode. I learned that this is because not only must you enable “Add Rest Position”, but also add a “Capture Rest” node group (UPD: adding fur does this on its own now, I appreciate the change!). While I like the design and understand why it’s done, I expected some form of error if the rest geometry is missing, instead of silently continuing. I used “Geometry” mode instead, which allowed for more control and made more sense to me.
I created a custom force that looks like brushing fur - no precise collisions (to avoid explosive behavior), but just “fur under a brush should move”. Didn’t know how to easily copy the brush object velocity, so you’d need to manually animate it. The system was flexible enough to allow me to easily create this (although again, wrangling the transform matrices stuff took some trial and error):
image
2104×664 117 KB
Was fiddly because I had to work without the Viewer node here, since it gave me transformed results. And I could not quite intuit in what context fields were being evaluated on / what geometry I should feed as Viewer input (is it each curve point? If so, Viewer would show non-surface-deformed curves, making it harder to work with).
Hair that is clipping into a collider in its rest pose caused explosive behavior that did not settle over time. I did not know how to resolve it. My workaround was to just comb the hair, or move the collider.
I tried to create rope physics with the cloth simulator, using a curve turned into a surface mesh. But I had no idea how to compute
rest_length
(and if I didn’t override it, then the rope got like 3x longer than I’d expect, even without bendiness or stretchiness). Best results I got was from
1 / numberOfSubdivisionCuts
but the rest pose was still chaotic.
image
837×409 33.4 KB
image
818×773 62.6 KB
A node group for rope physics, instead of going through cloth simulation, could be useful (but that would probably not be an essential asset).
I exclusively worked inside a larger node tree, instead of the modifier approach, since I was modifying existing fur node groups that were complex and not made by me. It was not as simple as “replace deform surface node with simulation node group”, because of various attribute transfer stuff happening with guide hairs, so I had to simplify parts of the node group.
The UX for baking is not great, I wish for bake/clear bake controls directly in the modifier, instead of it being in other editors or tabs. I also can’t use a custom frame range for baking, since the simulation zone is buried deep in groups. And finally, it feels hard to clear the “striped bake cache”, I mean this:
But I think this is a problem in more places in Blender (e.g. I often need to change the fluid sim resolution back and forth, since the cache did not clear after some effector changes). So maybe just having the delete cache button closer to the modifier would help. And maybe more aggressive cache clearing when editing the node tree? Not sure…
Tearing is an AMAZING feature and I am very happy with how it is set up out-of-the-box!
It is unclear to me how “Animation” mode hair dynamics differ from the “attach curves to surface” node. Is it superseding it, or are there (going to be) differences?
Very excited to see what’s coming in the future, hope some of this helps!

---

### Post #6 — TheLittleMouse — 2026-06-25T00:48:37.670Z

jacqueslucke:
Hair Animation: Hair simulation can be expensive and is often not necessary for simple cases. What features should be added to the “Animated” mode to fake hair dynamics?
One feature that I think is pretty important is the ability to loop an animation or simulation. When we pose bones, all we have to do is to keyframe the bones on a frame, copy and paste those keyframes to another frame, move the bones to a different location on a frame in between, then we have a loop. I would like to be able to do the same with hair, or in a similar way.
I am not sure if this next feature is relevant in this discussion, but I think it kind of is. I think hair made with hair cards or mesh, instead of curves, will continue to be used. I think we would not use the hair solver for them, because that is for curves. Instead we would use cloth simulation for hair cards or mesh hair, as we did previously. Again, I’d like the same option to make a cloth simulation loop.
And for cloth, I would also like the option to animate it like posing bones, same with hair. Of course, I know we can already rig and pose cloth with bones literally. So that’s not what I want. I just want more control over the simulation.

---

### Post #7 — JulianPerez — 2026-06-25T03:58:48.580Z

jacqueslucke:
Hair Animation: Hair simulation can be expensive and is often not necessary for simple cases. What features should be added to the “Animated” mode to fake hair dynamics?
I have to spend some more time testing everything to give an answer/feedback on the other points, but for this one I feel there should be a way to actually rig hair curves, not only depend on simulation or fake physics. I have found that is pretty hard to have curve hairs follow an animated mesh, and the method of converting a rigged mesh to curve guides and then generate more hair curves from those guides is also convoluted and tends to be very unpredictable.
Another thing, is it possible to simulate just a few curve guides and then generate more hair curves after the simulation that are stable over time? I haven’t been able to find a way to setup a hair system like that, anything like noise, clump, frizz, and other hair node groups that are setup AFTER the simulation seem to be calculated every single frame instead of just at frame 1, so when animated everything jumps constantly and it just looks bad.
image
1754×990 255 KB
This is the kind of setup I’m talking about, is this supposed to work, or am I using it wrong?
EDIT: Here’s the sample file from that screenshot, it’s a very simple setup but just in case it’s useful:
drive.google.com
HairGenAfterSim.blend
Google Drive file.

---

### Post #8 — JoelR_VC — 2026-06-25T06:20:46.492Z

I made a similar test, but with an object that had object-level animation; that seemed to work fine.
hair_dynamic_test.blend
(1.4 MB)
However, if the mesh is deformed(your example), the entire subsequent chain misses the relative space to where the transformation is supposed to occur. An option for a reference UV map should be added to the “Interpolate Curves” node group to maintain the generation during deformation. The other node groups should be reworked to apply deformation based on a relative base position(or a bake).
That applies to the workflow where you simulate first and then generate interpolated hairs and create the groom. But what happens when I already have an approved hairstyle and I create guides to “move” nearby hairs during the simulation. How would that be set up?

---

### Post #9 — Abraham_S — 2026-06-25T09:54:29.009Z

From a usability and UX standpoint, very much agree with this​
.
You’ve been doing a
fantastic
job so far in this Nodes & Physics module, especially for your team size​
,  and appreciate it’s still early days and lots of features to implement and improve on, but the end goal, imo, should indeed be to make things as artist-friendly, modifier-facing and familiar with the existing system as possible, once things are in a more robust state ofc.
Geo-nodes are very powerful, but some of us would love to be able to do these powerful things without diving into them, unless
really
necessary.

---

### Post #10 — costavojik — 2026-06-26T15:30:54.904Z

Hey!
I’m speaking as someone who’s familiar with GN and feels very comfortable using it.
First of all, the
“Cloth Dynamics”
node group itself could be simplified. I understand that it’s designed with users in mind who want to use it as a modifier, but honestly, nodes are always the better way. The Blender community should be pushed more toward nodes, not the other way around.
For example,
“Invert Pin Group”
and
“Gravity”
could be removed. For inverting the pin group, I’ll just use
Boolean Not
or
Map Range
to tweak the attribute. As for gravity, I’m already going to be using force effectors, so I might as well add a Gravity force if I need one.
A take that would be even more controversial is removing
Tearing
from the node tree itself. It should be an effector instead, because that would let us implement many more cloth behaviors, such as pressure, internal struts (to make the cloth more rigid), shrinking, sewing, and much more.
The
Structure
section could be renamed to
Parameters
, and I would expect
Stretchiness
and
Bendiness
to be included there as well. (Not sure about that because that’s an effector/constraint itself?)
Damping
could be part of the solver? Maybe
Another thing I dislike aboutusing node groups across different production files, is the huge number of packed node groups (currently
42!
). Whenever possible I think they should be exposed as frames, or if it’s possible there should be a way to have node groups that are only used once and not become a datablock, just like a folder or a frame with extra settings.
I understand that using node groups keeps things tidier and better organized, but most of them have only
one user
anyway.
image
712×1570 169 KB
For example what the heck
Why should it be a nodegroup?
image
896×427 60.3 KB

---

### Post #11 — modmoderVAAAA — 2026-06-26T20:38:39.286Z

costavojik:
Why should it be a nodegroup?
image
896×427 60.3 KB
This is legit way to reuse menu deffinition…

---

### Post #12 — Baardaap — 2026-06-26T21:56:16.931Z

To add to what Iliya said:
You can’t re-use a menu twice inside the same nodegroup, so if it’s needed twice you need to stick it inside a small sub-group and re-use
that
. I guess it has something to do with the ‘hide inactive inputs’ logic which is scoped to groups, not sure though.

---

### Post #13 — Baardaap — 2026-06-26T21:58:21.330Z

Volkashin3D:
Something hit me while writing this, having to only release node group presets during alpha versions doesn’t really make sense to me. It would be nice if they were exempt from this rule.
I wouldn’t be against tweaking stuff during beta, but please for the love of god keep different versions of bundled assets/nodetrees linked to releases or triaging/bisecting/bughuntig is going to be a nightmare.

---

### Post #14 — MartinZ — 2026-06-26T22:24:15.545Z

One feature absolutely essential for me for cloth simulation would be the ability to easily change the mesh density in the middle of the simulation. This lets me run rough simulation up to some point quickly and then increase the detail from that point. I played around with the cloth simulation, but I am not sure how one would do that - if I add subdivisions to cloth geometry during the simulation it just breaks the form. Is this something that may be done some way or maybe is planned to be possible?

---

### Post #15 — Dabreiss — 2026-06-28T08:06:22.421Z

Hello ! I am absolutely loving to where this is heading. Thank you all so much for all your hard work. My feedback is based on a simple “create fur” operator which sets up all the modifiers.
Hair Surface Attachment:
It does exactly what it says and I am super glad that the Growth geometry and it’s UVs now come as a bundle and don’t need to be plugged into most of the nodes. Maybe the “Hair Dynamics” naming of the modifier might be a bit confusing. While it also can serve as the dynamic solver the default animation setting is purely for the attachment (correct me if I’m wrong).
Having the Hair Dynamics pinned to the end of the modifiers stack is practical when using it for attachment but not so much when using it for simulation. In an ideal scenario, we should be able to drag to modifier to any level, and have the hairs simulated at this stage. Which is working as such, however the interpolate hair curves node and the clump curves node then need proper hacking to not fall apart. In my case I had to generate the curve points on the rest position and bring them back to the deformed position in order to avoid flicker due to deforming mesh but also follow the surface.
Same with the search radius for the clumping, which should do the search on the rest position instead of the deformed geometry.
So really we need a more robust growth mechanism, where the amount of hair curves and their IDs remain the same and still follow the surface/can be interpolated with the simulated guide curves.
This is probably more a re-desing of the hair node groups than the simulation itself.
Hair Animation:
I probably don’t fully understand what this group does, but simply attaching the curves to the surface ? A potential feature could be a sort of wrap functionality. Like on long hair on a bendy surface, the hairs start sicking out/going into the surface. I made a custom Surface Deform node group a while ago, which really fixes this issue.
hairs combed along the cylinder
image
1585×1232 100 KB
When bending the hairs fully rotate with the underlaying surface, making them stick out on outer bend and  or penetrate on inner bend.
image
1589×1265 115 KB
Custom deformer wraps the curves to the geometry and bends along with it. No sticking out or penetrating
image
1580×1256 109 KB
One more thing I also noticed, is that the simulation result highly depends on the point distribution along the curve. However when combing, growing/shrinking etc. the spacing can become uneven quite easily and gives odd simulation output. Maybe the “redistribute curve points” can become an operator from within the curves sculpt mode “curves” menu.
A big thank you again, not only for what you are doing, but also for asking for feedback and get the community involved.

---

### Post #16 — redmser — 2026-06-28T11:09:44.160Z

Did more experiments with cloth dynamics… I am very impressed.
jacqueslucke:
Does setting up custom forces work well? What are limitations of the current approach?
I don’t see any documentation on the order in which multiple effectors within the same phase are evaluated. For example, if I wanted to create a custom effector that displaces geometry, it could write a named attribute as a result of that displacement, that could then be used as a mask for a later effector. Current workaround is to compute the mask in pre-solve, then have the custom effector in post-solve, but ideally I’d have them within the same phase but with different priority order.
To me, a list of bundles would make a lot more sense than a bundle of bundles, since you could search elements and insert at a particular position in the list to determine order of execution.
jacqueslucke:
Hackability: How difficult is it to add some basic custom behavior to the high level dynamics groups? Please share some of the stuff you did or tried to do.
Similar to above, I wanted to affect the cloth sim “pin group” by a named attribute that is computed by an effector (to avoid jittering as the cloth sim repeatedly tries going against my custom deformation). To my surprise,
it works perfectly
- all without having to dig into the cloth dynamics node internals. I did not even need to set “Extra Sim Attributes” (likely due to the order of execution magically working out) :o

---

### Post #17 — Melvi — 2026-06-29T12:50:18.686Z

jacqueslucke:
Hair Animation: Hair simulation can be expensive and is often not necessary for simple cases. What features should be added to the “Animated” mode to fake hair dynamics?
Hi, Pls add keyframing to this new version of geometry nodes hair
. This enables the hair to be posed like 2d animation with interpolation between keyframes.
To make posing easier and faster, it would be awesome if we get selection sets for the hair strands so u can easily select the groups of hair we want to pose and pose them without affecting the other strands.
Also selection sets should be points based. Say u have a clump of hair tucked behind the ear, u can have two selection sets of those hair strands-
One for the points from the root to the areas around the ear and another set for the ear area to the tips. So if u select Selection set 2, u can now pose those lower hair strands part without affecting the upper part.
I have been hoping we get this keyframing for hair like AnimAll addon. AnimAll addon allows u to create multiple keyframes in one shapekey so I have been using AnimaAll shapekeys as a form of Animation layers in Blender.
Would also recommend adding tip bendiness feature to the hair dynamics settings if that is possible.
Awesome work so far, guys. Thanks a ton for all the work u guys have done so far.

---

### Post #18 — Jan_van_den_Hemel — 2026-06-30T08:38:01.815Z

Hi, I’m excited to test the new Cloth Dynamics. So far I can’t seem to make it work with Hooks, at least not the way it works with the legacy Cloth system. Normally you can attach Hooks to Vertices and then move the hooks during simulation to stretch the cloth. With the new Cloth Dynamics, it just pulls on the Vertex it’s attached to, but doesn’t really interact with the cloth sim. I’d like to share a test file, but apparently I’m not allowed to upload stuff (yet).
Not sure what I’m doing wrong. I tried playing with the Stretchiness and Bendiness which seems to help a little bit, at the cost of it having too much Stretchiness and Bendiness…
Any hints would be appreciated.

---

### Post #19 — Hadriscus — 2026-06-30T19:38:39.493Z

Are you using the pinning socket? see release notes
developer.blender.org
Physics - Blender Developer Documentation

---

### Post #20 — Bobo_The_Imp — 2026-06-30T20:14:59.381Z

image
1048×869 109 KB
You can use a typed bundle set to pin position to set this up. It’s sort of the same thing as a hook but just in the geonodes context. (Edit you don’t even need the pin group at the top)

---

### Post #21 — Arjjacks — 2026-07-01T03:20:35.065Z

New physics solvers in geometry nodes is such an amazing leap forward for Blender, massive congrats to the team for such an impressive milestone. I’d say one of the only other critical aspects of the legacy cloth system missing from the new system, besides self-collision, is sewing. The ability to have cloth objects physically ‘shrinkwrap’ around a collider via what amounts to drawstrings is an incredibly powerful feature of the current cloth system in Blender. I’m pretty sure even Maya’s nCloth doesn’t have anything like that.

---

### Post #22 — Jan_van_den_Hemel — 2026-07-01T11:50:34.353Z

Thanks for your reply. I’ve tried to recreate your GN setup, but my Combine Bundle node looks significantly different. It doesn’t have all those specific input sockets, for one. Do I need to enable something in Preferences? I don’t have any “Experimental” features that I can enable in the recent 5.2 Beta, so I’m not really sure what to look for other than that. Thanks a lot for your help (and apologies, for not knowing Geometry Nodes and potentially asking very obvious stuff).

---

### Post #23 — Jan_van_den_Hemel — 2026-07-01T11:55:13.298Z

Ah, I got it to work with the ‘simplified’ Combine Bundle node, but the same problem as when I do it the ‘old-fashioned’ way: the Empties/Hooks just pull one Vertex, rather than pull on the Cloth in a more expected method. I’ve attached my node setup, maybe you can spot the mistake…
Screenshot (281)
1328×1359 176 KB

---

### Post #24 — JulianPerez — 2026-07-01T13:24:37.982Z

This looks way too convoluted just to get the old “hook” functionality, isn’t there a simpler way to get it? Or maybe this could be turned into another nodegroup that comes pre-made by default where you just put the empties that will be used as hooks into a collection and use that one as an effector in the modifier UI?
I know the intention is to slowly move into node based workflows but there are still many non-technical users that will depend on the modifier stack for stuff like this, and having to jump into the node editor and try to come up with node setups like this just to have the hook functionality back seems like a regression, not just a different way to do the same…

---

### Post #25 — JulianPerez — 2026-07-01T13:47:17.919Z

I was just trying this and you have to use the node called Typed Bundle, and if you click on the text box you’ll get some options to choose from, just select the first one.
image
420×410 18.6 KB
Small UI complaint BTW, I’ve found that having to click on a text box to get a list of options is also very unintuitive. If there are already options to choose from there should be a clear indicator of a dropdown or a menu.

---

### Post #26 — Bobo_The_Imp — 2026-07-01T18:20:59.927Z

JulianPerez:
This looks way too convoluted just to get the old “hook” functionality, isn’t there a simpler way to get it?
1
583×546 49.4 KB
Technically the geonodes setup only requires two inputs, as does a hook modifier. I understand it can seem pretty intimidating but really it’s just about the same, just different know how. I do agree the typed bundle idea is just a bit tucked away right now, and perhaps feels like a dropdown would be better, but right now that’s just how it is. It’s important to remember this is all experimental currently.
It’s also important to note that the pin position constraint isn’t strictly a “hook”, it’s just an equivalent of sorts for the question that was asked. The typed bundles let you bring up a variety of constraints, allowing the user to get specific with the kind of behavior they want.
Physics is complicated stuff, and I’d say so far the entry level is pretty convenient really, they are doing a killer job.

---

### Post #27 — Bobo_The_Imp — 2026-07-02T16:46:49.397Z

jacqueslucke:
How difficult is it to add some basic custom behavior to the high level dynamics groups? Please share some of the stuff you did or tried to do.
I’m not sure if custom blending between rests states is possible right now. I see there is a nodegroup for setting up structural rest data, but without unpacking the cloth dynamics node it’s off limits and I’m not sure if blending is possible within it anyways.
hehe
1920×540 96.2 KB
Making a sheet bend like this is maybe possible with forces and constraints, but setting starting rest data and goal rest data and then blending between the two during the simulation and letting a high number of constraint steps carry you can be really ideal in certain situations, especially if it’s not as simple as this example.
That being said I tried following some tutorials from our neighbors online and setting up custom behavior like forces and constraints seems to be working well!
Glue
1734×883 117 KB
I tried making some super simple glue constraints to make this effect from a tutorial I saw and I literally just tried the first thing that came to mind and it worked without a hitch. It worked exactly how I thought it would in geonodes.

---

### Post #29 — Jan_van_den_Hemel — 2026-07-08T08:04:46.058Z

The reason it wasn’t working for me was because I still had those Hook modifiers. It actually works quite well with this node tree. However, when it tears (as it’s ripped apart by hooks) it’s quite violent and there’s ‘confetti’ of triangles. I tried with just a single line of Vertices as the custom tearing group (in a Vertex Group) as well as a custom Edge attribute, but both create these loose triangles.
Does anyone know how to make it look better?
Cloth Tearing Devtalk
1776×1914 338 KB

---

### Post #30 — Kenzie — 2026-07-08T12:36:33.450Z

In my tests I just deleted faces whose points had less than N neighbors (exluding the edges of the cloth) as a post processing step to get rid of shards.

---

### Post #31 — jonlampel — 2026-07-08T17:14:13.360Z

I like using a smooth modifier after to both make the tear less obviously geometric and shrink the single faces. They’ll still exist but kinda just become dust. The other alternative to remove them completely is using a small voronoi scale, so that not every single edge is eligible to tear but every few edges, and you can scale to your preference.

---

### Post #32 — Bobo_The_Imp — 2026-07-08T17:44:17.934Z

Generally speaking tearing behavior should be very specifically defined by the user. It’s not really something you get “totally for free”. Even in Houdini you don’t get a toggle like here in blender for “just tear please”. You have to set up what tears, the threshold and other kinds of more complex behavior if that’s what you want. This often means manual work before hitting the simulation nodes, and some inside the simulation nodes. On the blender side of things it’s similar in that it’s good to be really super duper specific. As Jonathan pointed out setting it to voronoi is a good step, but custom is where it can really shine. The trick is using a capture attribute node to get the pre-simulation attributes you want, so they don’t dynamically change (store named attribute works too). Once you have that you can add things to dynamically change things during simulation. Like having the edge group grow, changing the threshold etc, whatever you want.
image
1541×846 112 KB

---

### Post #33 — LukasTonne — 2026-07-09T08:27:09.098Z

The tear feature is not very sophisticated atm. It was added mostly as a test for changing topology during the simulation.
I haven’t done a whole lot of research yet, but i think the problem with the current approach is that we instantaneously tear the cloth in many places all at once, whereas in reality tearing a single thread would release the tension so quickly that the surrounding cloth is under much less stress and consequently doesn’t tear into lots of tiny pieces. And then you get the effect of fracture lines, where the highest stress concentration travels through the surface and forms a single line of tearing/fracturing.
Simulating that requires a bit more integration with the solver though. Slow tearing could probably be done by splitting only one edge in each sub-step and then re-evaluate stresses in the next step. For faster tear propagation it may be necessary to have a built-in feature, which can simulate progression of the tear over a sub-step interval.
For ultimate artistic control i think it’s reasonable to try and mark a single edge line along which tearing is allowed to occur, using the “Custom” tearing mode.

---

### Post #34 — EvertonSchneider — 2026-07-10T04:07:03.929Z

While testing the cloth node, I found a way of masking these ripped areas using a “is edge manifold” node as a mask of a custom smooth mesh approach that I learned from BlenderGrid. I came up with this solution, trying to get rid of the topology pattern of the teared areas.
https://www.instagram.com/p/DaV-vGHgfD0/
image
1920×1135 294 KB

---

### Post #35 — Anthony_Gibbs — 2026-07-10T05:58:26.169Z

Out of interest, has anyone figured out cloth self-collisions or does that really have to be implemented directly in the Blender code before the new cloth simulation is usable?

---

### Post #36 — costavojik — 2026-07-11T11:48:31.967Z

Is it planned to implement the old constraints tension, compression, shear & bending? Currently it’s stiffness/bending but it feels that tension/compression could give different results and fine tune the material parameters

---

### Post #37 — Anthony_Gibbs — 2026-07-15T07:49:10.905Z

So I just installed the 5.2 release and the first thing I tried was the cloth simulation, with just a standard ‘drop a plane on a cube’.
Mind you, what I did do, that most don’t, is scale the cube to basic real world human size and a matching plane. So it’s more like a poncho dropping on a person, then a circus tent falling on a 2m concrete block.
I was able to get pretty good results fairly quickly, helped by the fact it runs the simulation in real-time, which is very nice. The default values are a good starting point and overall it seems rather stable.
All very good signs, wanting me to play around with it a lot more.
However, I won’t, since there’s no point as it also looks very wrong, due to, you guess it, no self-collisions. There’s no point in testing something, when its actually impossible to get it to simulate correctly.
With focus now shifted to fluid simulations, I guess it won’t be till next year sometime before cloth simulations can actually be tested.

---

### Post #38 — TheLittleMouse — 2026-07-15T16:22:00.369Z

Oh yeah and, just like the hair rest shape feature that was being worked on, I think it is needed for cloth simulation too. I think often times, we have a hair style or cloth shape that we want to be the rest shape, and we want it to move with the character, but it should return to the original position. Basically how hair and clothes are in video games.
Edit: After more testing, I realised this behaviour already somewhat exists in the current XPBD cloth simulation, the ability to return to the original shape. However, it does not always return to the original shape, and there is no way to control how fast it returns to the original shape.

---

### Post #39 — Kenzie — 2026-07-17T12:57:42.362Z

From the fluid sim planning paper there is a mention about how particle self collisions should be implemented through features needed for both FLIP (fluids) and MPM (granular solids). I believe the work done on Point Grids will be needed to efficiency query points for self collision constraints, right now since points are unordered and cant be effectively queried any attempt at self collision would be unacceptably expensive. I would say the devs haven’t prematurely abandoned cloth they just are tackling some other stepping stones first.

---

### Post #40 — Anthony_Gibbs — 2026-07-17T16:03:40.731Z

Kenzie:
I would say the devs haven’t prematurely abandoned cloth they just are tackling some other stepping stones first.
Any actual dev meeting notes, etc that state all of that and/or give a possible time frame as to when ‘particle self collisions’ would be worked into cloth self collisions?
As of right now, the roadmap just marks it all as done and the focus going forward is fluids.

---

### Post #41 — filedescriptor — 2026-07-17T16:07:52.969Z

See
XPBD Solver Extensions - Blender Notes
for example. These were linked from the last meeting notes.
The roadmap lists development targets, and at some point they are done, yes. But that doesn’t necessarily mean that the feature is completed. The solver node groups are still marked as experimental for this reason.

---

### Post #42 — Anthony_Gibbs — 2026-07-18T08:57:54.618Z

filedescriptor:
See
XPBD Solver Extensions - Blender Notes
for example. These were linked from the last meeting notes.
Yes, that points out what is still required, but as I asked, nothing said about when/if any of it will be done.
Then there’s the other bit I’m not sure about or maybe just don’t understand. A few people talk about how the new focus on fluids is going to help, but then talk about the FLIP and MPM solvers for fluid but they aren’t the XPBD solver.
But if all these are so much the same for collisions, then why not work on those Solver Extensions first, which can then be directly and fully tested on Cloth (and even hair, not that it matters so much for that), since the work on the XPBD solver has already been done.
Rather then starting up a whole new project, having to make the solvers again before even thinking about self collisions and seeing how well it works and then at some point down the road adding it to the XPBD solver.
I would have also thought that continuing to focusing on hair and cloth, would mean that it could be moved out of experimental sooner, which in turn means it could replace the current hair and cloth simulation sooner. Instead, not only will both need to be in Blender 6.0, but fair chance Blender 7.0 will still have legacy hair/cloth.

---

### Post #43 — Kenzie — 2026-07-18T16:28:17.317Z

I am understanding that the XPBD will be used as the foundational kernel for cloth, hair, fluids, softbody, and granular solids (with rigid bodies possibly being their own seperate thing). FLIP and MPM would be advanced subcategories of XPBD. The improvements being talked about right now for FLIP right now is arround letting points from XPBD to interact with VDB grids and utilizing OpenVDB to implement fluid incompressibility forces, that seems to be the foundation of FLIP. MPM seems to be direct point to point interaction using the point grid acceleration structures provided through OpenVDB to allow for self collision. This self collision work will end up ported back into cloth to address self collision. At the end of the day all these simulation types will be based on the same building blocks of Position Based Dynamics with eXtensions (XPBD). Its all connected now.
This is my understanding from the conversation atleast. (Correct me if I am wrong)

---

### Post #44 — TheLittleMouse — 2026-07-20T02:33:37.143Z

I just discovered that, for example, if a hair object has simulation turned on, and then you pose the head or whatever the hair object is on, it becomes very slow even on the same frame. I think this is not the correct behaviour? While I am still on the same frame, there shouldn’t be any simulation running on the hair, and so it shouldn’t affect posing. Of course, I can just switch back to the animation mode, finishing posing, and then switch back to the simulation mode. But, I think it just shouldn’t affect the performance while I am posing on the same frame.
I also have a slightly unrelated question. If I am not mistaken, Blender is planning on using Jolt Physics for rigidbody. A week ago, Jolt Physics released a new version that includes a strand-based hair simulation running on GPU. Have you developers considered replacing this experimental hair dynamics with that?

---

### Post #45 — LukasTonne — 2026-07-20T09:12:12.051Z

I am understanding that the XPBD will be used as the foundational kernel for cloth, hair, fluids, softbody, and granular solids (with rigid bodies possibly being their own seperate thing). FLIP and MPM would be advanced subcategories of XPBD.
Not quite. The
XPBD Simulation
asset is just called that because it currently only uses the
XPBD Solver
node. It’s really a higher-level framework for constructing simulations with nodes. Future versions/variations can include different solver types, which can run next to each other in the same simulation loop and have some degree of cross-communication.
For example: This is what the simulation zone currently looks like in my fluid testing. The fluid solver and XPBD run next to each other, with potentially some feedback through obstacles/buoyancy.
02_simulation_loop
1920×330 53.3 KB
XPBD is just one solver method for softbody simulation, and not necessarily the “best”. For instance: Augmented Vertex Block Descent (AVBD, not to be confused with VDB) seems like an interesting candidate for the same kind of geometry (hair, cloth) with better performance. Fluids and rigid bodies have their own types of solvers that don’t fall under the “XPBD” umbrella. Grid-based self-collision for hair would need close integration with the hair solver, but the details are not fixed yet.

---

### Post #46 — LukasTonne — 2026-07-20T09:18:15.214Z

I just discovered that, for example, if a hair object has simulation turned on, and then you pose the head or whatever the hair object is on, it becomes very slow even on the same frame.
The way simulation zones work currently means that the last frame of the simulation will be redone when such user-edits are made. Changing the conditions for the simulation (animation, colliders, forces, etc.) is “correctly” updating the dependencies. In this technical sense it’s not a bug.
I agree this is undesirable. Ideally the simulation should be paused in some way during edits. I don’t know a nice way to do this without manually disabling the simulation currently.

---

### Post #47 — TheLittleMouse — 2026-07-20T11:15:46.088Z

I see. That’s fine. It may be a good thing for posing with physics, if that ever becomes a reality.

---

### Post #48 — TheLittleMouse — 2026-07-20T19:40:41.476Z

One common trick to get better performance for cloth simulation in Blender is to use a proxy mesh for simulation, and then transferring the simulation to the original mesh through the Surface Deform modifier. I wonder if it will ever be possible to completely remove the influence of pinned vertices on the performance of the simulation, so that we don’t have to use this trick? Right now, having many vertices on a mesh, even if they are pinned, make the simulation slow.

---

### Post #49 — Amethyspian — 2026-07-21T17:10:19.975Z

I hope this is the right place to suggest this, but I think a better solution for multiple “Pin Groups” would prove useful.
In this example, I am using a modified version of the Cloth Dynamics Node. As well as that, I created reusable Pin Group Nodes to Bundle together into a new “Constraints” field. This was possible by storing the pre-sim attribute the Pin Groups reference, and adding it into the new Node Group.
A personal use case is having the Pin Groups share the same Vertex Group as a Mesh’s Bone Weights. This allows for a more art-directed approach to simulations.
Of course, this means the “Pin Group” field can be deprecated, completely, leaving the “Constraints” field for similar use cases.
Illustration3
1920×1007 294 KB
1 - Edited reference to the pre-sim position.
2 - Internals of the custom “Dynamics Pin Group” Node.
3 - Edited/new “Constraints” field.

---

### Post #50 — greyArea — 2026-07-30T08:38:19.028Z

Pinning behavior when using cloth as rope is a little bit strange. If there is movement of pinned vertex, it will stretch the points. If the pinned vertex is static, everything behaves as expected.
video:
https://imgur.com/a/miXPWyn

---

### Post #51 — JulianPerez — 2026-07-31T19:10:03.449Z

I’ve noticed the same behaviour too, when vertices that are pinned have movement (from an armature modifier or a shapekey for example), sometimes they can cause weird stretching and/or shrinking

---

### Post #52 — TheLittleMouse — 2026-08-02T21:10:37.202Z

I have discovered yet another thing. It may just be what you described but, I think it is another problem, but similar. It is just using the Animation mode of the Hair Dynamics modifier. So it shouldn’t have anything to do with simulation. It uses another path in the Geometry Nodes. It still has a very heavy performance hit. Is that normal?

---

### Post #53 — TheLittleMouse — 2026-08-03T01:57:49.724Z

I noticed that there isn’t a minimum collision distance setting for Hair Dynamics. I looked into the Geometry Nodes graph, it is just using the Collider node. So the option is there, but it is not exposed. I think it should be exposed, because it helps avoid clipping for the hair.
And while I know curve is quite different from mesh, and so we can’t just pin vertices in curve like we do in mesh, it would be really useful if we can pin hair curve points so that they don’t move as much or at all by the hair simulation.
And a bit unrelated, the Interpolate Hair Curve modifier. It requires separating the underlying mesh to part the hair. That is very inconvenient. Is there no better way to part the hair? Can some developers explain how to use attribute for this parameter, as you can switch this parameter to use an attribute?

---

### Post #54 — LukasTonne — 2026-08-03T05:43:47.065Z

Can’t say without more detail. If you think it’s a bug please make a bug report and add reproducable steps and preferably a test file.

---

### Post #55 — TheLittleMouse — 2026-08-03T10:46:32.061Z

Blender Projects
Geometry Nodes: Animation mode on Hair Dynamics modifier lag
### System Information

Operating system: Windows-10-10.0.19045-SP0 64 Bits
Graphics card: NVIDIA GeForce RTX 2070 NVIDIA Corporation NVIDIA 591.74 Vulkan Backend

### Blender Version

Broken version: 5.2.0 LTS, branch: blender-v5.2-release, commit...
I have created the bug report. If it isn’t a bug, then never mind.

---

### Post #56 — miqueloc — 2026-08-03T16:41:16.900Z

Hello, I am testing the new simulation related nodes focusing on form finding architectural design workflows and I have a suggestion and a potential bug but I am not entirely sure.
I think the cloth dynamics node should expose the custom length option for a quick way to represent cloth under tensile stress. On that note, I was testing how to represent a simple piece of fabric under tensile strength
and found out that the result is not precise and has a pronounced bias.
image
1919×1047 389 KB
What I did is to increase internal tension making the edge length gradually decrease and playing with different “softness” values for boundary and internal edges. The result should yield a symmetric mesh,
but the parabola it forms is clearly biased towards one side, should I report it as a bug?
Resolved: I needed more sub-steps (for some reason I thought I checked that)
Thank you!

---

### Post #57 — I_E — 2026-08-20T04:48:07.252Z

I just want to offer this in case it helps anyone, because I’ve been struggling for 3 days straight. Of course, I don’t pretend to be someone incredibly knowledgeable or a developer–this is, in fact, my first time interacting and I’m not active as a community member, but…
The only real issue I continually have with the incredible Hair Dynamics system is not so much with the Dynamics specifically, but the fact that Surface Attachment seems to have considerably dropped its functionality since the update to 5.2 LTS–particularly for armature uses. Hair floats constantly above whatever mesh I choose, as soon as I put surface attachment to it, be that by parenting or a modifier. I’ve tried Attach Hair Curves to Surface, I’ve tried Hair Dynamics…
Hair Dynamics doesn’t seem to include full documentation on how its surface attachment works. It was mostly through trial and error that I figured out it’s supposed to be an all-in-one type of package. In any case, while this would be fine, the problem itself lies in 2 things: No clear order in which to stack the modifiers, and secondly, surface deform appears to fail drastically with the existence of Interpolation–some hairs seemingly always will be floating outside the surface. I promise I’ve checked and double-checked my UVs, and no such overlap appears with Blender’s native Select + Overlap, even if the UVs themselves require improvement. All the normals are facing correctly, no merging was needed. This did NOT happen before the new system was implemented, and it also happens with other surface methods, such as: Deform Curves on Surface, Surface Deform. Each situation consists of Interpolation being placed above a surface deformation method.
Hair Dynamics being pinned to the bottom by default definitely makes this more confusing. While it does not happen every time, there seems to be no solution for it, and can happen on a 100% new test cube. I would show the cube in question, but Blender crashed as I tried to switch to Edit Mode.
As I said, I’m not an active community member, so I am afraid you can’t expect that, and I’ll continue to work on this project; and if my comment is irrelevant, please dismiss it as amateur rambling, but it was something I noticed and have struggled with, and I genuinely think it may be a functionality problem and not user error.
image
1139×810 181 KB

---

### Post #58 — Realish — 2026-08-21T09:08:05.161Z

I’ve been testing the new cloth on a fairly specific case: a stack of paper sheets dropping and settling on each other. It turned out to be a good stress test because it needs several missing pieces at once, with collision between simulated sheets, bending that can be stiff without coupling to stretch, and decent convergence once things are stacked.
Single sheet behavior is good and the realtime feedback is a huge improvement over the old cloth. But with no collision between simulated geometry, my use case is still open, and to make a sheet read as paper rather than fabric I had to push the cross edge bending close to instability.
Since warm starting is the first item on the solver extensions note and
PR 159910
has been stalled since June, I started there. I managed to reproduce it and track the main cause to the pin constraint (its scalar multiplier misbehaves at rest distance zero). I posted the details and a patch on the PR.
One question though. For cloth self collision, would a proximity constraint implementation be acceptable as a contribution now? i.e. vertex-triangle and edge-edge, regenerated per substep, reusing the existing contact/friction machinery, with a per point thickness offset so contact resolves on d minus thickness rather than d. That’s the C-IPC formulation, and that part looks separable from the barrier solver, so it should port to xpbd even though the note flags IPC as maybe incompatible. Or is this intentionally parked until the point grid work lands? I’d assume the same constraint covers collisions across multiple simulated geometries, since the note asks for that and the pair source is the same either way.
I’m going to have a go at isometric bending next since it’s self-contained and it’s what my case needs. Shout if that conflicts with something planned.

---

### Post #59 — Realish — 2026-08-22T01:11:14.850Z

Following up on my last post with some juice. Isometric bending is done and actually grew into two separate PRs. I have my intended shot of paper falling nearly complete with a hacky solution, so trying to make it official with PRs over the next few bit. Overall, I’m liking the new physics and finding it very hackable.
The first one,
PR #162985
adds the constraint itself. Because it measures pure bending, you can crank up the stiffness without it fighting the stretch constraints. Unlike distance springs, it also doesn’t lose stiffness at higher mesh resolutions. I originally built it just for flat shapes, but realized it was actively flattening out curved models, so it now supports curved stencils as well. There’s a demo file on the PR you can check out to see if you want. UI changes are still pending (like adding a bending model switch or replacing the Bendiness path) and I’d like to hear how you all want that handled.
The second one,
PR #162986
fixes hard pins. While stress-testing those stiff settings, I kept having pinned points break loose. This actually has nothing to do with the new constraint, you can reproduce it on main right now. With a stiff enough cloth strip, the constraints eventually overpower the pins, and the mesh just free-falls. So now hard pins hold perfectly against heavy loads now, while soft pins are untouched. Stiff cross-edge bending will still generate internal energy, your pins just won’t rip off anymore. Combined with warm starting, this covers almost everything I need for my paper stack sim. The only missing piece now is self-collision, which I’m still looking into properly formalizing.

---

### Post #60 — Sven_Reinold — 2026-09-03T13:19:28.862Z

As cloth tearing has been implemented i need some things for my animations, which currently can’t be done without faking it in post.
I use tearing for transformations and with the self collision on the cloth part i also need that multiple fabric layers recognize each other, so that i can have my growing character wearing a shirt and a coat over that and both tear while not clipping WHILE fur is growing undereneath and not clipping through the fabric.
Also having objects stick to the fabric like buttons is something i can’t seem to get right. Especially when the fabric is twisting.
I tested the cloth tearing and it looks amazing, but using two cloth sims failed to get the collision right.

---

### Post #61 — KickAir_8p — 2026-09-23T19:16:49.788Z

I want a new fabric-draped-over-a-sphere material tester, so I thought I’d try  Cloth Dynamics (Experimental).  In 5.2.1 I made a plane with the topology and UV mapping I wanted, imported a collider (the new Quadsphere primitive from 5.3.0 alpha), set everything up (including a Subdivision modifier on the drape object above the CDE), animated it (several times to get the settings I was happiest with), everything went great.
Then I picked the frame of the animation that I wanted for my test object, and in Properties > Modifiers > Cloth Dynamics (Experimental) applied the modifier.  The drape froze perfectly, but the UV mapping that I need shredded.
screenshot.2026-09-23 14.52g1352x772a
1352×772 138 KB
screenshot.2026-09-23 14.52g1352x772b
1352×772 115 KB
Turns out that applying the subdivision before animating the Cloth Dynamics (Experimental) and applying the frame of the animation I wanted fixed the UV shredding problem (ID10T error
), then I Decimate > Un-Subdivided it back to the original quad count.  So I’ve got my new tester, and thanks muchly to everybody who worked on Cloth Dynamics (Experimental)!
20260922_FabricDrape_004_rendertest_001
1024×1024 74.2 KB
A simple thing, but mine own.

---