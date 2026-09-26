---
titulo: Hair Curve Sculpting Tools [feedback]
autor: Gareth-Jensen
url: https://devtalk.blender.org/t/hair-curve-sculpting-tools-feedback/24747
data: 2022-06-14
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — Gareth-Jensen — 2022-06-14T17:28:04.219Z

A short list of tools that we think would help artists sculpt hair curves. Again, most of this feedback is either already in progress (D15134) or probably will be. Hopefully some interesting ideas could grow from it though.
Hair Curve Sculpting Tools
CV selection
Similar to the current hair system, CVs selectable by root, tip, lasso, brush ect. It would also be great to be able to select curves by things like faces attached, UVs, vertex groups, face maps, hair groups ect
Freeze/Mask Curve Brush
Freeze/mask curves or CVs
Attract/Clump Brush
Self explanatory and already in testing I believe
Repel/Part Brush
Compliment to the Clump Brush
Jitter Brush
Selectively being able to add organic jitter to the curves
Orient
Orient entire curve from the root
Smooth/Relax with Gravity option
The ability to relax the curves in a realistic fashion
Hair Curve Groups
Making and storing hair curve groups for hiding/freezing ect. These could also potentially be called in the geom node graph

---

### Post #2 — DanielBystedt — 2022-06-14T22:04:45.720Z

Hi there!
I have an old suggestion about grooming that is using a projected curve from camera space in order to groom the hairs that are within close proximity of the first stroke point. The whole suggestion can be found here:
docs.google.com
blender fur/hair development suggestions
Blender fur/hair development suggestions  The intention of this document is to present some ideas regarding hair for the blender developers. If you need further clarification regarding my proposals, please let me know and I’ll try to clarify. I’m...
For better readability I’ll also post the text and images here. The steps below describes what happens under the hood during one single stroke. The problem this method tries to solve is to be able to groom separate strands at a time without accidentally deforming parts of the hair that the user does not want to deform when laying down the stroke:
Step 1.
image
689×558 150 KB
This red line represents the strand groom brush stroke done in screen space. This view will later be referred to as “original camera position”
Red curve  = original stroke from original camera position
Step 2
In order to see what is happening we can examine the stroke from the side. The stroke is a flat projection from the original camera position. It’s depth is based on the position of the brush at the start of the stroke
Step 3
image
488×518 94.2 KB
Project stroke by zdepth buffer
The stroke is then projected onto the visible mesh based on the original camera position (in img 1) using the zdepth buffer
If projection is slow for some reason, it might be better to simplify the curve/stroke so that it only has 10 points or less. This means that the depth only needs to be sampled 10 times
Blue curve = projected stroke
Step 4
Clamp projection
However it is better to clamp the projection so that no point is further away from the original camera position than the distance between the “camera” (eg original view) and the start of position of the original stroke (red line in img 1,2 and 3)
Purple curve = projected stroke with depth clamping
Step 5
Smooth curve
This step will lock the first and last point of the curve and smooth the rest of the points. I think the smooth strength should be set in a slider in the brush settings, since the results might vary depending on hair length etc.
Step 6
image
423×563 107 KB
Get hair curves, which root points are within the proximity of the brush radius at the first point of the groom strand stroke (green line)
If there are already curves selected, prior to making the stroke, only the selected curves should be affected by the groom strand stroke.
Step 7
image
414×535 101 KB
Shape the appropriate hair curves along the smoothed groom strand stroke (green curve)
Tapering is applied if it is set in the UI
Selection of the hair curves if the checkbox
“keep hair selection after stroke” is checked. This will enable the user to tweak the hair curves afterwards without touching the other parts of the hair.

---

### Post #3 — Vyach — 2022-07-10T05:47:02.159Z

I tested and found 2 heavy issues and 1 bug
pinch bends hair tips too much
selection with brush stroke become very hard
slide snaps hairs from backface as projected brush
2022 07 10 curve sculpt feedback - YouTube

---

### Post #4 — Vyach — 2022-07-10T09:41:17.424Z

Another one old issue, loops/knots that impossible to unravel

---

### Post #5 — fxztdede — 2022-07-11T06:21:16.470Z

感觉新毛曲 应该添加类似几何雕刻面集的 毛集
Feel that the new Hair Curve Sculpting should add a maoji similar to the geometric sculptured face set.
!

---

### Post #6 — And-Woo — 2022-07-11T07:32:01.496Z

One feature missing in the new hair system is the ability to able/disable the scalp’s modifier stack

---

### Post #7 — fxztdede — 2022-07-15T15:39:58.640Z

点色 或 曲线ID色 预览
Point or curve ID color preview
CCVV
2542×1208 340 KB

---