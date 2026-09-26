---
titulo: Procedural Hair Nodes: Nodegroup Assets for Blender 3.5
autor: SimonThommes
url: https://devtalk.blender.org/t/procedural-hair-nodes-nodegroup-assets-for-blender-3-5/27601
data: 2023-02-09
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — SimonThommes — 2023-02-09T11:38:32.139Z

EDIT:
Now that Blender 3.5 has been released I want to use this thread as an opportunity for users to post their feedback on the workflow and issues/potential improvements they run into.
Keep in mind
: Bugs should still just be reported and tracked on
projects.blender.org
Original post:
Blender 3.5 will include a set of node-group assets to empower the workflow of procedural hair using Geometry Nodes and the new hair grooming tools in Blender. For the past weeks I have been working on this package alongside the geonodes team. It’s still heavily WIP but the main building blocks and logic are there, so at this point it would be useful to get more feedback. But be aware that lots of the aspects are still subject to change.
The long-term target is to replace the old hair system with something more powerful and flexible. However, for 3.5 this will not yet be the case due to other missing aspects, like simulation. So the short-term goal of this bundle is to give a solid foundation of procedural hair tools for an out-of-the-box experience in Blender.
Deadline for user-facing features (anything except performance tweaks) is the transition to bcon3 on February 15th.
The idea is also with these node packs that they can change a lot between Blender releases, as they are implemented as node-groups and will not break compatibility for files that they are used in.
Thanks to
@DanielBystedt
for kickstarting this bundle with an initial pass of nodes!
Small showcase:
The current WIP version of the file can be downloaded here, it also contains a few testing setups with examples of how the node-groups can be used together in the modifier stack.:
https://svn.blender.org/svnroot/bf-blender/trunk/lib/assets/working/geometry_nodes/procedural_hair_node_assets.blend
Some notes on the current state:
Things that are still changing with iterations of feedback and discussion include:
Naming of nodes
Inclusion of certain nodes
Naming of sockets
Scaling/Interpolation/Unit of inputs
Defaults of in-/outputs
Available node outputs
Underlying functionality (Minor changes)
Missing to a large part:
Node descriptions
Socket descriptions
Asset thumbnails
Node documentation
Asset tags
Catalog organisation
Performance pass to optimize for realtime workflow
node-tree cleanup and structuring for readability
Additional Notes:
The
Performance Mode
toggles are temporary. It should be benchmarked how big the performance and the quality impact is for the individual nodegroups. Ideally the Toggle should be removed in favor of using it at all times.
Until the attribute propagation from the spline to the point domain is fixed there are some workarounds in the node-trees with some minor performance impact.
The symmetric hair shape as suggested by
@DanielBystedt
is currently only possible to achieve with Cycles and not with Eevee/Workbench due to the missing ability of rendering curves with an arbitrary radius attribute. Therefore I’m sticking with the shape that is supported by both Eevee and Cycles for now to avoid confusion.
The high-level nodes in the pack are designed to be useable together in the modifier stack, but also in the node-tree directly. Because of this, some of the inputs may be rendered redundant, depending on other inputs that are being used. This will hopefully be possible to avoid in the future, when users can define a more dynamic interface with nodegroups. But as I am locked to the same feature set as any other user with creating these node-groups that I settled with this as an acceptable trade-off.

---

### Post #2 — AlexisAndersson — 2023-02-09T13:58:17.714Z

Beautiful work from everyone! Just curious if there is any talks on being able to promote up ramps/curves to control shape of a clump for example?

---

### Post #3 — SimonThommes — 2023-02-09T16:29:15.580Z

The shape input gives general control over this. However, when the shape is set to 0, that means that this influence is constant along the curve and then the factor input can be used to achieve exactly that. As we don’t have the ability (yet) to expose a curve in the node directly this will work only in the node version of this function. But there will be an operator that allows you to promote a modifier to a node-group while keeping the inputs intact. That will allow you to use a node system to drive all of the inputs.
Blender Projects
Operator to create wrapper node tree of Geometry Nodes modifier
High level geometry nodes setups that are mainly meant for use in the modifier stack reach their limits quickly whenever the user wants to use some more flexible input than just a single value, or a paintable mask. Currently, moving to a node-tree...

---

### Post #4 — dan2 — 2023-02-09T18:14:59.808Z

Firstly, thank you for all your hard work on these. I’m sure a lot of people are looking forward to the new groom system, and it’s looking great.
I got a couple UX related questions -
Are there plans regarding the modifier stack? With many nodes there can be a lot of clutter, constantly having to expand, collapse and scroll in that list may be time consuming.
If I would want to work with maps (use a noise texture as a mask for a clump for example) - is the expectation to go into the geo node editor and connect the node manually?
I’ve been only giving it a quick try and the first thing I wanted to do is throw on a couple nodes onto an existing groom. How do I do that?
It would be great to add the selection flashing thing when changing meshes in sculpt mode using alt-q
Is there an example that would mimic a guide workflow? Like conciously placed guide hairs, not random picks. Currently when changing density on the distribution the hair shape changes constantly, which is probably not preferred.

---

### Post #5 — SimonThommes — 2023-02-09T21:10:44.190Z

Are there plans regarding the modifier stack? With many nodes there can be a lot of clutter, constantly having to expand, collapse and scroll in that list may be time consuming.
Yes, I agree. Using the node-editor and cherry picking inputs to control in the modifier UI would be an option. There are general plans to improve the modifier/node UI with subpanels and flexibly hiding redundant inputs. But that will only be some time in the future.
If I would want to work with maps (use a noise texture as a mask for a clump for example) - is the expectation to go into the geo node editor and connect the node manually?
Yes. That would be the expected workflow. Generally I kept an emphasis of keeping large parts of the functionality exposed in the modifier UI directly, but the node-tree is really the main interface for these nodes.
I’ve been only giving it a quick try and the first thing I wanted to do is throw on a couple nodes onto an existing groom. How do I do that?
Adding the nodegroups as modifiers is indeed right now a bit tedious. But there is a patch already to allow drag and drop into the viewport. That patch has been approved today afaik and should be merged any day now.
It would be great to add the selection flashing thing when changing meshes in sculpt mode using alt-q
I’m not sure what that means tbh
Is there an example that would mimic a guide workflow? Like conciously placed guide hairs, not random picks. Currently when changing density on the distribution the hair shape changes constantly, which is probably not preferred.
Hm, I see the issue here. Unfortunately in favor of being able to propagate arbitrary attributes from the surface mesh I had to remove the original guides from the curves and promote the closest new curve to be guide. That results in some inaccuracy and also these jumps, as a different curve receives the guide status with a different ID for the randomization of its shape.
I’ll try to think of a more stable approach that would still be acceptable…

---

### Post #6 — dan2 — 2023-02-09T21:32:20.825Z

Sounds great, thank you for the reply!
SimonThommes:
I’m not sure what that means tbh
In sculpt mode when switching meshes using alt-q we get a bright flash -
I’d be great to get similar visual feedback in curve sculpt mode, because currently while switching works, one can only guess which groom is being sculpted on unless interacting with it using a tool.
SimonThommes:
Using the node-editor and cherry picking inputs
I’m trying to think of more complex scenarios like the bear in Revenant, Planet of the apes, Lion king etc. the complexity would be pretty big. While 10 node groups can be worked with, 100 node groups might be an issue, without the ability to organize and group them in the UI.
SimonThommes:
That would be the expected workflow
Quickly accessing masks, painting them or modifying their values could be time consuming as well, if we’re relying on doing that in the node editor.
SimonThommes:
remove the original guides
I guess for a lot of people doing groom matches, working with guides would be essential. Placing them consciously, visualizing them in the viewport, selecting or grouping one or several of them is something that would happen quite frequently.

---

### Post #7 — SimonThommes — 2023-02-09T21:57:03.627Z

dan2:
In sculpt mode when switching meshes using alt-q we get a bright flash -
I’d be great to get similar visual feedback in curve sculpt mode, because currently while switching works, one can only guess which groom is being sculpted on unless interacting with it using a tool.
I see, I wasn’t even aware this operator also already worked for curve sculpting tbh. It sounds reasonable to me to add this there as well. Not sure if this a bug report or a feature request. I can make a note and bring it up.
dan2:
I’m trying to think of more complex scenarios like the bear in Revenant, Planet of the apes, Lion king etc. the complexity would be pretty big. While 10 node groups can be worked with, 100 node groups might be an issue, without the ability to organize and group them in the UI.
Quickly accessing masks, painting them or modifying their values could be time consuming as well, if we’re relying on doing that in the node editor.
For more complex scenarios the intention is to leverage the node-editor more and more. It’s reasonable to try and keep the modifier interface nice and clean, but for the proper flexibility the node-tree is the ultimate way to go. Of course, the way things are exposed in the modifier can still be improved, but for now we have to work with what we have. This will be the first iteration of the system and it will definitely improved/expanded over the coming releases.
dan2:
I guess for a lot of people doing groom matches, working with guides would be essential. Placing them consciously, visualizing them in the viewport, selecting or grouping one or several of them is something that would happen quite frequently.
Oh yea, a guide workflow like that is definitely the intention. There is a patch to have an overlay of the guide geometry in sculpt mode that will make it easier to select and sculpt guides.
I just pushed an update to the file that makes the guide ID stable and ensures that a generated new guide curve matches the original guide exactly. So the jumping around shouldn’t happen anymore.
The guide workflow is also more powerful in the node-tree version, but for the use in the modifier stack this is from my testing the best way moving forward.

---

### Post #8 — dan2 — 2023-02-09T22:15:08.327Z

SimonThommes:
I can make a note and bring it up.
SimonThommes:
a guide workflow like that is definitely the intention
Awesome, thank you Simon! Really appreciate it.
SimonThommes:
the intention is to leverage the node-editor more and more
I understand. Sounds feasible. I do prefer working with nodes, but it’s also super easy to break stuff. In most pipelines there’s often the issue of flexibility - I call it an issue because everyone does things a different way and a lot of time goes into making node networks readable and easy to use, with very mixed results. I just had a colleague talk to me about him having to untangle a katana node graph for days, this is also a recurring thing in fx/houdini or nuke.
A bit like texturing - it would be great to have a UI for groups/layers/masks as an alternative to having to dive into a node editor with all it’s complexities. In a pipeline with many people involved there will be a variety of skill sets and preferences, and the bottom line is always speed and efficiency.

---

### Post #9 — DanielBystedt — 2023-02-09T23:57:32.296Z

Amazing work Simon! I’m really liking the new braid and curl nodes :-).
Here are some thoughts:
Smoothen curves
Pin at parameter does not seem to have any effect. The root point changes position when weight is at 1 and lock ends == False. I would assume that the root point wouldn’t move with those settings.
Clump hair curves
Unclear what guide index map means. When I change the default value -987654, the clumping disappears. Perhaps only documentation is needed?
Shrinkwrap
I’m missing a shrinkwrap node that I made a prototype for. This is useful for wet fur that sticks closely to the skin and also for pusing points out that ended up under the surface.

---

### Post #10 — SimonThommes — 2023-02-10T10:47:25.621Z

dan2:
A bit like texturing - it would be great to have a UI for groups/layers/masks as an alternative to having to dive into a node editor with all it’s complexities. In a pipeline with many people involved there will be a variety of skill sets and preferences, and the bottom line is always speed and efficiency.
I see your point. I think this is something that will also crystalize more as people are using the system and maybe a node-tree abstraction as is planned for the texture nodes can also be applied here. But overall, I think, a safe bet is just continuing with what we are planning anyways, which is to expand the node-tree capabilities with a simplified modifier UI and making it more powerful and structured with more options for a better UX (like subpanels, enums, dynamic socket type and number)

---

### Post #11 — SimonThommes — 2023-02-10T10:53:25.363Z

DanielBystedt:
Smoothen curves
Pin at parameter does not seem to have any effect. The root point changes position when weight is at 1 and lock ends == False. I would assume that the root point wouldn’t move with those settings.
Hm, I’ll look into that!
DanielBystedt:
Clump hair curves
Unclear what guide index map means. When I change the default value -987654, the clumping disappears. Perhaps only documentation is needed?
That input is intended for use in the node version only to pass in an explicit guide map from previous nodes. We were going back and forth a bit on how we want to handle sockets that only make sense in the node and not in the modifier, but eventually this input will not be visible in the modifier. There is a patch afaik.
DanielBystedt:
Shrinkwrap
I’m missing a shrinkwrap node that I made a prototype for. This is useful for wet fur that sticks closely to the skin and also for pusing points out that ended up under the surface.
The node I made in replacement is called Hair Surface Collision, I didn’t realize your use-cases went beyond pushing points outside of a mesh. I can add a toggle to affect points outside of the mesh as well. I guess the naming might need to be revisited then.

---

### Post #12 — Hadriscus — 2023-02-10T11:36:40.621Z

I’m sure once textures are overhauled we’ll be able to expose texture sockets to geonodes modifiers. Having to dig into the node tree to add a mask is a pretty big hurdle for anyone not familiar with geonodes, and as always we can’t expect everybody to be.

---

### Post #13 — SimonThommes — 2023-02-10T13:26:09.405Z

@DanielBystedt
The pinning for the smooth node should be fixed and I added a
Shrink to Surface
parameter to the collision node. To me the name would still be okay, but maybe we’ll rename it.

---

### Post #14 — dan2 — 2023-02-10T18:38:06.532Z

SimonThommes:
simplified modifier UI and making it more powerful and structured with more options for a better UX (like subpanels, enums, dynamic socket type and number)
Well, with subpanels, dynamic sockets and texture inputs everyone could basically build their own little panel for their nodes, so I guess that could work just as well. I was hoping that template lists could get some love (like the outliner got a while ago) to at least have multi select and hierarchies, but if a node workflow is the main direction then it’s perfectly understandable to focus on that.
I found a little bug of sorts in the test scene. When adjusting the profile it’s having some issues with decimals (0.01 works, 0.1 gives us 10, and 1 gives us 1 but a much larger radius than there was originally with 1)
I looked at the node graph and saw that the radius is a multiplying the shape, which makes sense, but didn’t want to spend all that time untangling the math in the shape range group - you’ll probably know what to do right off the bat.
For consistency, I think every example groom should have Hair Shape and Distribution exposed. Currently not all do, and the naming is different for them, on some of them.
Also, some brushes work great, others change the whole groom (I guess the ones that are either changing the root positions or the number of points) which is something that would need to be avoided if possible -
It’s a super fun scene to play around with though, and I’m sure it’ll want people to jump right into the node graph and do their own things. Thanks again for working on this, great stuff!
And a quick suggestion on the side - I think it’d be great for these things to get some more exposure. Not sure who’s in charge of social media, but it’s not every day that one can test the new hair system and give some feedback. There are not a lot of users visiting devtalk since it’s generally not the place for user feedback.

---

### Post #15 — SimonThommes — 2023-02-11T13:56:24.201Z

dan2:
I found a little bug of sorts in the test scene. When adjusting the profile it’s having some issues with decimals (0.01 works, 0.1 gives us 10, and 1 gives us 1 but a much larger radius than there was originally with 1)
I looked at the node graph and saw that the radius is a multiplying the shape, which makes sense, but didn’t want to spend all that time untangling the math in the shape range group - you’ll probably know what to do right off the bat.
I’m actually not sure what is unexpected here. Hair with 1m thickness will look a bit ridiculous in any case…
Aah, I see the confusion. The units are set to adaptive in the scene settings. The displayed value will round to the nearest sensible unit. The values you are typing in are in meters, so typing 0.01m = 1 cm, 0.1m = 10cm and so on. You can change how these values are displayed/switch to imperial units in the scene settings.
dan2:
Also, some brushes work great, others change the whole groom (I guess the ones that are either changing the root positions or the number of points) which is something that would need to be avoided if possible -
That’s something we’ll just have to deal with for the time being, I’m afraid. I put quite some effort into trying to keep things as stable as possible, but at the end of the day these are procedural operations that will give a different result for different inputs. There are some things that could be improved on the Blender side. For example there could be an ID per curve that is managed by the sculpting tools.
Maybe we can push for that for 3.6, but depending on the exact use-case there will always be something that is not perfectly stable for certain operations with the procedural generation.
Keep in mind also that this new hair system also allows for a flexible destructive workflow. You can always apply any amount of modifiers and sculpt on the result for exact control.
dan2:
It’s a super fun scene to play around with though, and I’m sure it’ll want people to jump right into the node graph and do their own things. Thanks again for working on this, great stuff!
Thanks for the kind words and thanks for your extensive feedback, it’s much appreciated! The scene itself is only my WIP testing setup, we’ll have an example scene in a similar style (but hopefully much nicer) up on
b.org
for the actual release.
dan2:
And a quick suggestion on the side - I think it’d be great for these things to get some more exposure. Not sure who’s in charge of social media, but it’s not every day that one can test the new hair system and give some feedback. There are not a lot of users visiting devtalk since it’s generally not the place for user feedback.
This is something that is a little bit due to the timeline. Unfortunately the state is still very much unfinished while it needs to be merged in the coming days to make it in time (but it’s getting there). So extensive iteration with lots of user feedback is at this point not really possible on top of what is left to be done regardless, I’m afraid.
The good thing as that these nodes can potentially change a lot between releases, as there are no compatibility issues with them. I’m sure we will get a lot of feedback down the road with the release. So far we have gotten very useful feedback from some powerusers close to the Blender development, so I’m quite confident that the bundle will be in a useful state either way. Replacing the old system entirely will also not be done with 3.5 regardless, so getting a solid fundamental system that we can iterate over seems to be a good way to go for now.

---

### Post #16 — RonanDucluzeau — 2023-02-11T14:00:52.453Z

That looks rough, for the moment.
Examples with disabled or unnamed modifiers, muted connections is confusing.
Tags and Catalogs should be used in asset browser, to distinguish nodetrees generating curves from nodetrees displacing them, from nodegroups for Curves info, from materials for shading (currently all Curves objects have same hair material).
Examples dispatched into collections is not sufficient to clarify things.
Subpanels to quickly find redundant settings (subdivisions, viewport amount, shape, length, distance) is really a must-have to manage density of geometry, generated in viewport, and avoid a crash, or simply to harmonize shape through several modifiers.
Examples with textures or painted attributes should be present.
In absence of an edit mode to create guide groups, ability to paint a mask is really a must-have, too.
I think that an example involving several Curves objects for one haircut would be welcomed.
Subdividing and smoothing through nodes can not be as satisfying as being able to control resolution of guides, per curve or per object.
We have a limited control on placement of waves on long hair by that restriction in sculpt mode.
We have a very complicated control of that with nodes. We need to isolate long curves, to resample them and have to deal with a complicated setup if we want variations along curve.
That is very frustrating to be able to draw any simple Curve object geometry.
But not be able to exploit it with Curves object.
Your node groups are great. But that makes lack of base geometry control more frustrating.

---

### Post #17 — SimonThommes — 2023-02-11T14:26:09.860Z

A lot of the things you are giving feedback on are besides the point of this file. I listed in the initial post what aspects of the nodes are still missing/changing (e.g. tags and catalogs) and the file itself is just the WIP testing file, nothing to be bundled/released.
This upcoming release can not yet possibly aim at replacing the old curve or hair system entirely. A lot more will be possible once all the missing features from either system are merged to new Curves object. On top of that better/more options to customize node/modifier UI are planned.
But afaict none of that can be addressed by an asset pack which this is.

---

### Post #18 — RonanDucluzeau — 2023-02-11T14:32:40.230Z

In UI improvements are not for next release, to me, that looks pre-matured to think about such bundle for upcoming release.
Updated version would be requested for 3.6, anyways.

---

### Post #19 — dan2 — 2023-02-11T18:50:11.766Z

SimonThommes:
switch to imperial units in the scene settings.
I would never do such an awful thing.
That does explain the behavior though - what was confusing is that it was set to 1 by default, and changing it to the same value gave me a different result.
SimonThommes:
That’s something we’ll just have to deal with for the time being
SimonThommes:
there will always be something that is not perfectly stable for certain operations
That’s why it’s important for guides to not be procedurally generated I think. What I can see in production very often (literally with every digi double) is that groom artists get a 3D scan of an actor and have to match the groom to both that and the photogrammetry camera images. That’s only possible with making every clump by hand. Well mostly, but the recurring comment in dailies will be “match that clump in the upper left”, “that other strand is sticking out too much”, etc. A glimpse of what groomers have to deal with can be seen in this
tutorial teaser
for example. Not advertising anything, just wanted to show an example for the photo matching that’s part of a common workflow.
Even with creatures, more often than not it’s either matching a specific photo or a concept (which was most of the time made using photobashing for furry creatures). Supes will literally put one over the other and switch between them until they get a close match. So if people can’t  freeze/mask what they’re happy with they’re probably not going to use it.
That’s for VFX production. Since A/Bing has gained a lot of ground when it comes to supervision I’d imagine AAA gaming would be similar.
SimonThommes:
So extensive iteration with lots of user feedback
More people using it is always good. I think most people understand the time constraints and can set their expectation accordingly. What’s important is seeing how it’s used, what the most requested blockers are and how/if people get around limitations.
SimonThommes:
Thanks for the kind words
Well, thank you for all your hard work! A lot of people are looking forward to this, and since there are no great grooming tools publicly available there’s some real opportunity here.

---

### Post #21 — Andruxa696 — 2023-02-11T20:49:41.172Z

I am agree with most whar
@dan2
wrote.
It would be very nice to have more stable generation, maybe not for 3.5 if it is not possible, but for future relizes for sure .
And ability to chose painted texture masks in modifier for usability.
It would be Amazing to have the ability to generate clumps guide picking from other hair Curves Object.So you can manually change density of clumps and where they will be.(it doesn’t matter how they look, we take only position of hair roots from it to generate clump). So radius of the clump (distance between clumps) and their place always will be where you want. Maybe picture will help you get what I mean.( I moved green hairs Curves object (that will be used to generate clumps) upper so you see it better)
image
600×871 96.2 KB
I hope you understend what I mean.
Thanks Simon for your work, I love it already. Very fun file to play with.

---

### Post #22 — Xeofrios — 2023-02-12T10:17:11.214Z

Thanks for all the hard work and thought put into these nodes! Some of my initial thoughts
The shape input does not do what I would expect it to. I would expect setting the shape to 0 to disable pinning but that does not seem to be the case
image
1022×782 137 KB
I think it would be better if the random output of the curve info node is a float, because
Each time you require a single value you will need a separate XYZ node (more work each time). Plugging the vector directly into a float will result in less variation.
We can’t expect everyone to be aware of this problem
image
1137×730 52.6 KB
Consistency with shader nodes
Converting a random float to a random vector is very easy with a white noise node.
I find a global-space to curve-space (Tangent, Bitangent, Normal) conversion node to be useful
The noise node factor can be split into normal factor and bitangent factor. For example, I wanted the noise along bitangent to be stronger compared to the normal in one of my recent projects. This change can also be applied to the duplicate curves and frizz node.
image
1645×825 122 KB

---

### Post #23 — SimonThommes — 2023-02-13T10:19:20.319Z

Just want to mention that a lot of the feedback in this thread is on issues that we are aware of, but cannot be addressed in this coming Blender release. Building this hair system to be the best it can be will require more iterations, that involve Blender development that goes beyond what can be done with just nodegroups. But most of these things are on the roadmap and will just take some time until they can be prioritized.
But the feedback is very much appreciated, knowing that we’re moving in the right direction is also very valuable!
dan2:
what was confusing is that it was set to 1 by default
I changed this setting myself in the file. By default everything will be in meters.
dan2:
That’s why it’s important for guides to not be procedurally generated I think
That’s why there is a fully supported workflow of manually creating the guide mapping. There is a dedicated not to generate the guide map so that is can be used by the following nodes/modifiers. I’m planning to add more options of how this is created, I didn’t get around to it yet though.
The node is called
Create Guide Curve Map
.
I understand the importance of stability. With layers of procedural operations that depend on each other this is only partially achievable though. With the nodes we ship with Blender it’s for now a bit difficult to accommodate for several different workflows at the same time. Keep in mind that for more advanced use-cases, the node editor always gives the same amount of flexibility that I have building these node-groups.
And for freezing and working on top of something: We are planning to make this a general feature in the node workflow as well, but for now you can always apply the modifier and manually tweak whatever result you got.
Andruxa696:
It would be Amazing to have the ability to generate clumps guide picking from other hair Curves Object
(Partially also related to my previous response in the paragraph above)
This is definitely possible, I will try to find a way to make this intuitive as part of the
Create Guide Curve Map
node. The issue right now is that there can be several different ways of generating the guide map. There needs to be better node-group customizability to allow us to put these all into one node with a dropdown menu to pick which type should be used. Right now this needs to be split into different nodes (which I usually want to avoid) or all inputs need to be available and depending on which are used the another method is used. But that get confusing quickly, as the UI is not adapting.
This issue was already clear previously, but shipping nodegroups as full on feature sets elevates the issue to a more critical level imo. Hopefully we can address this until the next release after and adjust these node-groups in that regard.
Xeofrios:
The shape input does not do what I would expect it to. I would expect setting the shape to 0 to disable pinning but that does not seem to be the case
Pinning is currently always happening. Do you have a use-case for when you would need it disabled?
Xeofrios:
I think it would be better if the random output of the curve info node is a float, because
Good point, I agree. I will change that.
Xeofrios:
curve-space (Tangent, Bitangent, Normal) conversion node to be useful
Hm, to me this sounds like something that would be better suited as a generic space conversion node, rather than a specific node-group. This topic came up at some point, I believe.
Similar to the shader nodes
Vector Transform
node, but with axis inputs.
Tangent space is something that is also very useful with meshes, but there are currently no builtin tools for that either. I think that is something we can live with being available to advanced users for now, until we can support it properly.
Xeofrios:
The noise node factor can be split into normal factor and bitangent factor. For example, I wanted the noise along bitangent to be stronger compared to the normal in one of my recent projects. This change can also be applied to the duplicate curves and frizz node.
image
1645×825 122 KB
I can see that being useful in certain cases. But similar to my previous point: There is currently no proper support for aligning the normal of a curve, so I don’t think it really makes sense to build separate control like that into the nodes that we ship.
I think what I can do for now would be to expose an attribute output of the offset vector. Advanced users can then more easily adjust the deformation space how they need it.

---

### Post #24 — dan2 — 2023-02-13T18:52:40.165Z

SimonThommes:
a fully supported workflow of manually creating the guide mapping
Ah, got you. Yes, basically
this demo here
from Jacques is kind of what I was looking for. Groom and tweak the settings on the same hair object, without having to jump back and forth between a parent and a child groom.

---

### Post #25 — SimonThommes — 2023-02-13T19:04:34.244Z

Right, I mean that’s pretty much already how it works by default. The only difference is that right now the children are spawned on the entire surface using a mask input, rather than only within a certain radius around the guide.
I was thinking of adding a culling radius, but so far this didn’t seem to really be all that useful, but I can try it out and see how it feels.
But yeah, using the original curves as the guides is the intention for most workflows and how it should work by default. On top of that there are other ways of manually defining the guide map. Supporting all of them out-of-the-box at the same time is probably not possible without making a confusion mess of. That needs a more customizable node/modifier UI. Same thing for the hair parting.
Right now there are some compromises that need to be made with the tools that are exposed with these nodes that will be addressed in the future.

---

### Post #26 — dan2 — 2023-02-13T19:11:12.643Z

SimonThommes:
how it works by default
Ah, you’re right. He just did a basic clump thing so it wasn’t so obvious that everything is changing when he slides a single guide on the surface. I take that back then, this probably wouldn’t work.
Well, as long as you guys aware. This is great to play around with and I don’t think anyone is expecting the whole system to be perfect right off the bat.

---

### Post #27 — Xeofrios — 2023-02-14T09:31:38.296Z

SimonThommes:
Pinning is currently always happening. Do you have a use-case for when you would need it disabled?
Sorry my bad, I forgot how shape works in Blender. I was comparing it to exponentiation. But still, your implementation is not exactly clear to me. Setting the shape to negative in the noise node creates pinning on both ends. While doing so in the clump node simply clumps at the root instead of the tip.
Another small thing- the shape profiles are not as smooth as I would like them to be
image
1017×757 104 KB

---

### Post #28 — SimonThommes — 2023-02-14T10:43:38.528Z

Yes, it’s not actually symmetrical in that regard. I had it differently at first, but then got feedback that in a practical use-case you would want to keep the root pinned, even with a negative shape of noise. So I opted for doing it like this in favor of practicality over making it perfectly logical.
That’s one of the trade-offs I made in that regard.

---

### Post #29 — SimonThommes — 2023-02-14T10:50:31.778Z

Xeofrios:
Another small thing- the shape profiles are not as smooth as I would like them to be
image
1017×757 104 KB
Yes, part of that issue is that the catmull rom interpolation creates an overshoot. If you increase the amount of control points wit will be a lot smoother. I can try iterating over the function to achieve a better result for average cases though.

---

### Post #30 — dan2 — 2023-02-15T04:27:08.048Z

Really cool to see the groups in today’s build! Drag and drop works like a charm, the icons look neat, love it. Looking at the node graphs is intimidating I got to say.
While starting to play with them, a question came up regarding multiple hair clumps -  currently when I try to make big clumps, and try to further break them up, it doesn’t really work by adding another clump on top of the first one -
How would you go about doing that?
Actually, make that a general question for adding clumps. It seems it doesn’t have much of an impact when preceded by certain node groups -

---

### Post #31 — irfan — 2023-02-15T08:16:15.136Z

Creating different levels of clumps is the first thing I tried as well
When the “Existing Guide Map” Checkbox is turned off in the following Clumps, it does work.
Here are two examples of the same thing:
The left one is using the seperate modifiers and the right one is using the nodegroups instead.
For now I much prefer the connected nodegroups from the right example.
@SimonThommes
Is there a disadvantage in using it that way?
Also, is there a way to visualize the original guidehairs somehow?
image
1920×1181 160 KB

---

### Post #32 — SimonThommes — 2023-02-15T16:50:35.290Z

dan2:
Looking at the node graphs is intimidating I got to say.
Yes, I didn’t have a chance to actually clean them up yet. That will diefinitely happen, I might do a first pass of that today, to avoid people freaking out, as Blender 3.5 is now in beta.
dan2:
How would you go about doing that?
It’s important to have an understanding of the guide workflow that these nodes use for this. Unfortunately it isn’t super intuitive, as I don’t have a way to present it in a super clear way, that will be polished for 3.6, for now we have to rely on educating people with documentation I’m afraid. (which doesn’t exist yet, but it will before the release)
Every operation that creates a map from each curve to its guide stores this on the curves as an attribute. So whenever this exists and
Existing Guide Map
is turned on, it will use the mapping of the previous operation. So by default, If you start with spares guides, interpolate them on the surface and then clump, the clump guides will be the original, sculpted guides.
If that attribute does not exist or
Existing Guide Map
is turned off, the operation will fall back to the settings in the node and create + store a new guide map attribute, which can then be used by the next operation.
So in short: If you want to clump with different guides, turn of
Existing Guide Map
or use the
Create Guide Index Map
node explicitly in between the operations.

---

### Post #33 — SimonThommes — 2023-02-15T16:56:58.016Z

irfan:
Is there a disadvantage in using it that way?
Quite the opposite actually. I did focus mainly on the modifier usage, as that is the more restricted way of using them, so if this works the nodes will usually also work. But in nodes you have a lot more options for extending functionality.
There are some issues with UX that we unfortunately couldn’t resolve for this release, but will in the future, like having to manually point to the surface object and the attachment UV map.
So in your example you should ideally link up a
Named Attribute
node pointing to the right UV map to the
Surface UV Map
input.
irfan:
Also, is there a way to visualize the original guidehairs somehow?
A patch has recently been merged that visualizes the original curves in sculpt mode with an overlay. The first iteration of edit mode for the new curves has also landed and visualizes them as well.
To get a preview in the node-tree you can compare the Guide index attribute with the index. If they are equal the curve is a guide.

---

### Post #34 — irfan — 2023-02-15T17:04:42.777Z

That´s great! Looking forward to read the documention when it is available

---

### Post #35 — dan2 — 2023-02-15T18:35:31.708Z

SimonThommes:
It’s important to have an understanding
Yes, makes sense. For some reason I was dropping them into the viewport and using the modifier panel, but that’s not really going to work. Using the node editor as you suggested seems way more intuitive for this workflow.
Got me confused with the terminology
At work a map would usually refer to a baked version of a mapping, most times in form of a texture (like a dsp map, weight map, etc.). Getting closer to get the hang of it now.
Looking forward to the docs as well. Exciting to see the first node groups arrive! Can’t wait for the asset shelf as well - will that be something for 3.5, or rather something for later?

---

### Post #36 — koko_ze — 2023-02-20T22:43:03.182Z

How will the node setups get cleaned up (or are they already)? With frames or groups?
I’ve tried to reorganize the “Generate Hair Curves” nodes but in the process that produces a lot of groups which makes the “group list” long…
Current nodes:
Current nodes
1920×544 45.1 KB
Packed version:
Packed nodes
3252×874 243 KB
Group list:
large group list
471×825 40.5 KB

---

### Post #37 — SimonThommes — 2023-02-21T10:48:27.831Z

They aren’t cleaned up yet. I’ll do that soon though, hopefully.
I won’t be creating nested groups if there isn’t actually shared functionality. I’ll use frames, reroutes and hiding of sockets and options when sensible.

---

### Post #38 — William-Hurst — 2023-03-09T12:37:05.080Z

Just started playing with this stuff in the 3.5 Beta, and the first thing that popped to mind was the Shrigwarp Hair Curves might allow for basic rigging of hair. So after paying with it, it does. However, it has a limited range. Once the controlling mesh gets too far away it loses influence.
When it comes to GeoNodes I have zero experience. My Node knowledge stops with Unreal Engine and logic. So I can’t do this myself… yet. However.
TL;DR. If the “Shrinkwrap Hair Curves” node group kept the hair inside of the controlling mesh regardless of distance from the hair curves this could open up the possibilities for some really cool stuff.
Also sorry if this had been said before. I confess to not reading and only doing a search for the word “rig”.

---

### Post #39 — SimonThommes — 2023-03-09T18:00:47.773Z

Hair dynamics in the sense of rigging or simulating the hair are things that will need to be addressed in more detail later. For now the Surface deform modifier that is added by default to a new hair object is the only builtin way to move the hair with an animated surface.
Generally this topic will be revisited for a later release, the main focus for now has been static grooming cases.

---

### Post #40 — Royston — 2023-03-21T09:04:07.530Z

I just wanted to start by saying that I appreciate all the work thats gone into creating these node setups.
I think there is a case though for some “simple” hair node setups. I come from a teaching point of view and find these node setups pretty complicated to work out myself let alone trying to explain to someone who may have more difficulty than myself to understand. Is it possible to have some less complicated node setups that are a bit easyer to explain the inner workings? Maybe prehaps some simple templates with less options/controls and a set of more advanced nodes for people that know what they are doing more. I think its about making it all a bit more accessable for all artists! Cheers.

---

### Post #41 — modmoderVAAAA — 2023-03-21T11:24:18.361Z

The current version is just the simplest working version. As I understand it, they will still be redone to be much easier

---

### Post #42 — SimonThommes — 2023-03-21T14:30:16.509Z

Hey, so the intention for these nodes is less for people to go inside and make changes. For that they definitely would need to understand what’s going on inside. But for the most part artists can treat these as monolithic nodes that they don’t need to go inside of, just like any other node.
The notion that to use these you need to go inside the node-tree is a misunderstanding that I’ve seen before. But that’s not the case, the intention is very much to use these nodes on a surface level. Either as a modifier directly, only touching the parameters in the modifier panel. Or as a node on the top level, for example by starting with a modifier and using the
Move to Nodes
operator.
Also:
I’m not sure which version of the nodes you are talking about. Just the last few days I went over all the node-groups to clean them up by reorganizing the nodes and adding panels with titles of what is going on. That said, some of them are still quite difficult to work through, but that’s just how they work and at some point we just need to do better with the UI of the node editor to make node trees easier to understand.
Maybe you just saw a version before that, maybe not.
But yeah, regardless of that:
The intention is for people to use these nodes, as they are, in higher level setups which will then be quite simple. The documentation, example files and educational material in video still needs to be prepared for the release.

---

### Post #43 — FreeMind — 2023-03-23T08:12:29.808Z

This is good development.
The only thing i don’t like is the icons. They don’t look very “Blender-like”.
I’d envision them to look more simplified, not 3D renders. More into the stylistic direction of active tools in sculpt mode.

---

### Post #44 — Shwaky — 2023-03-23T08:20:24.574Z

But they are not icons but thumbnails, the node groups are assets

---

### Post #45 — FreeMind — 2023-03-24T09:21:16.987Z

Whether they’re called “icons” or “thumbnails”, my point stands.

---

### Post #46 — Hadriscus — 2023-03-24T10:22:59.200Z

What they mean is they’re automatically generated by capturing the viewport. That’s how assets get their thumbnails. Now I guess the system could be made to use Eevee instead of solid shading, or something, to improve on the looks. But it’s supposed to be wysiwyg, and I believe that’s a good thing

---

### Post #47 — FreeMind — 2023-03-24T23:31:53.618Z

Assets can use custom thumbnails. (Actually, they are not even called “Thumbnails” in the blender UI, but “Previews”).
And these previews were not autogenerated. These are custom made.
Nodegroup assets do not get autogenerated previews. By default, the preview of a nodegroup asset looks like this:

---

### Post #48 — Hadriscus — 2023-03-24T23:42:19.520Z

My bad, didn’t know that

---

### Post #49 — dan2 — 2023-03-25T09:34:26.956Z

For what it’s worth, I like them. They clearly put effort into making them.
A more simplified approach would look weird if we can’t make the size smaller.

---

### Post #50 — koko_ze — 2023-03-26T19:13:46.720Z

The node-setups are much more cleaned up now, great job!
But there is one thing that I find confusing. Why are the “Mesh, Point Cloud, Volume, and Instances” being routed over the network instead of just using another Group input at the end?
Current:
Current
2278×641 163 KB
Proposed:
Proposal
2349×546 131 KB
Ending closeup:
end
1386×1009 98.7 KB

---

### Post #51 — LudvikKoutny — 2023-03-26T19:15:35.420Z

Yeah, it shocks me that even hardcore blender users aren’t aware you can have multiple group inputs. It needs to be advertised more.

---

### Post #52 — koko_ze — 2023-03-26T19:17:16.994Z

Well, multiple group inputs are used in this network but not for that specific case which I don’t understand.
Maybe it is there to save performance because you only need to use the “Separate components” node only once?

---

### Post #53 — LudvikKoutny — 2023-03-26T19:19:21.573Z

It should be negligible compared to all the other stuff being calculated.

---

### Post #54 — modmoderVAAAA — 2023-03-26T19:32:48.428Z

Speaking of something like
geo_std
, one could have a group of nodes that would receive a geometry and 5 booleans inputs for each component to just disable the curves.

---

### Post #55 — modmoderVAAAA — 2023-03-26T19:38:56.416Z

If simplified for experienced users, as having seen the code, I will say:
If you are not editing the geometry (assigning a new attribute, or deleting something, join, …) then this is very cheap.
If you instantiate, it’s very cheap.
If you are joining with many nodes, it is better than one. Not sure why, but this is the test result.
Many inputs don’t have much overhead, again, as long as the data doesn’t change, you’re not missing anything.

---

### Post #56 — dan2 — 2023-03-29T21:26:40.628Z

Fist off, congrats to the devs on the release! Simon’s intro videos seem really helpful as well.
Had a lengthy post with questions which partially answered themselves throughout the day, plus the fact that I need more mileage with using the system.
Quick remaining question - any chance we can get a guide hair overlay with adjustable color/thickness? I might have seen something in the works, not sure if it’s planned anytime soon though.

---

### Post #57 — mlaveaux — 2023-04-02T19:18:02.873Z

After playing around with the interpolated hair node and these node groups I must say that they are very useful basis for future hair grooms, good job on that! I am not sure whether the issue tracker should now be used for these groups since they are part of the release? However, the ‘Clump Hair Curves’ group is behaving incorrectly in a number of cases that seem to be mostly related to guide curves being deleted by the ‘Density Mask’ or ‘Mask Texture’ in the ‘Interpolate Hair Curves’ group. I couldn’t find this issue being described before.
It seems that in some cases the ‘guide_curve_index’ becomes zero for all children. There is some logic that tries to select new guide hairs whenever one is deleted that I don’t fully understand. However, I could see that no ‘New Guide Points’ are being selected by ‘Select New Guides by Distance’. My ad-hoc solution was to avoid original guides from being deleted, but maybe it would be nice to resolve this procedure. I don’t quite understand why it selects a new guide hair and then puts it back into the spot of the original one. Doesn’t this just make it equivalent to the original ones (except that some get deleted because the closest one might overlap)?
I cannot seem to share attachments yet, but I will try to make some examples to showcase the issue.

---

### Post #58 — SimonThommes — 2023-04-03T10:13:54.595Z

Thank you! I’m glad a lot of the questions have been answered already.
dan2:
Quick remaining question - any chance we can get a guide hair overlay with adjustable color/thickness? I might have seen something in the works, not sure if it’s planned anytime soon though.
It’s not currently planned afaik. However, the way that the guide overlay works right now was added relatively late into the release cycle and once we have more user feedback I can definitely see changing that or adding more options.

---

### Post #59 — SimonThommes — 2023-04-03T10:29:22.960Z

mlaveaux:
However, the ‘Clump Hair Curves’ group is behaving incorrectly in a number of cases that seem to be mostly related to guide curves being deleted by the ‘Density Mask’ or ‘Mask Texture’ in the ‘Interpolate Hair Curves’ group. I couldn’t find this issue being described before.
Yes, due to the fact that the mapping is currently entirely based on the index, anything that changes the index breaks the mapping. I believe what you are describing is something different though and is not actually ‘breaking’ but the pattern of clumping is changing based on the curves that are available.
I put some effort into ensuring that the operations wouldn’t change depending the density of the base curves. This is the exception due to the way that the guides are selected based on the exisiting curves. I do want to make this more stable in future iterations of the system, but right now that is a restriction and part of how the system works.
The guides are selected procedurally. So when the existing curves change, the guide pattern also changes. To have more specific control you can either use the original guide curves, or generate guide points separately that you use with the
Create Guide Index Map
node. I’m not sure whether we mentioned that specifically in the docs already.
mlaveaux:
I am not sure whether the issue tracker should now be used for these groups since they are part of the release?
Yes, these nodes should be treated just as any other functions in Blender and issues are tracked the same way on
projects.blender.org
. The previous point is a known issue though, I would say. We just need to make sure that it’s documented if it isn’t already.
mlaveaux:
It seems that in some cases the ‘guide_curve_index’ becomes zero for all children. There is some logic that tries to select new guide hairs whenever one is deleted that I don’t fully understand.
I’m not exactly sure what you are referencing here. There is only ever 1 guide map on the same attribute currently, which is always replaced, but in nodes you can pass around previous guide maps as anonymous attributes, if the indices didn’t change. It should never just all become 0, unless there is not a single guide.
mlaveaux:
I don’t quite understand why it selects a new guide hair and then puts it back into the spot of the original one.
This is a bit of a workaround to make sure that all curves propagate the attributes from the surface mesh, as the original guides don’t. Hopefully this can be solved in a better way in the future.
Thanks for looking at this in-depth. I do believe that most of the things you run into might be known issues. I have a long list of things to improve myself. But please do make reports, for what you see as issues, if you can’t find anything about it in the documentation.

---

### Post #60 — mg1 — 2023-04-04T10:39:18.630Z

Great work all around so far. having played abit with Geometry node before, specifically on manipulating mesh/curve lines to procedural Haircards.
I noticed some inconsistencies in the new Hair curve object type when compare with Mesh and curve objects.
As far as i can tell the new Hair Curve and default hair geonodes are dependent on 2 “bespoke” attributes relative to the skin/growth mesh:
rest_position
(spline, Vector) &,
surface_uv_coordinate
(spline, 2D vector),
which are initiated upon object creation.
From debugging the values I tried to capture the corresponding vectors/data with the following nodes
FsxenBvacAEEetc.jpeg
2320×1098 130 KB
but I cant find a way to export the
surface_uv_corodinate
attribute in datatype 2D Vector

---

### Post #61 — mg1 — 2023-04-04T10:40:11.949Z

I also noticed some incompatibility when trying to convert mesh /curve object into the new Hair curve object type. Since there is no option to convert the attributes under Hair curve properties, etc. i cant convert the 3d vector to 2d vector
FsxeEy2akAAoIm1.jpeg
2743×1277 165 KB

---

### Post #62 — mg1 — 2023-04-04T10:42:20.886Z

i would like to suggest some additions:
add missing attribute tab under “curve properties”,
add datatype “2d vector” for geometry node output,
add “convert attribute” option in hair curve properties.
update mesh/curve “convert to hair curve” similar to below user flow.
Fsxj4W7aYAAjHpm.jpeg
1702×1606 172 KB
P.S. I previously reached out to Simon on twitter, and thanks for recommending me to post here.

---

### Post #63 — Baardaap — 2023-04-04T11:31:09.624Z

mg1:
but I cant find a way to export the
surface_uv_corodinate
attribute in datatype 2D Vector
You need to use
Store Named Attribute
. See
UV Unwrap Node - Blender 4.2 Manual

---

### Post #64 — SimonThommes — 2023-04-07T09:46:34.378Z

For the UV attribute you need to indeed use the
Store Named Attribute
node currently. I’m not sure why the 2D vector option is not available in the nodegroup outputs to be honest though.
The issues with the conversion between legacy curves and the new curves will be resolved by proxy at some point as the old system is being phased out in favor of the new once the features are all there. Of course, we should have some operators for conversion in the meantime though.
But keep in mind that geometry nodes already has a lot of functionality for this exactly. For your proposal you can for example just use an
Attach Hair Curves to Surface
modifier after piping in the legacy curves geometry on a new curves object.
Of course, that’s not a builtin operator. But as I said before, the idea is not to have both systems coexist in the long run. So fostering an environment where both are kept compatible at all times is at least to some degree misused development time.

---

### Post #65 — 2905710881 — 2023-04-08T21:19:27.403Z

Is it possible to translate blender’s built-in geometric node assets?

---

### Post #66 — SimonThommes — 2023-04-11T12:06:00.940Z

Unfortunately not yet in Blender 3.5, but in Blender 3.6 this will possible afaik, due to this commit
#105933 - I18n: Extract and translate asset catalog and asset names and descriptions - blender - Blender Projects

---