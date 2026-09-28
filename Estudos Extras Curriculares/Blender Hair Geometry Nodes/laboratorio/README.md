# Laboratório de grooming estilizado (Blender 5.2)

Tudo aqui foi testado em bpy 5.2.2 e renderizado em Cycles, numa cabeça em
escala real (raio 10 cm). As conclusões estão no cérebro, seção 17:
`../../_referencia/grooming/CEREBRO_GROOMING.md`.

- `receitas_grooming.blend`: biblioteca de node groups prontos.
- `img/`: folhas de contato de cada teste.
- `scripts/`: o laboratório (`lab.py`), um script por teste e as notas brutas.

## Como usar a biblioteca

1. Edit > Preferences > File Paths > Asset Libraries > **+**, aponte para esta
   pasta.
2. No Geometry Nodes do seu Curves, Shift+A > a biblioteca > grupos "GR".
3. Ou File > Append > `receitas_grooming.blend` > NodeTree.

## Os grupos

| Grupo | Faz o quê | Onde vai na cadeia |
|---|---|---|
| GR Guias Procedurais | gera guias penteadas sem esculpir (Curves vazio com Surface) | antes de tudo, opcional |
| GR Densidade Livre | Interpolate sem a trava de 10.000 fios/m² | primeiro |
| GR Mecha Estilizada | mecha em fita, raiz coberta | depois do Interpolate |
| GR Lado da Risca | 0/1 pelo lado da raiz | no Group ID da Mecha Estilizada |
| GR Strays em Arco | 4% dos fios em arco limpo | antes de Curl/Braid |
| GR Cacho por Mecha | cacho com raio e voltas por mecha, em voltas por metro | depois da Mecha |
| GR Onda S | onda plana de desenho | depois da Mecha |
| GR Cor por Mecha | grava `mecha_rand` para o shader | em qualquer ponto depois da Mecha |
| GR Mecha Chunky | fios viram fitas de malha torcidas | último |
| GR Ponta Virada | ponta para fora (flip) ou para dentro, variando por mecha | depois da Mecha |
| GR Trança Grossa | trança de raio constante | depois de Densidade Livre com Distância das guias ~0,02 |
| GR Corte por Região | curto onde o vertex group vale 0, sem clump ali | depois do Interpolate |
| GR Pelo em Tufos | pelo estilizado com subpelo e pelo de guarda opcionais | sozinho, no lugar do Interpolate |
| GR Volume na Raiz | empurra o fio pela normal do scalp, raiz parada | depois da Mecha |
| GR Máscara por Imagem | apaga fios onde a imagem é preta; devolve o cinza para reusar | depois do Interpolate |
| GR Física Estilizada | Hair Dynamics nas guias, segura o penteado | antes do Interpolate, num modificador só das guias |
| GR Rabo de Cavalo | junta tudo num elástico e deixa cair | depois da Densidade Livre, antes da Mecha |
| GR Forma por Malha | as guias colam numa malha simples (a silhueta) | nas guias, antes do Interpolate |
| GR Corte pela Malha | corte reto: apaga o que passa da malha | depois da Mecha/Onda |
| GR Comprimento até a Malha | fio reto da raiz até a malha (Trolls, espetado) | depois da Densidade Livre, antes do Clump |
| GR Hair Cards | fitas planas com UV para jogo (Convert > Mesh e FBX) | depois da Densidade Livre com 8.000-20.000/m² |
| GR Contorno | traço de desenho em volta das mechas de malha | depois da GR Mecha Chunky |
| GR Transição | anima ou mistura dois penteados com a mesma contagem de pontos | depois de separar os ramos A e B |
| GR Pentear por Curva | pelo curto deita no sentido de uma curva desenhada | logo depois de gerar os fios |
| GR Semente do Objeto | Seed e aleatórios diferentes por cópia do objeto | fora da cadeia, nos Seeds |
| GR Flutuar | ondulação animada sem física (água, vento de fundo) | nas guias depois de um Resample, ou nos fios |
| GR Chão | cabelo longo esparrama no piso em vez de atravessar | nas guias; de novo depois do Interpolate com Espalhar desligado |
| GR Crescer | animação: cada mecha cresce pelo caminho final | no fim, antes do Set Hair Curve Profile |
| GR LOD por Câmera | multidão: menos fios longe, fio mais grosso | no fim, depois do Set Hair Curve Profile |
| GR Ver em Cores | número vira azul/vermelho no Viewer | fora da cadeia |

Materiais: **GR Cabelo Cor por Mecha** (lê `mecha_rand` e escurece a raiz) e
**GR Cabelo Toon**, **GR Card Alpha** para os cards e **GR Contorno** para o traço.

## Física

Guias com Snap to Nearest Surface. Modificador 1 só com GR Física
Estilizada. Modificador 2 com a cadeia de groom. Colisão: modificador
Collider na cabeça inteira, a cabeça numa coleção, a coleção na entrada
Colisores. Não ligue Surface Collision no scalp. Vento: entrada Vento
(0,04 brisa, 0,12 vento de cena) e Direção do vento.

## Ordem que funciona

GR Densidade Livre → GR Mecha Estilizada → GR Volume na Raiz → GR Strays em
Arco → GR Ponta Virada → GR Onda S ou GR Cacho por Mecha → GR Cor por Mecha →
Set Hair Curve Profile → Set Material.

Ponta Virada depois do Cacho, com Subdivisão 2, deixou a cadeia 9× mais lenta
(6,8 s contra 0,72 s, CEREBRO 17.54).

Para variações, ligue um único node Integer no Seed de todos os grupos.

Personagem animado: Deform Curves on Surface é o último node de forma (depois
de Mecha, Cacho, Onda, Corte pela Malha), com Add Rest Position ligado no
scalp. Tudo que lê posição vem antes dele (CEREBRO 17.46).
