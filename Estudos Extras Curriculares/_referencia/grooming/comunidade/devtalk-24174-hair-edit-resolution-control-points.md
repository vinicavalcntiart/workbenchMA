---
titulo: Hair Edit Resolution & Control Points
autor: dfelinto
url: https://devtalk.blender.org/t/hair-edit-resolution-control-points/24174
data: 2022-04-28
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — dfelinto — 2022-04-28T15:14:38.290Z

Hi,
I’m exploring how much aware artists need to be of the control points during the hair combing process. The core of this discussion is the hair resolution. There are actually different hair resolutions, for instance:
Edit resolution: How many curve control points each hair strand has.
Simulation resolution: How many hair strands and control points are sent to the physics solver.
Rendering resolution: How smooth the final hair curves are drawn.
For this post I want to focus only on the
edit resolution
. There are a few moments in the process of hair combing that the artist is aware of the edit resolution:
Adding new hair strands.
Tweaking the control points in edit mode.
Sculpting the hair shape altering its silhouette or length.
The ideas discussed by the hair development team so far:
When creating new hair strands, you can set not only length but also the number of control points.
Tools in edit mode to subdivide a hair strand, or “dissolve” a control point.
An operator to resample the (selected) hair strands to a target number of “control points” or “control points/meter” (similar to how voxel remesh works for mesh sculpting).
At high precision levels of sculpting, editing of individual control points can get to the same level as in edit mode, e.g, in mesh sculpt mode that is solved with an overlay of the nearest vertex to the brush.
Dynamically change the amount of control points during sculpting based on a target control point density per curvature setting.
*
*
This may impact performance considerably, potentially making it a no-go for sculpting large chunks of hair at the same time.
I would love to hear other scenarios where the hair resolution may matter and whether the options here presented would be enough. Specially if dynamic changing the hair resolution is not prioritized.

---

### Post #2 — dfelinto — 2022-04-28T16:08:34.223Z



---

### Post #3 — DimitriBastos — 2022-04-28T20:43:41.859Z

Hi, Dalai. Thanks for all the info!
Is it possible to create a global subdivision (in lack of better word in the context of hair… or maybe not?), and also to have local/controlled/masked subdivisions? The same way where a node tree can have different branches each one with certain subdivision node. Because, for design sake, sometimes you may want to see the silhouette of a certain part of the hair at a higher subdivision while combing the rest at a lower subdivision for performance reasons.
I hope this makes sense.

---

### Post #4 — ikakupa — 2022-05-01T09:33:50.289Z

Hello Dalai,
I have previously
experimented
with procedural hair creation with geometry nodes. With new spline/ hair Data-Block the endless possibilities are now open, which is pretty exciting.
These ideas sound interesting, particularly resampling based on points per meters. The dynamic resampling based on curvature is something, that will be quite usefull. Just to extend the later, it will be helpful to have something like this as an operator, to quickly decimate the hairs all at once with percentage slider
There is a scenario which I don’t see yet mentioned, maybe it should be discussed somewhere else, if so please let me know. I am talking about shapekeys/sculpting layers for hairs. I am interested if these different resampling methods will be compatible with some kind of cached multi-res node with layers in the feature? It looks like these editing methods are destructive, and they will not be compatible with layered workflow.

---

### Post #5 — RiccardoBancone — 2022-05-01T12:22:56.148Z

Hi Dalai, in my limited production experience with blender grooming, I experienced being useful also to  have non uniform subdivision along hairs. In particular, for long hair, i used to select all roots, grow the selection with " Ctrl +" and subdivide hairs only near their root.
I found that useful because long straight hair tend to bend a lot in that part close to the scalp, and then go down fairly straight. To be honest, I’d like to have that control for styling/combing, and possibly, more procedural and non distructive as it can be.
I’m curious to know what other users think about this, and if anyone used this trick as well.
Edit:
I’m reading more carefully
@ikakupa
's post where he/she talks about curvature based resampling, and that made me think about the possibility to procedurally resample hairs, driving the density with
curve parameter through a ramp, that can be in normalized parameter range, or absolute length unit and then clamped or extrapolated. In that way one could procedurally obtain the outcome I described previously by , say, tripling the sampling rate on the beginning of the hair, and having uniform lower density on the rest of the hair.
The point is, could it be possible to manually edit/sculpt/comb the output of that procedural resample (I guess performed via node) without destructively apply it ?

---

### Post #6 — DarkKnight — 2022-05-01T13:23:01.416Z

Thats the number one trick i use. You want a nice falloff from the hair to the head. Also good to control the hair dynamics this way so the root is stiffer than the rest of the hair with more points.

---

### Post #7 — RiccardoBancone — 2022-05-01T13:27:00.536Z

Absolutely , same here with the stiffness control, I didn’t mention it because the topic is about editing, but I can confirm!

---

### Post #8 — DanielBystedt — 2022-05-02T22:10:10.628Z

Hi Dalai,
I think that the examples you bring up for resampling curves are great. Resample with same amount of points per spline/curve is especially useful when using some groom systems in other applications. Some of these applications require the imported curves to have the same amount of points per curve.
Dissolving hair strands based on angle could increase hair performance when simulating, so I’m all for that.
You mentioned:
Dynamically change the amount of control points during sculpting based on a target control point density per curvature setting
Personally I don’t think this would be all that useful, especially since it will impact performance. I think an operator for resampling the curves being edited would work just fine.
===========================
Here I’m going slightly off topic:
In my opinion, blender is actually one of the best hair solutions I’ve worked with when it comes to grooming. It has only been procedural scattering and deformation that could be improved.
When it comes to editing, an excellent tool is “select random”. This makes it possible to easily create overlapping in the hair. Bad cg hair usually has a very “uniform” look to it and by creating overlap you avoid that.
Selecting specific splines/curves can sometimes be tricky, since you need to show the points per curve and use “select linked” (hotkey L).  Being able to select specific curves in “path edit mode” would be nice. It would also be very cool to be able to expand your current selection by proximity to the root points of the currently selected curve(s). That way you could easily select curves that grow close to the current selection.
Another old issue is the uneven distribution of child hairs, but I think that will be solved with the new poisson disk algorithm.
One issue that can arise is when a user cuts hair so short that it is almost 0 units in length, which then makes it really hard to select and delete. Having hairs with close to zero length will make the child hairs really short as well and it becomes hard to find short curves and to get rid of them. I think a pruning operator would be nice. Something like “delete all curves with length below X”
5 Years ago I wrote an old groom brush suggestion on right click select. That implementation of a groom brush has not yet been implemented in any other grooming software (as far as I know). The whole idea is to not “sculpt” all hairs under the brush, but rather grab the hairs close to the brush at the initial brush position of the stroke and groom those.That sort of behaviour would make it easier to create overlap in hairstyles.
docs.google.com
blender fur/hair development suggestions
Blender fur/hair development suggestions  The intention of this document is to present some ideas regarding hair for the blender developers. If you need further clarification regarding my proposals, please let me know and I’ll try to clarify. I’m...

---

### Post #9 — EvertonSchneider — 2022-05-03T03:07:21.329Z

Hi, Dalai! Greetings from Brazil!
I’m with you on all your points and the comments here. I’m also not sure about how dynamically changing the resolution is useful… Waiting to hear a grooming case that can benefit from it.
In the current hair system, one thing I noticed is that weights manually set were not respected when re-keying(which I think is some kind of re-sample) the strands, so it would be nice if we can resample but keep attributes like weights or others…
dfelinto:
An operator to resample the (selected) hair strands to a target number of “control points” or “control points/meter” (similar to how voxel remesh works for mesh sculpting).
With this are you meaning that we could re-sample hair guides based on their lengths or the distances of the points? For example, the longer ones will receive more points clamped by the total given value and the shorten ones will receive fewer points since the distance between points will determine how many point will fit the short length? This would be very nice!
Off topic:
About Daniel’s words, grooming in blender is already really nice. I’m not familiar with other tools, never used them, but I watched tutorials and workshops on other grooming software.
One particular thing that I liked most in the current hair implementation is to be able to directly select the points of the hair guides and edit them like anything else, with G to grab, S to scale end R to rotate… and it seems that the guides adapt dynamically to the transformations maintaining the length and root position (while having the option to keep the root position or not)… It even works with proportional editing(unfortunately the only connected doesn’t work)…
so precise to positioning specific hair guides, It’s really powerful and consistent with the rest of blender.

---

### Post #10 — ikakupa — 2022-05-03T07:01:08.723Z

DanielBystedt:
It would also be very cool to be able to expand your current selection by proximity to the root points of the currently selected curve(s).
This would be very useful indeed.
To add to that, something that always comes to mind is Strand Sets (or Hair Sets). Similar to Face Sets in sculp mode. They would allow for easy selection even when working with densely placed strands. They could be Randomly colored to visualize all of the different parts of the groom. Swift hiding and un-hiding by hovering over Strand Set. This would speed up overall process in my opinion.
Again, sorry for drifting away from the main topic.

---

### Post #11 — dfelinto — 2022-05-11T08:43:49.737Z

Thanks for all the replies by the way. It helps to know that dynamically changing the control points is not the most pressing issue at the moment.

---

### Post #12 — DamienMonteillard — 2022-08-24T12:11:29.502Z

Hi,
I recently tested the new hair system with curves on blender 3.3.0 beta. I really like the new tools (density, pinch, smooth)
I’m writing here today because I’d like to improve the hair of the character I’ve modeled.
screenshot_character
1920×1080 465 KB
What is blocking me at the moment is that I can’t change the number of points on some hair strands.
Is it possible to add points after creating the hair strand ? Like a w > subdivide.
I feel stuck in the construction of the hair with the default 8 points proposed when creating the hair.
Maybe I didn’t see the option to add extra points.
See this screenshot below
screenshot_character_optimisation
1553×871 309 KB
Another remark it would be interesting to be able to see the points when you brush the hair.
I also notice a kind of bug when I use the slide tool with an object with armature. Hope I can recreate the bug on a simple scene.
Thanks to all the developers for working on this new hair improvement.
If you want my 3D model for testing I can send it to you.

---

### Post #13 — DamienMonteillard — 2022-09-03T09:42:47.328Z

In the future do you consider an improvement on the subject of adding points on a curve hair with w > subdivide ? Or should I be forced to delete the hair strands that don’t have the right number of points (8points) to redo them with 12 or 16 points.

---

### Post #14 — dfelinto — 2022-09-07T13:52:13.071Z

In the future yes the edit mode should support subdivide.
At the moment you can use Geometry Nodes to change that, but it is all or nothing (as in, it works on all hairs, and has no access to the selection).

---

### Post #15 — DamienMonteillard — 2022-09-09T20:26:52.557Z

Thank you for your answer.
This is great news. I can’t wait to test it in a future version.

---

### Post #16 — JuanGea — 2022-09-10T09:54:02.669Z

I’ve been testing the new hair system under a different perspective, to generate assets like towels or rugs, it works very well, however I’ve found that I cannot create haird from GN, I could create a curve and scatter it as an instance, but that’s not the same as creating the hairs on a surface, also if I create the curves that way I cannot make the curves move with the surface because the node responsible of that attachment says that the curves has no UV attached to them.
Am I doing something wrong?
If not, will the be available in the future? to generate hairs procedurally from GN and attache them to UV points.
Another problem I saw is that I cannot move full hairs from within GN, I can move points, but I cannot transform a full hair, if I use duplicate elements than I can somewhat do so, but it’s still not fully working because if I use a noise in hairs with ID 1 then I don’t get origin of those points distorted by the noise, but all their points distorted, so basically I cannot move an element by things like “Spline” for example.
Once again, am I doing something wrong?
If not, will this be supported in the future?
As always we tend to mention things we don’t like or that we miss here, but I have to say that the new Hair system is amazing, very efficient rendering wise, that is something that has always been a problem with hair and now since we can natively render curves, it’s very efficient, and the same goes for viewport / editing, pretty amazing job.
Congrats team
EDIT: I just realized this was for Hair Edit Resolution and Control Points, sorry for that, not sure where to put this feedback,
@dfelinto
move it whereever you think it should go, or tell me where to post it and we can delete this post if you think so.

---

### Post #17 — fland — 2022-09-10T14:02:45.350Z

New hair system can’t animate

---