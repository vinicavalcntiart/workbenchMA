# Cérebro de grooming: hair curves + Geometry Nodes no Blender 5.2

Síntese de trabalho, escrita a partir das fontes desta pasta. Cada afirmação
aponta o arquivo de onde veio, em `[colchetes]`. O que não tem colchete é
julgamento meu e deve ser tratado como opinião de quem leu tudo isso, não como
fonte. Última revisão: 2026-09-26.

Caminhos abreviados:
`manual/` = `../blender-manual-5.2-lts/manual/`,
`api/` = `../blender-python-api-5.2/api/`,
`int/` = `essentials-internals/`, `dev/` = `blender-dev/`,
`com/` = `comunidade/`, `jp/` = `blogs-jp-zh/`.

---

## 1. Modelo mental

O sistema tem três camadas, e quase todo problema vem de confundir duas delas.

**Guias.** O objeto Curves guarda as curvas originais. São elas que você
esculpe no modo Sculpt Curves, que ficam presas ao scalp pelo atributo
`surface_uv_coordinate`, e que o modo Sculpt desenha como "cage" por cima do
resultado avaliado [dev/studio-blender-2023-procedural-hair-nodes.md,
seção "Curve sculpting cage overlay"].

**Stack de modificadores.** Cada hair node da Essentials é um node group usado
como modificador. A ordem da stack é a ordem das operações. Os grupos são
assets embarcados; o mesmo grupo pode ser aberto no editor de nodes para ir
além do que o painel do modificador expõe [dev/studio-blender-2023-procedural-hair-nodes.md;
com/devtalk-27601-...md, posts 3 e 5].

**Resultado avaliado.** Filhos interpolados, clump, ruído, tudo isso só
existe na avaliação. Não dá para esculpir filho. Se algo parece errado num
filho, o conserto é na guia ou na stack.

Consequências práticas:

- Você trabalha com poucas guias e muitos filhos. Quem tenta esculpir milhares
  de curvas trava o viewport e conclui que o sistema é ruim; era isso que
  faltava entender [com/blenderartists-1460445-...md, posts 2, 4 e 8].
- Um groom realista é vários objetos Curves, um por região: scalp, franja,
  sobrancelha, cílio, barba, e no caso de fur, corpo, orelha, bigode
  [jp/ja-tenp-kukan-2025-10-hair-curves-fur.md; com/blenderartists-1460445-...md,
  post 8]. Cada um com sua stack, cada um com sua densidade. Copiar stack entre
  objetos: Ctrl+L, Copy Modifiers, e reatribuir a superfície no Interpolate
  [jp/ja-tenp-kukan-2025-10-hair-curves-fur.md].

---

## 2. A stack canônica

Ordem que funciona e por quê. Regra do blog japonês, confirmada pelos
internals: gerar, depois deformar, e Deform Curves on Surface sempre por
último [jp/ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md].

```
1. Interpolate Hair Curves        gera os filhos a partir das guias
2. Create Guide Index Map (grosso) escolhe guias de clump de nivel 1
3. Clump Hair Curves (nivel 1)    macro-mechas
4. Create Guide Index Map (fino)  guias de clump de nivel 2
5. Clump Hair Curves (nivel 2)    sub-mechas
6. Hair Curves Noise              ondulacao coerente
7. Frizz Hair Curves              crespo por ponto, flyaways
8. Curl / Roll (se o cabelo pede)
9. Trim Hair Curves               comprimento e variacao
10. Set Hair Curve Profile        raio raiz-ponta
11. Shrinkwrap Hair Curves        tira o que entrou na pele
12. Deform Curves on Surface      segue a animacao do scalp
```

Os passos 2 a 5 são a diferença entre "cabelo de CG" e cabelo. Foi exatamente
isso que um groomer de produção pediu aos devs em 2022: uma cadeia em camadas
de guia, interpolação e clump, controlando cada nível, porque "só adicionar
ruído ainda parece procedural" [com/devtalk-24686-...md, post 1]. Os nodes
saíram desenhados para isso.

---

## 3. Guias: esculpir bem antes de qualquer node

**Criar.** Shift+A, Curve, Empty Hair, com o scalp selecionado. Isso já liga
o objeto ao scalp e ao seu UV map [manual/sculpt_paint/curves_sculpting/].

**Quantas.** Poucas. Para fur de gato, o tutorial japonês usa o pincel
Density em modo Auto com Distance Min 0,02 m, Length 0,1 m, 6 pontos por curva
[jp/ja-tenp-kukan-2025-10-hair-curves-fur.md]. Para cabelo humano, dezenas a
poucas centenas de guias por região dão conta; o resto é interpolação.

**Pincéis que importam** [manual/sculpt_paint/curves_sculpting/brushes/]:

- Comb, com X Symmetry e Use Sculpt Collision ligados. Colisão evita que a
  guia entre no scalp; distância 0,002 m no exemplo de fur.
- Grow/Shrink com comprimento mínimo definido por região (0,07 m rosto,
  0,05 m e 0,03 m perto de olho e nariz, no gato).
- Puff com Strength baixo, 0,25, para levantar da pele.
- Add com "Front Faces Only" em áreas finas, para não plantar do lado errado.

**Pontos por curva.** Poucos pontos dão curvas duras; muitos pesam. Seis a
oito para fur, mais para cabelo longo. Redistribute Curve Points existe na
Essentials para reamostrar depois [int/redistribute-curve-points.md].

**Colisão travando pincel.** Reclamação antiga: com Use Sculpt Collision
ligado, os brushes param de funcionar em malha densa
[com/blenderartists-1460445-...md, posts 5 e 9]. Se acontecer, desligue a
colisão, penteie, e resolva penetração no fim com Shrinkwrap Hair Curves.

**Esconder guias não existe nativamente no 5.2.** Há um test build de
contribuidor com H e Alt+H, ainda em revisão [com/devtalk-44094-...md].

---

## 4. Interpolate Hair Curves, por dentro

O que o painel esconde, lido dos internals [int/interpolate-hair-curves.md]:

- A distribuição de pontos no scalp é um Distribute Points on Faces, em modo
  Random ou Poisson Disk conforme o menu. Density Mask entra direto no Density
  Factor. Density Max e Distance Min do Poisson são derivados da Density.
- Os filhos são gerados pelo node nativo Interpolate Curves. "Interpolation
  Guides" é o Max Neighbors dele: quantas guias cada filho mistura.
- Part by Mesh Islands alimenta os Guide Group ID e Point Group ID do node
  nativo com o índice de ilha da malha. É o único particionamento exposto. O
  node nativo aceita qualquer inteiro ali; um region map colorido vira Group ID
  se você duplicar o grupo e ligar uma entrada nos dois sockets.
- Mask Texture entra como Probability de um Random Value: a cor vira um float
  só. Máscara é escala de cinza. Um mapa RGB serve para três máscaras se você
  separar canais no editor de nodes.
- Distance to Guides limita o spawn a um raio em torno de cada guia; útil para
  tufo, barba rala, ou "só onde eu plantei guia".

**Surface Rest Position.** Ligado, a interpolação lê a malha em repouso, e o
Deform Curves on Surface no fim da stack faz o cabelo acompanhar a animação
[jp/ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md]. É o padrão certo
para personagem animado.

**Estabilidade das guias.** Na primeira versão, mudar a densidade fazia o
cabelo "pular", porque a guia original era removida e o filho mais próximo era
promovido a guia com outro ID. Simon Thommes corrigiu tornando o ID estável e
garantindo que o filho gerado no lugar da guia bata com ela exatamente
[com/devtalk-27601-...md, posts 5 e 7]. Ainda assim: mude a densidade cedo,
não no fim.

**Subdivision Surface no scalp é um problema real.** Os filhos seguem a malha
subdividida, mas as guias ficam na malha base, e Surface Rest Position
piora isso. Não há solução oficial; é o item mais votado da lista de pendências
#125700 [com/blenderartists-1621672-...md, posts 1, 3, 6 e 7]. Caminhos:
aplicar o Subdivision no scalp antes de groomar, ou trabalhar com um scalp
separado já subdividido. Para o erro "Invalid surface UVs on N curves" do
Surface Deform, mudar UV Smooth do Subdivision para None resolveu num caso
[com/blenderartists-1621672-...md, post 9].

---

## 5. Clump em níveis

**Como o Clump escolhe guias.** Se você não fornece Guide Index, o node cria um
mapa novo: Merge by Distance nas raízes com a Guide Distance como raio, filtra
pela Guide Mask, e cada curva recebe o índice da guia mais próxima por Sample
Nearest [int/create-guide-index-map.md]. Guide Distance grande, poucas guias,
mechas grandes.

**Existing Guide Map.** Ligado por padrão, faz o Clump reaproveitar o atributo
`guide_curve_index` que já esteja na geometria [int/clump-hair-curves.md,
Named Attribute "guide_curve_index"]. É assim que dois Clumps seguidos podem
usar guias diferentes: um Create Guide Index Map antes de cada um grava um
mapa novo.

**O sentinela -987654.** É o valor "não fornecido" do input Guide Index. Se
você mexer nele no painel, o clump some. Esse input existe para a versão em
nodes, não para o modificador [com/devtalk-27601-...md, posts 9 e 11].

**Group ID no Create Guide Index Map.** Entrada inteira que agrupa curvas para
a criação do mapa [int/create-guide-index-map.md]. Mesmo inteiro do region map
da interpolação, e clump nunca atravessa uma risca.

**Parâmetros que fazem diferença** [manual/modeling/geometry_nodes/hair/guides/clump_hair_curves.rst]:

- Factor: 1,0 é convergência total. Nível 1 alto, nível 2 mais baixo.
- Shape: 0 constante, 0,5 linear raiz-ponta. Cabelo real converge mais na
  ponta, então Shape positivo.
- Tip Spread: impede que as pontas se juntem num ponto só. Sempre um pouco.
- Clump Offset: desloca cada mecha numa direção aleatória. Quebra o padrão
  radial.
- Distance Falloff e Threshold: limitam a influência de cada guia por
  distância. Sem eles, guia longe puxa curva longe.
- Preserve Length: ligue, senão a mecha encurta ao convergir.

Uma limitação apontada em 2022 e ainda válida: não há operação nativa "sobre a
mecha inteira", como enrolar um clump como unidade. É por curva
[com/devtalk-24686-...md, post 9].

---

## 6. Noise, Frizz e flyaways

Os dois parecem iguais no painel e não são [int/hair-curves-noise.md;
int/frizz-hair-curves.md]:

- **Hair Curves Noise** amostra uma textura de ruído pela posição da raiz.
  Curvas vizinhas recebem deslocamento parecido. Scale controla o tamanho da
  onda no espaço; Scale along Curve, ao longo do fio; Offset per Curve quebra
  a coerência entre fios. É ondulação, não crespo.
- **Frizz Hair Curves** desloca cada ponto aleatoriamente. Vizinhas não se
  parecem. É crespo.
- Ambos têm Cumulative Offset: ligado, cada ponto herda o deslocamento dos
  anteriores e a curva vai se afastando da forma original. Desligado, é
  tremor local.
- Ambos expõem Offset Vector como saída, para reaproveitar o deslocamento em
  outro node.

**Flyaways.** Não há node. A receita que aparece nas fontes: duplicar o Trim
ou o Frizz e ligar um Random Value na Selection, com probabilidade de 0,1 a
0,5, Length Factor 1,5 a 1,8 e Random Offset 0,3 m no caso de fur
[jp/ja-tenp-kukan-2025-10-hair-curves-fur.md]. Ou seja: uma fração das
curvas recebe Frizz forte e comprimento maior. Alternativa: um objeto Curves
separado só de flyaways, com Duplicate Hair Curves e densidade baixa.

---

## 7. Comprimento, raio e perfil

**Trim Hair Curves** [int/trim-hair-curves.md]. Dois modos: Replace Length
(comprimento absoluto) ou Length Factor (multiplica o original). Random Offset
dá a variação de comprimento sem a qual toda ponta fica na mesma linha. Pin at
Parameter segura a curva num ponto do comprimento. Mask aceita field, então
um atributo pintado vira mapa de comprimento.

**Set Hair Curve Profile** [int/set-hair-curve-profile.md]. Radius é o raio de
base; Shape e Factor Min/Max desenham o afinamento raiz-ponta. Valores usados
nas fontes: 0,003 m corpo de gato, 0,001 m dentro da orelha, 0,01 m bigode com
Shape 0,8; sobrancelha 0,01 m para afinar ponta
[jp/ja-tenp-kukan-2025-10-hair-curves-fur.md;
jp/ja-tenp-kukan-2025-11-hair-curves-textura-sobrancelha.md]. Para cabelo
humano em escala real, o raio é bem menor; comece em 0,0003 m e ajuste pelo
render, não pelo viewport. Quanto mais fino, mais curvas você precisa, e mais
caro o render [com/blenderartists-1563512-blender-4-2-hair.md, post 4].

**Perfil simétrico só no Cycles.** EEVEE e Workbench não renderizam raio
arbitrário por ponto; por isso o profile foi desenhado para o que os dois
suportam [com/devtalk-27601-...md, post 1].

---

## 8. Máscaras e atributos

Tudo que é float no painel aceita field. A regra do sistema é: pinte no scalp,
leia com Named Attribute, ligue no input.

- **Onde pintar.** Vertex group ou color attribute no scalp. O Interpolate
  propaga atributos da superfície para os filhos; foi o motivo de a guia
  original ser trocada pelo filho mais próximo [com/devtalk-27601-...md,
  post 5].
- **Density Mask** e **Guide Mask**: float 0 a 1. Guide Mask define quem pode
  virar guia de clump [int/create-guide-index-map.md].
- **Por curva.** Atributos booleanos por curva (Top_Guides_01 e afins)
  marcam grupos de guias. Named Attribute, Separate Geometry, e cada grupo
  ganha sua faixa da stack. Quando as faixas se repetem, é hora de um node
  group com parâmetros, ou de um inteiro `region` num For Each.
- **Textura que não aparece nas curvas.** Problema conhecido com solução
  documentada em japonês [jp/ja-tenp-kukan-2025-10-hair-curves-problema-textura-nao-aparece.md].

---

## 9. Animação e deformação

- Deform Curves on Surface no fim da stack, Surface Rest Position ligado no
  Interpolate [jp/ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md].
- Shrinkwrap Hair Curves depois de qualquer deformação que possa empurrar
  ponto para dentro da pele: Offset Distance, Above Surface, Smoothing Steps,
  Lock Roots [int/shrinkwrap-hair-curves.md]. Foi pedido por Bystedt para fur
  molhado e para "empurrar para fora o que ficou embaixo"
  [com/devtalk-27601-...md, post 9].
- Subdivision no scalp: ver seção 4.

---

## 10. Simulação

**5.2 tem física de hair, experimental por rótulo oficial.** Hair Dynamics é
um node group sobre o XPBD Solver, com modos Animation e Physics. Exige mesh
de superfície e o modificador Capture Rest Geometry, que o operador Empty Hair
já adiciona [dev/devdocs-5.2-physics.md; dev/code-blender-2026-07-geometry-nodes-physics.md].

Parâmetros [manual/modeling/geometry_nodes/simulation/hair_dynamics.rst]:
Substeps, Constraint Iterations, Time Scale, Mass, Friction, Stretchiness
(1 = até dez vezes o comprimento sob gravidade), Bendiness, Root Bendiness,
Structure Randomness, Damping linear e angular, Surface Collision.

**O que quebra, segundo quem testou** [com/devtalk-45449-...md]:

- Attach à superfície umas duas vezes mais lento que o Surface Deform antigo.
- Cabelo dentro de collider em rest explode. Não há collision offset; a
  gambiarra é Shrinkwrap depois da sim.
- Escala do objeto propaga errado: curva em 0,1 fica dez vezes mais longa.
- Regenerar filhos a cada frame dá jitter. Simule guias e gere filhos depois,
  o que era o pedido de 2022 e continua sendo o desenho recomendado
  [com/devtalk-24686-...md, post 5].
- Pontos mal distribuídos ao longo da curva dão resultado estranho. Passe um
  Redistribute Curve Points antes.

**Antes da 5.2, e ainda o plano B.** Proxy mesh gerado das curvas, Cloth no
proxy com vertex groups, Surface Deform devolvendo o movimento às curvas
[com/blenderartists-1407111-rig-and-simulate-hair-curves-blender-3-3.md].

**Por que é assim.** O solver foi escolhido no workshop de outubro de 2024, e
o problema aberto de guide mapping, guardar de forma robusta qual filho segue
qual guia, é o que torna simulação por guias pouco confiável
[dev/code-blender-2024-11-geometry-nodes-workshop-october-2024.md].

---

## 11. Shading no Cycles

Principled Hair BSDF [manual/render/shader_nodes/shader/hair_principled.rst;
jp/ja-tenp-kukan-2025-09-principled-hair-bsdf-material.md]:

- **Cor.** Melanin Concentration é o modo realista: Melanin (quantidade) e
  Melanin Redness (proporção feomelanina). Tint por cima para tingido. Direct
  Coloring converte RGB em absorção e é menos previsível.
- **Random Color e Random Roughness.** O manual é explícito: cabelo realista
  precisa de variação entre fios. Sempre algum valor.
- **Modelo.** Chiang é o padrão; Huang, desde a 4.0, aceita seção elíptica via
  Aspect Ratio (0,5 a 1,0 conforme o tipo de cabelo) e desde a 4.2 alterna
  near e far field pela distância de câmera [dev/devdocs-4.0-cycles-principled-hair-huang.md;
  dev/devdocs-4.2-cycles-huang-hair.md]. Huang pode ficar lento em roughness
  baixo e "achatado" em close.
- **Valores de partida** para cabelo preto: Melanin 0,859, Redness 0,145,
  Roughness 0,223, Radial Roughness 0,355. Fur de gato: Roughness 0,7, Radial
  0,3 a 0,5, Random Roughness 0,1 a 0,2 [jp/...principled-hair-bsdf-material.md;
  jp/...hair-curves-fur.md].
- **Gradiente raiz-ponta e variação por fio.** Curve Info no shader: Intercept
  para raiz-ponta, Random para variar por fio. É o mesmo par usado para gerar
  texturas de sobrancelha por AOV [jp/ja-tenp-kukan-2025-11-hair-curves-textura-sobrancelha.md].
- **EEVEE não tem shader de hair.** Só Cycles [com/blenderartists-1563512-...md,
  post 4]. Para preview no EEVEE, Curve Shape Strip e Additional Subdivision 3
  [jp/...textura-sobrancelha.md].

---

## 12. Performance

- Viewport Amount no Interpolate: 0,1 a 0,3 enquanto pentear, 1,0 para render.
- Densidade real por objeto, não global. Corpo de gato 10.000 e mais; volume
  extra em pescoço 50.000 [jp/ja-tenp-kukan-2025-10-hair-curves-fur.md].
  Um cavalo precisou de 3,5 milhões de filhos onde partículas usavam 1,6
  milhão, porque a distribuição é por área, não por guia
  [com/blenderartists-1460445-...md, post 7]. Use Distance to Guides e
  Density Mask para não gastar densidade onde não aparece.
- Desligue os modificadores de deformação enquanto esculpe guias; ligue no
  fim. Afro é a pilha mais cara: Clump, Noise, Curl e Roll juntos
  [jp/ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md].
- Reduza pontos por curva. Cada ponto é geometria no render.

---

## 13. Export

- **Alembic e USD** aceitam o objeto hair curves em import e export desde a
  4.2 [dev/devdocs-4.2-pipeline-assets-io-hair-curves.md]. USD ainda não
  exporta cor por fio nem UV [manual/files/import_export/usd.rst].
- **Unreal.** O Alembic nativo não escreve o schema Groom que a Unreal espera;
  o fluxo documentado desabilita filhos e dynamics antes de exportar, aplica
  transforms, exporta com dados de curva e liga o plugin Groom na Unreal
  [com/irendering-2026-01-integrating-blender-hair-into-unreal-groom.md].
  Fazer o schema sem ferramenta de terceiro é escrever um exportador.
- **Hair cards a partir de curvas**, mantendo o groom editável: é o tema da
  palestra da Sara Matsumoto na BCON 2024 [dev/conf-blender-2024-1990-...md].
  A Essentials não tem esse node; é Geometry Nodes seu.

---

## 14. Problemas comuns

| Sintoma | Causa provável | O que fazer | Fonte |
|---|---|---|---|
| Interpolate não gera nada | Surface não atribuída, UV map errado, ou Rest Position sem malha em repouso | Conferir Surface e Surface UV Map no Interpolate; testar com Rest Position desligado | jp/ja-tenp-kukan-2025-11-hair-curves-guia-completo.md |
| Filhos atravessam a pele | Guias esculpidas sem colisão; ruído empurrou para dentro | Shrinkwrap Hair Curves no fim; Use Sculpt Collision ao pentear | int/shrinkwrap-hair-curves.md |
| Filhos flutuam ou entram na malha subdividida | Subdivision Surface não aplicado no scalp | Aplicar o Subdivision no scalp, ou scalp separado | com/blenderartists-1621672-...md |
| "Invalid surface UVs on N curves" | UV Smooth do Subdivision | UV Smooth = None no Subdivision | com/blenderartists-1621672-...md, post 9 |
| Cabelo pula ao mudar densidade | Guia promovida muda de ID | Definir densidade cedo; versões atuais já estabilizam o ID | com/devtalk-27601-...md, posts 5 e 7 |
| Clump sumiu | Mexeu no Guide Index (-987654) | Voltar ao sentinela; usar Guide Distance e Existing Guide Map | com/devtalk-27601-...md, post 11 |
| Viewport travando | Densidade alta com deformadores ligados | Viewport Amount baixo; desligar deformadores ao esculpir; dividir em objetos | com/blenderartists-1460445-...md |
| Pincel não faz nada | Use Sculpt Collision em malha densa | Desligar colisão, resolver com Shrinkwrap depois | com/blenderartists-1460445-...md |
| Textura não aparece nas curvas | Mapeamento de UV das curvas | Ver post dedicado | jp/ja-tenp-kukan-2025-10-hair-curves-problema-textura-nao-aparece.md |
| Sim explode | Curva dentro de collider em rest; escala do objeto | Shrinkwrap antes; aplicar escala | com/devtalk-45449-...md |
| Sim com jitter | Filhos regenerados por frame | Simular guias, interpolar depois | com/devtalk-45449-...md |

---

## 15. O que o Blender ainda não faz

- Esconder guias no Sculpt. Test build em revisão [com/devtalk-44094-...md].
- Region map exposto no Interpolate. Só Part by Mesh Islands; o resto é abrir
  o grupo [int/interpolate-hair-curves.md].
- Operar sobre uma mecha como unidade [com/devtalk-24686-...md, post 9].
- Guide mapping robusto para simulação [dev/code-blender-2024-11-...md].
- Subdivision no scalp sem aplicar [com/blenderartists-1621672-...md].
- Collision offset na física [com/devtalk-45449-...md].
- Schema Groom da Unreal no Alembic nativo [com/irendering-2026-01-...md].
- Física estável: rótulo experimental e aviso de que o design pode mudar
  [manual/modeling/geometry_nodes/simulation/hair_dynamics.rst].

---

## 16. Como este cérebro cresce

Quando você trouxer um problema novo, a resposta entra aqui com a fonte. Se a
fonte for a sua própria experiência, entra marcada como "observado em
produção" com a data e a versão do Blender. É assim que isso vira melhor que
qualquer tutorial: registro do que funcionou no seu groom, não no de um vídeo.

Pastas: `essentials-internals/` para o que cada node faz por dentro;
`blender-dev/` para o que os devs decidiram e por quê; `comunidade/` para o
que quebra na prática; `blogs-jp-zh/` para valores e receitas; `palestras/`
para transcrições da Blender Conference, quando houver legenda.
