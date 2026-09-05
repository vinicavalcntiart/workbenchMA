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
