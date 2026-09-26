---
titulo: Groom exporter for Unreal Engine
autor: TurboCheke
url: https://blenderartists.org/t/groom-exporter-for-unreal-engine/1415778
data: 2022-11-08
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — TurboCheke — 2022-11-08T17:04:28.047Z

GroomExporter_1280_450
1280×450 92.3 KB
I released an Addon for exporting the new Curves object datatype from blender to an alembic file with the schema dictated by the groom specification of Unreal Engine, the exporter gets the Attributes from the object to export it as properties on the alembic file.
Download and more Information:
Gumroad
Quick Manual:
Drive
Currently, the addon was only tested on Windows. (Linux needs to search for the pyalembic library.)

---

### Post #2 — melvi — 2022-11-10T01:39:43.013Z

Awesome work, mate. Thanks for sharing.

---

### Post #3 — TurboCheke — 2022-11-10T02:23:41.603Z

Updated to version 0.1.2,
Updated Manuals: For
Installation
and for
How to use the Addon

---

### Post #4 — DaluzLuciano — 2022-11-25T14:20:19.459Z

But can you please tell me how can I make the new hair on Blender use UV textures ? It seems to read it per curve and not mapped. Thanks
image
1596×589 211 KB

---

### Post #5 — TurboCheke — 2022-11-25T17:22:14.960Z

Are you using the update 0.1.3? It fixes a UV attribute export bug.
The hair asset must be children, parenting the object you are UV referencing. This is for resolving the mutual origin of the parent and groom.
In your case, it looks set but I don’t see the UV attribute, normally called surface_uv_coordinate.
I recommend double check the UV name is correct and checking on the spreadsheet view if the UV values are set.
The scale can fail to get a correct export, I see the curves object on a 0,002 value if the mesh parent has the same scale the import/export and binding could work, all my work cases had a standard value of 1.

---

### Post #7 — DaluzLuciano — 2022-11-25T18:14:47.009Z

“Are you using the update 0.1.3?” You mean the Blender version?  Im using the last one.
Well just did one empty hair for testing and nothing.
image
2246×791 416 KB
Should apply any material to it?

---

### Post #9 — TurboCheke — 2022-11-25T20:59:50.371Z

I was talking about the version of my add-on.
Maybe I misinterpreted your question, if you wanna set the individual hairs with the color of the root UV, you need to replicate this set of nodes.
haircolorfromuv.PNG
3762×2160 750 KB
The material is applied to the hair.

---

### Post #11 — DaluzLuciano — 2022-11-25T21:14:55.433Z

Yes, this is what I want to do. Thank you a lot for your help. And yes I will use the last version of your addon.
But as I m new to Blender would you be able to share this project? So I will know what comes in this places:
image
1227×464 87.4 KB
Once again thanks a lot.

---

### Post #12 — yeonggyoon — 2022-11-27T05:37:32.057Z

I tried to test the groom guide. The exporter displays an error. This happens when the data type is  integer. Could you fix the error? (or… is it a feature that can’t be used yet?
)
0001
3840×1964 717 KB

---

### Post #13 — TurboCheke — 2022-11-27T18:03:29.009Z

I will look into the issue, but however, you need to set all the related sets of attributes to get a correct guide assignment on unreal.
groom_guide,   _id,
closest
guides,  _guide_weights

---

### Post #15 — TurboCheke — 2022-11-27T19:12:16.956Z

I found the problem was an incorrect assignment of the value.
I expanded the attribute input tolerance of
groom_guide
and
groom_id
from only
int
to
int | int8
The update will be frozen a time, if you want to patch your addon its a simple modification of some code lines.
On the addon folder, the AlembicGroomExporter.py
lines 140->155
att_guide_prop,         att_guide_valid             = op.getAttribute(attributes_dict, groomProperty.att_groom_guide,          data_curves_attributes[0], ["INT", "INT8"])
        att_id_prop,            att_id_valid                = op.getAttribute(attributes_dict, groomProperty.att_groom_id,             data_curves_attributes[0], ["INT", "INT8"])
        att_closest_guide_prop, att_closest_guide_valid     = op.getAttribute(attributes_dict, groomProperty.att_groom_closest_guides, data_curves_attributes[0], ["BYTE_COLOR"])
        att_guide_weights_prop, att_guide_weights_valid     = op.getAttribute(attributes_dict, groomProperty.att_groom_guide_weights,  data_curves_attributes[0], ["FLOAT_VECTOR"])

        num_point = 0
        for num_curveslice in range(num_data_curves):
            data_curve_points = data_curves[num_curveslice].points # curveslices points
            
            numVerts[           num_curveslice] = len( data_curve_points ) 
            out_uvs[            num_curveslice] = op.getAttributeValue(att_surface_uv_valid,  att_surface_uv_prop,    num_curveslice, "FLOAT2", uv_flip=prop_uv_flip)
            #specialized case
            out_guide[          num_curveslice] = op.getAttributeValue(att_guide_valid,             att_guide_prop,         num_curveslice, "INT")
            out_id[             num_curveslice] = op.getAttributeValue(att_id_valid,                att_id_prop,            num_curveslice, "INT")
            out_closest_guide[  num_curveslice] = op.getAttributeValue(att_closest_guide_valid,     att_closest_guide_prop, num_curveslice, "BYTE_COLOR")
            out_guide_weights[  num_curveslice] = op.getAttributeValue(att_guide_weights_valid,     att_guide_weights_prop, num_curveslice, "FLOAT_VECTOR")

---

### Post #17 — yeonggyoon — 2022-11-28T03:54:45.369Z

It’s working! Thank you
00001
5117×1814 702 KB

---

### Post #18 — DaluzLuciano — 2022-11-29T13:22:55.402Z

I gave up
image
1209×921 208 KB

---

### Post #19 — DaluzLuciano — 2022-12-01T11:56:59.109Z

So how do we install the library? Just pointing to the folder and pressing “install dependencies” it doesnt seem to find anything and return with this message:
image
1370×728 141 KB

---

### Post #20 — TurboCheke — 2022-12-01T22:11:38.702Z

You need to select the library archive downloaded not the folder, and you have another version of the addon with the library already installed if the problem persists, read the manuals for more information

---

### Post #22 — DaluzLuciano — 2022-12-05T17:27:44.395Z

Thanks. Now I just need to find out how to transfer the uv textures to the groom. Im knew to Blender and the pdf is kind hard to understand.

---

### Post #23 — DaluzLuciano — 2022-12-06T09:38:50.842Z

Hi Cheke I was able to install the addon and create the nodes but I keep getting this error:
image
897×604 70 KB
It is set up like this:
image
2334×995 415 KB

---

### Post #24 — TurboCheke — 2022-12-06T10:31:16.122Z

your settings look good, sometimes it needed to reboot blender,  the library doesn’t load correctly. Tell me if the problem persists, and try with the addon version with the library preinstalled

---

### Post #26 — DaluzLuciano — 2022-12-06T10:35:53.868Z

I just read your update and desinstalled by hand, re installed and I am crying…I MADE IT!
Thanks a lot man! Just did a test with a cube:
image
873×557 206 KB

---

### Post #27 — ace.animation — 2023-01-06T09:52:42.805Z

Thanks! This Addon is amazing!

---

### Post #28 — Kyrandis — 2023-02-05T10:15:06.662Z

Hey I bought this addon it seems to be working however, I’m having trouble separating selection of hair curves to designated Group IDs is there a way to do that in this exporter or an example that you can show?
I have say 4 different hair curve groups but out of the selection I want 2 of them in Group ID 0 and the other 2 in Group ID 1, instead of each being Group ID 0,1,2,3 how would I go about doing that? Currently it just groups the selection in array order

---

### Post #29 — TurboCheke — 2023-02-06T20:00:43.669Z

You edit the data on geometry nodes, the addon can only take the data and export it on the alembic file; you can see the values on the spreadsheet panel, the way to edit the individual hair curves can be specific to your project

---

### Post #31 — Haohan_Ma — 2023-02-24T03:29:12.603Z

Hi, I encountered some problems when using this addon. After exporting rootuv to unreal, it seems that part of the uv is broken
Snipaste_2023-02-24_11-27-18
595×686 445 KB

---

### Post #32 — LeAfar77 — 2023-04-13T13:53:19.125Z

So a question regarding the root_uv.
If made a groom in Blender - using the Particle generated Hair.
While i can straightforward export this as alembic file (but seems not keeping the root_uv or vertex colors) - i cant use your AddOn right away (becaue i want to keep the root_uv).
So i thought i can convert the particle into curves - but i guess that alllrdy in the converting process it looses the root_uv´s (wich are there aslong beeing a particle based hair)
any workaround ?

---

### Post #33 — DaluzLuciano — 2023-04-25T21:37:11.510Z

Does it have UVs?

---

### Post #34 — DaluzLuciano — 2023-04-25T21:38:29.508Z

Hi Turbo. Does anybody got it working using the new Blender 3.5 hair node system with UE 5.1?
Im getting this error: Python: Traceback (most recent call last):
File “C:\Users\lucia\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py”, line 50, in execute
return create_file(context, self.filepath, self.groom_scale)
File “C:\Users\lucia\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py”, line 57, in create_file
WriteAbcContent(context, oarch, groom_scale)
File “C:\Users\lucia\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py”, line 70, in WriteAbcContent
loc_origin = curvesObjects[0].data.surface.location
AttributeError: ‘NoneType’ object has no attribute ‘location’

---

### Post #35 — TurboCheke — 2023-05-05T06:46:42.623Z

the curves asset needs to have a parent, its needs to be the mesh (skeletal mesh) the position its relative to the parent, and its needed to build a correct binding on unreal.

---

### Post #36 — TurboCheke — 2023-05-05T07:02:59.708Z

I replicated the issue, I do not know a method to passthrough conversion the uv map coordinates, its possible but I dont have something who helps at this moment

---

### Post #37 — TurboCheke — 2023-06-10T17:48:03.074Z

your blender version was 3.5 or 3.5.1 when the issue appeared? with the version 3.5.1 I have replicated the issue.

---

### Post #39 — TurboCheke — 2023-06-10T18:25:12.760Z

I updated a fix on the addon. it fix blender version 3.5.1, from the curves asset the surface and surface_uv_map are empty on Python. On a function, it tries to get the surface if not the parent if not a default location.
I will check the issue from blender code side.

---

### Post #41 — melvi — 2023-07-11T19:49:33.563Z

Hi, I noticed you wrote on gumroad this addon does not support animation? If I have animated mesh with hair on it, it won’t work?
Also, any chance it could work with this for keyframed hair?
Keymesh 2 (Curves! Frame Picker!)
Released Scripts and Themes
I did complete rewrite of iconic Keymesh add-on by Pablo Dobarro, that lets you create stop-motion animation inside Blender. 
Keymesh makes object data picker animatable, meaning objects can have new data on every frame. That gives you ability to sculpt animations frame-by-frame, or even do something more experimental, like frame-by-frame attribute painting. 
Here are some videos that showcase functionality of Keymesh:
[Blender Claymation (old KeyMesh)  - Random facial animation]
…

---

### Post #44 — chris_white — 2023-11-04T19:32:56.171Z

Hi! Im working to find a way to get color info fo rfur into unreal from blender. Found your addon and have tried following directions with multiple versions of blender with multiple objects, but the groom does not export, instead i get an error:
Python: Traceback (most recent call last):
  File "C:\Users\cwhit\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py", line 50, in execute
    return create_file(context, self.filepath, self.groom_scale)
  File "C:\Users\cwhit\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py", line 57, in create_file
    WriteAbcContent(context, oarch, groom_scale)
  File "C:\Users\cwhit\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\GroomExporter\AlembicGroomExporter.py", line 70, in WriteAbcContent
    loc_origin = curvesObjects[0].data.surface.location
AttributeError: 'NoneType' object has no attribute 'location'
would love some help because it looks like you are my only hope!

---

### Post #45 — chris_white — 2023-11-05T00:09:55.737Z

OK after looking carefully, it apepars I am unable to install the dependencies. I have unzipped the folder for the plugin but I am still unable to install dependencies.

---

### Post #46 — pertsevsergii — 2023-11-23T03:56:38.087Z

Hello everyone, I have the same problem,
loc_origin = curvesObjects[0].data.surface.location
AttributeError: ‘NoneType’ object has no attribute ‘location’

---

### Post #47 — MIQUELLA192 — 2023-12-29T18:42:05.926Z

image
559×891 90.2 KB
So great job,very thank you kind generosity
bind and group id is good work

---

### Post #48 — cho_ice — 2024-04-02T14:50:31.058Z

I can’t find the export button in any version
23232
1885×1005 522 KB
Unlike other YouTube tutorials and user manuals, there is no button to press.

---

### Post #49 — cho_ice — 2024-04-02T15:02:30.538Z

jj
1886×1052 801 KB

---

### Post #50 — TurboCheke — 2024-04-02T15:35:47.499Z

The first button is for autocompleting some of the panels on the specific hair curves, was extremely helpful on bodies with multiple hairs and different settings on the simulation on unreal.
That second button is the one that exports, until today I haven’t checked the addon on 4.1 and it will not work,
you can do the last part of the export with a version of blender 4.0 (open a copy of the scene, to avoid data loses on conversions)(its a bad solution but it could do the job)
the addon depends on a custom python library for export on alembic and the version of python has changed from 3.10 to 3.11, I will look on what I can do, I suffered a code burning while compiling it by myself the pyalembic library. (for a moment like this was needed and I needed the py alembic viewer)
I will make time to get something who works on blender 4.+

---

### Post #51 — TurboCheke — 2024-04-02T15:47:14.532Z

if you are not on blender 4.1 and it not work reinstall the addon with the library preinstalled, I could see now a glimpse of blender 3.6 but maybe its  an error

---

### Post #52 — cho_ice — 2024-04-03T09:52:42.197Z

I tried downloading it on another computer just in case, but the  “Button Export” was still deleted.
If I need Python libraries and PyAlembic, what else do I need to download?

---

### Post #53 — cho_ice — 2024-04-03T15:12:48.773Z

Ah, problem solved. Blender 3.6+ GroomExporter_Library_Preinstalled_v013 Combining the two creates Button Export! 2 days of pain is finally over

---

### Post #54 — cho_ice — 2024-04-03T15:14:05.013Z

Ah, problem solved. Blender 3.6+ GroomExporter_Library_Preinstalled_v013 Combining the two creates Button Export! 2 days of pain is finally over!!

---

### Post #55 — Carter9582 — 2024-04-15T10:10:28.435Z

Hello guys. I am looking for help regarding groom export from Blender to Unreal. Is there a way in Blender to assign Group IDs to Hair Curves and to combine different Curves into one so that you only export one Groom Asset into Unreal in which I have the option to edit each Group seperately? In the Meerkat Demo from Unreal they managed to do that but using Yeti for the Groom.
image
3418×1217 508 KB

---

### Post #57 — TurboCheke — 2024-04-15T21:18:43.519Z

I deleted a bad answer, I tested it some years ago, you only need to select the multiple curves asset you want to export, fulfill the attributes you want to export, the group_id its not needed to set, I need to look deeper if its the addon who manages to set it for every curve asset or its unreal itself, but with those steps it works.
Captura de pantalla 2024-04-15 221134
3779×2160 1.63 MB
Captura de pantalla 2024-04-15 221746
1893×1080 952 KB

---

### Post #58 — TurboCheke — 2024-04-15T21:25:39.065Z

I updated the addon to support Blender 4.1, with the updated python version from 3.10 to 3.11 the python module PyAlembic doesn’t work, it wasn’t easy it requires an cascade of libraries to be compiled prior, the addon don’t have any code update.

---

### Post #59 — Carter9582 — 2024-04-16T05:58:11.948Z

Exactly what I was looking for, thank you so much! Eventhough the solutions to this sounds so simple, I did not found anything about that elsewhere, only that you could combine everything in an new empty hair, but that did not work for me since all group inputs of the GN were destroyed.

---

### Post #60 — bietuocom — 2024-05-23T16:33:27.887Z

Hi guys does this work with UDIM’s? I can export the fur successfully but it’s not mapping correctly in UE.

---

### Post #61 — tangorn — 2024-07-29T16:05:12.390Z

Does it fully support Blender 4.2? Looks like very close but not quite yet: export goes fine, shows group stats in unreal properly (except max radius which for some reason is 0), but does not render anything visible… Unreal 5.2.1 here, I can change blender version, Unreal version is locked for me though, have to stay with 5.2.1…
EDIT: Confirmed that downgrading Blender to 4.1 fixes the issue - max radius shows as 1 and groom is visible in Unreal render window.
EDIT2: So export I can, but when I attach the groom to the skeletal mesh it does not follow the mesh when mesh is animated, which kinda defeats the purpose.
EDIT3: Never mind, was a typo in binding name on my end. You rule, everything is perfect!

---

### Post #62 — yeonggyoon — 2024-09-20T08:10:48.439Z

Hi! I recently tried using the Groom Exporter after a while, and I seem to be running into some issues.
I’m currently using UE5.4 and Blender 4.1. While I’m familiar with the basics, I wanted to explore more advanced features.
The first issue I encountered is that the guide seems to be reading the information incorrectly. Could this be a bug caused by the UE5.4 update? If you check the attached screenshot, you’ll see that I have only 2 guide curves, but there are more than 2 curves visible in the viewport. I eventually switched the guide type to Rigged Guides to fix the issue, but I’m not sure if that’s the proper solution.
Could you take a look at this?
Also, for the second issue, I created guides in Blender, but I’m unsure how to assign weights to the child (non-guide) curves. I’d like to manually add attributes in Blender to create something like the afro hair shown in the attached screenshot.
YG_001
3062×1442 299 KB
YG_002
2150×1113 652 KB

---

### Post #63 — yeonggyoon — 2024-09-20T08:39:20.802Z

And…I also came across the Groom Export plugin on the Unreal Engine Marketplace, and it looks really interesting. I haven’t tested it yet, but it seems like a great way to bring MetaHuman groom into Blender for study.
Have you thought about creating a Groom Importer addon that supports importing attributes? If you decide to release it as a paid option, I’m ready to pay for it!

---

### Post #64 — Amoeba — 2024-10-10T07:23:46.169Z

“How do I set the save guide property in blender Geometry nodes? Why is the guide automatically allocated when I import it into ue5 and import it into ue5.4 using Blender 4.2lts”

---

### Post #66 — kgerd — 2024-11-14T15:20:54.517Z

Hello, great addon. It is extremely useful.
I have an issue with the Interpolate Hair Curves node and the exporter. When the node is applied, the alembic gets totally messed up root colour in Unreal.
Has anybody dealt with such a problem? Any solution?
Thanks in advance

---

### Post #67 — PierreSchiller — 2025-04-06T06:27:34.701Z

Joining this conversation; is the addon updated for Blender 4.4 and Unreal 5.5.4? Unreal 5.5.4 instant-crashes with the old Blender 4.4 hair particle system. I need to export using curves + GN

---

### Post #68 — cfnjrey — 2025-07-07T15:22:10.355Z

Has anyone managed to get this to work on Linux? I copied similar libraries to the plugins directory and I get the error “initialization of imath failed without raising an exception”

---

### Post #70 — PierreSchiller — 2026-06-02T08:45:45.994Z

@TurboCheke
I got your gumroad email about the update. I downloaded GroomExporter_v016.zip - Tried to install it into Blender 5.1
I got this error:
Python: Traceback (most recent call last):
File “E:\Program Files\Blender-51\5.1\scripts\addons_core\bl_pkg\bl_extension_ops.py”, line 1504, in execute
cmd_batch = self.exec_command_iter(is_modal)
File “E:\Program Files\Blender-51\5.1\scripts\addons_core\bl_pkg\bl_extension_ops.py”, line 2598, in exec_command_iter
self.exec_legacy(source_filepath)
~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
File “E:\Program Files\Blender-51\5.1\scripts\addons_core\bl_pkg\bl_extension_ops.py”, line 2731, in exec_legacy
bpy.types.PREFERENCES_OT_addon_install.execute(self, bpy.context)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
File “E:\Program Files\Blender-51\5.1\scripts\startup\bl_operators\userpref.py”, line 830, in execute
bpy.ops.preferences.addon_enable(module=mod.
name
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Error: DLL load failed while importing alembic: The specified module could not be found.

---

### Post #71 — TurboCheke — 2026-06-28T23:39:22.061Z

Only the version > 0.1.7 supports Blender 5.1, when the Python version of Blender updates it invalidates the Pyalembic library, for that I need to recompile the cascade of libraries needed and update the addon.

---

### Post #72 — TurboCheke — 2026-06-28T23:39:38.620Z

Updated to version 0.1.9 added support to export hair Alembic animations as Groom Cache, added a Node Editor for custom groups of Hairs.
A Blender file made on Blender 5.2 Beta to check the new “Hair Dynamics” Geometry node, and to serve as a base for the ussage of the addon. And More Additions.

---

### Post #73 — PierreSchiller — 2026-06-29T16:51:41.948Z

Fantastic work! I will test it on 5.2 asap.

---