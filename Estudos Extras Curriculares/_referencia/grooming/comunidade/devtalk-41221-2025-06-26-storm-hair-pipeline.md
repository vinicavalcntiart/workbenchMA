---
titulo: 2025-06-26 - Storm Hair Pipeline
autor: dfelinto
url: https://devtalk.blender.org/t/2025-06-26-storm-hair-pipeline/41221
data: 2025-06-26
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — dfelinto — 2025-06-26T14:05:00.451Z

Attendees:
Dalai Felinto
Simon Thommes
Meeting to go over the hair-related development requirements of the upcoming
Project Storm
by the
Blender Studio
.
Related links:
New curves object type
#68981
Replace legacy curve code with new system
#105253
Remaining issues with hair curves
#125700
Realistic requirements
The studio team will find workarounds in regards to tooling. So the focus here are on things that would be could impact the final result.
Additionally we listed low hanging fruits that the community (or the core team) could use the momentum to work on.
Must have:
Edit mode hiding.
Hair solver
Node group/modifier.
[nice to have] Backward-solving initial rest pose.
Lists + Sample Nearest.
Tangent Interpolation (finish
PR
).
UV smoothing under Subdivision creating discrepancy/invalid curves.
Stable hair root tangents are needed for simulation
[not needed for Storm].
Good to have:
Rest position attribute yielding inaccuracy with Subdivision (
#107856
).
Move “strand/strip” display option to curves data-block.
Good community tasks:
Tool to resample curve.
Pen tool.
Merge by distance to support Group ID.
[may be too hard] Sample Nearest Curve.
To design (from
#125700
) in the upcoming workshop mid-July:
Surface geometry fallback.
Default UVmap fallback.
Presets/operators to manage operation order and modifier settings for correct deformation [
closures?
]
Ideal scenario
In the ideal scenario, a production like this should be able to have a (armature controlled) guide-hair pipeline:
Bones → Guiding Hair → Children Hair
Those targets are not realistic for the project timeline. But the project assets can be used in the future to proof this workflow.
Most of known TODOs
New curves object type
#68981
.
Replace legacy curve code with new system
#105253
.
Remaining issues with hair curves
#125700
.
Skeletal deformation for hair
Armature modifier.
Weight painting.
Guide deformation (native feature)
Lists.
Built-in nodegroup/modifier.
Tooling to assign guide curves.
Weight per children curve.
Simulation
Built-in node-group hair dynamics modifier.
Attribute painting to feed the solver.
Backward-solving initial rest pose.

---

### Post #2 — TheLittleMouse — 2025-06-30T02:11:07.692Z

Are there any plans to make hair objects reusable? Like transferring a hair object from one character to another? Right now, each hair object is very much tied to the mesh it is sculpted on

---

### Post #3 — JulianPerez — 2025-06-30T14:58:04.575Z

Will it be possible to add hair curves to meshes without UVs?
With the old hair particle system it is very useful and easy to add hair particles on triangulated meshes, for still renders or for creating grass on a terrain, for example; just setup vertex groups for density, lenght, etc and that’s it, no need to create UVs just for that.

---

### Post #4 — DarkKnight — 2025-06-30T15:21:44.239Z

From what i know a uv map is needed for the new system. That said a simple remesh with auto uv layout should be as simple and fast as the old one was. The only downside is that you need to go into edit mode with the high res mesh.

---

### Post #5 — JulianPerez — 2025-06-30T17:28:52.316Z

DarkKnight:
That said a simple remesh with auto uv layout should be as simple and fast as the old one was
It’s an extra step that wasn’t needed before, so no, it’s not as simple and fast as the old one

---

### Post #6 — sentharn — 2025-07-01T19:55:19.456Z

I know these issues are tracked in various bug reports, but I wanted to make sure they’re on peoples’ minds as IMO they are important blockers to being able to use geonodes hair.
#1
blocker for me is shared per-scene strand resolution.
125700
mentions per-system resolution (actually to be implemented in #
96455
) and the lack of this is
the
blocker for me transitioning to geonodes hair.
If I have a scene with both grass, fur, or other things that need lots of low-res strands, plus objects with long detailed hair, they both share the same scene-wide resolution (currently hardcoded at 3 steps in the source code with a comment saying “TODO don’t hardcode this”). You can increase it but it affects all systems in the scene. I have to choose between prohibitively long render times to make the long hair look good, or else the scene will render fast but the hair will be insufficiently subdivided.
The old particle system has the ability to set per-system resolution. Again, yes, I know this is in the bug report, but it’s extremely important for many workflows so I wanted to make sure it gets attention. It sounded like there was no roadmap for it last time I chatted with the devs so I’m hoping this changes.
#2
blocker is physics, which I’m happy to see is getting attention!
#3
blocker is my pet issue
Cycles strand normals preventing many stylized/smooth/blended normal effects
on hair, like making stylized grass/fur that inherits the surface normal, akin to the old “surface diffuse” feature in the blender 2.x era. Yes, you can convert to mesh, but it’s memory prohibitive. I don’t have a lot of hope for this one being fixed but I would be remiss not to mention it as it is important to me. If it is important to you as well I hope
you’ll consider upvoting the RCS feature request for it
.

---