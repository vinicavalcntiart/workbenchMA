---
titulo: Blender 3.5 Hair system question
autor: Filnisius
url: https://blenderartists.org/t/blender-3-5-hair-system-question/1460445
data: 2023-04-16
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — Filnisius — 2023-04-16T18:29:31.612Z

I’ve been trying to use this new system to create fur for a few animal character’s and I don’t think this is it.
It’s extremely sluggish to comb the hair on the characters even with my beefy system( 4080 RTX and 64GB RAM).
So, I assume this just works for human characters right? Is there a way to utilize some of it’s features with the older particle system?

---

### Post #2 — zeauro — 2023-04-16T18:58:40.790Z

No. New system is supposed to be as useful for animal fur than for human hair.
With old system, you would use several particle systems with interpolated children.
With new system, you have to use several Curves Object, with additional curves interpolated with geometry nodes modifier.
So, if you try to edit all hair curves rendered as a whole, at same time, you would have problem whatever system you are using.
It is possible to convert curves from a Curves object to older particle system : in Sculpt mode, Curves menu > Convert to Particle System.
But Particle Edit mode will not be faster than Hair Curves Sculpt mode
If you have too many guides to edit, you should suffer as much with old system.
Try to have less guides, and interpolate more of them using Interpolate Hair Curves nodegroup.

---

### Post #3 — Filnisius — 2023-04-16T20:17:26.753Z

That is wrong. Old Particle system causes me no lag whatsoever.
As soon as I had a Curve Object, it lags right from the start.

---

### Post #4 — zeauro — 2023-04-16T20:59:20.089Z

What I mean is that you have to compare what is equivalent.
Defaults are not the same for old particle system and Curves object.
In case of old particle system, default amount of particle is 1000 without interpolated children.
For a Curves Object added using Quick Fur operator, amount of hair guides can be an hundred or a thousand or tenth of thousands. And interpolated guides will be more or less numerous.
That will depend on size of model and setting of Density (low, medium or high).
If you add an Empty Hair primitive, you should not experience a lag. No hair guide is created.
If you do, you should report it as a bug.
But on a Curves Object created by Quick Fur operator, disabling modifiers creating interpolation should stop the lag. Reducing density settings in them, should help.

---

### Post #5 — Filnisius — 2023-04-16T21:16:33.783Z

Yes, on the empty there is no lag. But when I start adding guides everything slows down. The hair keeps clipping through the mesh. And when I turn the “Use Sculpt Collision” option, nothing works. Brushes no longer work and do anything. And how can I add interpolated children like in the old particle system?
How is anyone suppose to work with this?

---

### Post #6 — Matakani — 2023-04-16T23:21:03.067Z

Hi. Have you watched this yet?

---

### Post #7 — Filnisius — 2023-04-16T23:43:27.993Z

I did. And it worked great on a simple, flat plane. Once you try and add it to an actual character, it just isn’t feasible. Not a human character where you can just work on a simple scalp mesh. No. I mean on a horse and Cheeta model. Trying to comb is frustrating. The brushes freeze up when you enable sculpt collission, forcing you to comb without it which means the fur will clip through the mesh.
And then filling the mesh with child hairs doesn’t work the same way because of how they are calculated. I needed 3.5 million children to cover the horse in fur which is extremely wasteful use of resources. The old system only requires 1.6 million hairs in total to achieve similar results.
I think this procedural approach is great for Humans, but for animals is extremely inefficient. Until I see someone actually do it to a animal or creature character with good results, this is what I believe.

---

### Post #8 — thetony20 — 2023-04-17T09:30:11.900Z

Have you tried using a lot less actual hairs, as in just placing and sculpting main guide hairs for placement, length and direction change and then use the interpolate node to fill it all in for actual rendering.
You may also have to do the fur in sections, as in add more then one empty hair object, so you can turn off various areas. Like one hair object for the head, another for the tail, etc.

---

### Post #9 — Filnisius — 2023-04-17T09:51:14.499Z

Yes, I’ve tried. It’s frustrating to comb because the guides clip trough the mesh, and if I turn the collision on, the brushes don’t do anything.

---

### Post #10 — Matakani — 2023-04-17T10:46:33.120Z

Have you watched Johnny Matthews new tutorial?
Mixing 2 Hair Styles
Sorry to just drop videos. I am not touching the new hair system for a month or two more - when it more finalised…
Still watching any videos of those I am subbed to, and this new video seems to have useful info for you.

---

### Post #11 — zeauro — 2023-04-17T11:29:28.101Z

Filnisius:
I needed 3.5 million children to cover the horse in fur which is extremely wasteful use of resources. The old system only requires 1.6 million hairs in total to achieve similar results.
Indeed, for so much hair, I have to set View Amount to zero, in Interpolate Hair Curves modifier, to be able to comb several dozen of thousands of guides in sculpt mode.
Disabling modifier in edit mode does not work for that sculpt mode.
So, each brush stroke has to deal with an attempt of interpolation that is freezing viewport.
What I think could explain to use twice more hair for new system is that defaults for Strand Shape are different, in Set Hair Curve profile modifier, automatically added to a Fur object.
Without that modifier, Hair Guides have same radius, the only difference will be the length.
Longer hair are covering more surface. So, they don’t need to be as numerous.

---

### Post #12 — Jvry — 2023-04-17T19:59:39.664Z

Filnisius:
I think this procedural approach is great for Humans, but for animals is extremely inefficient. Until I see someone actually do it to a animal or creature character with good results, this is what I believe.
Well, there’s at least one person here who has managed a furry critter. I appreciate a cuddly toy might not be what you’re going for, but I’d still call it a proof of concept. Maybe some of his comments in that thread can help you?
Testing out the new Hair Node Group Assets with a Teddy Bear
Finished Projects
[teddy_bear_render_3]
Wanted to test out the new node group assets for myself! I found the animal fur samples really helpful for understanding how to get the best out of the system.

---

### Post #13 — spiotrx — 2023-04-24T21:54:37.661Z

This! I still didn’t switch from Hair Particles to Hair Curves because of no deflect emmiter, and when I learned it’s here, it doesn’t work
It doesn’t matter what I try, it only works sometimes when I comb for some reason… I watched tutorials, but didn’t find a solution yet.
A workaround though, you can use the shrinkwrap for hair curves which works well so far.
Also true for the performance. I’ve noticed with geometry nodes that compared to particle system, it takes much, much more resources for hair curves, or vegetation spawns. I had to get a beefy vram gpu to render anything with it. I think the next BIG thing for blender should be optimizing stuff like big scenes performance and such, unless they’re sticking to low poly, or individual meshes, but even sculpting with multi-resolution is tough compared to ZBrush.

---