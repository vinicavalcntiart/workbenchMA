---
titulo: "Here's how DreamWorks lent a whole new brand of stylized look and feel to Puss in Boots: The Last Wish"
autor: "Ian Failes (befores & afters), com citacoes do VFX Supervisor Mark Edwards (DreamWorks)"
url: https://beforesandafters.com/2023/01/11/heres-how-dreamworks-lent-a-whole-new-brand-of-stylized-look-and-feel-to-puss-in-boots-the-last-wish/
data: 2023-01-11
tipo: artigo
versao_blender: nao se aplica (DreamWorks, ferramenta propria "Willow")
coletado_em: 2026-09-28
---

## Nota de coleta

Artigo do befores & afters, fetch direto confirmado (HTTP 200). Ha tambem
uma sessao tecnica oficial no SIGGRAPH 2023 ("Visual Style of Puss In
Boots: The Last Wish", ACM DOI 10.1145/3577023.3585289) que nao consegui
abrir diretamente (paywall/bloqueio, HTTP 403), entao uso o artigo de
imprensa, que cita a equipe diretamente.

## Princípios

1. **Controlar detalhe, nao eliminar ele.** Citacao literal do VFX
   Supervisor Mark Edwards: "it wasn't about losing detail and richness,
   it was about controlling it." O objetivo estilizado nao e "menos
   pelo", e pelo organizado em grupos legiveis.

2. **Guard hairs como linha de acento, nao como pelo realista.** A equipe
   engrossou os guard hairs (pelos de guarda, os fios longos que
   normalmente ficam por cima da subcamada em pelagem realista) e
   adicionou quebra de transparencia neles, e podia "art direct just
   where they were, both in the silhouette and just on his face." Ou
   seja, guard hair virou uma ferramenta de desenho de linha e silhueta,
   controlavel fio a fio, nao um efeito automatico de simulacao.

3. **Cor por clump e sub-clump, tipo pincelada.** Controles de matiz por
   clump e sub-clump de pelo permitiram criar manchas de cor grandes que
   lembram pinceladas de tinta, em vez de variacao de cor por fio
   individual (que leria como ruido/textura, nao como pincelada).

4. **Transparencia mapeada para guias grossas, criando quebras entre
   grupos de pelo.** Isso da "gaps and broken edges" parecidos com o jeito
   que um ilustrador desenha pelo (tufos com espaco entre eles), em vez
   do preenchimento continuo tipico de fur realista.

5. **Groom continuou funcional apesar do estilo.** Mesmo estilizado, o
   sistema de groom preservava a capacidade de reagir a pose (pelo "em
   pe" quando o personagem se assusta). Estilizacao de olhar nao significa
   abrir mao de resposta a animacao.

6. **Linework foi testado e descartado para o pelo.** A equipe testou a
   abordagem de contorno de linha usada em "The Bad Guys" mas decidiu que
   nao combinava com o visual de pelo macio deste filme. Ou seja, nem
   todo principio de um filme estilizado da mesma produtora se aplica ao
   proximo: o "look" e uma escolha de projeto, nao uma formula fixa.

## Como aplicar em Geometry Nodes (traducao minha, nao veio da fonte)

- Principio 2 (guard hair como linha de acento): separar um segundo
  conjunto de guias mais grossas (Set Hair Curve Profile com radius maior
  so nelas, via um segundo grupo/atributo), possivelmente com o alfa do
  shader variando ao longo do fio para simular a quebra de transparencia.
- Principio 3 (cor por clump): usar o indice de clump gerado por Create
  Guide Index Map / Clump Hair Curves como entrada de um Color Ramp no
  shader, para cada clump ganhar uma variacao de matiz proxima mas
  distinta, em vez de ruido por fio.
- Principio 4 (quebra entre tufos): variar a Factor do Clump por regiao
  (por exemplo via textura de vertex group esparsa) para deixar buracos
  visiveis de proposito entre grupos de clump, em vez de clumping
  uniforme cobrindo 100% da superficie.
