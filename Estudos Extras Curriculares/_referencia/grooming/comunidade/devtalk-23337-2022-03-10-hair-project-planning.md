---
titulo: 2022.03.10 - Hair Project Planning
autor: dfelinto
url: https://devtalk.blender.org/t/2022-03-10-hair-project-planning/23337
data: 2022-03-10
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — dfelinto — 2022-03-10T15:04:14.586Z

Hair Project Planning
Attendants: Dalai Felinto, Hans Goudey, Jacques Lucke
10 March, 2022
Status of the project:
Edit mode foundation.
Sculpt mode with some brushes as experimental.
Patch for geometry nodes integration.
Next steps for the first delivery in master:
☐ Basic Edit mode (curve) tools
☐ Icons for new brushes
☐ Delete
☐ Density
☐ Snake Hook
☐ Final implementation for
first batch of brushes
.
☐ User manual.
☐ Design on how hair deforms with the geometry (
T95776
).
☐ Final design for multiple hairs in a single object / edit geometry node.
After that:
☐ Definition of use cases/milestones
☐ Blog post (
draft
)
☐ Rendering hair for combing and EEVEE
☐ Geometry nodes support for Catmull Rom curves
What needs to be done before the next sprint planning:
☐ Check with Kevin the status of the edit mode, see if the work needs to be split with others. [Dalai]
☐ Investigate the status of rendering hair for combing and EEVEE [Dalai]
The next sprint planning will be on Monday 14th March, at 14:00 CEST in the next
Geometry Nodes
meeting.

---

### Post #2 — DarkKnight — 2022-03-10T15:24:18.981Z

Amazing. Just a quick question in which step are hair children planned? I guess it would be in After that: geometry nodes support?

---

### Post #3 — RonanDucluzeau — 2022-03-10T22:17:55.373Z

Yes. Interpolation of children is missing.
About, basic editing, Symmetry is not mentioned, too.
Current Hair Particle Edit mode has mirror operator and X-mirror option.
Selection is also used as mask for combing like in Grease Pencil sculpt mode.
There are options to preserve roots positions.
So, there is a need for masking.
There are also operators to Subdivide or Rekey particles into desired amount of segments.
A Subdivide operator is probably obvious for future edit mode.
But a need to harmonize points according to length for dynamics is less obvious.
Cut Particles to Shape tool and most of addons about Hair are about creating Hair from a mesh shape.
That is an intuitive and frequent workflow.
Maybe a mesh could be converted into an Hair Curves object

---

### Post #4 — dfelinto — 2022-03-11T15:30:32.052Z

Child hair will be implemented via nodes. And it will show up in the plan once we get the use cases nailed down.
Selection and symmetry are expected in the sculpting mode (though not blocking for the first tools to land in master).

---

### Post #5 — DimitriBastos — 2022-03-11T18:13:04.184Z

@dfelinto
Sorry if this was already properly answered, but how this new hair workflow relates to Geometry Nodes?

---

### Post #6 — HooglyBoogly — 2022-03-11T18:49:05.512Z

Basically the idea is that curves and hair are the same thing. Geometry nodes already has support for curves, and the new curves data structure makes it fast enough to support hair use cases with nodes.
So nodes will cover the more procedural aspects of the hair workflow, including existing nodes and potential new nodes. The goal is to develop these procedural systems in combination with destructive editing tools.
Does that answer your question?

---

### Post #7 — DimitriBastos — 2022-03-11T19:17:19.964Z

Absolutely yes. Thank you. I’m really looking foward to this.

---

### Post #8 — Erindale — 2022-03-11T23:48:51.823Z

Very excited about the non-hair applications of the hair tools! Architectual,spatial, and furniture design could definitely use this with all the node-based control we already have around curves

---

### Post #9 — erickblender — 2022-03-12T13:29:13.370Z

I m here just to say that whatever implementation of child distribution you will implement please don’t use the one in the master, the actual particle child distribution is really bad.

---

### Post #11 — Rincewind3D — 2022-03-14T19:48:06.607Z

Can we have also some shapekey like feature for the hair?
So we could save multiple hair styles and morph them into each other via those hair shapekeys.

---

### Post #12 — SomeAB — 2022-03-16T02:33:19.129Z

One of my suggestion is that similarly to how the Geometry Nodes project clearly benefited from consultation from some of the known faces in the blender community like Erindale (for example)…
For Hair related future goals, I humbly request the blender dev team to reach out to one of the best artist out there in terms of hairs/grooming: Nazar Noschenko and he uses Blender in his pipeline intensively (afaik)
https://www.artstation.com/nazarnoschenko
After that, having experimented with making hair in blender using old particles system approach as well as  curves method, one of the biggest thing on my wishlist is a quick-simulation/cache system … for baking hair movements, similar to cloth simulator. Speed (equivalent to other softwares on similar hardware) is the biggest issue with all three cornerstones that are due for overhaul in blender: Texturing, Sculpting and Simulation.

---