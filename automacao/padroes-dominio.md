# Padrões de domínio provados

Arquivo criado em 03/09/2026 pelo Joe, na rodada dedicada aos estúdios grandes.

**Para que serve.** A página de contato de casa grande não publica endereço nenhum, e a
decisão do Vini de 03/09 foi que abordagem por LinkedIn a recrutador de estúdio grande não
funciona. Este arquivo resolve o problema por outro caminho: uma vez que se sabe que a Pixar
usa `inicial+sobrenome@pixar.com` e a Disney Animation usa `nome.sobrenome@disneyanimation.com`,
**qualquer nome novo daquela casa vira um endereço de confiança média**, sem precisar achar o
endereço da pessoa. O nome a gente acha em crédito de filme, palestra ou entrevista.

**De onde vêm as provas.** Duas fontes, as duas públicas e verificáveis:

1. **Log de commits de código aberto.** `git log` guarda nome e email reais de quem contribuiu.
   Foram clonados (raso, `--filter=blob:none --no-checkout`) OpenUSD e OpenSubdiv da Pixar,
   OpenMoonRay da DreamWorks, OpenColorIO e OpenShadingLanguage da Sony Imageworks, Ptex,
   SeExpr e BRDF Explorer da Disney, MaterialX, OpenEXR, OpenImageIO, OpenTimelineIO, OpenVDB
   e OpenCue da Academy Software Foundation, VMAF, Photon e Metaflow da Netflix, Luau da Roblox
   e League Director da Riot.
2. **Rodapé de autor de paper e production talk do SIGGRAPH**, nos PDFs abertos que a própria
   Disney Animation hospeda em `cdn.disneyanimation.com` e `media.disneyanimation.com`.

**Regra de honestidade.** Um padrão só entra aqui com **pelo menos dois endereços reais** que
confirmam o mesmo formato. Onde aparece mais de um formato no mesmo domínio, isso está escrito,
porque esconder a exceção transformaria confiança média em chute.

**Ressalva que vale para o arquivo inteiro.** Essas fontes puxam muito mais gente técnica, TD e
engenheiro de gráficos, do que diretor de arte. Um TD sênior não contrata ninguém. Mas ele
trabalha ao lado de quem contrata, e **o padrão de domínio que ele revela serve para a casa
inteira**, inclusive para o diretor de arte que nunca escreveu uma linha de código.

---

## Walt Disney Animation Studios

**`nome.sobrenome@disneyanimation.com`** e **`Nome.Sobrenome@disney.com`**, os dois válidos
para a mesma pessoa.

Prova de que são o mesmo endereço em dois domínios: **Brent Burley** aparece nos commits do
Ptex e do BRDF Explorer com `brent.burley@disney.com` **e** `brent.burley@disneyanimation.com`.
O mesmo com **Jennifer Stratton**, `Jennifer.Stratton@disney.com` no talk do SIGGRAPH 2024 e
`Jennifer.Stratton@disneyanimation.com` no outro talk do mesmo ano. A grafia com maiúscula é só
como o autor digitou; email não diferencia maiúscula de minúscula.

Endereços que servem de prova, todos publicados:

| Endereço | Fonte |
|---|---|
| `Keith.R.Wilson@disneyanimation.com` | rodapé do talk do SIGGRAPH 2014 "Simulating Wind Effects on Cloth and Hair in Disney's Frozen" |
| `Jennifer.Stratton@disneyanimation.com` | rodapé do talk do SIGGRAPH 2024 "Character Stylization in Disney's Wish" |
| `Avneet.Kaur@disneyanimation.com` | mesmo talk |
| `courtney.chun@disneyanimation.com` | rodapé do talk do SIGGRAPH 2023 "Creating the Art-Directed Groom for Legend in Disney's Strange World" |
| `jose.velasquez@disneyanimation.com` | mesmo talk |
| `haixiang.liu@disneyanimation.com` | mesmo talk |
| `alberto.luceno.ros@disneyanimation.com` | rodapé do talk do SIGGRAPH 2025 "The Art of Crowds Animation" |
| `jeff.sullivan@disneyanimation.com` | mesmo talk |
| `karl.li@disneyanimation.com` | rodapé do talk do SIGGRAPH 2025 "A Texture Streaming Pipeline" |
| `nathan.zeichner@disneyanimation.com` | mesmo talk |
| `nathan.devlin@disneyanimation.com` | talk do SIGGRAPH sobre crowds de Strange World |
| `yasser.hamed@disneyanimation.com` | mesmo talk |
| `dlun.wong@disneyanimation.com` | mesmo talk |
| `brent.burley@disneyanimation.com` | log de commits do Ptex, do SeExpr e do BRDF Explorer |
| `daniel.teece@disneyanimation.com` | log de commits do Ptex |
| `mark.mclaughlin@disneyanimation.com` | log de commits do Ptex e do SeExpr |
| `patrick.kelly@disneyanimation.com` | log de commits do SeExpr |
| `christian.eisenacher@disneyanimation.com` | log de commits do Ptex |
| `rasmus.tamstorf@disneyanimation.com` | paper de simulação de pano hospedado pelo estúdio |
| `matt.chiang@disneyanimation.com` | paper de subsurface scattering do SIGGRAPH 2016 |
| `Avneet.Kaur@disney.com`, `David.Hutchins@disney.com`, `Nikki.Mull@disney.com` | rodapé do talk do SIGGRAPH 2024 "Art-Directing Asha's Braids in Disney's Wish" |

**Variações que existem e que não quebram o padrão**, mas que obrigam a checar o nome do meio:
`Keith.R.Wilson` e `gene.s.lee` levam a inicial do meio; `alberto.luceno.ros` leva o sobrenome
duplo inteiro. Existe também uma minoria antiga em `inicial+sobrenome` (`nkagan@`, do mesmo
Noah Kagan que também usa `noah.kagan@`), então quando `nome.sobrenome` voltar, vale tentar a
forma curta antes de desistir.

**Quantos endereços provam:** mais de 20.

## Pixar Animation Studios

**`inicial+sobrenome@pixar.com`**

| Endereço | Pessoa | Fonte |
|---|---|---|
| `dyu@pixar.com` | David G. Yu | log de commits do OpenSubdiv |
| `jfong@pixar.com` | Julian Fong | log de commits do OpenSubdiv |
| `mkraemer@pixar.com` | Manuel Kraemer | log de commits do OpenSubdiv |
| `ssalituro@pixar.com` | Susan Salituro | log de commits do OpenSubdiv |
| `jmooney@pixar.com` | J. Mooney | log de commits do OpenSubdiv |
| `nporcino@pixar.com` | Nick Porcino | log de commits do OpenTimelineIO |
| `gelkoura@pixar.com` | George Elkoura | log de commits do OpenSubdiv |
| `jloy@pixar.com` | John Loy | log de commits do OpenTimelineIO |
| `sfriedma@pixar.com` | S. Friedman | log de commits do OpenShadingLanguage |
| `brandonwang@pixar.com` | Brandon Wang | log de commits do Ptex |

**Aviso importante, e é por isso que a Pixar é o padrão mais fraco desta lista.** O domínio tem
contas antigas em estilo Unix que fogem da regra: `gelder@` (Dirk Van Gelder, só o sobrenome),
`takahito@` e `sunya@` (só o primeiro nome), `steinbach@` e `peachey@` (só o sobrenome),
`joshm@` (nome + inicial do sobrenome) e `mikemahony@` (nome e sobrenome colados). A forma
`inicial+sobrenome` é a maioria clara e é a que vale para nome novo, mas se voltar, as
alternativas naturais são o sobrenome sozinho e o primeiro nome sozinho.

**Quantos endereços provam:** 10 na forma principal.

## DreamWorks Animation

**`nome.sobrenome@dreamworks.com`**

Provado por 20 endereços no log de commits do OpenMoonRay, do OpenUSD, do OpenSubdiv e do
OpenEXR: `barry.fowler@`, `alan.blevins@`, `bill.spitzak@`, `scott.cegielski@`, `ron.woods@`,
`randy.packer@`, `jon.lanz@`, `jeff.mahovsky@`, `toshi.kato@`, `mike.day@`, `dan.mccann@`,
`ashley.lee@`, `matthew.low@`, `paul.ramsey@`, `rob.wilson@`, `ibrahim.sani@`, `karl.rasche@`,
`connie.chang@`, `sean.wallitsch@`, `shane.smith@`.

Este é o padrão mais limpo dos grandes de animação. A única exceção vista foi `jbradley@`.

**Cuidado com o nome curto:** o domínio usa o nome pelo qual a pessoa é conhecida, não
necessariamente o formal. Coexistem `mike.day@` (Mike, não Michael) e `matthew.low@` (Matthew,
não Matt). Para alguém que assina "Matt", tente `matt.` primeiro e `matthew.` em seguida.

**Quantos endereços provam:** 20.

## Sony Pictures Imageworks

**`inicial+sobrenome@imageworks.com`**

Provado por 15 endereços no log de commits do OpenColorIO, do OpenShadingLanguage, do OpenEXR e
do OpenImageIO: `aconty@` (Alejandro Conty), `ckulla@` (Christopher Kulla), `cstein@` (Clifford
Stein), `dhaase@` (Derek Haase), `jreynolds@` (Jay Reynolds), `rzulak@` (Roman Zulak), `jrray@`
(J Robert Ray), `secooper@` (Sean Cooper), `slooper@` (Sean Looper), `plecocq@` (Pascal Lecocq),
`dtavares@` (Diego Tavares), `fperumal@` (Fermi Perumal), `rfigueiredo@` (Ramon Figueiredo),
`rbehrens@` (Rosa Behrens), `zfong@` (Zach Fong).

Exceções antigas, todas de gente que entrou cedo: `lg@` (Larry Gritz), `sam@`, `hall@`,
`jeremys@`, `blair@`, `chambers@`.

**Quantos endereços provam:** 15.

## Netflix

**`inicial+sobrenome@netflix.com`**, com uma segunda forma que também funciona.

Provado por mais de 25 endereços no log de commits do VMAF, do Metaflow, do Photon e do
OpenTimelineIO: `ereinecke@`, `fschleich@`, `aspyker@`, `aschuler@`, `akostenko@`, `cconcolato@`,
`hsutherland@`, `ikatsavounidis@`, `jge@`, `jsole@`, `kswanson@`, `lkrasula@`, `mafonso@`,
`mmanohara@`, `nahmad@`, `npow@`, `phieromnimon@`, `qhuang@`, `rchirravuri@`, `rspieldenner@`,
`rperezalcolea@`, `rpuri@`, `rcledat@`, `sbarati@`, `ssrikanth@`, `schakrovorthy@`, `svenkatrav@`,
`tcase@`, `zli@`, `zsimic@`.

**A segunda forma é `nome+inicial do sobrenome`**, e a prova de que as duas chegam na mesma
pessoa é **Nil Fons Miret**, que commita ora como `nilf@netflix.com` ora como
`nfonsmiret@netflix.com`. Na mesma linha existem `christosb@` (Christos Bampis), `chaoyingw@`
(Chaoying Wang), `arjunb@` (Arjun Barrett), `tingtingc@`, `santiagoc@` e `yinglaol@`. Ou seja,
na Netflix as duas formas convivem, e se `inicial+sobrenome` voltar, `nome+inicial` é a segunda
tentativa legítima.

**Quantos endereços provam:** mais de 30.

## Lucasfilm e Industrial Light & Magic

**`inicial+sobrenome@ilm.com`** e **`inicial+sobrenome@lucasfilm.com`**

Provado por 17 endereços no log de commits do OpenEXR, do MaterialX e do OpenUSD: `akunz@`,
`arasiah@`, `brobson@`, `dhess@`, `ehanway@`, `ewimmer@`, `mshooter@`, `pstanczyk@`, `sboorer@`,
`vlazar@`, `yshu@`, `abucior@`, `ilawson@`, `rherrera@`, `sgilligan@` no `ilm.com`, e `jstone@`
e `mkuo@` no `lucasfilm.com`. Exceções antigas: `cary@`, `nick@`, `pauls@`, `jihun@`, `juliencb@`.

**Quantos endereços provam:** 17.

## LAIKA

**`inicial+sobrenome@laika.com`**

`mprater@laika.com` (Mitch Prater) e `pfranz@laika.com`, os dois no log de commits do OpenEXR e
do OpenImageIO. São só dois endereços: é o mínimo aceitável, e o padrão fica marcado como frágil.

**Quantos endereços provam:** 2.

## Blizzard Entertainment

**`inicial+sobrenome@blizzard.com`**

`jburnett@` (John Burnett), `sdobbs@` (Stuart Dobbs) e `lpanian@` (Lucas Panian), os três no log
de commits do OpenUSD e do OpenEXR.

**Quantos endereços provam:** 3.

## Roblox

**`inicial+sobrenome@roblox.com`**, com uma segunda forma em `nome+sobrenome` colados.

Forma principal, no log de commits do Luau: `amccord@` (Alexander McCord), `ayoungblood@`,
`afriesen@` (Andy Friesen), `agoel@`, `hgoldstein@`, `irezvov@`, `jyoo@`, `lbrown@`, `malam@`,
`rblanckaert@`, `skanosue@`, `tbennett@`, `tschollenberger@`, `vegorov@`, `vvijay@`.

Segunda forma, no mesmo log: `aaronweiss@`, `arielweiss@`, `annietang@`. Se a primeira voltar,
tente o nome e sobrenome colados.

**Quantos endereços provam:** 15 na forma principal.

## Riot Games

**`inicial+sobrenome@riotgames.com`**

`agiacca@` (Andrew Giacca), `bnagappa@` (Bharath S Nagappa), `cbutler@` (Christopher Butler) e
`whagen@`, os quatro no log de commits do League Director, o repositório oficial da Riot.

**Quantos endereços provam:** 4.

---

## Lucasfilm (domínio próprio, diferente do da ILM) — provado em 05/09

**`inicial+sobrenome@lucasfilm.com`**

| Endereço | Pessoa | Fonte |
|---|---|---|
| `jstone@lucasfilm.com` | Jonathan Stone | log de commits do MaterialX |
| `mkuo@lucasfilm.com` | Malia Kuo | log de commits do MaterialX |

**Quantos endereços provam:** 2.

**Por que isso importa:** a campanha só conhecia `ilm.com`. Este é um segundo domínio
vivo da mesma casa, com o mesmo formato, e serve de segunda via quando um endereço em
`ilm.com` voltar.

**Endereços novos de `ilm.com` achados na mesma varredura, que reforçam o padrão de lá:**
`rherrera@`, `sgilligan@` (MaterialX), `abucior@` (Alan Bucior), `cary@` (Cary Phillips),
`ilawson@` (Ian Lawson) e `juliencb@` (Julien Cohen Bengio), estes quatro no log do
OpenUSD. Atenção: `cary@` e `juliencb@` são exceções ao formato, então em nome comprido
ou composto vale desconfiar.

---

## Sony (`sony.com`) — provado em 05/09, MAS NÃO É A SONY PICTURES ANIMATION

**`nome.sobrenome@sony.com`**

| Endereço | Pessoa | Fonte |
|---|---|---|
| `Jeremiah.Zanin@sony.com` | Jeremiah Zanin | log de commits do OpenUSD |
| `hamed.sabri@sony.com` | Hamed Sabri | log de commits do OpenUSD |

**Quantos endereços provam:** 2.

**AVISO QUE VALE MAIS QUE O PADRÃO.** Foi conferido: Jeremiah Zanin é do **Santa Monica
Studio**, que é PlayStation, ou seja, Sony Interactive Entertainment. Este domínio é da
Sony corporativa e do braço de jogos, **não** da Sony Pictures Animation. Portanto NÃO se
usa `sony.com` para montar endereço de gente da Sony Pictures Animation: seria chute entre
divisões diferentes, e Wendell Dalit continua **sem via**. O que este padrão abre de
verdade é o Santa Monica Studio, casa de jogos grande, em escopo e com zero cartas.

---

## Weta FX — três endereços reais, e DUAS formas

**`nome+inicial@wetafx.co.nz`** na maioria, com uma segunda forma em `inicial+sobrenome`.

`antond@` (Anton Dukhovnikov) e `peterh@` (Peter Hillman) são nome mais inicial;
`sfinnie@` é inicial mais sobrenome, e em 05/09 apareceu `navramoussis@` (Nicholas
Avramoussis), que confirma essa segunda forma. Todos no log de commits do MaterialX, do
OpenImageIO e do OpenVDB. Curiosidade útil: o mesmo Nick Avramoussis aparece como `nna@dneg.com`
e como `navramoussis@wetafx.co.nz`, ou seja, mudou de casa, e isso lembra que endereço de log
de commit envelhece.

**Quantos endereços provam:** 3, mas com duas formas, então a confiança de um endereço
novo aqui é **média para baixa** e vale tentar as duas.

---

## Exceções novas no padrão da Sony Pictures Imageworks, achadas em 05/09

O padrão `inicial+sobrenome@imageworks.com` continua valendo e ganhou mais provas
(`chambers@`, `jrray@`, `slooper@`, `aconty@`, `ckulla@`, `cstein@`, `plecocq@`), mas
apareceram **quatro exceções** que precisam ficar registradas: `jeremys@` (Jeremy Selan,
nome mais inicial), `blair@` (Blair Zajac, só o primeiro nome), `sam@` (Sam Richards, só o
primeiro nome) e `hall@` (Brian Hall, só o sobrenome). Ou seja, contas antigas fogem da
regra, igual à Pixar.

## Ubisoft — provado em 05/09, e abre uma casa grande inteira

**`nome.sobrenome@ubisoft.com`**

| Endereço | Pessoa | Fonte |
|---|---|---|
| `anton.brand@ubisoft.com` | Anton Brand | log de commits do OpenVDB / OSL |
| `brian.mckinnon@ubisoft.com` | Brian McKinnon | idem |
| `farchad.bidgolirad@ubisoft.com` | Farchad Bidgolirad | idem |
| `jerome.hubert@ubisoft.com` | Jerome Hubert | idem |

**Quantos endereços provam:** 4, todos na mesma forma, sem exceção vista.

**Por que importa:** a Ubisoft é casa grande dentro do escopo (Massive na Suécia, Montpellier
na França, Montréal no Canadá), a campanha tem **três candidaturas de portal travadas** lá
por causa do DataDome do SmartRecruiters, e **nenhuma carta pessoal**. Qualquer nome de arte
da Ubisoft que apareça daqui em diante nasce com endereço de confiança média.

---

## Animal Logic — nove endereços, duas formas, e uma ressalva que muda tudo

**`nome+inicial@al.com.au`** na maioria, com uma segunda forma em `Nome.Sobrenome@al.com.au`.

Primeira forma: `aloysb@`, `danielh@` (Daniel Heckenberg), `eoinm@`, `ghislainv@` (Ghislain
Veilleux), `jonc@` (JP Collins), `nickw@` (Nick Wu). Segunda forma: `Steve.Agland@`,
`Zhicheng.Ye@`, `fabrice.macagno@`. Todos no log de commits do OpenVDB e do OpenTimelineIO.

**Quantos endereços provam:** 9.

**RESSALVA QUE PRECISA SER LIDA ANTES DE USAR.** Em 05/09 a própria página de carreiras da
Animal Logic diz, com essas palavras, *"Our jobs have now moved netflixanimation.com"*. Ou
seja, a casa foi absorvida pela Netflix Animation e essas caixas em `al.com.au` podem ser
legado. Antes de escrever para alguém da Animal Logic, considere que a pessoa provavelmente
está hoje em `netflix.com`, cujo padrão a campanha já tem provado por mais de trinta
endereços nas duas formas.

## Image Engine — provado em 06/09, e e a casa de VFX de Vancouver

**`nome + inicial do sobrenome@image-engine.com`**, com desambiguação por segunda letra quando
há colisão de primeiro nome.

Cerca de **trinta endereços reais** no log de commits do **Gaffer** e do **Cortex**, os dois
projetos de código aberto mantidos pela própria Image Engine: `andrewk@` (Andrew Kaufman),
`bent@` (Ben Toogood), `brendanh@` (Brendan Holt), `cedricl@` (Cedric Launay), `danield@`
(Daniel Dresser), `davidm@` (David Minor), `ivani@` (Ivan Imanishi), `lukeg@` (Luke Goddard),
`mattig@` (Matti Gruener), `pauleliep@` (Paul-Elie Pipelin), `petruc@` (Petru Ciobanu),
`richardm@` (Richard Monette), `stefanf@` (Stefan Feess), `beatriced@` (Bea Domenge),
`aitorp@`, `bradleyh@`, `carlosg@`, `ehsans@`, `koichit@`, `lorenzop@`, `paulon@`, `piotrb@`,
`tomc@`, `valerieb@`, `yannics@`.

**A desambiguação é real e importa:** quando dois primeiros nomes colidem, o endereço estica
para duas letras do sobrenome. `michaeldu@` (Michael DuBelko), `michaelne@` (Michael Neynens)
e `michaelk@` (Michael Kessler) convivem; o mesmo vale para `donbo@` (Don Boogert), `timle@`
(Tim Lehr) e `christopherle@`.

**Duas exceções vistas.** Uma é `lberesna@` (Linas Beresna), na forma inicial mais sobrenome.
A outra é gente antiga ou muito sênior com **só o primeiro nome**: `john@` (John Haddon),
`lucio@` (Lucio Moser), `mark@` (Mark Williams), `blair@` (Blair Tennessee).

**Quantos endereços provam:** cerca de 30.

## Cinesite — provado em 06/09, e o grupo inclui a Image Engine

**`inicial + sobrenome@cinesite.com`**, com uma segunda forma em `nome + inicial`.

Forma principal, nos mesmos logs do Gaffer e do Cortex: `jhaddon@` (John Haddon), `gkeech@`
(Gregory Richard Keech), `proberts@` (Paul-George Roberts). Segunda forma: `ericm@` (Eric
Mehl), `tomc@` (Tom Cowland). E um caso de primeiro nome puro, `alexander@` (Alexander
Savenko).

**Quantos endereços provam:** 6.

**Contexto que vale saber antes de usar:** a Cinesite, a Image Engine e a Trixter são o mesmo
grupo, o que ficou explícito na página de equipe deles, onde o gerente geral da Image Engine
aparece também como Chief Operating Officer de VFX do grupo Cinesite, e onde o Group Head of
CG cobre as três marcas. Cada casa mantém o próprio domínio, então **não se troca um pelo
outro**: gente da Image Engine é `image-engine.com`, gente da Cinesite é `cinesite.com`.

## Luma Pictures — provado em 06/09, e a prova final veio do site deles

**`nome + inicial do sobrenome@lumapictures.com`**.

Três endereços reais, e o terceiro é o que fecha a conta porque está publicado pela própria
Luma: `palm@` (Pal Mezei) e `paulm@` (Paul Molodowitch) saíram do log de commits do
OpenColorIO e do OpenImageIO, e `ericr@` (Eric Robertson, New Business) está na página
About do site deles, ao lado de `pr@` e de `recruiting@lumapictures.com`.

**Por que importa:** a Luma é estúdio de VFX independente desde 2002, com cerca de 300
pessoas em Santa Monica, **Melbourne** e **Vancouver**, ou seja, cobre a Oceania e o cluster
mais denso da campanha de uma vez, e tem mais de 100 longas no currículo.

**Quantos endereços provam:** 3, sendo um publicado pelo próprio estúdio.

## Não provados, registrados para não se perder

- **Epic Games.** Só um endereço real encontrado, `matt.johnson@epicgames.com`, no log de
  commits do OpenEXR. Um endereço não prova padrão. A forma `nome.sobrenome` é a hipótese, e
  fica marcada como **não provada** até aparecer o segundo. **Varrido de novo em 05/09** nos
  logs completos de MaterialX, OpenColorIO, OpenImageIO e OpenUSD: nenhum segundo endereço
  apareceu. A Epic segue fechada.
- **Naughty Dog, e a tentação que veio junto com o padrão da Sony.** Em 05/09, ao provar
  `nome.sobrenome@sony.com`, apareceu a ideia de montar o endereço do Raf Grassetti, que hoje
  está na Naughty Dog e é dos alvos de arte mais próximos do perfil do Vini. **Recusado.** Um
  único funcionário de estúdio first party na base `sony.com` (Jeremiah Zanin, do Santa Monica
  Studio) não prova que a Naughty Dog use esse domínio, e a Naughty Dog tem domínio próprio,
  `naughtydog.com`, sem nenhum endereço real conhecido. É o mesmo tipo de chute entre divisões
  que foi recusado para Wendell Dalit no mesmo dia, e aceitar num caso e recusar no outro seria
  incoerência. Grassetti segue **sem via**.
- **Atomic Cartoons.** Um endereço real, `n.yue@atomiccartoons.com` (Nicholas Yue), no log de
  commits dos repositórios da Academy Software Foundation, na forma **inicial do nome, ponto,
  sobrenome**. Um só não prova. Fica marcado até aparecer o segundo, e por isso o Joey Wilson,
  Head of CG Assets deles, entrou no `pessoas.csv` com confiança **baixa** e não média.
- **Digital Domain.** Um endereço real, `fredriks@d2.com` (Fredrik Salomonsson), na forma
  nome mais inicial, e num domínio legado (`d2.com`) e não no `digitaldomain.com` público.
  Não serve para construir. Isso mantém a **Kasita Wonowidjojo**, Senior Texture Painter de
  lá, guardada sem via.
- **Method Studios** (`nome.sobrenome`, dois endereços: `blair.tennessy@` e `robert.minsk@`) e
  **Nvizible** (`nome.sobrenome`, dois endereços: `ben.deluca@` e `hugh.macdonald@`) têm forma
  consistente, mas as duas casas encolheram ou fecharam a operação de VFX, então o padrão fica
  registrado sem valor prático.
- **Mikros Image**: `cnt@` e `mfe@`, iniciais puras, não construível.
- **Framestore.** Um endereço real, `kevin.wheatley@framestore.com` (OpenUSD), na forma
  `nome.sobrenome`. Um só não prova. Fica marcado até aparecer o segundo.
- **DNEG, com a descrição corrigida em 05/09.** Agora são OITO endereços reais: `axs@`
  (Alex Schwank), `dan@` (Dan Bailey), `hb@` (Harry Biddle), `mels@`, `mkj@` (Mark Boorer),
  `mw@` (Matt Warner), `nna@` (Nick Avramoussis) e `rhj@` (Richard Jones). A descrição
  anterior, de que eram apelidos que não derivam do nome, estava **parcialmente errada**: a
  maioria é INICIAL DO NOME mais INICIAIS DO SOBRENOME (`hb`, `mw`, `nna`, `rhj`, `axs`).
  Mesmo assim **não é construível com segurança**, porque `dan@` é primeiro nome puro e
  `mkj@` não bate com Mark Boorer, e porque duas ou três letras colidem entre pessoas. Serve
  como reconhecimento, não como construção.
- **Sony Pictures Animation** é empresa distinta da Sony Pictures Imageworks e **não** usa
  `imageworks.com`. Nenhum endereço real dela foi encontrado. Não reutilize o padrão da
  Imageworks para a Animation.
- **Naughty Dog, Insomniac, Rocksteady, Bungie, Skydance, Illumination, Nickelodeon, Paramount
  Animation, Warner Bros. e Cartoon Network, Titmouse, Reel FX**: nenhuma contribuição em código
  aberto com email corporativo e nenhum PDF de talk com rodapé de autor. Zero endereços, zero
  padrão. Nada aqui é chute.
- **DreamWorks `research.dreamworks.com` está fora do ar** (página de manutenção do WordPress em
  03/09/2026), então a fonte de PDF de talk da DreamWorks não pôde ser usada. O padrão dela veio
  todo do log de commits, o que não fez falta porque o log deu 20 endereços.
- **`dl.acm.org` bloqueia o acesso** desta máquina (403 por curl, e o proxy de saída barra o
  domínio). A saída foi ir direto nos PDFs abertos que os estúdios hospedam, o que funcionou
  para a Disney Animation e não existe para a Pixar, que não publica PDF aberto no site próprio.

## Zoic Studios

**`inicial+sobrenome@zoicstudios.com`**

Achado em 05/09 e é o padrão mais barato de provar do arquivo inteiro: os quatro endereços
saem da **própria página de contato do estúdio**, `https://zoicstudios.com/contact`, cada um
com nome e cargo ao lado.

| Endereço | Pessoa | Cargo |
|---|---|---|
| `jweitzell@zoicstudios.com` | Julie Weitzell | Executive Producer, Episodic & Film |
| `smelchiorre@zoicstudios.com` | Steve Melchiorre | Senior Executive Producer |
| `rpassionino@zoicstudios.com` | Rocco Passionino | Senior Executive Producer |
| `nfina@zoicstudios.com` | Nicole Fina | Senior Executive Producer, Advertising |

A mesma página publica `zoic-ep@zoicstudios.com` como caixa geral de produtor executivo, em
Los Angeles, Nova York e Vancouver, e o telefone de cada escritório.

**Quantos endereços provam:** 4, todos publicados.

**Por que isso vale mais do que parece.** A Zoic é casa grande de VFX com escritório em
Vancouver, o cluster mais forte desta campanha, e tem vaga de 3D Artist aberta. Com o padrão
provado, qualquer nome de ARTE da casa que apareça em crédito de série ou entrevista vira
endereço de confiança média na hora, sem depender de o estúdio publicar o endereço dele.

## AVISO QUE PASSA POR CIMA DE TODOS OS PADRÕES ACIMA (medido em 06/09)

Em 06/09 o Vini disparou 24 cartas de uma vez, e isso deu a primeira **medição real** do
valor destes padrões. Separando os envios pela origem do endereço:

| Origem do endereço | Enviados | Entregues | Bounces |
|---|---|---|---|
| **Publicado** no site do estúdio ou da pessoa | 17 | 16 | 1 |
| **Montado** por padrão de domínio de log de commit | 8 | 3 | **5** |

**Padrão de domínio falha em mais de 60% das vezes.** Quicaram `jevgeni.laur@ubisoft.com`,
`bsick@netflix.com`, `hvoss@cinesite.com`, `kbourykina@riotgames.com` e `lli@blizzard.com`.
Sobreviveram só `ssharplin@wetafx.co.nz`, `barryp@image-engine.com` e
`j.wilson@atomiccartoons.com`, e este último estava marcado como confiança **baixa**, o que
mostra que a escala de confiança deste arquivo **não estava prevendo nada**.

**Por que falha, e a explicação é simples e desconfortável:** o log de commit prova que o
**formato** existe, não que **aquela pessoa** continua na casa nem que a caixa continua
ativa. Um endereço de um commit de 2019 é um endereço morto com o formato certo.

**O caso que mais dói:** `recruiting@lumapictures.com` estava **publicado na página About do
próprio estúdio**, ou seja, confiança alta pelo critério do brief, e quicou com 550 5.1.1.
Endereço publicado também envelhece.

**Como usar estes padrões daqui em diante:**

1. Endereço **publicado** continua sendo a primeira escolha, e agora vale conferir a data da
   página quando ela mostrar.
2. Endereço **montado por padrão** entra no máximo como **baixa**, nunca média, e vale como
   tentativa barata, não como via confiável.
3. **Nunca gastar a única carta de uma casa grande num endereço montado.** Se a casa tem uma
   via de formulário ou de recrutamento publicada, ela vem primeiro.

## Dois padroes provados em 06/09 pelo log de commits da Academy Software Foundation

| Casa | Padrao | Endereco que serviu de prova |
| --- | --- | --- |
| Framestore | `nome.sobrenome@framestore.com` | `kevin.wheatley@framestore.com` (Kevin Wheatley), log do OpenColorIO |
| Method Studios | `nome.sobrenome@methodstudios.com` | `blair.tennessy@methodstudios.com` e `robert.minsk@methodstudios.com`, dois enderecos reais, o que tira a Method da lista de padrao so inferido e coloca em padrao provado |

A mesma mineracao reconfirmou o padrao da ILM em treze enderecos distintos (`akunz@`, `brobson@`, `dhess@`, `ehanway@`, `ewimmer@`, `mshooter@`, `pauls@`, `pstanczyk@`, `sboorer@`, `tstraubinger@`, `vlazar@`, `yshu@`), com a excecao ja conhecida de gente de casa antiga que usa so o primeiro nome (`cary@`, `nick@`, `jihun@`), e o da Weta FX em quatro.

LEMBRETE QUE PASSA POR CIMA DISTO: padrao provado continua sendo confianca MEDIA e nada mais. A medicao de 06/09 mostrou que endereco montado por padrao quica em mais de 60 por cento das vezes, porque o padrao prova o FORMATO e nao que a pessoa continua na casa.

## Dois padroes provados em 06/09 pela PAGINA DE CONTATO da MPC, e nao por log de commit

A pagina `mpcvfx.com/contact` publica quatro enderecos de pessoa, com nome e cargo ao lado de cada um.
Isso prova dois formatos de uma vez, porque a MPC e a The Mill hoje sao a mesma marca sob a TransPerfect
e a mesma pagina usa os dois dominios.

| Casa | Padrao | Prova, toda publicada na propria pagina de contato |
|---|---|---|
| MPC | `nome.sobrenome@mpcvfx.com` | `helene.vanovre@mpcvfx.com` (Executive Producer), `anai.cabanes@mpcvfx.com` (Post-production sales manager), `laurence.hoeters@mpcvfx.com` (VFX Producer, Liege) |
| The Mill | `nome.sobrenome@themill.com` | `beatrice.bauwens@themill.com` (Director of MPC Paris and Liege, Head of Film & Series) |

**Por que estes dois valem mais que os anteriores:** os padroes deste arquivo saiam quase todos de log de
commit, e o aviso acima mediu que endereco montado assim quica em mais de 60% das vezes, porque o commit
prova o formato e nao prova que a caixa continua viva. Aqui a prova e uma pagina de contato que o estudio
mantem hoje, com o cargo escrito ao lado. Continua sendo padrao, e continua entrando como **baixa** quando
o endereco for montado; o que melhora e a chance, nao a regra.

## Rodeo FX — provado em 06/09 pelo codigo aberto da propria casa, e e casa grande NOVA

**`inicial + sobrenome@rodeofx.com`**

| Endereço | Pessoa | Fonte |
|---|---|---|
| `cfleche@rodeofx.com` | Charles Flèche | log de commits do OpenWalter, repositório de código aberto da própria Rodeo FX |
| `glaforge@rodeofx.com` | Guillaume Laforge | idem |
| `xcui@rodeofx.com` | Xue Cui | idem |

**Quantos endereços provam:** 3, mais a caixa interna `dev@rodeofx.com`.

**Exceção vista:** `lucille@rodeofx.com` (Lucille Caillaud), só o primeiro nome. Então, quando a
forma principal voltar, o primeiro nome sozinho é a segunda tentativa.

**Por que importa:** a Rodeo FX é casa grande de VFX com sede em Montréal e escritórios em
Toronto, Québec, Paris e Los Angeles, dona da Mikros Animation, e a campanha só tinha tocado
nela por banco de talentos (confirmação de 01/09 pelo `notification@rodeofx.com`), sem nenhuma
carta pessoal. A página de liderança deles publica quinze nomes com cargo, entre eles **Deak
Ferrand, Head of Art Department**, e **Yvon Jardel, Creative Director de Animation Development**.

**Detalhe de método que vale mais que o padrão:** essa página tinha sido registrada como **404**
na rodada anterior. Ela não é 404, ela **exige JavaScript**: `curl` recebe a casca do Vue e nada
mais. Abrindo com o navegador de verdade (`hb_run.sh`) a lista inteira aparece. Antes de dar uma
página de equipe como inexistente, abrir com navegador.

## Wētā Workshop — provado em 08/09, domínio PRÓPRIO e diferente da Wētā FX

**`nome.sobrenome@wetaworkshop.co.nz`**

Um endereço real, publicado pelo próprio estúdio na página de contato (`wetaworkshop.com/contact`,
seção Products): `lisa.birchall@wetaworkshop.co.nz`. É domínio `.co.nz` diferente do `wetafx.co.nz`
já provado (nome+inicial/inicial+sobrenome), então **não confundir os dois padrões da mesma
ilha**: FX e Workshop são empresas irmãs com domínio e formato próprios.

**Quantos endereços provam:** 1, então padrão marcado como frágil (precisa de um segundo para
deixar de ser "não provado"). Serviu para montar `rebekah.tisch@wetaworkshop.co.nz` (Supervising
Art Director, Wētā Workshop Design Studio, publicada na própria página de Design do estúdio),
mas **a carta NÃO foi escrita**: checagem no Gmail antes de escrever achou que a Wētā Workshop
já respondeu à campanha em 07/09 (recruitment@wetaworkshop.co.nz avisando que o Game Studio deles
fechou), e thread de quem já respondeu é do Comunicador, não do Joe. Padrão fica registrado para
quando (e se) a casa voltar a ser alvo de carta fria por outra via.

---

# SETE PADRÕES PROVADOS DE UMA VEZ, colhidos das respostas humanas de 09/09

Esta seção não veio de garimpo em página de equipe. Veio da caixa de entrada: sete pessoas
escreveram à mão para o Vini em 09/09, e **cada uma dessas mensagens é um endereço REAL,
funcionando, com nome e cargo conhecidos**. Isso é prova de padrão da melhor qualidade que
existe, e é de graça: o endereço não foi montado nem inferido, ele **entregou uma mensagem**.

Por que isso vale registro: a régua de 08/09 mediu que endereço MONTADO por padrão quica em mais
de 60% das vezes, porque o padrão prova o formato e não a caixa. Aqui o formato **e** a caixa
estão provados no mesmo ato.

| Estúdio | Pessoa | Cargo/contexto | Formato provado |
|---|---|---|---|
| **Eremite Games** (Polônia) | Lukasz Korzanowski | respondeu pela caixa institucional | `contact@eremitegames.com` é lida por pessoa com nome, não é robô |
| **Game Boost** (Suécia) | Jenny Österlund | fundadora | `nome.sobrenome@` no Teamtailor da casa |
| **Embark Studios** (Suécia) | Terri Kim-Bell | recrutadora | `nome-nome-sobrenome@` no Teamtailor da casa |
| **Warhorse Studios** (Chéquia) | Markéta Uhlíková | RH | responde pela caixa de candidato do Breezy, não por endereço próprio |
| **viennaFX** (Áustria) | Felix S. | sócio | `inicial.inicial@vfx.at`, endereço curto de casa pequena |
| **Airship Interactive** (Inglaterra) | Declan Blayney | recrutamento | `nome.sobrenome@` no Teamtailor da casa |
| **beffio** (Polônia) | Tom Lassota | recrutamento | `nome.sobrenome@` no Teamtailor da casa |

**A LIÇÃO DE MÉTODO, e ela muda a ordem de trabalho do Joe:** quatro dos sete escrevem por
`nome.sobrenome@<subdominio>.teamtailor-mail.com`, que é endereço da PLATAFORMA e não do estúdio,
então **não serve para carta fria** e não deve ser registrado como padrão do domínio da casa. Os
dois que valem de verdade são a viennaFX (`f.s@vfx.at`, casa pequena com formato de inicial) e a
confirmação de que a caixa institucional da Eremite é lida por um humano com nome.

**O que fazer com isso:** quando uma casa responde pelo Teamtailor, o nome da pessoa é ouro e o
endereço não é. Guarde o NOME, e procure o endereço do domínio próprio do estúdio por outra via.

## Rodada do Joe de 18h35 em 09/09: ZERO pessoas novas, e o motivo medido

Dez estúdios já contatados em caixa genérica, sem resposta e sem bounce, tiveram site aberto nas
rotas `/`, `/contact`, `/about`, `/team`, `/studio`, `/people` e `/careers`, procurando endereço
PESSOAL publicado: Jam Filled, Savian, Copernicus, Industrial Brothers, Steamroller, Baobab,
Flight School, Cyborn, Blow Studio e A. Film. **Resultado: um único endereço não genérico em
dez casas**, e ele é `games@baobabstudios.com`, que é departamental e não pessoa.

Segunda tentativa, extraindo NOME e CARGO das páginas de equipe (Art Director, Head of Art,
CG Supervisor, fundador): **zero em seis casas**. As páginas que respondem 200 montam a equipe por
JavaScript, exatamente como a armadilha já registrada na Rodeo FX. **Próxima rodada que for atrás
de página de equipe abre com navegador desde o começo, não com curl.**

Nenhum endereço foi inventado para bater a meta de 4 a 8 pessoas.

## Magnopus — provado em 10/09 pelo código aberto da própria casa, e é casa NOVA

**`nome.sobrenome@magnopus.com`**

Catorze endereços reais no log de commits do **Connected Spaces Platform**
(`github.com/magnopus-opensource/connected-spaces-platform`), repositório de código aberto
mantido pela própria Magnopus:

`adam.thorn@`, `adrian.meredith@`, `caio.andrade@`, `david.swift@`, `Elliot.Morris@`,
`garrett.hickey@`, `christopher.atkinson@`, `matthew.voisey@`, `ray.saltrelli@`,
`richard.searle@`, `sam.birley@`, `sandy.lepape@`, `thomas.yehya@` e `aidan.gustard@magnopus.com`.

**Quantos endereços provam:** 14, todos na mesma forma, sem nenhuma exceção vista. A maiúscula
de `Elliot.Morris@` é só como o autor digitou.

**Por que importa:** a Magnopus tem escritório em **Los Angeles** e em **St Albans**, os dois em
escopo, faz virtual art department para cinema e tempo real (o VAD de Fallout é trabalho deles),
e a campanha nunca tinha tocado a casa por pessoa. A candidatura de personagem pelo banco de
talentos do Pinpoint deles entrou em 10/09, com recibo, o que significa que o portfólio já está
no sistema quando a carta de pessoa chegar.

**Continua valendo a régua de 06/09 e de 07/09:** endereço montado por este padrão entra como
confiança **BAIXA**, porque o commit prova o FORMATO e não que a caixa está viva. O primeiro uso
foi `ian.palmer@magnopus.com` (Ian Palmer, Director of Art do estúdio do Reino Unido, cargo dito
por ele mesmo no post *Meet the Magnopians* do estúdio), e ele só foi usado porque a via de
recrutamento publicada tinha sido usada primeiro, no mesmo dia.

## Frost FX — a armadilha de domínio pela TERCEIRA vez (10/09)

O site é **`frostfx.com`** e todo endereço de pessoa é **`@frostfx.ee`**, com o nome próprio
sozinho: `heiki@`, `andres@`, `marko@`, `martin@`, `anton@`, `kalev@`, `will@frostfx.ee`, todos
publicados com nome e cargo na seção Team da home. É o mesmo caso da **Stunlock**
(`stunlock.com` com email `@stunlockstudios.com`, 07/09) e da **TELEVISOR** (`televisor.pl` com
email `@televisor.studio`, 10/09). **Regra reforçada: antes de montar qualquer endereço, procure
um endereço LITERAL na página, porque o domínio do site mente com frequência que já não é rara.**

## UBISOFT — padrão provado por três endereços literais (12/09, pelo Joe)

O talk aberto **"A Ragdoll-less Approach to Physical Animations of Characters in Vehicles"**
(SIGGRAPH 2019 Talks, PDF sem paywall em
https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Shin_A-Ragdoll-less-Approach.pdf)
traz no rodapé, com afiliação **Ubisoft Reflections**:

```
hyojong.shin@ubisoft.com   (Hyojong Shin)
mark.leadbeater@ubisoft.com (Mark Leadbeater)
ben.merrick@ubisoft.com     (Ben Merrick)
```

**O que isso prova:** o formato da casa é **`nome.sobrenome@ubisoft.com`**, o mesmo para todos os
estúdios do grupo, e não um domínio por estúdio. **O que isso NÃO prova:** que a caixa de outra
pessoa esteja viva — endereço montado sobre este padrão continua sendo confiança **BAIXA**, pela
régua de 06/09 (dos 8 montados daquele lote, 5 quicaram).

## O rodapé de paper tem DATA DE VALIDADE (medido em 12/09)

Varri os três anos de Talks abertos do `history.siggraph.org` (2019, 2020 e 2021; 224 talks, PDF
baixado e primeira página extraída). **Só esses anos trazem email no rodapé.** As páginas de
**2022 e 2023 do arquivo não hospedam PDF nenhum** (0 de 54 e 0 de 70) — o arquivo só linka o DOI
da ACM, que está atrás do Cloudflare e devolve **403 até com navegador**. Ou seja: o caminho do
rodapé de paper serve para achar gente cujo endereço foi publicado **até 2021**, e por isso vem
sempre com ressalva de vigência. Quando o PDF é hospedado pelo **próprio estúdio** (o caso da
Animal Logic), o ano pode ser mais recente.

## QUATRO PADRÕES PROVADOS POR ENDEREÇO LITERAL EM 12/09 ÀS 22h (pelo Joe)

Todos vieram de **endereço visto escrito**, nenhum foi deduzido. Ver a ressalva do rodapé de paper
acima: os três primeiros saíram de PDFs de Talks de 2019 a 2021, então provam o **formato** e não a
**vigência da caixa**.

### Frontier Developments — `inicial+sobrenome@frontier.co.uk` (fonte de HOJE, não de paper)

| Endereço | Pessoa e cargo | Fonte |
|---|---|---|
| `ebaldino@frontier.co.uk` | Ellie Baldino, **Talent Acquisition Advisor** | payload do próprio `careers.frontier.co.uk` |
| `yharniman@frontier.co.uk` | Yaz Harniman, **Talent Acquisition Partner** | idem |
| `lmowatt@frontier.co.uk` | Lee Mowatt (cargo nulo no payload) | idem |

**A veia, e ela é nova:** o site de carreiras da casa é front-end próprio em **Nuxt** e renderiza no
servidor o **payload do Lever**, que inclui o objeto do **usuário dono de cada requisição** com nome,
cargo e email corporativo. Resolvendo os índices do `__NUXT_DATA__` dá para dizer **quem é dono da
requisição de personagem**. É a irmã do `recruiter-email` do Teamtailor (veia de 07/09).
**Rendimento honesto: vazou em 1 de ~110 páginas de carreira testadas nesta rodada.**

### Electronic Arts — `inicial+sobrenome@ea.com`

`chlewin@ea.com` (Chris Lewin, EA/SEED), `jpower@ea.com` (James Power, EA/Tiburon) e
`jcobb@ea.com` (James Cobb, EA/Tiburon), no rodapé de *"Swish: Neural Network Cloth Simulation on
Madden NFL 21"*, SIGGRAPH 2021 Talks —
https://history.siggraph.org/wp-content/uploads/2022/06/2021-Talks-Lewin_Swish.pdf

### Valve — `nome+inicial@valvesoftware.com`

`joev@valvesoftware.com` (Joe van den Heuvel), `jamesc@valvesoftware.com` (James Cunliffe, **Animator**)
e `eddie@valvesoftware.com` (Eddie Parker), no rodapé de *"The Right Foot in the Wrong Place:
Character Locomotion in Half-Life: Alyx"*, SIGGRAPH 2021 Talks —
https://history.siggraph.org/wp-content/uploads/2022/06/2021-Talks-Heuvel_The-Right-Foot-in-the-Wrong-Place.pdf

### MPC / Moving Picture Company — `nome-duasletrasdosobrenome@`, em DOIS domínios

`michael-g@moving-picture.com` (Michael Gregory, **Creative Director**) e
`daniel-se@moving-picture.com` (Dan Seddon, VFX Supervisor), no rodapé de *"Creating Photoreal
Creatures that Audiences Can Connect With"*, SIGGRAPH 2019 —
https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Gregory_Creating-Photoreal-Creatures-that-Audiences-Can-Connect-With.pdf
E, no mesmo formato, em `mpcfilm.com`: `yanli-z@`, `darryl-g@`, `rob-p@` (*"Sculpting Color Spaces"*,
2019) e `rasmus-h@`, `christoph-ge@` (*"Mesh-Driven Generation and Animation of Groomed Feathers"*,
2019).

**Por que isto NÃO virou ficha nesta rodada, e a razão é dupla:** (1) o `pessoas.csv` já tem **duas**
pessoas de MPC (Beatrice Bauwens e Christophe Courgeau, as duas do braço Paris/Liège, em
`mpcvfx.com`), ou seja a casa está no teto; (2) nenhum dos dois domínios acima foi reconferido quanto
à vigência depois da queda do grupo Technicolor. Fica registrado como **formato**, não como porta.

### Blue Sky Studios — o caso em que o rodapé publica GMAIL, e por que isso não serve

O talk *"Reinventing a Character Creation Pipeline"* (SIGGRAPH 2021) traz cinco autores da Blue Sky e
**nenhum endereço corporativo**: `polyoptics.ca@gmail.com`, `chaniszewski@gmail.com`,
`toddejhill@gmail.com`, `chris.pagoria@gmail.com`. São endereços pessoais **publicados** e ainda
plausíveis — mas a **Blue Sky fechou em 2021**, então o vínculo morreu junto e não se sabe onde cada
um está hoje. **Cargo desatualizado é pior que alvo nenhum**: registrado só como aviso.
