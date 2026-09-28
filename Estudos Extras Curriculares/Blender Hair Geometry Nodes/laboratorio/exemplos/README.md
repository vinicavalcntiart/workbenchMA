# Exemplos prontos (Blender 5.2)

Três cenas montadas só com a biblioteca `receitas_grooming.blend`, nenhuma
guia esculpida. Abra, dê play (a cacheada tem física) e mexa nos números dos
grupos GR no Geometry Nodes do objeto de cabelo.

| Arquivo | O que tem | Receitas |
|---|---|---|
| `comeco_rapido.blend` | **ponto de partida**: cabeça com hair cap real (Add Rest Position ligado), Curves vazio e a cadeia Guias Procedurais → Densidade → Mecha → Cor → Deform Curves on Surface → Profile → Material | CEREBRO 17.0, 17.77 |
| `exemplo_cacheada.blend` | cabelo cacheado com vento, cílios, sobrancelha, scalp pintado | CEREBRO 17.50 |
| `exemplo_criatura_pictorica.blend` | criatura com pelo penteado por curva, cor por clump, normal da pele no Toon | 17.55, 17.64 |
| `exemplo_anime_cel.blend` | mechas de malha, cel-shading com normal da malha lisa, contorno, ahoge | 17.56, 17.65 |

Todos os node groups estão locais (nenhum arquivo externo). Render em Cycles.

Para começar um personagem: abra `comeco_rapido.blend`, troque a cabeça e a
HairCap pelas suas (a HairCap precisa de UV), aponte o Surface do objeto
Cabelo para a sua HairCap e ajuste os números da GR Guias Procedurais.
Viewport vem em 0,25 (o render usa 100%).
