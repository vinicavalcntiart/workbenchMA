---
titulo: Geometry Nodes Workshop: October 2024
autor: Jacques Lucke
url: https://code.blender.org/2024/11/geometry-nodes-workshop-october-2024/
data: 2024-11-06
idioma: en
coletado_em: 2026-09-26
---

Geometry Nodes Workshop: October 2024
November 6th, 2024
General Development
Jacques Lucke
After the Blender Conference, the Geometry Nodes team came together once again to discuss many design topics. This time our focus main focus was to improve support for physics, especially hair dynamics in Geometry Nodes. A few other topics were discussed as well though. You can also read the
raw notes
we took during the meetings.
The following people participated in the workshop (from left to right): Lukas Tönne, Hans Goudey, Simon Thommes (afternoons) and Jacques Lucke. Additionally, Dalai Felinto helped kickoff the workshop and Falk David joined in every now and then.
Previously in Geometry Nodes
Our
last workshop
was 5 months ago. This section provides a quick update on the topics we discussed there. Omitted topics don’t have any news.
Gizmos
: They are part of the Blender 4.3 release. Next step here is to add gizmos to some built-in nodes like the Transform Geometry or Grid nodes.
Baking
: Bakes can be packed now. Next step is to provide higher level tooling to work with multiple bakes in a scene.
Rename Sockets in Nodes
: Ctrl+click to rename sockets works in a few nodes now (e.g. Bake, Simulation, Capture Attribute). There are some technical difficulties with making it work with double click and for right-aligned labels.
Tools for Node Tree UX
: Built-in nodes support socket separators now (used in the For-Each Zone). Support will be added to node groups at some point. The viewer node automatically changes its position now.
Asset Embedding
: A
prototype
was built to test the behavior. We agreed on how we solve the technical difficulties with it, but some UI aspects are still somewhat unclear (e.g. how this is presented to the user as a new “import method” besides linking and appending).
Menu Socket
: We improved the error handling when there are invalid links, giving more information to the user about what is wrong. This applies to menu sockets, but also other invalid links like invalid type conversions.
Socket Shapes
: We found a design where everyone is okay with the trade-offs it makes. A
prototype
was built. The work on it is still ongoing.
Grease Pencil
: Geometry Nodes can work with Grease Pencil data starting with Blender 4.3.
For-Each Zones
: There is a new For-Each Element zone in 4.3. Work on other kinds of For-Each zones is ongoing.
Approaching Physics
As usual, there are many different perspectives that we have to take into account for when designing how we want to approach physics in Geometry Nodes:
Using high level node group assets to setup e.g. a hair simulation.
Building and/or customizing solvers for specialized effects.
The modifier-only workflow.
Higher level add-ons which abstract away the node and modifier interface.
We started out by clarifying that there is a fairly fundamental difference in how to think when chaining multiple geometry operations vs. setting up a physics simulation. The difference is that when creating a simulation, one thinks about the desired behavior (forces, emitters, colliders, …) first, and not so much about the order in which the geometry is actually processed. In fact, the majority of users should only have to care about the behavior without worrying about specific geometry operations.
We therefore want to provide better ways to separate
describing the desired behavior
from actually
implementing the behavior
. We call this the
declarative
approach. It gives users high level control over a potentially very complex evaluation system that makes all the desired behaviors work. The declarative approach can also be very useful for things beyond physics like building a brush engine or scattering system.
To achieve this separation, we will introduce two new socket types: bundles and closures, which are explained in more detail below (exact names are not set in stone yet).
Bundles
A bundle is a container that allows packing multiple values into a a single socket. Values of different types can be put into a single bundle. A work-in-progress
patch
is available already.
Bundles are quite useful to reduce the number of necessary links. For now, we are mostly interested in how they can be used to create a uniform interface for various kinds of simulation behaviors. Each behavior will be a bundle that contains the necessary information for the solver to understand what to do with it.
Closures
Closures sockets allow passing around arbitrary functions including entire node groups. For example, this allows passing a node group as an input into another group which will then evaluate it. This is an entirely new paradigm in Blender’s node systems, and without being already familiar with the concept of passing functions around as data, it’s not trivial to understand. However, it’s incredibly powerful and allows building much more flexible and user-friendly high level node groups.
In programming, the term “closure” refers to functions which may be passed around as data and can capture variables from where they are created. We have not found a good alternative name yet.
To create closures, we use a new closure zone. It’s a bit like creating a small local node group that can then be passed around. Just using existing node groups does not work, because we need the ability to pass data from the outside into the closure (like in all other zone types). Also, it’s good to have the ability to build the entire node tree in a single group to see everything at once.
Position Based Dynamics
The declarative approach with bundles and closures is generally useful for all kinds of physics simulations. While we want to enable users to build their own solvers, we also want to integrate hair simulation specifically into Geometry Nodes directly.
The hair simulation is designed around a Position-Based Dynamics (PBD/XPBD) solver. This solver has been applied to soft-body simulation, cloth, hair, granular materials and more.
The PBD method is often used for real-time game physics and is relatively easy to implement. It has advantages in terms of speed and accuracy over the linearized velocity-based cloth solver currently used for hair dynamics. There are lots of learning resources and scientific papers on the topic for people to learn more. When first looking into this, we found
this overview
and
this video tutorial series
particularly useful.
We will try and implement as much of this as possible using generic geometry nodes. Some parts like collision detection and constraint grouping may require new built-in nodes for performance reasons. This will be decided when we get there.
Lists
For this project we’ll likely need lists in different places, for example to manage a list of behaviors passed into the solver and to process contact points after collision detection. Lists have been a talking point in previous workshops and we don’t have much new information that has not been
said before
. We went over the set of nodes we’d need, but there were no real surprises there.
Lists are also particularly important for hair, because we need to map generated hair to potentially multiple guide hair strands. Currently, there is no good way to store that mapping which makes any workflow that uses guides, especially for simulation, quite unreliable.
The main blocker to get lists into Geometry Nodes is still the socket shapes discussion.
Socket Shapes
The
last blog post
contains an explanation of the topic. Last time, we didn’t come to a conclusion for how to deal with socket shapes when we get more types like fields, lists, grids and images. The tricky thing is that we can’t show all information we’d like to with just socket shapes, so we have to decide what we don’t want to show anymore.
Some design work has been done on the topic in the last couple of months and a simple
prototype
has been built too. We’re now at a point where we are all at least okay with the solution’s tradeoffs so that we can hopefully progress on the topic. Once that is resolved, volume grids and lists are much easier to get into a releasable state.
For Each Geometry Zone
Blender 4.3 comes with the
For Each Element
zone. While that’s very useful already, there are other kinds of for-each zones that can be useful. One of those is a “For Each Geometry” zone, that we used to call “For Each Unique Instance” in previous workshops.
Its purpose is to iterate over each “real” geometry in a geometry set that may contain an instance hierarchy. Many built-in nodes do this internally already. For example, the Subdivision Surface node applies its effect to all meshes in the input, including those in instances. For various reasons, not all built-in nodes can or should do this. A new For Each Geometry zone would allow adding the same functionality to all built-in nodes and custom node groups which is impossible currently.
This is quite different from the “Instances” mode in the For Each Element zone. If the geometry to be processed contains many instances of the same mesh, the existing zone would run for each mesh separately, while this new zone would only run once, because there is only a single mesh.
There is already some previous design work available in
#123021
.
Modal Node Tools
We reconfirmed the overall design for modal node tools from
a year ago
. Since then, we also noticed that there are two kinds of modal operators in Blender currently:
Operators based on the initial state (like bevel). These have redo panels.
History dependent operators using the previous state at every modal step (like brushes). These don’t have redo panels.
Both kinds of operators could be created with nodes. However, when we talked about modal node tools so far, we were mainly concerned with the second type. Many use cases of the first kind can probably be solved with gizmos or a gizmo like system. That’s because the interactive part of these operators is mostly just used to control some input values for a non-modal operator.
We also noticed that there are problems caused by fact that all node tools are just a single operator in the end (
geometry.execute_node_group
), but none of these seem impossible to solve. For example, we want modal node tools to come with their own keymap, but users should be able to override this keymap like any other keymap in Blender. Typically, there is a mapping from modal operator to keymap, but that does not work well here yet for the mentioned reason. Alternatively, it may be a nice solution to attach keymaps to specific assets in the user preferences instead of just to operators.
It can also be possible to register a separate operator for each node tool, but that comes with its own problems. For example, that would introduce yet another way to reference specific asset data-blocks by their operator name and can easily cause operator name conflicts too.
Field Context Zone
We started discussing a new “Field Context Zone”. The overall design is very incomplete and we don’t have concrete answers to many questions surrounding it yet. The general idea is to give access to the field evaluation context more explicitly.
For example, for a field that’s evaluated on a geometry, the new zone would have the context geometry as input, and would output a field that depends on that geometry. This opens up new opportunities for building fields that would be much more annoying to build before.
The zone would also reduce redundancy in the design of nodes. We have pairs of nodes like
Sample Index
and
Evaluate at Index
which are the same except that one has geometry as an input and the other does not. A goal of the zone is that the Evaluate at Index node could be built out of the Sample Index node.
Extra Modifier Evaluation Outputs
A limitation of geometry nodes is that it can only output a geometry that is then passed to the next modifier. Sometimes it would be very useful to output other data like another geometry or single values. Those values could become part of the “evaluated state” of an object so that it can be referenced by other objects using nodes or drivers.
This would allow outputting a bunch of vectors from Geometry Nodes which are then used to drive an armature. Additionally, we could allow outputting a bundle of values that is then passed into the next modifier. This way it becomes possible to build more rich modifier stacks without the limitation of having to encode all information in the geometry passed between modifiers.
We could even allow outputting fields and closures from objects (probably with some limitations due to the lifetime of some data). This would allow building all kinds of effector objects that encode some behavior that can be understood by other Geometry Nodes setups. This can also be thought of as a generalization of the existing force field object type.
Internal Data Sockets
In some cases, we want to add functionality that requires passing around data of that we don’t want to expose fully. A good example would be KD trees and BVH trees which allow speeding up algorithms that require finding nearest points or doing ray casts. These data-structures have well defined APIs that we could expose, but exposing their implementation details could make future optimization much more difficult, because optimizations could require breaking files.
It does not seem benefitial to add a new socket type for each kind of internal data. So far we think that it is good enough to only add a single type (with a single color) that is used to pass around all kinds of internal data.
Another use-case that came up in the past is a “Bake Reference” socket that passes data from a Bake to an Import Bake node (once we have that). The tricky thing with an Import Bake node is that it has to be able to read bakes from disk as well as packed bakes. So just giving it a file path input does not work. Reading from files should still be possible of course, but we also need a solution for packed bakes.
Group Input Defaults
Every input of a node group has a default value. For some types, the default is currently hardcoded (e.g. an empty geometry). Others can be choosen manually in the sidebar where some socket types support more complex inputs. For example, vector sockets can be the position field by default. However, the set of possible defaults is currently hardcoded. The goal of this topic is to generalize the system for defaults to remove limitations.
The overall idea is to have a new “Group Defaults” node that has an input socket for every input of the node group. The default of any input is specified by just connecting the value to the node like in the mockup below.
We could also make it possible for some default values to depend other input values, but it’s not clear yet how much complexity this adds, so that may only be done later.
A tricky aspect is that adding a default to a socket that did not have one yet may override its value in all group nodes that use this group. That’s kind of the inverse of a problem we have already: changing group input defaults are not propagated to group nodes at all. The problem is that we don’t really know if a value has already been modified or not, which becomes even trickier when the node group is linked from another file.
Context Inputs
The goal of this topic is to solve the following problems:
We want to remove the need for control node groups as a way to get global input values (
example
). While useful in some setups, this approach does not work all that well when building reusable node systems.
We have no good way to pass the hair system’s surface geometry to the relevant hair nodes in a good way.
We have no way to override existing contextual input nodes like Mouse Position, Active Camera and Scene Time.
We need a more flexible replacement for the “Is Viewport” node, which is used to control a performance vs. quality trade-off. Just making this decision based on whether we’re rendering or not is not good enough. Sometimes the “fast” mode of a node group should be used when in edit mode, and otherwise the high quality mode.
What all these issues have in common is that we want to pass information into nested node groups without having to set up all the intermediate links which would cause a lot of annoying boilerplate. Nevertheless, we want to be able to override all these inputs at any intermediate level.
The proposed solution is to generalize the concept of “Context Inputs”. There are many existing context input nodes (like “Scene Time” and “Mouse Position”) already. We also want to add a “Context Input” node for custom inputs. Whenever a context node is used in a (nested) node group, that will automatically create an input for the node group. Group nodes at a higher level can then decide to either pass in a specific value for that input or to not connect it. If it’s not connected, the context input will be propagated further up.
If the context value has not been provided by any node, it’s propagated up to the Geometry Nodes modifier where again users can choose to specify it. If not, we could support reading the value from a custom property of the object or scene.
There is a work-in-progress
pull request
for this feature.
Modifier Inputs
We want to add more features to group inputs in the modifier:
For context inputs, we need the ability to decide whether a specific input should be provided or not.
For geometry inputs we want to choose whether an object or collection input should be used and if the original or relative space is used (like in the Object Info node).
Putting all these choices in the modifier and having them always visible is problematic from a UI perspective. Even now, the button to switch between single value and attribute input adds clutter that is not needed in many cases.
We explored options for how this could work like putting the options in the right click menu, in the manage panel or having “edit” button in the modifier that allows temporarily showing all additional settings. For now, the approach with the right click menu seems best even if it is a little less discoverable at first.
Bundles for Dynamic Socket Counts
When we explored bundles further, we noticed that they may also provide a good solution for another long standing limitation which we discussed back in 2022:
dynamic socket counts
. Since then, quite some effort went into improved support for dynamic socket counts and nowadays we have them in multiple built-in nodes like all the zones, “Capture Attribute” and “Bake”. What’s missing is support for building node groups that have a dynamic number of inputs and outputs.
We could allow tagging a bundle input of a node group as an extensible socket. Then from the outside, one could pass multiple values which will become a bundle inside the group. When outputting that bundle from the group, all the values are separated again.
Inside of the group, the nodes would have to process all elements in the bundle. Built-in nodes could do that automatically. For example, when the Capture Attribute node has a bundle input, it could recursively capture each contained field and replace it with the captured anonymous attribute field. Something similar can be done in other nodes that already have a dynamic number of sockets.
Support Blender