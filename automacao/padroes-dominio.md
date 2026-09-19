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

---

## 19/09/2026 01h35 (Joe) — QUATRO ARMADILHAS DE LEITURA E UMA VEIA MORTA, todas medidas em 2.395 páginas de 1.446 domínios

Nenhum endereço montado saiu desta rodada; as seis fichas são literais publicados. O que vale registrar
aqui é **por que um endereço publicado pode parecer inexistente**, e **um dominio pode parecer dois**.

### 1. A família Stunlock ganhou um terceiro membro, e ela custou uma carta em 26/08: **MATHEMATIC**

O grupo usa **três** domínios: **`mathematic.tv`** (o estúdio, onde os endereços de pessoa estão
publicados: `bea@`, `rebecca@`, `guilow@`, `hadi@`, `guillaume.marien@`), **`mathematicfilm.com`** (o
rótulo de cinema) e **Player Two** como rótulo de jogo. A campanha mandou a carta fria de 26/08 e o
follow-up de 02/09 para `contact@mathematicfilm.com`, ou seja **para o domínio do rótulo, não para o
do estúdio**. Zero resposta. **Antes de dar uma casa como "já tocada e silenciosa", confira em qual
dos domínios dela a carta caiu.**

No mesmo dia apareceu o caso inverso, e ele **furou meu dedupe por endereço**: a **TELEVISOR** publica
o mesmo Michał Truszkowski como `michal.truszkowski@televisor.pl` (no `mailto:`) **e** como
`michal.truszkowski@televisor.studio` (no texto visível). Só o segundo está em `enviados.csv`, com
carta de 11/09. **Duas grafias do domínio da mesma casa derrotam dedupe por endereço; o que segurou
foi o `search_threads` do Gmail pelo sobrenome.** E a **B-Water** faz o mesmo com `.com` e `.es`
(`dh@b-waterstudios.com` publicado na `/contact`, e a resposta humana de 26/08 veio de
`idayra.pd@b-waterstudios.es`).

### 2. `mailto:` em **ENTIDADE HTML DECIMAL** — a Nuttery, e o `grep mailto` cru não vê

`https://nutteryentertainment.com/` publica

```
mailto:ma&#103;nus&#064;n&#117;tt&#101;rye&#110;&#116;&#101;rt&#097;inme&#110;t&#046;com
```

que é `magnus@nutteryentertainment.com`. Não é Cloudflare, não é ROT13: é entidade decimal misturada a
caracteres normais, **letra por letra**, para quebrar raspador de regex. Os três endereços do time
(`magnus@`, `erik@`, `lee@`) vêm assim. Conserto: `html.unescape` **antes** de qualquer regex de
e-mail. Ficou incorporado na varredura desta rodada, junto de `data-cfemail`, `data-enc-email` em ROT13
e `(at)`/`(dot)`.

```sh
curl -sS -L <url> | python3 -c "import sys,html,re;t=html.unescape(sys.stdin.read());print('\n'.join(sorted(set(re.findall(r'mailto:([^\"\x27?]+)',t)))))"
```

### 3. **DUPLA** escapagem de entidade em site de construtor — Red Vault, e é o cargo que se perde

Em `https://redvaultinteractive.com/about` o endereço sai com um `unescape`, mas **o cargo não**: o
texto dos cartões mora em JSON embutido com `&amp;quot;` dentro de `&quot;`. Com uma passada a ficha
nasce com "Tim Israelsson" e **sem** "Character Artist and Animator". **Duas passadas de
`html.unescape` viraram regra para site de construtor**, e o controle é simples: se o HTML contém
`&amp;quot;`, falta uma passada.

### 4. **406 não é 404**: porteiro de cabeçalho, medido na Clever Plays

`clever-plays.com` responde **200 na home** e **406 de 226 bytes** em toda subpágina (`/press-kit`,
`/about`, `/team`, `/contact`) quando o `curl` vai com User-Agent curto. Com cabeçalho de Chrome
completo **mais** `Accept: text/html,...` **e** `Accept-Language`, a mesma `/happy-bastards/` devolve
**200 com 93.204 bytes**. **Quem anotar "406 = página não existe" perde o gancho da casa.** É parente
do 404 gordo do Wix e do `presskit/data.xml`: **o corpo da resposta mente sobre a existência da
página.**

### 5. A veia do `recruiter-email` do Teamtailor está MORTA, com número

Varrida em `/careers`, `/career`, `/jobs`, `/careers/`, `/join-us` e `/` nos **1.128 domínios** de
Canadá, Nórdicos, Holanda, Reino Unido, Oceania e resto da Europa (`censo-wikidata.csv` +
`garimpo-cgstudiomap.csv`): o campo apareceu em **um único domínio, `stunlock.com`**, que já está
registrado desde 07/09. **Rendimento novo: zero.** A veia continua rica quando acerta, mas ela é
**rara demais para varredura** — vale só como teste de uma requisição em casa nova. Não gaste rodada
nela outra vez.

### 6. Endereços publicados achados e NÃO usados, guardados com o motivo

- **`marika.makaroff@gutsy.fi`** (Marika Makaroff, *Founder & CCO*), **`katherine.senior@gutsy.fi`**
  (*Commercial Director*) e **`emmi.nilivaara@gutsy.fi`** (*Concept Developer*) — Gutsy Pictures /
  Gutsy Animations, a casa de **Moominvalley**. Os três publicados com nome, cargo e bio em
  `https://www.gutsy.fi/`. **Não usar: a página diz *"Gutsy Pictures does not accept unsolicited
  material."*** Recusa escrita.
- **`timo.hakkarainen@kallagameworks.com`** (Timo Hakkarainen, **3D Artist**) — Kalla Gameworks,
  Kuopio, Finlândia. Pareado na home. Parado por disciplina do produto (*The Pegasus Expedition* é
  grand strategy de frotas). **Reabrir se a casa mudar de produto.**
- **`mette@galdrastudios.com`** (Mette Jakobsen, *Art & Writing*), `daniel@` e `jesper@` — Galdra
  Studios, Dinamarca. Parado por **visual novel**.
- **`Astrid@tripletopping.com`** (Astrid Refstrup, *CEO, Owner, Game-Director*; a mesma página nomeia
  **Inna Hansen, Art Director and Concept Artist**, sem endereço) — Triple Topping, Dinamarca, saiu de
  `data-cfemail`. Parado por **2D desenhado à mão**.
- **`deep@elevenfx.com`** (Deep Chahal, *Co Founder | Director*) — Eleven FX, Auckland. Parado por
  disciplina: a casa vende edição, VFX e cor, sem pipeline de personagem.
- **`scott@hilltop.so`** (Scott Christian, *co-founder*, narrativa e música) — Hilltop Studios,
  Toronto. Parado porque o **diretor de arte da casa declara ilustração 2D** (*"a distinct
  illustration art style"*, Artiom Komarov) e porque o endereço do lado de arte **não é publicado**.
- **`rax@threewintersgames.com`** — Three Winters Games, Montréal, casa nova de veteranos. **Endereço
  sem pessoa:** o local não é nome de ninguém achável e nem a ficha da Guilde nem o site nomeiam
  alguém. Não vira carta enquanto não houver pareamento.
- **`john@overthemoongames.com`** — Over The Moon, **Vancouver BC**, que é a primeira prioridade
  geográfica da campanha. O site está em obra (*"Unpacking…"*, 200, 471.866 bytes, sem uma linha de
  texto). **Endereço guardado; falta o pareamento nome+cargo em fonte aberta.**

---

## ADENDO DE 19/09 ÀS 02h35 (Joe) — **UBISOFT reprovada com endereço literal DE 2026, e o detalhe do HÍFEN**

O padrão `nome.sobrenome@ubisoft.com` estava provado por **rodapé de paper do SIGGRAPH de 2019**
(seção "UBISOFT — padrão provado por três endereços literais"), e a nota de 12/09 registra que
rodapé de paper prova **formato** e não **vigência da caixa**. Agora existe uma prova **de hoje**, na
página que o próprio grupo mantém:

| Endereço | Pessoa e cargo | Fonte, aberta em 19/09 às 02h35 |
|---|---|---|
| `antoine.leduc-labelle@ubisoft.com` | **Antoine Leduc-Labelle, Public Relations Manager** | `https://montreal.ubisoft.com/press` (**200, 209.240 bytes**; `/en/press` devolve a mesma página), bloco *"Media contact"* |

**O que isso acrescenta, e é acionável:** o sobrenome composto entra **com o hífen preservado**
(`leduc-labelle`, e não `leduclabelle` nem `leduc.labelle`). Toda montagem futura em `ubisoft.com`
para nome composto tem de manter o hífen do sobrenome e o ponto só entre nome e sobrenome. Isso
também reduz um pouco a leitura de 06/09 para **este** domínio: o formato segue vivo em 2026, o que
não muda a régua — montado continua **BAIXA**, porque o que falha é a caixa da pessoa, não o formato.

**E por que este endereço NÃO virou ficha nem carta** (registrado aqui para nenhuma rodada reabrir):
a própria página escreve, na linha de baixo, ***"*For media requests only. For all other requests,
write to infomtl@ubisoft.com"***. É recusa de escopo por escrito. Somado a isso, *Public Relations
Manager* não é nenhum dos alvos que o `BRIEF-JOE` manda perseguir em casa grande (recrutador de arte
com nome, Character Art Lead, ou artista sênior de dentro). A **Ubisoft Montréal** segue como casa
sem nenhuma pessoa na campanha — Massive tem uma (`jevgeni.laur@`, que **quicou** em 06/09) e Québec
tem duas (Henrick Pelletier e Thierry Dansereau).

## PADRÕES NOVOS PROVADOS EM 19/09 ÀS 02h35 (Joe), todos por endereço LITERAL publicado

### FiolaSoft Studio (Praga, Tchéquia) — `nome.sobrenome@fiolasoft.cz`, **sete** endereços provam

| Endereço | Pessoa e cargo | Fonte |
|---|---|---|
| `filip.kraucher@fiolasoft.cz` | Filip Kraucher, *Producent* | `https://fiolasoft.cz/about` (200, 22.786 bytes), cartão da seção *Jádro týmu* |
| `vojta.stransky@fiolasoft.cz` | Vojtěch Stránský, *Programátor* | idem |
| `vojta.siman@fiolasoft.cz` | Vojta Šiman, *Level Designer* | idem |
| `tomas.otahal@fiolasoft.cz` | Tomáš Otáhal, *Herní designér* | idem |
| `jakub.mirejovsky@fiolasoft.cz` | Jakub Miřejovský, *Sound Designer* | idem |
| `radek.jakl@fiolasoft.cz` | **Radek Jakl, *Vedoucí grafik*** | idem — **virou ficha nesta rodada** |
| `patrik.strnad@fiolasoft.cz` | Patrik Strnad, *Level Designer* | idem |

**Exceções no mesmo domínio, e elas importam:** o apelido vale (`vojta.siman`, não `vojtech.siman`), e a
casa usa **outro domínio** para a caixa de negócios (`bd@fiolasoft.com`, rotulada *"Kontaktní osoba Filip
Kraucher"*) além de `kontakt@fiolasoft.cz`. Não publicado: **Oleksii Avdieichyk** (*3D Grafik*), **Kateřina
Šumová**, **Rado Markovič**, **Hana Lískovcová**, **Lukáš Jech**.

### Wil Film (Copenhague, Dinamarca) — `nome.sobrenome@wilfilm.dk`, **cinco** endereços provam, **e a casa está VETADA**

| Endereço | Pessoa e cargo | Fonte |
|---|---|---|
| `anne.jorgensen@wilfilm.dk` | Anne Jørgensen, *Business & Legal* | `https://wilfilm.dk/team` (200, 129.858 bytes) |
| `brith.dahl@wilfilm.dk` | Brith Dahl, *CFO* | idem |
| `jimmi.gravesen@wilfilm.dk` | Jimmi Gravesen, *Head of Technology* | idem |
| `louise.barkholt@wilfilm.dk` | Louise Barkholt, *Producer* | idem |
| `morten.stahlhut@wilfilm.dk` | Morten Stahlhut, *Line Producer* | `https://wilfilm.dk/jobs` (200, 82.040 bytes), dentro do anúncio |

**Exceção:** o CEO usa a forma curta, `erik@wilfilm.dk` (Erik Wilstrup) — **carta enviada em 15/09**.
**NÃO MONTAR NADA NESTE DOMÍNIO, E NÃO MANDAR FOLLOW-UP:** a `/jobs` traz veto de visto por escrito —
*"**VISA Requirements — Apply for an open position ONLY if you are a EU pass holder.** Unfortunately, the
process and requirements in order to qualify for a work permit according to the Danish law can be very
complicated"*. O cargo que a campanha mais quer existe ali (**`Toke Uthaug Rasmussen — Head of
Modelling`**, mais dois *CG Supervisors*, um *Animation Supervisor*, dois *Concept Artists* e um *CG
Generalist / Modeler*, pipeline **Maya/NUKE** declarado) e **o endereço dele não é publicado** — o veto
fecha a porta antes da montagem.

## UMA CAMADA DE OFUSCAÇÃO NOVA, E NENHUM DECODIFICADOR DE TEXTO PEGA: **O DOMÍNIO DESENHADO COMO IMAGEM**

Até 18/09 este arquivo e o `BRIEF-JOE` listavam quatro camadas a decodificar antes de declarar "casa sem
e-mail": `data-cfemail` do Cloudflare, `data-enc-email` em ROT13, entidade HTML decimal e `(at)`/`(dot)`.
**Existe uma quinta**, achada em 19/09 na EGOSOFT: a página de vagas
`https://www.egosoft.com/company/jobs_en.php` (**200, 24.092 bytes**) tem **zero caracteres `@` no HTML
inteiro** e o que está escrito é

```html
<div align="center">Jobs @ <img src="/img/egosoft.gif" alt="" border="0" width="128"> . com </div>
```

ou seja **o domínio é um GIF** entre o `@` e o `.com`, com `alt` vazio. Decodificado pelo contexto:
`jobs@egosoft.com`. **Como detectar sem abrir a página no olho:** procurar `@` seguido de `<img` na mesma
linha, ou `<img` cercado por `@` e `.com`/`.de`/`.fr`. Onde isso aparece, o endereço é a concatenação
`local + @ + nome-do-arquivo-da-imagem + TLD`, e o nome do arquivo (`egosoft.gif`) costuma ser o próprio
domínio.

## ENDEREÇOS PUBLICADOS ACHADOS EM 19/09 ÀS 02h35 E **NÃO** USADOS, cada um com o motivo

- **`selina@5am-games.com`** (Selina Capol, ***Artist & Co-Founder***), `aleksandra@5am-games.com`
  (*CTO & Co-Founder*) e `martina@5am-games.com` (*Level Designer & Co-Founder*) — 5am Games, Zurique,
  Suíça, equipe 100% feminina. Os três pareados na `/about` (200, 139.844 bytes). **Parado por disciplina
  do produto:** *LETTERS – A written adventure* é jogo de palavra e tipografia, *Konditorei Kritzel* é
  protótipo de escrita manual para a ZHdK e *Radical Choices* é serious game. **Reabrir se a casa fizer
  jogo com elenco 3D.**
- **`till@awfullynicestudios.com`** (Till Aschwanden, *"ART MONKEY"*, e a bio dele diz *"4 years of
  experience as a **character artist working as a 3D modeler for Blizzard Entertainment**"*) e
  `rainer@awfullynicestudios.com` (Rainer Zoettl, *"DEV MONKEY"*, ex-Weta Digital e Scanline) — Awfully
  Nice Studios, Áustria. **Parado por 2D declarado na própria bio** (*"his true passion is in the world of
  2D … flash and photoshop"*), casa de duas pessoas e rodapé © 2023. **O histórico dos dois é ouro para
  rede, não para carta de vaga.**
- **`manu@firm-studio.fr`** (Beard Manuel, *Founder*), `julien@firm-studio.fr` (Amiard Julien, *Founder*),
  `coralie@firm-studio.fr` (Duarte Coralie, *Head Of Production*), `charlotte@` e `claire@` (*Production*),
  mais `job@firm-studio.fr` com convite escrito (*"We are always looking for new talents. VFX artists,
  Artistic directors, 2D and 3D directors, feel free to send us your reel or book"*) — Firm Studio, Paris.
  **Parado por disciplina:** pós-produção de comercial de beleza e luxo (Guerlain, Chanel, Dior, Bulgari),
  zero `character`/`creature`/`personnage` no domínio.
- **`erin@fortyork.tv`** (Erin Kuttner, *EP / Managing Director*), `valerie@`, `armen@`, `katie@` — Fort
  York VFX, Toronto. **Parado por disciplina:** *"colour grading, compositing, animation, motion design
  and graphics"*.
- **`andy@redlabto.com`** (Andy Hunter, *Flame Artist/Owner*), `walt@` (Walt Biljan, *Colourist/Owner*),
  `mark.s@` (Mark Stevens, *Head of Sales/Owner*) — REDLAB, Toronto. **Parado por disciplina:** cor e Flame.
- **Oito endereços `nome.sobrenome@thepostlounge.com`** (Kurt Royan *Managing Director*, Georgia Woodward
  *COO*, Matt Bennett *Creative Supervisor*, e cinco de produção/negócios) — The Post Lounge,
  Brisbane/Melbourne/Sydney/Gold Coast. **Parado por disciplina:** finalização de pós, zero `character`.
- **`ryan@builtbysnowman.com`** (Ryan Cash, *Founder & Creative Director*) — Snowman, Toronto. **Parado
  por disciplina:** *Alto's*, *Where Cards Fall*, *Skate City*, *Pok Pok*.
- **`olli.etuaho@lockpickle.com`** (Olli Etuaho, fundador **engenheiro** ex-NVIDIA) — Lockpickle,
  Helsinque. **Parado por cargo e produto:** puzzle, três pessoas, nenhuma cadeira de arte nomeada.
- **`macura@cinemaxgames.com`** — Cinemax, Praga. **Endereço SEM PESSOA:** o site `cinemax.cz` é SPA e
  devolve a mesma página de 31.878 bytes sem um nome em `/`, `/about`, `/team` e `/contact`. Armadilha de
  domínio registrada: site `.cz`, e-mail `@cinemaxgames.com`.
- **`sinsem@triskell-interactive.com`** — Triskell Interactive, Lannion/Rennes. Sem nome, e *"We are
  producing **2D games**"*.
- **`michal@circusatos.com`** e **`bara@circusatos.com`** — Circus Atos, Praga. **Recusa escrita:**
  *"Currently, we are not looking for any collaborators, and we don't do any contract work."*
- **`lino@` na EGOSOFT NÃO EXISTE PUBLICADO, e é o cargo certo.** A home da EGOSOFT publica
  *"Interview with **Lino**: Egosoft **Art Director**"*, com ele em primeira pessoa e 14 anos de casa, mas
  **só o primeiro nome**. Quem achar o sobrenome dele em fonte pública fecha a **segunda e última** pessoa
  da EGOSOFT. **Não montar.**
- **`petja@` e `janne@brinkhelsinki.com` NÃO EXISTEM PUBLICADOS.** A `/team` da Brink nomeia três
  *Animation Directors* e publica endereço de **um** só (`ilari@`). Petja Salmio e Janne Roivainen ficam
  sem endereço, e o teto da casa já fechou com Ilari Koskinen (15/09) e Alexander Seraidaris (esta rodada).
- **`toke.*@wilfilm.dk` NÃO MONTAR** — ver o veto de visto da Wil Film acima.

## Sobre o `john@overthemoongames.com` (Vancouver), agora com o motivo fechado

A nota anterior dizia *"falta o pareamento nome+cargo em fonte aberta"*. O pareamento **existe**, mas não
serve: `https://www.gamegrin.com/news/the-last-hero-of-nostalgaia-launches-in-2022/` (**200, 45.350
bytes**, aberta em 19/09) escreve *"has been described as a love letter to Dark Souls and its community by
**Over The Moon CEO, Jon Warner**"* — é **paráfrase de jornalista de dezembro de 2021**, não a casa falando
em primeira pessoa, que é o que a regra de 18/09 exige. E `overthemoongames.com` (**200, 472.233 bytes**)
segue em obra, com três linhas de texto (*"This page requires JavaScript to display. Unpacking…"*).
**Endereço guardado; carta não, enquanto a casa não voltar a publicar alguma coisa.**

## PADRÕES PROVADOS EM 19/09/2026 ÀS 04h35 (Joe), todos por endereço LITERAL publicado

Nada aqui é inferido. Cada linha tem pelo menos dois endereços reais do mesmo domínio, e onde o
domínio usa **mais de um formato** isso está escrito, porque esconder a exceção transforma confiança
baixa em chute.

### A REGRA NOVA QUE ESTE ARQUIVO AINDA NÃO TINHA: **PRIMEIRO NOME REPETIDO QUEBRA O PADRÃO, E O SEGUNDO HOMÔNIMO LEVA NOME+SOBRENOME COLADO**

A `/nosotros` da **Keytoon Animation Studio** (Paterna, Valência) publica os três da casa e o domínio
mostra o mecanismo inteiro numa página só:

| Endereço | Pessoa | Cargo |
|---|---|---|
| `david@keytoon.com` | **David** Cuevas | Director |
| `davidlacruz@keytoon.com` | **David** Lacruz | Productor |
| `jon@keytoon.com` | Jonathan Cuevas | Director |

O padrão da casa é **primeiro nome puro** (`david@`, `jon@`), mas **há dois Davids**, e o segundo
recebeu **nome+sobrenome colado, sem ponto** (`davidlacruz@`). Isto vale para a campanha inteira:
**quando um padrão de primeiro nome falha, a alternativa natural não é `nome.sobrenome` — é
`nomesobrenome` colado**, porque quem configurou a caixa estava resolvendo uma colisão, não mudando de
convenção. Fonte: `https://www.keytoon.com/nosotros` (200, 149.725 bytes, aberta em 19/09 às 04h35),
onde os três cartões trazem nome, cargo e `mailto:` no mesmo bloco.

### Freefolk (Londres) — **DUAS formas no mesmo domínio, e a separação é por antiguidade de cadeira**

`https://www.freefolk.com/contact` (**200, 23.628 bytes**) publica **treze** pessoas com cargo, todas
com o endereço ofuscado em `data-cfemail` do Cloudflare. As formas:

- **Primeiro nome puro** para a direção e a produção sênior: `fi@` (Fi Kilroe, *CEO / Executive
  Producer*), `paulw@` (Paul Wright, *COO* — **nome + inicial do sobrenome**), `vittorio@` (Vittorio
  Giannini, *Director of Business Development & Strategy*), `cheryl@` (Cheryl Payne, *Head Of Commercial
  Production*), `charles@` (Charles Gillett, *Producer*), `jessica@` (Jessica Verner, *Producer*),
  `meg@` (Meg Guidon, *Film and Episodic Executive Producer*), `sean@` (Seán O'Keefe, *PR & Marketing
  Manager*).
- **`nome.sobrenome@`** para quem entrou depois: `laura.ricketts@` (*Executive Producer*),
  `hannah.dakin@` (*Senior Producer*), `regan.perry@` (*Producer*), `robyn.guthrie@` (*Producer*),
  `megan.hindle@` (*VFX Coordinator*).

**Leitura:** num domínio assim, para nome novo **tente `nome.sobrenome` primeiro**, porque a forma
curta está tomada pelos antigos. E note que a casa é *"a registered trading name of **Finish TV Ltd**"*,
ou seja o grupo tem outro nome jurídico — armadilha de domínio a mais.

### SSVFX (Dublin) — **um formato, DOIS domínios**, o do estúdio e o do grupo-mãe

`inicial+sobrenome@`, e a seção *Meet the Team* de `https://www.ssvfx.ie/about` (**200, 20.762 bytes**)
publica os oito com `mailto:` cru e com o endereço repetido no atributo `title`:

| Endereço | Pessoa | Cargo |
|---|---|---|
| `ckeenan@ssvfx.ie` | Ciarán Keenan | Head of Production |
| `dnolan@ssvfx.ie` | Donal Nolan | VFX Supervisor |
| `lmcdowall@ssvfx.ie` | Laura McDowall | VFX Producer |
| `jkha@ssvfx.ie` | Johnni Kha | VFX Producer |
| `rgantly@ssvfx.ie` | Ronan Gantly | VFX Supervisor |
| `jwalshe@screenscene.ie` | Jake Walshe | President & CEO |
| `mobyrne@screenscene.ie` | Mura O'Byrne | Vice President and CFO |
| `hmontag@screenscene.ie` | Hubert Montag | COO |

**Os três do topo usam o domínio do grupo (`screenscene.ie`) e o mesmo formato.** Quem procura só o
domínio do estúdio perde a diretoria inteira.

### REALTIME (Real-Time Visualisation Ltd, Reino Unido) — `primeironome@realtimeuk.com`, com **prova de entrega**

`jane@realtimeuk.com` (Jane Forsyth, *Head of Production - Games*) recebeu carta em **07/09** e
**entregou, sem bounce** (`enviados.csv:741`). O rodapé de `https://www.realtimeuk.com/` (**200,
150.032 bytes**) publica mais três `mailto:` **rotulados por divisão e sem nome**: `dave@`→*Games* e
*Episodic & Film*, `paul@`→*Automotive*, `tony@`→*Immersive*; e
`https://realtimeuk.com/general-contact/` (**200, 69.406 bytes**) publica os **nomes com cargo e sem
endereço**: *David Cullinane — Executive Producer - Games*, *Paul McSweeney — Head of Automotive*,
*Tony Prosser — CEO*. **O casamento fecha nos três por rótulo de divisão E por primeiro nome.**
Método: quando o rodapé dá endereço sem nome, a página de contato costuma dar nome sem endereço —
**são as duas metades da mesma tabela**.

### B·Water Animation Studios — **DOIS domínios da mesma casa, com DOIS formatos diferentes**, e é a armadilha mais fina desta rodada

| Domínio | Formato | Endereços reais |
|---|---|---|
| `b-waterstudios.com` | **iniciais** (2 letras) | `dh@` (Dirk Hampel, *CEO*), `cb@` (Carlos García, *T. D. Director*), `ag@` (Angélica García, *General Manager*), `info@` |
| `b-waterstudios.es` | **nome.inicial(is) do sobrenome** | `fabian.s@` (Fabian Schier, *Ex. Producer assistant*), `idayra.pd@`, `juan.cg@`, `andrea.ug@` |

Os quatro primeiros e o `fabian.s@` estão publicados em `https://b-waterstudios.com/contact/`
(**200, 91.278 bytes**, `dateModified 2025-12-04`), com nome e cargo entre parênteses ao lado de cada
um. Os três do `.es` são **reais e vivos**: vieram do **Cc de uma resposta que a própria casa mandou ao
Vini em 26/08** (thread `1a03e2b4fabb6674`, de `idayra.pd@b-waterstudios.es`, Operations Department).
**Escrever para o `.com` quando a pessoa está no `.es` (ou o contrário) é erro garantido**, e as duas
formas não se convertem uma na outra.

### Quatro domínios de `nome.sobrenome@` provados por seis ou mais endereços publicados

- **`alteregopost.com`** (Alter Ego — Toronto, Vancouver, Los Angeles) — 6: `greg.edgar@` (*CEO /
  Managing Partner*), `hilda.pereira@` (*VP / Executive Producer*), `pravina.sippy@* (*EP / LA*),
  `craig.harris@` (*Managing Partner / Vancouver*), `genna.mcauliffe@` (*EP / Long Form*),
  `jane.garrah@` (*EP / Colour*). Fonte: `https://www.alteregopost.com/contact` (**200, 53.204 bytes**).
  **Bônus grande:** a mesma página lista **43 pessoas do time com cargo e SEM endereço**, incluindo
  *Leonardo Silva — **Head of CG***, *Darren Achim — **Head of VFX***, *David Whiteson — **Head of
  VFX***, *Erica Hou — **CG Artist*** e *Rob Fisher — Head of Motion Design*. Os endereços deles seriam
  **montados**, e a casa é grande — **não gastar a única carta num montado**.
- **`company3.com`** (Company 3) — **23** endereços `nome.sobrenome@` publicados em
  `https://www.company3.com/contact` (**200**). Uma exceção medida: `lindseyarnold@` (colado) coexiste
  com `lauren.arnold@`, o que é **outra colisão de sobrenome** resolvida por colagem — mesma mecânica
  da Keytoon.
- **`mels-studios.com`** (MELS, Montréal) — 6: `patrick.jutras@quebecormedia.com` (*Président*, e note
  o **domínio do grupo Québecor**), `auree.lepage@`, `raphael.rainville@`, `frederic.boucher@` (o
  publicado é `fred.boucher@`, **apelido e não o nome do cartão, que diz "Frederic Boucher"**),
  `sophie.houle@`, `jerome.bourgault@`. Fonte: `https://www.mels-studios.com/contact/` (**200, 55.020
  bytes**). **Cuidado: o cartão escreve "Frederic" e a caixa é `fred.`** — o domínio usa o apelido.
- **`rotorstudios.com`** (Rotor Studios — Sydney, Melbourne, Toronto, Nagoya) — 3 de pessoa
  (`colin.brennan@`, `kosuke.sawa@`, `shirley.li@`) mais **caixas de cidade** (`sydney@`, `melbourne@`,
  `toronto@`, `nagoya@`) e `incidents@`. Fonte: `https://www.rotorstudios.com/contact-us`.

### Três domínios franceses de `inicial.sobrenome@`, provados por cinco ou mais

- **`malherbe.paris`** — `e.birnbaum@` (Ella Birnbaum, *Managing & Creative Director*, Nova York),
  `m.cervantes@` (Maribel Cervantes Ochoa, *General Manager Asia Office & Creative Director*, Xangai),
  `j.dossantos@` (Johanna Dos Santos, *Chief of Staff*), `m.loiseau@` (Mallorie Loiseau,
  *Communication & Press relations*), `a.demalherbe@`, mais `myjob@`. Fonte:
  `https://malherbe.paris/contact-us` (**200, 106.724 bytes**).
- **`epicure.fr`** — 8: `b.niewiadomskyj@`, `c.cerutti@`, `c.martin@`, `e.dhonner@`, `e.jousse@`,
  `g.walbron@`, `s.cankaya@`, `s.domange@`.
- **`parmilesluciolesfilms.fr`** (Valence) — 8 com nome e cargo na `/a-propos` (**200, 32.243 bytes**):
  `j.ducmauge@` (Jérôme Duc-Maugé, *Producteur délégué*), **`f.bernard@` (François Bernard, *Directeur
  des productions et directeur studio d'animation*)**, `s.durand@` (Stéphanie Durand-Barracand,
  *Productrice fiction*), `b.petit@` (Bertrand Petit, *Directeur administratif et financier*),
  `p.pasquier@`, `i.canal@`, `m.prudon@`, `m.ayroulet@`. Note que **sobrenome composto é truncado no
  primeiro** (`s.durand@` para Durand-Barracand).

### Dois domínios de `inicial+sobrenome colado`, sem ponto

- **`atlantistv.fr`** (Kingsize / Atlantis TV, Paris) — 5: `cmalige@`, `cvignon@`, `fhouzelle@`,
  `jgalmisch@`, `jvivier@`.
- **`magelis.org`** (Pôle Magelis, Angoulême — **é a agência do polo, não um estúdio**) — **14**:
  `acsabas@`, `camiot@`, `cmirallez@`, `cnivault@`, `dbeauvallet@`, `ejacobjuin@`, `fbaillard@`,
  `fcros@`, `gzannier@`, `hbrunelle@`, `mmartinot@`, `plefort@`, `sdecros@`, `slilloriemain@`,
  `smassavie@`, `vmassiat@`. Serve como **porta de rede para os estúdios de Angoulême**, não como casa.

### Cocoa (Helsinque) — mais uma casa com DUAS formas, e a exceção é o CEO

`niko.waaralinna@cocoa.fi` (Niko Waaralinna, *CEO / EP*) é **`nome.sobrenome`**, enquanto todos os
outros são **primeiro nome ou apelido**: `lotti@` (Charlotte Molander), `eemeli@` (Eemeli Katajisto),
`ilona@` (Ilona Malinen), `anton@` (Anton Molander), **`dermot@` (Dermot Gallagher, *CFX — HEAD OF
STUDIO*)**. Fonte: `https://cocoa.fi/contact` (**200, 61.386 bytes**); o mesmo bloco repete em
`/about/`, `/studio-cocoa/` e `/production-service/`. **Nota de apelido: `lotti@` para Charlotte.**

### Autonomicity Games (Canadá) — `primeironome@acitygames.com` com cinco exceções medidas

`https://www.acitygames.com/team` (**200, 39.697 bytes**) publica uma tabela com **ROLE** e **EMAIL**
para **quatorze** pessoas. A forma principal é primeiro nome (`eugen@`, `marcos@`, `miguel@`, `kate@`,
`geo@`, `carlos@`, `yomi@`, `zxander@`), mas há `ceo@` (Sherif Botros), `chairman@` (Ramy Taraboulsi),
`sophiav@` (Sophia Vong, **nome + inicial**), `gilbertk@` (Gilbert Kong, **nome + inicial**),
`imack@` e `rchang@` (**inicial + sobrenome**), e `arty@` para **Alexander Melo** (apelido que não vem
do nome). **Casa registrada como descarte** (ver `PESSOAS-SEM-CARTA.md` desta rodada), mas o padrão
fica: num domínio pequeno convivem tranquilamente quatro formas.

### Endereços de pessoa PUBLICADOS achados nesta rodada e **NÃO** usados, com o motivo

| Endereço | Pessoa e cargo | Casa | Motivo de não virar carta |
|---|---|---|---|
| `cb@b-waterstudios.com` | Carlos García, *T. D. Director* | B·Water (Tenerife/Barcelona/Colônia/Budapeste) | **a casa já respondeu**: `idayra.pd@b-waterstudios.es` escreveu ao Vini em 26/08 e ele respondeu; isto é território do Comunicador, não prospecção |
| `ericr@lumapictures.com` | Eric Robertson, *New Business* | Luma Pictures (Melbourne/LA/Vancouver) | cargo é venda, e **`recruiting@lumapictures.com` quicou DUAS vezes** (02/09 e 06/09) |
| `keto@gimmick.dk` | Ulla Keto, *Studio Manager* | Gimmick VFX (Copenhague) | **veto escrito** na `/contact`: *"Work permit for the EU is needed"* |
| `dermot@cocoa.fi` | Dermot Gallagher, *CFX — Head of Studio* | Cocoa (Helsinque) | a única frase com `characters` do grupo é da **irmã 2D** (*"our wonderful sister company Boutique Animation will make you smile with characters … and 2D animation"*) |
| `vesku@toast.fi` | Vesa Vinni, *VFX* | Toast Post Production (Helsinque) | post de publicidade de **9 pessoas**, com `AI Services` e `Toastr ai` no menu principal |
| `tero@outo.fi`, `jussi@outo.fi` | *Creative Lead, Senior-animaattori* (×2) | Studio Outo (Oulu/Helsinque) | `hahmo` (personagem, em finlandês) dá **ZERO** no domínio; é animação de comunicação e ensino |
| `jon@keytoon.com` | Jonathan Cuevas, *Director* | Keytoon (Paterna, Valência) | **quinto toque no domínio**: `info@` em 04/08, 30/08 e 14/09, `david@` em 09/09 **com follow-up em 18/09**. A disciplina é ótima (*"animación 3D"*, Goya, vaga de **Modelador**) — reabrir só se o maestro quiser |
| `tom@cosavfx.com` | Tom Mahoney, *Partner / VFX Supervisor* | CoSA VFX | **virou ficha nesta rodada** |
| `erik@swiss.se` | Erik Holmedal, *Executive Producer* | Swiss International | **virou ficha nesta rodada** |
| `ckeenan@ssvfx.ie` | Ciarán Keenan, *Head of Production* | SSVFX | **virou ficha nesta rodada** |
| `dave@realtimeuk.com` | David Cullinane, *Executive Producer - Games* | REALTIME | **virou ficha nesta rodada** |

### Correção de arquivo: a **Keytoon não é de Madri**

`automacao/pessoas.csv:199` registra *"Keytoon Animation Studio, Espanha (Madri)"*. A `/contacto`
(**200, 150.522 bytes**, aberta em 19/09 às 04h35) diz, colado: *"KEYTOON ANIMATION STUDIO — Ronda
Narciso Monturiol Nº 6, oficina 108 B, Edificio Destro B, **Parque tecnológico, Paterna, Valencia
(46980)**"*, e a home diz *"Estudio de animación fundado en **Valencia, España**, en el año 2004"*.
Fica corrigido aqui para não propagar.

---

## JOE, 19/09 06h35 — **O `href` DO `mailto:` PODE MENTIR, E ELE MENTIU EM DOIS DOMÍNIOS NESTA RODADA**

Até agora este arquivo tratava o `href="mailto:…"` como a leitura confiável e o texto visível como a
possível decoração. **Medido hoje, é o contrário em duas casas, e numa delas o `href` aponta para
outra pessoa.**

### `televisor.pl` / `televisor.studio` (TELEVISOR Studio, Varsóvia, grupo PFX)

`https://televisor.pl/contact` (**200, 62.450 bytes**), cartão por cartão:

| Cartão | `href="mailto:…"` | Texto visível |
|---|---|---|
| Michał Truszkowski, *Studio Head* | `michal.truszkowski@televisor.pl` | `michal.truszkowski@televisor.studio` |
| Iwona Kachel, *Head of Postproduction* | `iwona.kachel@televisor.pl` | `iwona.kachel@televisor.studio` |
| **Michał Dębski**, *Client Partner* | **`mikolaj.valencia@televisor.pl`** | `michal.debski@televisor.studio` |
| Karolina Fesołowicz, *Client Partner* | `karolina.fesolowicz@televisor.studio` | (igual) |
| Magda Garska-Pasztelaniec, *Head of Growth* | *(nenhum)* | `magda.garska@televisor.studio` |

**Quem é o certo se resolve pela CAIXA, não por preferência:** a campanha escreveu em **11/09** para
`michal.truszkowski@televisor.studio` (a forma do **texto visível**) e a busca no Gmail devolve **o
`SENT` e nenhum mailer-daemon**. Oito dias sem 550: **`@televisor.studio` é a forma viva; `@televisor.pl`
é a antiga e serve só o site e a caixa funcional `career@televisor.pl`.** E `mikolaj.valencia@` é
resíduo de quem ocupava a cadeira do Dębski antes — **um `href` pode apontar para uma pessoa que não
existe mais na casa.**

### `dlpparis.com` (DLP Paris)

`https://www.dlpparis.com/contact` (**200, 45.000 bytes**) tem dois botões escritos `job@dlpparis.com`, e
**um deles aponta para `mailto:antoine@dlpparis.com`**. Ou seja a casa mostra uma caixa funcional e liga o
clique numa **pessoa sem nome publicado**. Os endereços de pessoa do domínio, com cargo, são:
`cedric@` (**Cédric Choppin**, *PARTNER / DIRECTOR*), `federico@` (**Federico Costa**, *PARTNER / ART
DIRECTOR*, já contatado em 11/09), `pascal@` (**Pascal Chinarro**, *PARTNER*), `nathesias@`
(**Nathésias Dellevi**, *FINANCIAL MANAGER*), mais `job@` e o `antoine@` órfão.
**Regra que sai daí: quando `href` e texto discordam, registre OS DOIS e resolva pela caixa (envio
anterior sem 550) ou por segunda fonte. Nunca escolha só porque um está no código.**

## `wp-json/wp/v2/types` REVELA TIPO DE CONTEÚDO DE PESSOA QUE NÃO ESTÁ NO MENU (achado em 19/09 06h35)

Em WordPress, `https://<dominio>/wp-json/wp/v2/types` lista os *post types* registrados, e às vezes há um
de **pessoa** que o menu do site não linka. Na TELEVISOR os tipos são
`post, page, attachment, nav_menu_item, wp_block, wp_template, wp_template_part, wp_global_styles,
wp_navigation, wp_font_family, wp_font_face, video, reel, **artist**`, e
`https://televisor.studio/wp-json/wp/v2/artist?per_page=100` (**200, 5.159 bytes**) devolve **quatro
perfis de artista** que não aparecem em navegação nenhuma: **Hubert Dłużniewski** (*Animation Director &
Online Artist*), **Krzysztof Fendryk**, **Mieszko Wiśniewski** e **Paweł Krzemiński** (slug
`artysta-testowy`, ou seja **um registro de TESTE deixado publicado**). A página
`/artist/hubert-dluzniewski/` (**200, 88.303 bytes**) traz a bio inteira (*"Renowned as the top online
artist in Warsaw … In 2018, he was recognized as the KTS winner for his groundbreaking 'Robson's bike'
social campaign animation … 15 years in the post-production and animation industry … notable clients
including McDonald's and Coca-Cola"*) e **nenhum endereço** além das duas caixas funcionais do rodapé.
**Vale como fonte de NOME e CARGO, não de endereço.**

E o mesmo `wp-json` dá **prova de disciplina em número**: `.../wp/v2/videos_tax?per_page=100` devolve as
categorias de trabalho **com a contagem**, e na TELEVISOR a primeira é `character_animation` com **44**
projetos (contra `motion_design` 142, `food_beverage` 154, `technology` 104, `vfx` 59, `transport` 32,
`case-study` 29, `health-beauty` 12). **Contagem de taxonomia é melhor prova de disciplina que contagem de
palavra-chave, porque é a casa classificando o próprio trabalho.**

## A CASA PODE PUBLICAR PESSOA POR **JSON:API DE OUTRO DOMÍNIO** (Frontier, 19/09 06h35)

`https://careers.frontier.co.uk/` (**200, 5.315.420 bytes**) renderiza no servidor o payload do Lever, e
foi de lá que saiu a Ellie Baldino em 12/09. **O que não estava registrado é que a MESMA página embute
também um segundo payload, de um Drupal em `cms.zaonce.net`**, e
`https://cms.zaonce.net/en-GB/jsonapi/node/team_member?page[limit]=50` (**200, 158.950 bytes**) devolve
**43 membros de equipe com cargo**, entre eles **"India" — *Senior Artist*, cuja bio diz *"current Project
Lead for the **Character Art** on Planet Zoo … My team and I are responsible for creating all of the cute
animals you see in-game … I first joined as a **Graduate Artist** in 2018 … then **Full Character
Artist**, then … **Senior Artist**"***. **Mas os artistas aparecem só com PRIMEIRO NOME** (India, Niki,
Carla, John, Mike…) e **sem endereço**; nome completo só nos executivos e no conselho (David Braben,
Jo Cooke, Piers Jackson, Yvonne Dawes…). **Serve para provar que a casa tem time de character art e para
o gancho de carta; não serve para achar endereço.**

## Endereços de pessoa PUBLICADOS achados em 19/09 06h35 e **NÃO** usados, com o motivo

| Endereço | Pessoa e cargo | Casa | Motivo de não virar carta |
|---|---|---|---|
| `cedric@dlpparis.com` | Cédric Choppin, *Partner / Director* | DLP Paris | **morreu por disciplina**: a casa é agência de pós de **beleza e automóvel** (Lancôme, YSL, Nivea, Garnier, Guerlain, Dior, Estée Lauder, Hyundai, Renault); `character` dá **ZERO** em `/`, `/about` e `/contact`, e `/work` responde **404** |
| `pascal@dlpparis.com`, `nathesias@dlpparis.com`, `antoine@dlpparis.com` | Partner, Financial Manager, e um órfão sem nome | DLP Paris | mesmo motivo, mais o `antoine@` **sem nome publicado** |
| `steve@jumbla.com.au` | Steve Bradshaw, *Head of Production* | Jumbla (Melbourne) | **está dentro de `<!-- -->` na `/contact`**, ou seja a casa REMOVEU o bloco da tela; e o domínio é `.com.au`, diferente do `jumbla.com` do site |
| `andrew@jumbla.com` | *(nenhum nome, âncora vazia ao lado de "London")* | Jumbla | `href` sem rótulo e sem nome |
| `aus@jumbla.com` | rotulado sob *Danielle Kilgour, Executive Producer* | Jumbla | é **caixa funcional** usada como endereço de uma pessoa nomeada; a Danielle fica guardada aqui como nome+cargo **sem endereço** |
| `yharniman@frontier.co.uk` | Yaz Harniman, *Talent Acquisition Partner* | Frontier Developments | **não é cargo complementar**: a Ellie Baldino, *Talent Acquisition Advisor* e **dona da requisição**, já levou carta em 14/09; escrever ao colega dela é passar por cima. A requisição **"Experienced Character Artist"** (department Art, team **Character**, Cambridge/Hybrid) **continua ABERTA hoje** na API oficial `https://api.eu.lever.co/v0/postings/frontier?mode=json` (**200, 199.544 bytes**, 12 vagas), e o `user` dela no payload **continua sendo a Ellie** |
| `lmowatt@frontier.co.uk` | Lee Mowatt, *(jobTitle nulo no payload)* | Frontier Developments | endereço publicado **sem cargo** |
| `paul@snafu-pictures.com`, `ross@snafu-pictures.com`, `natt@`, `joe@`, `joel@`, `tony@` | Paul Schleicher (*Co-founder/EP*), Ross Main (*Production Manager*), Natt Tapley (*Head Writer*), Joe Burns (*Head of Story*), Joel Veitch (*Creator – Bad Dinosaurs*), Tony Orsten (*Chairman*) | Snafu Pictures (Londres) | **morreu por disciplina e por cargo repetido**: `character`, `3D` e `sculpt` dão **ZERO** na `/team` (**200, 38.843 bytes**); é **produtora**, não fábrica, e o Dan Dixon (*Co-founder/EP*, mesmo cargo do Paul) já levou carta em 15/09 |
| `tash@engine-house.co.uk` | *(sem nome)* | Engine House (Redruth, Cornualha) | o endereço só existe **dentro do JSON-LD `Organization`** como e-mail da empresa, sem nome ao lado, e a `/team` (**200, 136.434 bytes**) publica os perfis **só com primeiro nome** ("Mike, the guy who makes everything look good") |
| `enna.licht@vfx.at`, `s.s@vfx.at`, `l.n@vfx.at`, `j.j@vfx.at`, `s.i@vfx.at`, `f.w@vfx.at`, `c.m@vfx.at`, `l.g@vfx.at`, `t.r@vfx.at`, `c.p@vfx.at` | Enna Licht (*Editorial/Schnittassistenz*), Svitlana Sergiienko (*VFX Artist*), Lee Niederkofler (*Senior Colorist/Creative Director*), Jacob Jabornig (*Colorist*), Stefan Imnitzer, Flynn Wiesenberger, Charly Müllner, Lisa Isabella Grabner, Thomas Rath, Clemens Puchinger | viennaFX (Viena) | a casa é **cor, mastering e editorial**; o **único** cargo sênior de VFX é o Felix Schruef, que **já é a pessoa registrada** da casa; o CEO **Christian Vollenhofer-Rohlfing** só tem `office@` (funcional); **Sebastian Blatter, *3D Generalist*, não tem endereço** |
| `thea@ntropic.com`, `helena@ntropic.com`, `mykeb@ntropic.com` | Thea Slevin (*EP, Londres*), Helena Lee (*EP, Nova York*), Myke Brown (*EP, Ho Chi Minh*) | Ntropic | **cinco das seis cadeiras publicadas são Executive Producer**; a Prudence Beecroft (*Managing Director*, Londres) **virou ficha** nesta rodada e fecha o teto. O `helena@` fica como **alternativa documentada**: foi a **própria autorresposta de ausência da Veronika Fontaine** que o indicou por escrito |
| `f.koenigs@`, `c.patorra@`, `s.grote@`, `a.fox@`, `d.dindar@sluggerfly.com` | Florian Königs (*Programminator*), Christian Patorra (*Game Boy*), Sebastian Grote, Annika Fox, Dilan Dindar | Sluggerfly (Essen) | cargos de programação e design, ou **piada sem função legível**; a Olha Osypenko, a única com `Artist` e `Senior` no título, **virou ficha** |
| `sander@polderanimation.com` | Sander Kamermans, *Production Design / Set Design* | Polder Animation (Utrecht) | é **ambiente**, a disciplina que a regra do Vini de 10/09 manda deixar por último; o Jean-Paul Tossings (*TD/Rigger*) **virou ficha** |
| `christophe@terminus-studio.com` | Christophe Moreau, *Co-Founder | VFX Sup.* | Terminus Studio (Nantes) | **virou ficha nesta rodada** |
| `iwona.kachel@televisor.studio` | Iwona Kachel, *Head of Postproduction* | TELEVISOR (Varsóvia) | **virou ficha nesta rodada** |

### `sluggerfly.com` — sete pessoas em `inicial.sobrenome@` com CARGO DE PIADA

`f.koenigs@`, `d.plassmann@`, `c.patorra@`, `o.osypenko@`, `s.grote@`, `a.fox@`, `d.dindar@`. Fonte:
`https://sluggerfly.com/` (**200, 12.152 bytes**, âncora `#weare`). **Aviso de uso:** os títulos são
brincadeira (*Programminator*, *Art Dictator*, *Game Boy*, *Employee of the Month*, *God of Destructive
Distractions*, *Executive Surpreme Elite Senior Pile Artist*), então **cargo real tem de vir de outra
fonte** antes de qualquer carta que afirme função.

### `ntropic.com` — duas formas convivendo, e a exceção é a EP mais antiga

`prudence@`, `thea@`, `helena@`, `mykeb@` são **primeiro nome ou nome+inicial**, e
`veronika.fontaine@` é **`nome.sobrenome`**. Fonte: `https://ntropic.com/about` (**200, 33.894 bytes**).
Mesma mecânica da Cocoa, onde a exceção era o CEO.

### `polderanimation.com` — primeiro nome, e **com hífen quando o nome é composto**

`bastiaan@`, `sander@` e **`jean-paul@`**. Fonte: `https://www.polderanimation.com/about` (**200, 50.257
bytes**). O hífen do nome **entra** no local, o que é o oposto do truncamento francês registrado na
Parmi Les Lucioles (`s.durand@` para Durand-Barracand).

### Armadilha de domínio morto: **`vancouveranimation.ca` NÃO é mais da indústria**

Tentado nesta rodada como porta para casas de Vancouver: responde **200 com 246.641 bytes** e o `<title>`
é *"Link RTP BEWOKWIN 2026 - Bocoran Game Gacor Malam ini dijamin Wede Nampol"* — **é site de aposta**.
Domínio expirado e revendido. **200 não é prova de que a fonte existe; confira o `<title>`.**
No mesmo pedaço de rodada, `digibc.org` (a associação de mídia digital da Colúmbia Britânica) responde
**403 de 103 bytes** em `/members/`, `/member-directory/` e `/wp-json/wp/v2/pages`, com e sem
*user-agent* de navegador, e `knowledgehub.creativebc.com/s/funding-recipients` (a lista de bolsistas da
Creative BC) **falha na verificação de TLS** (`unable to get local issuer certificate`) mesmo com
`--cacert /root/.ccr/ca-bundle.crt`. **As três portas de Vancouver desta rodada estão fechadas; a
`creativebc.com/programs-and-funding/interactive-digital-media/` abre (200, 222.768 bytes) mas só linka o
hub que não abre.**

### `parasol-island.com` (Parasol Island, Düsseldorf/Munique/Berlim) — **NOVE pessoas em `nome.sobrenome@`, todas ofuscadas em `data-cfemail` e todas decodificadas aqui**

Fonte: `https://parasol-island.com/about` (**200, 463.090 bytes**, aberta em 19/09 às 06h35). Na tela a
página imprime `[email protected]` em todos; o par nome↔cargo↔endereço sai de percorrer o documento e
casar cada `data-cfemail` com o último nome antes dele:

| Endereço decodificado | Pessoa | Cargo |
|---|---|---|
| `moritz.vonschroetter@` | Moritz von Schrötter | *Founder & Managing Partner* |
| `philip.hansen@` | Philip Hansen | *Founder & Director* |
| **`philippe.stalla@`** | **Philippe Stalla** | ***Partner, Animation*** |
| `sebastian.druschel@` | Sebastian Druschel | *Founder & Managing Director* |
| `till.emken@` | Till Emken | *Partner, Client Services* |
| `nils.hartmann@` | Nils Hartmann | *Chief …ive Officer, Managing Partner* (este aparece **em texto puro**, não ofuscado) |
| `hr@` | Merle Muß | *HR* |
| `accounting@` | Melanie Fischer | *Head of Accounting* |
| `hombre@` | Mila Mardan | *Office Management Düsseldorf* — e note que **`hombre@` é também a caixa geral da casa**, repetida sob os três endereços de escritório |

**Sobrenome composto NÃO é truncado** (`moritz.vonschroetter@` para *von Schrötter*), o que é o oposto do
padrão francês da Parmi Les Lucioles. **A casa está FORA da fila de prospecção porque JÁ RESPONDEU duas
vezes por `hr@` (03/09 e 06/09, a primeira dizendo *"Aktuell sind unsere Kapazitäten abgedeckt"*)** —
território do Comunicador. O `philippe.stalla@` fica guardado aqui para o maestro decidir.

### `studioruniq.com` (Studio RuniQ, Québec) — oito em **`inicial+sobrenome@`**, com cargo e biografia

`sgravel@` (Stéphane Gravel, *Production - Operations*), `pturcotte@` (Philippe Turcotte, *Design &
Scripting*), `twilson@` (Thomas Wilson, *Design - Art - Story*), `trigaud@` (Thomas Rigaud, *Animation -
Rig - VFX*), `dbergeron@` (Dave Bergeron, *Design - Art*), `lpatalano@` (Louis Patalano, *Storytelling*),
`glachance@` (Gabriel Lachance, *Engineering*), `bfagnant@`. Fonte: `https://studioruniq.com/team`
(**200, 503.199 bytes**; `/en/team` serve a mesma página byte a byte e `/equipe` não resolve).
**Casa SEGURADA pelo maestro** (jogo lançado é 2D à mão), e `character` dá **ZERO** no domínio inteiro,
o que confirma a leitura.

### `mikrofilm.no` (Mikrofilm, Oslo) — quatro sócias em **primeiro nome**, e cinco diretores SEM endereço

`lise@` (Lise Fearnley, *Producer and partner*), `tonje@` (Tonje Skar Reiersen, *Producer and partner*),
`kajsa@` (Kajsa Næss, *Director and partner*), `cathinka@` (Cathinka Tanberg, *Director and partner*),
mais `post@` (funcional). **Sem endereço:** Kristian Pedersen, Torill Kove, Robin Jensen, Hanne Berkaak,
Annette Saugestad Helland, os cinco *Director and designer*. Fonte: `https://mikrofilm.no/people`
(**200, 50.028 bytes**). **`3D` e `character` dão ZERO no domínio** — casa de autor e de traço, já
segurada.

### `finalfrontier.tv` (Final Frontier) — seis em **primeiro nome**, e a casa NÃO PUBLICA CARGO

`marcus@` (Marcus Lansdell, Barcelona/Nova York), `juanma@` (Juan Manuel Freire, Madri), `julieta@`
(Julieta Zajaczkowski, Buenos Aires), `michael@` (Michael Diaz, LA), `yeeman@` (Yeeman Lin, Xangai),
`gustavo@` (Gustavo "Gus" Karam, Singapura), mais `hello@` e `iwanttobe@` (funcional, e o
`iwanttobe@finalfrontier.tv` é a caixa de candidatura). Fonte: `https://finalfrontier.tv/about`
(**200, 175.457 bytes**). **Cada cartão traz nome, cidade, telefone e e-mail e NENHUM cargo** — é a razão
registrada em 06/09 para a casa não virar carta, e ela continua valendo. A mesma página vaza
`hello@1stlevel.games` e `hello@silk-gallery.com`, que são **as marcas irmãs**.

### `heycarbon.com` (Carbon) — **`inicial+sobrenome@` e primeiro nome convivendo**, tudo nos EUA

`ldefelice@` (Lauren DeFelice, Nova York), `gretchen@` (Gretchen Praeger, Chicago), `mmcmanus@`
(Matt McManus, *Managing Director*, Culver City). Fonte: `https://heycarbon.com/contact` (**200, 43.995
bytes**). **A mesma página publica representantes de venda de TERCEIROS** (`jake@stellarmass.co`,
`jill@`/`breanne@`/`maggie@`/`oren@grgdreps.com`, `sunoo@funkhaus.us`) — **não são da casa.**

### `hifi3d.com` (HiFi 3D, Nova York) — primeiro nome, com os DOIS Creative Director publicados

`jon@` (Jonathan Dorfman, *Executive Producer + Creative Director*), `szymon@` (Szymon Weglarski,
*Executive Producer + Creative Director*), `andrea@` (Andrea Sertz Jew, *Executive Producer + Sales*),
mais `staffing@` e `contact@`. Fonte: `https://www.hifi3d.com/contact` (**200, 61.415 bytes**). O menu da
casa tem uma aba literal **`Direction / Jon & Szymon`**. **A página vaza `maria@stenzandlew.tv` e
`sharon@stenzandlew.tv`, que são representantes de venda TERCEIRIZADOS.** Casa boa, fora da rodada só por
geografia (100% americana).

### `vfx.at` (viennaFX, Viena) — **`inicial.inicial@` com UMA exceção, e a página tem NOME DE TEMPLATE**

O padrão é a inicial do nome mais a inicial do sobrenome: `l.n@` (Lee Niederkofler), `j.j@` (Jacob
Jabornig), `s.i@` (Stefan Imnitzer), `f.w@` (Flynn Wiesenberger), `c.m@` (Charly Müllner), `l.g@`
(Lisa Isabella Grabner), `f.s@` (Felix Schruef), `s.s@` (Svitlana Sergiienko), `t.r@` (Thomas Rath),
`c.p@` (Clemens Puchinger), mais `office@`. **A exceção é `enna.licht@` (Enna Licht, *Editorial /
Schnittassistenz*), que é `nome.sobrenome`** — num domínio de dez iniciais. Fonte:
`https://vfx.at/team` (**200, 123.443 bytes**).
**ARMADILHA NOVA, e é para registrar: a mesma página publica DOIS NOMES DE TEMPLATE como se fossem
pessoas** — *Phyllis Price* e *Jeremy Phillips*, cada um com biografia em **lorem ipsum** (*"Donec eget
risus diam. In sit amet felis malesuada…"*) e **sem endereço**. Nome numa página de equipe **sem endereço
e com texto de placeholder ao lado não é pessoa da casa**; é o tema que a casa esqueceu de limpar, igual
ao endereço de Brooklyn e aos `techlink@qode.com` da Karandash.

### `snafu-pictures.com` (Snafu Pictures, Londres) — oito em primeiro nome, e o domínio do advogado é OUTRO

`dan@` (Dan Dixon, *Co-founder/EP*), `paul@` (Paul Schleicher, *Co-founder/EP*), `tony@` (Tony Orsten,
*Chairman*), `ross@` (Ross Main, *Production Manager*), `natt@` (Natt Tapley, *Head Writer & Creative
Development*), `joel@` (Joel Veitch, *Creator – Bad Dinosaurs*), `joe@` (Joe Burns, *Head of Story*),
mais `accounts@` (Beatriz Sardiña Prego, *Production Accountant*). Fonte:
`https://www.snafu-pictures.com/team` (**200, 38.843 bytes**). **Tony Morris, *Legal Counsel*, é publicado
com `hey@snafu-productions.com` — domínio DIFERENTE**, mais uma armadilha de domínio vizinho.

### `jumbla.com` — a caixa funcional usada como endereço DE UMA PESSOA NOMEADA, e o bloco COMENTADO

`soto@` (Marie Soto, *Executive Producer*, Madri) é o único endereço de pessoa vivo e visível. **Danielle
Kilgour, *Executive Producer*, Melbourne, é nomeada e o endereço ao lado dela é `aus@jumbla.com`**, caixa
funcional. **Steve Bradshaw, *Head of Production*, `steve@jumbla.com.au` (domínio DIFERENTE do site), está
dentro de `<!-- -->`** na `/contact` (**200, 80.934 bytes**), ou seja removido da tela. E
`andrew@jumbla.com` é uma **âncora `<a>` vazia** colada ao lado de "London", sem rótulo e sem nome.
**Três formas distintas de endereço que parece publicado e não está.**

### `globalmechanic.com` (Global Mechanic, Vancouver e Victoria, BC) — **DOIS critérios diferentes no mesmo domínio de DUAS pessoas**

`bruce@` é **primeiro nome** (Bruce Alcock, *Creative Director & Owner*) e `brodie@` é **SOBRENOME**
(Chris Brodie, *Executive Producer*). Fonte: `https://www.globalmechanic.com/design` (**200, 115.192
bytes**, aberta em 19/09 às 08h35) e o mesmo bloco no rodapé de `https://www.globalmechanic.com/`
(**200, 132.138 bytes**). **Num domínio de duas pessoas os dois critérios são diferentes, logo
NENHUM endereço desta casa sairia de montagem por padrão** — é o contraexemplo mais limpo do arquivo
contra endereço montado. A mesma página publica `liz@lizlainereps.com` (*Liz Shaw*,
*U.S. Representation*), que é **representante de venda de terceiro**.
**Armadilha de contagem:** `character` aparece **36 vezes** no HTML bruto da home e **as 36 são
texto de validação de formulário do Squarespace** (*"Value should be {0} characters long"*,
*"Email addresses should follow the format user@domain.com"*). A taxonomia de verdade está na
`/design`, e ela é *"Character | Drawing | Kids | Mixed Media | Vector | Painting"*.

### `hypergames.no` (Hyper Games, Oslo) — primeiro nome, e **só TRÊS das treze pessoas têm endereço**

`are@` (Are Sundnes, *CEO & Co-founder*), `terje@` (Terje Gran, *CTO & Co-founder*), **`runa@`
(Runa Haukland, *Project Manager*)**, mais `kristina@` (Kristina Haley, *Marketing & Community
Manager*), que a `/contact` publica **com `(at)`**: *"For content creator key requests use
**kristina (at) hypergames.no**"*. Fonte: `https://www.hypergames.no/studio` (**200, 58.872 bytes**).
Os quatro artistas da casa (*Mads Frantzen*, *Marcus Kjeldsen*, *Rolf Hove*, *Adriane Brennmoen*)
aparecem **com nome e cargo e sem endereço**.
**ARMADILHA NOVA E BARATA DE CAIR: `https://www.hypergames.no/services` responde 200 com 42.247
bytes e o corpo imprime, em texto, `404 - Page not found`.** É a família do `vancouveranimation.ca`
(200 com `<title>` de site de aposta): **200 não prova página; leia o corpo.**

### `soja.se` (Soja, Estocolmo e Tjörn) — primeiro nome, com **`%20` e BOM colados no href**

`simon@` (Simon Österhof, *Producent*), `sofie@` (Sofie Edvardsson, *Creative Director*), **`jakob@`
(Jakob Nyström, *Animation Lead*)**, mais `hej@` e `jobb@` (funcionais). Fonte:
`https://soja.se/om-oss-produktionsbolag-animation` (**200, 92.896 bytes**; `/om-oss` redireciona
para lá). A página serve alguns endereços como **`%20simon@soja.se`** e **`%20sofie@soja.se`**, com
um **BOM `U+FEFF`** depois do telefone; **o local real é sem o `%20`**, e a entrega da carta de 17/09
para `sofie@soja.se` prova isso. A mesma página vaza `rosemarie.strand@folketsbio.se`, que é
**distribuidora parceira**, não da casa.

### `studiocan.nl` (Studio CAN, Roterdã) — primeiro nome, e a casa tem **SÓ DUAS pessoas**

`igor@` (Igor Duspara, *Owner and Creative Director*) e **`jonas@` (Jonas Ott, *Owner and Creative
Producer*)**, mais `info@`. Fonte: `https://www.studiocan.nl/about` (**200, 690.256 bytes**).
**O teto de dois toques esgota o organograma inteiro desta casa.** Site Wix: os
`@sentry.wixpress.com`, `@sentry-next.wixpress.com` e `@sentry.io` que a varredura pesca são
**telemetria**, e `user@domain.com` / `name@email.com` são **texto de validação de formulário**.

### `cocoa.fi` (Cocoa Mediaproductions Oy, Helsinque) — **primeiro nome para todos e `nome.sobrenome` SÓ no CEO**, confirmado na página

`niko.waaralinna@` (**Niko Waaralinna, *CEO / EP*** — a exceção), `lotti@` (Charlotte Molander, *EP*),
`eemeli@` (Eemeli Katajisto, *EP*), `ilona@` (Ilona Malinen, *EP*), `anton@` (Anton Molander,
rótulo *General inquiries*), `dermot@` (Dermot Gallagher, **CFX / HEAD OF STUDIO**), mais `info@`,
`jobs@` (*"Want to work with us?"*) e `casting@`. Fonte: `https://cocoa.fi/about/` (**200, 90.350
bytes**; o mesmo bloco em `/` — 200, 107.833 bytes — e em `/contact/` — 200, 61.386 bytes).
**Isto confirma, com a página na mão, a nota que o arquivo já trazia** (*"mesma mecânica da Cocoa,
onde a exceção era o CEO"*). A casa irmã é **Boutique Animation** (2D).

### `freefolk.com` (Freefolk, Londres e Nova York) — **treze pessoas, TODAS em `data-cfemail`, e nenhuma de arte**

Decodificadas de `https://freefolk.com/contact/` (**200, 23.628 bytes**, aberta em 19/09 às 08h35).
O padrão é **primeiro nome** e vira **`nome.sobrenome`** quando o primeiro nome colide:

| Endereço | Pessoa | Cargo |
|---|---|---|
| `fi@` | Fi Kilroe | *CEO / Executive Producer* |
| `paulw@` | Paul Wright | *Chief Operating Officer* |
| `vittorio@` | Vittorio Giannini | *Director of Business Development & Strategy* |
| `cheryl@` | Cheryl Payne | *Head Of Commercial Production* |
| `laura.ricketts@` | Laura Ricketts | *Executive Producer* |
| `charles@` | **Charles Gillett** | *Producer* |
| `jessica@` | Jessica Verner | *Producer* |
| `meg@` | Meg Guidon | *Film and Episodic Executive Producer* |
| `hannah.dakin@` | Hannah Dakin | *Senior Producer* |
| `regan.perry@` | Regan Perry | *Producer* |
| `robyn.guthrie@` | Robyn Guthrie | *Producer* |
| `megan.hindle@` | Megan Hindle | *VFX Coordinator* |
| `sean@` | Seán O'Keefe | *PR & Marketing Manager* |

Funcionais: `jobs.ldn@`, `production.ldn@`. **Treze cadeiras e nenhuma de arte** — sem VFX
Supervisor, sem Head of CG, sem Art Director. **Aviso de homônimo, para não disparar veto errado: o
`charles@freefolk.com` é Charles *Gillett*, e não tem relação com o Charles Ellison que a campanha
não contata.**

### `blinkink.co.uk` (Blinkink, Londres) — **cinco pessoas publicadas e VETO ESCRITO na mesma página**

`josef@` (Josef Byrne, *Executive Producer*), `ellie.goodwin@` (Ellie Goodwin, *Executive Producer*),
`shiara.miranda@` (Shiara Miranda, *New Business Lead*, e a página usa o mesmo endereço como caixa de
*New Project Enquiries*), **`alex.halley@` (Alex Halley, *Head of Production*)**; *Bart Yates*
(*Executive Producer / Founder*) aparece **sem endereço**. Mais `hello@` e
`HELLO@BLINKINDUSTRIES.TV` (a divisão irmã, **domínio diferente**). Fonte:
`https://www.blinkink.co.uk/about` (**200, 43.301 bytes**).
**A MESMA PÁGINA IMPRIME O VETO, e ele vale para os dois domínios:** *"**Unfortunately we do not
accept any unsolicited material and cannot return any unsolicited material sent to us. We do not
respond to individual submissions and anything which is sent to us will not be read and will instead
be burned.**"* **Casa com veto escrito a material não solicitado não recebe carta fria.** A página
publica ainda representantes de terceiros que **não são da casa**: `bryan@`/`millie@wearebueno.com`,
`gisela@`/`nata@hunkydoryus.com`, `rowley@rowleysamuel.com`, `tess@softcitizen.com`,
`alexa@freeagent.uk.com`.

### `ludocraft.com` (LudoCraft, Oulu) — **`nome.sobrenome@` sob RÓTULO DE FUNÇÃO, e o cargo não é publicado**

`tony.manninen@` vem rotulado *"**Business Proposals** | CEO Tony Manninen"* e
**`marja.kuipers@`** vem rotulado só *"**Career & Support**"* — **sem cargo, sem foto e sem
biografia; o nome dela existe apenas dentro do local part**. Fonte: `https://ludocraft.com/`
(**200, 141.716 bytes**; `/about` serve a MESMA página byte a byte). **Endereço de pessoa com rótulo
de função e sem cargo publicado não vira carta** — é a morte da Final Frontier e do Michael Diaz.

### `theflyingcolourcompany.com` (The Flying Colour Company, Carnaby Street, Londres) — **cargo publicado SEM nome**

`simon@` sob *"Managing Director"*, `leonie@` sob *"Head of Production"*, `micheline@` sob
*"VFX Producer"*, mais `tfcc.general@` sob *"Reception"*. Fonte:
`https://www.theflyingcolourcompany.com/contact` (**200, 31.318 bytes**). **A página publica o CARGO
e o PRIMEIRO NOME dentro do endereço, e não nomeia ninguém** — é o espelho exato da armadilha da
Engine House (nome sem endereço). **Cargo sem nome de pessoa é meio par, não par.**

### `helmet.no` (Helmet, **Trondheim** e não Oslo) — quatro em primeiro nome, e só UMA cadeira de arte

`alex@` (Alexander Somma, *VFX Supervisor, Creative Director*), `oystein@` (Øystein Moe, *Director,
Cinematographer*), `line@` (Line K. Johansen, *Director, Producer*), `stian@` (Stian Eriksen,
*Cinematographer, 1st AC*), mais `contact@`. Fonte: `https://helmet.no/contact` (**200, 130.828
bytes**). **Correção de arquivo:** o `pessoas.csv` registra a casa em *Oslo*; o `<title>` do site diz
*"Helmet | Film Production & Visual Effects Studio – **Trondheim**, Norway"*.

### `densisteskilling.no` (Den Siste Skilling, Bergen) — **o href tem o domínio ESCRITO ERRADO**

A `/` (**200, 32.011 bytes**) e a `/about-2/` (**200, 30.442 bytes**) publicam `post@densisteskilling.no`
**e** `post@den**i**ssteskilling.no` — o segundo é **erro de digitação da própria casa dentro do
`mailto`**. **Armadilha nova: endereço publicado pode trazer o domínio da casa errado**; confira o
domínio caractere por caractere contra o domínio do site.

### `truststudio.co.kr` e `kog.co.kr` (Coreia do Sul) — **`data-cfemail` protegendo caixa FUNCIONAL**

Decodificados nesta rodada: `truststudio@truststudio.co.kr` (fonte:
`https://truststudio.co.kr/contact/`, **200, 18.055 bytes**, e `/studio/`, **200, 18.690 bytes**) e
`KOG@KOG.CO.KR` (fonte: `https://www.kog.co.kr/`, **200, 481.049 bytes**, e `/en`, **200, 478.196
bytes**). **Os dois são o nome da empresa como local part, ou seja funcional** — a ofuscação
Cloudflare aqui não esconde pessoa nenhuma. **Decodificar `cfemail` é obrigatório, mas decodificar
não garante pessoa.**

### `knowledgehub.creativebc.com` — **a porta de Vancouver tranca SEMPRE no mesmo lugar**

Medido em 19/09 às 08h35, e agora com o mapa completo: `creativebc.com/bc-film-commission/in-production/`
(**200, 174.540 bytes**), `creativebc.com/bc-film-commission/production-credits/` (**200, 168.875
bytes**) e `creativebc.com/bc-film-commission/library-production-services/` (**200, 180.786 bytes**)
abrem e têm **ZERO endereço de e-mail**; `creativebc.com/motion-picture-contacts/` responde **404**.
Todas as listas de contato — *Motion Picture Contacts*, *Industry Contacts*, *Funding Recipients*,
*In Production* em tempo real — apontam para **`knowledgehub.creativebc.com`, um Salesforce
Experience Cloud que falha na verificação de TLS** (`unable to get local issuer certificate`) mesmo
com `--cacert /root/.ccr/ca-bundle.crt`. **Não existe caminho por creativebc sem resolver o
knowledgehub; pare de gastar rodada nele.** No mesmo pedaço de rodada, `animallogic.ca:443` devolveu
**`gateway answered 502 to CONNECT`** no proxy.

### Falsos positivos de varredura que valem uma linha cada

- **Squarespace e Wix**: `user@domain.com`, `name@email.com`, `email@example.com`, `you@company.com`
  são **texto de validação de formulário**; `@sentry.io`, `@sentry.wixpress.com`,
  `@sentry-next.wixpress.com` são **telemetria**. Nenhum é endereço de pessoa.
- **`GunHil_logo@2.png`** (em `https://gunhil.com/about/`, **200, 58.490 bytes**) casa com regex de
  e-mail e é **nome de arquivo de imagem retina**.
- **`gimpville.no` serve a MESMA casca de ~33.8 KB em nove caminhos diferentes** (`/about-us`,
  `/team`, `/people`, `/studio`, `/kontakt`, `/om-oss`, `/company`, `/en`), todos com 200 e só
  `jobs@`. **Casca repetida com 200 não é página de equipe.**
- **`afilm.dk/studio` e `/meet-the-team` devolvem `508 Resource Limit Is Reached`** (1.006 bytes) —
  hospedagem estourada, não ausência de página. Vale reabrir noutra hora.

---

## RODADA DAS 10h35 DE 19/09 — O JSON EMBUTIDO É MELHOR PROVA QUE O DOM, E SEIS PADRÕES NOVOS

### A REGRA DE MÉTODO, e ela substitui a leitura de DOM como primeira escolha

Em site feito com framework moderno (Next.js, Squarespace, Wix) o pareamento nome↔cargo↔email
**existe duas vezes na mesma página**: uma no HTML renderizado e outra num **JSON de dados
embutido**, geralmente num `<script>` de hidratação. **Prefira o JSON**, por uma razão que a
armadilha de 06h35 deixou clara: no DOM o nome, o cargo e o `href` são **três elementos vizinhos**,
e vizinhança é inferência; no JSON eles são **três campos do mesmo objeto**, e isso não pode
discordar. Prova medida hoje, na Brand New School:

```
{"contact_title":"Human Resources","people":[{"title":"Director of People / HR",
 "name":"Amanda Collazo","email":"amanda@brandnewschool.com","phone":null}]}
```

**Como achar:** procure no HTML cru por `"email":"`, `"name":"`, `data-name=`, `__NEXT_DATA__`,
`"people":[` e `"contact` antes de flatten do DOM. No Wix o mesmo bloco costuma vir **renderizado
mais de uma vez** — na CarpeDiem o organograma aparece **três vezes** no mesmo arquivo, o que dá
três leituras independentes da mesma adjacência e vale quase tanto quanto um JSON.

### `carpediemfilmtv.com` — **INICIAIS DO NOME, e este é o único padrão de iniciais com PROVA DE ENTREGA**

Fonte: `https://www.carpediemfilmtv.com/` (**200, 1.144.089 bytes**, aberta em 19/09 às 10h35;
site Wix de página única, e o `<title>` publica o endereço: *6630 Hutchison Street, Outremont, QC*).

| pessoa | cargo publicado | endereço | regra |
|---|---|---|---|
| Anouk L'heureux | Vice Présidente de la production et des opérations | `Al@` | iniciais, **A maiúsculo como publicado** |
| Sylvie Desrosiers | Vice-president finance | `sd@` | iniciais |
| July Katherine Bustos | Institutional Affairs Supervisor | `jkb@` | **três** iniciais |
| Sophie Roy | Director | `sr@` | iniciais |
| Benoit Godbout | Director / Artistic director | `bg@` | iniciais |

**Por que este padrão vale mais que os outros de iniciais:** o `bg@` ↔ *Benoit Godbout* foi lido
desta mesma estrutura em 11/09, virou carta e **a carta entregou**, com o cargo certo citado no
corpo e zero bounce. Ou seja o layout já está **validado por entrega**, não só por leitura.
**Ressalva que fica registrada:** `Al@`, de duas letras, é o mais frágil da série, e a página
publica três pessoas **sem** endereço (Gérard Porlon, Nicolas Proulx CPA, Vanessa Loubineau), o que
prova que o organograma da página não é a folha inteira.

### `heycarbon.com` — **DOMÍNIO MISTO, inicial+sobrenome E primeiro nome puro na MESMA página**

Fonte: `https://heycarbon.com/contact` (**200, 43.997 bytes**, aberta em 19/09 às 10h35).
`mmcmanus@` = **M**att **McManus** e `ldefelice@` = **L**auren **DeFelice** são inicial+sobrenome,
mas `gretchen@` = *Gretchen Praeger* é **primeiro nome puro**. **Não extrapole o formato de um
domínio misto**: aqui o `gretchen@` derrubaria qualquer endereço montado como `gpraeger@`.
O pareamento é ótimo porque o nome visível está **dentro da âncora do `href`**:
`<strong><a href="mailto:ldefelice@heycarbon.com">Lauren DeFelice</a></strong><br /> Executive Producer`.

### `timelessfilms.co.uk` — primeiro nome puro, e a equipe vive em `/about` porque `/contact` é 404

Fonte: `https://www.timelessfilms.co.uk/about` (**200, 30.617 bytes**). `ralph@` (Ralph Kamp,
Chairman & CEO), `rebecca@` (Rebecca Kamp, SVP Production & Marketing), `gareth@` (Gareth Kamp, SVP
Distribution & Production), `jon@` (Jon Clifford, Head of Technical & Post Production), `jade@`
(Jade Spinks, Contracts & Collections Manager). **`/contact` devolve 404 de 6.603 bytes** com
`<title>Not Found</title>`. O template é Bootstrap e traz **tripla** confirmação: `<h4>` com o nome,
`<h6>` com o cargo e, no botão do modal, `data-name="Jon Clifford" data-job="Head of Technical &amp;
Post P…" ` ao lado do `mailto:`. **Quando existir `data-name`, confira contra o `<h4>` e o `href`:**
é justamente o campo que discordou em dois domínios na rodada das 06h35.

### `frostfx.ee` e `take-five.be` — primeiro nome puro, cartão completo com telefone, e caminho fora do canônico

- **`frostfx.ee`** (fonte `https://frostfx.ee/`, **200, 42.023 bytes**): `heiki@` (Heiki Luts,
  Producer & Supervisor), `marko@` (Marko Post, Producer), `andres@` (Andres Kluge, Creative
  Supervisor), `martin@` (Martin Turu, Lead Compositor & 3D Generalist), `anton@` (Anton Shtolf,
  Compositor), `kalev@` (Kalev Mölder, VR & AR Specialist, Developer). A casa é **página única**:
  `/about`, `/contact`, `/team` e `/impressum` **não existem**. **Endereço sem cadeira, para o
  registro:** a mesma página imprime `will@frostfx.ee` sob o rótulo `Email:` **sem nome e sem
  cargo** — é a morte da LudoCraft e da Final Frontier, e não vale ficha.
- **`take-five.be`** (fonte `https://take-five.be/team`, **200, 583.255 bytes**): `gregory@`
  (Gregory Zalcman, Producer), `alon@` (Alon Knoll, Producer), `david@` (David Grançon, Producer /
  production manager), `eric@` (Eric Jaminet, Production Accountant). **`/contact` devolve 404 de
  2.206 bytes** e a equipe vive só em `/team`.

### `brandnewschool.com`, `mythstudio.co.uk`, `sarofsky.com` — três formatos, e o do meio é o que engana

- **`brandnewschool.com`**: **primeiro nome puro** (`zack@`, `devin@`, `garrett@`, `amanda@`,
  `gracie@`), **com uma exceção funcional**: a *Controller* Megan Schmidtlein é publicada como
  `accounting@`. **Rótulo de função no lugar do nome de uma pessoa nomeada** é um caso novo e vale
  a nota: o nome existe, o cargo existe, e o endereço é de setor.
- **`mythstudio.co.uk`**: **`nome.sobrenome@`** (`james.finlay@`, `izzy.hill@`), ao lado de
  `hello@` e `Jobs@` (com J maiúsculo, como a casa escreve). Fonte `https://mythstudio.co.uk/contact`
  (**200, 20.244 bytes**).
- **`sarofsky.com`**: **MISTO e com Cloudflare** — `erin@` (Erin Sarofsky, Founder, ECD) é primeiro
  nome puro, mas `joel.signer@` (Head of Production) e `rudy.downey@` (UK Representative) são
  `nome.sobrenome@`. Fonte `https://sarofsky.com/contact` (**200, 45.695 bytes**), tudo em
  `data-cfemail`, e o texto visível mostra `[email protected]` **ao lado** do endereço real, o que
  faz a página parecer ter dois endereços por pessoa quando tem um.

### `engine-house.co.uk` e `chasing-carrots.com` — endereço bom, cargo que não é cargo

- **`engine-house.co.uk`**: a `/contact` (**200, 128.729 bytes**) publica **um** endereço,
  `tash@engine-house.co.uk`, **sem nome ao lado**; a `/team` (**200, 136.492 bytes**) nomeia *Mike*,
  *Jason Robbins* e *Tash Price*, e o que ela imprime como cargo são **piadas**: *"The Guy Who Makes
  Everything Look Good"*, *"The Movement & Storytelling Expert"*, *"The Story & Strategy Powerhouse"*.
  Padrão: **primeiro nome puro** (`jason@`, `tash@`). **Cargo de piada não é cargo publicado.**
- **`chasing-carrots.com`**: o `/impressum` (**200, 60.514 bytes**) imprime *"Vertreten durch:
  Dominik Schneider, Patrick Wachowiak"* com `dominik@` e `patrick@` logo abaixo. Padrão **primeiro
  nome puro**, pareado por ordem. **`Vertreten durch` é rótulo jurídico de representante legal, não
  cargo** — serve para pareamento, não para ficha.
- **`gentletroll.com`**: a `/about` (**200, 25.515 bytes**) publica sob o rótulo *"Key personal"*
  `mw@` (Michel Wacker, Founder & CEO, **iniciais**) e `lena.schubert@` (Administration & PR,
  **nome.sobrenome**). **Domínio misto, e as duas pessoas são a casa inteira.**

### MEDIDO: CASA GRANDE NÃO PUBLICA PESSOA, E AGORA COM NÚMERO

Varredura de **23 caminhos por domínio** em 19/09 às 10h35, e o resultado é **zero endereço de
pessoa** nas seis casas grandes abertas. O que elas publicam é **rótulo de função**:

| casa | o que publica |
|---|---|
| `gurustudio.com` | `peopleandculture@`, `productionservices@`, `business.affairs@`, `questions@`, `marketing@`, `sales@` |
| `hybride.com` | `bidding@`, `communications@`, `info@`, `support@` |
| `dexterstudios.com` | `vfx@`, `immersive@`, `theeye@`, `pr@`, `dexterstudios@` |
| `nexusstudios.com` | `eps@`, `oc@`, `prmarketing@`, `info@`, `jobs@` |
| `aardman.com` | nenhum endereço em nenhum caminho (a `/contact/` serve a home, `<title>Home | Aardman`) |
| `macguff.fr` | `recrutement@` e já está **no teto de dois** |

**Guru Studio serve a MESMA casca de 62.105 bytes em nove caminhos diferentes** (`/about`, `/team`,
`/our-team`, `/people`, `/crew`, `/meet-the-team`, `/who-we-are`, `/impressum`, `/press`, `/om-oss`,
`/equipe`), todos 200 com `<title>Guru Studio` e só `questions@` dentro. **É a mesma assinatura do
`gimpville.no`: casca repetida com 200 não é página de equipe.** Só `/contact` e `/contacto`
(**38.208 bytes**) trazem a lista de setores.

### MEDIDO: O POOL DE "CASA TOCADA SÓ EM CAIXA FUNCIONAL" É POBRE EM GENTE

Cruzamento reproduzido em 19/09 às 10h35: **407 domínios** com `pessoas=0` e `toques=1`, isto é
casas em que a campanha escreveu para `info@`/`jobs@`/`careers@` e nunca achou uma pessoa.
Varri **200 deles** em cinco caminhos (`/`, `/contact`, `/about`, `/team`, `/impressum`), com
decodificação de `data-cfemail`, entidade HTML, ROT13, `data-enc-email` e `(at)`/`(dot)`, e o
universo inteiro devolveu **DOIS** endereços de pessoa novos: `michalis@cat-astrophe-games.com` e
`rick@gummycat.com`. **O motivo é circular e óbvio depois de escrito: se a casa publicasse uma
pessoa, a campanha já teria achado essa pessoa** — a caixa funcional foi usada justamente porque não
havia nome. **O pool que rende é o de casa com UMA pessoa já tocada** (`pessoas=1 toques=1`), e foi
ele que deu as seis fichas de 10h35. **Comece sempre por ele.**

Na mesma varredura, **58 domínios de animação inéditos** do `censo-wikidata.csv` (Nórdicos, Holanda,
Reino Unido, Alemanha, França, Coreia, Irlanda) deram **ZERO** endereço de pessoa em cinco caminhos:
o que sai é `info@`, `hello@`, `jobs@`, `sales@`, `contact@`, mais lixo de terceiros
(`dpo-google@google.com`, `privacy@calendly.com`, `dpo@brevo.com`, `hosting@gabia.com`,
`cloudsupport@blender.org`, `info@archive.org`, `exemple@monsite.com`, `info@domain-evo.com`).
**Estúdio pequeno de animação europeu quase nunca publica pessoa; o que publica é caixa.**

### Falha de ambiente nova

- **`gigglebug.fi` não passa verificação de TLS**, nem com `www`: `curl: (60) SSL: no alternative
  certificate subject name matches target host name 'gigglebug.fi'`. Entra na mesma lista do
  `knowledgehub.creativebc.com` e do `animallogic.ca`. **Não se desliga verificação de TLS** — esta
  casa só se caça por outra fonte.
- **`deck13.com/en/contact/` devolve 404** de 53.561 bytes **com `<title>404 Not Found | Deck13
  Interactive`**, e a página de 404 **contém `info[at]deck13.com` ofuscado**. É o caso exato da
  regra *"200 não prova fonte"* pelo avesso: **um 404 pode conter endereço, e um endereço achado num
  404 não prova que a casa o publica numa página viva.** Confira sempre o `<title>`.
