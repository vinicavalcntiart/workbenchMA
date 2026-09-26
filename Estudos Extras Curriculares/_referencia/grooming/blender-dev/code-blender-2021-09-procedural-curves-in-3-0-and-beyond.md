---
titulo: Procedural Curves in 3.0 and Beyond
autor: Hans Goudey
url: https://code.blender.org/2021/09/procedural-curves-in-3-0-and-beyond/
data: 2021-09-16
idioma: en
coletado_em: 2026-09-26
---

Procedural Curves in 3.0 and Beyond
September 16th, 2021
General Development
,
General Updates
Hans Goudey
Developer Hans Goudey shares the results of the geometry nodes curve project, and future goals.
Adding a procedural curve editing pipeline in 3.0 has been a large focus for the geometry nodes team and community for the past few months. One of the last larger changes for 3.0, supporting the geometry nodes modifier on curve objects, was committed a few days ago. So I thought it would be a good idea to give an update on the project. Where are we, and what does the future hold?
Just like curve objects, three curve types are supported in geometry nodes:
Bezier
With control points handles, and handle types, each editable as separate attributes
Poly
A simple series of connected points
NURBS
A more advanced spline type with different controls exposed
The current built-in attributes on curve data
The New Nodes
One of the fundamental ideas of the changes is that it should be clearer when data is a curve and when it is a mesh. Currently Blender doesn’t distinguish very well between the two, because it implicitly changes a curve into a mesh. But we can take advantage of the flexibility of nodes to make the process much more visible.
That flexibility means that now any object that supports geometry nodes can output curve data, not just curve objects!
Curve to Mesh
The curve to mesh node with 16 profile splines
This node is the counterpart of the existing “Curve Bevel”, except that the node can accept multiple input profiles, and automatically marks sharp edges.
Curve Fill
The fill node creates a 2D mesh from curves, filling the inside with faces. It was contributed by
Erik Abrahamsson
, building on the triangulation library built by
Howard Trickey
for exact boolean. It’s the counterpart to the existing 2D curve fill in 2.93, but it should give better, more predictable results.
Curve Trim
The curve  trim and fill nodes used on curve splines from text characters
The trim node makes curve splines shorter, with a length or factor input. The node was contributed by
Angus Stanton
.
Curve to Points
This node generates a point cloud with evenly spaced points on the curve, generating the data needed for instancing like rotation.
Curve Endpoints
Also contributed by
Angus Stanton
, this node is a simpler counterpart to the curve to points node that only outputs the start and end of each spline.
Resample Curve
Drawing clouds with the points to volume node
This node outputs a new curve, sampling consistent lengths from the input. This is just like the curve to points node, except the output is still a curve.
Curve Subdivide
Like the resample curve node, this node makes a higher resolution curve, but it keeps the original spline type, and doesn’t change the shape at all for Bezier curves. Each segment can have its own number of cuts.
Mesh to Curve
Blender hasn’t had the ability to create a curve from mesh edges procedurally before. Now it does! With a selection input, any of a mesh’s edges can be turned into curve splines, and any extra attributes will be automatically transferred.
Handle Type Nodes
This node procedurally change the left or right handle types of Bezier control points.
Set Spline Type
Suddenly the star primitive gets much more interesting!
Contributed by developer
Johnny Matthews
, this node changes each spline’s type between the Bezier, poly, and NURBS types mentioned above, just like the edit mode operator.
Curve Reverse
Also created by Johnny, this is a simple node that switches the direction of a curve, just like in edit mode.
Curve Length
Another simple node to output a curve’s total length. Created by Johnny as well, who shared it on his
YouTube channel
.
Primitives
The defaults for each curve primitive node
Just like the existing mesh primitive nodes, there are now curve primitive nodes,
again
by Johnny Matthews. These provide a surprisingly useful and flexible base for both 2D and 3D contexts. Many of the nodes have options for different input methods, like finding the circle that passes through three points in space.
The Internals
Curve support in geometry nodes has also provided an opportunity to significantly improve the internals of the curve code. A large portion of the existing curve code in Blender dated back to the it’s initial open source commit, 19 years ago! While that’s not a problem in itself, standard good practices of software development have changed a lot in that time, and it was often confusing and hard to work with. Existing curve data in Blender also didn’t support storing generic
attributes
, which is essential for geometry nodes.
With the aim of replacing most of the existing code, we created a new implementation for the basics of curves, designed to be more efficient, much easier work with, and properly documented. Already this has been worth it; with an improved foundation we could make progress much more quickly than I expected!
Conclusions
Personally I’ve been interested in curves since I started working on Blender two years ago, so I’ve been happy to take on such a specific area and push it forward for a while. Five months actually– I’ve been very invested in the project, so time has really flown by!
I want to thank the community of developers contributing to this project who made it a joy to work on, and Jacques Lucke for the consistent advice.
The Future
What we have now should already be a solid base of features for 3.0, but more is planned for the near future:
Curve Fillet
Bevel-like behavior in a node from
Dilith Jayakody’s
2021 GSoC project
.
Connect Splines
A node to join multiple sections of a curve into one.
Curve Parameter
A field input node, to output how far along the curve each point is.
More complete attribute support: Transfer attributes in the curve to mesh node, expose the handle position attributes.
Curve sampling with any arbitrary factor.
Convert more of the features from curve objects into nodes.
And much more! Now that the project is mostly wrapping up, the developer community will be essential in adding new features.
Further in the future, these changes can be applied to curve edit mode as well. Editing and painting custom attributes will be particularly important.



## Nota de coleta

Este post e de setembro de 2021, um pouco antes da janela 2022-2026 pedida no brief, mas foi incluido por ser o precursor direto e diretamente referenciado do sistema de curvas que fundamenta o novo sistema de hair/grooming anunciado em 2022 ("The Future of Hair Grooming").