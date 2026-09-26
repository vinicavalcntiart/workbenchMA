---
titulo: Procedural Hair Nodes
autor: Simon Thommes
url: https://studio.blender.org/blog/procedural-hair-nodes/
data: n/d (contexto: desenvolvimento pre-Blender 3.5, ~inicio de 2023)
idioma: en
coletado_em: 2026-09-26
---

Procedural Hair Nodes
Simon shares what he has been up to recently as a part of Blender development.
Simon Thommes
Author
38
Report Problem
For the past few weeks I have been busy developing a set of node-group assets for procedural grooming with Geometry Nodes to be bundled with Blender. This project is the next step in the long-term effort to replace the old hair system in Blender with a new and improved system that is fully based on Geometry Nodes and much more powerful, flexible and customizable than its predecessor.
Screenshot of the procedural hair node assets as they show up by default in the assets browser in Blender 3.5
The goal here was to use the existing (and add some new) capabilities of working with curves in Geometry Nodes. We wanted to create an ecosystem of node-groups aimed at procedural hair grooming that can be used in Blender out of the box. The main focus was to allow a simplified workflow that is purely based on using these node-groups as high-level modifiers and extending their capabilities by moving them to the node editor to use them to their full potential.
This effort was a collaboration with
Daniel Bystedt
who kicked off the project by making a selection of which nodes would be useful and providing mock-ups of their functionality. Then I came in and built the node-groups based on these mock-ups, made sure they are following a consistent logic and then added thumbnails and descriptions to make them ready to be released with Blender, which is still ongoing up until the actual release.
The Target Workflow
This system brings the familiar workflow of using parent hairs that can be edited manually and then iterating with procedural operations on top of that to spawn child curves, add noise, clumping and other effects on top of that, while keeping the editable guide (parent) curves intact.
Small workflow showcase of some of the functionality that the node assets allow with very little setup.
The major benefit here, compared to the old system, is that everything is fully integrated into the rest of Geometry Nodes. Thus anyone that knows their way around those is able to customize these operations on a very granular level. But because the focus was on high-level interaction, it should be easy for people not very familiar with Geometry Nodes to pick them up and include them in their workflow. Something to also keep in mind about this new system is that it makes it very easy to allow for a destructive workflow. You can always apply the modifiers and make manual tweaks for each generated hair.
There are a few aspects to this system in which it is still lacking in comparison to the old one, which has been in Blender for several years. Mainly, those are regarding simulation and the behavior for animating the surface geometry. These will still need to be addressed for future Blender releases to reach feature parity and eventually replace the old system completely.
Influence on the Blender Development
Large part of this work was also to coordinate with the Geometry Nodes development team what features we needed to add in Blender to make the workflow with this node-group bundle smoother and more flexible.
Screenshot showing one of the new features that have been added as a part of this project. Shown here is the curve falloff setting for the curve sculpt mode
There is still a whole list of things that would improve this workflow by a large margin but has to wait for Blender 3.6 and onward; on the other hand there is also a list of things that have been improved because of this project, despite the relatively small time window:
Curve sculpting cage overlay
Curve sculpting curve falloff
Curve sculpting surface collision
Hiding inputs in the modifier UI
Operator to move an existing modifier to nodes for a smoother flexible workflow
Drag and drop in the viewport for nodegroup assets
Fur in the add menu to quickly add procedural hair
Sample custom normals in the
Distribute Points on Faces
node
And most importantly:
The ability and first precedent to bundle and ship Blender with a built-in selection of essential assets
This is something that will be done more and more in the future, especially for node-groups. The idea is to mainly rely on this method of adding nodes for high-level operations that take away the need for people to build specialized node-groups like these themselves. Even though they would be possible to achieve with existing nodes, that should be possible but not necessary. This will help artists that don't have a lot of technical depth to have an easier time using the node system and help with a less steep learning curve.
Showcase of using the nodes in combination with the grooming tools that have been implemented for the new hair system. The cage overlay shows the original curve that can be sculpted on as an overlay on top of the procedurally generated result.
Packaging node-group assets just like any other node in the regular download of Blender also means that the possibilities of customizing the interface of node-groups/modifiers need to be improved to the point where everything that the built-in modifiers can do can be replicated with custom node-groups. This has been the plan for a while now, but finally this means that there is a concrete need to improve this, which will help propel the development in that direction.
What is left to do?
Until the release, there are still plenty of things to prepare for the nodes to be ready to be adopted by the masses. This includes small fixes of the functionality and how the nodes operate together, cleaning up the messy node-trees, writing documentation the same as all other nodes have it and preparing a downloadable example file that showcases different setups using the nodes in a nice way. But the main work on what nodes are there, how they work and what their parameters are is wrapped up and can be tested in the
latest download of Blender 3.5 Beta
.
Getting closer to the release of Blender 3.5 we will also follow this up with some educational material to communicate better how these nodes are intended to be used for their full potential. For now I just want to share what I have been up to in regards of working on Blender, outside of the regular film projects that we are working on.