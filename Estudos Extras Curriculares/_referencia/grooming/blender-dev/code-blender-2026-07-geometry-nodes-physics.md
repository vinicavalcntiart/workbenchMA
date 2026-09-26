---
titulo: Geometry Nodes Physics
autor: Jacques Lucke
url: https://code.blender.org/2026/07/geometry-nodes-physics/
data: 2026-07-30
idioma: en
coletado_em: 2026-09-26
---

Geometry Nodes Physics
July 30th, 2026
General Development
Jacques Lucke
In Blender 5.2 LTS we released the first version of a new hair and cloth dynamics system powered by Geometry Nodes. This post describes what we have so far and what our plans for the future are.
State in Blender 5.2 LTS
The new physics systems are implemented as built-in node group assets. They wrap a more general declarative XPBD simulation framework which is internally powered by the new XPBD Solver node. The high-level cloth and hair assets are easy to use by design and don’t require users to understand the physics underneath.
Geometry Nodes Physics Demo File:
Space Fabric Cloth Tear by Cartesian Caramel
This section of the article overlaps a lot with the
release notes
. Expand to learn more.
Currently, the new physics systems are still marked as experimental in the UI. That’s because the design might still need to be iterated on slightly as we gain more experience over the coming months.
Cloth Dynamics
The new Cloth Dynamics modifier and node group can just be added to any mesh to give it cloth-like behavior. It supports various built-in features like pinning, stretchiness/bendiness controls and tearing.
The asset can also be used as node group.
Hair Dynamics
Hair works similarly but needs a bit more setup because it requires a surface the hair is attached to. When using the updated
Empty Hair
operator in the add menu, this setup is done automatically.
Note how this also adds the
Capture Rest Geometry
modifier to the surface mesh. This is required for the dynamics modifier to know how the surface changed from the rest to the deformed state. This data is stored in the new
geometry bundles
.
A fully procedural setup within Geometry Nodes is possible too.
Effectors
An effector is anything impacting the simulation. The Hair and Cloth Dynamics groups have a bunch of built-in effectors for ease-of-use like gravity and surface collision.
It’s also possible to pass in additional effectors though. Currently, there are three types of customizable effectors available:
Collider: Any closed mesh can be used as collider.
Custom Force: Allows computing custom force vectors for each point.
Custom Effector: Allows injecting fully custom behavior at specific stages into the simulation using a closure.
Additional effectors can be added to the simulation in two ways:
Effector Collection: One can create a collection containing objects which have effector information stored.
Effector Bundle: In a node-based workflow, one can also create a bundle containing an arbitrary number of effectors.
Colliders
A collider object is created by adding a
Collider
modifier to it. This uses the geometry at that point in the modifier stack as collision mesh.
In a fully procedural setup, one can use the collider effector bundle and pass into the dynamics node. To pass in multiple effectors, a
Combine Bundle
node can be used.
It works the same way for hair.
Forces
Besides the built-in gravity, there are no ready-to-use forces for this system yet. However, one can easily build custom forces.
This setup can also be modified to create custom force objects. The
Set Effector
asset attaches effector bundles to a geometry so that the simulation finds it later on. This also works very well together with the new support for
Geometry Nodes on Empty objects
.
Custom Effectors
Custom effectors can be used to inject fully custom behavior into the simulation using closures. It runs at the specified stage (e.g. “Post Solve”) in the simulation loop. Because the geometry is in simulation space, which usually matches world space unless specified otherwise, the
To World Transform
is provided. It contains the information needed to transform the geometry into world space, from which it could be transformed into any space as necessary.
Filters
Effectors can have a filter to determine which geometries they affect. The filtering system uses tags. Each simulated geometry can have one or multiple tags. An effector can then specify which tags it should affect.
XPBD Solver
The Cloth and Hair Dynamics assets are internally powered by a new built-in XPBD Solver node. It does the heavy lifting solving various constraint types. The assets build a use-case specific declarative system around this built-in node. For more advanced users, there are two main approaches of customizing the simulation at a deeper level:
Adapt the Hair/Cloth Dynamics node groups. These are fairly hackable, i.e. one can just add or remove constraints as needed in a declarative fashion. With this approach, one is building on top of the
XPBD Simulation
framework.
Build a completely new simulation system directly on top of the
built-in XPBD Solver
node. This is quite a bit harder as the solver needs a lot of information in the form of typed bundles and attributes.
Future of Physics in Blender
At a high level, the goal is to provide easy to use node group and modifier assets for the most common physics use cases including hair, cloth, rigid bodies, soft bodies and fluids. This is similar to what we already have for hair and cloth now.
At the same time, these systems should be highly customizable using Geometry Nodes. Custom forces and other effectors can already be created; solvers should eventually combine freely too, instead of only working in isolation.
The physics simulations should not only be available as modifiers but also in node tools. This will allow using physics for modelling, sculpting and interactive applications.
While a single physics solver that does everything would be perfect, it is unrealistic since each solver comes with trade-offs. Therefore, it is more future proof to design a framework that easily allows integrating various different solvers. Those can either be implemented as node groups or directly into Blender. Also, some of those we might implement ourselves while for others we can rely on existing libraries. High level assets like the Cloth Dynamics modifier then just internally pick the right solver to use.
Next Steps
The XPBD Solver node contains our first solver. We already tried to design it in a way that other solvers can use the same overall framework to setup constraints etc. However, to really test this framework further, we need more than one solver to more accurately determine the similarities and differences between them.
On that front, work is ongoing to make an initial
fluid solver
and we started looking into the
jolt solver
mainly for rigid bodies. Together with the existing XPBD solver, this should provide us with a good set of different solvers allowing us to finalize a common physics simulation framework for Blender.
At the same time, we still want to improve the existing solver of course with things like self-collision for cloth and hair. Custom solver support keeps improving too, gaining more functionality for volume grids and lists.
Ongoing work for modal node tools also makes physics solvers available for destructive editing in e.g. edit and sculpt mode and other interactive applications.
Support Blender