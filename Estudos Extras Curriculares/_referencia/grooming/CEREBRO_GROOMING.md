# Cérebro de grooming: hair curves + Geometry Nodes no Blender 5.2

Síntese de trabalho, escrita a partir das fontes desta pasta. Cada afirmação
aponta o arquivo de onde veio, em `[colchetes]`. O que não tem colchete é
julgamento meu e deve ser tratado como opinião de quem leu tudo isso, não como
fonte. Última revisão: 2026-09-26, com as transcrições das palestras incorporadas.

Caminhos abreviados:
`manual/` = `../blender-manual-5.2-lts/manual/`,
`api/` = `../blender-python-api-5.2/api/`,
`int/` = `essentials-internals/`, `dev/` = `blender-dev/`,
`com/` = `comunidade/`, `jp/` = `blogs-jp-zh/`, `pal/` = `palestras/`.

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

## 2b. Como quem faz groom de verdade trabalha

Isto vem das transcrições das palestras da Blender Conference, de artistas
que entregaram groom realista em produção com hair curves. É a parte mais
valiosa da base, porque ninguém escreve isso em manual.

**Prepare o scalp antes de qualquer guia**
[pal/bcon2023-daniel-bystedt-...md; pal/bcon2025-kerstin-schmidbauer-...md]:

- **Hair cap**: uma malha de crescimento separada da cabeça, para o groom não
  depender da topologia nem da densidade do personagem. É ela que entra como
  Surface nos modificadores.
- **Topologia e UV fechadas antes do groom.** As curvas vivem no espaço UV.
  UV sobreposta dá "Invalid Surface UVs"; UDIM pode, overlap não. Costura
  central "quase fundida" por espelhamento se resolve com Merge by Distance no
  editor de UV.
- **Risca**: vertex group marcando a linha da risca e uma hard edge dividindo
  a cap em duas metades. Isso é o que faz a interpolação respeitar a risca.
- **Referência por subespécie e estação**, antes de abrir o Blender. Misturar
  fotos de indivíduos, regiões ou estações diferentes dá um híbrido que não
  convence. Desenhe por cima da referência onde o pelo muda de tipo e a
  direção, para não decidir isso já em 3D.

**Esculpir guias**
[pal/bcon2023-daniel-bystedt-...md; pal/bcon2025-kerstin-schmidbauer-...md]:

- Comece com **2 pontos por guia** para definir direção no corpo inteiro;
  suba para 3, e só cabelo comprido precisa de 8. Guia de 8 pontos no início
  se emaranha e atravessa a malha. Quando precisar de forma detalhada, Resample
  Curve para 15 pontos e aplique.
- Comb em modo **Projected**, não esférico, para pentear atrás sem a esfera
  bloquear.
- **Scale Uniform desligado** no Grow: o fio continua na direção existente em
  vez de escalar da raiz.
- Paint Selection em modo **Curve** para selecionar fio inteiro; serve para
  encher comprimento de uma área e ajustar depois.
- Guia nova com nada selecionado nasce sozinha selecionada: penteie a direção
  dela antes que as vizinhas comecem a interpolar.
- Densidade de guias **uniforme e sem buraco**. Buraco vira careca, e
  deformação de rig amplia o buraco. Excesso vira blob e render lento.
- Guia presa dentro da malha em área fina: Puff; se não sair, apague e
  recrie. "Não lute contra o sistema."
- Mudou topologia depois do groom: **Snap to Nearest Surface** no Sculpt
  resolve quase tudo.

**Organização do groom**
[pal/bcon2026-steve-chow-...md; pal/bcon2025-kerstin-schmidbauer-...md]:

- Regiões por **grandes formas**, não por variação. Um gato inteiro em duas
  regiões, cabeça e corpo, com a linha de corte atrás das bochechas seguindo a
  estrutura do modelo. Os modificadores cuidam de densidade, espessura e forma;
  no sistema antigo cada variação exigia mais uma camada.
- Região por **vertex group**, não por textura: é dado do próprio modelo e não
  quebra quando o arquivo muda de lugar. Textura só onde precisa de resolução
  maior que a malha.
- Muitos vertex groups por região e por efeito é normal. Desligue o
  Interpolate enquanto pinta pesos.
- **Pinte em camadas coloridas** para depurar: Store Named Attribute por
  camada, cor no shader, e você enxerga onde cada clump está. O mesmo truque
  serviu para discutir o groom com cliente por e-mail.

**A ordem que funcionou em produção**
[pal/bcon2026-steve-chow-...md; pal/bcon2023-daniel-bystedt-...md]:

- Corpo de gato: **Clump, depois Curl, depois Frizz**. Muitos clumps, cada um
  suave; ponta afiada lê como falso na hora. Frizz por último e sutil; forte
  fica sujo.
- **Existing Guide Map desligado no Clump e no Curl** (relato do Chow). Ele
  desligou só no Clump e o Curl seguiu as guias esparsas antigas, dando
  "permanente" indesejado. Com o toggle desligado, a densidade dos clumps sai
  da Guide Distance, sem plantar guia à mão.
  **Medido na 5.2.2 (2026-09-28, t_chow.py), o caso não se reproduz**: com um
  mapa esparso antigo na geometria (6 guias), o Clump com Existing desligado
  (GD 0,02) regrava o atributo com o mapa dele (117), e o Curl com Existing
  **ligado** usa esses 117. Ou seja: na 5.2, Clump → Curl com Existing ligado
  é o que faz o cacho acompanhar a mecha (17.3). O risco agora é o contrário:
  **Curl com Existing desligado cria o próprio mapa com o Guide Distance
  padrão de 0,1**, poucas guias, e aí sim dá "permanente". Se desligar no
  Curl, iguale o Guide Distance ao do Clump.
- Bystedt usou **duas camadas de clump**, largo e fino, cada uma com seu
  seed e seu ruído, para não sobrepor igual.
- Noise com **Offset per Curve ligado** e escala reduzida ao longo da curva
  para não estourar o comprimento. Roll na ponta, porque cabelo real não
  termina reto.
- Trim com **aleatoriedade de comprimento** é citado por dois palestrantes como
  o que separa real de uniforme.
- Modificador de comprimento na posição errada da stack quebra tudo que vem
  depois, em silêncio.

**Fendas no pelo** [pal/bcon2026-steve-chow-...md]: onde a pele estica, o pelo
abre. Sem isso o gato vira pelúcia. Trim controlado por **textura** pintada,
porque vertex weight fica grosseiro na densidade da malha. Quatro regras
juntas: distribuição aleatória, comprimentos variados, ponta afunilada em
diamante, curvatura variada. Armadilha: ligar a textura no painel não faz
nada; tem que entrar no editor e ligar no input certo.

**Undercoat e topcoat** [pal/bcon2026-steve-chow-...md]: gato tem duas
pelagens. O topcoat, mais longo, mais aleatório e com muito menos fios, entra
só depois que o shader do undercoat fechou, senão é retrabalho. Ele existe
para suavizar a silhueta e dar a borda fofa. "Seis milhões de fios bagunçados
não são melhores que seis mil com camadas boas."

**Densidade por textura** [pal/bcon2023-daniel-bystedt-...md]: mapa pintado
com branco denso, cinza 50% base, preto sem cabelo, ligado no Density Mask
por Image Texture, Named Attribute do UV e Color Ramp cortando logo acima de
0,5. Mais um multiplicador global de densidade exposto no modificador, para
baixar tudo quando a cena pesa.

**A risca** [pal/bcon2023-daniel-bystedt-...md]: copie a cap, apague tudo
menos a linha central pelo peso "Parting Center", e cole as raízes próximas
nessa linha com Mix. Para o volume que sobe na risca: Deform Curves on Surface
com Surface Normal Displacement, dirigido por Geometry Proximity até a linha
central, Map Range e Float Curve, sem mexer nas raízes exatas.

**Shading de pelo denso** [pal/bcon2026-steve-chow-...md]: camada interna
escurece e parece sujeira. Transparent BSDF misturado por Light Path para a
sombra ficar um pouco transparente. Gradiente raiz-ponta por cima. Se o
viewport não atualizar depois de mexer no shader, alterne Solid e Rendered.

**Groom como entrega de produção** [pal/bcon2026-christopher-strommer-...md]:
variações de groom para o cliente escolher à distância; fios soltos de
propósito para pegar luz de contraluz; passes de cabelo com hold-out, com
Shadow Catcher e sem hold-out para a composição; crescimento de cabelo é um
keyframe de 15 frames no Trim.

**Hair cards a partir do groom** [pal/bcon2024-sara-matsumoto-...md]: mecha
renderizada em câmera ortográfica gera as texturas; Curve to Mesh com perfil
Arc de 3 lados para card e Spiral para tubo; Curve Tangent no Tilt para o card
seguir a superfície; UV construída com Capture Attribute e Store Named
Attribute; raiz colada por Geometry Proximity. O resultado continua editável
com os mesmos pincéis e assets. A palestrante passou a preferir mesh a curvas
para render de personagem completo, por estabilidade e tempo.

**Shape key de cabelo** [pal/bcon2025-kerstin-schmidbauer-...md]: não existe
nativo. Set Position com Mix entre a Position de dois objetos de cabelo por
Sample Index, fator num driver. Quebra se a contagem de curvas mudar.

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

**Dois Clumps em fila, testado em bpy 5.2.2 (2026-09-28, 1600 fios retos
em grade, script test_2clumps.py).** O usuário reportou que "mecha dentro da
mecha" com dois Clumps não funcionava na 5.2. Confirmado, e a causa é dupla:

- O Clump **grava** `guide_curve_index` na saída (o Create Guide Index Map
  interno tem um Store Named Attribute). Então o segundo Clump, com Existing
  Guide Map ligado (padrão), reaproveita as guias do primeiro e o resultado é
  idêntico ao primeiro sozinho: diferença máxima de posição 0,0.
- Com Factor 1,0 no primeiro, as pontas já convergiram; o segundo, mesmo com
  Existing Guide Map desligado, só troca fios de mecha (saltos de até 15 cm),
  sem criar sub-mechas: 108 grupos antes, 108 depois.

O que funciona: **Clump grande com Factor 0,5** (Guide Distance 0,08), depois
**Clump pequeno com Factor 1,0, Guide Distance 0,02, Existing Guide Map
desligado, Seed diferente**. Resultado: 1043 grupos a 5 mm dentro de 495
grupos a 3 cm. Ordem inversa (pequeno antes, grande depois com Factor 0,5 e
Existing desligado) dá hierarquia parecida. A regra: o primeiro nível nunca
fecha tudo, e o segundo nível sempre ignora o mapa herdado.

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

**Observado em produção (2026-09-27, Blender 5.2 LTS)**: Image Texture com
Named Attribute do UV ligado no Density Mask, sobre um plano de uma face só,
gerou zero fios. Causa: o Density Mask entra no Density Factor do Distribute
Points on Faces [int/interpolate-hair-curves.md, ligação 227] e esse campo é
avaliado nos cantos das faces e interpolado dentro delas. Com a mancha branca
no meio da imagem, os quatro cantos leem preto e a face inteira vale zero.
Regra: Density Mask tem resolução de vértice (bom para vertex group); imagem
com detalhe vai no slot **Mask Texture** (ícone de imagem abaixo do Density
Mask), que amostra por ponto depois da distribuição e não depende da malha
[manual interpolate_hair_curves.rst, dica em Mask Texture]. Os dois se
multiplicam. O UV do Mask Texture vem do Surface UV Map do objeto Curves.

**Observado em produção (2026-09-27, Blender 5.2 LTS): máscara por imagem
com cadeia de nodes.** Os inputs Surface, Surface UV Map e Surface Input Type
não existem mais no Interpolate Hair Curves da 5.2.2 [int/interpolate-hair-
curves.md, interface]: o node lê o scalp e a UV do bundle de attachment do
próprio objeto Curves, pelo grupo interno Get Hair Surface Geometry (campos
Surface e Surface UV Map em Object Data, os mesmos do Ctrl+P). O Generate Hair
Curves mantém um menu Surface Source (Attached ou Object) [int/generate-hair-
curves.md; manual generate_hair_curves.rst]. Campos do objeto: manual
curves_new/properties.rst, seção Surface. O jeito de sampler uma imagem por fio com cadeia livre de
nodes, testado e funcionando:

1. Interpolate com Density Mask 1.0 e Mask Texture vazio.
2. Depois dele, Named Attribute (Vector) `surface_uv_coordinate`. Esse é o
   atributo oficial de fixação no scalp, gravado em todo filho pelo Interpolate
   [int/interpolate-hair-curves.md, Store Named Attribute `surface_uv_coordinate`, domínio Curve].
3. Attribute -> Vector do Image Texture.
4. Color -> cadeia livre (Color Ramp, Math, Mix, Separate Color para R, G e B
   como três máscaras).
5. Resultado -> Random Value (Boolean) em Probability -> Delete Geometry
   (Curve) em Selection. Boolean Math NOT antes se branco deve manter.

A mesma Named Attribute alimenta Trim, Clump, Frizz, Curl e raio: qualquer
parâmetro por fio vira textura. Se a UV do scalp mudar, rodar Snap to Nearest
Surface nas guias [manual curves_new/properties.rst, linha 44].

## 8b. Fields: o que foi testado em bpy 5.0.1 (2026-09-27)

Observado em teste headless, nao em fonte externa:

- **Vertex group pintado no scalp atravessa o Interpolate Hair Curves** e
  aparece nos filhos como atributo float no dominio de curva, com o mesmo
  nome e os valores 0 a 1 preservados. Named Attribute com o nome do grupo,
  depois do Interpolate, e o caminho de mascara mais simples.
- **Curve Info (Essentials) → Random** funciona nos filhos: um valor 0 a 1 por
  curva. Com Map Range vira variacao de qualquer float input.
  **Observado em producao (2026-09-27, 5.2 LTS)**: e o padrao do Blender
  Studio para randomizar Factor e Shape do Clump (e Curl, Trim): Curve Info
  Random → Map Range (ex. 0,4 a 1,0) → Factor. Refeito em bpy 5.2.2
  (2026-09-28): Curve Info fica em Add > Hair > Read; Map Range com Clamp;
  Factor fixo 1 deixa todas as mechas pontudas e iguais, 0,4 a 1,0 solta
  fios, 0 a 1 vira frizz [img/121_clump_random_sheet, 121_clump_random_nodes;
  scripts/r121_clump_random.py].
  **So nas pontas** (2026-09-28, bpy 5.2.2): o Factor do Clump e avaliado por
  ponto (multiplica a curva do Shape antes do Mix, ver
  essentials-internals/clump-hair-curves.md), entao aceita mascara ao longo
  do fio. Spline Parameter → Map Range (From 0,6 a 1,0) → Factor de um Mix
  Float; A = 1; B = Curve Info Random → Map Range (To 0,3 a 1,0); Mix →
  Factor do Clump. Corpo fechado, cada ponta solta de um jeito. Sem node:
  **Tip Spread** (6 mm) abre as pontas. **Curve Tip nao serve**: Tip
  Selection marca so o ultimo ponto, o cone continua igual
  [img/122_clump_pontas_sheet, 122_clump_pontas_nodes].
- **Atributo de cor** (2026-09-28, bpy 5.2.2): Store Named Attribute tipo
  **Color**, dominio Spline (uma cor por fio, ex. Curve Info Random → Color
  Ramp) ou Point (varia no fio, ex. Spline Parameter → Color Ramp), Name
  `cor`. No material: Attribute Type **Geometry**, mesmo nome → Color do
  Principled Hair BSDF em Direct Coloring. Direct Coloring clareia: use tons
  mais escuros [img/124_cor_atributo_sheet, 124_cor_atributo_nodes].
- **Edit Mode sempre mostra as guias originais** (2026-09-28): Delete ou
  Separate Geometry no modificador nao escondem nada no Edit Mode. E o
  Curves de cabelo **nao tem Hide/Reveal** na 5.2 (bpy.ops.curves sem hide;
  manual modeling/curves_new sem Show/Hide; o Hide de curve.rst e do Curve
  antigo). Duas saidas nativas:
  1. Node tool "Selecionar Conjunto": Named Attribute (Boolean, Name do
     input) → **Set Selection** (Spline) → Output; Identifier
     `curves.selecionar_conjunto`, Modes Edit e Sculpt
     [img/125_tool_selecionar_conjunto]. Nao executado aqui (sem UI).
  2. Conjuntos em objetos Curves separados, mesmo scalp: no objeto
     principal, Object Info (Relative) de cada conjunto → Join Geometry com a
     propria geometria → Interpolate. Testado em bpy 5.2.2: 53 + 107 guias em
     dois objetos deram 15.495 filhos, igual a um objeto so. Edita um objeto
     por vez (Local View, tecla /). Por fio, sem Create Guide
  Index Map; da o visual de fios escapando da mecha. Random por mecha (Random
  Value com ID = Guide Index) e outro efeito, mais raro. Tip Spread e Clump
  Offset ja sao aleatorios por dentro, so o Seed do Clump. Para ver em cores:
  Map Range → Color Ramp → Viewer (Ctrl+Shift+clique), com a geometria do
  Viewer vinda da saida do Clump. Curve Info nao tem Seed: Math Add + Fraction
  antes do Map Range, ou Random Value com ID vazio e Seed.
- **Named Attribute nao le `.selection`.** Atributo interno com ponto no nome
  volta zero. A selecao do Sculpt nao entra no tree diretamente.
- **Selecao da viewport so entra por node tool** (2026-09-28). O node
  Selection so existe no Tool context [manual/modeling/geometry_nodes/tools.rst;
  geometry/read/selection.rst]. Receita "Salvar Selecao": editor em Tool,
  Usage Tool, modo Edit, tipo Curves; Group Input (Geometry, string Nome) →
  Store Named Attribute (Boolean, Curve) com Value = Selection → Output.
  Roda em Edit Mode pelo menu **so com icone** no fim do header da
  viewport, depois de Segments (ICON_FILE_HIDDEN, secao "Non-Assets";
  node_group_operator.cc da 5.2). So aparece com Types = Curves e Modes =
  Edit marcados nos popovers do header do editor. O input Name precisa de
  Default preenchido, senao roda sem gravar; o Nome tambem aparece no redo.
  Erros vistos com o Vini: Selection ligado no socket Selection do Store em
  vez do Value, e Store em Float.
  **Causa real de "nao aparece" (5.2.0 e 5.2.2):** o tool local precisa do
  **Identifier** no popover Options do header do editor (propriedade
  `node_tool_idname`). Vazio, o grupo nao e registrado como operador e o
  painel mostra "Missing operator identifier" [node_group_operator.cc,
  custom_idname_for_group; space_node.py; conferido na tag v5.2.0]. Formato:
  minusculas, numeros e _, exatamente um ponto, ex. `curves.salvar_selecao`
  [wm_operators.cc, operator_idname_ok_or_report_impl]. Grupo novo via API
  nasce com o campo vazio (bpy 5.2.2). Cada
  execucao substitui o conjunto; para somar, Boolean Math OR com o Named
  Attribute antigo. Diagrama: laboratorio/img/118_node_tool_selecao.png.
  Nao executado aqui: o operador de node tool nao existe no bpy headless.
- **Curves > Set Attribute** (bpy.ops.curves.attribute_set) so funciona em
  Edit Mode, e grava valor cheio em tudo que estava selecionado, inclusive
  ponto com selecao 0,4. E mascara dura. Mascara suave nas proprias curvas so
  vem do scalp (Weight Paint) ou do addon Groom Select desta pasta.
- **Move to Nodes** existe como `bpy.ops.object.geometry_nodes_move_to_nodes`
  e no menu do modificador [manual/modeling/modifiers/introduction.rst].
- Suave e duro em qualquer modo de pintura e a curva de **Falloff** do pincel
  (Smoother ate Constant, ou Custom); Hardness separado so existe no Sculpt
  de malha [manual/sculpt_paint/brush/falloff.rst;
  manual/sculpt_paint/brush/brush_settings.rst].

---

## 9. Animação e deformação

- Deform Curves on Surface no fim da stack, Surface Rest Position ligado no
  Interpolate [jp/ja-tenp-kukan-2025-09-hair-curves-nodes-geometria.md].
  Medido na 5.2.2 (lab 17.46): no fim gruda a raiz (0,06 mm); nas guias antes
  do Interpolate não segura (12,6 mm). No 5.2 o socket chama "Resting
  Surface" e vem ligado.
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
| Density não passa de 10.000 no painel; cabeça real fica rala | Campo do Interpolate com máximo 10.000 fios/m² | Value node ligado no socket Density (ou GR Densidade Livre) | lab 17.1 |
| Cacho quase não aparece | Curl dá 3 × Frequency voltas por metro; em escala real Frequency 1 é menos de uma volta | Frequency ≈ voltas/m ÷ 3 (Merida ≈ 9 a 10) | lab 17.1, 17.3 |
| Cacho vira cilindro liso | Frequency variando por fio; a hélice vem da guia | Frequency fixa ou por mecha (ID = guide_curve_index); Radius pode variar por fio | lab 17.3 |
| Variação "por fio" sai como ruído, fita enrugada | Random Value sem ID num input de ponto sorteia por ponto | Evaluate on Domain (Curve) depois do Random Value | lab 17.3, 17.11 |
| Mechas mudam de lugar depois de mexer no scalp | Remesh/Decimate/Triangulate mudam a ordem das faces, que semeia a distribuição | Fechar a topologia do scalp antes de pentear | lab 17.38 |
| Fios descem ou somem com Raycast na malha | Raiz fora da malha | A malha tem que conter todo o scalp | lab 17.40 |
| Cabeça atravessa o cabelo na animação | Sem Deform Curves on Surface, ou ele antes do Interpolate | Deform no fim da cadeia; Add Rest Position no scalp | lab 17.46 |
| Padrão de cor escorrega quando anima | Textura por Position lida depois do Deform | Calcular antes do Deform ou usar surface_uv_coordinate | lab 17.46 |
| Contorno (casca invertida) deixa tudo preto | A casca bloqueia os raios de sombra | Factor = Maximum(Backfacing, 1 − Is Camera Ray) | lab 17.47 |
| Groom de repente pesado (segundos por avaliação) | Roll/Ponta Virada depois do Curl, com Subdivision 2: pontos × 4 | Ponta Virada antes de Onda e Cacho, Subdivisão 0 ou 1 | lab 17.54 |
| Topo careca ou com ruído depois de trançar | Braid junta o fio inteiro na guia e afunda o trecho do crânio (58% dentro) | Shrinkwrap na cabeça depois do Braid (GR Trança Grossa com Cabeça ligada) | lab 17.61 |
| Groom sumiu inteiro | GR Corte pela Malha sem malha ligada (versão antiga) | Atualize a biblioteca ou ligue a malha | lab 17.62 |
| Cabelo escurece no close de fio grosso | Shape 3D Curves faz sombra entre fios; Ribbons não | Ajuste a cor no Shape do render final; em vista normal a diferença é < 7% | lab 17.68 |
| Interpolate não gera filhos com guias de Grease Pencil ou Curve | Falta o bundle de fixação (surface_geometry/surface_uv_map) | Set Attachment Surface antes; não use Attach Hair Curves (1 ponto) | lab 17.71 |
| Grupos GR quebrados ao abrir em outra máquina | Utilitários do Essentials (Curve Root, Rest Surface...) vieram linkados com caminho da instalação | Tornar local antes de salvar (feito na biblioteca do laboratório) | lab 17.72 |
| Cabeça inteira vira uma trança só | GR Trança Grossa antiga com Guide Distance fixo 0,3 m | Use o Tamanho da trança (~1,5 cm) | lab 17.75 |
| Cabelo cai para o lado errado em cabeça inclinada | Gravidade das guias procedurais é o −Z do objeto | Modele a cabeça em pé; em cena, física ou Simulation to World | lab 17.87 |
| Cópias do personagem carecas ou com o mesmo cabelo | Alt+D compartilha o Surface (cabelo vai para a cabeça original); Collection Instance reusa o mesmo objeto | Shift+D do conjunto e reapontar o Surface | lab 17.59 |
| Strays explodem para cima depois do cacho | Noise/Frizz com Cumulative depois de um node que subdivide | Noise e Frizz cumulativos antes de Curl, Braid e Subdivide | lab 17.7 |
| Cachos seguem poucas guias gigantes, cabelo "some" | Clump com Guide Index ligado grava guide_curve_index com o próprio Guide Distance | Não ligar Guide Index; Create Guide Index Map antes e Clump com Existing Guide Map ligado | lab 17.18 |
| Mecha de malha vira tubo de 1 metro | Curve to Mesh 5.2 com Scale solto ignora o raio do fio | Node Radius no Scale do Curve to Mesh | lab 17.11 |
| Onda S faz trançado em X | Amplitude maior que o tamanho da mecha | Amplitude menor que a mecha (1,5 cm para mechas de 2 cm) | lab 17.19 |
| Ponta enrola de lado com Roll | Roll Direction é para onde a ponta enrola, não o eixo | Roll Direction = ± Root Position | lab 17.20 |
| Displace Hair Curves por normal não faz nada | Precisa do UV do scalp para amostrar a normal | Surface Normal do Interpolate guardada em atributo + Set Position | lab 17.21 |
| Shrinkwrap achata o groom inteiro | Above Surface 0,5 (padrão) puxa também o que está fora | Above Surface 0 para colisão | lab 17.24 |
| Simulação explode no quadro 1 | Guias sem surface_uv_coordinate; ou Surface Collision com o próprio scalp | Snap to Nearest Surface; Collider na cabeça via Effectors Collection | lab 17.25 |
| Penteado estilizado desaba na física | Solver não converge com Substeps 10; Bendiness baixo não basta | Bendiness 0, Root 0, Substeps 40 | lab 17.25 |
| Cabelo não balança quando a cabeça gira | Transform do próprio objeto ligada no Simulation to World | Deixar vazio (espaço de mundo) | lab 17.26 |
| Mola crespa serrilhada | Menos de 8 pontos por volta | Resample antes do Curl, Subdivision 0 | lab 17.28 |
| Smooth deixa o topo careca | Shape 0 alisa a curva da raiz que deita o fio | Shape 0,8, ou Blend Hair Curves | lab 17.34 |
| Coque ou corda vira nuvem | Fase e raio sorteados por fio numa forma coletiva | Valores iguais para o grupo; sorteio só na espessura | lab 17.31 |
| Density Mask por Image Texture não gera nada, ou some tudo | Density Mask é lido nos cantos das faces; malha pobre lê preto nos cantos | Usar o slot Mask Texture do node (amostra por ponto) ou subdividir o scalp; Density Mask só para vertex group | int/interpolate-hair-curves.md; manual interpolate_hair_curves.rst |
| Segundo Clump não cria sub-mechas | Clump grava `guide_curve_index`; o segundo herda o mapa (Existing Guide Map ligado) ou não sobra espalhamento (Factor 1,0 no primeiro) | Primeiro Clump Factor 0,5; segundo com Guide Distance menor, Factor 1,0, Existing Guide Map desligado, Seed diferente | testado bpy 5.2.2, seção 5 |
| Interpolate não gera nada | Surface não atribuída, UV map errado, ou Rest Position sem malha em repouso | Conferir Surface e Surface UV Map no Interpolate; testar com Rest Position desligado | jp/ja-tenp-kukan-2025-11-hair-curves-guia-completo.md |
| Filhos atravessam a pele | Guias esculpidas sem colisão; ruído empurrou para dentro | Shrinkwrap Hair Curves no fim; Use Sculpt Collision ao pentear | int/shrinkwrap-hair-curves.md |
| Filhos flutuam ou entram na malha subdividida | Subdivision Surface não aplicado no scalp | Aplicar o Subdivision no scalp, ou scalp separado | com/blenderartists-1621672-...md |
| "Invalid surface UVs on N curves" | UV Smooth do Subdivision | UV Smooth = None no Subdivision | com/blenderartists-1621672-...md, post 9 |
| Cabelo pula ao mudar densidade | Guia promovida muda de ID | Definir densidade cedo; versões atuais já estabilizam o ID | com/devtalk-27601-...md, posts 5 e 7 |
| Clump sumiu | Mexeu no Guide Index (-987654) | Voltar ao sentinela; usar Guide Distance e Existing Guide Map | com/devtalk-27601-...md, post 11 |
| Viewport travando | Densidade alta com deformadores ligados | Viewport Amount baixo; desligar deformadores ao esculpir; dividir em objetos | com/blenderartists-1460445-...md |
| Pincel não faz nada | Use Sculpt Collision em malha densa | Desligar colisão, resolver com Shrinkwrap depois | com/blenderartists-1460445-...md |
| Textura não aparece nas curvas | Mapeamento de UV das curvas | Ver post dedicado | jp/ja-tenp-kukan-2025-10-hair-curves-problema-textura-nao-aparece.md |
| "Invalid surface UVs" com UV certa | UV sobreposta, ou costura espelhada quase fundida | Sem overlap (UDIM pode); Merge by Distance no UV Editor | pal/bcon2025-kerstin-schmidbauer-...md |
| Careca depois do rig deformar | Buraco na densidade de guias, ampliado pela deformação | Adicionar guias no vazio; densidade de guias uniforme | pal/bcon2025-kerstin-schmidbauer-...md |
| Pelo nascendo dentro da boca | Superfície fina embaixo do pincel de densidade | Separar essa parte da malha; sem superfície, sem pelo | pal/bcon2025-kerstin-schmidbauer-...md |
| Marca escura de comprimento desigual | Grow/Shrink não pegou todos os fios | Apagar e re-adicionar com o pincel Density na área | pal/bcon2025-kerstin-schmidbauer-...md |
| Curvas flutuando após editar topologia | UV intacta, superfície mudou | Snap to Nearest Surface no Sculpt | pal/bcon2025-kerstin-schmidbauer-...md |
| Curl virou "permanente" | Curl seguindo um mapa esparso (antigo, ou o próprio com Guide Distance 0,1) | Na 5.2: Existing Guide Map ligado no Curl logo depois do Clump; se desligar, Guide Distance igual ao do Clump | pal/bcon2026-steve-chow-...md; lab t_chow.py |
| Textura ligada no Trim não faz nada | Input não ligado no editor | Entrar no grupo e ligar a textura no input certo | pal/bcon2026-steve-chow-...md |
| Pelo denso escuro por dentro | Sombra sólida entre camadas | Transparent BSDF por Light Path no shader | pal/bcon2026-steve-chow-...md |
| Sim explode | Curva dentro de collider em rest; escala do objeto | Shrinkwrap antes; aplicar escala | com/devtalk-45449-...md |
| Sim com jitter | Filhos regenerados por frame | Simular guias, interpolar depois | com/devtalk-45449-...md |
| Cílio em fileira única, parece pente | Todos os fios com a mesma direção | Manter a raiz fina e ligar Random Value por curva na Gravidade da GR Guias Procedurais | lab 17.97 |
| Cílio com raiz grossa, parece escova | Scalp largo demais (margem inteira) | Scalp de um loop só, < 1 mm, e densidade maior | lab 17.97 |
| Cílio curto, sumindo para dentro da pálpebra | Normal do scalp para dentro | Recalculate Outside no scalp; conferir com Face Orientation | lab 17.97 |

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

---

## 17. Laboratório: receitas testadas em bpy 5.2.2 (2026-09-28)

**Índice rápido** (a receita completa está na subseção; a biblioteca pronta,
em `laboratorio/receitas_grooming.blend`, 17.19; as regras que mais pesaram
estão resumidas em 17.0):

| Quero | Faça | Onde |
|---|---|---|
| Passar de 10.000 fios/m² | Value node no Density | 17.1 |
| Mecha estilizada, raiz coberta | Clump Shape 0,25, ou Shape 0 + Factor em rampa até 0,3 | 17.2 |
| Cacho definido | Clump → Curl Frequency ≈ voltas/m ÷ 3, Subdivision 2 | 17.3, 17.23 |
| Cacho variando | Random por mecha (ID = `guide_curve_index`); Frequency nunca por fio | 17.3 |
| Onda de desenho | Onda S, amplitude menor que a mecha | 17.4 |
| Cor de desenho | `mecha_rand` por mecha no shader + raiz escura por Intercept | 17.5 |
| Fio solto estilizado | 4% dos fios com Noise cumulativo, **antes** do Curl | 17.6, 17.7 |
| Variações rápidas | Seed mestre | 17.8 |
| Pelo de personagem | tufos GD 8 mm Shape 0,25; sem clump vira feltro | 17.9, 17.16 |
| Trança | Braid Shape 0, Factor Min 0,7 | 17.10 |
| Cabelo "esculpido" | Curve to Mesh com Radius ligado no Scale | 17.11 |
| Risca seca | ilhas + Group ID; não ligar Guide Index no Clump se vier Curl | 17.13, 17.18 |
| Deixar leve | ordem Clump → Trim → Noise → Frizz → Profile → Curl; Viewport 0,25 | 17.14 |
| Corte curto nas laterais | vertex group no Trim Mask e no Clump Factor | 17.17 |
| Ponta virada | Roll Direction = ± posição da raiz | 17.20 |
| Volume na raiz | normal do Interpolate → Set Position | 17.21 |
| Franja | Trim → Displace por região → Shrinkwrap Above 0 | 17.24 |
| Física sem desabar | guias com UV, Bendiness 0, Substeps 40, Collider na cabeça | 17.25 |
| Balanço no giro | Simulation to World vazio | 17.26 |
| Máscara por imagem | `surface_uv_coordinate` → Image Texture → Random → Delete | 17.27 |
| Crespo | ≥ 8 pontos por volta | 17.28 |
| Penteado sem esculpir | Generate Hair Curves + parábola + Shrinkwrap | 17.29 |
| Rabo de cavalo | Mix(raiz, amarração) até t, depois cai; Shrinkwrap | 17.30 |
| Maria-chiquinha, rabo trançado, coque | campo na amarração; Braid depois; espiral de fase única | 17.31 |
| Sobrancelha, barba, bigode | região recortada + GR Guias Procedurais como gerador | 17.32 |
| Muitos cortes rápido; ombré | uma árvore, só números; Intercept → Color Ramp | 17.33 |
| Limpar ruído | Blend Hair Curves 1 cm; Smooth só com Shape 0,8 | 17.34 |
| Vento | Scene Time → seno + Noise 4D → Custom Force → Effectors; força 0,12 | 17.35 |
| Cílios | loop fino na quina da pálpebra (< 1 mm) + gravidade aleatória por cílio; tufos + canto externo longo | 17.97 (17.36 superado) |
| Cabelo crescendo | Scene Time − atraso por mecha → Trim Length Factor, Replace off | 17.37 |
| Multidão (LOD) | distância raiz-câmera → Random Boolean → Delete; raio × 1/√fração | 17.38 |
| Silhueta por malha simples | Geometry Proximity na malha → Mix com Spline Parameter → Set Position nas guias | 17.39 |
| Corte reto pela malha | Raycast do ponto para fora; sem acerto → Delete Point | 17.40 |
| Cabelo Trolls | raiz → Raycast (normal + viés para cima) até elipsoide alto; Clump 0,45 | 17.40 |
| Afro que enche | casca renderizada + pelo curto cacheado nascendo nela | 17.41 |
| Menos fios, mesma cobertura | scalp com a cor da raiz: 60 mil/m² cobre como 300 mil | 17.42 |
| Hair cards para jogo | Curve to Mesh com perfil em linha, normal = Tangent × n_raiz, UV em Face Corner | 17.43 |
| Listra, mancha, roseta no pelo | textura na raiz → atributo → cor + Trim 40% | 17.44 |
| Mesmo groom em outra cabeça ou criança | troque scalp e colisão; criança = escala de objeto não aplicada | 17.45 |
| Cabelo seguir cabeça animada | Deform Curves on Surface no fim; padrões por posição antes dele | 17.46 |
| Contorno de desenho | casca invertida no GN + material só para raio de câmera | 17.47 |
| Redemoinho | Vector Rotate em volta da coroa, ângulo × falloff × Spline Parameter | 17.48 |
| Transição ou mistura de penteados | Resample igual → Sample Index de B → Mix com A | 17.49 |
| Personagem completo sem esculpir | Guias Procedurais → Física → Densidade → Mecha → Strays → Cacho → Cor | 17.50 |
| Procedural e depois esculpir | Apply no modificador das guias; mantém UV de fixação e id | 17.51 |
| Mecha colorida, mecha branca, molhado, ahoge | seleção por mecha → atributo `destaque` → shader e Set Position | 17.52 |
| Alongar fios | Trim Length Factor > 1 (1,5 = +50%) | 17.52 |
| Direção do pelo por curva desenhada | Tangente da curva mais próxima projetada na pele | 17.53 |
| Cadeia leve | Ponta Virada antes de Onda/Cacho, Subdivisão 0 ou 1: 9× mais rápido | 17.54 |
| Criatura completa | Pentear por Curva + listra no dorso + barriga clara | 17.55 |
| Anime / NPR | 3.000/m², Mecha Chunky raio 1,8 cm sem torção, Toon, Contorno | 17.56 |
| Cabelo flutuando / vento barato | Noise 4D com W = tempo × Spline Parameter^1,5 no offset das guias | 17.57 |
| Cabelo que esparrama no chão | profundidade abaixo do piso vira deslocamento para fora | 17.58 |
| Cada cópia com cabelo diferente | Hash da posição do Self Object no Seed e nos Random | 17.59 |
| Meio preso, mistura regional | GR Transição com Fator = máscara de região; B = GR Rabo de Cavalo | 17.60 |
| Cabelo atrás da orelha | Transição + Rabo de Cavalo com amarração atrás de cada orelha | 17.60 |
| Trança lateral no ombro | Rabo de Cavalo com amarração lateral e Para trás −0,5 → Trança Grossa com a cabeça ligada | 17.61 |
| Fio saindo por dentro da pele | Shrinkwrap antes de Onda/Cacho (barato); no fim só para render (9× mais caro) | 17.62 |
| Reproduzir groom animado pesado | Node Bake (Animation) no fim: 353 → 9 ms por quadro | 17.63 |
| Pelo pictórico | normal da pele no fio (Toon) + cor por clump e sub-clump | 17.64 |
| Cel-shading no cabelo | normal da malha proxy (Sample Nearest Surface) no Toon | 17.65 |
| Cabelo sob chapéu | Shrinkwrap na cabeça com Factor = copa acima OU aba abaixo (dois Raycasts) | 17.66 |
| Cabelo apoiado nos ombros | Shrinkwrap no tronco, Above 0, nas guias e no fim | 17.67 |
| Cor muda no close | Shape das curvas: em close de fio grosso, Ribbons sai ~2× mais claro que 3D Curves | 17.68 |
| Comprimento pintado | surface_uv_coordinate → Image Texture → Map Range → Trim Length Factor | 17.69 |
| Parâmetro de valor único variando por região | dois ramos + GR Transição com máscara | 17.70 |
| Desenhar as guias | Grease Pencil to Curves → Set Attachment Surface → Densidade | 17.71 |
| Mandar biblioteca de grupos para outra máquina | tornar locais os utilitários que o Essentials traz linkados | 17.72 |
| Despenteado com mechas coesas | Rotate + Noise nas guias; strays nos filhos | 17.73 |
| Dreadlocks | 2.200/m² → Onda S lenta → Mecha Chunky redonda → relevo por Noise | 17.74 |
| Tranças box | GR Trança Grossa com Tamanho da trança ~1,5 cm, Guias por fio 1 | 17.75 |
| Barba longa de fio ou em blocos | Guias Procedurais na região; Chunky + Cel + Contorno para blocos | 17.76 |
| Menor groom estilizado | Value → Interpolate → Clump 0,25 → Profile → Material (5 nodes, 46 ms) | 17.77 |
| Animal com tufos e manchas por região | máscaras de posição → Trim e atributos; cor por Color Ramp, não melanina | 17.78 |
| Máscara de região sem vertex group | GR Máscara por Posição (caixa suave pela raiz) | 17.79 |
| Moicano / crista | raspado + Comprimento até a Malha misturados por Máscara por Posição | 17.80 |
| Undercut | Trim 5% fora da Máscara por Posição (altura e lateral) + Volume na Raiz | 17.81 |
| Cacho em cabelo curto | raio relativo ao comprimento manda, não as voltas | 17.82 |
| Pelo arrepiado (susto) | animar o Levanta da GR Pentear por Curva | 17.83 |
| Mão/objeto passando pelo cabelo | GR Desviar de Objeto depois do Shrinkwrap | 17.84 |
| Anel de brilho de anime | faixa na coordenada Object (não no Intercept) → Emission | 17.85 |
| Franja reta ou em bicos | GR Corte pela Malha com a borda da frente na altura da franja | 17.86 |
| Groom não muda ao mover o personagem | tudo é local ao objeto; gravidade procedural = −Z do objeto | 17.87 |
| Balanço com follow-through sem física | Vector Rotate na raiz com seno defasado pelo Spline Parameter | 17.88 |
| Hairline suave na testa | campo de posição no Density Mask (1 → 0,08 nos últimos 3,5 cm) | 17.89 |
| Vibrissas de animal | Guias Procedurais na região do focinho, 26 fios, Shape 0,9 | 17.90 |
| Franja cortina | dois conjuntos de guias procedurais misturados por Transição + risca em ilhas | 17.91 |
| Pontos certos para cada comprimento | Resample em modo Length depois do Trim | 17.92 |
| Levar o groom para outro programa | USD leva os atributos; Alembic só posição e raio | 17.93 |
| Quanto custa mais fio no render | 28× fios = 2,2× tempo; o caro é avaliar a cadeia | 17.94 |
| Sobrancelha expressiva | escala de um Empty → offset (levantar e franzir) | 17.95 |
| Personagem com cortina e balanço | dois ramos de guias + GR Balanço + Transição | 17.96 |
| Cílio cartoon com raiz fina | loop < 1 mm, 9 milhões/m², Random Value na Gravidade, Clump 1,8 mm, Trim por X | 17.97 |
| Princípios de estúdio (Pixar, Disney, DreamWorks) | fontes coletadas e resumidas | 17.12 |
| Material estilizado | Principled BSDF para cor fiel; Toon diffuse + glossy | 17.15 |
| Biblioteca pronta (33 grupos) | `laboratorio/receitas_grooming.blend` e `laboratorio/exemplos/` | 17.19 |
| Renders de referência | `laboratorio/img/finais/` | 17.22 |


Tudo aqui foi renderizado em Cycles numa cabeça de teste em **escala real**
(raio 10 cm, scalp 0,052 m², fios de 24 a 28 cm, 160 a 220 guias).
Limite da cabeça de teste: o scalp termina **2 cm abaixo do centro** da
esfera, também na nuca e nas laterais. Uma hair cap real desce 6 a 8 cm
abaixo disso atrás. Receitas de nuca e lateral (undercut 17.81, orelha
17.60) mostram menos cabelo curto que numa cabeça real; as alturas das
máscaras precisam ser ajustadas à sua hair cap. O scalp de teste também
**não cobre a costeleta** (recorta \|X\| > 8 cm abaixo de 2,5 cm junto com a
orelha): um teste de costeleta com a regra 17 deu 0 raízes na região e não
vale como resultado. Refeito como **região própria** recortada da cabeça
(igual a sobrancelha e barba, 17.32): GR Guias Procedurais 3,5 cm,
gravidade 3, 700 mil/m² (3,6 mil fios), Clump 5 mm. Lê como costeleta;
saiu em bloco retangular porque a região recortada é um retângulo: dê à
região o formato final da costeleta [img/109_costeleta]. Os valores
valem direto para uma cabeça humana em metros. Scripts em
`Blender Hair Geometry Nodes/laboratorio/scripts/`, folhas de contato em
`laboratorio/img/`. Cada receita cita a folha.

### 17.0 As regras que mais pesaram (resumo do laboratório)

| # | Regra | Por quê (medido) | Onde |
|---|---|---|---|
| 1 | Value node no Density do Interpolate | o painel trava em 10.000/m² (~420 fios na cabeça) | 17.1 |
| 2 | Curl: Frequency = voltas por metro ÷ 3; nunca sorteada por fio | Frequency por fio desmancha o cacho | 17.1, 17.3 |
| 3 | Clump Shape 0,25 | Shape 0 abre careca na raiz | 17.2 |
| 4 | Aleatório por mecha: ID = `guide_curve_index` | por fio vira ruído | 17.3, 17.5 |
| 5 | Noise/Frizz cumulativos antes de Curl, Braid e Subdivide | o deslocamento cresce com o número de pontos | 17.7 |
| 6 | Ponta Virada (Roll) antes de Onda/Cacho, Subdivisão 0 ou 1 | 6,8 s → 0,7 s | 17.54 |
| 7 | Shrinkwrap com Above Surface 0 | 0,5 (padrão) achata o groom inteiro | 17.24 |
| 8 | Deform Curves on Surface é o último node de forma | nas guias, a raiz descola 12,6 mm; posição lida depois dele escorrega 46% | 17.46 |
| 9 | Feche a topologia do scalp antes de pentear | Triangulate re-sorteia todas as raízes | 17.38 |
| 10 | Scalp pintado com a cor da raiz | 60 mil fios cobrem como 300 mil | 17.42 |
| 11 | Escala de objeto não aplicada | o groom inteiro escala junto (criança = réplica) | 17.45 |
| 12 | Depois do Braid (trança), Shrinkwrap na cabeça | o Braid afunda 58% do trecho do crânio | 17.61 |
| 13 | Normal de uma malha lisa no shader | cel-shading e pelo pictórico com 2 nodes | 17.64, 17.65 |
| 14 | Node Bake para reproduzir groom animado | 353 → 9 ms por quadro | 17.63 |
| 15 | Física: guias com UV de fixação, Substeps 40, Collider por coleção | sem UV explode; Surface Collision no scalp explode | 17.25 |
| 16 | Ajuste a cor no Shape do render final (Ribbons ou 3D Curves) | em close de fio grosso, Ribbons sai ~2× mais claro; em vista normal < 7% | 17.68 |
| 17 | Região com direção própria (franja, costeleta): segundo conjunto de guias + GR Transição | a direção das guias domina; Trim e empurrão não bastam. As raízes dos dois ramos são idênticas | 17.91 |
| 18 | Para levar o groom a outro programa, USD | Alembic perde todos os atributos (cor por mecha, UV da raiz); USD leva | 17.93 |
| 19 | Multidão: Shift+D do conjunto e reapontar o Surface | Alt+D empilha o cabelo na cabeça original; Collection Instance repete igual | 17.59 |
| 20 | Cílio: raiz em loop fino (< 1 mm), variação só na direção (gravidade aleatória por fio) | gravidade igual para todos vira pente; raiz larga vira escova com profundidade; normal invertida faz o fio nascer para dentro | 17.97 |

### 17.1 Armadilhas da 5.2 medidas

- **Scalp.** O Interpolate acha o scalp pelo Object Data do Curves (Surface e
  Surface UV Map). Não precisa de nada na frente. Colocar Attach Hair Curves to
  Surface com Named Attribute "UVMap" no Surface UV Map **quebra** o groom
  (fios de 1 ponto): o campo é lido nas curvas, que não têm UVMap.
- **Density trava em 10.000 por m² no painel.** Em escala real isso dá uns 420
  fios na cabeça inteira. Um node **Value** ligado no socket Density passa do
  limite: 100.000 deu 5.088 fios, 300.000 deu 15.500.
- **Curl: voltas por metro = 3 × Frequency** (dentro do grupo, Segment Length
  acumulado × Frequency × 3). Frequency 1 num fio de 28 cm é menos de uma
  volta. O valor depende da escala da cena.

### 17.2 Mecha estilizada (Pixar/Disney) [img/03_shape_sheet, 04_ribbon_sheet]

Clump com Guide Distance 0,02, Factor 1, Preserve Length ligado. O que decide
o visual é o **Shape**:

| Shape | Resultado |
|---|---|
| 0 | Fecha desde a raiz, abre careca no topo |
| 0,25 | Mechas marcadas, raiz coberta. **A receita de 1 node** |
| 0,5 (padrão) | Fecha só nas pontas, "vassoura" |
| 1,0 | Quase não junta |

Distance Falloff de 0,006 a 0,01 apaga o clump; não use para estilizado.

**Mecha em fita** (3 nodes a mais, controle total): Shape 0, e o Factor vem de
Spline Parameter → Map Range (From 0 a 0,3, To 0 a 1, Clamp) → Factor do
Clump. Mais Tip Spread 0,004. A rampa segura a raiz aberta e fecha a mecha a
partir de 30% do fio. Rampa 0,15 é cedo demais e abre buraco.

### 17.3 Cachos definidos (Merida) [img/06_curlfreq_sheet, 07_curlvar_sheet]

Cadeia: Interpolate → Clump (Shape 0,25, GD 0,02) → Curl (Existing Guide Map
ligado, Subdivision 3, Curl Start 0,08) → Set Hair Curve Profile.

| Visual | Radius | Frequency |
|---|---|---|
| Cacho em mola, Merida | 0,010 a 0,011 | 9 a 10 |
| Mola apertada | 0,007 | 20 |
| Onda aberta | 0,012 | 5 |

- Clump antes do Curl, com Existing Guide Map ligado no Curl: o cacho
  acompanha a mecha.
- **Variação por mecha**: Random Value (Float) com **ID = Named Attribute
  (Integer) `guide_curve_index`** no Radius (0,007 a 0,016) e na Frequency
  (6 a 13). Cada mecha ganha seu cacho e a definição fica.
- **Variação por fio** [img/07b_curlvar_sheet, 07c_curlvar_sheet], corrigido
  depois de isolar: o Curl calcula a hélice na **guia** (Sample Curve pelo
  índice da guia, dentro do grupo) e aplica nos filhos.
  - **Radius por fio funciona**: Random Value → Evaluate on Domain (Curve) →
    Radius. Cacho mais cheio, ainda definido.
  - **Frequency por fio quebra**: a hélice do filho desencontra da guia e o
    cacho vira cilindro liso. Frequency só fixa ou por mecha (ID =
    `guide_curve_index`).
  - Random Value **sem ID e sem Evaluate on Domain** num input de ponto
    sorteia **por ponto**, não por fio. No Curl vira massa felpuda; no Set
    Curve Tilt, fita enrugada. Esse foi o erro do primeiro teste.
- Custo: Subdivision 3 leva 12 pontos para 89 por fio. 20 mil fios = 1,8
  milhão de pontos.

### 17.4 Ondas (Rapunzel, Moana) [img/08_waves_sheet, 09_swave_sheet]

- **Hair Curves Noise** amostra o ruído pela posição da raiz (dentro: Noise
  Texture com Scale 5 × posição × Scale). Em escala real, Scale 1 não faz
  nada. **Scale 10 + Scale along Curve 8 + Distance 0,015** dá onda orgânica.
- **Curl com Frequency 3 e Radius 0,015** dá onda de praia estilizada. É
  hélice, então tem volume.
- **Onda plana em "S"** (visual de desenho), 8 nodes sem grupo: Subdivide
  Curve (Cuts 2) → Set Position com Offset = eixo lateral × seno × rampa.
  - eixo lateral = Normalize(Cross(Tangent, 0,0,1))
  - seno = Sine(Spline Parameter Length × 2π/período + fase)
  - fase por mecha = Random Value (0 a 2π) com ID = `guide_curve_index`
  - rampa = Map Range(Spline Parameter Factor, 0 a 0,2 → 0 a amplitude, Clamp)
  - **Amplitude 2 cm, período 12 cm** = S limpo. Sem a fase por mecha, fica
    padrão de carimbo.

### 17.5 Cor estilizada por mecha [img/10_color_sheet]

- Geometria: Random Value (Float) com ID = `guide_curve_index` → Store Named
  Attribute (Float, **Curve**) com nome `mecha_rand`.
- Shader: Attribute `mecha_rand` → Map Range (To 0,3 a 0,65) → Melanin do
  Principled Hair. Dá faixas de tom por mecha, o "brilho de desenho".
- Hair Info → Random (por fio) só suja o tom. Não serve para estilizado.
- **Raiz escura**: Hair Info → Intercept → Map Range (From 0 a 0,25, To 0,45 a
  0, Clamp) somado à melanina.

### 17.6 Strays e flyaways [img/11_strays_sheet, 12_arcs_sheet]

Seletor: Curve Info → Random → Compare (Less Than) → Factor do node.

| Visual | Fração | Node e valores |
|---|---|---|
| Realista, zigue-zague | 0,12 | Frizz, Distance 0,02, Cumulative |
| **Estilizado, arco limpo** | 0,04 | Hair Curves Noise, Distance 0,04, Shape 0,7, Scale 3, Offset per Curve 1, Cumulative |
| Arco dramático | 0,04 | o mesmo com Distance 0,07 |

Ligar o mesmo Compare no Mask de um Trim com Length Factor 1,25 deixa realista
e bagunçado demais para estilizado.

### 17.7 Cumulative Offset depende da quantidade de pontos [t_cumul.py]

Medido na ponta do fio, Distance 0,02:

| Pontos por fio | Noise, Cumulative ligado | Frizz, Cumulative ligado | Qualquer um, desligado |
|---|---|---|---|
| 12 | 6,3 cm | 6,0 cm | 1,2 a 2,7 cm |
| 34 | 19 cm | 10,5 cm | igual |
| 78 | 44 cm | 16 cm | igual |

Noise cresce em linha reta, Frizz como passeio aleatório. **Regra: Noise e
Frizz com Cumulative vão antes de qualquer node que subdivide** (Curl,
Braid, Subdivide Curve). Com strays depois do Curl (89 pontos), os fios
explodiram para cima [img/13_seed_sheet vs 13b_seed_sheet].

### 17.8 Seed mestre: variações com um número [img/13b_seed_sheet]

Um node **Integer** ("Seed mestre") → um **Integer Math Add** por node, com um
deslocamento fixo (0, 1, 2, 3...) → Seed de Interpolate, Clump, Curl, Random
Value e Noise. Mudar um número troca o groom inteiro sem repetir padrão entre
nodes. A mesma árvore faz liso, ondulado ou cacheado mudando só a Frequency do
Curl (0 desliga, 3 onda, 9 cacho).

### 17.9 Pelo estilizado de personagem (DreamWorks) [img/14_fur_sheet]

Esfera de 15 cm, guias de 3,5 cm penteadas para baixo.

| Visual | Receita | Fios |
|---|---|---|
| Feltro, "bicho de pelúcia" | Interpolate 3 M/m², sem clump | 846 mil |
| **Tufo estilizado** | Interpolate 1,5 M/m² → Clump GD 0,008, Shape 0,25, Tip Spread 0,001 | 423 mil |
| Pele aparecendo | o mesmo com Shape 0 | 423 mil |
| Macio realista | subpelo (3 M/m², Trim 0,45) + topo (0,6 M/m², Clump GD 0,01, Trim 1,15), Join Geometry | 1 milhão |

Sem clump o pelo vira feltro, o problema que o Steve Chow descreve na palestra
[pal/bcon2026-steve-chow-photoreal-cat-hair-curves.md]. As duas camadas são
dois ramos saindo do mesmo Group Input, cada um com seu Interpolate e Seed,
juntados por Join Geometry.

### 17.10 Trança [img/15_braid_sheet, 15b_braid_sheet]

Uma guia na nuca, Interpolate com **Distance to Guides 0,02** (só nasce fio
perto da guia), Density 4 M/m², Braid Hair Curves com Guide Distance 0,3 (uma
trança por guia) e Existing Guide Map desligado.

- Frequency maior dá mais cruzamentos: 2 = fechada, 0,5 = solta.
- Shape 0,5 com Factor Min 0 (padrão) afina a trança até sumir.
- **Trança grossa estilizada**: Radius 0,016 a 0,02, **Shape 0, Factor Min
  0,7**.
- Flare Length 0,05 com Opening 0,025 vira um disco achatado na ponta.
  Começar bem menor.

### 17.11 Mecha "chunky" em malha (cabelo esculpido) [img/16b_chunky_sheet]

Cabelo de personagem "de brinquedo": poucas mechas grossas viradas em malha.

1. Interpolate com Density 3.000 a 6.000 por m² (150 a 300 mechas).
2. Resample Curve, Count 24.
3. Set Hair Curve Profile: Radius 0,004 a 0,006, Shape 0,3, Factor Min 0
   (ponta afiada).
4. (opcional) Set Curve Tilt = Spline Parameter × π: fita torcida.
5. Curve to Mesh: Profile = Curve Circle (Resolution 10) com Transform Scale
   Y 0,35 (fita achatada). **Ligar um node Radius no Scale do Curve to
   Mesh.** Na 5.2, com o Scale solto, o perfil ignora o raio do fio e cada
   mecha vira um tubo de 1 metro.
6. Set Shade Smooth, material de malha comum (Principled BSDF, Coat 0,4).

Torção por mecha: Random Value (−π a π) → Evaluate on Domain (Curve) →
multiplica o Spline Parameter. Sem o Evaluate on Domain, sorteia por ponto e
a fita enruga [img/16_chunky_sheet]. Render: 2,5 a 3 s por quadro.

### 17.12 Fontes estilizadas e princípios de estúdio

Pasta `estilizado/` (coleta de 2026-09-28): 12 fontes com URL verificada,
`SINTESE.md` com 13 princípios. Os vídeos do YouTube ficaram sem transcrição
(bloqueio do ambiente); os arquivos têm descrição e capítulos. Princípios
confirmados no laboratório:

- **Cor por mecha, não por fio** (DreamWorks, Gato de Botas: manchas de cor
  "como pinceladas") = 17.5.
- **Poucas guias grandes definem a silhueta** (Pixar, Brave: 1.500 guias para
  111 mil curvas) = a base de todos os testes aqui.
- **Clump em camadas, macro depois detalhe** = 17.2 e o teste dos dois Clumps
  na seção 5.
- **Fita torcida com Set Curve Tilt** (BlenderArtists, 2022). A dúvida sem
  resposta do fórum, variar a torção por mecha, está resolvida em 17.11.

### 17.13 Risca limpa [img/17_part_sheet]

Vista de cima, mesmo groom:

1. Scalp inteiro: risca borrada, fios atravessando.
2. Scalp rasgado em duas ilhas na risca, Interpolate com Part by Mesh Islands:
   a interpolação respeita, mas o **Clump ainda puxa fio de um lado para o
   outro**.
3. Duas ilhas **+ Create Guide Index Map com Group ID** = Compare (Curve Root →
   Root Position X > 0), ligado no Guide Index do Clump: **risca seca**.

O Group ID aceita qualquer inteiro: uma máscara de região pintada no scalp
serve para franja, nuca e laterais que nunca se misturam.

**Cuidado com esse ligamento** (ver 17.18): o Clump com Guide Index ligado
junta certo, mas grava `guide_curve_index` com o mapa dele. Se vier Curl ou
Braid depois, use Create Guide Index Map com Group ID + Clump com Existing
Guide Map ligado, **sem** ligar o Guide Index.

### 17.14 Custo por node e ordem da cadeia [t_perf.py, t_perf2.py]

62 mil fios, 12 pontos cada, CPU de 4 núcleos, avaliação sem render:

| Node | Custo adicionado |
|---|---|
| Interpolate | 76 ms |
| Clump | 161 ms |
| **Hair Curves Noise** | **412 ms** (o deformador mais caro) |
| Frizz | 90 ms |
| Curl Subdivision 2 | 303 ms, e multiplica os pontos por 4 |
| Trim depois do Curl | 905 ms |
| Set Hair Curve Profile | 110 ms |

- **Ordem otimizada**: Clump → Trim → Noise → Frizz → Profile → Curl (o que
  subdivide por último). 2,1 s caiu para 1,4 s, mesmo resultado.
- **Viewport Amount 0,25** no Interpolate: 1,35 s caiu para 0,29 s. Render
  continua com a densidade cheia.
- Noise e Frizz com Cumulative também precisam vir antes do Curl (17.7).

### 17.15 Shading estilizado [img/18b_shading_sheet]

Mesma cor base (0,30; 0,11; 0,04), mesmo groom:

- **Principled Hair, modo Direct Coloring**: Chiang clareia muito a cor
  (espalhamento múltiplo), Huang clareia e dessatura. Para castanho escuro,
  escolha uma cor bem mais escura que o alvo ou use Melanin.
- **Principled BSDF comum nas curvas**: a cor sai como escolhida. Bom para
  estilizado e para a mecha chunky.
- **Toon BSDF**: Diffuse (Size 0,6, Smooth 0,05) + Glossy (Size 0,15, Smooth
  0,02) num Add Shader dá a faixa de brilho chapada de desenho. Funciona em
  curvas no Cycles.
- **Gradiente raiz → ponta**: Hair Info → Intercept → Color Ramp → Base Color.

### 17.16 Pelo de guarda e buracos (DreamWorks) [img/19_guard_sheet]

- **Guarda**: um ramo extra do mesmo Group Input com Interpolate 30 mil/m²,
  sem clump, Trim Length Factor 1,4, raio 0,0009 (3× o pelo base). Join
  Geometry. Aparece como franja fina na silhueta.
- **Buracos de propósito**: Random Value **Boolean** (Probability 0,18, ID =
  `guide_curve_index`) → Selection de um Delete Geometry (Curve). Some o tufo
  inteiro. Em pele clara vira mancha branca; só funciona com subpelo ou pele
  escura por baixo.

### 17.17 Regiões com vertex group: corte curto nas laterais [img/20b_regions_sheet]

Na 5.2, o vertex group pintado no scalp chega nos fios como atributo Float de
Curve com o mesmo nome (medido). Com um grupo `topo` (1 em cima, 0 nas
laterais e na nuca):

- Trim Hair Curves com Replace Length ligado, Length 0,025 e **Mask = 1 −
  topo** (Math Subtract) encurtou 22% dos fios para 2,5 cm.
- Clump com o mesmo cabelo curto faz espetinhos. **Factor do Clump = topo**
  desliga o clump na área curta, que vira máquina baixa limpa.

### 17.18 Achado: Clump com Guide Index ligado grava o mapa errado [t_clumpgi.py]

Medido, 15 mil fios, Create Guide Index Map com Guide Distance 0,02 (117
guias) ligado no Guide Index de um Clump com Guide Distance 0,1 (padrão):

| Situação | Mapa que o Clump usa | `guide_curve_index` que ele grava |
|---|---|---|
| Guide Index ligado, Existing desligado | 117 | **7** |
| Guide Index ligado, Existing ligado | 116 | **6** |
| Guide Index solto, Existing ligado | 117 | 117 |

O Clump junta com o mapa que recebeu, mas grava no atributo o mapa que ele
mesmo calcula com o Guide Distance interno. Qualquer node depois com
Existing Guide Map (Curl, Braid, outro Clump) lê o mapa errado. Na prática:
os cachos seguiram 6 guias gigantes e o cabelo "sumiu" do render
[img/21d_sheet].

**Regra**: para passar um mapa próprio (com Group ID, por exemplo), use Create
Guide Index Map antes e o Clump com **Existing Guide Map ligado, sem ligar
Guide Index**. Ou iguale o Guide Distance do Clump ao do mapa.

### 17.19 Biblioteca pronta: `laboratorio/receitas_grooming.blend` [img/21_lib_sheet]

Trinta e cinco node groups "GR" e cinco materiais, marcados como asset, feitos com as
receitas desta seção e validados abrindo o .blend do zero:

- GR Densidade Livre, GR Mecha Estilizada, GR Lado da Risca, GR Strays em
  Arco, GR Cacho por Mecha (em voltas por metro), GR Onda S, GR Cor por
  Mecha, GR Mecha Chunky, GR Ver em Cores, GR Ponta Virada, GR Trança
  Grossa, GR Corte por Região, GR Pelo em Tufos, GR Volume na Raiz, GR Máscara por
  Imagem, GR Física Estilizada (com entrada de Vento, 17.35), GR Guias
  Procedurais, GR Rabo de Cavalo, GR Forma por Malha, GR Crescer, GR LOD por
  Câmera, GR Corte pela Malha, GR Comprimento até a Malha, GR Hair Cards, GR
  Contorno, GR Transição, GR Pentear por Curva, GR Semente do Objeto, GR Flutuar, GR
  Chão, GR Normal da Malha (31 grupos)
  [img/21_lib_sheet, 23_lib2_sheet, 45_lib6_sheet, 47_lib7_sheet].
- Materiais GR Cabelo Cor por Mecha, GR Cabelo Toon, GR Card Alpha, GR
  Contorno e GR Cabelo Cel.
- Toda entrada tem dica ao passar o mouse, com os valores medidos aqui.
  Nenhum dado linkado (17.72). Arquivo de partida e três cenas prontas em
  `laboratorio/exemplos/`.

Como usar e ordem da cadeia: `laboratorio/README.md`. A validação achou o
problema de 17.18 e a regra da Onda S: **amplitude menor que o tamanho da
mecha**, senão mechas vizinhas se cruzam em X.

### 17.20 Ponta virada com Roll (flip e ponta para dentro) [img/22_roll_sheet, 22c_roll_sheet, t_roll.py]

**Roll Direction não é eixo**, apesar da descrição dizer "axis". Por dentro, o
Roll tira do vetor a componente ao longo do fio e usa o que sobra como o lado
para onde a ponta enrola. Medido na ponta, Roll Length 0,06 e Roll Radius
0,02, Random Orientation 0:

| Roll Direction | Ponta, distância horizontal do eixo da cabeça |
|---|---|
| sem Roll | 14,4 cm |
| Curve Root → Root Position | **17,8 cm: vira para fora** (flip anos 60) |
| − Root Position (Vector Math Scale −1) | **10,2 cm: enrola para dentro** (bob) |
| Cross(Root Position, Z) | igual a sem Roll: enrola de lado |
| eixo fixo no mundo | cada lado da cabeça enrola para um lado |

Nos dois casos a ponta sobe cerca de 6 cm. Roll Length sorteado por mecha (0,6
a 1,4 × o valor, ID = `guide_curve_index`) fica mais natural. Pronto em GR
Ponta Virada.

### 17.21 Variação procedural sem pintar [img/24_proc_sheet, 24b_proc_sheet, t_proc.py]

- **Comprimento por mecha**: Random Value (0,7 a 1,0, ID = `guide_curve_index`)
  → Length Factor do Trim (Replace Length desligado). Barra recortada.
- **Clump quebrado por ruído 3D**: Noise Texture (Scale 25, Detail 0) na
  Root Position do Curve Root → Map Range (0,4 a 0,6 → 0,15 a 1, Clamp) →
  Factor do Clump. Regiões mais soltas sem pintar.
- **Volume na raiz**: o **Displace Hair Curves com Surface Normal não moveu
  nada** (medido: raiz, meio e ponta iguais) sem o UV do scalp. O que
  funciona, 4 nodes: a saída **Surface Normal do Interpolate** → Store Named
  Attribute (Vector, Curve) `n_raiz`; depois Set Position com Offset =
  `n_raiz` × Map Range(Spline Parameter Factor, 0 a rampa → 0 a volume,
  Clamp). A raiz fica parada.

| Volume | Rampa | Terço do fio se afasta | Visual |
|---|---|---|---|
| 1,5 cm | 0,3 | +1,1 cm | volume leve |
| 3 cm | 0,15 | +2,3 cm | topete, volume de princesa |

Pronto em GR Volume na Raiz (a GR Densidade Livre grava o `n_raiz`).

### 17.22 Renders finais feitos só com a biblioteca [img/finais/]

1024 px, 64 amostras, Cycles CPU de 4 núcleos:

| Estilo | Cadeia de grupos GR | Fios | Tempo |
|---|---|---|---|
| Pixar (bob) | Densidade 450 mil/m² → Mecha (2,2 cm, Lado da Risca) → Volume 2 cm/0,2 → Strays 3% → Ponta Virada p/ dentro → Cor por Mecha | 23 mil | 94 s |
| Disney (Merida) | Densidade 350 mil/m² → Mecha 1,8 cm → Volume 2,5 cm → Strays 3% → Cacho por Mecha (0,9 a 1,6 cm, 22 a 38 voltas/m) → Cor por Mecha | 18 mil (1,6 M pontos) | 229 s |
| DreamWorks (bicho) | Pelo em Tufos (tufo 9 mm, subpelo, guarda) → Cor por Mecha | 1,28 milhão | 213 s |

Dois defeitos que ficaram visíveis e viram regra:

- **Redemoinho no polo**: onde todas as guias saem de um ponto (o topo da
  esfera), o volume na raiz vira um nó escuro. Na cabeça real: guias
  penteadas no redemoinho ou volume menor ali (vertex group no Volume).
- **Raiz escura em ruivo e loiro**: +0,45 de melanina na raiz faz a linha do
  cabelo parecer castanha. Para cabelo claro, use +0,1 a +0,2.

### 17.23 Quantos pontos o cacho precisa [img/26_pts_sheet]

13 mil fios cacheados, 400 px:

| Configuração | Pontos por fio | Avaliação | Render | Visual |
|---|---|---|---|---|
| Curl Subdivision 1 | 23 | 96 ms | 9,0 s | poligonal, pedaços soltos |
| **Curl Subdivision 2** | 45 | 156 ms | 7,8 s | **igual à 3** |
| Curl Subdivision 3 | 89 | 234 ms | 7,8 s | referência |
| Resample 30 + Subdivision 0 | 30 | 129 ms | 8,6 s | aceitável |

O Cycles quase não sente a quantidade de pontos (ele suaviza a curva). O
custo está na avaliação e na memória. **Subdivision 2** é o padrão do GR
Cacho por Mecha.

### 17.24 Franja e colisão com a cabeça [img/27_fringe_sheet, 27b_fringe_sheet]

Vertex group `franja` na frente do topo. Ordem que funciona:

1. Trim Hair Curves: Replace Length ligado, Length 0,09, **Mask = franja**.
   Antes do Displace, para medir o fio original.
2. Displace Hair Curves: Displace Vector (0; −0,06; −0,03), Shape 0,5,
   **Factor = franja**. Sozinho, atravessa a testa.
3. **Shrinkwrap Hair Curves**: Surface = o objeto da cabeça (não o scalp),
   **Above Surface 0**, Offset Distance 0,004, Smoothing Steps 2, Lock Roots
   ligado. Empurra para fora só o que entrou.

**Above Surface 0,5 (padrão) puxa também o que está fora da cabeça e achata o
groom inteiro.** Para colisão, sempre 0.

### 17.25 Física 5.2: simular as guias e manter o penteado estilizado [img/28_dyn_sheet, 28c_dyn_sheet, 28d_dyn_sheet; t_dyn_dbg.py, t_dyn_hold.py]

Hair Dynamics (asset em `geometry_nodes_dynamics_assets.blend`), aplicado só
nas 260 guias; Interpolate e o resto da cadeia vêm em outro modificador
depois. Manual: `modeling/geometry_nodes/simulation/hair_dynamics.rst`.

**Armadilhas medidas:**

- O Mode vem em **Animation** (só segue a superfície). Para física, "Physics
  (Experimental)". O socket de entrada chama "Hair".
- **Guias sem `surface_uv_coordinate` explodem**: a raiz é presa pelo UV, e
  sem ele todas ficam no UV (0,0). No Blender: Snap to Nearest Surface nas
  guias antes de simular. O scalp precisa ter UV.
- **Surface Collision com o scalp explodiu** em todas as repetições (pontas
  subindo 25 a 50 cm já no quadro 3): as raízes estão sobre o próprio
  colisor. O caminho estável: **Collider** (asset) num modificador da cabeça
  inteira, a cabeça numa coleção, a coleção no **Effectors Collection** do
  Hair Dynamics. Estável até o quadro 48. Neste teste nenhum ponto chegou a
  encostar na cabeça, então o efeito do Collider em si não ficou provado.

**Segurar um penteado estilizado contra a gravidade** (groom espetado, queda
média da ponta no quadro 36):

| Configuração | Queda | Custo por quadro |
|---|---|---|
| Padrão (Bendiness 0,5, Root 0,2, Substeps 10, Steps 15) | 12,5 cm, desaba | 26 ms |
| Bendiness 0,05 ou 0, Root 0,02 ou 0 | 12,4 cm, igual | 26 ms |
| Constraint Steps 60 | 5,4 cm | 81 ms |
| Constraint Steps 120 | 2,8 cm | 152 ms |
| **Bendiness 0, Root 0, Substeps 40** | **1,5 cm, mantém** | **84 ms** |
| Steps 60 + gravidade 1/4 | 1,5 cm | 79 ms |
| Mass 0,001 | igual ao padrão | — |

Leitura: com os valores padrão, a rigidez pedida não é cumprida porque o
solver não converge. **Substeps é a alavanca eficiente.** Massa não muda a
queda, porque a gravidade acelera qualquer massa igual. Para estilizado:
Bendiness 0, Root Bendiness 0, Substeps 40, e aumente Bendiness só onde quer
movimento.

### 17.26 Movimento: Simulation to World [img/29_motion_sheet e os dois GIFs]

Cabeça, scalp e guias filhos de um Empty que gira 60° e volta (quadros 1 a
36), Hair Dynamics com Bendiness 0,5, Root 0,1, Substeps 20.

- **Simulation to World vazio (padrão)**: a simulação é em espaço de mundo. O
  cabelo atrasa no giro e passa do ponto na volta. É o que dá vida.
  [img/29_giro_padrao_espaco_mundo.gif]
- **Self Object → Object Info → Transform ligado no Simulation to World**: a
  simulação passa a ser no espaço do objeto. O cabelo segue a cabeça quase
  rígido, sem inércia. [img/29_giro_transform_do_objeto_rigido.gif]

Uso: deixe vazio para ter balanço. Ligue uma transformação (de um osso raiz ou
de um Empty que acompanha o personagem) quando o deslocamento grande do
personagem andando não deve virar inércia no cabelo.

### 17.27 Máscara por imagem validada no laboratório [t_mask.py, t_lib3.py]

Imagem 64×64 metade preta (u < 0,5), metade branca, 15.669 fios:

| Método | Fios que sobraram no preto |
|---|---|
| sem máscara | 4.890 |
| slot Mask Texture do Interpolate | 56, na borda (interpolação Linear) |
| cadeia: Named Attribute `surface_uv_coordinate` → Image Texture (Closest) → Random Value Boolean (Probability) → NOT → Delete Geometry (Curve) | 0 |
| GR Máscara por Imagem (Linear) | 53 |

Confirma a receita de 8 (observado em produção). A GR Máscara por Imagem
devolve também o cinza da imagem por fio, para reusar em Trim, Clump e Curl.
GR Física Estilizada carregada do .blend: 1,5 cm de queda em 36 quadros,
igual ao teste manual de 17.25.

### 17.28 Cacho apertado e crespo: pontos por volta [img/30_coily_sheet, 30b_coily_sheet]

- Crespo estilizado: raio 2 a 4,5 mm, 110 a 180 voltas por metro. Num fio de
  16 a 20 cm são 20 a 30 voltas.
- Com Curl Subdivision 3 (89 pontos) a mola **serrilha**; com 2, vira zigue-
  zague. **Regra: pelo menos 8 pontos por volta.** Resample Curve (Count 200)
  antes do Curl, com Subdivision 0.
- Custo: 36 mil fios × 200 pontos = 7,2 milhões de pontos. Crespo estilizado
  pede menos fios e mechas maiores.
- A silhueta redonda de afro vem das **guias** (esculpidas), não dos nodes.
  Guias retas e radiais dão silhueta de escova, com qualquer node depois.

### 17.29 Guias procedurais: penteado sem esculpir [img/31_procguides_sheet, 32_zero_sculpt]

Bloqueio de penteado em segundos, antes de esculpir. Parte de um objeto Curves
**vazio** com Surface definida:

1. **Generate Hair Curves**: Poisson Disk, 4.000 por m² (cerca de 200 guias
   numa cabeça real), 12 pontos, Hair Length L. Sai reto pela normal.
2. **Set Position**, Offset = (Surface Normal × (para fora − 1) + (sinal de
   Root X, 0, 0) × lado + (0, para trás, 0)) × L × t − Z × gravidade × L × t²,
   com t = Spline Parameter Factor. É uma parábola: sai, vai para o lado da
   risca e cai.
3. **Shrinkwrap Hair Curves** na cabeça, Above Surface 0, Offset 0,006,
   Smoothing 3.
4. Daí em diante, a cadeia normal (Interpolate, Mecha...).

| Penteado | Para fora | Lado | Gravidade | Comprimento |
|---|---|---|---|---|
| Bob liso | 0,4 | 0,35 | 1,2 | 22 cm |
| Longo ondulado (+ Onda S) | 0,4 | 0,25 | 2,2 | 34 cm |
| Volume cacheado (+ Cacho) | 0,8 | 0,45 | 0,5 | 24 cm |
| Espetado | 1,2 | 0,1 | 0 | 12 cm |

Pronto em **GR Guias Procedurais**. Validado: um groom completo com 10 nodes,
só grupos GR, sem uma guia esculpida. Para refinar, aplique o modificador e
esculpa por cima das guias geradas.

### 17.30 Rabo de cavalo procedural [img/33_pony_sheet, 34_pony_lib_sheet]

Reposiciona cada fio a partir da raiz; a forma das guias não importa, só onde
as raízes estão. Depois da GR Densidade Livre:

1. Resample Curve, 24 pontos.
2. Set Position, **Position** (não Offset) =
   Mix Vector(Root Position, ponto da amarração, Map Range(t, 0 a tf))
   + Normalize(0, para trás, −1) × Map Range(t, tf a 1) × comprimento da cauda
   + Random Vector por curva (Evaluate on Domain) × abertura × Map Range(t, tf a 1).
   Com tf = 0,35 (fração do fio até o elástico) e abertura 0,03.
3. Shrinkwrap na cabeça, Above Surface 0: o trecho até o elástico cola no
   crânio.
4. Mecha Estilizada (1,2 cm), e Onda ou Cacho só na cauda.

**Regra**: o "Começa em" do Cacho ou da Onda tem que ser maior que tf, senão o
cacho começa em cima do crânio e bagunça a parte presa. Abertura de 1,2 cm
deixa a cauda fina demais; 3 cm lê bem. Pronto em GR Rabo de Cavalo.

### 17.31 Maria-chiquinha, rabo trançado e coque [img/35_updos_sheet, 35b_bun_sheet]

Todos em cima da GR Rabo de Cavalo:

- **Maria-chiquinha**: um campo no socket Amarração. X = Sign(Root Position
  X) × 0,085, Y 0,035, Z 0,03. Cada lado vai para o seu elástico, e a risca
  central sai limpa sem mais nada.
- **Rabo trançado**: GR Trança Grossa depois, com "Começa em" 0,4 (maior que o
  "Até a amarração"). Funciona, mas a trança sai fina e o topo ganha textura
  de ruído; precisa de ajuste.
- **Coque**: depois do rabo com cauda 0, um Set Position enrola a parte depois
  do elástico numa espiral no plano perpendicular à direção do elástico: raio
  de 3 a 4 mm crescendo até 2,2 a 3 cm, 2,2 a 3 voltas, subindo 1,8 cm.
  **Fase e raio iguais para todos os fios** (a cauda é uma corda). O único
  sorteio por fio é um deslocamento de 6 a 8 mm, a espessura da corda.
  Com fase e raio sorteados por fio, o primeiro teste virou uma nuvem.

Regra geral que sai daqui: **forma coletiva (coque, corda, trança) usa valores
iguais para o grupo; variação por fio só para textura**. É o mesmo princípio
da Frequency do Curl (17.3).

### 17.32 Pelos do rosto estilizados [img/36_face_sheet]

Cada região é uma malha recortada da cabeça (como uma hair cap), com um objeto
Curves vazio apontando para ela. **GR Guias Procedurais serve direto como
gerador**: pelo curto não precisa de Interpolate. Depois, Clump pequeno e Set
Hair Curve Profile afinando a ponta.

| Região | Comprimento | Para fora | Lado | Gravidade | Fios/m² | Clump |
|---|---|---|---|---|---|---|
| Sobrancelha | 1,4 cm | 0,25 | 1,2 | −0,4 (sobe) | 600 mil | 4 mm |
| Barba | 1,8 cm | 0,5 | 0,15 | 1,0 | 900 mil | 5 mm |
| Bigode | 2 cm | 0,4 | 1,4 | 0,6 | 900 mil | 5 mm |
| Cílio | 1 cm | 0,9 | 0,3 | −1,6 | 120 mil | sem |

O "Lado" usa o sinal do X da raiz: na sobrancelha e no bigode isso penteia
para fora a partir do centro do rosto, que é o sentido natural. Gravidade
negativa curva para cima. Os cílios (67 fios) ficaram escondidos atrás dos
olhos: precisam de mais comprimento e de uma região na borda da pálpebra.

### 17.33 Uma árvore, oito cortes; cor ombré [img/37_gallery_sheet]

Mesmo tree de grupos GR (Guias Procedurais → Densidade Livre → Mecha →
Volume → Strays → Cacho, Onda ou Ponta Virada → Cor por Mecha → Profile),
trocando só números:

| Corte | Comprimento | Para fora | Lado | Gravidade | Extra |
|---|---|---|---|---|---|
| Bob | 20 cm | 0,4 | 0,35 | 1,2 | Ponta para dentro |
| Longo ondulado | 34 cm | 0,4 | 0,25 | 2,2 | Onda S |
| Cacheado volumoso | 24 cm | 0,8 | 0,45 | 0,5 | Cacho por Mecha |
| Espetado | 12 cm | 1,2 | 0,1 | 0 | nada |
| Flip anos 60 | 18 cm | 0,45 | 0,3 | 1,4 | Ponta para fora, Volume 3 cm |
| Curto cacheado | 12 cm | 0,9 | 0,2 | 0,3 | Cacho 4 a 7 mm, 50 a 80 voltas/m |
| Longo liso | 36 cm | 0,35 | 0,2 | 2,6 | Ponta para dentro |

**Ombré**: Hair Info → Intercept → Color Ramp (cor da raiz em 0,45, cor da
ponta em 0,95), multiplicado por Attribute `mecha_rand` (Map Range 0,7 a 1,2)
para variar por mecha, no Color do Principled Hair em Direct Coloring.
**Preto em Direct Coloring (0,02) saiu cinza**, confirmando 17.15. Para preto e
castanho escuro, use Melanin.

### 17.34 Limpar um groom bagunçado [img/38_cleanup_sheet, 38b_smooth_sheet]

Groom com Noise forte (Distance 0,012, Scale 20, cumulativo), depois:

| Node | Resultado |
|---|---|
| Smooth Hair Curves, Shape 0 (padrão), 10 ou 30 iterações | **Topo careca**: alisa a curva perto da raiz, que é o que deita o fio no crânio |
| Smooth, Shape 0,5 | ainda careca no topo |
| **Smooth, Shape 0,8**, 20 iterações | limpa e mantém a raiz |
| **Blend Hair Curves**, raio 0,01, 10 vizinhos | limpa o ruído e deixa as mechas coesas; a melhor limpeza para estilizado |
| Straighten Hair Curves 0,5 | alisa pela metade |
| Rotate Hair Curves, Random Offset 0,6 rad | varia a direção por fio e encorpa a silhueta |

### 17.35 Vento com Custom Force [img/39_wind_sheet, 39_vento_0.04.gif, 39_vento_0.12.gif]

Custom Force é o asset de efetor do mesmo arquivo do Hair Dynamics
(`geometry_nodes_dynamics_assets.blend`). Sua saída **Force** é um Bundle que
entra no socket **Effectors** do Hair Dynamics. Oito nodes:

1. Scene Time **Seconds** × (2π ÷ 1,5 s) → Sine → Multiply Add (×0,4 + 0,6)
   = rajada que oscila entre 20% e 100%.
2. × Força → Combine XYZ no X = direção do vento.
3. Turbulência: Noise Texture **4D**, Vector = Position, **W = Seconds**,
   Scale 15 → Color − 0,5 → Scale (Força × 1,2).
4. Soma 2 + 3 → Custom Force **Force** → Hair Dynamics **Effectors**.

Guias com Bendiness 0,3, Root Bendiness 0,05, Substeps 20; o groom vem
depois, no segundo modificador. Deslocamento médio das pontas no X (fio 30 cm):

| Força | q12 | q24 | q36 | q48 |
|---|---|---|---|---|
| 0 | −0,2 cm | −0,2 | −0,2 | −0,2 |
| 0,04 | +3,4 | +0,7 | +2,4 | +3,9 |
| **0,12** | **+8,5** | +1,8 | +6,9 | **+10,9** |

- 0,04 é brisa quase invisível no render; **0,12** é vento de cena.
- A rajada lenta (seno) dá o ritmo; o Noise 4D faz as mechas se moverem
  fora de fase. Só o seno = cabelo inteiro balançando como um bloco.
- Custo: 48 quadros de simulação + render 320 px em 37 s (4 núcleos).
- Para vento de outra direção, troque o eixo do Combine XYZ; não gire nada.

### 17.36 Cílios estilizados [img/40_lash_sheet]

> **Superado por 17.97.** O Vini apontou (2026-09-28) que estes cílios saem como pente: todos na mesma direção, como se o scalp fosse uma edge. Mantido como referência do erro.

O teste 17.32 escondia os cílios porque a região ficava na cabeça, atrás do
globo ocular. A superfície certa é a **pálpebra**: uma faixa da própria
esfera do olho, 6% maior.

1. Copie a malha do olho e apague tudo menos a faixa logo acima do centro
   (em coordenadas locais do olho: Z 1 a 6 mm, só a frente). Escala 1,06.
2. GR Guias Procedurais nessa faixa: Comprimento 9 mm, Para fora 1,
   **Gravidade −1,3** (negativa = curva para cima), 250.000 guias/m²
   (~65 por olho).
3. Sem Interpolate e sem Clump. Set Hair Curve Profile raio 0,5 mm,
   **Shape 0,8** (afina bem na ponta).

| Variante | Resultado |
|---|---|
| Faixa alta (Z 5 a 13 mm) | leque vertical, parece escova |
| **Linha da pálpebra, fora 1, grav −1,3** | leque curvo acompanhando o olho |
| Só canto externo (x > 4 mm), 6 fios, raio 0,9 mm | cílio "Disney" de 3 a 6 fios grossos |
| Clump 2,5 mm | tufos: pouco ganho no estilizado |

Regra: a curva vem de **Para fora** (sai da pálpebra) + gravidade negativa
(sobe no fim). Comprimento acima de 70% do raio do olho fica cartunesco.

### 17.37 Cabelo crescendo (animação procedural) [img/41_grow_sheet, 41_crescer_por_mecha.gif]

Efeito mágico estilo Trolls, sem keyframe. Seis nodes no fim da cadeia, antes
do Profile:

1. Scene Time **Seconds** → Multiply Add (× 0,8) = velocidade.
2. Random Value Float 0 a 0,4, **ID = Named Attribute int
   `guide_curve_index`** → Evaluate on Domain (Curve) = atraso por mecha.
3. Subtract (1 − 2) → Clamp (mín 0,02) → **Trim Hair Curves Length Factor**,
   Replace Length **desligado**, Scale Uniform desligado.

| Variante | Resultado |
|---|---|
| **Corte, atraso por mecha** | cada mecha cresce pelo caminho final, em blocos; o melhor para estilizado |
| Scale Uniform ligado | o cacho inteiro encolhe junto: viram escamas coladas no crânio |
| Atraso por fio (sem ID) | crescimento macio e uniforme, sem leitura de mecha |

- Trim no fim porque o fio cresce já penteado, cacheado e com clump.
- O Profile vem **depois** do Trim: a ponta afina em qualquer comprimento.
- Custo: Trim depois do Curl é o node mais caro da cadeia (17.14). Nos 10
  mil fios deste teste, 24 quadros + render em 43 s. Para cena longa, faça
  cache (Bake) do modificador.
- Termina em 2 s com esses valores. Para mudar a duração, mexa só no × 0,8.

### 17.38 LOD por distância da câmera (multidão) [img/42_lod_sheet]

Truque de multidão: longe da câmera, menos fios e fio mais grosso para manter
a cobertura. Nove nodes logo **depois do Interpolate** (tudo que vem depois
já processa menos fios):

1. Object Info (a câmera), **Relative** → Location. Relative põe a câmera
   no espaço do objeto do cabelo; sem isso a distância erra quando o
   personagem se move.
2. Curve Root → Root Position; Vector Math **Distance** (raiz, câmera).
3. Map Range, clamp: 1 m → 8 m vira **1 → 0,04** = fração que fica.
4. Random Value **Boolean**, Probability = fração → Boolean NOT →
   Delete Geometry (Curve).
5. Depois do Profile: Radius × **Inverse Sqrt**(fração) → Set Curve Radius.
   Raiz quadrada porque cobertura é área: com 1/4 dos fios, raio × 2.

Mesmo processo, só a fração mudando (12.865 fios no groom cheio):

| Distância | Fios | Pontos | Avaliação | Visual |
|---|---|---|---|---|
| 0,75 m | 12.865 (100%) | 154 mil | 40 ms | idêntico |
| 2,5 m | 10.237 (80%) | 123 mil | 39 ms | idêntico |
| **6 m** | **4.055 (31%)** | **49 mil** | **22 ms** | igual; leve falha no topo |

- O ganho é memória e avaliação, não render: o Cycles levou o mesmo tempo
  (1,3 a 1,6 s) com a cabeça pequena no quadro. Numa multidão de 100
  personagens, 15 milhões de pontos viram 5.
- Sem o Set Curve Radius a cabeça distante fica rala e transparente.

**Ordem das faces do scalp define a distribuição.** No laboratório, o scalp
gerado por script saía com ordem de faces diferente a cada execução, e o
Interpolate dava 12.843 a 12.865 fios com mechas em lugares diferentes. Numa
.blend salva a ordem é estável. Medido na mesma malha, mesma forma:

| Mudança no scalp | Fios | Raiz mais próxima | Ponta mais próxima |
|---|---|---|---|
| Sort Elements aleatório (faces) | 12.862 → 12.849 | 0,98 mm | 5,2 mm |
| Triangulate | 12.849 → 12.864 | 0,97 mm | 5,4 mm |

0,98 mm é a distância esperada entre duas distribuições independentes com
esse espaçamento: **todas as raízes foram re-sorteadas** e as mechas mudaram
de lugar (pontas 5 mm). Remesh e Decimate mudam a topologia ainda mais.
Feche a topologia do scalp antes de pentear, nunca depois.

### 17.39 Silhueta por malha proxy [img/45_shell_sheet, 45_lib6_sheet]

Técnica do laboratório (as fontes de estúdio desta base não citam): o artista
modela uma malha simples em volta da cabeça, o "capacete" da silhueta, e as
guias colam nela. Trocar de corte = trocar a malha. Sete nodes nas **guias**,
antes do Interpolate:

1. Object Info (a malha), **Relative** → Geometry → Geometry Proximity
   (Faces) → Position.
2. Spline Parameter Factor → Map Range clamp, From Max **0,35** (a partir
   de 35% do fio ele está na malha).
3. Mix **Vector**: A = Position, B = posição da Proximity, Factor = 2 →
   Set Position.

| Forma | Sem proxy | Com proxy |
|---|---|---|
| **Bob** (esfera 14,5 × 15 × 13 cm, cortada em z −13 cm) | fios longos caindo | bob limpo; as pontas dobram na borda da malha e fecham a linha do corte |
| **Topete** (esfera deslocada para frente e para cima) | fios espetados para trás | corte curto com volume na frente |
| Afro (esfera 19 cm) + Curl | cachos espalhados | **casca oca**: o volume fica numa camada só; afro continua dependendo das guias (17.28) |

- Funciona para formas de **superfície** (bob, topete, capacete, franja
  reta). Para formas de **volume** (afro, nuvem), não.
- Malha aberta: apague a parte do rosto e a de baixo. Onde a malha acaba, as
  pontas dobram na borda; isso é o que dá o bob.
- O fio encurta ou estica para caber na malha; o comprimento das guias vira
  secundário.
- Armadilha medida: no Mix em modo Vector, a saída válida é a segunda
  (índice 1). Ligar a de Color (desativada) não dá erro e o Set Position
  simplesmente não faz nada.

Pronto em **GR Forma por Malha** (entradas: Malha da forma, Força, Cola a
partir de). Validado carregando do .blend. Os dois usos de 17.40 estão em GR
Corte pela Malha e GR Comprimento até a Malha.

### 17.40 Raycast na malha: corte reto e cabelo Trolls [img/46_ray_sheet, 47_sheet]

Outra forma de usar a malha proxy (17.39): em vez de colar o fio nela, a
malha **mede** o comprimento ou **corta**.

**Corte pela malha (bob reto), 5 nodes depois do Clump:**
Position → Normalize (direção do centro da cabeça para fora) → Raycast
(Target = malha via Object Info Relative, Source = Position, Direction =
Normalize, Length 1) → Is Hit → NOT → Delete Geometry **Point**. Ponto
dentro da malha acerta o raio e fica; ponto fora não acerta e é apagado. O fio
cai natural e para na linha da malha: corte reto de verdade, diferente do
bob colado de 17.39, onde as pontas dobram.

**Comprimento até a malha (radial), 9 nodes depois da GR Densidade Livre:**
Resample 24 → Raycast da raiz (Curve Root) na direção `n_raiz` (+ um viés,
ex. (0,0,1,5) para subir) → Position = raiz + direção × Spline Parameter ×
Hit Distance → Set Position → Clump.

| Variante | Resultado |
|---|---|
| **Trolls**: elipsoide alto (16 × 16 × 35 cm), direção normal + (0,0,1,5), Clump GD 4 cm **Factor 0,45**, Profile Shape 0,1 | chama lisa e alta: silhueta Trolls |
| Mesmo com Clump Factor 1 | tufo espetado (as mechas fecham em ponta) |
| Afro radial (esfera 19 cm) + Curl | silhueta certa, mas **espetado**: fios radiais divergem e não enchem, mesmo com 31 mil fios e cacho de 1 cm |

Armadilhas medidas:
- **A malha tem que conter todo o scalp.** Elipsoide mais estreito que a
  cabeça na altura das orelhas: 671 fios de 15 mil nasceram fora da malha e
  desceram. Com a malha maior, 0.
- Clump **Guide Distance 0,2 m** num fio de 30 cm juntou 15 mil fios em 2
  mechas. Guide Distance é o tamanho da mecha em metros.

### 17.41 Afro estilizado: casca sólida + pelo curto [img/47_sheet]

Afro com fio da raiz até a borda não enche (17.28, 17.40). O que leu como
massa foi separar **forma** e **textura**:

1. Malha do afro (esfera 17 × 17,5 × 16 cm, aberta no rosto e embaixo),
   **renderizada** com material marrom quase preto, roughness 0,9. Ela é o
   volume.
2. Um Curves com Surface = essa malha (precisa de UV). GR Guias Procedurais
   como gerador: Comprimento 3,5 cm, Para fora 1, Gravidade 0, 150.000/m²
   (42 mil fios); Cabeça (colisão) = a própria malha.
3. Resample 40 → Clump GD 8 mm Shape 0,2 → Curl raio 3 mm, Frequency 45
   (135 voltas/m ≈ 5 voltas), Subdivision 0 → Profile 0,6 mm.

1,7 milhão de pontos; a casca esconde o interior, então não precisa de fio
lá dentro. Falta refinar a borda da abertura, que mostra a espessura zero da
casca.

Variações só trocando a malha [img/88_afros_sheet]: casca larga e baixa
(20 × 19 × 13 cm), casca alta (15 × 16 × 22 cm) e **dois puffs** (duas
esferas de 7,5 cm juntadas num objeto, 19,7 mil fios). O node tree é o
mesmo. Limite visto: o recorte do rosto feito por faces fica em degrau e a
borda oca aparece de frente. Para produção, modele a abertura com borda
virada para dentro (Solidify curto na casca) ou esconda com cabelo da linha
do rosto (GR Guias Procedurais na hairline).

Testado [img/47_borda_sheet]: recorte do rosto por **elipse** (22 × 19 cm
no plano XZ, numa esfera de 128 × 64 segmentos) + modificador **Solidify
2 cm para dentro** na casca. A borda da abertura ganha espessura coberta de
pelo e perde o degrau; não aparece mais o oco. Com elipse pequena demais
(17 × 15 cm) o afro engole o rosto: dimensione o recorte pela vista de
frente.

### 17.42 Scalp pintado com a cor da raiz [img/48_scalp_sheet]

Zero node. O scalp (ou a região do cabelo na textura da cabeça) recebe a cor
da raiz: aqui um Principled marrom escuro (0,06; 0,028; 0,014), roughness
0,6, no objeto scalp 0,4% acima da cabeça, visível no render.

Medido com render de máscara (pele emissiva verde, scalp azul, cabelo preto),
pixels de pele à mostra no topo da cabeça, vista de cima:

| Fios/m² | Fios | Pele | Scalp pintado |
|---|---|---|---|
| 60.000 | 2.900 | 4.606 px | **461 px** |
| 150.000 | 7.600 | 1.799 px | 354 px |
| 300.000 | 15.400 | 809 px | 262 px |

**60 mil fios com scalp pintado mostram menos pele que 300 mil sem pintar**:
um quinto dos fios para a mesma cobertura. Na risca e no redemoinho, onde o
cabelo abre, a diferença é a maior. Para estilizado, combine com densidade
baixa e fio grosso: é o que deixa o groom leve na viewport.

### 17.43 Hair cards para jogo a partir do groom [img/49_cards_sheet]

O mesmo scalp e as mesmas guias geram cards (fitas planas com UV) para
engine. GR Densidade Livre com densidade **baixa** (8.000 a 20.000/m² = 280
a 860 cards) e depois:

1. Resample 10 → Set Hair Curve Profile (Radius = meia largura, 9 mm;
   Shape 0,4 afina para a ponta).
2. **Set Curve Normal, modo Free, Normal = Cross(Tangent, `n_raiz`)**.
3. Spline Parameter → Store Named Attribute `v` (Point).
4. Perfil: Curve Line (−1,0,0) a (1,0,0) → Store `u` = Spline Parameter.
5. Curve to Mesh, **Scale = Radius** (17.11) → Combine XYZ(u, v) → Store
   Named Attribute **2D Vector, Face Corner, nome `UVMap`**.

Orientação do card, medida como |normal do card · direção radial| (1 =
deitado no crânio, 0 = de pé):

| Normal da curva | Valor | Leitura |
|---|---|---|
| Minimum Twist (padrão) | 0,74 | gira sem controle ao longo do fio |
| `n_raiz` | **0,12** | de pé: o card some de frente |
| **Tangent × `n_raiz`** | **0,76** | deitado, estável |

- 860 cards = 15,8 mil triângulos.
- **Exportar**: Object > Convert > Mesh no objeto Curves. O atributo
  `UVMap` vira UV map real e o FBX sai com ele (testado, 7.911 faces).
- Material GR Card Alpha: alpha procedural = faixas de fio (Noise esticado
  40× no U) × borda (1 − |2u−1|⁴) × ponta (1 − v³); raiz mais escura por v.
  Para engine, troque por uma textura de fios; o UV já está pronto.
- Card precisa de scalp pintado (17.42): com poucos cards a pele aparece.

Pronto em **GR Hair Cards** + material **GR Card Alpha**, validado do .blend.

### 17.44 Pelagem com padrão: listra, mancha, roseta [img/50_pattern_sheet]

Um atributo por fio controla **cor e comprimento** juntos; o padrão lê como
relevo, não como pintura. Corpo de 15 cm de raio, 1,5 M fios/m², tufos de 8 mm.

1. Curve Root → Root Position → textura:
   - **Listra**: Wave Texture Bands, direção Z, Scale 7, Distortion 8 →
     Map Range 0,62–0,68 → 0–1.
   - **Mancha**: Voronoi F1, Scale 12, Distance → Map Range 0,40 → 0,34
     (invertido: perto do centro da célula = 1).
   - **Roseta** (onça): o anel do Voronoi = Map Range 0,26–0,30 × Map Range
     0,44–0,40.
2. Evaluate on Domain (Curve) → Store Named Attribute `padrao` (Float, Curve).
3. Trim Length Factor = 1 − 0,4 × padrao (Scale Uniform ligado): a parte
   escura fica 40% mais curta e afunda.
4. Shader: Attribute `padrao` → Map Range 0,3–1 → Melanin, Redness 1.

- Só cor (escala 3): faixa chapada. Cor + comprimento: sulco com leitura
  de pelagem.
- Escala da textura é em metros do objeto: Scale 3 num corpo de 30 cm dá
  duas faixas; 7 dá listra de tigre.
- Em personagem animado, calcule o padrão **antes** do Deform Curves on
  Surface ou use `surface_uv_coordinate` (17.27). Medido em 17.46: depois
  do Deform, 46% dos fios trocaram de cor.

### 17.45 Um groom, várias cabeças [img/51_heads_sheet]

A cadeia GR Guias Procedurais → Densidade Livre → Mecha Estilizada → Onda S
→ Cor por Mecha (zero escultura) foi aplicada sem mexer em nenhum valor em
cabeças de formatos diferentes, trocando só o scalp e a cabeça de colisão:

| Cabeça | Fios | Resultado |
|---|---|---|
| Redonda | 15.662 | referência |
| Ovo (0,9 × 1 × 1,25) | 16.999 | o penteado acompanha o crânio alto |
| Larga (1,25 × 1,1 × 0,88) | 18.304 | acompanha; mais área, mais fios |
| Criança, malha 0,7 | 7.683 | fio, mecha e onda continuam em metros de adulto: tudo parece grande |
| Criança, malha 0,7, Comprimento × 0,7 | 7.697 | melhor, mas mecha e onda ainda grandes |
| **Criança, escala do objeto 0,7** | 15.536 | **réplica exata do adulto** |

- Geometry Nodes trabalha no espaço do objeto. Cabeça, scalp e Curves com
  **escala de objeto não aplicada** escalam todas as distâncias juntas:
  comprimento, mecha, onda, cacho e raio do fio. Não aplique a escala se
  quiser que o groom acompanhe.
- Formato diferente (ovo, larga) não pede ajuste: as guias saem da normal e
  o Shrinkwrap segura no crânio novo.
- A contagem acompanha a área em metros do objeto: cabeça larga ganha fios.

### 17.46 Cabeça que deforma: onde vai o Deform Curves on Surface [img/52_deform_sheet]

Scalp e cabeça com shape key (inclina 5 cm e estica 2 cm no topo), scalp com
**Add Rest Position** ligado (Object Data), guias com
`surface_uv_coordinate`, Interpolate com Resting Surface ligado (padrão).
Medido com a shape key em 0 e em 1, mesmos fios:

| Onde está o Deform Curves on Surface | Raiz até o scalp deformado | Padrão por posição muda | Padrão por UV muda |
|---|---|---|---|
| Nenhum | 12,7 mm (máx. 40) | 0% | 0% |
| Nas guias, antes do Interpolate | 12,6 mm (máx. 40) | 42% | 39% |
| No fim, padrão calculado **depois** dele | **0,06 mm** | **46%** | 0% |
| **No fim, padrão calculado antes dele** | **0,06 mm** | **0%** | **0%** |

1. **Deform Curves on Surface é o último node de forma** (depois de Clump,
   Curl etc., antes de Profile e Material). Nas guias antes do Interpolate
   não serve: os filhos nascem na superfície em repouso e a cabeça atravessa
   o cabelo.
2. Tudo que lê **Position** (textura por posição, máscara por região,
   distância à câmera) vem **antes** do Deform, ou lê
   `surface_uv_coordinate`. Depois dele o padrão escorrega: 46% dos fios
   trocaram de cor com uma inclinação de 5 cm. Isso confirma a nota de 17.44.
3. Sem Add Rest Position no scalp, o Rest Surface avisa "Missing rest
   geometry on surface" (visto no dump do grupo, 5.2.2).
4. **Resting Surface do Interpolate ligado** (padrão). Desligado, na mesma
   cena: a contagem muda com a deformação (**7.834 → 8.446 fios**: fios
   aparecem e somem a cada quadro) e as raízes descolam **16 mm** em média
   (máx. 43 mm), mesmo com o Deform no fim.

### 17.47 Contorno de nanquim nas mechas de malha [img/53_toon_sheet]

Para cabelo em malha (GR Mecha Chunky, 17.11) com GR Cabelo Toon. Casca
invertida feita **dentro do Geometry Nodes**, sem modificador Solidify:

1. Flip Faces na malha → Set Position Offset = Normal × (−espessura) →
   Set Material "contorno" → Join Geometry com a malha original.
2. Material do contorno: Mix Shader entre Emission quase preta e Transparent,
   Factor = **Maximum(Backfacing, 1 − Is Camera Ray)**.

| Versão | Resultado |
|---|---|
| Factor = só Backfacing | **cabelo inteiro preto**: a casca bloqueia os raios de sombra e de luz |
| Factor = Maximum(Backfacing, 1 − Is Camera Ray) | contorno certo: só a câmera vê a casca |
| Espessura 1,2 mm | traço fino, quase some a 70 cm |
| **Espessura 2,5 mm** | traço de desenho legível |

- A casca dobra as faces (40,6 mil → 79 a 84 mil).
- Cycles: Transparent Max Bounces ≥ 32 (usei 64); com muitas mechas
  sobrepostas o padrão 8 pode escurecer.
- Espessura em metros do objeto: com escala de objeto (17.45), o traço
  acompanha.

Pronto em **GR Contorno** + material **GR Contorno**, validado do .blend.

### 17.48 Redemoinho na coroa [img/54_whorl_sheet]

Oito nodes nas **guias**, depois da GR Guias Procedurais e antes do
Interpolate:

1. Curve Root → Distance até o ponto da coroa C (aqui 3,5 cm atrás do topo).
2. Map Range clamp: 0 → 7 cm vira **1 → 0** (falloff).
3. Ângulo = Spline Parameter × falloff × força.
4. **Vector Rotate** Axis Angle: Vector = Position, Center = C, Axis = C
   normalizado (a normal da coroa), Angle = 3 → Set Position.
5. Shrinkwrap Hair Curves na cabeça (Above 0) para nada entrar no crânio.

| Força (rad na ponta) | Fio 16 cm | Fio 7 cm |
|---|---|---|
| 1,5 | espiral suave | (não testado) |
| **3,5** | mechas saem voando da cabeça | **redemoinho claro** |

A rotação desloca a ponta proporcional à distância dela até o eixo: em fio
longo, use até ~1,5 rad; 3,5 só em cabelo curto. Várias coroas = some
os ângulos de cada uma.

### 17.49 Transição entre penteados [img/55_morph_sheet, 55_transicao_liso_cacheado.gif, 55_lib_fator05]

Um penteado vira outro sem simulação. Depois da GR Mecha Estilizada:

1. **Resample 64** (os dois penteados precisam da mesma contagem de pontos).
2. Ramo B: GR Cacho por Mecha com **Subdivisão 0** (senão muda a contagem).
3. Sample Index (Geometry = B, Value = Position, Index = Index) → Mix
   Vector (A = Position, B = amostra) → Set Position em A.
4. Fator = Map Range **Smooth Step** (Scene Time Seconds − atraso por mecha
   0 a 0,5 s; de 0,3 s a 1,2 s → 0 a 1).

- 10 mil fios × 64 pontos, 24 quadros + render em 43 s.
- O atraso por mecha (Random com ID = `guide_curve_index`) faz o cacho
  "enrolar" em ondas pela cabeça, em vez de tudo junto.
- **Fator parado em 0,5 é um terceiro penteado** (onda larga entre liso e
  cacheado): a transição também serve de slider de estilo.
- O fio cacheado é mais curto no espaço; durante a transição o cabelo
  "sobe". Para manter o comprimento, faça B com Preserve Length e mesmo
  comprimento de A.

Pronto em **GR Transição** (Penteado A, Penteado B, Fator), validado do .blend.

### 17.50 Personagem inteiro só com a biblioteca [img/56_hero_sheet, finais/56_hero_biblioteca, 56_hero.gif]

Teste de integração: um personagem com cabelo, cílios e sobrancelha, zero
escultura, todos os grupos na mesma cadeia, carregados do .blend:

- **Cabelo**: GR Guias Procedurais (26 cm) → GR Física Estilizada (Vento
  0,06, Movimento 0,3, Substeps 20) → Shrinkwrap na cabeça → GR Densidade
  Livre 220 mil/m² → GR Mecha Estilizada → GR Strays em Arco → GR Cacho por
  Mecha (18–30 voltas/m, raio 9–14 mm) → GR Cor por Mecha → Profile → GR
  Cabelo Cor por Mecha. 11,5 mil fios, 517 mil pontos.
- **Cílios** (17.36) e **sobrancelha** (17.32) com a GR Guias Procedurais
  como gerador. **Scalp pintado** (17.42).
- Render 900 px, 48 amostras: 103 s (CPU, 4 núcleos). GIF de 48 quadros
  com física e vento, 360 px: 149 s.

Os grupos convivem sem ajuste interno. O que precisou de ajuste foi **design**:

| Versão | Problema | Ajuste |
|---|---|---|
| v1 | cachos da linha da testa caem na frente do rosto | **Para trás 0,25 → 0,6** nas guias |
| v1 | topo crespo e escuro | Cacho **Começa em 0,15 → 0,35**: o topo fica liso e o cacho nasce na altura da orelha |

Regra: em cabelo cacheado estilizado, o cacho começa depois do topo; a
silhueta de cima é lisa e lê a forma do crânio.

### 17.51 Híbrido: começar procedural, terminar esculpindo [img/57_hibrido_sheet]

GR Guias Procedurais num Curves vazio → **Apply** no modificador
(Ctrl+A no modificador). Resultado medido: 240 guias reais, 2.880 pontos,
com `surface_uv_coordinate`, `id` e o Surface apontando para o scalp. Ou seja,
as guias aplicadas:

- abrem no **Sculpt Mode** de curves para ajuste à mão;
- servem direto para a GR Física Estilizada e para o Deform Curves on
  Surface (têm a coordenada de fixação, 17.25 e 17.46);
- mantêm o `id` estável, que o Interpolate usa para não "pular" quando a
  densidade muda (seção 8).

No teste, as guias do lado direito foram puxadas para fora por script
(simulando o pincel) e a cadeia Densidade Livre → Mecha → Cor → Deform →
Profile rodou em cima sem ajuste.

Fluxo: procedural para chegar em 80% em minutos; Apply; esculpir os 20%
que dão personalidade (franja, mecha de destaque, assimetria).

### 17.52 Mecha de destaque, mecha branca, molhado e ahoge [img/58_destaque_sheet]

Quatro variações de personagem com 3 a 10 nodes cada, todas por **seleção
por mecha** + Store Named Attribute `destaque` (Float, Curve) lido no shader:

| Variação | Seleção | O que muda |
|---|---|---|
| **Mecha colorida** | Random Value **Boolean**, Probability 0,10, ID = `guide_curve_index` | Tint azul e melanina 0,05 no shader; Curl com Factor = seleção (só elas enrolam). 3% deu ~3 mechas, escondidas atrás; **10% = 1.831 fios**, aparece |
| **Mecha branca** (Vampira) | raiz com Y < −3,5 cm e \|X\| < 3 cm (frente, na risca) | Map Range destaque → melanina 0,8 → 0,03 |
| **Molhado** | nenhuma | Mecha 1,2 cm, fecha em 12%, Tip Spread 0; melanina 0,95, roughness 0,15 |
| **Ahoge** | raiz a menos de 6 mm de um ponto da coroa | Set Position com Selection: raiz + (0; −0,07 t²; 0,09 t − 0,05 t²) = arco para cima e para frente |

- Tint no modo Melanin fica dessaturado (azul acinzentado). Para cor viva,
  melanina bem baixa e aceite o tom pastel, ou use Principled BSDF na
  curva (17.15).
- A seleção por mecha (ID da guia) mantém a mecha inteira coesa; por fio,
  sairia salpicado.
- **Trim Hair Curves também alonga.** Medido (fio de 24 cm, Replace Length
  desligado): Length Factor 0,5 = 12 cm; 1,5 = 36 cm (com e sem Scale
  Uniform); 2 = 47,9 cm. No teste da mecha colorida, o Trim 1,25 com Mask =
  seleção deixou só ela mais longa.

### 17.53 Pentear pelo de criatura com uma curva [img/60_flow_sheet]

O artista desenha um objeto Curve sobre o corpo, no sentido do pelo, e o
pelo deita nessa direção. Logo depois de gerar os fios (Generate Hair Curves,
60.000/m², 3,5 cm):

1. Object Info (a curva, Relative) → Curve to Points (Evaluated) → Store
   Named Attribute `fluxo_t` = saída **Tangent** do Curve to Points.
2. Sample Nearest (esses pontos, posição = raiz) → Sample Index (`fluxo_t`).
3. Projeta no plano da pele: fluxo − normal × (fluxo · normal) → Normalize.
   A normal pode ser a **Root Direction** do Curve Root: o fio recém-gerado
   sai pela normal.
4. Direção = Mix(fluxo, normal, **Levanta 0,35**) → Position = raiz +
   direção × Spline Parameter **Length** → Set Position. Depois Clump 8 mm.

| Curva | Resultado |
|---|---|
| Reta da frente para trás | pelo corre para trás; **redemoinho natural** na ponta onde a curva começa |
| Espiral em volta do corpo | pelo gira na diagonal |
| Zigue-zague no dorso | desenho em espinha de peixe na linha das costas |

Pronto em **GR Pentear por Curva** (Curva de fluxo, Levanta), validado do
.blend. Várias curvas no mesmo objeto funcionam: vale a mais próxima.

### 17.54 Custo de cada grupo da biblioteca [img/61_roll_sheet]

Cadeia completa, 300 mil/m² = 15,4 mil fios, 4 núcleos. Tempo de avaliação
acumulado (mede o grupo ligando um por vez):

| Grupo | Ordem original | Pontos | Ordem otimizada | Pontos |
|---|---|---|---|---|
| Densidade Livre | 24 ms | 185 mil | 22 ms | 185 mil |
| Mecha Estilizada | +32 | | +41 | |
| Volume na Raiz | +9 | | +7 | |
| Strays em Arco | +117 | | +101 | |
| Ponta Virada | (depois do cacho) | | **+93, Subdivisão 0** | 185 mil |
| Onda S | +85 | 526 mil | +95 | 526 mil |
| Cacho por Mecha | +305 | 2,06 M | +349 | 2,06 M |
| Ponta Virada, Subdivisão 2 | **+5.912** | **8,18 M** | | |
| **Total** | **6.759 ms** | 8,18 M | **721 ms** | 2,06 M |

- **O Roll (GR Ponta Virada) tem Subdivision própria.** Cada nível dobra os
  pontos, e ele subdivide o que já foi subdividido pela Onda e pelo Cacho.
  Mesmo com Subdivisão 0, depois do cacho ele custou 1,4 s: o Roll é caro
  por ponto.
- Regra: **Ponta Virada antes de Onda e Cacho**, Subdivisão 0 ou 1.
  Visualmente 0, 1 e 2 ficaram quase iguais numa cabeça a 70 cm (154 mil,
  295 mil e 578 mil pontos).
- Viewport 0,25 na cadeia otimizada: 171 ms (3,7 mil fios).
- Conferido que o **render usa 100%** com Viewport 0,25: a viewport avaliou
  633 fios contra 2.950, e o render cobriu a mesma área (15,7% contra 15,4%
  dos pixels). Deixe a GR Densidade Livre no padrão 0,25 sem medo.
- A GR Ponta Virada agora expõe **Subdivisão** (padrão 1; antes era 2 fixo).
- Ordem completa que funciona: Densidade → Mecha → Volume → Strays → Ponta
  Virada → Onda ou Cacho → Cor → (Deform) → Profile.

### 17.55 Criatura inteira: fluxo, listra e barriga [img/finais/62_criatura]

Corpo em gota (frente mais larga), Generate Hair Curves 90 mil/m² (27,6 mil
fios, 4 cm) → **GR Pentear por Curva** (curva reta do focinho à cauda,
Levanta 0,4) → Clump 1,2 cm → Noise leve (3 mm) → listras (Wave Bands Y,
Scale 6, Distortion 5) × máscara de dorso (Z da raiz 0 a 6 cm) → Trim 35%
mais curto na listra → atributo `barriga` (Z da raiz −2 a −8 cm) clareia a
melanina em 0,22. Render 900 px, 40 amostras: 24 s.

- O redemoinho do focinho veio de graça: é onde a curva de fluxo começa.
- Listra só no dorso = multiplicar o padrão por uma rampa de altura da raiz.

### 17.56 NPR estilo anime: mechas de malha + Toon + contorno [img/63_npr_sheet, finais/63_npr_anime]

GR Guias Procedurais (20 cm, para fora 0,7, lado 0,5, gravidade 1,3) → GR
Densidade Livre → ahoge (17.52) → **GR Mecha Chunky** → Toon azul → **GR
Contorno** 2,2 mm; a cabeça também recebe o GR Contorno (1,8 mm) num
modificador próprio. Fundo claro só para a câmera: no World, Mix entre fundo
escuro e claro com Factor = Is Camera Ray (senão o fundo claro vira luz e
lava o Toon).

| Versão | Resultado |
|---|---|
| 2.500/m², raio 1,1 cm | careca: ~130 fitas finas |
| 9.000/m², raio 1 cm, torção 0,5 | capacete bagunçado: fitas torcidas em todas as direções |
| **3.000/m², raio 1,8 cm, torção 0** | mechas largas de anime, franja lendo em blocos |

Regra para NPR: **poucas mechas largas e sem torção**. A leitura vem do
contorno e da forma de cada bloco, não da quantidade.

### 17.57 Cabelo flutuando (embaixo d'água) sem simulação [img/64_agua_sheet, 64_agua.gif]

Nas guias, depois da GR Guias Procedurais (34 cm, para fora 0,6, lado 0,5,
**para trás 0,9, gravidade 0,15**) e de um Resample 24:

1. Scene Time Seconds × 0,4 → W de uma Noise Texture **4D**, Vector =
   Position, **Scale 7**, Detail 0.
2. Color − 0,5 → × (Spline Parameter^1,5 × **0,2**) → Set Position Offset.

A raiz fica parada, a ponta ondula até 10 cm, e a onda anda pelo fio porque a
Noise é lida na posição de cada ponto. 24 quadros a cada 3 (72 quadros),
render 320 px: 37 s.

| Versão | Resultado |
|---|---|
| Gravidade −0,3, Scale 4, amplitude 0,12 | chafariz rígido para cima, mexe pouco |
| **Gravidade 0,15, para trás 0,9, Scale 7, amplitude 0,2** | cabelo deitado para trás, ondulando como na água |

Mesma receita serve de "vento contínuo" barato para cabelo de fundo, onde a
física (17.35) seria cara demais. Pronto em **GR Flutuar** (Amplitude,
Escala, Velocidade).

### 17.58 Cabelo longo que chega ao chão [img/65_chao_sheet]

Fio de 1,1 m, chão a 55 cm abaixo do centro da cabeça. Nas guias (Resample
60), antes do Interpolate, oito nodes:

1. Profundidade = max(Z do chão − Z do ponto, 0).
2. Direção horizontal = Normalize(X, Y + 0,05, 0) (do centro para fora).
3. Offset = direção × profundidade + (0, 0, profundidade) → Set Position.

Todo ponto que furaria o chão sobe até ele e anda para fora o mesmo tanto:
o cabelo **esparrama** em volta, em vez de atravessar. Depois do Interpolate,
um Set Position com Z = max(Z, chão) segura os filhos que furam entre duas
guias.

- Shrinkwrap com Above Surface no chão empilharia tudo no ponto de contato
  (projeta para cima, não para fora).
- As mechas no chão ficam retas e radiais; para leitura orgânica, um Noise
  leve depois da dobra.
- 10,4 mil fios × 60 pontos = 626 mil pontos.
- Pronto em **GR Chão** (Altura do chão, Espalhar). Validado do .blend com
  Flutuar junto: 10,4 mil fios, ponto mais baixo a 3 mm acima do piso
  [img/65_lib_chao].

### 17.59 Cada cópia com cabelo diferente, mesmo node tree [img/66_multidao]

Self Object → Object Info (Original) → **Location → Hash Value (Vector)** =
um inteiro diferente para cada cópia. Ligue esse inteiro:

- no **Seed** de todos os grupos (Densidade, Mecha, Cacho, Cor);
- no **ID** de Random Values que sorteiam por personagem: tamanho da mecha
  (1,2 a 2,8 cm), voltas por metro (4 a 40), Trim (55% a 105%) e um atributo
  `obj_rand` que o shader usa para melanina (0,08 a 0,95) e redness.

Quatro cópias (cabeça, scalp e Curves duplicados juntos, o Curves com o
mesmo node tree): preto longo, loiro curto, castanho médio, ruivo longo. Nada
foi ajustado à mão. Render 900 px com as quatro: 17,5 s.

- Mover a cópia muda o cabelo dela. Para travar, troque Location por um
  inteiro fixo exposto no modificador.
- Pronto em **GR Semente do Objeto** (saídas Seed, Aleatório A, B e C),
  validado do .blend: três posições deram 0,422, 0,097 e 0,191.

Como multiplicar o personagem importa [img/110_copias_sheet]:

| Como | Resultado |
|---|---|
| **Shift+D** (Curves com dados próprios, Surface apontando para a HairCap da cópia) | cada um com cabelo diferente (o teste acima) |
| **Collection Instance** | os quatro **idênticos**: a instância reusa o mesmo objeto avaliado, a posição da instância não chega no Self Object |
| **Alt+D** (dados compartilhados) | o Surface está nos dados: as cópias plantam cabelo na HairCap original, **empilhado na primeira cabeça**, e as outras ficam carecas |

Para multidão com variação: Shift+D do conjunto (cabeça, HairCap, Cabelo)
e reapontar o Surface; ou instâncias com variação pela cor/material apenas.

### 17.60 Meio preso com dois grupos prontos [img/67_meiopreso_sheet]

Nenhum node novo: **GR Transição** com A = cabelo solto e B = o mesmo cabelo
passado pela **GR Rabo de Cavalo** (amarração em (0; 9,5 cm; 4,5 cm), atrás
da coroa). O Fator é a máscara de "quem vai preso":

Curve Root → Z da raiz → Map Range **Smooth Step** 3,5 cm → 5,5 cm → 0 a 1 →
Evaluate on Domain (Curve) → Fator da Transição.

- Os dois ramos precisam da mesma contagem de pontos: Resample 24 antes de
  separar (a GR Rabo de Cavalo usa 24 por padrão).
- O Smooth Step evita a linha dura entre preso e solto.
- Resultado: topo liso puxado para trás, resto solto. A cauda some dentro do
  cabelo solto de mesma cor; para destacar, dê cor (17.52) ou cacho só à
  cauda.
- A mesma ideia vale para qualquer mistura regional de penteados: franja de
  um, nuca de outro.
- **Atrás da orelha** [img/76_orelha_sheet]: mesma técnica. B = GR Rabo de
  Cavalo com Amarração = (sinal do X da raiz × 10,8 cm; 3,5 cm; 0,5 cm),
  atrás de cada orelha, Até a amarração 0,3. Fator = três Smooth Steps
  multiplicados sobre a raiz: \|X\| de 2,5 a 4,5 cm, Y de 7 a 4 cm, Z de 9 a
  7 cm (lateral acima da orelha). A orelha fica à mostra e o cabelo passa
  por trás. Primeira tentativa, com uma orelha que saía só 9 mm do crânio,
  não deu para julgar; com orelha saindo ~2 cm, funcionou.

### 17.61 Trança lateral no ombro e o Braid que afunda o crânio [img/68_elsa_compare]

Trança estilo Elsa com dois grupos: GR Rabo de Cavalo com a amarração na
nuca, de lado (7,5; 6; −7 cm), **Para trás −0,5** (a cauda vai para frente,
por cima do ombro), cauda 30 cm → GR Trança Grossa (raio 2,2 cm, Começa em
0,38, Cruzamentos 1).

**Bug achado e medido:** o Braid Hair Curves junta os filhos na guia pelo
fio **inteiro**, não só a partir do Braid Start. Depois da GR Rabo de
Cavalo, o trecho da raiz até a amarração foi puxado para dentro da cabeça:

| Cadeia | Pontos do 1º terço dentro da cabeça |
|---|---|
| Rabo de Cavalo sozinho | 0% |
| Rabo de Cavalo → Trança Grossa | **58%** (o topo parece careca) |
| → Trança Grossa → Shrinkwrap na cabeça (Above 0, Offset 4 mm) | 0,6% |

Correção na biblioteca: a **GR Trança Grossa ganhou a entrada opcional
Cabeça (colisão)**. Com a cabeça ligada, ela aplica o Shrinkwrap depois do
Braid; sem nada ligado, passa direto como antes. O "topo com ruído" do rabo
trançado de 17.31 era isso.

- Loiro platinado (melanina 0,02) some em pele clara: use 0,1 a 0,15 e scalp
  pintado (17.42).

### 17.62 Auditoria: quanto cabelo entra na cabeça, grupo por grupo

Cadeia típica, 15 mil fios, porcentagem de pontos dentro da cabeça
(raio < 99,5 mm) depois de cada grupo:

| Depois de | Dentro | Pontos |
|---|---|---|
| GR Guias Procedurais | 0,10% | 3 mil |
| GR Densidade Livre (Interpolate) | **1,71%** | 188 mil |
| GR Mecha Estilizada | 2,19% | |
| GR Volume na Raiz | 1,14% (empurra para fora) | |
| GR Strays em Arco | 1,17% | |
| GR Ponta Virada | 2,29% | 360 mil |
| GR Onda S | 2,25% | 1,05 M |
| GR Cacho por Mecha | 2,54% | 4,15 M |

- O próprio **Interpolate já põe 1,7% dos pontos dentro**: o filho nasce
  entre guias e corta a curvatura do crânio. Não é bug de grupo.
- Limpeza com Shrinkwrap Hair Curves (Above 0, Offset 3 mm, sem
  suavização), medida:

| Onde | Dentro | Avaliação |
|---|---|---|
| Sem | 2,34% | 1,1 s |
| **Antes de Onda e Cacho** | 1,32% | 1,95 s |
| No fim da cadeia | 0,00% | **9,7 s** |

  Regra: na viewport, Shrinkwrap antes de Onda/Cacho (pouco ponto). Para o
  render final, se ainda aparecer fio saindo da pele, um no fim.
- **Bug corrigido: a GR Corte pela Malha sem malha ligada apagava todos os
  fios** (o Raycast não acerta nada e o Delete leva tudo). Agora, sem malha,
  passa direto.
- Teste de todos os grupos que pedem objeto, **sem o objeto ligado**
  (comprimento médio do fio; referência 23,8 cm):

| Grupo | Antes | Depois da correção |
|---|---|---|
| GR Forma por Malha | pontas colapsam no centro da cabeça (10,9 cm) | passa direto |
| GR Comprimento até a Malha | **fio com 0 cm** | passa direto |
| GR Pentear por Curva | tudo em pé pela normal | passa direto |
| GR Corte pela Malha | **0 fios** | passa direto |
| GR Rabo de Cavalo, GR Trança Grossa, GR LOD por Câmera | funcionam sem objeto (só perdem a colisão ou o LOD) | igual |

  Padrão da correção, útil para qualquer grupo seu: Object Info do objeto
  → Domain Size (Point Count) → Compare > 0 → Switch (Geometry) entre a
  entrada e o resultado.

### 17.63 Node Bake: groom animado pesado em tempo real

Groom animado (GR Flutuar nas guias → Densidade 300 mil/m² → Mecha →
Cacho → Cor → Profile), 1,44 milhão de pontos. Node **Bake** no fim da
cadeia, modo Animation, quadros 1 a 12, alvo Disco:

| | Tempo por quadro na reprodução |
|---|---|
| Sem Bake | 353 ms |
| **Com Bake** | **9 ms** (39× mais rápido) |

- Bake de 12 quadros: 8 s. Disco: **282 MB** (23,5 MB por quadro nessa
  densidade). Para cena longa, faça o Bake **antes** do que multiplica
  pontos (antes do Cacho) ou baixe a densidade da viewport.
- Criado por script, o node Bake vem **sem item**: a saída fica vazia e o
  cabelo some. Na interface ele já vem com Geometry; por Python, adicione
  com `bake_items.new('GEOMETRY', 'Geometry')`.
- Operador: `object.geometry_node_bake_single` (session_uid do objeto, nome
  do modificador, bake_id), com `bake_mode = 'ANIMATION'` e intervalo
  próprio no item de bake do modificador.

### 17.64 Pelo pictórico (DreamWorks recente) [img/72_pictorico_sheet]

Aplicando os princípios coletados em `estilizado/artigo-dreamworks-puss-in-boots-fur.md`
e `estilizado/artigo-dreamworks-wild-robot-painterly.md` (cor por clump e
sub-clump como pincelada; pelo respondendo à luz como superfície contínua;
buracos entre grupos; guarda grossa como acento). Na criatura de 17.55:

1. **Normal da pele no fio.** Logo depois do Generate Hair Curves: Store
   Named Attribute `nsurf` (Vector, Curve) = saída Surface Normal. No
   shader: Attribute `nsurf` → Vector Transform (Normal, Object → World) →
   **Normal** de um Toon BSDF Diffuse (Size 0,55, Smooth 0,25).
2. **Cor em dois níveis.** Clump 2 cm → Random por `guide_curve_index` =
   `clump_a` (matiz: Color Ramp laranja → ocre). Clump 6 mm (sub-clump) →
   outro Random = `clump_b` (valor 0,75 a 1,15, multiplicado).
3. **Buracos.** Random Boolean 12% por clump grande → Delete Geometry.
4. **Guarda.** 1,5% dos fios, Trim 1,5×, raio 1,2 mm, cor escura, Join.

| Versão | Leitura |
|---|---|
| Principled Hair por fio | brilho e sombra fio a fio: textura, não pincelada |
| **Toon com a normal da pele + cor por clump** | a luz agrupa em massas grandes, como bola pintada; manchas de cor por tufo |
| + buracos e guarda | quebras de borda aparecem; a guarda escura quase não lê nessa escala (precisaria ser mais longa e mais rara) |

A normal da pele é o truque de maior efeito com menos nodes (2 no GN, 2 no
shader). Personagem que se move: o Vector Transform Object → World é o que
mantém certo.

### 17.65 Cel-shading de cabelo com a normal de uma malha lisa [img/73_normal_sheet]

A mesma ideia de 17.64 para cabelo humano estilizado. Em vez da normal do
fio (que acende fio a fio), o shader usa a normal da **malha proxy lisa**
em volta do cabelo (a de 17.39):

1. No fim da cadeia: Object Info (malha, Relative) → **Sample Nearest
   Surface** (Value = Normal da malha) → Store Named Attribute `nvol`
   (Vector, Point).
2. Shader: Attribute `nvol` → Vector Transform (Normal, Object → World) →
   Normal do Toon Diffuse **e** do Toon Glossy.

| Normal usada | Leitura |
|---|---|
| Do fio (padrão) | brilhos brancos espalhados fio a fio |
| `n_raiz` (normal do scalp) | chapado, pouco volume |
| **Da malha proxy** | um terminador de luz limpo no bob inteiro e um brilho em faixa: cel-shading |

Pronto em **GR Normal da Malha** (entrada Malha; sem malha passa direto) e
no material **GR Cabelo Cel** (lê `nvol`). Para pelo, ligue o próprio corpo
como Malha.

Também funciona em mecha de malha (17.56) [img/63_npr_cel]: GR Normal da
Malha **antes** da GR Mecha Chunky (o Curve to Mesh leva o atributo para a
malha), com uma esfera lisa de 12,5 cm como proxy. As mechas ganham um lado
claro e um escuro coerentes. Armadilha: o ahoge, que sai da esfera, ficou
escuro; tudo que deve receber a luz do volume precisa estar dentro ou
colado na malha proxy.

### 17.66 Cabelo embaixo do chapéu [img/74_chapeu_sheet]

Chapéu = copa (cilindro) + aba (disco), **objetos separados**. Depois da
mecha, um Shrinkwrap Hair Curves na cabeça (Above Surface 1, Offset 3 mm,
Lock Roots) com **Factor = máscara "acima da aba"**:

- Raycast na **copa**, direção (0,0,1): bate = ponto embaixo da copa.
- Raycast na **aba**, direção (0,0,−1): bate = ponto acima da aba.
- Boolean OR das duas → Factor.

| Máscara | Pontos atravessando a parede da copa |
|---|---|
| Sem ajuste | 1.568 de 154 mil |
| Raio para cima no chapéu inteiro (copa + aba juntas) | cabelo **inteiro** colado no crânio: embaixo da aba larga tudo "está sob o chapéu" |
| Raio para cima só na copa | 1.644: não pega o fio que sai pela parede lateral |
| **Copa para cima OU aba para baixo** | **0** |

O que está acima da aba cola no crânio (escondido pelo chapéu); o que está
abaixo cai normal.

### 17.67 Cabelo longo apoiado nos ombros [img/75_ombro_sheet]

Fio de 40 cm, tronco (elipsoide 44 × 24 × 32 cm) + pescoço num objeto só.
Shrinkwrap Hair Curves com Surface = **tronco**, Above Surface 0, Offset
4 mm, Smoothing 3, Lock Roots:

| Onde | Pontos dentro do tronco |
|---|---|
| Sem | **9,8%** (o cabelo some dentro dos ombros) |
| Nas guias e de novo no fim | 0,20% |
| Só no fim | 0,30% |

- O cabelo desliza pela superfície do ombro e apoia; não precisa de física
  para pose parada.
- Nas guias sai um pouco mais natural (os filhos já nascem entre guias
  apoiadas); no fim é o que garante zero.
- Mesma peça serve de colisão com roupa (gola, capuz): troque o Surface.

### 17.68 Forma da curva no Cycles muda a cor [img/77_shape_sheet]

Render Properties > Curves > **Shape**. A cena nova do bpy 5.2.2 vem em
**Rounded Ribbons**, e todo o laboratório (17.1 a 17.67) foi renderizado
assim. Mesmo groom (cachos, raio 0,8 mm, melanina 0,4), close, 24 amostras:

| Shape | Tempo | Luminância média do cabelo | Leitura |
|---|---|---|---|
| Rounded Ribbons | 18,4 s | **0,343** | dourado claro |
| 3D Curves | 24,3 s | **0,184** | castanho escuro, sombra própria entre fios |
| Linear 3D Curves | **11,9 s** | 0,216 | quase igual ao 3D, o mais rápido |

- **A diferença depende da escala do fio na tela.** Mesma cabeça em vista
  normal (fio de 0,5 mm, cabeça inteira no quadro, só o cabelo na medição):

| Melanina | Ribbons | 3D Curves com a mesma luminância |
|---|---|---|
| 0,2 | 0,347 | 0,2 (0,324) |
| 0,4 | 0,234 | 0,38 (0,230) |
| 0,6 | 0,176 | 0,56 (0,180) |
| 0,8 | 0,141 | 0,8 (0,138) |

  Na vista normal os dois ficam a menos de 7%: as receitas valem igual.
  Só em **close com fio grosso** (0,8 mm, cacho ocupando o quadro) o Ribbon
  sai quase 2× mais claro. Nesse caso, confira a cor em 3D Curves.
- Ribbon é uma fita virada para a câmera: some a sombra entre fios, o
  cabelo fica mais claro e mais chapado, o que já é meio caminho para o
  estilizado.
- Linear 3D Curves foi o mais rápido e ficou perto do 3D: bom para cacho
  grosso em close.

### 17.69 Comprimento pintado numa textura [img/78_comprimento_sheet]

Mesma cadeia da máscara por imagem (17.27), agora no comprimento. Depois do
Clump:

Named Attribute `surface_uv_coordinate` → Image Texture (a pintura) → Map
Range (0 → 1 vira **0,35 → 1,1**) → Evaluate on Domain (Curve) → **Trim
Length Factor** (Replace Length desligado).

- Branco = fio 10% mais longo, preto = 35% do comprimento. Qualquer imagem
  em cinza pintada no UV do scalp (Texture Paint, ou exportada do ZBrush
  como polypaint).
- Faixas alternadas no U deram camadas longas e curtas; gradiente deu um
  lado mais curto. O **layout de UV do scalp** decide onde cada faixa cai:
  pinte em cima do scalp, não no espaço de UV às cegas.
- Mais fino que vertex group (resolução da imagem) e reutilizável entre
  personagens com o mesmo UV de scalp.

### 17.70 Tamanho de mecha diferente por região [img/79_clumpreg_sheet]

O Guide Distance do Clump é um valor só. Para mecha larga no topo e fina
nas laterais: dois ramos da mesma Densidade Livre, GR Mecha Estilizada com
**3,5 cm** e com **8 mm**, misturados pela **GR Transição** com Fator =
Z da raiz → Map Range Smooth Step 3 → 7 cm. Os dois ramos têm a mesma
contagem de pontos (vêm do mesmo Interpolate), então a Transição funciona
sem Resample. A passagem entre regiões não mostra costura.

Serve para qualquer parâmetro "de valor único" por região: dois ramos +
Transição com uma máscara (vertex group, textura, posição).

### 17.71 Guias desenhadas com Grease Pencil [img/80_gpencil_sheet]

Desenhe poucos traços de Grease Pencil em volta da cabeça (no Blender,
placement Surface faz a raiz nascer no couro) e use como guias. No Curves
(Surface = scalp):

1. Object Info (o Grease Pencil, Relative) → **Grease Pencil to Curves**
   (Layers as Instances desligado) → Realize Instances → Resample 16.
2. **Set Attachment Surface** (Essentials 5.2): Surface Object = scalp,
   Surface UV Map = Named Attribute `UVMap`.
3. Daí em diante, a cadeia normal (GR Densidade Livre → Mecha → ...).

Resultado: **14 traços → 11,5 mil fios**, 184 mil pontos.

| Entre os traços e o Interpolate | Resultado |
|---|---|
| Nada | o Interpolate não gera filhos (só os 14 traços saem) |
| **Set Attachment Surface** | funciona |
| Attach Hair Curves to Surface (com ou sem Set antes) | fios de **1 ponto** (o mesmo problema de 17.1) |

**Achado de bastidor da 5.2:** o vínculo com o scalp não é só o Surface do
objeto Curves. Ele viaja num **Geometry Bundle** junto da geometria
(itens `surface_geometry` e `surface_uv_map`; ver
`essentials-internals/set-attachment-surface.md`). Curva que nasce fora do
objeto Curves (Grease Pencil, Curve comum, Mesh to Curve) chega sem esse
bundle, e o Interpolate não acha onde plantar. Set Attachment Surface cria o
bundle.

Nota de laboratório: em modo sem interface, só ter um Grease Pencil na cena
fez o Cycles tentar abrir EGL e o render parou; aplicar o modificador e
apagar o Grease Pencil antes do render resolveu. Na interface isso não
acontece.

Pronto em **GR Guias Desenhadas** (entrada Grease Pencil). O grupo tira o
scalp do próprio Curves vazio com **Get Attachment Surface** e passa para o
Set Attachment Surface em modo Geometry: o artista só liga o Grease Pencil.
Validado do .blend: 11.455 fios.

Vale para **objeto Curve comum** também (medido): 12 guias num Curve POLY,
Object Info → Interpolate dá **12** curvas (nenhum filho); com Set
Attachment Surface antes (Get Attachment Surface do Curves vazio, modo
Geometry) dá **10.412**. Então curvas extraídas de malha (Mesh to Curve de
mechas esculpidas no ZBrush) ou desenhadas como Bezier servem de guia pelo
mesmo caminho.

### 17.72 Biblioteca própria: Essentials traz utilitários linkados

Ao abrir `receitas_grooming.blend` fora do meu ambiente, **8 node groups
estavam linkados** por caminho relativo a arquivos da instalação usada no
laboratório: Curve Info, Curve Root, Curve Segment, Curve Tip, Get
Attachment Surface, Get Rest Geometry, Rest Surface (do
`procedural_hair_node_assets.blend`) e Edge Length (do
`geometry_nodes_essentials.blend`). São os utilitários que Interpolate,
Clump e cia. usam por dentro. Mesmo fazendo Append dos grupos do Essentials,
esses vieram como link.

- Corrigido: a biblioteca e os exemplos (`laboratorio/exemplos/`) agora são
  salvos depois de tornar tudo local (`make_local` em laço até não sobrar
  link, e as bibliotecas removidas). Conferido: 0 bibliotecas externas,
  exemplos renderizando.
- **Para quem monta biblioteca própria**: antes de mandar o .blend para
  outra máquina, olhe o Outliner no modo Blender File. Se aparecer alguma
  Library apontando para a pasta de instalação, torne os dados locais antes
  de salvar. (Não testei se uma instalação 5.2 diferente reencontra esses
  links sozinha; tornar local elimina a dúvida.)

### 17.73 Despenteado controlado (bedhead) [img/84_despenteado_sheet]

Cabelo curto (13 cm) de guias procedurais. A bagunça vai **nas guias**
(200 curvas de 12 pontos, custo quase zero), antes do Shrinkwrap e do
Interpolate, para as mechas continuarem coesas:

| Nível | Node nas guias | Leitura |
|---|---|---|
| 0 | nenhum | penteado |
| 1 | Rotate Hair Curves, Random Offset 0,5 rad | mechas apontando para lados diferentes |
| 2 | + Hair Curves Noise, 2 cm, Scale 6, Offset per Curve 1 | forma quebrada, ainda em mechas |
| 3 | + GR Strays em Arco 6% (nos filhos) | "acabei de acordar" |

Bagunça nos **filhos** (depois do Interpolate) quebraria as mechas por
dentro e custaria por ponto; nas guias, a Mecha Estilizada ainda junta tudo.
Um Integer ligado nos Seeds sorteia outra bagunça.

### 17.74 Dreadlocks estilizados [img/85_dreads_sheet]

Uma dread = um fio grosso de malha. GR Guias Procedurais (30 cm) → GR
Densidade Livre com só **2.200/m²** (~110 dreads) → GR Onda S → **GR Mecha
Chunky com Achatamento 1** (tubo redondo), raio 7 mm, torção 0, 48 pontos →
relevo: Noise Texture (Scale 180, Detail 3) na posição → Map Range ±1,2 mm →
Normal × valor → Set Position Offset. Scalp pintado escuro. 62 mil faces.

| Versão | Leitura |
|---|---|
| Onda S padrão (período 10 cm, 1,5 cm) | ondas miúdas: parece macarrão |
| **Período 25 cm, amplitude 1 cm** | cordas pesadas caindo: dread |

- A Onda S é calibrada para mecha de fio fino; em peça grossa, aumente o
  período com a espessura.
- Cor: Principled BSDF marrom 0,06 com roughness 0,75 ainda leu marrom
  médio acinzentado; para dread escura, baixe a cor base (≈0,03) ou use o
  GR Cabelo Cel com a normal de uma casca (17.65).

### 17.75 Tranças box (muitas tranças finas) [img/86_box_sheet]

GR Guias Procedurais (34 cm) → GR Densidade Livre (400 mil/m², **Guias
por fio 1**) → GR Trança Grossa com **Tamanho da trança 1,5 cm**, raio 4
mm, Cruzamentos 6, Começa em 0,03, cabeça ligada. ~21 mil fios, 940 mil
pontos. Scalp pintado escuro.

**Bug da biblioteca achado aqui:** a GR Trança Grossa tinha o Guide Distance
interno do Braid **fixo em 0,3 m** (feito para o rabo de cavalo, onde todos
os fios vão numa trança só). Na cabeça inteira, isso juntou tudo **numa
única trança**. Agora o grupo expõe **Tamanho da trança** (padrão 0,3, o
comportamento antigo; ~1,5 cm para tranças box). Regressão das tranças
antigas: sem mudança.

- Guias por fio 1 no Interpolate: cada filho segue uma guia só, e a trança
  não mistura duas guias vizinhas.
- Auditoria de valores fixos nos outros grupos: só sobraram Offset do
  Shrinkwrap (4 a 6 mm, intencional) e o Guide Distance 0,1 do Curl dentro
  da GR Cacho por Mecha. Medido: com Existing Guide Map ligado, trocar esse
  valor para 0,01 mudou **0,0** na geometria. Ele é ignorado.

### 17.76 Barba longa: fio contra blocos [img/89_barba_sheet]

Região da barba recortada da cabeça (17.32), GR Guias Procedurais como
gerador (7 a 8 cm, para fora 0,6 a 0,7, **Para trás −0,3** = para frente,
gravidade 1,4 a 1,5).

| Versão | Nodes depois das guias | Leitura |
|---|---|---|
| Fio | 600 mil/m², Clump 8 mm, raio 0,4 mm, Principled Hair | barba cheia, realista estilizada |
| Blocos | 4.000/m² → GR Mecha Chunky (raio 1,2 cm, torção 0,15) → GR Normal da Malha (cabeça) → GR Cabelo Cel → GR Contorno 2 mm | barba de desenho em placas |

Na versão em blocos, a normal da cabeça embaixo do queixo aponta para
baixo, e a barba toda ficou no lado escuro do Toon. Para barba, use como
Malha da GR Normal da Malha uma esfera/casca na frente do rosto (a barba
"olha" para a câmera), não a cabeça.

### 17.77 O mínimo de nodes que ainda é um groom estilizado [img/90_minimo_sheet]

Mesmas guias, 12,8 mil fios:

| Nodes | Cadeia | Avaliação | Leitura |
|---|---|---|---|
| 4 | Value → Interpolate → Set Hair Curve Profile → Set Material | 23 ms | massa lisa, "peruca" |
| **5** | + **Clump Shape 0,25** | 46 ms | **mechas de desenho**: já é estilizado |
| 7 | + Curl (Sub 2) + Roll (Sub 0) | 646 ms | cachos com ponta virada |

O Clump é o node que mais muda a leitura por custo. Tudo depois dele é
personalidade. O salto de custo vem do Curl (Subdivision multiplica
pontos, 17.14 e 17.54): comece a sessão com os 5 nodes e ligue o Curl no
fim.

### 17.78 Cabeça de raposa: comprimento e cor por região [img/91_raposa_sheet]

Cabeça com focinho e orelhas (cones) numa malha com UV. Generate Hair
Curves 120 mil/m² (2 cm) → GR Pentear por Curva (curva reta do focinho para
trás) → **comprimento por região**: Length Factor = 1 + 2,2 × max(bochecha,
ponta da orelha), com bochecha = Smooth Step de \|X\| (6 → 9,5 cm) ×
Smooth Step de Z (2 → −3 cm) e ponta da orelha = Smooth Step de Z (15 → 17,5
cm) → Clump 8 mm → atributos `branco` (queixo e peito) e `orelha` (ponta)
para o shader. 23,5 mil fios, 141 mil pontos, render 720 px em 10 s.

- Leu como raposa: o redemoinho do focinho vem da curva de fluxo, e o
  **tufo na ponta da orelha** saiu da máscara de altura.
- Os atributos estavam certos (6.406 fios `branco`, 201 `orelha`), mas **não
  apareceram**: com Principled Hair, melanina 0,02 e redness 1 continua
  laranja-claro, e a ponta com +0,5 de melanina não contrastou sob luz de
  cima. Zerar a redness onde é branco ajudou pouco. Para manchas de cor bem
  definidas em estilizado, use Principled BSDF ou Toon com Color Ramp nos
  atributos (17.15, 17.64), não a melanina.
- O branco embaixo do queixo fica na sombra: em personagem, ponha a região
  clara onde a luz principal bate, ou compense com emissão/luz de preenchimento.
- **Confirmado** refazendo só o material: Toon Diffuse (Size 0,6, Smooth 0,2)
  com cor = Mix(laranja, creme, `branco`) → Mix(…, quase preto, `orelha`) e
  Normal = `nvol` da GR Normal da Malha com o corpo. Laranja saturado, queixo
  branco e ponta da orelha escura aparecem [img/finais/91_raposa_toon].

### 17.79 GR Máscara por Posição [img/92_lib_mascara]

A máscara "caixa suave pela raiz" apareceu em seis receitas (meio preso,
orelha, mecha por região, raposa, chapéu, mecha branca). Virou grupo de
campo: **GR Máscara por Posição**, entradas Altura mín/máx, Lateral mín/máx
(\|X\|), Frente mín/máx (Y), Borda suave, Inverter; saída 0 a 1 por fio.

Ligue a saída no Fator da GR Transição, no Length Factor do Trim (via Map
Range), no Factor de Clump/Curl/Shrinkwrap ou num Store Named Attribute
para o shader. Validado: Altura mín 5 cm, Trim 100% → 40% = topo curto;
8.833 fios na máscara, 4.842 fora, 1.775 na borda suave.

### 17.80 Moicano com três grupos prontos [img/93_moicano]

Da mesma GR Densidade Livre (350 mil/m²), dois ramos:

- **A, raspado**: Trim Replace Length 6 mm → Shrinkwrap na cabeça (Above 0,
  Offset 2 mm) → Resample 12.
- **B, crista**: GR Comprimento até a Malha (elipsoide 3 × 16 × 20 cm sobre
  a linha do meio, Viés (0,0,0,8), 12 pontos) → GR Mecha Estilizada 1,5 cm.

GR Transição (A, B) com Fator = **GR Máscara por Posição** (Lateral máx
1,8 cm, Altura mín 2 cm, borda 6 mm). 18 mil fios, 217 mil pontos.
Scalp pintado. A crista abre em leque porque o viés para cima se soma à
normal do crânio; para crista em lâmina reta, zere o X da direção (Viés
maior ou uma malha mais fina).

### 17.81 Undercut masculino estilizado [img/94_undercut_sheet]

GR Guias Procedurais (12 cm; topete: para fora 0,9, lado 0,2, para trás 0,8;
de lado: para fora 0,6, lado 1,0) → Densidade 350 mil/m² → GR Volume na
Raiz → GR Mecha Estilizada 1,8 cm → Trim com Length Factor = Map Range(GR
Máscara por Posição invertida → 1 a 0,05) → Cor por Mecha. 18 mil fios.

| Máscara do topo | Resultado |
|---|---|
| Só altura > 5,5 cm | laterais continuam compridas: nesta cabeça quase todo o scalp lateral está acima disso |
| **Altura > 7,5 cm e \|X\| < 5 cm** | laterais raspadas (5%), topo inteiro |

A máscara de undercut precisa limitar a lateral (\|X\|), não só a altura.
Scalp pintado escuro faz o raspado ler como sombra de cabelo curto.

Refeito com **hair cap realista** (desce até 7 cm abaixo do centro na nuca,
recorta rosto e orelhas) [img/94_cap_sheet]: mesmo node tree, 22,6 mil
fios; nuca e laterais raspadas aparecem inteiras por trás. Confirma o
limite anotado no início da seção 17: a receita estava certa, o scalp de
teste é que era curto.

A GR Rabo de Cavalo também foi refeita na hair cap real [img/95_pony_cap_sheet]:
os fios da nuca sobem até o elástico e cobrem a parte de trás (19,4 mil
fios contra 15,7 mil). Nenhum ajuste no grupo.

### 17.82 Cacho em cabelo curto [img/96_curto_sheet]

Fio de 7 cm, hair cap real, 450 mil/m² (29 mil fios, 1,3 M pontos), mecha
1 cm, GR Cacho por Mecha com raio 4 a 6 mm:

| Voltas por metro | Voltas no fio | Leitura |
|---|---|---|
| 20–36 (padrão do grupo) | 1,5 a 2,5 | textura crespa miúda |
| 45–60 | 3 a 4 | igual |
| 70–90 | ~5 a 6 | igual, só mais densa |

As três leram quase iguais. Em fio curto, o **raio do cacho em relação ao
comprimento** manda: raio de 5 mm num fio de 7 cm já é 7% do comprimento,
e qualquer número de voltas vira textura. Para textura crespa, o padrão
basta.

**Medido**: raio 9 a 12 mm (~15% do comprimento), 14 a 20 voltas/m (~1
volta) e mecha 1,8 cm → **cachinhos de desenho separados**, cada mecha um
cacho. É o controle certo para cabelo curto cacheado estilizado.

### 17.83 Pelo arrepiado (susto) animado por um valor [img/97_arrepio_sheet, 97_arrepio.gif]

A fonte da DreamWorks (`estilizado/artigo-dreamworks-puss-in-boots-fur.md`,
princípio 5) diz que o groom estilizado continuou respondendo à pose, com o
pelo "em pé" no susto. Em GN isso é **um input**: o Levanta da GR Pentear
por Curva, animado.

Scene Time Seconds → Map Range **Smooth Step** (0,3 s → 0,6 s vira 0,3 →
0,95) → Levanta. Criatura pictórica de 17.64, 27,5 mil fios. O pelo sai de
deitado para em pé em 0,3 s e a silhueta incha, sem simulação.

Na animação real, troque o Scene Time por um **controle na viewport**
(testado): um Empty "CTRL_susto" → Object Info (Original) → **Scale Z** →
Map Range 1 → 2 vira 0,3 → 0,95 → Levanta. Keyframes na escala do Empty
(1 no quadro 8, 2 no 16) arrepiaram o pelo igual [img/97b_arrepio_ctrl.gif].
O animador mexe num objeto da cena, sem abrir o node tree; o Empty pode
ser filho do rig.

### 17.84 Mão ou objeto passando pelo cabelo [img/98_pente.gif]

Sem física: um Empty (a "mão", com uma esfera de 3,5 cm filha dele) empurra
os pontos para fora. Depois da Mecha:

Object Info (Empty, Relative) → Position − Location → Length e Normalize →
penetração = max(R − distância, 0), R = 4,5 cm → Set Position Offset =
direção × penetração → Shrinkwrap na cabeça (Above 0).

Pontos dentro da esfera, medido:

| Quadro | Sem desvio | Com desvio |
|---|---|---|
| 25 (mão ao lado do cabelo) | 1.773 | **0** |
| 13 (mão encostada no crânio) | 1.747 | 650 |

No quadro 13, o Shrinkwrap depois devolve os fios para fora da cabeça,
para dentro da mão: cabeça e mão disputam o mesmo espaço. **Desvio depois
do Shrinkwrap**: 0 pontos dentro nos dois quadros (medido). Animar o Empty
basta; 7 nodes.

Pronto em **GR Desviar de Objeto** (Objeto, Raio). Validado do .blend: 0
pontos dentro de 4,4 cm do Empty. Serve para ombro, gola, mão, chapéu
redondo: um Empty no centro e o raio certo.

### 17.85 Anel de brilho de anime [img/99_anel_sheet]

Sobre o GR Cabelo Cel (17.65), uma faixa de brilho desenhada, que não
depende da luz. No shader:

1. Texture Coordinate **Object** → Z + 3 × (x² + y² + z²) (a faixa desce
   nas laterais acompanhando a curva do crânio) → Map Range −0,1 → 0,2.
2. Color Ramp **Constant**: preto, branco de 0,52 a 0,57, preto.
3. Rampa → Strength de uma Emission rosa-clara (0,8) → Add Shader com o Toon.

| Faixa lida em | Resultado |
|---|---|
| Hair Info **Intercept** (0,22 a 0,30 do fio) | degraus: cada fio começa numa altura diferente |
| **Coordenada do objeto** | arco contínuo contornando a cabeça |

O anel fica preso à cabeça e se move com ela (coordenada do objeto). Nada
no Geometry Nodes: só o material.

### 17.86 Franja reta ou em bicos pela malha de corte [img/100_franja_sheet]

GR Corte pela Malha com uma esfera (20 × 20 × 25 cm) sem as faces da frente
abaixo de Z = 3,5 cm: o fio que desce na frente passa da malha nessa altura e
é cortado. Franja em bicos: a altura da borda varia em seno ao longo do X
(3,5 cm − 1,5 cm × \|sen(140 x)\|). 19,4 mil fios, fio 30 cm.

- A malha de corte desenha **o corte inteiro**: no teste, a esfera de 20 cm
  também cortou as costas na altura do queixo (virou um bob com franja).
  Modele a malha como o contorno final do penteado, frente e costas.
- Mais simples que a franja por região de 17.24 quando o corte é "de
  tesoura" (reto ou serrilhado); a de 17.24 serve para franja que muda de
  direção.

### 17.87 A biblioteca é local ao objeto (e a gravidade também)

Cadeia Guias Procedurais → Densidade → Mecha → Volume → Ponta Virada →
Onda S, com cabeça, scalp e cabelo filhos de um Empty. Diferença máxima na
posição local de cada ponto em relação ao conjunto na origem:

| Conjunto | Diferença máxima |
|---|---|
| Deslocado (0,6; 0,3; 1,5 m) | **0** em todos os grupos |
| Girado (25° em X, 60° em Z) | 0,0000002 m até a Ponta Virada; 0,08 mm depois da Onda S (arredondamento) |

Mover ou girar o personagem **não muda o groom**. Consequência: a
"gravidade" da GR Guias Procedurais e da GR Rabo de Cavalo é o **−Z do
objeto**, não do mundo. Personagem modelado em pose deitada ou com a
cabeça inclinada na pose de repouso recebe gravidade inclinada junto.
Modele a cabeça em pé; para cabelo que cai com o mundo em cena animada,
use a física (17.25) ou o Simulation to World vazio (17.26).

Nova entrada **Gravidade do mundo** na GR Guias Procedurais
[img/102_gravmundo_sheet]: Self Object → Object Info (Original) → Rotation
→ Invert Rotation → Rotate Vector aplicado ao vetor de gravidade. Com a
cabeça girada 50°, o deslocamento médio raiz → ponta em X foi de −43,7 cm
(gravidade do objeto, cabelo inclinado junto) para **+3,2 cm** (reto para
baixo). Ela lê a rotação do objeto: serve para pose de repouso inclinada;
animar a rotação reposiciona o cabelo quadro a quadro, sem inércia.

### 17.88 Balanço de caminhada com follow-through, sem física [img/103_balanco_sheet, 103_balanco_2.5.gif]

Nas guias (Resample 24), antes do Interpolate. Vector Rotate eixo Y,
Center = Root Position, Angle = **0,35 × s × sen(2π t / 1 s − atraso × s)**,
com s = Spline Parameter e t = Scene Time Seconds. Depois Shrinkwrap na
cabeça.

| Atraso | Leitura |
|---|---|
| 0 | pêndulo rígido: o cabelo gira em bloco |
| **2,5 rad** | a ponta chega depois da raiz; o fio faz curva em S (follow-through) |

Período 1 s = um passo por lado a 24 fps. Para sincronizar com a
animação, troque o Scene Time por um valor do rig (o controle por Empty de
17.83). Nove nodes, custo de nada (feito nas guias).

Pronto em **GR Balanço** (Amplitude, Período, Atraso, Eixo). Validado do
.blend: ponta média em X nos quadros 1, 7, 13 e 19 = +7,7; +6,2; −6,7;
−5,2 cm (ciclo de 1 s).

### 17.89 Linha do cabelo suave (hairline) [img/104_hairline_sheet]

A borda do scalp recortado dá uma linha seca na testa. Campo no **Density
Mask** do Interpolate: Position → d = Z − Y (cresce para frente e para
baixo) → Map Range clamp 0,09 → 0,125 vira **1 → 0,08**. Os últimos ~3,5 cm
antes da testa afinam até 8% da densidade. 28,9 mil → 25,5 mil fios.

- O Density Mask aceita campo (lido nos pontos da distribuição): não
  precisa de vertex group. Com vertex group pintado, é o mesmo socket.
- Numa cabeça real, troque a fórmula por distância até a borda (vertex
  group com gradiente, ou Geometry Proximity até uma curva da hairline).

**Babyhairs**: um segundo Interpolate das mesmas guias, Density Mask = só a
faixa da borda (Map Range 0,112 → 0,124 vira 0 → 1), Trim Replace Length
2,5 cm com Random Offset 1 cm, Noise 4 mm Scale 40 → Join com o cabelo.

| Densidade do ramo baby | Leitura |
|---|---|
| 900 mil/m², faixa 2 cm | faixa de penugem que esconde a hairline |
| **150 mil/m², faixa 1,2 cm** | fiozinhos soltos na borda |

### 17.90 Vibrissas (bigode de animal) [img/finais/91_raposa_vibrissas]

Região recortada do focinho (20 faces dos dois lados), um Curves com Surface
nela e só a **GR Guias Procedurais** como gerador: Comprimento 9 cm, Para
fora 1, Para o lado 1,2, Para trás 0,4, Gravidade 0,3, **12.000 guias/m²**
(26 fios). Set Hair Curve Profile raio 0,6 mm, **Shape 0,9** (afina quase
até zero). Material claro separado. Sem Interpolate: poucas vibrissas
grossas leem melhor que muitas finas.

### 17.91 Franja cortina [img/106_cortina_sheet, 107_cortina_sheet]

Máscara por Posição na frente (Y < −4,5 cm, Altura > 3 cm) → Trim para 42%
na máscara → abrir para os lados.

| Como abrir | Resultado |
|---|---|
| GR Ponta Virada "para fora" na máscara | **falhou**: na frente do topo a raiz aponta para cima, o "para fora" enrola para cima e a franja virou um tufo espetado |
| Offset = sinal(X da raiz) × s^1,5 × 6 cm × máscara, + Shrinkwrap | a franja aparece e cobre a testa, mas o "V" da cortina ainda é fraco |

Para a cortina de verdade faltam: risca no meio (scalp em duas ilhas, 17.13)
e o empurrão lateral crescer mais cedo no fio. Testado s^0,6 × 9 cm: abre
um pouco mais no centro, mas a franja fica rala e sem o "V" limpo.

Terceiro passo: **scalp em duas ilhas** (17.13) + GR Lado da Risca no Group
ID da Mecha + Para o lado 0,6 nas guias. Sai um "V" limpo no meio e o
cabelo emoldura o rosto, mas a parte curta da franja fica escondida nas
laterais. Resultado: risca central com moldura, ainda não a cortina curta.
Testada a máscara só perto da risca (\|X\| < 3,5 cm, frente, topo):
visual praticamente igual. Diagnóstico: **a direção das guias domina**; com
Para o lado 0,6, os fios da risca já saem para os lados e o Trim só os
encurta lá. A franja cortina precisa de **guias próprias** caindo sobre a
testa e abrindo em arco (um segundo conjunto de guias procedurais, ou
guias desenhadas 17.71, misturado pela GR Transição com a máscara).

**Resolvido assim** [img/107_cortina_sheet]: do mesmo Curves vazio, dois
ramos GR Guias Procedurais → GR Densidade Livre → Resample 24:
- A, cabelo: 30 cm, para fora 0,35, lado 0,6, para trás 0,2, gravidade 2,2;
- B, franja: **14 cm, para fora 0,5, lado 1,1, para trás −0,9 (para
  frente), gravidade 1,4**.

GR Transição (A, B) com Fator = GR Máscara por Posição (frente Y < −3 cm,
altura > 3,5 cm, \|X\| < 5 cm), depois Mecha com GR Lado da Risca e scalp
em duas ilhas. Mechas curtas saem da risca e abrem em arco pelos lados da
testa. Funciona porque os dois ramos saem do **mesmo scalp com o mesmo
seed**: o Interpolate distribui as raízes igual e a contagem de pontos bate.
Medido: A e B com 20.869 fios e 500.856 pontos, diferença máxima entre as
raízes **0 mm**. A distribuição depende do scalp, da densidade e do seed,
não das guias.

### 17.92 Resample por comprimento em corte de camadas [img/108_resample_sheet]

Topo cortado a 12% (Máscara por Posição + Trim), resto 30 cm, Onda S
depois do Resample:

| Resample | Pontos | Avaliação | Visual |
|---|---|---|---|
| Count 24 | 1,36 M | 187 ms | — |
| **Length 1,25 cm** | 1,27 M | 171 ms | igual |

Ganho pequeno (7%) porque só o topo é curto. Count fixo gasta os mesmos
pontos em fio de 3 cm e de 30 cm; em pelo com comprimentos muito
diferentes (17.78, bochecha 2,2× e corpo 1×) ou com muitos fios curtos, o
modo Length rende mais. Regra: Resample **Length** quando o Trim deixa
comprimentos muito variados; Count quando o corte é uniforme.

### 17.93 Exportar o groom: Alembic ou USD

Objeto Curves com a cadeia (Densidade → Mecha → Onda S → Profile), File >
Export > Alembic, só o selecionado, avaliação Render, 1 quadro:

| | Antes | Depois de reimportar |
|---|---|---|
| Fios / pontos | 7.653 / 260.202 | 7.653 / 260.202 |
| Raio médio | 0,254 mm | 0,254 mm |
| Atributos | UVMap, guide_curve_index, id, n_raiz, position, radius, resolution, surface_uv_coordinate | **só position, radius, resolution** |

Export em 0,11 s, 4,2 MB. A geometria e a espessura chegam intactas; os
atributos de grooming **não** vão. Testado também atributo de cor (Color,
Point e Curve), 2D Vector e Float, com Vertex Colors, UVs e Custom
Properties ligados no exportador: **nenhum** sobreviveu no Alembic.

**USD** (File > Export > USD, só selecionado, avaliação Render): 0,64 s,
8,7 MB, e voltaram **UVMap, cor_mecha, cor_curva, guide_curve_index, n_raiz,
peso, surface_uv_coordinate, uv_teste** (só `id` e `resolution` ficaram).
Para levar o groom com cor por mecha e máscaras, use USD.

### 17.94 Tempo de render contra quantidade de fios

Cycles CPU (4 núcleos), 540 px, 32 amostras, cabeça inteira no quadro, fio
de 26 cm com mecha:

| Fios/m² | Fios | Render |
|---|---|---|
| 50 mil | 2,4 mil | 5,1 s |
| 150 mil | 7,6 mil | 6,6 s |
| 450 mil | 23 mil | 8,2 s |
| 1,35 M | 70 mil | 11,4 s |

28× mais fios custaram 2,2× o tempo: o render de curvas no Cycles escala
bem abaixo do linear (BVH). O custo pesado está na **avaliação do Geometry
Nodes e na memória** (17.14, 17.54), não no render. Para agilidade, economize
pontos na cadeia antes de economizar fios no render.

### 17.95 Sobrancelha expressiva por um Empty [img/113_sobrancelha_sheet]

Sobrancelha de 17.32 (GR Guias Procedurais na região, 900 mil/m², Clump 4
mm) + um Empty "CTRL_sobrancelha". Depois do Clump, Set Position Offset Z =

- **levantar**: (Escala Z − 1) × 1,2 cm;
- **franzir**: (Escala X − 1) × −1 cm × Map Range(\|X\| do ponto, 1,2 → 5 cm
  vira 1 → 0) (só a ponta interna desce).

Escala (1,1,2) = surpresa, (2,1,1) = bravo. O animador anima o Empty.
Ressalva: o offset move a raiz junto e a sobrancelha **descola** da pele. Em
toon isso passa (sobrancelha "flutuando" é convenção); para ficar colada,
anime a pele com shape key e use Deform Curves on Surface (17.46).

Testado com a raiz presa (offset × Spline Parameter) [img/113b_sobrancelha_sheet]:
a "surpresa" vira sobrancelha **arrepiada** (os fios levantam, a forma não
sobe) e o "bravo" quase não lê. A expressão vem de mover a forma inteira;
mexer só nos fios serve para textura (susto, 17.83), não para expressão.

**Forma de produção, validada** [img/113c_sobrancelha_sheet]: shape keys na
malha da região da sobrancelha ("surpresa": +1 cm em Z; "bravo": ponta
interna −9 mm), Add Rest Position ligado nela, Deform Curves on Surface no
fim da cadeia. As três expressões leem e a raiz fica a **0,3 mm** da pele
deformada em todas. Numa cabeça real, a região é parte da malha do rosto e
usa as mesmas shape keys do rig facial.

### 17.96 Personagem final: cortina + balanço [img/114_final_sheet, finais/114_final_cortina, 114_final.gif]

Integração das receitas novas, só biblioteca: HairCap real em duas ilhas;
dois ramos (cabelo 32 cm e franja 14 cm, 17.91), cada um com Resample 24 →
**GR Balanço** → Shrinkwrap → Densidade 260 mil/m² → Resample 24; GR
Transição com GR Máscara por Posição; Mecha com GR Lado da Risca; Cor por
Mecha; sobrancelha por região. 18 mil fios, 434 mil pontos, 900 px em 94 s.

Na primeira versão, dois erros de ordem que as regras já previam:
- **GR Strays em Arco depois de um Resample 24** (os filhos tinham 12
  pontos): o Noise cumulativo dobrou e os strays explodiram (regra 5).
- Balanço com amplitude 0,22 rad: no quadro 7 a franja cobria o rosto.
  0,12 rad é o limite para franja curta não invadir o olho.

### 17.97 Cílios cartoon: raiz em linha fina, direção variada [img/116_cilios_linha_fina_sheet; histórico em img/115_cilios_palpebra_sheet]

Duas críticas do Vini (2026-09-28), nesta ordem:
1. Sobre o 17.36: "o scalp é como uma edge, não tem geração em outros
   eixos, só na horizontal". Os cílios saíam como pente: todos com a mesma
   direção, porque a faixa na esfera do olho tem as normais quase iguais.
2. Sobre a primeira correção, com a margem inteira da pálpebra como scalp
   (faixa de −10° a 90°, 2,8 mm): "estão com profundidade. Tem que ser
   uma linha fina". A raiz tem que ser um traço de delineador. A
   variação vai na **direção** do fio, não na posição da raiz.

Receita final, sem node novo:

1. **Scalp = um loop fino na quina da margem da pálpebra**, do lado de
   fora, com menos de 1 mm de largura. No lab foi o tubo da margem (raio
   1,6 mm) só entre 25° e 45°, o que dá 0,56 mm (0° = para fora do olho,
   90° = para a abertura). A quina arredondada já inclina a normal para a
   frente.
2. **Confira a normal**: Face Orientation azul para fora. Com a normal
   invertida os fios nasceram para dentro da pálpebra.
3. **Densidade alta para compensar a área pequena**: 9 milhões/m² deu 318
   cílios por olho, contra 74 com 2 milhões.
4. GR Guias Procedurais: Para fora 1, 12 mm, sem Cabeça (colisão). Com
   colisão, o offset de 6 mm do Shrinkwrap achatou os cílios para trás.
5. **Gravidade aleatória por cílio** (3 nodes ligados no input Gravidade
   da GR Guias Procedurais): Index → Evaluate on Domain (Curve, Integer) →
   Random Value Float, com Min −0,4, Max −2,2 e o ID vindo do Evaluate. É
   isso que tira o pente com a raiz fina: uns cílios vão para a frente,
   outros sobem. O input do grupo aceita field.
6. **Canto externo mais longo** (4 nodes): Curve Root → Separate X → Map
   Range Smoothstep (X do canto interno → X do externo, 0,5 → 1) → Trim
   Hair Curves Length Factor, com Replace Length e Scale Uniform
   desligados. **Random Offset do Trim é distância**: 0,002 (2 mm) quebra
   a borda; 0,15 apagou quase todos os cílios.
7. **Tufos**: Clump Hair Curves com Guide Distance 1,8 mm, Shape 0,3 e Tip
   Spread 0,2 mm. Profile com raio 0,3 mm e Shape 0,8.

| Variante | Cílios por olho | Resultado |
|---|---|---|
| Faixa na esfera (17.36) | 65 | pente: uma direção só |
| Margem inteira, −10° a 90° | 333 | cheio, mas a raiz tem profundidade (rejeitado) |
| Linha fina, gravidade fixa, 2 milhões/m² | 74 | ralo e volta a parecer pente |
| **Linha fina + gravidade −0,4 a −2,2 + 9 milhões/m²** | 318 | traço fino na raiz, tufos em direções variadas |
| + Random Offset 2 mm | 318 | borda irregular, mais desenhada |
| Chunky: Clump 3 mm, raio 0,5 mm, gravidade −0,6 a −2,4 | 250 | poucas pontas grossas, raiz fina |

Gravidade fixa, medida com a normal certa: −0,6 deixa os cílios quase
retos para a frente, −1,3 dá a curva para cima do cartoon e −1,8 deixa os
tufos quase verticais.

Script: `laboratorio/scripts/r115_lash_lid.py`, com as variantes a a e e
as variáveis de ambiente PSI, GRAV, RG, ROFF, DENS, COL e SIDE.
