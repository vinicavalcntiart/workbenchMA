---
titulo: Case Uses for clumping and interpolation
autor: Gareth-Jensen
url: https://devtalk.blender.org/t/case-uses-for-clumping-and-interpolation/24686
data: 2022-06-10
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — Gareth-Jensen — 2022-06-10T18:50:14.583Z

In last weeks meeting Dalai asked for a visual explanation of how we would like to use clumping and interpolation nodes. Below is a mockup showing a very basic demo of using a guided clump/interp chain. This workflow allows us to achieve organic clumping and subclumping while using the least amount of sculpted curves possible. In my experience this is the best way to make photorealistic grooms, often simply adding some noise will still look procedurally generated. The only way to remove the “CG curse” is to have a layered system where you can control each step of guiding/interp and clumping to control a high hair count. Hopefully this demonstrates that to some degree

---

### Post #2 — Gareth-Jensen — 2022-06-10T18:50:57.451Z

clumpInterpMockupNodes
1790×991 156 KB

---

### Post #3 — RiccardoBancone — 2022-06-11T07:27:04.980Z

This would be great, I can confirm that I missed more granular control for clumping in the current system. I had pretty much the same Idea in my mind.
A system like this would boost the ease of creating photoreal hair.
A bit off-topic maybe, but it would great of one could choose where to put the simulation solver in the tree, while the interpolation stays “consistent” during the animation/simulation.
For example, If choose to simulate just the level 1 curves, it would be great if the interpolarion algorithm can create new hair that follow the simulated/animated deformations  in a continuous way, without popping effects between frames. I don’t know if it makes sense or if it’s even possible.

---

### Post #4 — Gareth-Jensen — 2022-06-13T16:20:22.554Z

Thanks for the support! I feel like the the idea of Virtual Parents was supposed to cover this, but they unfortunately lacked any control whatsoever and so they only way to gain control back was to turn them off and use a ridiculous number of sculpted parents.

---

### Post #5 — brecht — 2022-06-13T16:54:57.108Z

For physics simulation, what some other systems are doing is finding a representative subset of hairs on the full hair, and then binding nearby hairs to them. This can be done automatically and/or manually.
I think it’s probably best to decouple the physics simulation from the hair generation like that. It may be that the hair at some point in the node graph works well for physics simulation, but it’s not a given, especially as you get more complicated node graphs.
The algorithms to find and bind representative hairs will be challenging. But it’s more flexible if at the physics simulation stage you can decide where you need more or less detail, without having to makes changes in the node graph and unintentionally affect the look of the hair. And it could work when the hair is not procedurally generated at all, but maybe imported from another application or scan.

---

### Post #6 — Gareth-Jensen — 2022-06-13T17:05:20.184Z

Historically I believe we’ve simulated a lower number of curves and then do a final interpolation before rendertime. I’m not familiar with doing it they way you are talking about, sounds super interesting though. Especially being able to apply it to external data.

---

### Post #7 — Xeofrios — 2022-06-14T09:41:13.199Z

Over on Blenderartists we have been exploring creating hair using geometry nodes. It allows the more granular control you want. Maybe it can provide some inspiration.
https://blenderartists.org/t/hairs-geometry-nodes/
This the latest blend file in the experiment (by me)
https://blenderartists.org/uploads/short-url/3yFBc8dr1NFk1jZH1oyoQbXW8fj.blend

---

### Post #8 — Gareth-Jensen — 2022-06-14T17:47:30.771Z

I have been following this project keenly, it is very inspiring!

---

### Post #9 — BertVandenBosch — 2022-07-27T12:44:32.047Z

Within this specific example, how would one curl or modify an entire ‘clump’ of hairs? Shouldn’t there be a way to apply fields operations over entire clumps instead of just single curves?

---

### Post #10 — And-Woo — 2022-07-27T15:11:16.416Z

Wouldn’t it be better to have more control on the profile of the interpolated hair?
CLUMPS_1
1774×1485 300 KB
CLUMPS_2
1774×1485 280 KB
CLUMPS_3
1774×1485 274 KB
Basically
CLUMPS_4
858×995 84.8 KB

---