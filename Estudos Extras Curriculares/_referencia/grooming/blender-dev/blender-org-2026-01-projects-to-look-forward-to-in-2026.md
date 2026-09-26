---
titulo: Projects to Look Forward to in 2026
autor: Dalai Felinto
url: https://www.blender.org/development/projects-to-look-forward-to-in-2026/
data: 2026-01-30
idioma: en
coletado_em: 2026-09-26
---

Projects to Look Forward to in 2026
January 30th, 2026
Development
,
News
Dalai Felinto
It is that time of year again. You may be enjoying a scorching hot summer, the serenity of snow, or something in between. For those of you staying inside, buckle up. There is a lot to look forward to!
2025 Releases
Before we start with the fresh new targets, let’s take a moment and admire what was put out into the world last year. With no surprises, the release schedule went
as planned
with three annual major releases.
Blender 4.4
March 18th, 2025
Blender 4.4 splash artwork Flow©
Dream Well Studio, Sacrebleu Productions, Take Five
Image licensed under CC-BY-SA –
flow.movie
Animation slots.
Compositor CPU rewrite.
Grease Pencil v3 feature parity.
Video Sequencer text editing improvements.
Over 700 issues addressed.
Blender 4.5 LTS
July 15th, 2025
Blender 4.5 LTS splash artwork “DOGWALK” by
Blender Studio
.
Full Vulkan support.
Faster startup and EEVEE shader compilation.
Grease Pencil compositor pass.
Enhancements to the animation timeline.
Importing multiple formats in Geometry Nodes.
UV visibility in all modes.
Faster Video Sequencer with HDR support.
Compositor procedural nodes.
Nearly 400 bugs fixed.
Blender 5.0
November 18th, 2025
Blender 5.0 splash artwork by
Juan Hernández
ACES pipeline.
Improved HDR capabilities.
UV Sync.
New volumes and SDF nodes in Geometry Nodes.
Storyboarding template and workflow (scene sync).
New modifiers, such as Array and Scatter on Surface.
Compositor creative effects assets.
Animation and rigging improvements.
VR scene inspection, vignetting, and snap turns.
Nearly 600 bugs fixed.
The result was a combination of new features, stability, performance enhancements, planned project and long-standing issues.
In addition, 2025 saw 20
LTS
releases across Blender 3.6 LTS, 4.2 LTS, and 4.5 LTS.
Looking Back
If you compare what was released with
last year’s projects announcements
, you may notice that some features weren’t even announced.
On the one hand, this is good news. It reflects the dynamic nature of Blender development, with modules working closely with community developers and artists who can steer the project in unexpected ways. These contributions often lead to the discovery of new talent who could eventually become full-time developers. So, the more, the merrier.
On the other hand, not all of the announced projects were completed and released. The reasons are plenty: overly optimistic (and ambitious) targets, over-scoping, unclear designs or scope, missed deadlines, limited resources, shifting priorities, my-dog-ate-my-homework, you name it. There is no sugarcoating it. There is room for improvement, and we aim to do even better this year.
That said, it is in the spirit of the Blender project to propose targets that serve as a beacon, helping focus the community’s efforts toward common goals. So, without further ado, let’s unveil what the team has planned, aim for the stars, and see where we land.
Looking Ahead
The proposed projects for this year are organized into the following areas:
Storytelling
World Building and Asset Creation
Animation
Lighting, Rendering and Compositing
Collaboration
Interactivity
Platforms
Blender Lab
Storytelling
As a follow-up to Story Tools and Compositor node-modifiers, expect more
video sequencer improvements
– GPU support, sequencer effects, media bins, ripple and three points editing.
Story Tools early Mockup.
World Building and Asset Creation
Improved texture workflow with
3D brush
, and the beginning of
layered textures
.
The latter is not straightforward. Its
original design dates back to 2022
, and it was held back until it could receive proper attention. While it won’t land in Blender this year, features like a revamped baking workflow are on the horizon.
On the rendering side, this is the year NPR will shine brighter.
Non-Photorealistic Rendering
was prototyped and iterated over in 2024-2025, and it is now ready for development.
Animation
After a hiatus,
animation layers
are back on the menu. The initial goal is to expose this functionality in the Action Editor, building on existing features. The design is being finalized and work is expected to start during Q2.
Lighting, Rendering and Compositing
The Cycles
texture cache
is in its final stages of development, and will make rendering with many high resolution textures much more efficient. This has been a long requested feature. This will be followed by new principled features and a new OpenPBR node.
Also worth mentioning is a new approach for
Scene Layered Compositing
. Imagine a stack of effects similar to the new Compositor modifier in the Video Sequencer Editor. It’s so similar, in fact, that an effect designed for the sequencer will also work for the scene.
There are still nodes under the hood, but artists shouldn’t need to deal with them (only if they want to). This is similar to how the new
Geometry Nodes Array
modifier lets artists focus on the big picture of the intended “effect”, while others can dive into the nodes for extra flexibility and power. To each their own – and to everyone, Blender! :)
Collaboration
Online assets
will arrive in Blender in the first half of the year. Opening the door to natively extending Blender with materials, collections, and more from the internet. The Blender Foundation will host a small library of assets on the extensions platform, and third-party platforms can adopt a similar solution.
Project Setup
reached its initial milestone in 2025 with variables and
path templates
. Next up is a dedicated project editor and shared project settings, like assets, add-ons, and project-specific variables.
Finally, overrides will be revisited based
on the late-2024 design
. A new system, nicknamed
dynamic override
, will allow for more flexible runtime-defined tweaks. This may also better accommodate simpler single-character rigs, providing an experience similar to the old (pre-2.80 old!) proxy system.
Overrides mockup, the final user interface will change.
Virtual Reality
Location scouting
began
last year but was put on hold to focus on wrapping up VR locomotion improvements. The latter will arrive in Blender 5.1 and are already familiar to all
brave early-adopters
.
Location scouting itself was demoed as a prototype at the Blender Conference 2025 and is expected in the first half of this year.
Location Scouting mockup.
Meanwhile,
Vulkan and OpenXR
interoperability
will start
in parallel, bringing the XR experience up to par with Blender’s other graphics improvements.
Interactivity
Hair dynamics
development
continues to make progress, building on the work already highlighted as a target last year. While
Closures
and
Bundles
may only be experienced firsthand by technical artists, asset integration features like packing and improvements to the modifier UI enabled the new built-in modifiers in Blender 5.0.
There’s still a long way to go before replacing the legacy particle system, but a new hair solver with a
user-friendly interface
will be a important step in that direction.
Speaking of nodes,
Modal Node Tools
will expand the
Node-Based Tools
to support
modal operations
. With an evolving design over the years (
2023
,
2024
,
2025
), it’s now ready to move from prototype into development. This will also lay groundwork for an interactive mode for Geometry Nodes simulations.
Platforms
The initial port to
Android
devices, including touch support, will start. This is but the first mobile platform that is targetted for release. Others should follow in the future.
The initial focus is on tablets, but the same technology will allow Blender to run natively on XR devices. Overall, usability improvements should benefit both on-the-go artists and those already using regular display (or even non-display) tablets.
Blender Lab
To launch the
Blender Lab
initiative, the development team will explore natural language input in Blender. The experiment aims to develop an
MCP server
for Blender, with communication handled via the existing Python API.
Model Context Protocol (MCP) is an open-source standard that enables LLMs to connect with external data, tools, and systems.
On-going Projects
There is always maintenance and ongoing development in the modules. Here are a few areas being worked on:
EEVEE
feature parity (with pre-EEVEE-next releases) such as
better planar reflection
. As well as raytracing pipeline improvements and shader compilation optimizations.
After recent
Grease Pencil
developments to
improve curve types support and adding more rendering options
, the focus now is on updating the workflow for
creating fills
and adding support for holes.
After the initial
Cycles
projects have been completed, the plan is to work on either improved light transport or handling of complex scenes. Improvements to the external render engine API are also being investigated.
And more:
Multiresolution spike fixes
.
Collection import
.
Flamenco
and
BAT
(Blender Asset Tracer) improvements.
Exploring editor tabs and docked editors.
Other module work.
Releases
The planned releases for 2026 and their initial dates are:
Blender 5.1 (March)
Blender 5.2
LTS
(July)
Blender 5.3 (November)
On top of this, LTS release updates are expected throughout the year:
Blender 4.2 LTS – until July 2026
Blender 4.5 LTS – until July 2027
Blender 5.2 LTS – until July 2028
Make this Possible
All of this progress is made possible
thanks to the donations
and the ongoing involvement and contributions of the community.
Support the Future of Blender
Donate to the
Development Fund
to support the Blender Foundation’s work on core development, maintenance, and new releases.
To follow new developments, keep an eye on the
Developers Blog
and join the discussions on the
DevTalk Forum
.
On behalf of the team, I hope everyone has a great 2026. Happy Blending!
Dalai Felinto
Head of Product, Blender