---
titulo: Interpolate Hair Curves and Subdivision Surfaces
autor: animas3D
url: https://blenderartists.org/t/interpolate-hair-curves-and-subdivision-surfaces/1621672
data: 2025-12-02
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — animas3D — 2025-12-02T23:56:43.723Z

Hi there. I would love to get some more information or an update about the geonode hair curve system.
No question it is very powerful, but it has already been around two years of waiting and still no word about why the Interpolate Hair Curves modifier does not work in conjunction with the Subdivision Surfaces Modifier.
That is to say if you have a low poly mesh and add a subdivision surface modifier to it to smooth it out to create more subdivided polygons on the fly, if you add curve hairs to it and then use the Interpolate Hair Curves modifier to add more hairs, the new interpolated hairs ignore the subdivided surfaces and only take into account the low poly mesh, thus intersecting the mesh where the subdivision surfaces are.
In the legacy particle hair system, applying hair to a subdivided mesh and adding children hairs result in the child hairs precisely sticking on the surface of the subdivided mesh exactly as they should. This causes me to wonder why this seemingly simple fix could not be added in days. I mean, why not just feed the subdivision surface to the interpolate hair curves modifier instead of the low poly cage like the particle hair does?
Using subdivision surfaces is very important for animated and while Curve Hair is promising, it is basically rendered useless by not having it work with subdivision surfaces!
I know there are other things on the list for curve hair, such as physics, but this is actually more important than that. Sure it would be nice if hair reacted to physics, but sometimes hair doesn’t. This is much more of a priority and should be at the top of the list. It also seems like it wouldn’t be that hard to implement.
Does anyone have any information about this. It would be most appreciated. Thank you!

---

### Post #2 — thoslos — 2025-12-03T05:15:18.606Z

I think the issue is after you subdivide the mesh and change its shape, the guide hairs - which you’ve carefully sculpted - have to be somehow remapped to the new shape in a way that won’t mess them up.  I can imagine some sort of mesh-cage-like deformation to remap them, but…it sounds like it would lead to frustration as you tried to sculpt the hair in a way that would look good at different subsurf levels without requiring adjustments.  That sounds doable, but what if you went into edit mode and extruded the mesh, or merged it with another mesh, or something like that?
The whole process sounds pretty hairy.  HAHAHAHAHAHA
But seriously, it does.

---

### Post #3 — MmAaXx — 2025-12-03T06:56:18.927Z

In the -Interpolate Hair Curves- modifier try to turn off -Surface Rest Position - in this way the new hair should follow the subdivided mesh.

---

### Post #4 — animas3D — 2025-12-03T18:43:40.027Z

Thanks for the suggestion. The issue here is that the interpolated guide hairs need to follow the subdvision surface not the low poly. It’s really kind of simple and straightforward and probably could be fixed in a day because it works on the legacy particle hair perfectly. Does anyone know how to get the message through?

---

### Post #5 — animas3D — 2025-12-03T19:16:36.253Z

A few months ago I tried all kinds of things. I would be willing to try it again if I knew it had been fixed, but I spent so much time trying to get it to work that I would rather learn that it has been addressed before diving back in. By the way, I am not the only one that has brought this up. See this post:
Interpolated hair curves clipping into mesh with unapplied subdivision modifier
Technical Support
Recently discovered something that ruins geonode hair for fur on animated characters, if a mesh has an unapplied subdivision modifier, interpolated hairs created by interpolate hair curves will clip into the mesh. This issue will disappear once the subdivision modifier is applied (unideal solution due to the fact that subdivided meshes are a PITA to modify) 
From my understanding, this seems to just straight up be a technical issue/flaw with how the rest_pos attribute works and thus isn’t fixabl…

---

### Post #6 — thoslos — 2025-12-03T22:04:30.560Z

Guide curves stay where they are placed on the base mesh, but the interpolated hairs conform to the faces and normals of the subsurfed mesh.  It can look just fine, but it’s really awkward to sculpt the hair because the guide curves aren’t where they’re supposed to be.
Obviously this is much more of an issue if subsurf significantly alters the shape.  With a cube, for example, you’re sculpting curves that are stuck to planes way up in the air and watching the effect be applied to a ball of hair.
Edit:  At least, this is how it works in v3.6.

---

### Post #7 — Ducktor_Cid — 2025-12-03T23:42:48.321Z

Unfortunately there just doesn’t seem to be a known solution. This exact issue is lumped under the exhaustive list of remaining issues with hair curves which has had one item checked off in the year it has existed and it wasn’t even technically related to hair curves.
https://projects.blender.org/blender/blender/issues/125700
tl;dr: probably just stick to legacy particle system if you need to have a working hair system for fur in order to complete work

---

### Post #8 — animas3D — 2025-12-04T17:00:31.966Z

Thanks, that is what I am realizing is what I will have to do until it is fixed (rely on particle hair).
Honestly, the curve hair system would be usable, even without the other items on the “exhaustive list” if it just recognized the subdivision surfaces. I don’t even care much about physics or dynamics, although one day it would be nice. having it follow subdivision surfaces is, however, extremely crucial.
And the thing is that it seems to me that it just wouldn’t be that hard to accomplish, especially since the legacy particle system doesn’t seem to have a problem with it.
I just don’t see the problem with feeding the Interpolate Hair Curves Modifier the surface after it has been subdivided instead of before it has been subdivided. Why is that so hard?
Thank you again for your reply. If you hear anything else about this, would you please let me know and vice versa.
Cheers,
Joe.

---

### Post #9 — SchnuuuPu — 2025-12-07T20:03:10.202Z

Hello there,
i had also problems after adding hair to a rigged body. On animating, a lot of hair didnt move or would be out of place from the mesh entirely.
On the Curves Hair Object , the Modifier Surface Deform also gives me the error “Invalid surface UVs on 1081 curves”
In the end i could get it fixed after changing the UV Smooth Option within the Subdivision Surface Modifier of the Mesh, changing it to keep boundaries, reduces the behavior (“Invalid Surface UVs on 5 curves)”, and setting it to None, seems to have fixed the error and the hair problem completely.
Yes for the cost of non smoothed UVs, but i have to find out how this really affect my render ^^.
Have you already tried this setting?
Edit: I just have seen that they also mention this in the remaining issues list posted by Ducktor_Cid as “UV smoothing under Subdivision creating discrepancy/invalid curves”.

---

### Post #10 — Ducktor_Cid — 2026-07-16T20:25:58.384Z

Good news! It seems this issue has
finally
been fixed in 5.2 LTS! The new Hair Dynamics node has a ‘animation’ mode which appears to be a replacement for Deform Curves On Surface. Here, I’ve setup a simple geometry node group to switch between the two on the test file I originally uploaded to the issue on the blender repository and it does infact fix the issue.
All you need to do is replace Deform Curves on Surface with Hair Dynamics and set Hair Dynamics to Animation. Here’s the minimum needed:
image
800×245 15.2 KB

---

### Post #11 — animas3D — 2026-07-23T20:58:06.020Z

HALLELUJAH! I have been waiting for this for a long time. Can’t wait to give it a try! Thank you so much for replying and letting us know. This made my day.
Cheers!
C

---

### Post #12 — Ducktor_Cid — 2026-08-02T23:13:29.702Z

I forgot to mention you also need a Capture Rest Pose nodegroup at the bottom of your surface mesh’s modifier stack. Easiest way to get it is by selecting your surface mesh and adding a new hair curves fur object (shift + A → Curve → Fur), this should automatically add the Capture Rest Pose nodegroup to the selected surface mesh. You can safely delete the newly created fur object.

---