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
- **Existing Guide Map desligado no Clump e no Curl.** Chow desligou só no
  Clump e o Curl seguiu as guias esparsas antigas, dando "permanente"
  indesejado. Os dois têm que falar a mesma língua. Com o toggle desligado, a
  densidade dos clumps sai da Guide Distance, sem plantar guia à mão.
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
  Random → Map Range (ex. 0,4 a 1,0) → Factor. Por fio, sem Create Guide
  Index Map; da o visual de fios escapando da mecha. Random por mecha (Random
  Value com ID = Guide Index) e outro efeito, mais raro. Tip Spread e Clump
  Offset ja sao aleatorios por dentro, so o Seed do Clump. Para ver em cores:
  Map Range → Color Ramp → Viewer (Ctrl+Shift+clique), com a geometria do
  Viewer vinda da saida do Clump. Curve Info nao tem Seed: Math Add + Fraction
  antes do Map Range, ou Random Value com ID vazio e Seed.
- **Named Attribute nao le `.selection`.** Atributo interno com ponto no nome
  volta zero. A selecao do Sculpt nao entra no tree diretamente.
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
| Curl virou "permanente" | Curl seguindo guide map antigo | Existing Guide Map desligado no Clump e no Curl | pal/bcon2026-steve-chow-...md |
| Textura ligada no Trim não faz nada | Input não ligado no editor | Entrar no grupo e ligar a textura no input certo | pal/bcon2026-steve-chow-...md |
| Pelo denso escuro por dentro | Sombra sólida entre camadas | Transparent BSDF por Light Path no shader | pal/bcon2026-steve-chow-...md |
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

---

## 17. Laboratório: receitas testadas em bpy 5.2.2 (2026-09-28)

Tudo aqui foi renderizado em Cycles numa cabeça de teste em **escala real**
(raio 10 cm, scalp 0,052 m², fios de 24 a 28 cm, 160 a 220 guias). Os valores
valem direto para uma cabeça humana em metros. Scripts em
`Blender Hair Geometry Nodes/laboratorio/scripts/`, folhas de contato em
`laboratorio/img/`. Cada receita cita a folha.

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

Catorze node groups "GR" e dois materiais, marcados como asset, feitos com as
receitas desta seção e validados abrindo o .blend do zero:

- GR Densidade Livre, GR Mecha Estilizada, GR Lado da Risca, GR Strays em
  Arco, GR Cacho por Mecha (em voltas por metro), GR Onda S, GR Cor por
  Mecha, GR Mecha Chunky, GR Ver em Cores, GR Ponta Virada, GR Trança
  Grossa, GR Corte por Região, GR Pelo em Tufos, GR Volume na Raiz (14 grupos)
  [img/21_lib_sheet, 23_lib2_sheet].
- Materiais GR Cabelo Cor por Mecha e GR Cabelo Toon.

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
