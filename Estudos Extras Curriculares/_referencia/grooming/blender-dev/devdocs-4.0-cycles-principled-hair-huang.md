---
titulo: Blender 4.0 Release Notes: Cycles - Principled Hair BSDF (Huang model)
autor: n/d (Blender Developer Documentation)
url: https://developer.blender.org/docs/release_notes/4.0/cycles/
data: n/d (Blender 4.0, lancado nov/2023)
idioma: en
coletado_em: 2026-09-26
---

Principled Hair BSDF
¶
A new variant called "Huang" is added, based on the paper
A
Microfacet-based Hair Scattering
Model
by Weizhen Huang, Matthias B.
Hullin and Johannes Hanika (
PR#105600
).
The previous Principled Hair BSDF is now the "Chiang" variant.
Supports elliptical cross-sections, adding more realism as human hairs
  are usually elliptical. The orientation of the cross-section is
  aligned with the curve normal, which can be adjusted using geometry
  nodes. Default is minimal twist.
This is a far-field model, as opposed to the near-field Principled
  Hair BSDF model. The hair is expected to be less noisy, but lower
  roughness values takes longer to render due to numerical integration
  along the hair width. The hair also appears to be flat when viewed
  up-close.
Gives nicer focused reflection when viewed against the light.
For more detailed comparisons, please refer to the original paper and
the
Principled Hair user
manual
.
Chiang Model
Microfacet Based Huang Model
Scene by Simon Thommes and Fernando Alcala.
Open Shading Language



## Nota de coleta

Esta pagina de release notes cobre varias areas de Blender; conforme instrucao, foi coletada apenas a secao relevante a hair/Huang/curves. A pagina completa esta em https://developer.blender.org/docs/release_notes/4.0/cycles/ (pagina inteira nao coletada, apenas a secao de hair).