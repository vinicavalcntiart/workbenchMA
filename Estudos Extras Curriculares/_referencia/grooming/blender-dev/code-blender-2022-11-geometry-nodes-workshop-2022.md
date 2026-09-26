---
titulo: Geometry Nodes Workshop 2022
autor: Dalai Felinto
url: https://code.blender.org/2022/11/geometry-nodes-workshop-2022/
data: 2022-11-28
idioma: en
coletado_em: 2026-09-26
---

Geometry Nodes Workshop 2022
November 28th, 2022
Code Design
,
General Development
Dalai Felinto
The Blender Conference 2022 was an opportunity for part of the Geometry Nodes team to get together. To make the best out of having the entire core team in the same place, a 4-day workshop was held in Amsterdam.
Present there were Dalai Felinto, Hans Goudey, Jacques Lucke and Simon Thommes, besides occasional visitors such as Brecht Van Lommel, Jeroen Bakker and Julien Kaspar.
Development Process, Recap
For an overview of the Geometry Nodes development process check the
Blender Conference 2022 video
:
After tackling procedural modeling and initial hair grooming, the next big target for Geometry Nodes is simulation. This is not trivial, and one of its show-stoppers was that a more clear design was required.
This wasn’t the only long-standing topics that could use an all-hands on board meeting though. While a lot can be done with online collaboration tools, a big white board and being in the same room goes a long way. The workshop started by collecting a few of those topics. The main ones are presented here in-depth, but you can skip to the end of this article to find the
complete list
.
Those topics are:
Simulation
Loops
Geometry Object
Switch Node
Simulation
Geometry Nodes has focused on animation so far. In those cases each frame can be calculated independently of any other, and no “state” carries over. Simulation on the other hand is about using the result of one frame to influence the next one. That way even a set of simple rules can lead to complex results, with the passing of time. The most common type of them is physics simulation, with specific solvers for physical phenomena.
Local vs Global
Some simulations are
local
,  (e.g., a waving flag), while others are global with multiple objects interacting with each other (e.g., a soccer ball against a goal net). In Blender at the moment cloth and hair simulations are local, with no collision calculated between simulated objects, while rigid-body is global.
The idea is to first support local simulation, and later to extend the design to account for global simulation.
Simulation Nodes
People do so much with the currently available tools that just giving access to the previous frame’s data would make so much possible. Following this premise, a simulation is made of two dedicated nodes, and can use all the other nodes already available in Geometry Nodes.
Simulation region/frame with the Simulation Input and Simulation Output nodes.
For the input, artists can control when the simulation should start to run, and pass geometry and values to be simulated as fields. The delta time (difference of time since the last simulation step) and the elapsed time are available for the simulation. The regular nodes can be used inside the simulation region.
The simulation output node allows the simulation to stop based on an internal status, as well as receive the geometry and fields that are passed to the next step of the simulation. Outside the simulation region it is possible to know if the simulation started/ended, the elapsed time, and to get the simulated geometry with its simulated attributes.
Geometries cannot be outputted from an intermediate state of the simulation.
The inputs that are connected to the Simulation Input node are evaluated only once, at the beginning of the simulation, passed to the next simulation state and eventually outputted. Other nodes can be linked inside the simulation region from the outside. Those are re-evaluated every step based on their value at the given frame.
By design, it is not possible to have any link going towards outside. The result of the simulation can only be accessed via the Simulation Output node. This also allows sub-frame interpolation for motion blur.
Simulation Clock
At first the simulation will be tied to the animation system, besides support for sub-steps. It will only be evaluated while the animation frame changes, and it can be cached like the existing physics simulations in Blender.
Eventually simulations will be able to run on their own clock. That physics/real-time clock should run independently from the animation clock, allowing users to setup and control the simulation interactively.
Loops
Back in May 2021, “generator artist”
Erindale
Woodford was asked to provide a
comprehensive feedback
on how would they achieve arced walls, and which showstoppers may get on the way.
Although the walls and arcs were doable, growing Ivys were too much work until there were a way to iteratively loop over geometry components.
Early 2021 experiment by Erindale, inspired by Marc Chevry.
There are two main loops that were expected in a node-tree, and both can be built on top of the simulation design: Serial loops and Parallel loops.
Serial Loop
Sometimes a set of node logic needs to be repeated a few times in a row, in a Serial loop. Following the design of the simulation system, users can control the loop parameters (e.g., max iteration) and decide when to stop.
Serial loop bare-bones.
There are some similarities between the serial and the simulation loop. However, while the simulation loop is tied to
time progression
, the serial loop is fully evaluated every single frame.
Parallel Loop
If instead of running things sequentially they run simultaneously, we have a Parallel loop. There are two modes planned: Count and Elements.
Count is a more generic loop that can output a geometry (or in the future, lists) that is a combination of the individual geometry bits created in parallel. The output is joined similarly to the Join node, and individual values are outputted as fields of the combined geometry.
Parallel loop: Count mode.
The Elements mode is specifically to iterate over the elements of a domain in the geometry (points, edges, …). This mode outputs the part of the geometry that corresponds to the current iteration.
Parallel loop: Elements mode.
Nested Loops
Loops can be inside other loops, inside simulations and on and on. To see how nested loops may look like, here is a node-tree that can connect points to each other based on a distance parameter.
Plexus effect, based on
Entagma’s tutorial
.
Visuals Explorations
While the designs presented here are close to “pixel perfect”, their main focus is on the functional level. There is a lot of room to explore on how those features will end up looking, and this was left as a follow up after the workshop.
There are a few early explorations that are worth sharing though:
Convex Hull
Any node that is connected to the Input node is involved in a convex hull.
Overlaid Input and Output
Draw the input and output nodes on top of the loop/simulation region.
Other ideas that were discussed:
Aligning inputs and outputs on the same row
Node panels
Geometry Object
Geometry Nodes allow an object to have geometries of different types. The same object can have volume, curve, point cloud, mesh and instance data. This is at odds with the original design of Blender, where an object type is rigid and would determine the available edit modes as well as the panels in the properties editor.
To make matters more complicated, since the
new hair system
it became more evident that would be good to have a way to freeze parts of a node tree and edit the (baked) generated geometry. That leads to any object potentially having multiple editable meshes, or a combination of meshes, curves, and other geometries.
A solution for this is to unify all the geometry-related object types into a Geometry type. Those objects should support multiple editable geometries, while the active edit data determines which modes and panels are available.
Read-only list of edit data available via nodes.
The primitives in Blender (cube, cylinder, …) can have an initial modifier with a geometry nodes setup with the Edit Geometry node. For users that don’t want to dive into the nodes and want to go straight to edit mode there would be no functional difference.
Initial node group setup for primitives, the data-block used by the node can also be exposed as an Input, to make it simple to set it.
Menu Switch
One of the guiding principles of Geometry Nodes is that any built-in node could be re-created by a user with a node-group. So far the biggest limitation for this were the drop-down menus some nodes have as part of their options.
The Menu Switch, together with Menu sockets should allow users to close that gap. Editing the menu entries names is done in the Node properties in the properties region.
Mockup also demoing proposed node panels.
Other Topics
The list of topics covered in those few days is extensive:
Spreadsheet Editing
Import Nodes
Attribute Editing
Dynamic Socket Type
Dynamic Socket Count
Automatic Caching
Freeze Caching
Geometry Object
Usability
Node UI
Math Nodes
Preview Node
Comments
You can read more about those topics in the
complete report
.
Support Blender