---
titulo: The Future of Hair Grooming
autor: Dalai Felinto
url: https://code.blender.org/2022/07/the-future-of-hair-grooming/
data: 2022-07-08
idioma: en
coletado_em: 2026-09-26
---

The Future of Hair Grooming
July 8th, 2022
General Development
Dalai Felinto
A new curves system, suitable for hair, is going to be part of the upcoming Blender 3.3 LTS.
This article covers the main design philosophy behind the new system, the initial deliverables and what is to be expected in the near future.
Curves Object
The new system is based on Curves objects. To start working with hairs you first need a (scalp) surface. This is the mesh that will be used for deformation and to add new curves on its surface.
With the surface object active, go to the
Add
menu and pick
Curve
→
Empty Hair
. This will create a new curves object and automatically set up a few things:
Set the active mesh object as the surface.
Parent the new Curves object to the surface.
Setup a
Deform Curves with Surface
node.
Add -> Curve menu
This should cover most of the cases when artists want to add a new Curves object for hair and start to add and comb its curves. For animations, the curves get automatically deformed if the surface is animated. If artists need a more complex setup, they can tweak the initial node group.
The Outliner is the place where artists can group multiple Curves objects, hide/unhide them, and have a basic layering system.
Outliner
This Curves object will eventually replace the old curve object (still used for the Bezier, Nurbs and Path curve primitives).
Spherical Brush
Back in 2020, during the discovery phase for the Geometry Nodes project, Blender Studio’s artist Andy Goralczyk was asked about the existing particle system, and what he was expecting the most. He shared his needs for set dressing tools. This was the
initial step
to the Geometry Nodes project, helping to pivot the particles project into what we have today.
Andy’s user story
Andy was also inquired about hair grooming, since the hair particle system was the way artists would often do set dressing. Besides commenting on the existing features, he raised a special concern about the existing brush. The brush allowed only for a projection mode, commonly known as a 2D brush. That leads to unnatural effects, and uncanny distortions in the hair comb.
This inspired the team to prioritize this in the new tools. The new 3D brush calculates a position in space based on the curves closer to the cursor, and from that point, it applies its effect as a sphere.
Different Workflows
There are two main workflows for digital hair creation: procedural and destructive. A destructive workflow is perfect for hero characters, while a procedural pipeline excels at throughput – you can replicate and tweak hairdos in a more scalable fashion.
The destructive pipeline focuses on tools that allow artists to manually bring their vision to fruition. Hair strand by hair strand if needed. For that we need tools such as comb, pinch, puff, shrink, slide.
The procedural workflow, on the other hand, creates and shapes the hair based on parameters, such as clumpiness, length, density, kink, roughness, twist.
Which system to pick? Why not a combination of both?
Destructive Workflow
There is an old adage in the industry that goes roughly like: “just paint”. If artists want to edit the hair, they should be able to pick a brush, pick a hair, and comb it the way they want.
The tools that allow this are the best friends of an art-director. Instead of spending time fiddling with knobs and abstract parameters, the tool gives them a direct way to manipulate their subjects.
This is the initial focus of the hair project. The system should be able to support at least 120,000 hair strands edited at the same time. Artists should be able to add and remove hair, and transform them in diverse ways. The initial tool set available is:
Add
Comb
Delete
Density
Grow/Shrink
Pinch
Puff
Slide
Smooth
Snake Hook
Besides those, there are a few selection tools available – from a
Selection Paint
brush to
different selection operators
. They allow users to work in a small part of the hair to have more control, as well as adding quick random variations.
The next planned tools are: Cut, Smooth Distribution, Smooth Length, Smooth Selection.
Project Heist file
used to test and develop the grooming tools.
Procedural Workflow
The Geometry Nodes project showed the potential of a procedural pipeline within the Blender workflow. Non-destructive modeling was possible before, but combining the existing modifiers with granular user controlled geometry nodes increased this exponentially.
The same benefits can be had for the new Curves objects. Given that the hair is just curves, and that curves are already supported in Geometry Nodes, this is possible from day one.
There is still a need for curves nodes focusing on hair use cases, like: children interpolation, hair parting, complex hairdos and non-straight hair types.
All the effects possible via the destructive tools should also be possible via nodes, allowing for a fully-procedural pipeline, or a mixed pipeline with guiding hairs enhanced with nodes.
At the moment generic curve effects are possible with the node system. The
Project Heist
is helping test this already to add messy hair: Objects using the same the curves data-block from the main hair object, but with a few Geometry Nodes modifiers on top to add extra randomness and more volume.
Procedural Destructive Tools
During the early stages of the hair development process, Andy was working with Simon Thommes to create a few “disposable” Geometry Nodes to add one-off effects to be applied as part of the destructive combing for
Project Heist
.
He would work with the existing tools, add a new Geometry Nodes modifier, tweak a few parameters, and apply the modifier. This included effects such as: Noise, Density Adjustments, Random Delete, Hair Resample, Thickness and Randomize Lengths.
Geometry Nodes
It soon became clear that although some of those effects could become a widely-usable tool (e.g., resampling), other effects were unique to the look of the production (e.g., hair thickness which was defining the hair curve profile).
These tools might be specific to the production, but they also helped the development process. Even while developing the existing brushes, a lot of the time was spent going back and forth between the artists testing the features and the developers doing small adjustments. At the end of the day the core part of each brush was rather small.
To leverage the artist’s input as much as possible and give them tools to create pipeline specific effects an idea was born …
Geometry Nodes based curve sculpting brushes.
Geometry Nodes based curve operators.
Node based curves sculpting brushes and operators.
This would also be beneficial for mesh modeling, as well as the prototype of new tools. There is no final design on how to integrate operator-specific inputs and outputs (such as selection and error messages) to the nodes, as well as how to have a separation between the brush engine and the operator logic.
This should be integrated with the Asset Browser system, as part of presets, together with regular brushes.
Next Steps
The new curves system is now officially in Blender, but it is still in its infancy. The team is now focusing on making the system exciting enough for a SIGGRAPH 2022 demo. As of now this includes a preliminary node based operator support, new tools for cutting the hair, to smooth it and a fill operator.
The next step is to support more hair specific Geometry Nodes, for the non-destructive pipeline. Finally we will need to work towards replacing the old curve system, including an edit mode for the new Curves object. There will be a task force / call for help once the project gets to this point, so more people can help porting the existing operators.
Try It Out
To test the new system download a
daily build of Blender 3.3
. Remember to
check the documentation
to read about the current limitations, and please
report bugs
if you find them.
Don’t forget to share your artwork using
#b3d
and
#HairCurves
in social media, so everyone can celebrate the new curves system together.
Hair workshop, June 2022 – Dalai Felinto, Hans Goudey, Jacques Lucke, Simon Thommes, photo by Andy Goralczyk.
Download Blender 3.3 Alpha
Download grooming demo file
Support Blender