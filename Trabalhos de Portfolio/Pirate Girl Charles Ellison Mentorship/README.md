# Pirate Girl, Mentoria Charles Ellison

Personagem estilizada para animação ou game, baseada em concept 2D do próprio
Charles Ellison (Character Art Director, Warner Bros. Animation). As sessões em
grupo já acabaram. Falta a one-on-one final de portfólio com o Charles, e é
pra ela que essa peça precisa chegar pronta.

## Personagem

- Jovem adulta, expressão ladina e confiante, boca aberta em risada, sobrancelha arqueada.
- Cabelo loiro em dois coques enormes. É o shape primário da cabeça e domina a silhueta.
- Colete de couro marrom com amarração dourada, blusa branca bufante, lenço vermelho,
  capa turquesa curta com forro de tentáculos, cinto largo com fivela de polvo, shorts
  marrom de barra rasgada, meia listrada laranja em uma perna só, botas dobradas.
- Props: tubo de ensaio na mão, garrafa bojuda no quadril, frasco menor no cinto. Líquido azul.
- Companion: polvo turquesa de olhar entediado agarrado ao ombro e braço.
- Pose: contrapposto, quadril deslocado, mão erguida com o tubo.

## Régua de qualidade (estilo Charles)

- Appeal acima de tudo. Formas grandes, limpas, legíveis. Primário, secundário, terciário.
- Silhueta que lê em preto.
- Olhos como ponto focal, emoção legível à distância.
- Lookdev polido, superfície limpa, sem ruído de detalhe.
- Regra-mãe: se um detalhe não reforça apelo, leitura ou história, ele sai.

Aplicada ao cabelo: os dois coques são forma primária. Os fios são textura em
cima da forma, não a forma. Se um passe de fio (noise, frizz, flyaway) quebra a
leitura do coque em preto, o passe está forte demais.

## Pipeline

| Etapa | Estado |
|---|---|
| Sculpt (ZBrush) | ✅ |
| Retopo | ✅ |
| Pose | ✅ |
| Retopo pós-pose | ✅ |
| UVs | ✅ |
| Bake | ✅ |
| Grooming (Blender, hair curves + GN, sem addon) | 🔧 em andamento, alvo: madrugada de 25 pra 26/09 |
| Lookdev / materiais / cabelo renderizado | ⏳ fim de semana |
| Luz, câmera, render, turntable | ⏳ fim de semana |
| Apresentação (ArtStation + material pra one-on-one) | ⏳ fim de semana |

## Arquivos desta pasta

- `plano_madrugada_grooming.md`: o plano da noite: ordem de ataque, stack de
  nodes, mapa Houdini → Blender, blocos de tempo e regra de parada.
- `plano_fim_de_semana.md`: sábado e domingo, até a peça fechada.
- `diario.md`: o safeplace. Uma entrada por sessão, sem filtro.

## Ferramentas de apoio já no repositório

Quando um addon próprio deixa de ser "addon de terceiro" fica a seu critério,
mas os dois estão prontos e testados na 5.2, caso a sessão precise:

- `Estudos Extras Curriculares/Blender Hair Geometry Nodes/addons/groom_hide/`:
  esconde guias no Sculpt Curves (H, Shift+H, Alt+H). É o que aparece no painel
  Groom Hide da screenshot.
- `Estudos Extras Curriculares/Blender Hair Geometry Nodes/addons/groom_select/`:
  seleciona guias por atributo.
- `Estudos Extras Curriculares/Blender Hair Geometry Nodes/pesquisa_hair_geonodes.md`:
  a pesquisa de material. O artigo do tenp-kukan (seção 2.2) é o dicionário
  node a node da Essentials, útil se algum node se comportar de forma estranha.
