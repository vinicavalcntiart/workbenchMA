---
titulo: Blender 5.3a | GroomFlow & New Hair Simulation Geometry Nodes Test
autor: ChamIseul_ZEPETO
url: https://blenderartists.org/t/blender-5-3a-groomflow-new-hair-simulation-geometry-nodes-test/1645689
data: 2026-06-20
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — ChamIseul_ZEPETO — 2026-06-20T02:44:55.843Z

Hi everyone,
I wanted to share a quick hair physics simulation test I’ve been working on in Blender 5.3a.
This setup combines the brand new
Hair Simulation Geometry Nodes
with the
GroomFlow addon
(50 Guide Curves / 100 Strands).
One specific issue I wanted to tackle was the notorious root point detachment. When you duplicate hair curves using Geometry Nodes, the duplicated strands often end up floating or clipping away from the head mesh surface rather than staying perfectly snapped.
To fix this, I utilized
GroomFlow’s feature that automatically corrects and snaps the root points back to the head mesh surface
. It saved me a ton of manual troubleshooting and kept the physics simulation completely stable during the movement.
The new GeoNodes hair physics feels great, and combining it with GroomFlow seems to make the workflow much faster.
What do you think about this workflow? For those who do a lot of grooming in Blender, what are your thoughts on using addons like GroomFlow compared to pure vanilla GeoNodes setups? I’d love to hear your feedback!
GroomFlow Test

---