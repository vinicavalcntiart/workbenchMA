---
titulo: Geometry Nodes Workshop: July 2025
autor: Jacques Lucke
url: https://code.blender.org/2025/07/geometry-nodes-workshop-july-2025/
data: 2025-07-24
idioma: en
coletado_em: 2026-09-26
---

Geometry Nodes Workshop: July 2025
July 24th, 2025
General Development
Jacques Lucke
In July 2025, various Geometry Nodes and Blender contributors gathered at the Blender HQ in Amsterdam to discuss many design topics. This post gives a general overview of the topics that were discussed. You can also read all the
raw notes
we took during the meetings.
Previously in Geometry Nodes
Our
last workshop
was 8 months ago. Here’s a quick update on the main topics we’ve worked on since then. Some even made it into the recent Blender 4.5 LTS release.
Mesh Normals
: The new
Set Mesh Normal
node has been added to be able to work with custom normals in Geometry Nodes. This was made possible by various changes in recent years, especially regarding Auto Smooth.
Import Nodes
: It’s possible to
import various file types
directly from disk now (.obj, .stl, .ply, .vdb .csv, .txt).
Grease Pencil
: Working with Grease Pencil data in Geometry Nodes has been simplified by the
addition of various built-in nodes
to set attributes.
Visual Geometry to Objects
: It’s possible to convert the Geometry Nodes
output to separate objects
now which can be edited or exported.
Node Editor UX
: The node editor has seen various UX improvements, especially related to
frame nodes
, error handling, node search and
more
.
Closures and Bundles
: This is an experimental feature now which should be ready very soon.
Hair Project
: This is still ongoing. The general
declarative system
for setting up physics simulations will be possible with closures and bundles. Solver development is still ongoing.
Lists
: An initial version of lists will soon be merged as experimental feature.
Socket Shapes
: The socket shapes updates are currently available as experimental feature and will be done after some missing finishing touches.
Hair Dynamics
The overall
declarative design
we are going for is unchanged. Development work is ongoing on multiple fronts including closures and bundles, solver and lists.
In this workshop we mainly focussed on being a little more specific about the milestones we want to achieve. The main observation is that there is a big difference between building a system that can be used to build production files and one that has a proper workflow that can be used by anyone to create hair simulations.
Our first milestone is to build a vertical slice that results in a .blend file with a nice hair simulation that mimics the final intended experience. Importantly, at that stage, the workflow to get to that file may not be fully done. However, this intermediate step is necessary to validate the overall direction.
More milestones
will be to release a solver and then build workflows around that.
Lists
The overall design has not changed. The main goal in this workshop was to define a good minimal set of features that can be merged as experimental feature. A
PR
is available already.
The initial experimental feature will come with a new socket shape and three nodes: one to create a list, one to retrieve individual or many elements and one to get a list length. While not optimal, these nodes can be combined to build various other important list operations already like concatenation, slicing etc.
Color Ramp and Curve Mapping
One long-standing and annoying limitation is that node groups can’t have color ramps or curve mappings as inputs, which reduces their reusability. The issue is that these widget types are fairly different data than all the other types we support currently.
Fortunately, with the introduction of Closures, there is a more clear way forward to resolve this limitation. The observation is that color ramps and curve mappings are just a special kind of function and thus can be passed around as closure. For example, a color ramp is a function that maps a
float
to
color
.
Of course, people using high-level group nodes shouldn’t need to know exactly what a closure is. So, we want to show the corresponding widget directly in the node. This can be achieved by giving closure group inputs a subtype that specifies what kind of widget should be used for the input by default. Of course, it’s still possible to override the built-in closure with a custom one.
An
initial PR
is available already. We still want to try to display a collapsed version of the widget in the node UI by default which takes up less space. It can be expanded by clicking on it. Additionally, showing these widgets in the Geometry Nodes modifier is more tricky and still has to be implemented too.
Curves and Color Ramps exposed in Node Groups.
Node Group Interface Layout
Nowadays, w e have the ability to group sockets in arbitrarily nested panels. While this got us closer to being able to replace all (or at least most) layouts we see in built-in modifiers, there are still a
few missing aspects
. For example, we can’t display more than one property in a row.
The solution is to support building more kinds of layouts in the node-group interface tree view. What’s now called “panel” will be renamed to “layout” and each of these layouts has a type of either panel, column or row. This is akin to how layouts are defined using the Python API.
One major design constraint is that we want the node group interface to look as Blender-like as possible. For example, panels should always come after sockets, but that is not the case for rows. The design problem is how to ensure that people can build such a UI without making the authoring process annoying, by forbidding all invalid states by construction, even if those states are only meant as intermediate steps while building the final UI.
The approach we chose is to remove all the limitations in the tree view UI when authoring the assets. However, all constraints are still applied when actually using the node-group somewhere. For example, panels are automatically displayed after all sockets even if they are ordered differently in the tree view UI. The node-group author will see obvious warning signs when something is invalid.
Enforcing all constraints while building the interface is already often annoying, and it will become even more so as additional, less obvious constraints are introduced, which are still important for UIs to feel consistent with official Blender.
Socket and layout options.
Viewing Individual Instances
This is a new topic that was brought up. The initial idea was that selecting a specific instance in the spreadsheet could also just make that instance visible in the 3D viewport. The goal is of course to make it easier to inspect a small part of a potentially very large geometry with many instances.
While that can work, the initial approach wasn’t ideal because many use Geometry Nodes without the spreadsheet and this functionality still makes sense. Currently, the best approach seems to be to make this a special case of local view. One could imagine entering local view not just on individual objects, but also on sub-objects. The exact UI for that is still somewhat fuzzy though.
View Any Data
With the introduction of bundles, grids, and lists, the need for new ways to view data arises. The current Viewer node can only view a geometry with potentially one field on it, but it’s often impractical to use with other data.
The two main approaches seem to be to either generalize the existing viewer node or to have different built-in viewer nodes for different purposes. We found that having a single general built-in viewer node likely works better.
We want to generalize it by giving it some kind of dynamically typed multi-input. The idea is that one can connect arbitrary data to it, so it can have even more than just two links. Then the viewer node checks what data it actually received and decides how to display it based on that. The existing Ctrl+Shift+LMB behavior functionality becomes a bit less obvious, but we can probably fairly easily make it work as least as well as it works now.
Custom Viewers
Related to that is also the topic of custom viewers, i.e. a node-group which should be treated as Viewer. The node-group can do some additional processing on the input to prepare a different kind of visualization than what the built-in viewer would provide.
This should work with the Ctrl+Shift+LMB functionality and it should be easy to author and select these custom viewers. It became clear that the author needs to be able to make a distinction between viewer input that receive the viewable data and other inputs that configure properties of the viewer.
The topic is separate from overlays for attribute data in the 3D viewport, which should also receive more functionality.
Debug Views
The idea here is that node-groups could have prepared Viewer nodes which display debugging information that is not just useful for the author but also for users. When using a Group node or modifier, one could enable these debug views to get insights into how the group is working.
It’s not entirely clear what the UI for this would look like. It seems like it would be good to interleave toggles for specific debug views with other node-group inputs instead of having a separate panel for them all. However, ideally it would also be obvious to the end-user that enabling a debug view does not affect the final result in any way.
Furthermore, a good solution would also allow for composability, i.e. a node-group can inherit debug views of nested node-groups.
Geometry Nodes Features Everywhere
Many advanced node-tree features are currently only available in Geometry Nodes, such as repeat zones and soon also closures and bundles. However, technically all of these features also make sense in shading and compositing nodes. The reason they exist only in Geometry Nodes right now is that the evaluator is more general by design and these features are most useful there. Nevertheless, it would be good to get at least a limited version of this functionality into other tree types.
A fairly simple approach to solve this is to pre-process the user-defined node-tree and to inline all the more advanced features like repeat zones so that the actual evaluator does not have to deal with them. There is a
PR
that does that already. It’s still somewhat limited compared to Geometry Nodes, because e.g. the number of iterations has to be a constant value to be able to inline the zone. This might be a good trade-off for shader nodes though, to get these features in Blender sooner rather than later, or even at all.
The main discussed alternative is to have a new intermediate representation for the inlined node-tree. While that can work, it’s a much bigger project, and it’s not obvious that it will be significantly more useful than the simpler approach in the future. If renderers eventually support the more advanced evaluation features out of the box, they could also skip the pre-processing.
For the compositor, the situation is less obvious because its evaluation mechanism is more similar to Geometry Nodes, i.e. it has simple left-to-right data flow and it is only invoked once instead of per sample. That makes it easier for the Compositor to support these more advanced features directly without requiring an intermediate inlined node-tree. Staying closer to the original node-tree also helps with debugging because there is a more direct correlation between what the user sees and what the evaluator sees.
Asset Menu Path
Node-group assets can show up in various places in the UI including the node and modifier “Add” menu, and in the 3D Viewport header/menus for node tools. Currently, the asset catalog path is used as menu path. While that works well in simple cases, there are limitations with this approach. For example, the same node-group could show up in different places in the node and modifier add menus (see e.g. the
Subdivide
operation). Similar issues exist for node tools that can be used with different object types.
Overall, we want to separate the catalog path from the menu path, and probably also have more than one menu path per asset for the different uses. We could store the menu paths per catalog, but currently the best approach seems to be to store them on the asset directly. This gives asset authors the most control.
Additionally, we can use path variables in the menu path. For example, the tool menu path
{OBJECT_CONTEXT}/Transform/...
would map to
Object/Transform/...
or
Mesh/Transform/...
depending on the current mode.
Bone Info
There is a
PR
for a new
Bone Info
node. The purpose of that node is to get information from an armature into Geometry Nodes. During the workshop we discussed how that fits into the overall future of armatures in Geometry Nodes. Additionally, we also agreed on a set of sockets that we are confident can be released in an initial version.
Obviously, getting information from one specific bone is quite limited compared to getting an entire armature. However, this is not an either-or situation. Having a node that retrieves data from one hardcoded bone can be beneficial because the dependency graph knows what Geometry Nodes depends on and does not have to create a generic dependency on the entire armature. This is especially important to avoid dependency cycles when the output of Geometry Nodes is supposed to drive other bones in the same armature.
Work in progress Bone Info node.
Asset Versioning
Now that the asset ecosystem around Blender is growing, and we ship assets with Blender, it is becoming more important to be able to update assets and to inform the user about it. While Blender can detect that an asset has changed (at least with
packed assets
), it doesn’t know if the version on disk is older or newer than the used one. For that, one needs an explicit user controlled version number, ideally using
a form of semantic versioning
.
There are various ways to add a version number. It could be stored in the asset
.blend
file, in file names, or in separate config files. Currently, the best solution appears to be to encode version numbers in file names like so:
materials_v1.0.0.blend
. While this does come with some limitations, like all assets in that file having the same version number, it seems like a simple-to-manage solution that could work well in practice.
A minimum supported Blender version is commonly tied to file rather than the asset anyways. For now this is just the version a file was last saved with.
Closures and Bundles
Closures and bundles have been introduced in a
previous post
. They are essential for building
declarative systems
. Both features have been in Blender as experimental feature for a while now. During the workshop we mainly went over some of the details again, making sure that we are aligned on everything.
We found a few cases where the automatic population of sockets could be improved, and we considered a few additional warnings that could be generated when these features are not used quite correctly.
The main functional change we discussed is to forbid using certain special characters in the names of bundle items. This became necessary, because we want to be able to specify paths in nested bundles like
root/forces/wind/...
.
Other Topics
We also talked about several tangential topics that seemed interesting for the future direction of Geometry Nodes but didn’t result in any concrete actionable development yet. For example, we talked about a more general way of extending the input socket interface by changing the way they are exposed (e.g. expose Geometry socket as an Object or Collection input on demand).
We also signed off multiple ready-to-be-merged PRs and had general discussions about Blender architecture and code.
Again, the
complete raw notes of the workshop
are available as well.
Support the Development
These projects are still in development, and will need dedicated design and development resources. Join the