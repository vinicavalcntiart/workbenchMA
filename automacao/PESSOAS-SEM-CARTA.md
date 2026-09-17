# Pessoas achadas e verificadas, ESPERANDO CARTA

## ✅ DESTRAVADO EM 12/09 ÀS 11h30. SETE CARTAS ESCRITAS.

**O bloqueio caiu, e a causa não era a que este arquivo supunha.** A suposição registrada
abaixo é que `create_draft` estava travado para todo mundo. Não estava: **travava só para
AGENTE**. A chamada feita da sessão principal passa calada, e foi assim que as sete saíram.
A permissão do projeto lista `mcp__Gmail__create_draft` no `allow` desde 11/09, e mesmo assim
o subagente continua abrindo pedido de aprovação na tela do Vini — ou seja o `allow` do
projeto não alcança o subagente nesta sessão remota.

**A regra que fica, e ela é de divisão de trabalho, não de configuração:**
**agente NUNCA escreve carta. Agente acha e verifica; o maestro escreve.**

| Pessoa | Casa | Rascunho |
|---|---|---|
| Arno Schmitz | Guerrilla Games | criado |
| Eva Balvirčáková | MADFINGER Games | criado |
| Giles Sander | Polyester Studio | criado |
| Jake Fishman | Concept Art House | criado |
| Tim Remmers | Team Reptile | criado, e ele **assume a primeira carta de 06/09** em vez de fingir que é o primeiro contato |
| Curtis Andrus | Animal Logic | criado |
| *(caixa `jobs@`, não a pessoa)* | HundredStar Games | criado |

**As duas que continuam paradas, e por quê:** **Jan Philip Cramer** (Digital Domain) e
**Paweł Mielniczuk** (CD PROJEKT RED). Nos dois casos o endereço **não existe em fonte
pública** e o que havia era chute. Casa grande não se gasta em endereço montado, então elas
seguem valendo pelo nome, pelo cargo e pelo domínio provado, esperando endereço literal.

**Os rascunhos saem pelo Apps Script (`enviarRascunhos()`), nunca à mão pelo Gmail:** a API
embrulha todo link em `https://www.google.com/url?q=...` e só o `limparLinks` do
`automacao/envia-rascunhos.gs` desfaz isso na hora do envio. Conferido de novo hoje no
rascunho do Arno: os três links saíram embrulhados.

---


Criado na rodada das 06h35 de 12/09/2026 pelo Joe.

**Por que este arquivo existe:** na madrugada de 12/09 três agentes seguidos morreram
pendurados em `mcp__Gmail__create_draft`, que abre pedido de aprovação na tela do Vini e
não retorna enquanto ninguém clica. A regra desta rodada foi fazer só a metade cara do
trabalho — **achar e verificar** — e deixar a carta para um lote quando ele acordar.

**Como usar:** cada ficha abaixo tem tudo que a carta precisa. Abrir, escrever, mandar.
Quem escrever a carta deve marcar a ficha como feita e trocar o campo `rascunho` da linha
correspondente em `pessoas.csv` (hoje `PENDENTE-create_draft-bloqueado`) pelo ID do
rascunho.

---

### Eva Balvirčáková — Senior Recruiter — MADFINGER Games, Brno, Chéquia
- **Email:** ebalvircakova@madfingergames.com · confiança **alta** · fonte: https://madfingergames.com/careers (bloco de contato no fim da página, nome + cargo + endereço, lido nesta rodada)
- **Por que ELA e não outra pessoa:** casa de porte médio-grande (FPS AAA, Gray Zone Warfare) onde a própria página de carreiras nomeia só duas pessoas — ela, Senior Recruiter, e Monika Pavlišová, HR Lead — e convida explicitamente quem não achou vaga a escrever; a recrutadora sênior é a porta, não o filtro.
- **Gancho, com a frase do próprio estúdio entre aspas:** "Didn't find YOUR position? If needed, contact our team for more information." e, na mesma página, o benefício listado como **"relocation support — Extensive assistance with visa, work permits, and communication."** Esse segundo é o gancho de ouro: é o estúdio dizendo por escrito que trata visto e permissão de trabalho, que é exatamente o item de checklist que faz RH generalista descartar o Vini em cinco segundos.
- **Fora dos EUA?** Sim — Chéquia, União Europeia. A frase de realocação da carta pode citar de volta o "relocation support" deles.
- **Dedupe:** zero ocorrência de "madfinger" em `pessoas.csv`, `enviados.csv`, `automacao/processados.csv` e `docs/index.html`. **E o Gmail confirma**: `search_threads` por "madfinger" devolve zero, então a casa é de fato inédita e não só ausente do arquivo. PRIMEIRA pessoa desta casa. Monika Pavlišová (mpavlisova@madfingergames.com, HR Lead) fica como SEGUNDA e última possível.
- **Ressalva honesta:** as vagas abertas hoje são AI Programmer, Lead Technical Artist e Senior Level Designer — nenhuma de personagem. A carta é de porta, não de vaga.

---

### Tim Remmers — Cofundador (contato publicado de imprensa e negócios) — Team Reptile, Enschede, Holanda
- **Email:** tim@team-reptile.com · confiança **alta** · fonte: https://team-reptile.com/presskit/ ("Press/Business contact tim@team-reptile.com", lido nesta rodada)
- **Por que ELE e não outra pessoa:** casa de menos de 30 pessoas, onde o BRIEF-JOE manda ir no fundador; dos dois fundadores (Dion Koster e Tim Remmers), só o Tim tem endereço publicado. Não existe recrutador nem RH nessa casa — quem lê é quem faz.
- **Gancho, com a frase do próprio estúdio entre aspas:** o presskit diz que **"Team Reptile is a venture in cold blood started by Dion Koster and Tim Remmers in 2011"** e que **"Team Reptile will keep creating more cyberfunk style games in the future."** O encaixe é direto: Bomb Rush Cyberfunk vive de personagem 3D estilizado — elenco, roupas, silhueta — e "mais jogos no estilo cyberfunk" é exatamente mais elenco para modelar.
- **Fora dos EUA?** Sim — Holanda, União Europeia.
- **Dedupe, e ele foi CORRIGIDO dentro desta própria rodada:** os quatro arquivos de campanha (`pessoas.csv`, `enviados.csv`, `automacao/processados.csv`, `docs/index.html`) davam **zero** para "team reptile". A caixa de entrada não: em **06/09 saiu uma carta fria para `contact@team-reptile.com`**, caixa genérica, **sem resposta até hoje**. Arquivo não é log — foi o Gmail que provou, exatamente como o `dedupe-agora.sh` avisa. Então esta é a **SEGUNDA e ÚLTIMA** aproximação desta casa, seis dias depois da primeira, agora para uma pessoa com nome em vez de caixa genérica. O teto de duas fecha aqui: Dion Koster já não cabe.
- **Ressalva honesta:** https://team-reptile.com/jobs/ diz "We currently don't have any open vacancies" — carta de porta, não de vaga. O endereço do Tim é rotulado como contato de imprensa/negócios, então a carta tem que se apresentar rápido e não parecer press release. **E a carta precisa saber que já houve uma primeira**: não pode chegar como se fosse o primeiro contato; o tom certo é o de quem escreveu para a caixa geral, não teve resposta, e agora procura a pessoa certa.

---

### Giles Sander — Producer — Polyester Studio, Toronto, Canadá (e Nova York)
- **Email:** giles@polyesterstudio.com · confiança **alta** · fonte: https://polyesterstudio.com/say-hello/ ("Producer Giles Sander — Email: giles@polyesterstudio.com", nome, cargo e endereço na mesma linha; lido nesta rodada)
- **Por que ELE e não outra pessoa:** é a única pessoa que o estúdio publica, e a página existe exatamente para receber quem quer trabalhar com eles. Casa pequena de produção sob demanda: produtor é quem lê e quem distribui trabalho.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"LEAD WITH CHARACTERS"** e, logo abaixo, **"Polyester is the imagination studio that crafts unforgettable characters for the world's most memorable brands."** A própria página Say Hello convida com **"Let's characterize your world; Giles would be happy to help."** O portfólio deles é etiquetado "3D characters" (peças: Character Anthem, 2026 Canadian Census, DoorDash). Não existe encaixe mais literal para um Senior 3D Character Artist do que um estúdio cujo produto É personagem.
- **Fora dos EUA?** Sim — Canadá (Toronto), com presença em Nova York. Canadá é o país de maior prioridade do BRIEF-JOE, e a carta deve dizer de frente que ele precisa de patrocínio de visto, porque é o item que o RH usa para cortar e o estúdio de personagem é quem atropela.
- **Dedupe:** zero ocorrência de "polyester" em `pessoas.csv`, `enviados.csv`, `automacao/processados.csv` e `docs/index.html`, **e zero também no Gmail** (`search_threads` por "Polyester Studio" e "polyesterstudio"). PRIMEIRA pessoa desta casa.
- **Ressalva honesta:** o cargo é produção, não direção de arte; e o estúdio é de publicidade/branded content com personagem, não de jogo ou longa.

---

- **ROTA MEDIDA EM 12/09 às 07h20 (pelo maestro, não pelo Joe):** a casa **não tem formulário de candidatura**. O único `<form>` do site inteiro é inscrição de newsletter do Mailchimp (`list-manage.com/subscribe/post`), que NÃO é candidatura e não deve ser usada como tal. A página `/careers/` não lista vaga nenhuma: traz só o endereço de Toronto (145 Augusta Ave.), o telefone e o mesmo `giles@polyesterstudio.com`. Portanto **a rota é carta para pessoa com nome, e só**. Zero sinal de captcha em qualquer página.
- **Reforço de gancho, medido na navegação do site:** o menu de primeiro nível deles é `Work. Characters. Culture.` — **"Characters" é seção própria do site**, não subcategoria de portfólio. Vale citar isso na carta junto com o "LEAD WITH CHARACTERS" da home.

### Jake Fishman — Director of Business Operations — Concept Art House (CAH), San Francisco, EUA (com Xangai e Chengdu)
- **Email:** jake.fishman@conceptarthouse.com · confiança **alta** · fonte: https://conceptarthouse.com/contact ("Have a project in mind? Reach out to discuss it! jake.fishman@conceptarthouse.com", lido nesta rodada). Cargo em https://theorg.com/org/concept-art-house/org-chart/jake-fishman — fonte de terceiro, e a carta não deve citar o cargo como se ele o tivesse publicado.
- **Por que ELE e não outra pessoa:** é a única pessoa com nome que a casa publica, e numa casa de terceirização é ele quem decide para quem o trabalho vai. Não existe RH generalista no meio.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Since 2007, Concept Art House has been the trusted art outsourcing partner for top game developers, including Activision | Blizzard, Epic Games, Roblox, and NCSoft. We specialize in AAA and mobile game art, crafting high-quality character designs, 2D & 3D assets, animation, and VFX that bring game worlds to life."** Personagem é o produto da casa, não um detalhe dela.
- **Fora dos EUA?** NÃO — sede em San Francisco. **Mas isto aqui inverte a frase de realocação em vez de piorá-la:** CAH é casa de terceirização, contrata artista por projeto e a distância. A carta deve pedir trabalho remoto por projeto, não vaga com visto, e dizer isso na primeira linha. É a única ficha desta rodada em que o problema do patrocínio simplesmente não se aplica.
- **Dedupe:** zero ocorrência de "concept art house"/"conceptarthouse" em `pessoas.csv`, `enviados.csv`, `automacao/processados.csv` e `docs/index.html`, **e zero também no Gmail**. PRIMEIRA pessoa desta casa.
- **Ressalva honesta:** a página de contato é comercial ("tem um projeto em mente?"), então a carta chega numa caixa de clientes e não de candidatos. Tem que se identificar como artista nas duas primeiras linhas.

---

### ~~Joost van Dongen — Galaxy Grove~~ — **DESCARTADA NESTA RODADA, NÃO ESCREVER**
Ela chegou a entrar no `pessoas.csv` e foi **removida na mesma rodada**. Fica registrada aqui como
aviso, porque o erro é repetível.

O email `joost@galaxy-grove.com` está publicado na home do estúdio e os quatro arquivos de campanha
davam zero para "galaxy grove". Só que a **caixa de entrada** conta outra história: **em 06/09 o Vini
já escreveu para esse mesmo endereço**, e em **07/09 a casa respondeu recusando** (resposta de
`jobs@galaxy-grove.com`: *"Recently you reached out to us regarding a possible position as a 3D artist
at Galaxy Grove. While you have an impressive skill set, we are afraid we have to disappoint you..."*).
O Vini ainda respondeu à mão agradecendo. **Estúdio que já recusou e pessoa que já respondeu estão
duplamente fora dos limites da campanha.**

**A lição, e ela custou duas fichas desta rodada:** dedupe só por `grep` nos arquivos do repositório
**não basta**. A prova de que uma casa é nova é a **caixa**, não o arquivo — é o que o
`automacao/dedupe-agora.sh` já dizia por escrito e o que esta rodada mediu de novo. Rodar
`mcp__Gmail__search_threads` com o nome e o domínio da casa **antes** de escrever a ficha, sempre.


---

### Paul Widelski — artista de personagem (título exato não publicado) — HundredStar Games, Londres, Reino Unido
- **Email:** **NÃO EXISTE endereço de pessoa publicado** · confiança **sem-email** · fonte da pessoa: https://uk.linkedin.com/in/paul-widelski-6152984a (perfil público, lido nesta rodada sem login); fonte do estúdio: https://www.hundredstar.games/
- **Por que ELE e não outra pessoa:** casa AAA de 100 pessoas que não publica um único nome; ele é a única pessoa de personagem identificável, e foi ele quem divulgou publicamente a vaga "Expert/Principal Character Artist" da casa.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de vagas diz, com estas palavras, **"While we may not currently be advertising for the kind of position you feel best aligns to your skillset, we'd welcome you to speculatively apply by sharing your CV and portfolio with our Recruitment team via jobs@hundredstar.games for future consideration should a role become available."** É convite escrito a candidatura espontânea. A home diz só **"AAA games, 100 people in london"**.
- **Fora dos EUA?** Sim — Reino Unido. Continua precisando de patrocínio (UK exige), então a frase de realocação vale inteira.
- **Dedupe:** "hundredstar" não aparece em `enviados.csv`, `pessoas.csv` nem `docs/index.html`, e o Gmail também devolve zero; aparece uma vez em `automacao/processados.csv`, e é justamente a nota do agente que morreu na madrugada de 12/09 deixando esta casa pendente. PRIMEIRA pessoa desta casa.
- **O QUE FALTA, e é o que trava a carta para a pessoa:** o site publica só `info@hundredstar.games` e `jobs@hundredstar.games`. Não há nenhum endereço de pessoa em fonte pública gratuita; o único lugar que oferece um é serviço pago de busca de email, que o BRIEF-JOE proíbe. **Nada foi montado nem inventado.** Enquanto não aparecer endereço literal, a carta possível é para `jobs@hundredstar.games`, e ela tem chance real porque a própria casa pediu candidatura espontânea — quem escrever decide se manda assim ou se guarda.

---

## RODADA DAS 09h35 DE 12/09 — CASA GRANDE POR RODAPÉ DE PAPER

**Caminho novo, e ele funciona.** A rodada das 05h35 já tinha registrado em `processados.csv`
que "os PDFs desses talks ficam atrás do paywall da ACM". Isso é verdade para `dl.acm.org`
(medido de novo hoje: **403 Forbidden**, com e sem navegador falso). Mas **não é verdade para as
cópias abertas**: `history.siggraph.org` hospeda centenas de PDFs de Talks do SIGGRAPH sem
paywall, e vários estúdios hospedam o próprio PDF no próprio domínio. **O rodapé desses PDFs traz
nome, afiliação, cidade e email institucional**, ou seja, endereço PUBLICADO — não montado.
Medido nesta rodada em três PDFs diferentes, todos abriram e todos tinham email.

---

### Curtis Andrus — Groom artist (título exato não publicado pelo estúdio) — Animal Logic / Netflix Animation Studios, Vancouver, Canadá
- **Email:** curtis.andrus@animallogic.ca · confiança **alta** · fonte: rodapé da primeira página de **"Improving Groom Interactivity in Houdini"**, DigiPro 2022 (DOI 10.1145/3543664.3543678), **PDF hospedado pelo próprio estúdio**: https://animallogic.com/wp-content/uploads/2023/06/Improving-Groom-Interactivity-in-Houdini.pdf — bloco de autores lido literalmente nesta rodada: *"Curtis Andrus — curtis.andrus@animallogic.ca — Animal Logic — Vancouver, BC, Canada"*. A publicação também está listada na página pública de publicações da casa: https://animallogic.com/technology/publications/improving-groom-interactivity-houdini/
- **Por que ELE:** groom é a disciplina colada em personagem, e ele não é um nome solto — é o autor do sistema de grooming da casa e **o mesmo Andrus de "Furtility: Robust Hair Styling"** (SIGGRAPH 2015, feito na MPC). É especialista de cabelo e pelo de carreira, dentro de uma casa que não publica um único email de contato.
- **Gancho, com a frase do próprio paper entre aspas:** **"To improve performance and interactivity working with our Houdini-based Grooming Tools, Animal Logic developed a set of custom nodes to control and optimize the process of evaluating our groom generation networks."** A carta deve falar de personagem e de groom como quem entende a cadeia modelagem → groom → look dev, não como quem viu a palavra no site.
- **Fora dos EUA?** Sim — Vancouver, Canadá. **Canadá é o país de maior prioridade do BRIEF-JOE**, e a carta deve dizer de frente que ele precisa de patrocínio.
- **Dedupe:** "animal logic" só aparece em `pessoas.csv` como `Netflix Animation / Animal Logic` (Bradley Sick, `bsick@netflix.com`, **BOUNCE em 06/09**); zero em `enviados.csv`; **e o Gmail devolveu ZERO** para `{"animal logic" animallogic al.com.au "Curtis Andrus"}`. Esta é a **SEGUNDA e ÚLTIMA** pessoa desta casa.
- **Ressalva honesta, e ela é grande:** o paper é de **2022**, e em **janeiro de 2024** a Animal Logic foi integrada à Netflix Animation Studios. O endereço é **publicado, não montado** — mas a vigência do domínio `animallogic.ca` não foi confirmada nesta rodada, e o `bsick@netflix.com` do Bradley Sick já bounceou, o que mostra que a migração de domínio dessa casa é terreno movediço. Se bouncear, **a via alternativa da MESMA casa já está medida**: `beau.parkes@al.com.au` (Beau Parkes, Animal Logic Sydney, no mesmo rodapé do mesmo paper). Ela **não abre carta própria** — o teto de duas fecha no Curtis.

---

### Jan Philip (Phil) Cramer — Visual Effects Supervisor (ex-Head of Animation) — Digital Domain, Los Angeles / Playa Vista, EUA
- **Email:** **não publicado.** `jcramer@d2.com` é **MONTADO** · confiança **baixa** · o que está publicado é o **domínio**: `d2.com`, provado por **três endereços literais** no rodapé do PDF aberto do talk *"Simplified facial capture with head mounted cameras"* — https://history.siggraph.org/wp-content/uploads/2022/06/2021-Talks-Serra_Simplified-facial-capture-with-head-mounted-cameras.pdf — `jserra@d2.com` (Jose Serra), `lmoser@d2.com` (Lucio Moser), `dmclean@d2.com` (David Mclean), todos no formato inicial+sobrenome. **Fontes da pessoa (essas sim publicadas):** https://digitaldomain.com/leadership/jan-philip-cramer/ e https://digitaldomain.com/news/the-fantastic-four-first-steps-jan-philip-cramer-vfx-supervisor-digital-domain/
- **Por que ELE:** é literalmente o homem de personagem da casa. A bio oficial dele diz que **"As Head of Animation, he revolutionized the studio's approach to photorealistic creatures and facial animation"** e que **"His vision was instrumental in bringing 'Thanos' to life in Avengers: Infinity War."** O resumo oficial do talk dele no SIGGRAPH 2023 ("She Hulk: Lawyer to Fashion Icon") diz que ele ia discutir **"the creation of the main character, motion studies, and the final shot work"** — She-Hulk é personagem integral em CG. Não é RH, não é produção, não é ambiente: é quem decide como a criatura fica.
- **Gancho:** as duas frases acima. Criatura fotorreal e personagem integral em CG são exatamente o centro do portfólio do Vini, e a casa segue nisso — a própria Digital Domain publicou em 2025 o material dele em *The Fantastic Four: First Steps* e ele está em *Godzilla x Kong: Supernova*.
- **Fora dos EUA?** **Não** — sede em Los Angeles. Mas a casa tem escritórios em **Vancouver e Montreal**, e a carta pode pedir explicitamente a unidade canadense, que é o país de maior prioridade do BRIEF-JOE.
- **Dedupe:** "digital domain" aparece **uma** vez em `pessoas.csv` (Kasita Wonowidjojo, Senior Texture Painter, `sem-email`, 05/09), **zero** em `enviados.csv`, **e o Gmail devolveu zero** para `{digitaldomain "digital domain" d2.com Cramer guerrilla}`. Esta é a **SEGUNDA e ÚLTIMA** pessoa desta casa.
- **O QUE TRAVA, e está dito sem maquiagem:** o endereço **dele** não existe em fonte pública. `jcramer@d2.com` é chute, e **chute duplo**, porque o primeiro nome é composto — `jpcramer@d2.com` é igualmente provável. O BRIEF-JOE proíbe gastar a carta de uma casa grande num endereço montado, então **esta ficha vale pelo nome, pelo cargo e pelo domínio provado**, e quem escrever decide: ou arrisca o montado sabendo do risco, ou escreve para `lmoser@d2.com`, que é **publicado** mas é P&D de humano digital, não decisão de arte de personagem.

---

### Arno Schmitz — **Lead Character Artist** — Guerrilla Games (PlayStation Studios), Amsterdã, Holanda
- **Email:** info@arnoschmitz.com · confiança **alta** · fonte: **site pessoal dele**, https://www.arnoschmitz.com/about/ — página aberta e lida nesta rodada, onde ele se apresenta como **"Lead Character Artist"** na **"Guerrilla Games"** e publica o endereço como contato. Cargo confirmado pela própria casa em https://www.guerrilla-games.com/read/creating-the-many-faces-of-horizon-forbidden-west
- **Por que ELE:** é o alvo mais literal que a campanha inteira já achou — **lead de arte de personagem numa casa AAA cujo produto é personagem**. Não é recrutador, não é produtor, não é ambiente. É a pessoa que decide como o personagem fica, dentro de um estúdio que **não publica o email de ninguém**.
- **Gancho, com a frase da própria casa entre aspas:** **"Arno Schmitz is the Lead Character Artist at Guerrilla."** Os créditos que a casa lista para ele: **Killzone Shadow Fall, Horizon Zero Dawn e The Frozen Wilds, Horizon Forbidden West e a DLC Burning Shores.** A carta deve ir direto ao ofício — silhueta, elenco, roupa, groom — e falar de artista para artista, porque é isso que chega numa caixa pessoal.
- **Fora dos EUA?** Sim — Holanda, União Europeia. A frase de patrocínio de visto vale inteira.
- **Dedupe:** **zero** ocorrência de "guerrilla" em `pessoas.csv` e em `enviados.csv`; em `automacao/processados.csv` só há duas notas de varredura de ATS (03/09 e 06/09), **nenhuma carta e nenhuma pessoa**; e o **Gmail devolveu zero** para Guerrilla. **PRIMEIRA** pessoa desta casa — sobra uma.
- **Ressalva honesta, duas:** (1) o endereço é **caixa pessoal**, não corporativa — nesta campanha isso é vantagem, porque a Guerrilla não publica endereço de pessoa nenhuma, mas a carta tem que se comportar como carta a um artista, não como candidatura a RH. (2) O domínio `guerrilla-games.com` **estourou o tempo três vezes** nesta rodada (duas por WebFetch, uma por curl) — a frase da casa veio do índice de busca daquela página, **não** da página aberta por mim. O site pessoal, esse sim, abriu e foi lido inteiro. Fica registrado: **guerrilla-games.com entra na lista de fontes travadas.**

---

### Paweł Mielniczuk — Art Director de personagem (ex-Lead Character Artist) — CD PROJEKT RED, Varsóvia, Polônia
- **Email:** **não publicado** · confiança **sem-email** · fonte primária lida nesta rodada: sala de imprensa da própria CDPR, https://press.cdprojektred.com/en/news/1654/promised-land-art-festival-reaches-new-heights-in-2024
- **Por que ELE:** entrou no departamento de arte da CD PROJEKT RED em **2006**, virou **Lead Character Artist em 2010**, trabalhou nos três Witcher e, em **Cyberpunk 2077**, supervisionou todo o processo de arte de *Phantom Liberty* e **dirigiu os departamentos de personagem, armas e veículos** do jogo base. Hoje aparece como Art Director do *Project Hadar*. É a definição de "quem decide arte de personagem numa casa grande".
- **Gancho, com a frase dele entre aspas:** **"Promised Land is all about making the impossible possible, and creating this year's event really felt like the embodiment of that thought."** — dita como **"Festival Director of Promised Land Art Festival"**, o festival de arte que a própria CDPR organiza com a cidade de Łódź. É um homem que passa o ano chamando artista para dentro; a carta certa fala com o organizador de festival de arte, não com um RH.
- **Fora dos EUA?** Sim — Polônia, União Europeia.
- **Dedupe:** **zero** ocorrência de "cd projekt"/"cdprojekt" em `pessoas.csv`, `enviados.csv` e `automacao/processados.csv`, **e zero no Gmail**. **PRIMEIRA** pessoa desta casa.
- **O QUE FALTA, sem maquiagem:** a CD PROJEKT RED **não publica o endereço de pessoa nenhuma**, o formato de `cdprojektred.com` não está provado por nenhum endereço real, o ArtStation dele (`artstation.com/blooddragon`) está atrás do Cloudflare 403 e o único lugar que oferece um endereço é agregador pago, proibido pelo BRIEF-JOE. **Nada foi montado.** E mais uma ressalva de fonte: o cargo de arte veio do artigo da própria CDPR *"Promised Land Art Festival 2023 — Interview with Art Director Paweł Mielniczuk"*, que está hospedado no LinkedIn — que devolve **999** para esta campanha —, então ele foi lido pelo **índice de busca**, não pela página aberta. O que eu abri e li foi a sala de imprensa da CDPR.

---

### ~~Alena Dubrovina — Art Director, Larian Studios~~ — **DESCARTADA NESTA RODADA, NÃO ESCREVER**
Ela é o alvo perfeito no papel: entrou na Larian em 2016 como estagiária, subiu a Character Designer,
depois **Lead Character Designer** e hoje é **Art Director** de *Baldur's Gate 3*. A ficha chegou a
ser montada.

**O Gmail matou.** `mcp__Gmail__search_threads` por `{larian "cd projekt" cdprojektred Dubrovina Mielniczuk}`
devolveu **duas** threads da Larian: em **07/09** o Vini aplicou para *Character Artist – Open Application*
pelo Lever, e em **08/09** o time de recrutamento respondeu, com estas palavras:
*"Thanks for registering your details in our open application... **While we may not have a role that suits
your profile right now**, we will keep your details and share them with the relevant teams to see if there
is a need in future."*

**Casa que já respondeu está fora dos limites da campanha.** É o mesmo erro da Galaxy Grove, evitado
desta vez **antes** de virar linha no `pessoas.csv` — e evitado outra vez pela caixa, não pelo arquivo.

---

## RODADA DAS 12h50 DE 12/09 — JOE. AGENTE NÃO ESCREVE CARTA (regra das 11h35). FICHAS SÓ.

**Caminho da rodada, e ele repete o do Arno Schmitz:** casa grande não publica email de pessoa
nenhuma, mas o **lead de personagem dela tem site pessoal** e publica o endereço lá. O caminho é:
achar o NOME do lead de personagem por imprensa/entrevista, e depois procurar o site pessoal dele.

### Beatrice Harty — **Lead Character Artist** — IO Interactive (IOI), Malmö, Suécia
- **Email:** contact@beaharty.com · confiança **alta** · fonte: **site pessoal dela**,
  https://www.beaharty.com/about — página aberta e lida nesta rodada, que termina com
  **"Get in touch: contact@beaharty.com"**.
- **Por que ELA e não outra pessoa da casa:** é a **lead de arte de personagem** de uma casa AAA
  (Hitman, 007 First Light, Project Fantasy) que **não publica o email de ninguém** — o site inteiro
  só oferece `ioi@ioi.dk`, e essa caixa já respondeu ao Vini com resposta automática. Não é
  recrutador, não é produção, não é ambiente: é quem decide como o personagem fica. A própria
  página dela conta a carreira: Game Art na The Game Assembly (2015), estágio e depois emprego na
  **Massive Entertainment – A Ubisoft Studio** até 2021 (The Division, The Division 2, Avatar:
  Frontiers of Pandora), 2021–2022 com a Shapefarm e com o time da **A44** na Nova Zelândia, e
  desde agosto de 2022 na IOI: *"working as a Lead Character Artist in our Malmö studio"*.
- **Gancho, com a frase do próprio estúdio entre aspas:** https://www.ioi.dk/about diz
  **"IOI's ambition has always been to create immersive, system-driven worlds filled with beautiful
  art and innovative design"**, e https://www.ioi.dk/careers publica, no fim da página,
  **"Did you not find the job you were looking for? Unsolicited applications"** — a casa convida
  candidatura espontânea por escrito. Como a carta vai para a caixa PESSOAL dela, o tom certo é de
  artista para artista (silhueta, elenco, roupa, groom), não de candidatura a RH.
- **Fora dos EUA?** Sim — Suécia (Malmö), sede dinamarquesa, União Europeia. A frase de realocação e
  a de patrocínio entram inteiras.
- **Dedupe, e o Gmail mudou a leitura:** `pessoas.csv` e `enviados.csv` dão **zero** para
  "io interactive"; a **caixa não**. Em **06/09** saiu carta fria para `ioi@ioi.dk`, caixa genérica,
  que devolveu **só resposta automática** (*"we cannot reply to all emails that are sent to this
  address"*), e no mesmo dia entrou um painel de candidato do Teamtailor da IOI (relay
  `kasper-raaby-abrahamsen@ioi.teamtailor-mail.com`, que é o nome do recrutador da casa).
  **Nenhum humano respondeu e a casa não recusou.** Esta é a **SEGUNDA e ÚLTIMA** aproximação
  da casa, seis dias depois da primeira, agora para pessoa com nome. A carta **precisa saber que
  já houve uma primeira** e não chegar como se fosse o primeiro contato.
- **Ressalva honesta:** (1) o endereço é caixa **pessoal**, então ela pode ler devagar e a carta não
  pode parecer spam de recrutamento; (2) o site pessoal dela não diz a data da última atualização, e
  a confirmação de que ela segue na IOI vem do texto dela mesma, não de página da casa; (3) o Vini já
  está no banco de candidatos do Teamtailor da IOI desde 06/09, o que é bom (mostra interesse) e ruim
  (ela pode responder "aplica pelo portal") — a carta deve pedir **direção**, não vaga.

### François Lord — CG Supervisor (autor do pipeline de criaturas em USD) — Rodeo FX, Montréal, Canadá
- **Email:** flord@rodeofx.com · confiança **alta** (publicado, **mas leia a ressalva**) · fonte: rodapé
  do PDF aberto de **"Case study on using a parallel pipeline and USD to build creatures"**,
  SIGGRAPH 2020 Talks —
  https://history.siggraph.org/wp-content/uploads/2022/08/2020-Talks-Lord_Case-study-on-using-a-parallel-pipeline-and-USD-to-build.pdf
  — bloco de autor lido literalmente: *"François Lord — Rodeo FX Inc, Montreal, Quebec, Canada —
  flord@rodeofx.com"*.
- **Por que ELE:** o talk inteiro é de **criatura** (*"a photorealistic CG dromedary, one of the main
  stars"*), e ele é o supervisor de CG que montou o caminho por onde a criatura passa. Numa casa que
  publica só `info@`, ele é a única pessoa do lado de personagem com endereço literal em fonte aberta.
- **Gancho, com a frase do próprio estúdio entre aspas** (a página só renderiza com JavaScript; foi
  aberta com navegador nesta rodada): https://rodeofx.com/about diz **"WE ARE BORN TO CRAFT"**, define
  a casa como **"INDEPENDENT, ARTIST-DRIVEN & BORN IN QUEBEC"**, e cita o fundador Sébastien Moreau:
  **"Rodeo was founded by artists and has always put people at the centre of everything we do...this
  guarantees that our work, our creations, are always the very best they can be."**
- **Fora dos EUA?** Sim — Canadá (Montréal), o país de maior prioridade do BRIEF-JOE. A carta diz de
  frente que ele precisa de patrocínio.
- **Dedupe:** `pessoas.csv` tem **uma** linha de Rodeo FX (Deak Ferrand, Head of Art Department,
  `dferrand@rodeofx.com`, 06/09) e o **Gmail prova que aquela carta quicou no mesmo dia**
  (`mailer-daemon`, *"550 5.1.1 the email account that you tried to reach does not exist"*). Nenhuma
  recusa da casa, nenhuma resposta humana. Esta é a **SEGUNDA e ÚLTIMA** pessoa desta casa.
- **Ressalva honesta, e é grande:** (1) o endereço é **publicado, mas de 2020**; (2) **outro endereço
  do mesmo domínio já quicou** seis dias atrás, o que mostra que a casa desativa caixa de quem sai;
  (3) a página de liderança de hoje lista quinze executivos e **ele não está entre eles**, e os
  créditos públicos dele na Rodeo (Jumanji 2017 e 2019) são antigos — ele pode ter saído. Se quicar,
  o que sobra desta casa é `info@rodeofx.com`, genérico. **Nota de estrutura que a carta deve saber:**
  a própria página About declara **MIKROS ANIMATION** e **ALCHEMY 24** como divisões da Rodeo FX, e a
  confirmação de candidatura da Mikros de 01/09 chegou de `notification@rodeofx.com` — ou seja, o
  grupo já recebeu uma candidatura do Vini.

---

### Michael Skyers — **Principal Character Artist (Warframe)** — Digital Extremes, London (Ontario), Canadá
- **Email:** **não existe em fonte pública gratuita** · confiança **sem-email** · fonte da pessoa e do
  cargo: https://80.lv/author/michael-skyers — página aberta e lida nesta rodada, que apresenta a
  entrevista de **26/03/2026** com esta frase literal: **"Principal Character Artist at Digital
  Extremes, Michael Skyers, discusses designing the latest frame, Follie, evolving silhouettes, and
  building characters for a long-running live-service game."**
- **Por que ELE:** é o artista de personagem **principal** do Warframe, dentro de uma casa AAA
  canadense de ~400 pessoas. Personagem puro: não é recrutador, não é produção, não é ambiente.
- **Fora dos EUA?** Sim — **Canadá**, o país de maior prioridade da campanha.
- **O QUE TRAVA, sem maquiagem:** `digitalextremes.com` **não publica endereço de pessoa nenhuma** —
  a varredura de `/contact`, `/about`, `/team`, `/careers` e `/jobs` desta rodada devolveu **zero**
  email, nem genérico. Os únicos lugares que oferecem endereço dele são **agregadores pagos**
  (ZoomInfo e RocketReach, que mostram só `m***@digitalextremes.com`), proibidos pelo BRIEF-JOE.
  **Nada foi montado.** ArtStation dele está na lista de fontes travadas e o LinkedIn devolve 999.
- **Armadilha evitada e registrada, porque é repetível:** `skyerzz.com` existe e responde 200 — e é de
  **outra pessoa**, um site de mods de Minecraft. Domínio que "parece" o apelido do artista não é
  fonte; foi aberto e conferido antes de virar linha.
- **Dedupe:** zero ocorrência de "digital extremes" em `pessoas.csv` e `enviados.csv`; o **Gmail**
  mostra só recibo automático de candidatura de 06/09 (`no-reply@digitalextremes.com`, vaga de Concept
  Artist) e um código de segurança do Greenhouse. **Nenhuma recusa, nenhuma resposta humana.**
  PRIMEIRA pessoa desta casa.
- **Gancho já pronto para o dia em que aparecer endereço:** a entrevista dele é sobre **silhueta** e
  construção de personagem para jogo-serviço de longa duração, que é o vocabulário do portfólio do Vini.

---

## RODADA DAS 15h40 DE 12/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Caminho novo da rodada, e ele é repetível e barato:** varrer os **slugs de Teamtailor que a
campanha já conhece** seguindo o redirecionamento **para o domínio próprio da casa** e procurar
`mailto:` de pessoa dentro da página de cada vaga. O campo `recruiter-email` do payload (veia de
07/09) apareceu em **zero** dos 78 slugs — mas o `mailto:` no corpo do anúncio apareceu, e é a
mesma coisa: endereço **publicado pela própria casa**, não montado.

### Maria Sjöman — HR (dona da requisição de Art Director and Art Lead) — Coffee Stain North, Estocolmo, Suécia
- **Email:** maria.sjoman@coffeestain.com · confiança **alta** · fonte: https://jobs.coffeestain.com/jobs/8083591-art-director-and-art-lead — fim do anúncio, em texto e em `mailto:`, lido nesta rodada: **"If you have any questions regarding the role, please reach out to Maria Sjöman, HR, maria.sjoman@coffeestain.com"**. O mesmo endereço aparece na outra vaga aberta da casa (Senior Game Designer).
- **Armadilha de domínio, confirmada de novo:** o site de recrutamento é `jobs.coffeestain.com`, o relay do Teamtailor é `coffeestainstudios.teamtailor-mail.com` e o email corporativo é **`@coffeestain.com`**. Endereço montado sobre `coffeestainstudios.com` teria quicado. É a lição da Stunlock, de novo.
- **Por que ELA e não outra pessoa:** a casa tem **34 pessoas** e não publica o email de mais ninguém; ela é a pessoa nomeada na requisição de arte. O cargo de Art Director está **aberto**, ou seja não há diretor de arte a quem escrever hoje.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"COFFEE STAIN NORTH is a small game developer based in Stockholm that belongs to the Coffee Stain Group. Since the company was founded in 2013, we have grown to 34 employees and are now open to adding a couple of new friends"**, e o produto é Goat Simulator 3, que o anúncio descreve como um jogo onde o jogador **"can explore the island of San Angora solo or with friends, wreaking havoc as a goat (or one of many unlockable characters)"**. Elenco de personagens estilizados desbloqueáveis é exatamente o portfólio dele.
- **Fora dos EUA?** Sim — Suécia, União Europeia. A linha de realocação e a de patrocínio entram.
- **Dedupe, feito na caixa:** `pessoas.csv` dá zero para "coffeestain"; `enviados.csv` tem uma linha que **não é carta**, é o registro reconstruído da candidatura de portal; e o **Gmail** mostra que em **06/09** o Vini se candidatou a **esta mesma vaga** pelo Teamtailor e que o recibo veio **assinado por ela** (`maria.sjoman@coffeestainstudios.teamtailor-mail.com`, *"Thank you for your application to the role as Art Director and Art Lead... we will review your application shortly"*). **Nenhuma recusa e nenhuma resposta humana.** PRIMEIRA carta desta casa.
- **Ressalva honesta, três:** (1) ela é **HR, não arte** — numa casa de 34 pessoas isso pesa menos, mas não é o diretor de arte; (2) o próprio anúncio escreve **"Due to GDPR, we can't accept applications through email"**, então a carta **não pode ser candidatura por email**: tem que ser pergunta de direção a quem cuida da requisição, e se citar a vaga precisa dizer que ele **já aplicou pelo portal em 06/09**; (3) a vaga aberta é de Art Director, não de personagem, e o anúncio é de **17/07/2026**.

### Marie Schindler — HR Manager — Stellar Creative Lab, Vancouver, Canadá (e Toronto)
- **Email:** **não existe em fonte pública gratuita** · confiança **sem-email** · fonte da pessoa e do cargo: https://www.stellarcreativelab.com/marie-schindler (página de perfil no site do próprio estúdio, achada pelo https://www.stellarcreativelab.com/sitemap.xml e lida nesta rodada)
- **A casa, e é a pista quente do dia:** estúdio de animação de alto padrão em Vancouver, hoje **produzindo uma série premium de streaming da Marvel Animation**, com as duas vagas da disciplina abertas no JazzHR e lidas por mim nesta rodada: **Modeling Artists (Mid & Senior)** — *"Whether you are building characters, sprawling sets, vehicles, or organic hard-surface props, you are the artist who translates 2D brilliance into optimized 3D reality"* — e **Surfacing Artists (Mid & Senior)** — *"You will be responsible for creating the look, feel, and texture of characters, environments, and objects... exceptional painting skills to achieve a specific 'painterly' aesthetic"*. As duas citam personagem por escrito.
- **Por que ELA e não outra pessoa:** o estúdio publica **treze** pessoas com nome e cargo (Hasmi Ferguson e Bert Van Brande, cofundadores; Angel "Tote" Gonzalez, Head of Animation; Jacquie Doyle, Vis Dev; Alex Baehr, Pipeline TD; e as demais de câmera, direção e finanças) e **nenhum Head of Art, Art Director ou supervisor de assets**. Com as vagas abertas sendo de assets, a HR Manager é a única pessoa publicada que responde por contratação.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"We are a high-end animation studio founded by industry veterans Hasmi Ferguson and Bert Van Brande"**, e o anúncio abre com **"At Stellar, we aim to build a studio where people actually want to work... We value honesty, creativity, and looking out for one another."**
- **Fora dos EUA?** Sim — **Canadá**, o país de maior prioridade do BRIEF-JOE.
- **Dedupe, feito na caixa:** zero carta em `enviados.csv` e zero pessoa em `pessoas.csv`; o **Gmail** mostra **um recibo automático de candidatura de 31/08** (`noreply@applytojob.com`, *"Thank you for your interest in Stellar Creative Lab... we will contact you if your skill set is suitable for one of our open roles"*, sem nome de vaga) e o alerta do LinkedIn de hoje que trouxe as vagas. **Nenhuma recusa, nenhuma resposta humana.** PRIMEIRA pessoa desta casa.
- **O QUE TRAVA, sem maquiagem:** o site inteiro — home, `/our-studio`, `/contact`, `/work-with-us`, `/privacy-policy` e as **treze** páginas de perfil — publica **um único endereço**, `hello@stellarcreativelab.com`, e nenhum endereço de pessoa. Os únicos lugares que oferecem um são ZoomInfo, RocketReach e ContactOut, **agregadores pagos**, proibidos. **Nada foi montado.**
- **ROTA REAL ENQUANTO ISSO, e ela é boa:** carta para `hello@stellarcreativelab.com`, que é publicado, **citando as duas vagas pelo nome** e dizendo que o formulário barrou — os dois formulários do JazzHR estão atrás de **reCAPTCHA v2** medido hoje pela força-tarefa e foram para a fila de mão do Vini. É o mesmo desenho da saída da Lightfox de hoje: quando o formulário fecha a porta, escrever para a caixa publicada explicando por quê é honesto e é informação útil para a casa.
- **Ressalva honesta:** o cargo dela é RH e não arte, que é justamente o filtro que descarta o Vini em cinco segundos pela linha do visto. Por isso a carta, se sair, tem que abrir pela **vaga e pelo portfólio de personagem**, não pelo pedido de patrocínio.

### Michael Reuter — Geschäftsführer / Managing Director — Automatik VFX Berlin GmbH (grupo The Post Republic), Berlim, Alemanha (e Londres)
- **Email:** **não existe endereço de pessoa publicado** · confiança **sem-email** · fonte do nome e do cargo: https://automatik-vfx.com/impressum — **"Automatik VFX Berlin GmbH, Schlesische Straße 38, 10997 Berlin, Deutschland... Geschäftsführer / Managing Director: Michael Reuter"**. A página **só abre com navegador**: o site é SPA em Nuxt e por `curl` devolve casca de 4,6 kB com `LOADING...`. Foi aberta com `hb_run.sh` nesta rodada.
- **Por que esta casa, e ela é INÉDITA:** a vaga da disciplina está viva e veio da planilha pública da comunidade (regra 16): **"Automatik VFX / Berlin / Germany / Character Artist / Mid / On-Site / August 28, 2026"**, com **ZBrush, Maya, Arnold, Mari** como software exigido e a nota *"Starts mid/end September and goes for 3-4 months"*. Ela **não aparece na página de carreiras deles** — as quatro de lá são de Londres (FX, Nuke, Houdini FX, Houdini Generalist) — porque foi anunciada só no LinkedIn, que devolve 999 para esta campanha.
- **Por que ELE:** a casa **não publica nenhum nome de arte**. O impressum alemão é o único lugar onde um nome de pessoa aparece, e é o do diretor-gerente da entidade de Berlim, que é justamente onde está a vaga.
- **Gancho, com a frase do próprio estúdio entre aspas:** a home diz **"VISUAL EFFECTS — Concepts • Creatures • Environments • FX"**, o rodapé assina **"TWO STUDIOS ONE MINDSET"**, e a página de contato convida por escrito: **"Whether you have a project opportunity, are seeking a new role or work experience / internship, or just want to say hi... We'd love to hear from you."** Créditos da casa, da própria página de notícias: *All Quiet on the Western Front* (Oscar de filme internacional), *Faruk* (Berlinale), *Motel Destino* (Cannes) e trabalho no universo de *Doctor Who*.
- **Fora dos EUA?** Sim — Alemanha, União Europeia (e um segundo estúdio no Reino Unido).
- **ROTA REAL:** `jobs_berlin@automatik-vfx.com`, **publicado** em https://automatik-vfx.com/contact e específico do estúdio de Berlim, citando a vaga de Character Artist pelo nome. As outras caixas publicadas são `info@`, `jobs_london@` e `pressrelations@`.
- **Dedupe, feito na caixa:** zero ocorrência de "automatik" e "post republic" em `pessoas.csv`, `enviados.csv`, `automacao/processados.csv` e `docs/index.html`, **e o Gmail devolveu zero**. Casa inédita, PRIMEIRA pessoa.
- **Ressalva honesta, três:** (1) ele é o diretor-gerente, **não** o supervisor de arte; (2) a vaga é **contrato curto (3-4 meses) e presencial em Berlim**, o que significa pedir visto alemão para poucos meses — é o ponto fraco desta ficha; (3) a existência da vaga vem da planilha da comunidade e de um anúncio do LinkedIn que eu **não consegui abrir**; o que abri e li foi o site da casa.

### ~~Ricard Cussó / Ryan Greaves — Cosmic Dino Studio (Brisbane, Austrália)~~ — **DESCARTADA NESTA RODADA, NÃO ESCREVER**
A casa é ótima no papel: estúdio australiano de longas estilizados (*Scarygirl* 2023, *The Sloth Lane*, *Combat Wombat*), fundadores publicados em https://cosmicdinostudio.com/our-story/ com nome e cargo (**Ricard Cussó, Founder / Feature Director**; **Ryan Greaves, Founder / Producer & Screenwriter**; **Tania Vincent, Director / Head of Animation**), e **vaga viva de CG Supervisor** com `jobs@cosmicdinostudio.com` publicado na planilha pública de vagas.

**O Gmail matou, de novo pela caixa e não pelo arquivo.** Em **02/09** saiu carta fria para `hello@cosmicdinostudio.com` e em **03/09** um humano respondeu, de **`stephen.d@cosmicdinostudio.com`**: *"Cosmic Dino has received your application! ... We'll be reviewing your submission shortly ... and will be in touch if your profile aligns with future job openings."* **Quem já respondeu está fora dos limites do Joe: a thread é do Comunicador.**

**O que fica de útil, e é um padrão de domínio novo provado por endereço LITERAL:** `cosmicdinostudio.com` usa **`nome.inicial@`** (`stephen.d@cosmicdinostudio.com`, visto na caixa, não montado). Se um dia a casa voltar para a fila, é esse o formato — e o `hello@` continua sendo a porta publicada.

---

## OS TRÊS TRAVADOS: o que foi tentado hoje e o que caiu

Nenhum dos três ganhou endereço literal nesta rodada. Fica escrito **o que foi medido**, para ninguém repetir:

- **Jan Philip Cramer (Digital Domain).** A página https://digitaldomain.com/contact-us **publica sim endereços de pessoa**, e eu os li hoje com o decodificador ligado — mas são todos da holding asiática e da área comercial: `arthur.ma@ddhl.com` (VP Operations), `allen.chen@ddhl.com`, `hongjie.liu@ddhl.com` (GM China), `william.yang@ddpo.com`, `yaqi.ren@ddhl.com`, `colin.kwok@ddhl.com`, mais `pr@ddhl.com`, `marketing@d2.com` e `newbusiness@d2.com`. **Nenhum de arte, nenhum na América do Norte**, e a linha de recrutamento aponta para `careers.digitaldomain.com`. O talk dele no SIGGRAPH 2023 (*She Hulk*) **não tem PDF hospedado** no `history.siggraph.org` (a página existe e mostra `2023-Image-Not-Available`), então não há rodapé de autor para ler. `jpcramer.com` existe e é **domínio estacionado** (114 bytes, redireciona para `/lander`); `janphilipcramer.com` e `philcramer.com` não respondem.
- **Paweł Mielniczuk (CD PROJEKT RED).** Varri `cdprojektred.com` e `cdprojekt.com` com decodificação de entidade e de `data-cfemail`: só saem `ir@cdprojekt.com`, `recepcja@`, `esg@`, `gielda@` e `wza@cdprojekt.com`, todas caixas corporativas de relações com investidores. **Armadilha de domínio evitada e registrada:** `mielniczuk.art` responde 200 e **é de outra pessoa** — um pintor polonês de pastel e óleo, sem ligação com ele. Mesma família do `skyerzz.com`.
- **Michael Skyers (Digital Extremes).** `michaelskyers.com` e `skyers.art` não existem. A única oferta de endereço continua sendo agregador pago. Sem novidade.

---

## RODADA DAS 22h DE 12/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Veia nova desta rodada, e ela é a irmã do `recruiter-email` do Teamtailor:** estúdio que usa
**Lever mas renderiza as vagas no domínio PRÓPRIO** com front-end Nuxt costuma imprimir no HTML,
dentro do `__NUXT_DATA__`, o **objeto de usuário do DONO de cada requisição**, com nome, cargo e
**email corporativo real**. Não é padrão deduzido: é endereço publicado pela casa. E, resolvendo os
índices do payload, dá para dizer **qual pessoa é dona da requisição de personagem**, que é
exatamente o que o BRIEF-JOE pede em casa grande.

```
curl -sS -L https://careers.<dominio>/ | grep -oE '[a-z.]+@<dominio>'
# depois: json.loads do __NUXT_DATA__ e resolver posting['owner'] -> {name, email, jobTitle}
```

**Rendimento honesto, medido:** testei **~110 páginas de carreira** de casas no escopo (subdomínios
`careers.`/`jobs.` e `/careers` do domínio próprio, games e animação). O payload vazou em **UMA**:
a Frontier. As outras devolveram só caixa genérica (`recruitment@sumogroupltd.com`,
`jobs@supermassivegames.com`, `office@peoplecanfly.com`, `info@wetaworkshop.co.nz`) ou nada.
**Veia rica e rara**, igual à do Teamtailor: vale como teste barato em casa nova, não como varredura.

### Ellie Baldino — **Talent Acquisition Advisor** — Frontier Developments plc, Cambridge, Reino Unido

- **Email:** ebaldino@frontier.co.uk · confiança **alta** · fonte: https://careers.frontier.co.uk/ —
  payload do próprio site de carreiras da casa, lido nesta rodada, literal: `"Ellie Baldino"`,
  `"ebaldino@frontier.co.uk"`, `"Talent Acquisition Advisor"`.
- **Por que ELA e não outra pessoa:** resolvendo os índices do payload, a requisição
  **"Experienced Character Artist" tem como *owner* exatamente ela** (as outras dela são Lead Artist,
  Lead Technical Artist e VFX Artist). É o alvo literal do BRIEF-JOE para casa grande: **recrutador
  com nome e sobrenome e com a requisição de personagem na mão**, numa casa que não publica o email
  de nenhum artista. A vaga foi confirmada na fonte oficial nesta rodada
  (`https://api.eu.lever.co/v0/postings/frontier?mode=json`): department **Art**, team **Character**,
  Cambridge/Hybrid, Permanent — https://jobs.eu.lever.co/frontier/3571ace3-9f1a-4db2-9e2b-5eb8c8487181
- **Gancho, com a frase do próprio anúncio entre aspas:** **"The Experienced Character Artist will be
  responsible for delivering high-quality, game-ready character and creature assets"** e, no mesmo
  anúncio, **"We can provide a comprehensive relocation support package as part of any offer, should
  you need to relocate."** A segunda é ouro: é a casa respondendo por escrito a dúvida número um do
  leitor, e a carta pode citá-la de volta.
- **Fora dos EUA?** Sim — Reino Unido. A linha de realocação e a de patrocínio entram inteiras.
- **Dedupe, feito na caixa:** `pessoas.csv` dá **zero** para "Frontier Developments" (as três
  ocorrências de "frontier" são **Final Frontier** e **Digital Frontier FX** — armadilha de grafia); o
  **Gmail** mostra que em **10/09 o Vini já se candidatou a ESTA vaga** (recibo do Lever EU) e que o
  alerta do LinkedIn ainda a anunciava hoje às 17h46. **Nenhuma recusa, nenhuma resposta humana.**
  PRIMEIRA pessoa desta casa.
- **Alternativas da MESMA casa, que NÃO abrem carta própria:** Yaz Harniman
  (`yharniman@frontier.co.uk`, Talent Acquisition Partner) e Lee Mowatt (`lmowatt@frontier.co.uk`,
  cargo nulo no payload). O formato `inicial+sobrenome@frontier.co.uk` fica provado por **três**
  endereços literais.
- **Ressalva honesta, três:** (1) o endereço está no **payload JSON** da página — publicado pelo site
  da casa, mas **não escrito em texto visível na tela**; (2) ela é recrutamento, não arte, o que aqui
  é vantagem porque é quem despacha a requisição; (3) **a carta tem que dizer que ele já aplicou pelo
  portal em 10/09**, senão chega como se fosse primeiro contato.

### Glauco Longhi — **Character Director** — Santa Monica Studio (PlayStation Studios), Los Angeles, EUA

- **Email:** **não existe em fonte pública** · confiança **sem-email** · fonte da pessoa e do cargo:
  **site pessoal dele**, https://www.glaucolonghi.com/about, lido nesta rodada.
- **Por que ELE e não outra pessoa da casa:** é o **diretor de personagem** de uma casa AAA de
  personagem. O próprio texto dele: *"Currently working at Santa Monica Studio as **Character
  Director**, previously at Unknown Worlds Entertainment as Studio Art Director, Art Director at
  Striking Distance Studios, **Character Director for The Callisto Protocol**, **Lead Character
  Artist at Sony Santa Monica Studio**, working on the God of War Franchise and **Senior Character
  Artist at Naughty Dog**"*, com créditos em The Callisto Protocol (2022), God of War Ragnarök
  (2022), God of War (2018) e Uncharted 4 (2016). Não é recrutador, não é produção, não é ambiente.
- **Fora dos EUA?** Não — Los Angeles. A frase de realocação **não** entra; o que entra é o pedido de
  patrocínio, e ele é o ponto fraco desta casa.
- **Dedupe, feito na caixa:** o Gmail devolve **três** threads — a carta de **08/09 para Josiah
  Scholten** (`josiah.scholten@sony.com`, endereço **montado**, sem resposta e sem bounce na thread),
  o recibo de candidatura de 31/08 para Senior 3D UI Artist (*"Thank you for applying to Santa Monica
  Studio!"*) e um boletim de terceiro. **Nenhuma recusa, nenhuma resposta humana.** Esta é a
  **SEGUNDA e ÚLTIMA** pessoa da casa — e é alvo melhor que a primeira.
- **O QUE TRAVA, sem maquiagem:** https://www.glaucolonghi.com/contact-me **não publica endereço
  nenhum**, só lista de espera de mentoria e cursos da Longhi Academy; a única string com `@` na
  página é o placeholder `user@domain.com` do tema. **Nada foi montado.**
- **Ressalva honesta:** o site oficial do estúdio está **travado para esta campanha**
  (`sonysantamonica.com` devolveu **502 no túnel do proxy** e `santamonicastudio.com` devolveu
  **403**), então o gancho disponível vem das palavras **dele**, não das da casa.

### ~~Frank Tzeng — Naughty Dog~~ — **ARMADILHA DESCARTADA NESTA RODADA, e ela é repetível**

A busca devolve "Frank Tzeng, Lead Character Artist, Naughty Dog", e `franktzeng.com` responde 200
**com email publicado**: `frank@TzengMgmt.com`. O endereço é literal — e é de **outra atividade**:
o site hoje é de uma **consultoria de gestão** (*"Frank D. Tzeng / CEO 曾敦仁 / 執行長 — Irvine, CA —
Taipei, Taiwan"*), com método de cinco P e nenhuma menção a arte de personagem. **Endereço publicado
não prova cargo atual**, e cargo desatualizado é pior que alvo nenhum. Descartado antes de virar linha.

### Olcun Tan — **Founder** — Gradient Effects, Los Angeles, EUA

- **Email:** **não existe endereço de pessoa publicado** · confiança **sem-email** · fonte do nome e
  do cargo: https://www.gradientfx.com/about/ — **"Gradient Effects is a Los Angeles based VFX
  company founded in 2006 by academy member Olcun Tan"**, e a mesma página declara que **"SCRTLB was
  founded in 2013 out of Gradient Effects as a branch dedicated to animation and VFX for blockbuster
  movies."**
- **Como a casa apareceu:** filtro do `automacao/garimpo-cgstudiomap.csv` por
  `ja_na_campanha=nao` + `tem_vaga_disciplina=sim` + observação **ALTA**, dentro do escopo — sobraram
  **quatro** casas, e esta é a única dos EUA sem pessoa registrada.
- **Por que ELE:** casa pequena que **não publica o nome de mais ninguém**, nem de arte nem de RH;
  o BRIEF-JOE manda ir no fundador quando não há diretor de arte publicado.
- **A vaga, lida nesta rodada** em https://www.gradientfx.com/jobs/ : **"3D MODELER - Los Angeles,
  California"**, pedindo *"Expert knowledge of Maya, ZBrush, Mud Box"*, *"Expert knowledge of
  Photoshop, Mari"*, *"Must understand Deformers and basic knowledge of Rigging techniques"* e
  *"Strong knowledge and experiences in materials/shader/look development"*.
- **Fora dos EUA?** Não — Los Angeles. Sem frase de realocação; o patrocínio é o ponto fraco.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv` e `processados.csv`;
  `docs/index.html` tem **uma** linha de 07/09 que é registro de **portal**, não carta; e o **Gmail
  devolveu ZERO**. PRIMEIRA pessoa desta casa.
- **ROTA REAL enquanto não houver endereço de pessoa:** `contact@gradientfx.com`, que é o **único**
  endereço do site inteiro, citando a vaga pelo nome — e o próprio anúncio escreve **"NO PHONE
  CALLS"** e que candidatura presencial não é aceita, ou seja email é a porta que sobra.
- **Ressalva honesta, três:** (1) o anúncio **não usa a palavra character nem creature** — pela regra
  PERSONAGEM PRIMEIRO é modelagem genérica, e a carta tem que se vender por personagem sem fingir que
  a vaga é de personagem; (2) o rodapé do site marca **Copyright 2021**, então o quadro pode estar
  parado, ainda que a campanha o tenha reconferido em 07/09; (3) ele é **fundador, não supervisor de
  arte**, e não confirmei o título operacional dele hoje — o que vale é o critério do BRIEF-JOE, de
  que fundador não muda de casa.

### TRÊS CASAS MORTAS PELA CAIXA NESTA RODADA, e as três pareciam boas no arquivo

O `grep` dava sinal verde nas três. Quem matou foi o **Gmail** e, num dos casos, o **painel** —
exatamente o que o `dedupe-agora.sh` manda fazer antes de escrever a ficha.

- **~~Behaviour Interactive (Montréal)~~ — RECUSOU.** No papel era o achado do dia: **três**
  *Senior 3D Character Artist* abertas ao mesmo tempo no Lever (`bhvr`) — 7 Days to Die, Dead by
  Daylight e projeto não anunciado —, casa AAA canadense, e `pessoas.csv` com **zero** pessoa. O
  Gmail conta outra história: em **11/09 às 17h17** chegou *"Thank you for your interest in Behaviour
  Interactive and application for the Senior Character Artist position, on 7 Days to Die. We are
  sorry to inform you that we have decided to move..."*. **Casa que já recusou está fora dos limites
  do Joe.** Fica valendo só o que é da caça: a candidatura de **10/09** para a Dead by Daylight segue
  sem resposta, e a de projeto não anunciado (`86ddd557`) continua aberta.
- **~~DNEG~~ — RECUSOU DUAS VEZES.** `pessoas.csv` tem zero pessoa da DNEG e o site publica até
  endereços de área (`art@dneg.com`, `dneg-animation@dneg.com`, `cto-office@dneg.com`, lidos hoje na
  página About). Mas o Gmail tem **duas recusas escritas**: **01/09**, Character Modeller (DNEG
  Animation), Londres — *"we are currently unable to consider candidates who live overseas"* — e
  **11/09**, *Modeleur de personnages / Character Modeler (DNEG Animation)*, Montréal, com a mesma
  frase em francês. **Fora dos limites.**
- **~~Wil Film (Copenhague)~~ — VETO DE VISTO ESCRITO, e o painel já sabia.** A varredura mecânica
  desta rodada achou o que parecia uma ficha perfeita: estúdio de **animação 3D de personagem
  estilizado** há quase 20 anos (*"9 seasons of the outstanding TV series 'Ninjago: Masters of
  Spinjitzu' with 102 episodes and several 'LEGO Star Wars' productions"*), com a página `/team`
  publicando **`erik@wilfilm.dk` — Erik Wilstrup, CEO** e o `/jobs` convidando candidatura espontânea
  (*"send your CV and portfolio to: jobs@wilfilm.dk"*), mais `morten.stahlhut@wilfilm.dk` de um
  anúncio. Gmail e CSVs davam **zero**. O que mata está na mesma página `/jobs`: **"Apply for an open
  position ONLY if you are a EU pass holder"**, e o `docs/index.html` já registrava isso em **07/09**
  como *"DESCARTE COM VETO ESCRITO"*. **O dedupe tem que incluir o painel, não só os CSVs e a caixa.**

### ATUALIZAÇÃO DOS QUATRO TRAVADOS — o que esta rodada tentou e o que sobrou

- **Paweł Mielniczuk (CD PROJEKT RED) — ROTA NOVA, e é a única novidade dos quatro.** Ele é
  **Festival Director do Promised Land Art Festival**, que a própria CDPR organiza. O site do festival
  existe e publica endereço: **`contact@promisedland-artfestival.com`** e **`biz@`** e **`media@`**
  (https://www.promisedland-artfestival.com/en, lido nesta rodada), e o **regulamento oficial de 2024
  hospedado pela própria CDPR** (https://cdn-l.cdprojektred.com/Regulamin_PLAF_24_EN.pdf, 6 páginas,
  lido nesta rodada) confirma o festival como coisa da casa e repete o mesmo `contact@`. **Não é o
  endereço dele** e o site do festival **não escreve o nome dele em lugar nenhum** — mas é uma caixa
  publicada da operação que ele dirige, e é melhor porta que `ir@cdprojekt.com`. Quem escrever decide.
  O que continua valendo: **nenhum `@cdprojektred.com` aparece no regulamento nem no site do festival**.
- **Jan Philip Cramer (Digital Domain).** Busca pelo literal `"@d2.com" Cramer` devolve **só agregador
  pago** (ZoomInfo com `a***@d2.com`, adapt.io) e as caixas comerciais que a rodada das 15h40 já tinha
  lido. Nada novo. Continua sem endereço dele.
- **Michael Skyers (Digital Extremes)** e **Marie Schindler (Stellar Creative Lab).** Busca pelo nome
  + estúdio + "email" devolve, nos dois casos, **apenas RocketReach/ZoomInfo/ContactOut com o
  endereço mascarado** (`m******@stellarcreativelab.com`). Serviço pago é proibido. **Nada foi
  montado, e as duas fichas seguem valendo pelo nome e pelo cargo.**

---

## RODADA DAS 15h35 DE 13/09 — JOE. ALVO GEOGRÁFICO: **HOLANDA PRIMEIRO, NÓRDICOS EM SEGUIDA**.

**Por que esta rodada é geográfica:** a medição de 12/09 às 22h conta **125 vetos escritos de
autorização de trabalho no Canadá**, 21 nos EUA e **ZERO na Holanda**; e a varredura de 12/09 às
23h mediu **zero vaga de personagem no quadro nacional holandês**. Porta aberta, prateleira vazia:
a rota holandesa é **carta para pessoa com nome**, não fila de formulário. Reconferido nesta
rodada: `https://www.dutchgamesindustry.nl/jobs` responde 200, declara **119 vagas, 38 casas, 19
cidades**, e **nenhuma é de personagem** — as de arte são 2D Artist (Miniclip), estágio de 3D e 2D
(Little Chicken) e Game Art stage (hackshield). A Guerrilla segue com **uma** vaga no país inteiro
(Studio Technical Director) e a Nixxes com duas, **as duas de programação**.

**Agente não escreve carta.** A escrita do Gmail não está na lista `tools` deste agente. Leitura do
Gmail foi usada em todas as fichas, e é ela que manda no dedupe.

### Jeff Dronkers — **Lead Character Artist** — Vertigo Games, Roterdã, Holanda

- **Email:** **não existe em fonte pública** · confiança **sem-email** · fonte do nome e do cargo:
  https://theorg.com/org/vertigo-games-1/org-chart/jeff-dronkers , aberta nesta rodada, literal:
  *"Jeff Dronkers / Lead Character Artist / Rotterdam, Netherlands / Jeff Dronkers is a seasoned
  Senior Character Artist at Vertigo Games, with a career spanning various roles in 3D art and
  animation since 2010"*, dentro do time **"Art and Animation Team, 37 people"** da casa.
- **Por que ELE e não outra pessoa da casa:** é o **único cargo de chefia de personagem** que a
  casa tem nome público. Vertigo é o maior estúdio holandês de VR (PLAION), com Arizona Sunshine,
  Metro Awakening e Thief VR, ou seja **criatura e personagem em primeira pessoa** — a disciplina
  exata dele. Não é recrutador, não é ambiente, não é produção.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de vagas deles, aberta nesta
  rodada (https://www.vertigo-games.com/jobs/), não lista **nenhuma** posição aberta e em vez disso
  escreve **"You are welcome to send us an open application. Please include a motivation letter,
  resume and/or portfolio where applicable"**. E o About diz: **"Vertigo Studios Rotterdam (the
  Netherlands) creates cutting-edge, high-quality games that offer unrivaled immersion, realizing
  the stoutest dreams of gamers everywhere."** A carta entra exatamente pela porta que eles
  próprios abriram.
- **Fora dos EUA?** Sim — Holanda. Leva a linha de realocação e a de patrocínio. E a Holanda é o
  país com **zero veto escrito** na contagem da campanha, o que torna essa linha barata de escrever.
- **Dedupe, feito na caixa:** `pessoas.csv` dá **zero** para Vertigo; o **Gmail** devolve **uma**
  thread, com a carta fria de **02/09 para `jobs@vertigo-games.com`** e o follow-up de **07/09** na
  mesma thread. **Nenhuma resposta, nenhuma recusa, nenhum bounce.** PRIMEIRA pessoa desta casa.
  `grep` por "Dronkers" no Gmail: zero.
- **Ressalva honesta, três:** (1) **não há endereço** — nem publicado nem montável com honestidade,
  porque a casa não expõe nenhum endereço individual e o único `@vertigo-games.com` que existe em
  fonte pública é o `jobs@`, que já recebeu duas mensagens; (2) o cargo vem do **The Org**, que
  marca o perfil como **"Unverified"** e cuja fonte é o LinkedIn — o site do estúdio **não publica
  nome de artista nenhum**, então o cargo não tem confirmação de primeira mão; (3) a casa foi
  tocada há **seis dias** (follow-up de 07/09), então a carta para ele é a **segunda e última**
  aproximação permitida e precisa assumir isso na primeira linha, nunca chegar como primeiro contato.

### Dario van Vree — **Cofundador e Diretor** — Studio Pupil, Amsterdã, Holanda

- **Email:** dario@studiopupil.com · confiança **alta** · **PUBLICADO** · fonte:
  https://studiopupil.com/people/ e https://studiopupil.com/contact/ , as duas abertas nesta
  rodada. O endereço aparece **em texto visível** no topo das duas páginas e de novo no fim da
  biografia dele. É o **único** endereço do site inteiro: não existe `info@` nem `jobs@` ali.
- **Por que ELE e não outra pessoa da casa:** a página `people` publica **uma pessoa só**, ele.
  Casa pequena, e o BRIEF-JOE manda ir no **fundador** quando não há diretor de arte publicado.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Dario van Vree directs animation with
  an eye for the weird, the incentive and the power of character performance."** E, na mesma
  página: **"With Studio Pupil we find ourselves at the heart of European indie animation"**. Ele
  também **ensina storytelling e animação de personagem na Willem de Kooning Academy** e
  **cofundou o Kaboom Amsterdam Animation Festival** — e isso casa com o lado de escola do Vini
  (a Vini Cavalcanti School), que é justamente o link que a carta fria costuma desperdiçar.
- **Fora dos EUA?** Sim — Holanda. Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv` e `docs/index.html` dão **zero** para
  "Studio Pupil"; `automacao/processados.csv` tem **uma** ocorrência, que é registro de varredura e
  não de carta; e o **Gmail devolveu ZERO** para `snowcloud OR "Studio Pupil" OR studiopupil OR
  Dronkers`. CASA NOVA para a campanha inteira, PRIMEIRA pessoa.
- **Ressalva honesta, e ela é pesada:** **é estúdio de animação de autor, majoritariamente 2D**
  ("I'm Perfectly Fine", "Luce and the Rock", "Sisters of the Mist"), então o encaixe com
  **personagem 3D** é **indireto** — o que aproxima é a frase deles sobre *character performance* e
  o fato de ele ensinar animação de personagem, não uma pipeline de sculpt/retopo/textura. Segunda
  ressalva: **não há vaga aberta**, o site não tem página de carreira; é carta de porta. Terceira:
  a página de contato tem telefone publicado, que **não** foi registrado aqui, porque o repositório
  é público.

### Juras Rodionovas ("Juras") — **Character Artist (time de personagem de Darktide)** — Fatshark, Estocolmo, Suécia

- **Email:** **não existe endereço vivo** · confiança **sem-email** · fonte do nome, do cargo e do
  trabalho: **o dev blog do próprio estúdio**,
  https://forums.fatsharkgames.com/t/darktide-101-enemy-character-art-dev-blog/105178 (11/02/2025),
  aberto nesta rodada, literal: **"Hello! My name is Juras, and I am one of the character artists
  who worked on enemy character art for Warhammer 40,000: Darktide"** e **"with a (quite) small
  in-house team of character and concept artists"**.
- **POR QUE ESTA CASA É A MELHOR DA RODADA, e é medição de hoje:** a Fatshark tem **vaga de
  personagem VIVA**, lida nesta rodada em `https://fatshark.teamtailor.com/jobs.json` (HTTP 200,
  5 vagas) e conferida no anúncio
  `https://fatshark.teamtailor.com/jobs/8190501-character-artist` (publicado em **07/08/2026**).
  É a **única** vaga da disciplina que esta rodada achou em toda a Holanda e nos nórdicos.
- **Gancho, com a frase do próprio anúncio entre aspas:** **"As a member of the Character Art
  Team, you will help us in creating gritty and believable characters and creatures, developing our
  pipeline, and integrating content into the engine... applying your skills in high-poly sculpting,
  modeling, texturing, as well as hair grooming."** E, na lista de benefícios,
  **"Relocation package for international talent"**. As duas linhas são de ouro: a primeira nomeia
  **grooming**, que é o diferencial dele, e a segunda é a casa respondendo por escrito à dúvida
  número um do leitor. Do dev blog, o gancho de colega para colega:
  **"Making character art begins with having great concepts to use as reference and target."**
- **Por que ELE e não outra pessoa da casa:** é artista de personagem de dentro, e o BRIEF-JOE diz
  que **colega de ofício responde colega de ofício** e que indicação interna pula a fila. A
  alternativa seriam as duas recrutadoras que já apareceram na caixa (ver dedupe), e elas são
  **relay do Teamtailor**, não endereço corporativo.
- **Fora dos EUA?** Sim — Suécia. Entram realocação e patrocínio, e a carta pode citar de volta o
  **"Relocation package for international talent"** deles.
- **Dedupe, feito na caixa:** o Gmail devolve **três** threads da Fatshark, todas de 06 e 07/09 e
  todas do relay `@fatshark.teamtailor-mail.com`: o "Welcome to Fatshark" de **Jonas Wallin**, dois
  "Log in to Connect" automáticos, e o **"Thank you for your application! :)" de Rachel Raschke**
  (*"We have successfully received your details, but since many Sharks are on summer vacation now,
  the process will be a bit slower than usual"*). **Nenhuma recusa e nenhuma resposta humana de
  verdade** — as três são automáticas do Connect. `pessoas.csv` dá **zero** para Fatshark.
  PRIMEIRA pessoa desta casa.
- **O QUE TRAVA O ENDEREÇO, sem maquiagem:** o site pessoal dele, `juras3d.com`, aparece em busca
  com o endereço `juras.rodionovas@juras3d.com`. **Eu não usei esse endereço e ele não entra na
  linha**, porque o domínio **não existe mais**: `curl` devolve `CONNECT tunnel failed 502` e a
  consulta de DNS em `https://dns.google/resolve?name=juras3d.com&type=A` responde
  **`"Status":3`, que é NXDOMAIN**. Endereço em domínio morto quica por definição. Foi medido, não
  suposto.
- **Ressalva honesta, três:** (1) o sobrenome **Rodionovas** e o título **"Lead Character Artist"**
  vêm de **resumo de busca**, não de fonte aberta por mim — a fonte de primeira mão (o dev blog do
  estúdio) escreve só **"Juras"** e **"one of the character artists"**, então é assim que a linha
  guarda o cargo; (2) o dev blog é de **fevereiro de 2025**, e cargo desatualizado é pior que alvo
  nenhum — não confirmei hoje que ele continua na casa; (3) **sem endereço não há carta para ele
  hoje**; o que esta ficha entrega de valor imediato é **a vaga viva**, e a decisão de escrever
  para uma das recrutadoras do relay é do maestro, sabendo que montar
  `nome.sobrenome@fatshark.se` seria exatamente o chute que produziu as 17 devoluções de 07/09.

### Michael Bengtsson — **Cofundador (contato publicado de business inquiries)** — Mindbender (Meindbender), Gotemburgo, Suécia

- **Email:** michael@mindbender.com · confiança **alta** · **PUBLICADO** · fonte:
  https://meindbender.com/ , aberta nesta rodada. O endereço está no `mailto:` do bloco
  `contact-info-business-inquiries`, com o nome **"Michael Bengtsson"** no `<span>` imediatamente
  acima e o LinkedIn dele ao lado. Os únicos dois endereços do site são `mail@mindbender.com` e
  este.
- **ARMADILHA DE DOMÍNIO, pela quinta vez nesta campanha, e ela está registrada aqui de propósito:**
  o site é **`meindbender.com`** e o email é **`@mindbender.com`**. Endereço montado sobre o
  domínio do site teria quicado — é o caso Stunlock (`stunlock.com` / `@stunlockstudios.com`), o
  Apparat (`apparat.studio` / `@apparat.no`) e a TELEVISOR de novo.
- **Por que ELE e não outra pessoa da casa:** a casa foi **fundada em 2006 por Michael Bengtsson,
  Calle Halldin, Olov Burman e Tony Österlund** (texto da própria home) e ele é o **único dos
  quatro com endereço publicado**. Casa pequena e de fundador: o BRIEF-JOE manda ir no fundador.
- **Gancho, com a frase do próprio estúdio entre aspas:** a lista de serviços da home diz, literal,
  **"Iconic character design: From concept to full 3D"**, e o parágrafo seguinte:
  **"working together to create characters and story that is not only memorable in their own right,
  but simultaneously tailored to communication."** No mesmo bloco eles listam **"Digital animation:
  Commercials, Game Trailers"** — ou seja, personagem 3D para jogo é serviço de casa. Esta é a
  frase mais próxima do portfólio do Vini em toda a rodada.
- **Fora dos EUA?** Sim — Suécia. Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** `meindbender`, `mindbender` e `Michael Bengtsson` dão **zero** em
  `pessoas.csv`, `enviados.csv`, `automacao/processados.csv`, `docs/index.html` **e `alvos.csv`**;
  e o **Gmail devolveu ZERO** para `mindbender OR meindbender OR Bengtsson`. **CASA NOVA para a
  campanha inteira**, PRIMEIRA pessoa.
- **Ressalva honesta, três:** (1) o endereço está publicado sob a rubrica **business inquiries**,
  ou seja é a caixa comercial dele e não uma caixa de recrutamento — a carta tem que se apresentar
  como oferta de trabalho e não como pedido de emprego genérico; (2) **não há vaga aberta** e o
  site não tem página de carreira, então é carta de porta; (3) não confirmei hoje, por fonte
  independente, que ele continua ativo na casa — o que sustenta a escolha é o critério do BRIEF-JOE
  de que **fundador não muda de casa**, e o fato de o endereço estar no site que está no ar hoje.
- **Segunda e última pessoa possível, para outro dia:** nenhuma com endereço — os outros três
  fundadores aparecem só pelo nome.

### Are Sundnes — **CEO & Cofundador** — Hyper Games, Oslo, Noruega

- **Email:** are@hypergames.no · confiança **alta** · **PUBLICADO** · fonte:
  https://hypergames.no/studio , aberta nesta rodada. A página lista os treze funcionários com
  nome e cargo e publica **três** endereços em texto visível: **"Are Sundnes CEO & Co-founder
  are@hypergames.no"**, "Terje Gran CTO & Co-founder terje@hypergames.no" e "Runa Haukland Project
  Manager runa@hypergames.no".
- **CORREÇÃO DE REGISTRO ANTIGO, e é o achado de método desta ficha:** o
  `automacao/processados.csv` de **06/09** deu esta casa como **DESCARTADA**, com a justificativa
  *"o wp-sitemap completo de paginas nao tem nenhuma pagina de carreiras ou vagas. A pagina de
  contato so trata de suporte do Moomintroll"*. Aquilo estava certo sobre `/contact` e **errado
  sobre a casa**: quem publica endereço de pessoa aqui é **`/studio`**, não `/contact` nem
  `/careers`. É o mesmo erro de rota que já tinha custado a Storm Studios em 10/09. **Descartar uma
  casa por causa de uma rota que não abriu é descartar a rota, não a casa.**
- **Por que ELE e não outra pessoa da casa:** dos três endereços publicados, os outros dois são
  **CTO** e **Project Manager**; nenhum artista da casa tem endereço publicado. Em casa de **13
  pessoas** o BRIEF-JOE manda ir no **fundador**, que responde ele mesmo.
- **Gancho, com a frase do próprio estúdio entre aspas:** a home, aberta nesta rodada, anuncia o
  jogo novo assim: **"From the creators of Snufkin: Melody of Moominvalley comes a new adventure
  based on the wonderful Moomin stories by author Tove Jansson. This time we follow Moomintroll
  himself, in a cold but cozy winter adventure."** E a página do estúdio:
  **"Hyper Games is an independent game studio based in Oslo, Norway. We're most known for our
  games 'Mørkredd', and 'Eggggg'. We started out in 2012 and now count 13 employees."** Casa que
  vive de **personagem licenciado estilizado** (Moomin, Alfie Atkins/Alfons Åberg) é exatamente
  onde o portfólio dele — personagem estilizado e pintado à mão — compete.
- **Fora dos EUA?** Sim — Noruega. Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `hypergames OR "Hyper Games"`.
  `pessoas.csv`, `enviados.csv` e `docs/index.html` dão **zero**; `processados.csv` tem as duas
  ocorrências citadas acima, e **nenhuma delas é carta** — é a nota de descarte de 06/09.
  PRIMEIRA pessoa desta casa, e a casa nunca recebeu mensagem nenhuma.
- **Ressalva honesta, três:** (1) **não há vaga aberta** e o estúdio não tem página de carreiras —
  é carta de porta, e o próprio registro de 06/09 já tinha medido isso; (2) a casa tem **quatro
  pessoas de arte publicadas** (Mads Frantzen, Marcus Kjeldsen, Rolf Hove, Adriane Brennmoen) e
  **nenhuma com endereço** — montar `nome@hypergames.no` para elas seria chute, ainda que o padrão
  de primeiro nome esteja provado por três endereços, e por isso **nada foi montado**; (3) treze
  pessoas é pequeno, então a chance de existir orçamento para patrocínio de visto é a mais fraca
  desta rodada.

### Diana Varro — **Character Artist (theHunter: Call of the Wild)** — Avalanche Studios Group, Malmö, Suécia

- **Email:** **não existe em fonte pública** · confiança **sem-email** · fonte do nome, do cargo e
  do trabalho: **o site do próprio estúdio**,
  https://avalanchestudios.com/stories/character-artist-interview (08/03/2025), aberta nesta
  rodada, literal: **"Diana Varro is a Character Artist on theHunter: Call of the Wild. Originally
  from Hungary, Diana is based in Malmö and is part of the team that brings to life the undisputed
  stars of the game: the animals that populate its many reserves."**
- **Por que ELA e não outra pessoa da casa:** é a **única pessoa de arte de personagem que a
  Avalanche nomeia publicamente**. E o encaixe é raro: o trabalho dela é **criatura com pelo**, que
  é onde o grooming em Houdini do Vini deixa de ser adorno e vira a competência principal. Com as
  palavras dela, do mesmo texto: **"When the research is complete, I get to work on the 3D sculpt
  of the animal – the textures, and a low-poly mesh – which is then set up for technical
  animation."** Isso é o pipeline inteiro dele, descrito por ela.
- **O contexto que dá urgência, conferido na fonte oficial nesta rodada:** a **Lead Character
  Artist** de Estocolmo **continua viva** — `https://api.lever.co/v0/postings/avalanchestudios?mode=json`
  respondeu **HTTP 200 com 12 vagas**, e a requisição `8f7bd580-5877-446e-83cb-97bb1fce0f6a`
  aparece com department **Development**, location **Stockholm**,
  https://jobs.lever.co/avalanchestudios/8f7bd580-5877-446e-83cb-97bb1fce0f6a
- **Gancho, com a frase do próprio estúdio entre aspas:** a chamada da matéria é
  **"Bringing life to Call of the Wild"**, e o texto continua: **"Since we're reproducing real
  animals, the process doesn't involve a lot of pre-production, especially if compared to games
  where you create fantasy characters or monsters."** A carta pode pegar exatamente essa frase e
  trazer o outro lado dela, que é o lado do portfólio dele.
- **Fora dos EUA?** Sim — Suécia. Entram realocação e patrocínio.
- **Dedupe, feito na caixa:** o Gmail devolve **uma** thread — o recibo do Lever de **10/09**,
  *"we received your application for the Lead Character Artist position"*. **Nenhuma recusa e
  nenhuma resposta humana.** `pessoas.csv` dá **zero** para Avalanche. PRIMEIRA pessoa desta casa,
  e a carta para ela é **indicação interna em cima de uma candidatura que já está no sistema**,
  que é o cenário favorito do BRIEF-JOE.
- **Ressalva honesta, quatro:** (1) **não há endereço** e o estúdio não publica nenhum endereço
  individual — o único `@avalanchestudios.com` em fonte pública é comercial, e **nada foi montado**;
  (2) ela é **artista, não lead e não recrutadora**, então a via é encaminhamento e não decisão;
  (3) a matéria é de **março de 2025** e ela mesma diz ter entrado na casa um ano antes daquilo —
  não confirmei hoje que continua lá; (4) ela está em **Malmö** e a vaga aberta é em **Estocolmo**,
  que são divisões diferentes do grupo.

### Petter Lindblad — **Founder (produtor)** — Snowcloud Films, Estocolmo, Suécia

- **Email:** petter.lindblad@snowcloud.se · confiança **alta** · **PUBLICADO** · fonte:
  https://www.snowcloud.se/about-us , aberta nesta rodada. O bloco de equipe traz, em texto
  visível e um embaixo do outro, **"Petter Lindblad" / "Founder" / "petter.lindblad@snowcloud.se"**.
  O único `mailto:` da página é o `contact@snowcloud.se`, ou seja o endereço dele é **publicado em
  texto** e não escondido.
- **Por que ELE e não outra pessoa da casa:** o bloco de equipe publica **uma pessoa só**. A
  própria página diz: **"The company was founded in 2014 by producer Petter Lindblad, formerly
  full-time producer at Copenhagen Bombay for over seven years."**
- **Gancho, com a frase do próprio estúdio entre aspas:** a home deles, aberta nesta rodada,
  publica um item de notícia intitulado **"Looking for Stockholm-based 3D-artists"**, com o texto
  **"We're looking to find some final artists to join our team, available 100% on site in
  Stockholm."** E a descrição da casa: **"Swedish production company focusing on projects for
  children and youths, mainly animation. Specializing in low-cost, lean productions with high
  quality screen results."**
- **Fora dos EUA?** Sim — Suécia. Entram realocação e patrocínio, e a frase deles sobre *100% on
  site in Stockholm* torna a linha de realocação obrigatória e não opcional.
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `snowcloud`. `pessoas.csv`,
  `enviados.csv`, `automacao/processados.csv` e `docs/index.html` também dão zero. **CASA NOVA para
  a campanha inteira**, PRIMEIRA pessoa.
- **Ressalva honesta, três, e a primeira é séria:** (1) o anúncio de 3D artists é de **27/10/2025**,
  ou seja **quase um ano atrás**, e a casa não tem página de carreira para reconferir — pode estar
  morto, e a carta não deve tratá-lo como vaga aberta, só como prova de que a casa contrata artista
  3D em Estocolmo; (2) ele é **produtor e fundador, não arte** — não abre portfólio, encaminha; (3)
  a Snowcloud se define como **produtora** e terceiriza execução (a própria página lista Sun
  Creature, LEE Film, Copenhagen Bombay e Meindbender como clientes/parceiros), então o encaixe com
  personagem 3D é de **serviço**, não de cadeira fixa.

### O NEGATIVO DESTA RODADA, escrito para a próxima não refazer

**Casas que morreram no dedupe, e as duas por motivo diferente:**

- **~~Submarine (Amsterdã)~~ — RECUSOU, e está no `enviados.csv` desde 26/08** com o desfecho
  escrito: *"recusado (respondido; vagas exigem residência NL/BE)"*. É a maior casa de animação
  holandesa e **está fora dos limites do Joe**. Ela aparece como "thread viva" no BRIEFING, o que
  engana: o campo de desfecho é que manda.
- **~~Paladin Studios (Haia)~~ — A CASA FECHOU.** Parecia ficha pronta: `stein@paladinstudios.com`
  publicado com nome (Stein Damen, Business Development) e uma página `/team` com 45 pessoas,
  incluindo quatro 3D Artists. O que mata está no topo de toda página do site, lido nesta rodada:
  **"ANNOUNCEMENT: Our quest has ended, and Paladin has shut down operations on May 1st 2024."**
  Endereço publicado não prova casa viva.

**Falsos amigos de domínio medidos hoje**, para a lista que já tinha `chopchop`, `mpc.wd1`,
`icon.wd3`, `remedy`, `rain`, `triumph` e `playground`:

| domínio | o que eu esperava | o que é |
|---|---|---|
| `studiomassa.com` | Studio Massa, animação holandesa | **escritório de contabilidade italiano** em Casale Monferrato |
| `spektrum.dk` | Spektrum, animação dinamarquesa | **banca de advocacia** em Herning |
| `filmtecknarna.se` | Filmtecknarna, animação sueca | **blog de conteúdo** com posts sobre cassino e mudanças |
| `blackstudios.se` | Bläck, estúdio sueco | **blog** de 2019 sobre desenvolvimento de jogos |
| `storyline.no` | VFX norueguês (16 endereços de pessoa publicados) | **serviços de produção e rental** — câmera, som, grading, estúdio. Zero arte de personagem |

**`juras3d.com` está MORTO, e isso quase virou endereço falso nesta ficha.** A busca oferece
`juras.rodionovas@juras3d.com` como se fosse endereço publicado. `dns.google/resolve` responde
**`"Status":3`, NXDOMAIN**, e o `curl` devolve `CONNECT tunnel failed 502`. **Antes de usar
endereço de site pessoal que veio de resumo de busca, resolva o domínio.**

**O que ficou NÃO CONFERIDO, com essas palavras:**

- `triumphstudios.com`, `forcefieldvr.com`, `codeglue.com` e `bugbear.fi` devolveram **000** (o
  túnel de saída não resolveu), com e sem `www`. **NÃO CONFERIDO**, não é casa sem site.
- `www.mobygames.com` e `magazine.artstation.com` devolveram **403**. Os créditos do MobyGames e os
  *art blasts* da ArtStation seriam a melhor fonte de nome+cargo pareados da rodada.
  **NÃO CONFERIDO.**
- `funcom.com/careers` responde 200 mas escreve **"Loading vacancies..."**: a lista é montada por
  JavaScript e o `curl` não a vê. **NÃO CONFERIDO** — não escrever "Funcom sem vaga".
- A busca global do Workable com o termo `character artist` devolveu **HTTP 429**. Os outros três
  termos (`character art`, `creature artist`, `3d character`) responderam 200 e **nenhum acerto em
  escopo** — tudo Bengaluru, Cairo, Amman, Manila e Istambul. O 429 é **NÃO CONFERIDO**.

**Zeros medidos de verdade (200 na mão, corpo lido):**

- **Quadro nacional holandês** (`dutchgamesindustry.nl/jobs`): 119 vagas, 38 casas, **zero de
  personagem**. Confirma a medição de 12/09 com número de hoje.
- **Housemarque** (`boards-api.greenhouse.io/v1/boards/housemarque/jobs`): **3 vagas, as três de
  iluminação**. Zero da disciplina.
- **Sharkmob** (`sharkmob.teamtailor.com/jobs.json`): **5 vagas**, nenhuma de arte. A
  *Lead Character Artist* que a busca ainda mostra no ArtStation **não está no quadro vivo**.
- **Avalanche** (`api.lever.co/v0/postings/avalanchestudios`): **12 vagas, uma de personagem**, que
  é justamente a que o Vini já enviou em 10/09.
- **Fatshark** (`fatshark.teamtailor.com/jobs.json`): **5 vagas, uma de personagem** — o achado da
  rodada.

**Uma via anotada e NÃO gasta, porque a casa já tem pessoa:** o anúncio arquivado de
*Character Art Director* da Guerrilla em `https://gamejobs.co/Character-Art-Director-at-Guerrilla-1412`,
aberto nesta rodada, publica **"contact Dave Benach (Senior Talent Acquisition Business Partner)
through recruitment@guerrilla-games.com"**. É **caixa funcional**, não endereço de pessoa, e a
Guerrilla já tem **Arno Schmitz** como primeira pessoa. Fica registrado como a **segunda e última**
via possível daquela casa, para quem precisar dela.

## RODADA DAS 00h35 DE 14/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Rota desta rodada, na ordem que o maestro pediu:** Holanda primeiro, nórdicos em seguida.
Reconferido nesta rodada, e o número de hoje bate com o de 12 e 13/09:
`https://www.dutchgamesindustry.nl/jobs` responde **200 com 304 KB** e o quadro nacional holandês
**continua sem uma única vaga de personagem** — o que há de arte é 2D Artist, Game Art (stage),
Environmental Artist Internship, Internship Game Artist 2D/3D e um Art Lead contratado. Porta
aberta, prateleira vazia: na Holanda a rota é **carta para pessoa com nome**, e foi o que esta
rodada caçou.

**Dedupe feito na CAIXA, não no arquivo.** As cinco casas abaixo devolveram **ZERO** no Gmail, em
busca por nome de casa, por domínio e por **janela de tempo** (`newer_than:10d` cruzado com os
nomes). As duas únicas coisas que a janela devolveu foram a Digital Rain da Áustria (outra casa,
`office@digitalrain.at`) e a recusa já conhecida da Galaxy Grove.

### Peter Wingaard — **Management, Level Design (cofundador; contato de "Inquiries" do estúdio)** — Rain Games, Bergen, Noruega

- **Email:** peter@rain-games.com · confiança **alta** · **PUBLICADO** · fonte:
  https://rain-games.com/press , aberta nesta rodada. É o presskit() oficial da casa e ele publica,
  na seção **Contact**, três endereços em texto visível: **"Inquiries peter@rain-games.com"**,
  **"Press requests Marion@rain-games.com"** e **"Support support@rain-games.com"**, além do
  **"Press / Business contact: andersson@rain-games.com"** do Factsheet.
- **Por que ELE e não outra pessoa da casa:** a mesma página publica o time inteiro com cargo, e as
  pessoas certas de arte estão lá — **"Ole Ivar Rudi — Art Director"**, **"Aslak Helgesen — Lead
  Artist"** e **"Petter Amland — Artist"**. **Nenhum dos três tem endereço publicado, e nada foi
  montado.** Dos endereços que existem, o do Peter é o único que não é caixa de imprensa nem de
  suporte, e ele é da direção de uma casa pequena, que é exatamente onde o BRIEF-JOE manda ir.
  A carta ganha uma vantagem rara aqui: **o fecho fixo ("if someone else there is the right person
  for this, just point me") tem destinatário com nome e cargo já sabidos**, o Ole Ivar Rudi.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Rain Games is an independent,
  employee-owned game development studio based in Norway. Founded in 2010, the creators at Rain
  Games share a passion for crafting memorable worlds which engage curious players through a sense
  of exploration and discovery."** E, na mesma página, a lista de lançamentos:
  **"the critically acclaimed puzzle platformer Teslagrad, as well as the 3D action-adventure
  World to the West"**. O *World to the West* é o encaixe: ação-aventura 3D com elenco de
  personagens estilizados, que é o portfólio dele.
- **Fora dos EUA?** Sim — Noruega. Entram a linha de realocação e a de patrocínio. Atenção de
  redação: a Noruega **não é União Europeia**, então a frase não deve falar em cidadania da UE.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `rain-games`; o **Gmail devolveu ZERO** para `rain-games OR "Rain Games" OR
  Teslagrad` e zero para `Wingaard`. A única coisa que o Gmail tem com a palavra "rain" é a
  **Digital Rain**, austríaca, que é outra casa. **CASA NOVA para a campanha inteira**, PRIMEIRA
  pessoa.
- **Ressalva honesta, quatro:** (1) o pareamento `peter@` ↔ **Peter Wingaard** é **inferência
  minha**: a página publica o endereço sob o rótulo "Inquiries" e publica um único Peter no time;
  é a leitura óbvia, mas não está escrito lado a lado; (2) **o presskit está velho** — ele fala do
  Girl Genius *"gearing up for their own release later in 2023"*, então nome e cargo podem ter
  mudado, e cargo desatualizado é pior que alvo nenhum; (3) o cargo dele é **gestão e level design,
  não arte** — ele encaminha, não abre portfólio; (4) **não há vaga aberta** e a casa é pequena e
  de capital próprio dos funcionários, o que torna patrocínio de visto a hipótese mais fraca.

### Karlijn Walters — **Lead Graphical Designer (a cadeira de arte da casa)** — Denda Games, Hengelo, Holanda

- **Email:** karlijn@denda.com · confiança **alta** · **PUBLICADO** · fonte:
  https://denda-corporate.com , aberta nesta rodada. O bloco **OUR EXPERTS** publica quatro pessoas
  com nome e cargo, cada uma com o seu `mailto:` no cartão, e os quatro saem no HTML na mesma ordem
  das quatro pessoas: **Jacques Neuvel (Managing Director) → neuvel@denda.com**, **Thomas Veldhuis
  (Director of Business Development) → thomas@denda.com**, **Lennard Mulder (Technical Game
  Producer) → lennard@denda.com** e **Karlijn Walters (Lead Graphical Designer) → karlijn@denda.com**.
- **ARMADILHA DE DOMÍNIO, e ela é a sexta da campanha:** o site é **`denda-corporate.com`** e o
  email é **`@denda.com`**. Qualquer endereço montado sobre o domínio do site teria quicado — é o
  caso Stunlock (`stunlock.com` / `@stunlockstudios.com`), Meindbender (`meindbender.com` /
  `@mindbender.com`) e Apparat. Aqui não houve montagem: o estúdio publicou os dois.
- **Por que ELA e não outra pessoa da casa:** dos quatro nomes publicados, três são gestão,
  desenvolvimento de negócio e produção técnica. **Ela é a única cadeira de arte da casa**, e o
  BRIEF-JOE manda, em casa pequena e média, ir na arte antes do RH e antes do comercial.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"We develop games from idea to release
  with full focus on every detail needed to make it a great success."** e, na descrição do serviço
  de desenvolvimento, **"From high quailty game ports for HTML5, PlayStation, Xbox and Nintendo
  Switch to full work-for-hire activities, we provide you with all your needs."** (o erro de
  digitação em "quailty" é do site deles, e fica aqui como está para quem for conferir a fonte).
  **"full work-for-hire"** é o gancho de verdade: casa que faz trabalho por encomenda é casa que
  precisa de artista por projeto, e aí o problema do patrocínio de visto muda de tamanho.
- **Fora dos EUA?** Sim — Holanda, União Europeia, que é o país de **zero veto escrito** na
  contagem de 12/09 e a rota preferida desta rodada.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `denda`; o **Gmail devolveu ZERO** para `denda OR "Denda Games" OR Walters`, e zero
  também na busca por janela de tempo. **CASA NOVA para a campanha inteira**, PRIMEIRA pessoa.
  Jacques Neuvel fica como **segunda e última** possível.
- **Ressalva honesta, três, e a primeira é séria:** (1) **"Graphical Designer" pode não ser 3D** —
  em casa de porte pequeno esse título costuma cobrir 2D, interface e marketing, e o site não
  mostra nenhum personagem 3D no portfólio; o encaixe é de **casa que terceiriza arte**, não de
  time de personagem; (2) **não há vaga aberta** e o site não tem página de carreiras, então é
  carta de porta; (3) o rodapé do site diz **"© Copyright 2024"**, ou seja a página pode estar
  desatualizada e o cargo dela não foi confirmado por fonte independente hoje.

### Tony Manninen — **CEO (e o endereço que a casa publica para "Business Proposals")** — LudoCraft, Oulu, Finlândia

- **Email:** tony.manninen@ludocraft.com · confiança **alta** · **PUBLICADO** · fonte:
  https://www.ludocraft.com , aberta nesta rodada. O rodapé publica em texto visível, um embaixo do
  outro: **"Drop us a line / Business Proposals / CEO Tony Manninen / tony.manninen@ludocraft.com"**
  e **"Career & Support / marja.kuipers@ludocraft.com"**. São os dois únicos endereços do site, e
  **os dois são de pessoa** — não existe `info@` nem `jobs@` ali.
- **Por que ELE e não outra pessoa da casa:** são **18 pessoas** (o próprio site conta:
  **"2006 LudoCraft Established / 18 LudoCraftians / 218 Projects Completed"**), e o BRIEF-JOE manda
  ir no **fundador** em casa desse tamanho, porque ele responde ele mesmo e não lê checklist. A
  alternativa publicada é a caixa de **Career & Support**, que é o caminho de RH, e o BRIEF-JOE
  coloca o RH por último justamente porque é ele que descarta por causa do visto em cinco segundos.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"LudoCraft is a group of individuals who
  came together to form a team. We usually talk about programmers and graphic artists. But in
  reality we are so much more."** E, sobre o método: **"Games are a media that combine technology,
  psychology, art and interaction into a seamless experience."** A casa também publica que trabalhou
  no **Hill Climb Racing para a Fingersoft** e no **Donald Duck CodeMaster para a Sanoma Kids
  Media** — ou seja **personagem licenciado infantil**, que é onde o estilizado dele compete.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `ludocraft`; o **Gmail devolveu ZERO** para `ludocraft OR LudoCraft OR Manninen`, e
  zero também por janela de tempo. **CASA NOVA para a campanha inteira**, PRIMEIRA pessoa.
  Marja Kuipers (Career & Support) fica como **segunda e última** possível.
- **Ressalva honesta, três:** (1) **a casa não é de entretenimento de personagem** — ela se descreve
  como parceira de *"gamified design and development"* e o portfólio é serious game e gamificação
  para Nokia, para o Parlamento Sámi e para empresas de aquecimento urbano; o encaixe com personagem
  3D é **indireto** e a carta não pode fingir o contrário; (2) o rodapé diz **"© 2021 LudoCraft
  Ltd."**, então o site é antigo e o cargo não foi confirmado hoje por fonte independente —
  o que sustenta a escolha é o critério do BRIEF-JOE de que **fundador não muda de casa**; (3)
  **não há vaga aberta** e não existe página de carreiras: é carta de porta.

### Joost Spek — **Fundador e artista 3D (o estúdio é ele)** — 3Dpicnic, Holanda

- **Email:** joost@3dpicnic.nl · confiança **alta** · **PUBLICADO** · fonte: https://3dpicnic.nl/contact
  (bloco **"Get In Touch — Email: joost@3dpicnic.nl"**, em texto visível) e https://3dpicnic.nl/about ,
  as duas abertas nesta rodada. É o **único endereço do site inteiro**: não existe `info@` nem `hello@`.
- **Por que ELE e não outra pessoa da casa:** não há outra. A página About diz, na primeira pessoa:
  **"I'm Joost Spek, the digital artist behind 3Dpicnic. I've been making 3D work for clients around
  the world for over a decade, from my studio in the Netherlands. The studio is small on purpose: it
  means craft, attention, and direct contact with the person actually doing the work."**
- **Gancho, com a frase do próprio estúdio entre aspas:** **"We work with marketers, creatives and
  producers on animations for social, product visuals and characters."** e, logo abaixo, **"Some
  weeks that means a 3D animation for a social campaign. Other weeks it's a character, a product
  visual, or an AR mural"**. O serviço de animação 3D é descrito assim: **"Social pieces, explainers,
  character work, product films. We try to make every frame feel alive, not just moving."** É um
  estúdio holandês que escreve **"character work"** três vezes na própria página de serviços.
- **Fora dos EUA?** Sim — Holanda, União Europeia.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `3dpicnic`; o **Gmail devolveu ZERO** para `3dpicnic OR picnic`, e zero também por
  janela de tempo. **CASA NOVA para a campanha inteira**, PRIMEIRA e única pessoa possível.
- **Ressalva honesta, e ela é a mais pesada desta rodada:** (1) **é um estúdio de UMA pessoa** —
  ele não tem cadeira para contratar ninguém, e pedir emprego ali seria pedir o que não existe.
  **A única forma honesta desta carta é a do caso Concept Art House**: oferta de **colaboração por
  projeto, remota**, para quando entrar trabalho de personagem que ele não dê conta sozinho. Se a
  carta chegar como candidatura a vaga, ela morre na primeira linha; (2) o portfólio público dele
  pende para **AR e mural**, e ele próprio explica por quê — **"A lot of what we make for brands and
  agencies is white-label, so it can't sit on this page"** —, então não dá para medir quanto de
  personagem existe de fato; (3) não há vaga, não há página de carreiras, e o volume de trabalho de
  um estúdio solo é imprevisível.

### Simon van der Linden — **Cofundador (game design, conceitos)** — Monobanda, Utrecht, Holanda

- **Email:** simon@monobanda.nl · confiança **alta** · **PUBLICADO pelo próprio site**, mas leia a
  ressalva 1 antes de usar · fonte: https://monobanda.nl/contact e https://monobanda.nl/about , as
  duas abertas nesta rodada. O endereço está no bloco de dados estruturados que o site publica em
  todas as páginas, com o nome legal da casa junto:
  `{"legalName":"Monobanda PLAY", ... "email":"simon@monobanda.nl"}`. O nome e o cargo dele saem da
  mesma fonte, na página About: **"Simon van der Linden — Co founder / game design, concepts"**.
- **Por que ELE e não outra pessoa da casa:** a About publica o time inteiro — Rosalie van Velsen
  (Creative Operations Lead), Joanneke Weerdmeester (Behavioural Scientist), **Niki Smit (Co founder
  / game design, visual design / concepts)**, Rian Evers (Project lead) e Jesse van Leeuwen (Coding
  & Development) — e **nenhum outro tem endereço publicado**. Nada foi montado. O Niki Smit, que é
  o lado visual da dupla fundadora, fica como **segunda e última** pessoa possível, e só no dia em
  que aparecer endereço dele publicado.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Monobanda is an award winning studio
  that explores and expands the boundaries of play and interaction."** e, o que de fato abre a porta
  para o Vini: **"We work in hybrid freelance teams where our art is informed, and co-created by
  scientists, psychologists, care professionals and other experts on the broad spectrum of human
  experience."** Casa que monta **time híbrido de freelancers** é casa que contrata artista por
  projeto, e isso contorna o item de checklist que mata a candidatura dele em RH generalista.
- **Fora dos EUA?** Sim — Holanda, União Europeia, a rota preferida da rodada.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `monobanda`; o **Gmail devolveu ZERO** para `monobanda` e para `"van der Linden"`,
  inclusive na busca por janela de tempo. **CASA NOVA para a campanha inteira**, PRIMEIRA pessoa.
- **Ressalva honesta, três:** (1) **o endereço não está escrito ao lado do nome dele.** Ele é o
  endereço de contato que o próprio site publica no bloco de dados estruturados, enquanto o texto
  visível da página de contato mostra `info@monobanda.nl`. **Não é endereço montado** — é o estúdio
  publicando —, mas quem escrever deve saber que `simon@` pode ser uma caixa que ele compartilha, e
  a carta tem que funcionar mesmo se outra pessoa abrir; (2) **o encaixe com personagem 3D é
  indireto**: a casa faz VR, instalação de arte, oficina e intervenção em saúde mental, e o lado de
  design visual é do Niki, não dele; (3) **não há vaga aberta** e o site não tem página de
  carreiras, só um menu **"FOR HIRE"** — é carta de porta. A página de contato publica telefone, que
  **não** foi registrado aqui porque o repositório é público.

### O NEGATIVO DESTA RODADA, escrito para a próxima não refazer

**1. DUAS VAGAS DE PERSONAGEM VIVAS, e as duas estão FECHADAS por veto escrito ou por cadência.**
Varridos por `jobs.json` os **151 slugs de Teamtailor** que o repositório conhece, num passe de
`curl`, filtrando título por personagem, criatura, groom, sculpt, look dev, surfacing e 3D art.
Voltaram **doze acertos em cinco casas**, e o que importa é isto:

| Casa | Vaga | Publicada | Situação medida hoje |
|---|---|---|---|
| **Snowprint Studios** (Estocolmo) | **Senior 3D Character Artist** | 08/09 | **VETO ESCRITO**, lido na fonte: *"You are currently located in Stockholm, Sweden. We are unable to support relocation for this position."* |
| **Kepler Interactive / Tactical Adventures** (Paris) | **Lead 3D Character Artist** | 02/09 | anúncio **inteiro em francês**, com o inglês como *nice to have* (*"Vous pratiquez l'anglais professionnel"*). Porta condicionada ao idioma, pela regra da TAT de 11/09. E a casa já recebeu candidatura. |
| Beffio (Poznań, remoto Europa) | Senior Character Artist Unity3D, Lead 3D Character Artist, Senior Character Concept Artist | 2025-2026 | **três candidaturas já enviadas em 06/09**. Quarta aproximação não se faz. |
| Fatshark | Character Artist | 07/08 | já é a ficha de 13/09 |
| Airship Interactive | Character Artist, Groom Artist | 27/08 | quatro registros em `enviados.csv` |

A do Snowprint dói e vale escrever por quê: o corpo do anúncio é o retrato do Vini —
*"You'll create stylized 3D characters and creatures, taking them from sculpting and modelling
through texturing and into Unity"*, *"fluent in ZBrush, Maya, Substance Painter"*, portfólio pedindo
*"Stylized 3D characters with a strong eye for shape, proportions, detail, and visual style"*. O que
fecha é a última linha dos requisitos, e ela é veto de residência, não de habilidade.

**2. DESCOBERTA que vale como veto novo: a Wil Film exige passaporte da UE, por escrito.**
A Wil Film (Copenhague, estúdio de animação CG com pipeline em Maya) publica time inteiro com nome,
cargo e email — inclusive **Toke Uthaug Rasmussen, Head of Modelling**, e dois CG Supervisors — e
parecia a melhor ficha da rodada. A página `https://wilfilm.dk/jobs` mata a casa em uma frase:
**"Apply for an open position ONLY if you are a EU pass holder. Unfortunately, the process and
requirements in order to qualify for a work permit according to the Danish law can be very
complicated."** Isso é veto escrito de autorização, não leitura de contexto. **Nenhuma carta foi
escrita e nenhuma linha entrou.** Fica registrado para ninguém "descobrir" a casa de novo.

**3. As cinco casas que o maestro mandou testar, medidas por `jobs.json` nesta rodada:**
**Kepler Interactive** é a única que vale, e vale pela vaga acima (6 vagas no quadro).
**Opus Major** e **OFM Studios** respondem 200 com **`items: []`**, ou seja quadro vivo e vazio.
**Swift Games** tem uma vaga só, QA Tester em Berlim. **New Moon Production** abre com Unity
Developer. Nenhuma das quatro tem cadeira de arte anunciada hoje.

**4. A varredura mecânica de `mailto:` continua esgotada, e desta vez tem número.**
Foram varridos **cerca de 300 domínios** de Holanda, Suécia, Dinamarca, Noruega, Finlândia, Suíça,
Bélgica, Alemanha, Áustria, Reino Unido e Irlanda, em `/`, `/contact`, `/team`, `/about`, `/people`,
`/studio`, `/jobs`, `/careers`, `/press` e `/presskit`, com decodificação de entidade HTML e de
`data-cfemail`. **Quase todo endereço de pessoa que apareceu já estava na campanha**: Nørlum
(Jericca Cleland, carta em 11/09), Storm Studios (Håvard Munkejord), Milford (Demian Zarins),
Polder Animation (Bastiaan Schravendeel), Aardman (Pauline Mallam), 10 Chambers (robin@, carta em
06/09), Naraven, Qvisten, A. Film. **Isso não é fila seca, é a mesma veia devolvendo o mesmo
minério.** As cinco fichas desta rodada saíram de casas que **nenhuma varredura anterior tinha
aberto**, e as três holandesas saíram de listas fora do gamedevmap.

**5. Mais uma casa morta que parecia ficha pronta:** a **Paladin Studios** (Haia) voltou a aparecer
com `stein@paladinstudios.com` publicado. Ela **fechou em 01/05/2024** e já está registrada assim na
rodada de 13/09. O aviso de encerramento continua no topo do site.

**6. O que ficou NÃO CONFERIDO, com essas palavras:** `postpanic.nl`, `pedrianimation.com`,
`il-luster.nl`, `xform.nl`, `codeglue.com` e `ofm-studios.com` devolvem **000** por este túnel de
saída, com e sem `www`, por `https` e por `http`. **Não é casa sem site.** A `triumphstudios.com`
redireciona para a página da Paradox e a `codeglue.com` para a Behaviour Rotterdam, ou seja as duas
perderam site próprio. A `forcefieldvr.com` só abre por `http` e não publica endereço nenhum.

## RODADA DAS 12h35 DE 14/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Rota desta rodada:** Holanda primeiro, nórdicos e Reino Unido em seguida. A varredura mecânica
de `mailto:` sobre lista de estúdio **continuou esgotada** (ver o negativo no fim desta seção),
e o que rendeu foi uma fonte que nenhuma rodada anterior tinha aberto: **os diretórios de
associação da indústria**, lidos por `curl` — `dutchgamesassociation.nl/members` (116 domínios
holandeses), `animationuk.org/directory` (102 domínios britânicos) e
`ukscreenalliance.co.uk/directory` (105). Das cinco fichas abaixo, quatro saíram de lá.

**Dedupe feito na CAIXA, não no arquivo.** As cinco casas devolveram **ZERO** no Gmail em quatro
buscas diferentes: por nome de casa, por sobrenome da pessoa, por domínio e por **janela de
tempo** (`newer_than:12d` cruzado com animação/estúdio/personagem e com as cidades). E duas
casas que pareciam achado novo morreram justamente aí, no arquivo: **Sir Lancelot** (Daniel
Claesson) e **Troll VFX** (Antti Kulmala) já receberam carta em 09/09 e 11/09.

### James Finlay — **Founder / Creative Director** — Myth Studio, Londres, Reino Unido

- **Email:** james.finlay@mythstudio.co.uk · confiança **alta** · **PUBLICADO** · fonte:
  https://www.mythstudio.co.uk/careers , aberta nesta rodada. O botão **Enquire now** da vaga
  aberta é um `mailto:` com dois destinatários, literal no HTML:
  `mailto:jobs@mythstudio.co.uk,james.finlay@mythstudio.co.uk?subject=MYTH%20STUDIO%20-%203D%20ANIMATORS%20%26%20ARTISTS`,
  e a mesma página traz a âncora `james-finlay#person`. Nome e cargo saem de
  https://www.mythstudio.co.uk/studio , também aberta nesta rodada: **"The Senior Team — James
  Finlay, Founder/Creative Director"**.
- **Por que ELE e não outra pessoa da casa:** o /studio publica seis pessoas — Frankie Evans
  (Head of Production), Danny Prothero (Creative Director), Izzy Hill (Head of Client Success and
  Marketing), Jono Kamester (Head of Animation) e Antonieta Martinez-Hernandez (Senior Producer) —
  e **só dois endereços existem no site**: o dele e o `izzy.hill@`, que é de **novos negócios**.
  Entre o fundador que dirige a parte criativa e a caixa comercial, o BRIEF-JOE manda ir na
  arte. Nada foi montado para as outras quatro pessoas.
- **Gancho, com a frase do próprio estúdio entre aspas:** a vaga aberta diz **"We are looking for
  3D animators and artists to join us on upcoming projects. You will help bring characters,
  worlds, and stories to life across commercials, brand films, and broadcast work, collaborating
  closely with our directors and designers"**, e mais: **"A strong reel matters more than a long
  CV"** e **"We are also open to speculative applications for a full time position."** O estúdio
  se apresenta como **"a small, award-winning animation studio in London"**.
- **Fora dos EUA?** Sim — Reino Unido, que exige patrocínio. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv`, `alvos.csv` e
  `docs/index.html` dão **zero** para `mythstudio` e `Myth Studio` (o único "Finlay" do
  repositório é **Joe Finlayson, da Pixomondo**, outra casa); e o **Gmail devolveu ZERO** para
  `myth OR mythstudio`, para `Finlay`, para `"mythstudio.co.uk"` e na janela de 12 dias.
  **CASA NOVA para a campanha inteira**, PRIMEIRA pessoa. Izzy Hill fica como segunda e última.
- **Ressalva honesta, três:** (1) **a vaga aberta é de ANIMAÇÃO, não de modelagem** — ela pede
  **"Character animation in C4D"** e **"Proficient in C4D Octane"**, e o Vini é modelador de
  personagem, não animador; a carta não pode fingir que a vaga é dele, e o caminho honesto é a
  candidatura espontânea que a própria página convida; (2) o /studio diz que a casa
  **"will always prioritise traditional and handmade techniques"**, com animação quadro a quadro
  e modelo feito à mão, o que reduz o espaço de personagem 3D; (3) o endereço dele está no
  `mailto:` **junto com o `jobs@`**, ou seja é o canal de candidatura da casa e não a caixa
  privada dele — a carta tem que funcionar se o RH abrir antes.

### Dan Dixon — **Cofundador / Executive Producer** — Snafu Pictures, Londres, Reino Unido

- **Email:** dan@snafu-pictures.com · confiança **alta** · **PUBLICADO** · fonte:
  https://snafu-pictures.com/team , aberta nesta rodada. A página publica **nove pessoas com nome,
  cargo e endereço**, um embaixo do outro: **"Dan Dixon — Co-founder/EP — dan@snafu-pictures.com"**,
  Paul Schleicher (Co-founder/EP), Tony Orsten (Chairman), Ross Main (Production Manager), Natt
  Tapley (Head Writer & Creative Development), Joel Veitch (Creator - Bad Dinosaurs), Joe Burns
  (Head of Story) e mais dois.
- **Por que ELE e não outra pessoa da casa:** dos dois fundadores, é o que vem do lado de
  produção de CG — a bio dele na mesma página diz que produziu **"full CG animation for TV drama,
  games and advertising"** e que trabalhou em **"Axis Studios, Aardman, The Imaginarium, MPC and
  Framestore"**. Não existe diretor de arte nem RH publicado nessa casa; pelo BRIEF-JOE, em casa
  pequena a porta é o fundador, e entre os dois o Dan é quem já contratou artista de CG.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Snafu Pictures is a London based
  Animation Production Company established by Dan Dixon & Paul Schleicher in 2020."** O produto
  atual é personagem: o Joel Veitch está creditado ali como **"Creator - Bad Dinosaurs"**, e a bio
  do Natt Tapley diz que ele é **"our Head Writer and Voice Director on Bad Dinosaurs for
  Netflix"**. Uma série de dinossauro em CG é elenco de criatura estilizada, que é exatamente o
  que o portfólio do Vini entrega.
- **Fora dos EUA?** Sim — Reino Unido. Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv`, `alvos.csv` e
  `docs/index.html` dão **zero** para `snafu` e para `Dixon`; o **Gmail devolveu ZERO** para
  `snafu`, para `"snafu-pictures.com"`, para `"Bad Dinosaurs"` e na janela de 12 dias — e vale
  dizer que a caixa tem carta para muita casa de Londres (Union VFX, Framestore, Untold, Golden
  Wolf, BlueBolt, No Ghost), **nenhuma delas esta**. **CASA NOVA**, PRIMEIRA pessoa. Paul
  Schleicher fica como segunda e última.
- **Ressalva honesta, três:** (1) é **produtora**, não estúdio de execução — quem modela os
  personagens de uma série dela pode ser um estúdio parceiro, e a carta tem que pedir para entrar
  na lista de artistas dos projetos, não vaga de quadro fixo; (2) o cargo dele é **produção
  executiva**, não direção de arte, então ele encaminha mais do que abre portfólio; (3) o site
  **não tem página de carreiras nem vaga publicada** (o menu é só Adult, Family, News, About),
  ou seja é carta de porta.

### Greg Maguire — **Founder / CEO (ex-Creature Supervisor da ILM)** — Humain, Belfast, Reino Unido

- **Email:** greg@humain-studios.com · confiança **alta** · **PUBLICADO**, mas leia a ressalva 3 ·
  fonte: https://humain-studios.com/contact , aberta nesta rodada. O link **"contact us"** da
  página é, literal no HTML, `<a href="mailto:greg@humain-studios.com">contact us.</a>`. Nome e
  cargo saem de https://humain-studios.com/about , também aberta nesta rodada: **"Greg Maguire —
  Founder – CEO"**.
- **Por que ELE e não outra pessoa da casa:** é o único do time com endereço publicado (a página
  de carreiras manda tudo para `careers@humain-studios.com`, caixa funcional), e a bio oficial
  dele é a de um homem de criatura, não de RH: **"He was R&D Supervisor at Lucasfilm Animation
  and a Creature Supervisor at Industrial Light & Magic"**, com passagem por **"Walt Disney
  Feature Animation, Industrial Light & Magic, Lucasfilm Animation and Digital Domain"**, créditos
  em *Harry Potter and the Prisoner of Azkaban*, *Happy Feet* e *Avatar*, e a fundação do curso de
  animação 3D da Ulster University.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"The team at Humain is busy creating
  and perfecting body and facial rigs for leading game and film production studios, but our
  capacity is always expanding."** E a página diz para quem ela é: **"If you are a producer,
  animator, outsource manager or rigger working on a live or planned project..."**. O encaixe é
  de cadeia: quem faz rig facial para casa grande trabalha em cima de malha de personagem, e o
  Vini é quem entrega essa malha — a carta é de artista para artista, e o fecho fixo ("aponte a
  pessoa certa") tem valor extra aqui, porque os clientes dele são justamente as casas grandes.
- **Fora dos EUA?** Sim — Belfast, Reino Unido (HUMAIN Ltd. é registrada lá, conforme a própria
  política de privacidade do site). Entram a linha de realocação e a de patrocínio.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv`, `alvos.csv` e
  `docs/index.html` dão **zero** para `humain` e para `Maguire`; o **Gmail devolveu ZERO** para
  `humain`, para `"humain-studios.com"`, para `Maguire` e na janela de 12 dias. **CASA NOVA**,
  PRIMEIRA pessoa.
- **Ressalva honesta, três, e a primeira é a que mais pesa:** (1) **a casa é de RIGGING**, facial
  e corporal, com framework próprio (EKER) — ela não contrata modelador de personagem, e fingir
  o contrário mata a carta na primeira linha; o pedido honesto é ser lembrado quando um cliente
  precisar de modelagem, ou ser apontado para a casa certa; (2) o time publicado é pequeno e
  internacional (**"our talented people live all over the world"**), o que enfraquece a hipótese
  de patrocínio de visto e sugere trabalho remoto por projeto; (3) o endereço **não está escrito
  ao lado do nome dele** — está atrás do texto "contact us" da página de contato, então é o
  estúdio publicando o endereço dele como canal de entrada, e não uma caixa pessoal.

### Igor Duspara — **Owner and Creative Director** — Studio CAN, Roterdã, Holanda

- **Email:** igor@studiocan.nl · confiança **alta** · **PUBLICADO** · fonte:
  https://studiocan.nl/about , aberta nesta rodada. O bloco de contato do fim da página publica,
  um embaixo do outro, **"Igor Duspara — Owner and Creative Director — igor@studiocan.nl"** e
  **"Jonas Ott — Owner and Creative Producer — jonas@studiocan.nl"**, ao lado do `info@studiocan.nl`
  genérico. (A mesma página publica telefone, que **não** foi registrado aqui porque o repositório
  é público.)
- **Por que ELE e não outra pessoa da casa:** a casa tem duas pessoas e as duas estão publicadas.
  Dos dois donos, ele é o **Creative Director** e o outro é produtor — o BRIEF-JOE manda ir na
  arte antes da produção.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Studio CAN is a Rotterdam-based
  animation studio telling your stories in the most compelling and playful way"** e, o que
  interessa de verdade, **"Our work tends to be playful and lighthearted, character driven and
  narrative, with a hint of silliness thrown in for good measure."** Casa que se define como
  *character driven* é casa que conversa com um portfólio de personagem estilizado.
- **Fora dos EUA?** Sim — Holanda, União Europeia, que é a rota preferida (zero veto escrito de
  autorização na contagem de 12/09).
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv` dão
  **zero** para `studiocan` e para `Duspara`; a única ocorrência de "studio can" em
  `docs/index.html` é coincidência de texto corrido ("...nenhum estúdio can..."), não registro de
  casa. O **Gmail devolveu ZERO** para `studiocan`, `"Studio CAN"`, `"studiocan.nl"`, `Duspara` e
  na janela de 12 dias cruzada com Roterdã. **CASA NOVA**, PRIMEIRA pessoa; Jonas Ott fica como
  segunda e última.
- **Ressalva honesta, e ela é pesada, três:** (1) **o estúdio é 2D**, não 3D — a própria bio dele
  na página diz que ele **"focuses on 2D animation, motion graphics, and drawing"**, e o serviço
  anunciado é videoclipe, motion graphic, explainer e animação de logo; o encaixe com personagem
  3D é **indireto** e a carta não pode fingir o contrário; (2) **são duas pessoas** — não há
  quadro para contratar, e a forma honesta é oferta de colaboração por projeto, como no caso da
  Concept Art House e do 3Dpicnic; (3) **não há vaga aberta nem página de carreiras**, é carta de
  porta.

### Ilari Koskinen — **Animation Director (e Executive Producer da casa)** — Brink Helsinki, Helsinque, Finlândia

- **Email:** ilari@brinkhelsinki.com · confiança **alta** · **PUBLICADO** · fonte:
  https://www.brinkhelsinki.com/team , aberta nesta rodada. O cartão dele traz, no HTML,
  `<h2 class="exad-team-member-name">Ilari Koskinen</h2>` seguido de
  `<span class="exad-team-member-designation">Animation Director</span>` e do
  `<a href="mailto:ilari@brinkhelsinki.com">`. O mesmo cartão aparece de novo na seção **Crew**,
  ali com o cargo **Executive Producer**. (A página publica telefone de cada um, que **não** foi
  registrado aqui porque o repositório é público.)
- **Por que ELE e não outra pessoa da casa:** a página publica **três** Animation Directors —
  Ilari Koskinen, **Petja Salmio** e **Janne Roivainen** — e **só o dele tem endereço**; os
  outros dois não têm e **nada foi montado**. Os demais endereços publicados são do CEO
  (Alexander Seraidaris), de outra produtora executiva (Molla Karjaluoto) e do CFO (Ilpo
  Virtanen). Ele é o único que junta cadeira de direção de arte e poder de produção.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"We are a Helsinki-based creative
  illustration and animation studio, founded in 2011"** e **"Creating lovable characters,
  engaging design, and captivating animations is what thrives us."** É a própria casa dizendo que
  o centro do trabalho dela é criar personagem.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. Entram a linha de realocação e a de
  patrocínio.
- **Dedupe, feito na caixa:** `pessoas.csv`, `enviados.csv`, `processados.csv` e `docs/index.html`
  dão **zero** para `brinkhelsinki`, `Koskinen` e `Seraidaris`; a única ocorrência no repositório
  inteiro é uma linha do `automacao/garimpo-cgstudiomap.csv`, que é lista de garimpo e **não**
  registro de contato. O **Gmail devolveu ZERO** para `brinkhelsinki OR Brink OR Koskinen OR
  Seraidaris`. **CASA NOVA**, PRIMEIRA pessoa; Alexander Seraidaris fica como segunda e última.
- **Ressalva honesta, três, e a primeira é medida:** (1) **a palavra "3D" aparece ZERO vez na
  página de trabalhos deles**, contra duas de "character" — é casa de ilustração e animação, com
  cara de 2D, então o encaixe com personagem 3D é **indireto** e a carta tem que se oferecer como
  quem acrescenta uma disciplina, não como quem responde a uma vaga; (2) o cargo dele é **direção
  de animação**, não direção de arte de personagem; (3) **não há vaga aberta nem página de
  carreiras** no site — é carta de porta.

### Julien Kaspar — **3D Artist do Blender Studio (módulo de Sculpt, Paint & Texture)** — Blender Studio / Blender Foundation, Amsterdã, Holanda — **SEM EMAIL, e o motivo está medido**

- **Email:** **não existe endereço dele publicado** · confiança **sem-email** · fonte do nome e do
  cargo: perfil público dele no Gitea do próprio projeto,
  https://projects.blender.org/api/v1/users/JulienKaspar , lido nesta rodada, que devolve
  `full_name: "Julien Kaspar"` e `description: "3D Artist @ Blender Studio. Sculpt, Paint &
  Texture Module artist"`.
- **Por que ELE, e quem mais existe ali:** o mesmo caminho devolve
  **Andy Goralczyk** (`eyecandy`), com a descrição **"Art Director at Blender HQ, working on Open
  Movies and Blender Studio content. Lighting, modeling, fx and grooming"**, e **Demeter Dzadik**
  (`Mets`), **"the character rigger at Blender Studio"**. É um time de personagem inteiro, numa
  casa holandesa, com nome e cargo publicados pela própria casa.
- **O QUE TRAVA, e é para ninguém repetir o caminho:** o Gitea publica o email dos artistas como
  `NNNN+login@noreply.localhost`, ou seja **anonimizado**. Os sites pessoais deles não ajudam:
  `juliankaspar.com`, `artificial3d.com` e `goralczyk.net` abrem com HTTP 200 e publicam **zero
  endereço**; `julienkaspar.com` devolve **000** neste túnel. `blender.org/jobs`,
  `blender.org/about/jobs` e `studio.blender.org/about` também devolvem zero endereço.
- **O padrão do domínio está provado, e mesmo assim NADA foi montado:** o log de commits do
  próprio Gitea (`/api/v1/repos/blender/blender/commits` e
  `/api/v1/repos/studio/blender-studio-tools/commits`, lidos nesta rodada) devolve **dez endereços
  literais** no formato `primeironome@blender.org` — `bastien@`, `hans@`, `jacques@`, `jeroen@`,
  `philipp@`, `sergey@`, `simon@` (Simon Thommes, tech artist do Studio), `francesco@`, `anna@` e
  `marton@`. Montar `julien@blender.org` ou `andy@blender.org` em cima disso seria exatamente o
  chute que produziu as dezessete devoluções de 07/09. **A linha entra sem email, de propósito.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para Blender e para os nomes; o repositório
  também. **CASA NOVA.**
- **Ressalva honesta:** o Blender Studio é financiado por doação e por assinatura, tem time
  pequeno e contrata pouco; e a disciplina publicada do Julien é escultura e textura dentro do
  desenvolvimento do software, não produção de elenco para cliente.

### O NEGATIVO DESTA RODADA, escrito para a próxima não refazer

**1. A MELHOR FICHA DA RODADA MORREU NA GEOGRAFIA: 3D Sparrow Group.**
`3dsparrow.com/aboutus` publica o time de gestão inteiro com nome, cargo e endereço —
**Oli Bernard (CEO) oli@**, **Debbie MacDonald (Creative Director) debbiemacdonald@**,
**Leo Rakhmanin (Studio Director) leo.rakhmanin@**, **Nick Okorokov (COO) okorokov@** e
**Anna Voronova (Head of Pre-Production) voronova@** — e a casa é de personagem 3D de verdade:
o IP **Booba** é descrito por eles como **"A little creature who explores the world like a child"**,
com **"13 billion views across digital platforms"**. O que mata está em `3dsparrow.com/contacts`,
lido nesta rodada: além da **"UK headquarters"** em Londres, os escritórios são **na Rússia
(Krasnogorsk)** e **em Dubai**. A sede britânica é a entidade; a produção está fora do escopo
geográfico da campanha. **Nenhuma carta foi escrita e nenhuma linha de carta entrou.** Se o
escopo mudar, os cinco endereços já estão mapeados aqui. O `/careers` deles responde 404.

**2. DUAS CASAS QUE PARECIAM ACHADO NOVO JÁ TINHAM CARTA, e as duas vieram da mesma armadilha.**
**Sir Lancelot Animation Studio** (Malmö; Daniel Claesson, 3D/Houdini Artist) recebeu carta em
**09/09**, e **Troll VFX** (Antti Kulmala, EP/CEO) em **11/09**. As duas apareceram na varredura
desta rodada porque o `automacao/garimpo-cgstudiomap.csv` ainda as marca como
`ja_na_campanha=nao`. **Esse campo está desatualizado e não serve de dedupe**: o que vale é
procurar o domínio e o sobrenome em `pessoas.csv` e `enviados.csv`, e depois no Gmail.

**3. A FONTE QUE RENDEU NESTA RODADA: diretório de associação da indústria, lido por `curl`.**
Três abriram e nenhuma tinha sido usada antes:
`dutchgamesassociation.nl/members` (**116 domínios holandeses** depois de tirar escola, banco e
advogado), `animationuk.org/directory` (**102 domínios britânicos**, dos quais **72 inéditos** no
repositório) e `ukscreenalliance.co.uk/directory` (**105**, quase toda casa de pós-produção e
acabamento, pouca arte). Quatro das seis fichas desta rodada saíram daí. **Não abriram:**
`ukie.org.uk/members` (404), `neogames.fi/companies` (404), `gamesdenmark.dk/members` (é uma
imagem PNG), `flandersgamehub.be/studios` (a lista é montada por JavaScript) e
`accessvfx.org/members` (500).

**4. Casas com endereço de pessoa publicado que NÃO viraram ficha, e por quê** (para ninguém
gastar rodada nelas de novo):

| Casa | Endereço publicado | Por que não |
|---|---|---|
| Super Spline Studios (Leamington Spa) | `aron@`, `eoin@`, `james@supersplinestudios.com` | o `/about` publica **dezesseis pessoas e todas são animadoras**; a casa vende animação de jogo, não modelagem |
| Eaglet Films (Londres) | `massimo@eagletfilms.com` (Massimo Fenati, CEO/CCO) | o catálogo é desenho à mão e boneco de tricô (*Froglets* é **"a hand-crafted, puppetry production"**) |
| V+ Animation (Londres) | `vit.nico@vplusanimation.com` | estúdio **2D "powered by artists & AI"** |
| Armchair & Rocket (Belfast) | `stephen@`, `michael@armchairandrocket.com` | os dois nomes aparecem **sem cargo** na página, e cargo desatualizado ou desconhecido é pior que alvo nenhum |
| The Barn Games (Holanda) | cinco endereços de pessoa no `/about-us` | serious game para treinamento corporativo; a única cadeira de arte é "Ontwerper" e não há 3D no portfólio |
| Solid Clouds (Reykjavík) | `stefangun@solidclouds.com` | o endereço é real e publicado, mas **não há página de equipe** para parear nome e cargo |
| Pixomondo | `joe.finlayson@pixomondo.com` (Head of Business Development, PXO Clara) | **Naomi Foakes já recebeu carta em 09/09**; a segunda vaga da casa não se gasta em desenvolvimento de negócio |
| Haymaker VFX | quatro pessoas com nome e cargo | **veto escrito já registrado em 10/09**: *"Only candidates eligible to work within the EU/Europe will be considered"* |

**5. Achado de método que vale repetir: o campo `"recipient"` no JSON da página de vagas.**
É irmão do `recruiter-email` do Teamtailor. Em `solidclouds.com/jobs` o payload traz
`"recipient":"stefangun@solidclouds.com"`, que é o endereço corporativo real que recebe a
candidatura espontânea, e ele **não aparece em lugar nenhum do texto visível**. Vale o `grep` em
toda página de vaga nova.

**6. A varredura mecânica de `mailto:` continua esgotada, agora com o número desta rodada.**
Foram varridos **cerca de 230 domínios novos** (116 holandeses da DGA, 72 britânicos da Animation
UK, mais lotes de Alemanha com `/impressum`, Áustria, Bélgica, Irlanda, Espanha, Polônia, Chéquia,
Hungria, Coreia do Sul e nórdicos), em `/`, `/contact`, `/about`, `/team`, `/jobs`, `/careers`,
`/press` e `/privacy`, com decodificação de entidade HTML e de `data-cfemail`. O que saiu foi
quase só caixa genérica. **O que rendeu foi ler a PÁGINA DE EQUIPE das poucas casas que publicam
cargo ao lado do endereço**, não a varredura em si.

**7. O que ficou NÃO CONFERIDO, com essas palavras:** `sun-creature.com`, `macrograph.co.kr`,
`mofac.com`, `digitalidea.co.kr`, `4thcreativeparty.com` e `julienkaspar.com` devolvem **000**
neste túnel; `axisstudiosgroup.com` devolve **403**; `api.github.com` está **fechado para esta
sessão** ("GitHub access to this repository is not enabled"), o que fecha a via de log de commit
pelo GitHub — a do Gitea do Blender, essa, abriu.

## RODADA DAS 16h30 DE 14/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**A rota pedida foi Holanda primeiro, e a Holanda deu zero nesta rodada. Digo com a palavra
exata: a veia holandesa devolveu nada aproveitável.** O que rendeu foi a Irlanda, que é a
terceira da ordem. O negativo holandês está medido no fim desta seção, com números.

**O ACHADO DE MÉTODO, e ele corrige uma conclusão anterior do próprio repositório.** A rodada de
11/09 já tinha usado `animationireland.com/studios/` e registrou em `processados.csv` que um BFS
pelos **sites dos estúdios** devolveu Revelator, Engine House, Treehouse Republic, ALT Animation,
Sanam e Moetion. **O que ninguém tinha aberto era a PÁGINA DE DETALHE de cada estúdio dentro do
próprio diretório** — `animationireland.com/studios/<slug>/`. Ela publica, num bloco só, **nome,
cargo e email de cada pessoa da direção**, e publica endereço de gente que o site do estúdio não
publica em lugar nenhum. Abri as **47** páginas de detalhe e elas devolveram **mais de 40
endereços de pessoa com cargo**, quase todos inéditos.

**Isso desmente, com prova, uma linha que está gravada no painel da campanha.** O registro de
06/09 em `docs/index.html` diz, literal: *"Aardman, Blue Zoo, Brown Bag, Cartoon Saloon, Boulder,
Kavaleer e Sun Creature também: nenhuma publica nome com email."* Para a **Boulder Media** isso
agora está errado — o diretório da associação publica os dois Creative Directors dela com
endereço. **A frase não estava mentindo: estava medindo o lugar errado.**

**Dedupe feito na CAIXA, não no arquivo.** As sete casas devolveram **ZERO** no Gmail em quatro
buscas diferentes: por nome de casa, por sobrenome da pessoa, por **domínio** e por **janela de
tempo** (`newer_than:30d` cruzado com Dublin/Ireland/Irish/Belfast, e `newer_than:90d` pelos
sobrenomes). E uma casa que parecia achado pronto morreu justamente aí, na caixa: a **Giant
Animation** (Dublin, a única irlandesa com 3D declarado e Creative Director com endereço
publicado, `sean@giant.ie`) **já recebeu carta em 26/08 na caixa `hello@giant.ie` e follow-up em
02/09, sem resposta** — o Gmail devolveu a thread inteira. Não virou ficha.

### Gillian Comerford — **Creative Director** — Boulder Media, Dublin, Irlanda

- **Email:** Gillian.Comerford@bouldermedia.tv · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/boulder-media/ , aberta nesta rodada. O bloco de contato
  traz quatro pessoas com cargo e endereço, um embaixo do outro: **Colm Tyrrell — Head of Studio
  Production — colm.tyrrell@**, **Jenni MacNeaney — Head of Studio Operations — jenni.macneany@**,
  **Paul O'Flanagan — Creative Director** e **Gillian Comerford — Creative Director —
  Gillian.Comerford@**. O cargo dela está confirmado por **segunda fonte independente**, o site da
  própria casa: https://bouldermedia.tv/who-we-are/ , também aberta nesta rodada, publica
  **"Gillian Comerford — Creative Director"** com bio. **NADA foi montado.**
- **Por que ELA e não outra pessoa da casa:** a direção publicada tem duas cadeiras de produção e
  operação (Tyrrell e MacNeaney) e **duas cadeiras criativas de mesmo nível**, Paul O'Flanagan e
  ela. Entre os dois Creative Directors eu escolhi ela **por uma razão medida, não por gosto**: o
  `mailto:` de Paul O'Flanagan **está quebrado no HTML do próprio diretório**. Extraí os `mailto:`
  crus da página e o dele sai truncado como `mailto:Paul.O` — o apóstrofo corta o link. Não dá
  para saber se o endereço real usa apóstrofo reto, apóstrofo curvo ou nenhum, e chutar isso é
  gastar a melhor carta da maior casa de animação da Irlanda num endereço que pode não existir.
  O dela sai inteiro e sem ambiguidade: `mailto:Gillian.Comerford@bouldermedia.tv`. A bio dela
  ainda é a mais próxima do trabalho do Vini: **"She has worked as an Animator, Animation Director
  and Director on a considerable number of award winning series and shorts including works for
  Disney, Cartoon Network, Nickelodeon and most recently Netflix."** Paul O'Flanagan fica como
  **segunda e última** da casa, e só se alguém conseguir o endereço dele de fonte não truncada.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de carreiras publica a missão,
  e ela é sobre personagem: **"To combine our passion, expertise and experience to deliver the
  best animation, breathing life and soul into characters and storytelling"**
  (https://bouldermedia.tv/careers/). A mesma página diz que a casa **"has been creating and
  sharing the best TV shows and movies in 2D and 3D and has a mix of Children's and Adult
  Animation in our portfolio"**, e o Who We Are abre com **"Established in 2000, Boulder Media is
  one of Ireland's largest animation studios."**
- **Fora dos EUA?** Sim — Irlanda, que exige autorização de trabalho. A linha de realocação vale
  inteira.
- **Dedupe, feito na caixa:** `enviados.csv` dá **zero** para Boulder (a casa **nunca recebeu
  carta**); em `docs/index.html` ela existe só como **porta de portal**, com a nota de 02/09
  *"SEM VAGAS... só formulário de contato sem upload e o info@bouldermedia.tv"*; e o **Gmail
  devolveu ZERO** para `boulder`, `bouldermedia`, `Comerford`, `O'Flanagan`, para o domínio
  `"bouldermedia.tv"` e nas janelas de 30 e 90 dias. **PRIMEIRA pessoa da casa.**
- **Ressalva honesta, quatro:** (1) **a visão declarada da casa é 2D** — o Who We Are diz
  **"Our vision is to be both an originator and the best creative animation partner for high end
  2D TV content and features"**; o 3D aparece no diretório da associação (`2D 3D VFX`) e na página
  de carreiras, mas não é o carro-chefe, e a carta não pode fingir que é; (2) **é a maior casa de
  animação da Irlanda**, com estrutura de RH e a frase **"Boulder Media does not accept unsolicited
  pitches or submissions"** no rodapé do formulário — a frase é sobre **pitch de projeto**, não
  sobre candidatura, mas é sinal de casa que filtra; (3) o cargo dela é direção criativa de série
  de TV, **não direção de arte de personagem**, e nenhum chefe de CG aparece publicado; (4) a
  seção VACANCIES da página de carreiras estava **vazia** quando eu abri, então **não há vaga
  aberta** e isto é carta de porta.

### Andrew Hamilton — **Creative Director** — elk.Studios, Dundalk, Irlanda

- **Email:** andrew.hamilton@elkstudios.tv · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/elk-studios/ , aberta nesta rodada. Os `mailto:` crus da
  página são quatro e saem ao lado do nome e do cargo: **Ian Hamilton — Managing Director —
  ian.hamilton@**, **Andrew Hamilton — Creative Director — andrew.hamilton@**, **Brian Gilmore —
  Head of Studio — Brian.gilmore@** e a caixa `info@`. **NADA foi montado.**
- **Por que ELE e não outra pessoa da casa:** dos três publicados, um é gestão (Managing Director)
  e outro é chefia de estúdio; ele é **a única cadeira criativa**, e o BRIEF-JOE manda ir na arte
  antes da gestão e do RH em casa pequena e média. Ian Hamilton fica como segunda e última.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de carreiras **convida
  candidatura espontânea com todas as letras** — **"We're not currently hiring, but we're always
  on the lookout for talented people across animation, production and development. If you think
  you'd be a good fit for Elk, we'd love to hear from you!"**
  (https://www.elkstudios.tv/careers). E a apresentação da casa:
  **"An agile first adapter animation studio producing bold, story-driven work for key partners
  and platforms"**, **"Founded in 2017 by some of Ireland's most experienced animation
  professionals"** e **"Based in Dundalk, Ireland, with a sibling studio in Newry, Northern
  Ireland"** (https://www.elkstudios.tv/).
- **Fora dos EUA?** Sim — Irlanda. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `elkstudios`, e o **Gmail devolveu ZERO** para
  `elkstudios`, `elk.Studios`, `Hamilton`, o domínio `"elkstudios.tv"` e por janela de tempo.
  **CASA NOVA, PRIMEIRA pessoa.** **CUIDADO COM O FALSO AMIGO:** existe uma **ELK Studios sueca**,
  `elk-studios.com`, de jogo de cassino, já registrada em `garimpo-cgstudiomap.csv` como
  `nao_encontrada`. **Não é esta casa** — o domínio certo é `elkstudios.tv`, sem hífen.
- **Ressalva honesta, três:** (1) **não consegui confirmar que a casa faz 3D** — o diretório da
  Animation Ireland deixa o campo de habilidades **vazio** para ela, e a página de trabalhos
  mostra **um único título**, *Gangsta Granny* (48×11', entrega em outubro de 2026, para BBC e
  WDR), sem dizer a técnica; (2) o convite da página de carreiras cita **"animation, production
  and development"** e **não cita modelagem nem arte de personagem**; (3) a casa é de 2017 e
  pequena, com estúdio irmão em Newry, o que enfraquece a hipótese de patrocínio de visto.

### John McDaid — **Creative Director** — Dog Ears, Derry, Reino Unido (Irlanda do Norte)

- **Email:** john@cheersdogears.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/dog-ears/ , aberta nesta rodada. Os `mailto:` crus são três:
  **Fionnuala Deane — Managing Director — fionnuala@**, **John McDaid — Creative Director —
  john@** e a caixa `hello@`. **NADA foi montado.**
- **Por que ELE e não outra pessoa da casa:** só duas pessoas são publicadas, uma de gestão e uma
  criativa. Ele é a criativa. Fionnuala Deane fica como segunda e última.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Dog Ears creates beautiful engaging
  content for children that we would love in our own homes"** e **"We are known for thoughtful
  creative work, made with integrity in collaboration with our partners and super talented crew"**
  (https://cheersdogears.com/). O produto é personagem e está medido: **"Our focus has always been
  on the creation of strong original IP, including Puffin Rock, which we produce with Cartoon
  Saloon"**, e a mesma página diz que **"Our first two seasons were streamed on Netflix for over
  32.9 million hours in 2025"** e que o longa *Puffin Rock and the New Friends* foi
  **"the first animated movie ever made in Northern Ireland"**.
- **Fora dos EUA?** Sim — Reino Unido (Irlanda do Norte), que exige patrocínio. A linha de
  realocação vale inteira. **Atenção: é Reino Unido, não Irlanda** — a carta não pode falar em
  União Europeia.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `cheersdogears`, `Dog Ears` e `McDaid`, e o **Gmail
  devolveu ZERO** para todos eles, para o domínio `"cheersdogears.com"` e nas janelas de 30 e 90
  dias. **CASA NOVA, PRIMEIRA pessoa.**
- **Ressalva honesta, e ela é pesada, três:** (1) **a casa diz que não executa** — a própria
  página afirma **"The Dog Ears team specialise in pre-production and collaboration, developing
  and creating stories with like minded studios worldwide"**, ou seja a produção pesada vai para
  outra casa e não há cadeira de modelagem 3D ali; (2) **as vagas abertas são de storyboard**, não
  de personagem: a página *Work Here!* pede **"Storyboard Supervisor"** e **"Storyboard Artists"**
  para uma série pré-escolar nova, e manda responder para `hello@` — a carta tem de ser de porta e
  não pode fingir encaixe na vaga; (3) *Puffin Rock* é **2D**, e não há sinal de 3D no site.

### Lee McQuade — **Creative Director** — ALT Animation, Bangor, Reino Unido (Irlanda do Norte)

- **Email:** lee@altanimation.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/alt-animation/ , aberta nesta rodada: **Tim Bryans —
  Managing Director — tim@**, **Andrea McQuade — Head of Production — andrea@** e **Lee McQuade —
  Creative Director — lee@**, mais a caixa `info@`. Cargo confirmado por **segunda fonte**, o site
  da própria casa: https://www.altanimation.com/team , também aberta nesta rodada, publica
  **"Lee McQuade — Creative Director"**. **NADA foi montado.**
- **Por que ELE e não outra pessoa da casa:** dos quatro nomes publicados no site (os três acima
  mais Matthew Bradley, Development Producer), ele é **a única cadeira criativa**; os outros são
  gestão, produção e desenvolvimento.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"ALT Animation — Passionately
  providing imaginative and creative work through considered collaboration and efficient
  delivery"** e, no bloco de curtas, **"We pride ourselves on our ability to tell complex stories
  through the art of animation, using vivid imagery and dynamic characters to bring ideas to
  life"** (https://www.altanimation.com/). A casa se apresenta como capaz de **"take on any part
  of the pipeline"**.
- **Fora dos EUA?** Sim — Reino Unido (Irlanda do Norte). Realocação vale, e **não** se fala em UE.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `alvos.csv` e
  `docs/index.html` para `altanimation` e `McQuade`. **A única ocorrência no repositório é uma
  linha de método em `processados.csv` de 11/09**, que registra ter achado "ALT Animation com
  endereço de pessoa publicado" e **nunca transformou isso em ficha nem em carta** — é pendência
  antiga, não duplicata. O **Gmail devolveu ZERO** para `altanimation`, `ALT Animation`, `McQuade`,
  o domínio `"altanimation.com"` e por janela de tempo. **PRIMEIRA pessoa da casa.**
- **Ressalva honesta, três:** (1) **o diretório deixa o campo de habilidades vazio e o site não
  cita 3D em lugar nenhum** — o portfólio visível é *Doodle Girl* (RTÉ Jr, 26×7') e trabalho de
  eLearning para **BBC Bitesize e BBC Teach**, o que puxa para 2D e para conteúdo educativo; (2)
  a casa é **muito pequena**, quatro pessoas publicadas, e vive de fundo público (**"supported
  with funds awarded by the UK Global Screen Fund"**), o que enfraquece muito a hipótese de
  patrocínio de visto; (3) o rodapé do site diz **©2023**, então o quadro de pessoal não foi
  confirmado hoje por fonte independente — o diretório da associação é de 2026 e bate, o que
  ajuda, mas não é o site da casa.

### Veronica Lassenius — **Creative Director e cofundadora** — Pikkukala, Helsinque, Finlândia

- **Email:** veronica@pikkukala.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/pikkukala/ , aberta nesta rodada. A página publica **dois**
  `mailto:`, os dois de pessoa e nenhum de caixa: **Veronica Lassenius — Creative Director —
  veronica@** e **Pablo Jordi — Producer — pablo@**. A condição de cofundadora sai de **segunda
  fonte**, o site da própria casa: https://www.pikkukala.com/about , também aberta nesta rodada —
  **"Founded in Helsinki in 2012 by animation veterans Veronica Lassenius and Pablo Jordi"**.
  **NADA foi montado.**
- **Por que ELA e não outra pessoa da casa:** são só duas pessoas publicadas, os dois fundadores;
  ele é produtor e ela é a direção criativa. O BRIEF-JOE manda ir na arte antes da produção.
  Pablo Jordi fica como segunda e última.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"We love good design, fun characters
  and interesting atmospheres. Our creations stand for values of respect, diversity and
  curiosity"** e **"We are worldbuilders who use animation and interactive entertainment to create
  cool and purposeful universes for everyone"** (https://www.pikkukala.com/about). A home
  acrescenta: **"With studios in Helsinki and Barcelona, we are the partners of choice for
  like-minded companies searching for co-production and high quality animation production
  services"**. O produto atual é personagem e está em plataforma grande: *Royals Next Door* e
  *Samuel*, este último com estreia na Netflix registrada no próprio blog deles.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv` e `alvos.csv`. As duas
  ocorrências no repositório **não são contato**: `portal_only.md` lista a casa como "formulário
  de contato no site, vaga de personagem não conferido" e `caca-sem-ats-1109.md` só registra que
  `pikkukala.eu` responde em `http`. O **Gmail devolveu ZERO** para `pikkukala`, `Lassenius`, o
  domínio `"pikkukala.com"` e por janela de tempo. **PRIMEIRA pessoa da casa.**
- **Ressalva honesta, três:** (1) **não há prova de 3D** — o diretório deixa o campo de
  habilidades vazio e o catálogo deles (*Taste Buddies*, *Royals Next Door*, *Samuel*, *Who Will
  Comfort Toffle?*) é de aparência 2D; o encaixe com personagem 3D é **INDIRETO**; (2) a casa é de
  **coprodução e serviço**, com metade da operação em **Barcelona**, então a cadeira, se existir,
  pode não ser em Helsinque; (3) a única vaga que achei no site deles é **"Senior Storyboard
  artist for Froggie"**, de outubro de 2025, fora da disciplina e velha — a carta é de porta.

### Dale Robinson — **Producer / General Manager** — Treehouse Republic, Dublin, Irlanda

- **Email:** dale@treehouserepublic.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/treehouse-republic/ , aberta nesta rodada. É o **único**
  `mailto:` da página, e sai duas vezes: no bloco de contato da casa e ao lado de
  **"Dale Robinson — Producer/ General Manager"**. **NADA foi montado.**
- **Por que ELE e não outra pessoa da casa:** a mesma página publica **"Graham Holbook — Creative
  Director"**, que seria o alvo preferido pela regra da arte antes da produção — mas dele a casa
  publica **só o Twitter, nenhum endereço**. Montar `graham@` sobre o domínio seria exatamente o
  chute que produziu cinco devoluções em 07/09, e não foi feito. Fica ele, que é o único
  publicado, e **Graham Holbrook fica como segunda e última, se e quando aparecer endereço
  literal dele**. (Registro a grafia: o diretório escreve "Holbook" no nome e "GrahamHolbrook" no
  Twitter — não sei qual das duas é a certa.)
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Established in 2010, Treehouse
  Republic is a creative-led award-winning 2D animation studio, who, having been raised on
  Saturday morning cartoons while searching for the toys in the cereal box, have a strong comedy
  action core that they pour into all their work"**, e a capacidade que interessa:
  **"With the capability to create any part of a production from concept to final output"**
  (https://treehouserepublic.com/).
- **Fora dos EUA?** Sim — Irlanda. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `alvos.csv` e
  `docs/index.html` para `treehouserepublic` e `Dale Robinson` (as ocorrências de "Treehouse" no
  repositório são de outros arquivos e outras casas). Como na ALT, **a única menção é a linha de
  método de 11/09 em `processados.csv`**, que achou a casa e nunca escreveu. O **Gmail devolveu
  ZERO** para `treehouserepublic`, `Treehouse Republic`, `Dale Robinson`, o domínio e a janela de
  tempo. **PRIMEIRA pessoa da casa.**
- **Ressalva honesta, e é a mais dura desta rodada, três:** (1) **a casa se declara 2D na
  primeira linha do próprio site** — o diretório da associação diz `2D 3D VFX`, mas quem manda é a
  casa, e ela diz **"2D animation studio"**; o encaixe com personagem 3D é **fraco e não
  confirmado**; (2) **o alvo é produção, não arte** — ele encaminha, não abre portfólio, e a carta
  precisa pedir o encaminhamento para o Graham Holbrook pelo nome; (3) o catálogo é pré-escolar e
  infantil (*Hey Fuzzy Yellow*, *Atom Town*, *Cozmo & Friends!*, *Hungry Bear Tales*) e não há
  página de vagas — é carta de porta.

### Susan Broe — **Producer e cofundadora** — Wiggleywoo, Dublin, Irlanda

- **Email:** susan@wiggleywoo.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/wiggleywoo/ , aberta nesta rodada: a página publica
  **"Gilly — Director / Writer, Creative Director"** e **"Susan Broe — Producer —
  susan@wiggleywoo.com"**. É o **único** `mailto:` da página. Confirmado por **segunda fonte** no
  site da própria casa: o bloco de dados estruturados de https://www.wiggleywoo.com/ traz
  `"email": "susan@wiggleywoo.com"` com `"contactType": "General Enquiries"`. **NADA foi montado.**
  A página do diretório publica **telefone e endereço residencial**, que **NÃO** foram registrados
  aqui porque o repositório é público.
- **Por que ELA e não outra pessoa da casa:** a casa publica duas pessoas. A outra, "Gilly", é
  Director/Creative Director e seria o alvo preferido — mas **nem nome completo nem endereço dela
  existem publicados**, e não montei nada. Susan Broe é a única com endereço, e é cofundadora.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Wiggleywoo is a Dublin-based studio
  crafting original, character-driven stories for audiences of all ages. From laugh-out-loud kids'
  TV to sharp adult comedy — we bring big personalities to life with bold visuals and a healthy
  dose of Irish spirit"** e **"Crafted in Ireland. Loved Everywhere."** (https://www.wiggleywoo.com/).
  A casa está em produção do primeiro longa: **"We are currently in production on our first
  animated feature film Tea with the Dead"**, e a série *The Day Henry Met* **"has been broadcast
  in 192 countries worldwide including Nick Jr International"**.
- **Fora dos EUA?** Sim — Irlanda. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `wiggleywoo` e `Broe` (o único "Broe" do repositório é uma
  linha de `fila-gamedevmap-europa.csv`, que é lista de garimpo e não registro de contato). O
  **Gmail devolveu ZERO** para `wiggleywoo`, `Broe`, o domínio `"wiggleywoo.com"` e nas janelas de
  30 e 90 dias. **CASA NOVA, PRIMEIRA pessoa.**
- **Ressalva honesta, três:** (1) **o diretório declara a habilidade da casa como `2D` e só** —
  é o rótulo mais restritivo desta rodada inteira, e o encaixe com personagem 3D é **fraco**; (2)
  o cargo dela é **produção**, não arte, e a pessoa de arte da casa não tem nem nome completo
  publicado, então a carta tem de pedir o encaminhamento sem poder citar um nome; (3) a casa é
  **muito pequena** e sem página de carreiras — é carta de porta, e a hipótese de patrocínio de
  visto é fraca.

### JAM Media — Dublin, Irlanda — **três nomes com cargo, ZERO endereço. `sem-email`, e isso vale.**

- **Pessoas, publicadas com cargo em** https://animationireland.com/studios/jam-media/ , aberta
  nesta rodada: **John Rice — CEO / Executive Producer**, **Alan Shannon — CCO / Director** e
  **Mark Cumberton — COO / Producer**.
- **Por que entra sem email:** é, pelo rótulo do próprio diretório, **a casa irlandesa com o
  perfil técnico mais próximo do Vini desta rodada inteira** — o campo de habilidades dela lista
  **`2D 3D After Effects Animation Software Development Flash Games Development Live Action Maya
  Maya Max Puppetry Stop Motion`**. É a única da lista que declara **Maya e Max**.
- **Por que NÃO tem endereço, e o que eu não fiz:** os `mailto:` crus da página do diretório são
  **um só, `info@jammedia.com`**. Nenhuma das três pessoas tem endereço publicado ali nem no site
  da casa. **Existe padrão de domínio plausível nas casas vizinhas** (`nome@dominio` e
  `nome.sobrenome@dominio` aparecem em Boulder, elk, ALT e Dog Ears), **e mesmo assim nada foi
  montado**: padrão de OUTRA casa não prova o padrão desta, e é esse chute que quicou cinco vezes
  em 07/09. A linha entra guardando nome, cargo e estúdio.
- **Dedupe:** `jammedia` só aparece em `backlog-estudios.md`, que é lista de garimpo; o **Gmail
  devolveu ZERO** para `jammedia`, `"jammedia.com"` e `JAM Media`. **Casa nova.**
- **Ressalva:** o alvo certo seria **Alan Shannon (CCO / Director)**, e é dele justamente que
  falta o endereço. Se alguma rodada futura achar o endereço dele publicado em texto, a ficha está
  meio pronta aqui.

### O QUE MORREU NESTA RODADA, com número, para ninguém repetir

**1. A HOLANDA DEU ZERO, e o gasto foi grande.** Varri **385 domínios** de estúdio da Holanda,
Suécia, Dinamarca, Noruega e Finlândia — todos os que as filas `fila-gamedevmap-ch-fi-nl.csv`,
`fila-gamedevmap-se-dk.csv` e `fila-gamedevmap-europa2/3/4.csv` têm e que **ainda não estavam** em
`enviados.csv`, `pessoas.csv`, `processados.csv`, `alvos.csv` ou `docs/index.html` — em sete
caminhos cada (`/`, `/contact`, `/about`, `/team`, `/press`, `/presskit`, `/press-kit`), com
decodificação de entidade HTML e de `data-cfemail`. **Rendimento: 127 linhas de saída e nenhum
alvo aproveitável.** O que apareceu foi **estúdio de uma a três pessoas de jogo indie 2D**
(`martin@soupmasters.com`, `christofer@talemaker.se`, `jussi@platonicpartnership.com`,
`mikael@eldenpixels.com`, `michael@shellander.se`, `magnus@orsakverkan.com`,
`roy@wispfire.com`, `niels@weirdbeard.nl`, `dimme@monkeybizniz.com`,
`sebastianbazelmans@purpleflamestudio.com`), sem nenhum sinal de personagem 3D e sem cargo
publicado. **Não inventei ficha com eles para bater meta.**

**2. Dois falsos amigos custaram leitura e ficam registrados:** `fido.se`, que a fila lista como
estúdio sueco de VFX, **redireciona hoje para a Goodbye Kansas**, que já recebeu carta; e a
**ELK Studios sueca** (`elk-studios.com`, cassino) não tem nada a ver com a **elk.Studios
irlandesa** (`elkstudios.tv`) desta rodada.

**3. A lista de membros da Dutch Games Association não serve mais para endereço de pessoa.**
Reabri `dutchgamesassociation.nl/members`, extraí **171 domínios** e varri os de estúdio: quase
todo site é SPA e devolve **a mesma home em qualquer caminho**, com `info@` e nada mais. O pouco
que era de pessoa (`jord@wantedgamestudio.com`, da Wanted 5 Games de Haarlem — com a **armadilha
de domínio** de sempre, site `wanted5games.com` e email `@wantedgamestudio.com`) **não tem
sobrenome nem cargo publicado**: o site só chama o sujeito de "Jord" e de *"Chief Lunch Officer"*
numa piada. Sem sobrenome e sem cargo **não vira ficha**.

**4. O que ficou NÃO CONFERIDO, com essas palavras:** `finnanimation.fi` (associação finlandesa de
animação), `animationinnorway.no`, `animationinthenetherlands.nl` e `klik.amsterdam` **não abrem
por este túnel de saída** — `connect_rejected` e `ws_closed_mid_exchange`, que é **erro de rede e
não casa sem site**. As três primeiras são exatamente a versão nórdica e holandesa do diretório
que rendeu esta rodada inteira na Irlanda, e **são a primeira coisa a tentar de novo na próxima**,
de preferência por navegador. `www.nfpa.nl` falha na verificação de certificado.

**5. Sobrou fila boa na Irlanda, medida e não usada, para a próxima rodada não recomeçar do
zero.** As páginas de detalhe do diretório ainda têm, com nome, cargo e endereço publicados e
**sem carta na campanha**: **Turnip + Duck** (Colm Tobin MD, Aidan O'Donovan Creative Director),
**Studio 9** (Joe Coveney e John O'Connell, cofundadores), **Paper Panther** (Carol Freeman,
Founder & Director), **Trickshot Films** (Matt Pidgeon, Director), **Pictor** (Aria Ungerer,
Creative Producer / Founder), **Cantilever Media** (Andrew Baker e Andrea Martin, com a
**armadilha de domínio** `cantilever.media` no site e `@cantilevermedia.ie` no email),
**Studio Meala** (Stephan Fagan, MD — e atenção, o nome sai "Stephan" e o endereço sai
`stephen@`), **Flickerpix** (Johnny Schumann, Creative Director), **Sixteen South** (Colin
Williams, Creative Director), **Stiúidio Fia** (Paul McDonnell, CEO, com endereço de **Gmail
pessoal**), **Lazy Sunday** (Artem Vasiliev, CEO), **SANAM** (Aislí Madden, Producer) e
**Monster Entertainment** (Andrew Fitzpatrick, Chairman — mas é **distribuidora**, não estúdio).

---

## RODADA DAS 18h45 DE 14/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Alvo pedido: repetir nos diretórios nórdicos e holandês o achado da rodada das 16h30. Os quatro
diretórios NÃO renderam, e a causa NÃO é a que a rodada anterior registrou.** Ela anotou
`connect_rejected` e `ws_closed_mid_exchange` e concluiu "erro de rede". Reabri os quatro por
**três tubos independentes** (`WebFetch`, `curl` pelo proxy e **DNS-over-HTTPS na resolvedora
pública do Google**) e o veredito é outro, medido e não opinado. Está no bloco "OS QUATRO
DIRETÓRIOS" no fim desta seção. **O que rendeu foi a fila irlandesa que a rodada anterior deixou
apontada, e ela devolveu 7 pessoas novas.**

**O ACHADO DE MÉTODO DESTA RODADA, e ele vale mais que qualquer ficha: PUBLICADO NÃO É
ENTREGÁVEL.** A campanha inteira trata "endereço publicado" como confiança alta e para por aí
(regra medida em 06/09: dos 17 publicados, 16 entregaram). Nesta rodada um endereço **publicado**
no diretório da Animation Ireland, `andrew@cantilevermedia.ie`, está num domínio que **NÃO
EXISTE**: `cantilevermedia.ie` devolve **NXDOMAIN autoritativo do registro `.ie`** em **quatro
tipos de registro** (A, NS, SOA e MX). Se essa carta saísse, quicava. **Passa a haver um segundo
portão, e ele é barato:** antes de gravar um endereço numa ficha, consultar o **MX do domínio**.
Os outros seis domínios desta rodada passaram no portão (`trickshotfilms.com` doteasy,
`turnipandduck.com` e `sixteensouth.tv` Google, `paperowlfilms.com` Outlook, `pictor.ie` Zoho,
`ink-and-light.com` IONOS). **A Cantilever caiu para `sem-email` por causa desse portão, e isso é
o portão funcionando, não fracasso.**

**SEGUNDO ACHADO DE MÉTODO: o campo "Skills in..." do diretório MENTE por omissão.** A rodada
anterior usou esse campo para julgar se a casa faz 3D e descartou várias por ele estar vazio.
**A Trickshot Films tem o campo VAZIO e escreve no corpo da própria página: "We specialize in 3d
characters."** É o encaixe mais direto com o Vini que este diretório inteiro tem, e o campo de
rótulo não sabia disso. Refiz a varredura no **TEXTO** das 44 páginas e não no rótulo, e foi assim
que apareceram Trickshot, Cantilever (longa CGI) e Ink and Light ("mostly with CG animation").

**TERCEIRO, e conserta uma ressalva da rodada das 16h30.** Ela registrou que o `mailto:` de
**Paul O'Flanagan (Creative Director, Boulder Media)** sai truncado como `mailto:Paul.O` porque o
apóstrofo corta o link, e por isso escolheu a Gillian Comerford. **O endereço dele está publicado
inteiro em TEXTO na mesma página**, fora do atributo `href`: `Paul.O'Flanagan@bouldermedia.tv`
(https://animationireland.com/studios/boulder-media/). **NÃO virei ficha dele nesta rodada** — a
Gillian Comerford já é ficha da casa e a carta dela nem saiu ainda; ele fica como **segunda e
última** da Boulder, agora com o endereço resolvido. A lição é a de 12/09 outra vez: **extrair só
`mailto:` perde endereço; tem de ler o texto também.**

### Colin Williams — **Founder e Creative Director** — Sixteen South, Belfast, Reino Unido (Irlanda do Norte)

- **Email:** colin@sixteensouth.tv · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/sixteen-south/ , aberta nesta rodada. No bloco
  `studio_contacts` do HTML ele é **a única pessoa publicada**, e o par nome/cargo/endereço sai
  colado: `<h4>Colin Williams</h4>` + `Creative Director` + `mailto:colin@sixteensouth.tv`. A
  caixa geral da casa é outra (`website@sixteensouth.tv`), então **este é endereço de pessoa, não
  de caixa**. Cargo confirmado por **segunda fonte**, o site da própria casa:
  https://www.sixteensouth.tv/about , também aberta nesta rodada — **"Sixteen South has grown from
  an idea in the head of our founder and Creative Director, Colin Williams"**. **NADA foi
  montado.** MX do domínio conferido: Google.
- **Por que ELE e não outra pessoa da casa:** é a única pessoa que o diretório publica, é o
  fundador e é a cadeira criativa — não há a quem preferir. Não existe aqui o dilema de gestão
  contra arte que apareceu nas outras casas.
- **Gancho, com a frase do próprio estúdio entre aspas, e é o melhor desta rodada:** a página
  About diz que o slate de desenvolvimento entrega **"shows that will be delivered in 2D, 3D,
  hybrid animation, live action and fur"** (https://www.sixteensouth.tv/about). **"fur" é groom**,
  que é exatamente o diferencial de apoio do Vini, e é a primeira casa desta frente inteira a
  escrever a palavra. A mesma página dá o tamanho: **"Founded in 2007, Sixteen South has grown
  from an idea in the head of our founder and Creative Director, Colin Williams to a group that
  currently employs over 100 brilliantly talented people and a solid management team in downtown
  Belfast"**, e a casa se apresenta como **"proudly wholly owned and independent"**. No diretório
  ela mede o próprio catálogo: **"We've made 667 episodes of 15 original series of quality
  television... we've won over 100 international awards, including a BAFTA, two RTS awards, three
  IFTAs, two British Animation Awards, the Prix Jeunesse and two EMMY nominations"**
  (https://animationireland.com/studios/sixteen-south/).
- **Fora dos EUA?** Sim — **Reino Unido (Irlanda do Norte)**, que exige patrocínio. A linha de
  realocação vale inteira. **Atenção: é Reino Unido, não Irlanda** — a carta não pode falar em
  União Europeia.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `sixteensouth` — **nenhum arquivo do repositório cita esta
  casa**. O **Gmail devolveu ZERO** para a busca `sixteensouth OR "Sixteen South" OR "Colin
  Williams"`. **CASA NOVA, PRIMEIRA pessoa.** O ZERO é confiável porque rodei **controle** na
  mesma sessão: a busca `flickerpix OR littlemoonanimation OR kavaleer` devolveu **4 threads** e a
  busca por janela `Ireland OR Irish OR Dublin OR Belfast newer_than:30d` devolveu **9**, então a
  ferramenta estava respondendo e o vazio é vazio de verdade, não falha de parser.
- **Ressalva honesta, três:** (1) **o ofício da casa é 2D** — o carro-chefe *Odo* é descrito por
  eles como **"Premium quality, hand-drawn 2D animation with 3D post lighting"**, e o único título
  em CGI, *The Coop Troop*, é **"being co-produced with our partners Mikros Animation Studio and
  Technocolor in Paris in super-deluxe CGI"**, ou seja **o CGI sai de casa e vai para Paris**; o
  "3D" e o "fur" estão no **slate de desenvolvimento**, que é promessa e não cadeira aberta; (2)
  com mais de 100 pessoas e **"a solid management team"**, é casa com filtro de RH, e escrever
  direto ao fundador pode ser desviado; (3) **não há página de vagas** no site (o menu é HOME,
  ABOUT, MANIFESTO, AWARDS, CONTACT) — **não confirmei vaga aberta** e isto é carta de porta.

### Matt Pidgeon — **Director** — Trickshot Films, Dún Laoghaire (Dublin), Irlanda

- **Email:** matt@trickshotfilms.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/trickshot-films/ , aberta nesta rodada. Conferi no **HTML
  cru** porque o endereço aparece duas vezes: dentro de `<div class="studio_contacts">` sai
  `<h4>Matt Pidgeon</h4> <p class="c_role">Director</p> <p class="email"><a
  href="mailto:matt@trickshotfilms.com">`. **NADA foi montado.** MX do domínio conferido
  (doteasy).
- **Por que ELE e não outra pessoa da casa:** a página publica dois nomes, **Matt Pidgeon
  (Director)** e **Deirdre Griffin (Producer)**, e o BRIEF manda ir na cadeira criativa antes da
  produção. Deirdre Griffin fica como **segunda e última** da casa.
- **Por que ESTA CASA é a melhor desta rodada, e é a frase deles que decide:** **"We specialize in
  3d characters. The design, build and technical aspects that allow them to feel alive in the
  hands of a skilled animator."** (https://animationireland.com/studios/trickshot-films/). É a
  **única casa do diretório inteiro que declara especialização em personagem 3D com essas
  palavras** — não é 3D genérico, é personagem 3D, que é o cargo do Vini.
- **Gancho, com a frase do próprio estúdio entre aspas, e aqui tem dois:** além da de cima, o site
  deles responde na FAQ, com todas as letras, o que o Vini está fazendo — **"Can I send my reel in
  for a spec job application? Yes! Please do share your showreel with us—we may not be able to
  reply to every submission, but we make time to review them carefully, and we'll reach out if
  your work is a fit for our upcoming projects."** (https://www.trickshotfilms.com/, aberta nesta
  rodada). A mesma página abre com **"We bring stories to life with heart and humour"** e diz que
  a casa **"handles every stage of production with craft, care, and precision"** e que **"Our
  pipeline is based on industry standards like OpenColor"** e ACES. **A carta não precisa pedir
  licença: eles convidam o reel por escrito.**
- **Fora dos EUA?** Sim — Irlanda, União Europeia. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `trickshotfilms` — **nenhuma ocorrência no repositório**. O
  **Gmail devolveu ZERO** para `trickshotfilms OR Trickshot OR Pidgeon`. **CASA NOVA, PRIMEIRA
  pessoa.**
- **Ressalva honesta, quatro:** (1) **o endereço dele é TAMBÉM a caixa geral da casa** — o mesmo
  `matt@trickshotfilms.com` aparece no bloco de contato do estúdio e no bloco da pessoa, então
  pode ser lido por mais gente que ele, e a carta deve nomeá-lo na primeira linha para não virar
  correspondência de caixa; (2) **é casa pequena** — só duas pessoas publicadas, e o site não diz
  quantas são no total, o que enfraquece muito a hipótese de patrocínio de visto; (3) o próprio
  site avisa **"we may not be able to reply to every submission"**, então silêncio ali não é
  recusa nem sinal de nada; (4) **não há vaga aberta** — o convite é para reel espontâneo, e o
  site não tem página de vagas; é carta de porta, ainda que de porta aberta.

### Aidan O'Donovan — **Creative Director e cofundador** — Turnip + Duck, Dublin, Irlanda

- **Email:** aidan@turnipandduck.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/turnipandduck/ , aberta nesta rodada. O bloco
  `studio_contacts` publica dois pares nome/cargo/endereço: **Colm Tobin — Managing Director —
  colm@** e **Aidan O'Donovan — Creative Director — aidan@**, mais a caixa `info@`. A condição de
  cofundador sai de **segunda fonte**, o site da própria casa:
  https://turnipandduck.com/about , também aberta nesta rodada — **"Turnip + Duck was set up in
  2016 by Colm Tobin and Aidan O'Donovan"**. **NADA foi montado.** MX conferido (Google).
- **Por que ELE e não outra pessoa da casa:** são dois publicados, um é gestão (Managing Director)
  e ele é a **única cadeira criativa**. Colm Tobin fica como segunda e última.
- **Gancho, com a frase do próprio estúdio entre aspas, e ele é feito sob medida para carta de
  personagem:** a casa lista o que toda produção original dela precisa ter — **"Every T+D Original
  needs five elements; a unique hook, something clever that helps audiences grow, funny
  characters, lots of heart, and of course a killer theme tune!"** E, o que abre a porta de
  verdade: **"Because we are not tied to any particular pipeline, our shows can take whatever
  forms they need to, making us a very co-production friendly studio. In the past we have worked
  with 2D studios, 3D specialists, nature documentarians and puppet builders to bring our ideas to
  life. We love to collaborate!"** (https://animationireland.com/studios/turnipandduck/ e
  https://turnipandduck.com/about). A casa se apresenta como **"an award-winning writer-led
  creator studio based in Dublin, Ireland"** e tem prêmio recente registrado no próprio site
  (**"Kidscreen Award for Best New Series!"**, 12 de março de 2026).
- **Fora dos EUA?** Sim — Irlanda, União Europeia. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html` para `turnipandduck` — **nenhuma ocorrência no repositório**. O
  **Gmail devolveu ZERO** para `turnipandduck OR "Turnip + Duck" OR "Turnip and Duck" OR
  O'Donovan`. **CASA NOVA, PRIMEIRA pessoa.**
- **Ressalva honesta, e é pesada, três:** (1) **a casa não executa 3D, ela contrata quem executa**
  — o catálogo inteiro do site é 2D ou mídia mista (*Maddie + Triggs* 2D, *Critters TV* "2D
  mixed", *Atom Town* "2D Animation", *Brain Freeze* "mixed media"), e o 3D aparece só como
  **parceiro que eles procuram**; a carta tem de ser escrita como oferta a um **parceiro de
  coprodução**, não como candidatura a cadeira interna; (2) eles se declaram **"writer-led"** e
  **"Development Specialists"**, com foco em roteiro, prototipagem e pitch — o peso da casa está
  antes da produção, não na modelagem; (3) é casa de duas pessoas publicadas, então a hipótese de
  patrocínio de visto é fraca, e **não há página de vagas** — carta de porta.

### Gráinne McGuiness — **Creative Director e cofundadora** — Paper Owl Films, Belfast, Reino Unido (Irlanda do Norte)

- **Email:** grainne@paperowlfilms.com · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/paper-owl-films/ , aberta nesta rodada. O bloco
  `studio_contacts` publica três pessoas e **só duas com endereço**: **Gavin Halpin — Managing
  Director — gavin@**, **Gráinne McGuiness — Creative Director — grainne@** e **Stephen Petticrew
  — Head of Post Production — sem endereço**. **NADA foi montado.** MX conferido (Outlook).
- **Por que ELA e não outra pessoa da casa:** dos dois que têm endereço, um é gestão e ela é a
  **cadeira criativa**; e ela é **cofundadora**, dito na mesma página — **"Paper Owl Films Ltd.
  was founded in 2012 by Grainne McGuinness, Stephen Petticrew and Gavin Halpin"**. Gavin Halpin
  fica como segunda e última. **Registro a divergência de grafia, porque ela é do próprio
  diretório:** o bloco de contatos escreve **"Gráinne McGuiness"** (um `n`) e o texto da mesma
  página escreve **"Grainne McGuinness"** (dois `n`, sem acento). **Não sei qual é a certa**, e o
  endereço, que é o que importa, é `grainne@` nas duas leituras.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de carreiras deles convida
  candidatura espontânea por escrito — **"Can I submit a speculative application? Yes. We welcome
  speculative CVs and portfolios at jobs@paperowlfilms.com"** — e ainda diz **"Do you review
  portfolios outside hiring windows? Yes. We keep strong portfolios on file for future
  opportunities"** e **"Some roles require experience; others prioritize strong portfolios and
  creative potential"** (https://paperowlfilms.com/careers, aberta nesta rodada). A missão, da
  home: **"At Paper Owl Films we create award winning content that matters for young audiences,
  opening up new ways of seeing the world and making space for all kinds of minds to be
  represented on screen"** (https://paperowlfilms.com/). O alcance, do diretório: **"Their work is
  enjoyed all over the world on channels such as CBeebies, RTÉjr, TG4, BBC, CBC, NBC Universal,
  Netflix and digital platforms"**.
- **Fora dos EUA?** Sim — **Reino Unido (Irlanda do Norte)**. Realocação vale, e **não** se fala
  em União Europeia.
- **Dedupe, feito na caixa:** **zero em `enviados.csv`** — a casa **nunca recebeu carta**. As três
  ocorrências no repositório **não são contato**: `automacao/caca-sem-ats-1109.md` registra a
  **porta** (`https://paperowlfilms.com/careers`, HTTP 200) e nunca escreveu, e
  `europa-mr-reabertos-07-09.csv` e `processados.csv` são listas de garimpo. O **Gmail devolveu
  ZERO** para `paperowlfilms OR "Paper Owl" OR McGuiness OR McGuinness`. **PRIMEIRA pessoa da
  casa.**
- **Ressalva honesta, e a primeira é séria, quatro:** (1) **a própria FAQ deles impõe a barreira
  de visto** — **"Can international applicants apply? Yes, though you must have the right to work
  in the UK or Ireland"**; isso **não é patrocínio**, é exigência de quem já tem direito, e a
  carta **não pode fingir que não leu isso** — o caso de visto tem de ser feito de frente; (2)
  **não achei sinal de 3D em lugar nenhum** — nem o campo de habilidades do diretório (vazio) nem
  o site citam 3D, CG ou modelagem, e os títulos conhecidos (*Pablo*, *Sol*) são 2D; o encaixe com
  personagem 3D é **fraco**; (3) **o endereço da casa diverge entre as duas fontes** — o diretório
  diz **Holywood, Northern Ireland** e o site da própria casa diz **Belfast**; segui o site, que é a casa falando; (4) o rodapé do site traz **"we do not accept any
  unsolicited materials"**, e embora a FAQ de carreiras convide currículo espontâneo no `jobs@`, a
  contradição existe e o convite é para o `jobs@`, não para a caixa dela.

### Aria Ungerer — **Creative Producer / Founder** — Pictor Productions, Irlanda

- **Email:** aria@pictor.ie · confiança **alta** · **PUBLICADO** · fonte:
  https://animationireland.com/studios/pictor/ , aberta nesta rodada. É a **única pessoa** do
  bloco `studio_contacts` (`<h4>Aria Ungerer</h4>` + `Creative Producer / Founder` +
  `mailto:aria@pictor.ie`) e **não há caixa geral na página**, só o endereço dela. **NADA foi
  montado.** MX conferido (Zoho).
- **Por que ELA e não outra pessoa da casa:** é a única pessoa publicada, e é fundadora e cadeira
  criativa ao mesmo tempo. Não há alternativa nem dilema.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"we are passionate about visual art
  and aim to express that through the medium of animation"**, e o projeto em curso, que é
  personagem puro: **"With the support of the Irish Film Board and Creative Europe MEDIA fund, we
  are currently developing our first TV show, Flix; a comedy about the only dog living in Cat
  Town"**, que é **"an adaptation of the eponymous children's book by world famous, children's
  book author, Tomi Ungerer"**, coproduzido **"with UK production company, Eye Present"**
  (https://animationireland.com/studios/pictor/).
- **Fora dos EUA?** Sim — Irlanda, União Europeia. A linha de realocação vale inteira.
- **Dedupe, feito na caixa:** zero em `pessoas.csv`, `enviados.csv`, `alvos.csv` e
  `processados.csv`. A **única** ocorrência no repositório é uma linha de `docs/index.html` que
  **não é contato**: registra que `pictor.ie` respondeu com **Cloudflare Robot Challenge Screen**
  numa varredura de portas, junto com outros quatro domínios. O **Gmail devolveu ZERO** para
  `"pictor.ie" OR Pictor OR Ungerer`. **PRIMEIRA pessoa da casa.**
- **Ressalva honesta, e esta é a ficha mais fraca da rodada, quatro:** (1) **não abri o site da
  própria casa** — `pictor.ie` está atrás do **Cloudflare Robot Challenge**, registrado no
  repositório em 11/09 e não vencido hoje; **NÃO CONFERIDO** por segunda fonte, então cargo e
  técnica vêm só do diretório; (2) **não há nenhuma prova de 3D** — o campo de habilidades está
  vazio e o texto não cita técnica nenhuma; (3) a casa está **desenvolvendo o primeiro programa**,
  ou seja é pré-produção financiada por fundo, sem pipeline de produção montado e sem cadeira de
  modelagem provável; (4) o **sobrenome dela é o mesmo do autor do livro** que estão adaptando
  (Tomi Ungerer) — pode ser parentesco e pode ser coincidência, **não confirmei**, e a carta **não
  deve especular sobre isso**.

### Andrew Baker — **CEO e cofundador** — Cantilever Media, Dublin, Irlanda — **`sem-email`, e a razão é uma PROVA, não uma falta**

- **Pessoa, publicada com cargo e endereço em** https://animationireland.com/studios/cantilever-media/ ,
  aberta nesta rodada: o bloco `studio_contacts` traz **Andrew Baker — CEO —
  andrew@cantilevermedia.ie** e **Andrea Martin — CEO — andrea@cantilevermedia.ie** (os dois com o
  mesmo título). O texto confirma: **"Founded by Andrew Baker and Andrea Martin, Cantilever Media
  is a Dublin based production company"**.
- **POR QUE O ENDEREÇO NÃO ENTRA, apesar de PUBLICADO:** o domínio `cantilevermedia.ie` **não
  existe**. Consultei a resolvedora pública do Google em **quatro tipos de registro** e todos
  devolveram **`Status: 3` (NXDOMAIN) com autoridade do registro `.ie`** (`a.ns.ie.`): **A, NS,
  SOA e MX**. Como controle, `cantilever.media` — o domínio do **site**, que o diretório publica
  como `/www.cantilever.media` — resolve normalmente (`Status: 0`, A em 198.185.159.145). Ou seja
  **a armadilha de domínio que a rodada anterior anotou como "site `cantilever.media`, email
  `@cantilevermedia.ie`" é pior do que ela pensava: o domínio do email está morto.** Carta enviada
  ali **quica**. A linha entra guardando **nome, cargo e estúdio**, que é o que o BRIEF manda.
- **Por que a casa vale o registro mesmo assim:** é, junto da Trickshot, a casa desta rodada com
  sinal de **CGI de longa-metragem** — **"Our first project, 'The Amazing Maurice' is a CGI
  animated theatrical film based on the award winning book 'The Amazing Maurice and his Educated
  Rodents' by Sir Terry Pratchett, starring Hugh Laurie, Emilia Clarke, David Thewlis, Himesh
  Pate, Gemma Arterton and Hugh Bonneville"**. Longa em CGI com elenco desse porte é exatamente o
  tipo de produção que emprega modelador de personagem.
- **O que eu NÃO fiz:** **não montei** `andrew@cantilever.media` trocando o domínio pelo do site.
  Seria chute, é o chute que quicou cinco vezes em 07/09, e desta vez com um agravante: **o
  domínio do site não publica MX nenhum** (consulta MX em `cantilever.media` devolveu `Status: 0`
  **sem registro MX**), então nem sequer há prova de que aquele domínio receba email.
- **Dedupe, feito na caixa:** as duas ocorrências no repositório são a **nota da própria rodada
  das 16h30** em `PESSOAS-SEM-CARTA.md` e uma linha de método em `processados.csv`; **zero em
  `enviados.csv`**. O **Gmail devolveu ZERO** para `cantilevermedia OR "cantilever.media" OR
  "Cantilever Media"`. **CASA NOVA.**
- **Ressalva:** os **dois** fundadores levam o título de **CEO** no diretório, então **não sei
  qual dos dois é a cadeira criativa** e escolhi o primeiro listado; o site
  `https://www.cantilever.media/` abre (HTTP 200) mas o conteúdo é montado por JavaScript e o
  corpo servido tem só o menu (**About**, **Contact**) — **NÃO CONFERIDO** por segunda fonte; e
  *The Amazing Maurice* é de 2022, então **não é prova de produção viva hoje**.

### Leevi Lemmetty — **Director** — Ink and Light, Irlanda — **`sem-email`, e isso vale**

- **Pessoas, publicadas com cargo em** https://animationireland.com/studios/ink-and-light/ ,
  aberta nesta rodada: o bloco `studio_contacts` traz **Tamsin Lyons — Producer** e **Leevi
  Lemmetty — Director**, e **nenhum dos dois tem endereço**. O único `mailto:` da página é a caixa
  `info@ink-and-light.com`.
- **Por que entra sem email:** é uma das **três** casas desta rodada com sinal explícito de 3D, e
  a frase é da própria casa — **"Ink and Light is a boutique production house creating original
  films and TV series for the international and domestic markets. We work mostly with CG
  animation, but enjoy exploring whatever form fits to tell a great story."** O catálogo publicado
  (*Ollie*, *Hopscotch and the Christmas Tree*, *Harry & Bip*, *Royals Next Door*, *Stories from
  Backwoods*) é de série de personagem.
- **O alvo certo é o Leevi Lemmetty (Director)**, que é a cadeira criativa, e é dele que falta o
  endereço. **Nada foi montado**, embora o padrão `nome@dominio` seja o mais comum nas casas
  vizinhas deste mesmo diretório: padrão de outra casa não prova o padrão desta. O domínio
  `ink-and-light.com` **tem MX vivo** (IONOS), então o dia em que aparecer um endereço literal,
  ele é entregável.
- **Dedupe:** **zero** em todo o repositório para `ink-and-light`, e o **Gmail devolveu ZERO**
  para `"ink-and-light" OR "Ink and Light" OR Lemmetty OR "Tamsin Lyons"`. **CASA NOVA.**
- **Ressalva:** o campo de habilidades do diretório lista **`Stop Motion` e `VFX` e NÃO lista
  3D**, o que contradiz a frase "mostly with CG animation" da mesma página — é o mesmo defeito de
  rótulo que quase fez perder a Trickshot, e quem manda é o texto; **não abri o site
  `www.ink-and-light.com`** nesta rodada, então **NÃO CONFERIDO** por segunda fonte; e *Royals
  Next Door* também aparece no catálogo da **Pikkukala** (ficha da rodada das 16h30), o que sugere
  coprodução entre as duas — **duas cartas sobre o mesmo título**, e o maestro deve saber disso.

### OS QUATRO DIRETÓRIOS: o veredito é MEDIDO, e desmente "erro de rede" em dois dos quatro

A rodada das 16h30 registrou `connect_rejected` e `ws_closed_mid_exchange` nos quatro e concluiu
**erro de rede**. Reabri por três tubos independentes. **Em dois casos não é rede: o domínio não
existe.** A prova é resposta **autoritativa do registro nacional**, que é o juiz final:

| Diretório | DNS (resolvedora pública) | HTTP | Veredito |
|---|---|---|---|
| `finnanimation.fi` | **resolve** (A = 104.247.81.99) | **503** em `http://`, **connection reset** em `https://`, por `WebFetch` **e** por `curl` | **NÃO CONFERIDO** — o site existe e **o servidor dele é que não entrega**. Não é o túnel. |
| `animationinnorway.no` | **`Status: 3` NXDOMAIN**, autoridade `charm.norid.no.` (registro `.no`) | não chega a haver | **O DOMÍNIO NÃO EXISTE.** Não é erro de rede. Não insistir. |
| `animationinthenetherlands.nl` | **`Status: 3` NXDOMAIN**, autoridade `ns1.dns.nl.` / `dns.sidn.nl.` (registro `.nl`) | não chega a haver | **O DOMÍNIO NÃO EXISTE.** Não é erro de rede. Não insistir. |
| `klik.amsterdam` | **`Status: 2` SERVFAIL** — os **cinco** servidores de nome delegados respondem **REFUSED** (*lame delegation*) | não chega a haver | **NÃO CONFERIDO** — o domínio está delegado no registro mas o DNS dele está quebrado **do lado deles**. |

**O que isso muda para a próxima rodada, e economiza o tempo que eu gastei:** **parar de tentar
`animationinnorway.no` e `animationinthenetherlands.nl`** — não são "rede ruim", não existem, e
nenhum navegador vai abri-los. `finnanimation.fi` e `klik.amsterdam` continuam valendo **uma**
tentativa futura, porque a falha ali é de servidor e pode passar. **Não procurei qual seria o
domínio certo da associação norueguesa e da holandesa** — busca na web devolveu só diretórios
comerciais de terceiros (ensun, ProductionHub, GoodFirms), que não publicam cargo com endereço e
não servem para esta frente. **Isso fica aberto e eu digo que fica.**

**Também NÃO abri `/impressum` em casa alemã ou austríaca nenhuma**, que o pedido mencionava: a
rodada foi inteira consumida pelos quatro diretórios e pela fila irlandesa, e não chegou lá.
**NÃO CONFERIDO.**

### O QUE O DEDUPE MATOU, com nome, para ninguém repetir

A fila irlandesa que a rodada anterior deixou apontada tinha nomes que **já receberam carta**, e
só se descobre abrindo `enviados.csv` e a caixa:

- **Flickerpix** (Johnny Schumann, Creative Director) — **carta em 02/09 para
  `jobs@flickerpix.com`** e follow-up em 07/09, os dois na caixa. **FORA.**
- **Little Moon** (3D declarado, o rótulo mais forte do diretório) — **carta em 02/09 para
  `jobs@littlemoonanimation.com`**, e a casa **respondeu** com resposta automática de
  `vanessa+canned.response@littlemoonanimation.com`, que é a **Vanessa Robinson** publicada no
  diretório como Creative Producer. **FORA, e doeu**, porque era a única casa com habilidade
  declarada **`3D` e só**.
- **Piranha Bar** (Epic MegaGrant, **"blending 3D animated characters with live action using the
  Unreal Engine"**) — já em `enviados.csv`. **FORA**, e é a maior perda das três pelo encaixe.
- **Kavaleer**, **Revelator**, **Engine House**, **Moetion Films**, **Brown Bag**, **Giant
  Animation** — todas já em `enviados.csv`. **FORA.**

E o dedupe também **confirmou que o maestro escreveu** as fichas da rodada das 16h30: a caixa
mostra cartas saindo às **17h54 de 14/09** para `john@cheersdogears.com` (Dog Ears),
`susan@wiggleywoo.com` (Wiggleywoo) e Treehouse Republic, esta com **resposta automática de
ausência de Dale Robinson no mesmo minuto** (fora a trabalho, volta dia 15). **Nenhuma dessas
casas pode ser reaberta.**

### A FILA QUE SOBROU, medida e não usada

Ainda com nome, cargo e endereço publicados no diretório, **sem carta e sem ficha**, para a
próxima rodada não recomeçar do zero — **todos com MX a conferir antes de virar ficha**:
**Studio 9** (Joe Coveney e John O'Connell, Co Founders, `joe@`/`john@studio9.ie`, MX Titan — mas
a casa declara **"stop-motion and 2d animation techniques"** e **zero 3D**, encaixe fraco, por
isso ficou fora hoje); **Paper Panther** (Carol Freeman, Founder & Director, `carol@paperpanther.ie`
— **stop-motion de bonecos de feltro e recorte de papel**, encaixe muito fraco com 3D digital);
**Studio Meala** (Stephan Fagan, Managing Director — atenção, o nome sai "Stephan" e o endereço
sai `stephen@studiomeala.com`); **Lazy Sunday** (Artem Vasiliev, CEO); **Stiúidio Fia** (Paul
McDonnell, CEO, endereço de **Gmail pessoal**, e a casa é de **efeitos práticos**: "special
effects, prop making, sculpting, moulding & casting, model making, and puppet fabrication");
**SANAM** (Aislí Madden, Producer, `aisli@sanam.ie`); **Igloo Animations** (Paul Dowling, Producer,
`paul@iglooanimations.com` — e **Julie Rush, Design Lead**, que é a cadeira de arte, mas dela o
diretório publica só a caixa `info@`); **Distillery Films** (Jonathan Clarke, Producer, mas só com
a caixa `info@`); **Boulder Media** (Paul O'Flanagan, Creative Director, endereço resolvido nesta
rodada, **segunda e última** da casa); **Monster Entertainment** (Andrew Fitzpatrick, Chairman —
mas é **distribuidora**, não estúdio).

---

## RODADA HOLANDA + NÓRDICOS, 15/09 03h40 UTC — sete fichas, e a Holanda saiu quase vazia

**O alvo era a Holanda primeiro e os nórdicos em seguida.** O resultado inverteu a ordem: a
Holanda entregou **uma** ficha e ela é `sem-email`; os nórdicos entregaram **seis**. Isso não é
preguiça de busca, é uma parede que já estava medida no repositório e que eu remedi hoje — está
escrita no bloco "A PAREDE HOLANDESA" no fim deste bloco de fichas.

**A fonte que destravou os nórdicos** foi `https://nordicanimation.com/studios-producers/`, um
diretório que publica, para cada casa, **nome da pessoa, telefone e email** — o mesmo formato do
`animationireland.com` que rendeu a rodada irlandesa. **Ele NÃO é descoberta minha:** o
`processados.csv` de 02/09 já registra *"fila do backlog reabastecida com a lista Nordic
Animation: Sagatoon e Fenomen pendentes"*. O que é novo é ter aberto o diretório inteiro nesta
rodada e transformado em ficha o que estava parado há treze dias.

### Erik Wilstrup — **CEO** — Wil Film, Copenhague, Dinamarca

- **Email:** erik@wilfilm.dk · confiança **alta** · **PUBLICADO** pela própria casa · fonte:
  https://www.wilfilm.dk/team , aberta nesta rodada. O bloco "Know the team" traz cinco
  `mailto:` emparelhados com nome e cargo. **NADA foi montado.** **MX conferido:**
  `10 smtp.google.com` (Google Workspace).
- **Por que ELE e não outro da casa:** a página publica cinco pessoas — **Erik Wilstrup (CEO)**,
  Louise Barkholt (Producer), Anne Jørgensen (Business & Legal), Brith Dahl (CFO) e **Jimmi
  Gravesen (Head of Technology)**. A cadeira criativa de verdade, **Peter Hausner (Supervising
  Director)**, aparece na mesma lista **sem endereço nenhum**. Das cinco publicadas, produção,
  jurídico e finanças estão mais longe de personagem do que o fundador que dá nome à casa, e em
  casa desse porte o fundador responde ele mesmo. Por isso Erik.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"WIL FILM is a production company and
  3d animation studio with almost 20 years of experience"** e, no mesmo texto, o catálogo que é
  personagem estilizado puro: **"9 seasons of the outstanding TV series 'Ninjago: Masters of
  Spinjitzu' with 102 episodes and several 'LEGO Star Wars' productions are under our umbrella"**
  (https://www.wilfilm.dk/about). A página de equipe ainda descreve o pipeline: **"WIL FILM's CG
  pipeline is based on Maya animation platform and our talented crew works with NUKE and After
  Effects for image compositing and visual effects."**
- **Fora dos EUA?** Sim — Dinamarca, União Europeia. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `wilfilm OR "Wil Film" OR Wilstrup`
  **e ZERO** para o domínio `"wilfilm.dk"`. No repositório: zero em `pessoas.csv`,
  `enviados.csv`, `processados.csv` e `alvos.csv`. **PRIMEIRA pessoa da casa, e casa inédita na
  campanha.**
- **Ressalva honesta:** (1) ele é **CEO, não a cadeira criativa** — o Supervising Director é o
  Peter Hausner e é dele que a carta gostaria de falar, mas **não montei** `peter@wilfilm.dk` nem
  `peter.hausner@wilfilm.dk`, porque **o domínio usa DOIS padrões ao mesmo tempo** (`erik@` curto
  e `louise.barkholt@`/`anne.jorgensen@`/`brith.dahl@`/`jimmi.gravesen@` longos), e onde há dois
  padrões não há padrão — seria exatamente o chute que quicou cinco vezes em 06/09; (2) *Ninjago*
  terminou em 2022 e o site **não anuncia produção em curso**, então **não há prova de pipeline de
  personagem aberto hoje**; (3) a página `/contact` só tem formulário, e `/team` **não está no menu
  principal** (Home, About us, Our work, Contact) — cheguei nela pelo link "Know our team" do
  `/about`, ou seja é página viva mas pouco exposta, e não sei há quanto tempo a lista não é
  atualizada.

### Jørn Kolsrud — Sagatoon, Hamar, Noruega — **a frase de encaixe mais forte da rodada, e o site mais vazio**

- **Email:** jorn@sagatoon.com · confiança **alta** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada. O diretório publica, no
  bloco da Sagatoon, **`Sagatoon, Norway | Jørn Kolsrud | +47 91 51 16 56 | jorn@sagatoon.com |
  http://www.sagatoon.com/`**. **NADA foi montado.** **MX conferido:**
  `mx1/mx2/mx3.mailpod1-osl1.g1i.uniweb.no` (Uniweb, vivo).
- **Por que ELE e não outro da casa:** é a **única pessoa** que o diretório publica para a
  Sagatoon, e a Sagatoon é casa pequena de um produto só. Não há alternativa nem dilema.
- **Gancho, com a frase do próprio estúdio entre aspas, e é a melhor da rodada:** **"The
  company´s main focus is the development and production of 3D CGI feature film animation for a
  global theatrical audience"**, e o que está acontecendo agora: **"We are now in pre-production
  with our new film, Ludolf Lemming at Anger Academy. Our production partner is nGenious in
  Canada"**. O catálogo publicado é **"Troll – The Tale of a Tail (feature, 2018)"**, **"Ludolf
  Lemming at Anger Academy (feature in pre-production)"** e **"Dustbin Heroes (in development)"**.
  Longa em **3D CGI** dito com essas palavras é o encaixe exato do Vini.
- **Fora dos EUA?** Sim — Noruega. **A linha de realocação vale inteira.** (Noruega não é UE, é
  EEE; a frase de patrocínio continua valendo igual.)
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `"sagatoon.com"` e zero para
  `sagatoon OR Kolsrud`. No repositório há **uma** ocorrência e ela **não é contato**: a linha de
  prospecção de 02/09 do `processados.csv` que diz *"fila do backlog reabastecida com a lista
  Nordic Animation: Sagatoon e Fenomen pendentes"*. Ou seja a casa estava **na fila desde 02/09 e
  nunca virou nada**. Zero em `enviados.csv`, `pessoas.csv` e `alvos.csv`. **CASA NOVA.**
- **Ressalva honesta, e são três:** (1) **o cargo dele NÃO é publicado** — o diretório dá nome,
  telefone, email e site, e **nenhum título**; tratar como contato da casa, e a carta **não pode
  chamá-lo de diretor de nada**; (2) **o site da própria casa está praticamente vazio** —
  `https://www.sagatoon.com/` responde **HTTP 200 com 1.963 bytes**, XHTML 1.0 Transitional
  estático, e o corpo inteiro é o título "Sagatoon" e duas letras soltas; `/about` dá **404**.
  Logo **NÃO HÁ SEGUNDA FONTE** e não há prova de casa viva por site; o que sustenta a ficha é o
  MX vivo e o diretório; (3) o único longa **entregue** é de **2018** e o novo está só em
  **pré-produção** com parceiro de produção **no Canadá** (nGenious), então o trabalho de
  personagem pode nem ser feito em Hamar.

### Trine Heidegaard — **dona e produtora** — Pop Up Production, Copenhague, Dinamarca — **email vivo, site que não existe**

- **Email:** trine@popupproduction.dk · confiança **alta** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada:
  **`Pop Up Production, Denmark | Trine Heidegaard | +45 6065 7028 | trine@popupproduction.dk`**.
  **NADA foi montado.** **MX conferido:** `10 popupproduction-dk.mail.protection.outlook.com`
  (Microsoft 365, vivo).
- **Por que ELA e não outra pessoa da casa:** **ela É a casa.** O texto do diretório diz
  **"Pop up Production is located in Copenhagen and owned by Trine Heidegaard an independent
  animation producer with many years of experience in the animation industry"**. Não existe
  segunda pessoa a escolher.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"The mission of Pop Up Production is
  to team up with passionated people and animation studios and develop and produce animated
  feature films"** e **"Trine Heidegaard has produced and co-produced some of the most successful
  feature films in Denmark, recently the Checkered Ninja trilogy"**. O catálogo publicado é de
  longa de personagem em CG: **"Checkered Ninja 3 (feature, 2025)"**, **"Little Allan – The Human
  Antenna (feature, 2022)"**, **"Checkered Ninja 2 (feature, 2021)"**, **"Checkered Ninja
  (feature, 2018)"** e **"The Incredible Story Of The Giant Pear (feature, 2017)"**.
- **Fora dos EUA?** Sim — Dinamarca, União Europeia. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `"popupproduction.dk"` e zero para
  `popupproduction OR "Pop Up Production" OR Heidegaard`. Zero em `pessoas.csv`, `enviados.csv`,
  `processados.csv` e `alvos.csv`. **CASA NOVA.**
- **Ressalva honesta, e a primeira é séria:** (1) **o site da casa NÃO EXISTE.**
  `popupproduction.dk` **não tem registro A** (consulta à resolvedora pública do Google:
  `Status 0` com resposta **vazia**), embora os NS estejam delegados à Cloudflare e o **MX esteja
  vivo no Microsoft 365**. Ou seja: **a caixa recebe, o site não abre.** É o inverso exato da
  armadilha da Cantilever Media de 14/09, e por isso vale escrito: **A record e MX record são
  coisas independentes, e quem decide se a carta chega é o MX.** O próprio diretório, no campo de
  link, não aponta para site nenhum, aponta para um perfil de LinkedIn — o que **confirma** que a
  casa não tem página; (2) por consequência, **NÃO CONFERIDO por segunda fonte**: tudo o que sei
  vem do diretório; (3) ela é **produtora, não cadeira criativa**, e a casa é uma produtora que
  **se junta a estúdios** (*"team up with ... animation studios"*), ou seja **ela não contrata
  modelador diretamente** — a carta aqui é porta e indicação, não vaga.

### Kristine Knudsen — Den Siste Skilling, Bergen, Noruega — **nome publicado, endereço de CAIXA, e um endereço podre na mesma página**

- **Email:** post@densisteskilling.no · confiança **alta** para a entrega, **mas é CAIXA e não
  endereço de pessoa** · fontes, as duas abertas nesta rodada:
  https://nordicanimation.com/studios-producers/ (que publica
  **`Den Siste Skilling, Norway | Kristine Knudsen | +47 48 35 16 38 | post@densisteskilling.no`**)
  e https://www.densisteskilling.no/ , o site da própria casa, cujo rodapé traz
  `post@densisteskilling.no`. **NADA foi montado.** **MX conferido:** `alt2/alt3/alt4.aspmx.l.google.com`
  (Google Workspace, vivo).
- **ARMADILHA MEDIDA, e ela está na própria página da casa:** o HTML de
  `https://www.densisteskilling.no/` contém **DOIS** endereços parecidos —
  `post@densisteskilling.no` e **`post@denissteskilling.no`** (com **dois `s`** em "denis"). O
  segundo é **erro de digitação deles** e é **endereço morto**: consultei a resolvedora pública do
  Google e `denissteskilling.no` devolve **`Status: 3` (NXDOMAIN)** em **A** e em **MX**. **Quem
  copiar o endereço errado da página perde a carta.** O bom é o de **um `s`**.
- **Por que ELA e não outra pessoa da casa:** é a **única** pessoa que qualquer das duas fontes
  nomeia. A casa é boutique e não publica equipe.
- **Gancho, com a frase do próprio estúdio entre aspas:** do site,
  **"Den siste skilling AS is a Norwegian production company based in Bergen. Named after the
  former inn 'The last Shilling', as an inspiration to spend your resources on culture! The
  company specializes in developing and producing animated as well as live action feature films
  and TV series"**; e do diretório, o catálogo que é 3D CG de longa:
  **"A Bergen-based boutique production company founded in 2010, focusing on animated feature
  films. Their track record includes co-productions RICHARD THE STORK & THE MYSTERY OF THE GREAT
  JEWEL (2023) and RICHARD THE STORK (2017). Our current slate includes animated feature
  COCOBANANA, based on a popular audiobook – series, as well as GINGERBREAD TOWN and SANDER`S
  MIDSUMMER"**.
- **Fora dos EUA?** Sim — Noruega. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `"densisteskilling.no"` e zero para
  `densisteskilling OR "Den Siste Skilling" OR Knudsen`. Zero no repositório inteiro. **CASA
  NOVA.**
- **Ressalva honesta:** (1) **o endereço é uma CAIXA `post@`, não o endereço dela** — em casa
  desse tamanho a caixa provavelmente cai no colo dela, mas isso é aposta e não prova, e **não
  montei** `kristine@densisteskilling.no`; a carta deve abrir com o nome dela mesmo indo para a
  caixa; (2) **o cargo dela não é publicado** em nenhuma das duas fontes; (3) a casa é
  **produtora e coprodutora**, não estúdio de produção — *Richard the Stork* foi animado em
  parceiros estrangeiros, então o assento de personagem **não fica em Bergen**; (4) os dois longas
  entregues são de 2017 e 2023 e o resto do slate está em desenvolvimento.

### Anttu Harlin — **cofundador** — Gigglebug Entertainment, Helsinque, Finlândia — **e ela CORRIGE um registro de 05/09**

- **Email:** anttu.harlin@gigglebug.fi · confiança **alta** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada:
  **`Gigglebug Entertainment, Finland | Anttu Harlin | +358 50 575 4862 | anttu.harlin@gigglebug.fi`**.
  **NADA foi montado.** **MX conferido:** `aspmx.l.google.com` e alternativos (Google Workspace).
- **CORREÇÃO DE REGISTRO ANTIGO, e é o motivo principal desta ficha existir:** o
  `processados.csv` de **05/09** registra, sobre doze casas de CH/FI/NL, *"sem NENHUM email
  publicado: Anima Vitae, Gigglebug e Pyjama Films (Finlândia) ... Marcados no backlog para não
  repetir a busca de contato; a via é o ATS"*. **Isso estava certo para o site deles e errado para
  o mundo:** o endereço do cofundador **existe publicado**, só não está em `gigglebug.fi` — está
  no diretório nórdico. A lição de método é grande e vale para as outras onze: **"o site da casa
  não publica" não é o mesmo que "não existe endereço publicado".**
- **Por que ELE e não outro da casa:** os dois fundadores são **Joonas Utti e Anttu Harlin**, e o
  diretório publica **só o do Harlin**. A segunda fonte é a própria casa: o rodapé de
  https://www.gigglebug.tv/about diz **"Gigglebug is an created by Joonas Utti & Anttu Harlin"**
  (o erro de gramática é deles) e lista, ao lado, apenas contatos de **vendas de TV,
  licenciamento e booking de evento** em domínios de terceiros — nenhum de arte.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Gigglebug Entertainment is an
  animation IP studio based in Finland. We create, develop and produce positive children's
  content with multi-platform distribution and global growth potential. Our company's mission is
  to make fun stuff with a purpose!"**, e a origem dos dois, que é o que dá liga com um artista de
  personagem: **"Gigglebug Entertainment was founded in 2013 by Joonas Utti and Anttu Harlin, who
  previously led the animation studio, Anima Boutique Oy, with clients such as Disney, Nokia,
  Veikkaus and Rovio"**.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa, e aqui ele NÃO voltou vazio:** o **Gmail devolveu ZERO** para
  `"gigglebug.fi"` e zero para `Harlin`, **mas devolveu UMA thread** para `gigglebug`: o recibo de
  **27/08** de `sanni.vainio@gigglebug.teamtailor-mail.com`, *"Thank you for your Open
  application! We have now saved your details for future use."* O `enviados.csv` e o
  `processados.csv` confirmam: **a casa já foi abordada uma vez, por Open Application no
  Teamtailor**. Logo esta é a **SEGUNDA porta da mesma casa**, e **Sanni Vainio está FORA dos
  limites** por já ter respondido. Anttu Harlin nunca foi contatado. **Fica sendo a primeira e
  última pessoa nomeada desta casa.**
- **Ressalva honesta, e são três:** (1) **a casa já recebeu uma candidatura espontânea em 27/08 e
  ela foi aceita e arquivada** — a carta precisa **assumir isso**, não fingir primeiro contato, do
  mesmo jeito que a do Tim Remmers assumiu a carta de 06/09; (2) **não há prova de 3D** — o
  catálogo publicado (*Best & Bester*, *Gigglebug*, o negócio com o Milkshake! do Channel 5 e com
  a *101 Dalmatian Street* da Disney) é conteúdo infantil de marca, e a casa se descreve como
  **"animation IP studio"**, que é dona de propriedade intelectual e não necessariamente casa de
  produção com assento de modelagem; (3) `www.gigglebug.fi` **tem certificado que não bate com o
  host** (`SSL: no alternative certificate subject name matches target host name`) e
  `www.gigglebug.tv/about` responde **404** — a frase dos fundadores foi lida no **rodapé da
  página de erro**, que é conteúdo publicado deles mas é lugar frágil.

### Cornelia Boysen — Maipo Film, Oslo, Noruega — **a ficha mais fraca da rodada, e a fraqueza é a técnica**

- **Email:** cornelia@maipo.no · confiança **alta** para a entrega · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada:
  **`Maipo Film, Norway | Cornelia Boysen | +47 91 39 47 18 | cornelia@maipo.no`**. **NADA foi
  montado.** **MX conferido:** `aspmx.l.google.com` (Google Workspace).
- **Por que ELA e não outra pessoa da casa:** é a única pessoa nomeada em qualquer fonte que
  consegui abrir. O site próprio, https://www.maipo.no/ , publica **apenas a caixa**
  `maipo@maipo.no` e **nenhum nome**.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Maipo has produced more than 25 films
  and is one of Scandinavia's leading production companies. Maipo produces animated feature films,
  series, live action family films and award-winning art house flicks"**, e o que é novo:
  **"Rufus, The Sea Serpent Who Couldn't Swim (feature, 2025)"** e **"The Polar Bear Prince
  (feature, 2024)"**.
- **Fora dos EUA?** Sim — Noruega. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `maipo OR Boysen OR "Maipo Film" OR
  nordicanimation`. Zero em `pessoas.csv`, `enviados.csv`, `processados.csv` e `alvos.csv`.
  **CASA NOVA.**
- **Ressalva honesta, e é por isso que eu digo que é a mais fraca das seis com endereço:** (1)
  **a técnica da casa é a errada.** O texto do diretório é explícito: o maior sucesso deles é
  **"the stop motion puppet animation Louis & Luca's Christmas"**, e o catálogo destacado é
  *Hocus Pocus, Alfie Atkins*, *Louis & Luca – The Big Cheese Race* e *Luis & Luca: Mission to the
  Moon*. **Boneco de stop motion não é personagem 3D digital** e o Vini não faz isso; os dois
  títulos recentes (*Rufus*, *The Polar Bear Prince*) **podem** ser CG, mas o diretório **não diz
  a técnica** e eu **não confirmei**; (2) **o cargo dela não é publicado** em nenhuma das duas
  fontes; (3) a Maipo é **produtora**, e produtora grande faz muita coisa que não é animação
  ("live action family films", "art house flicks"), o que dilui ainda mais a chance de haver
  assento de modelagem dentro de casa. **Se o maestro precisar cortar uma carta desta rodada,
  corte esta.**

### Koen Deetman — **cofundador e game director** — KeokeN Interactive, Hoofddorp, Holanda — **`sem-email`, e a razão é uma PROVA**

- **Pessoa, publicada com nome, cargo e biografia pela própria casa** em
  https://keokeninteractive.com/team , aberta nesta rodada. O bloco "Our Founders" traz os dois
  irmãos e distingue os papéis com todas as letras: **"Koen Deetman — Co-founder of KeokeN
  Interactive and an expert in games. He always knows how to connect the right people and to find
  that perfect balance between business and creatives. This innovative mastermind is the game
  director at KeokeN Interactive"**, contra **"Paul Deetman — Co-founder of KeokeN Interactive and
  the award-winning founder of Hunchback specialises in game- and movie trailers"**.
- **POR QUE ELE e não o irmão:** o texto deles mesmo diz que o **game director** é o Koen. O Paul
  é trailer. A cadeira criativa do jogo é a do Koen, e a regra desta rodada é personagem primeiro.
- **POR QUE ENTRA SEM EMAIL, e isto é uma prova e não uma falta:** **o domínio
  `keokeninteractive.com` NÃO PUBLICA MX NENHUM.** Consulta à resolvedora pública do Google:
  **`A` devolve `Status 0` com três endereços** (198.185.159.144, 198.49.23.145, 198.49.23.144 —
  Squarespace), e **`MX` devolve `Status 0` com resposta VAZIA**. Site vivo, correio inexistente.
  Endereço montado ali **quica com certeza**, e por isso **não montei nada**. O único endereço que
  aparece no HTML do site é o **placeholder `user@domain.com`** do formulário, que não é endereço
  de ninguém.
- **A pista que fica aberta, e ela é boa:** o domínio antigo **`keoken.nl` redireciona 301 para
  `keokeninteractive.com`**, mas **continua com MX próprio vivo** (`10 mail.keoken.nl`). Ou seja
  **a casa recebe correio no domínio velho e não no novo.** Isso é pista, **não é endereço**: eu
  **não montei** `koen@keoken.nl`, porque não há um único endereço literal daquele domínio para
  servir de prova de padrão, e padrão sem prova foi o que quicou cinco vezes em 06/09.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Envisioning the game's industry as a
  platform to go beyond traditional gaming and create immersive experiences, KeokeN Interactive
  aim to develop rich and believable worlds that will make you forget your surroundings and push
  the boundaries of your reality"**; e o parágrafo que praticamente escreve a carta sozinho, por
  citar uma casa onde a campanha já tem gente:
  **"Looking up to industry titans like Guerrilla Games, also hailing from the Netherlands, KeokeN
  Interactive quickly became a creative place where extremely talented people express themselves
  into the art of games"**. O catálogo é *Deliver Us The Moon*, *Deliver Us Mars* e, anunciado,
  **"Deliver Us Home is a solitary sci-fi experience where one astronaut works to secure a home
  and new future for humanity"**.
- **Fora dos EUA?** Sim — Holanda, União Europeia. **A linha de realocação vale inteira**, e é o
  país que esta rodada foi mandada abrir.
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `keoken OR Deetman OR "Deliver Us"` e
  **ZERO** para o domínio `"keokeninteractive.com"`. Zero em `pessoas.csv`, `enviados.csv`,
  `processados.csv` e `alvos.csv`. **CASA NOVA.**
- **Ressalva honesta:** (1) **sem MX no domínio do site, não há como entregar carta hoje** — a
  ficha vale pelo nome, pelo cargo e pela casa, esperando endereço literal, exatamente como o
  BRIEF manda; (2) **não abri `/jobs`**, que é a outra porta da casa, nem procurei perfil público
  do Koen fora do site; (3) a trilogia *Deliver Us* é **sci-fi realista de astronauta e ambiente**,
  com pouquíssimo elenco humano — é o encaixe **mais fraco de personagem** entre as sete fichas, e
  o estilizado do Vini não é o que a casa mostra; (4) *Deliver Us Home* está **anunciado** no site
  sem data, então **não é prova de produção viva hoje**.

### A PAREDE HOLANDESA, medida nesta rodada — **a porta está aberta e a prateleira está vazia**

O pedido desta rodada dizia que a Holanda tem **zero veto escrito de visto** e **zero vaga de
personagem**, e que por isso a via é carta para pessoa. **Abri a Holanda e ela entregou UMA
ficha, e sem email.** O motivo não é falta de varredura. É que **estúdio holandês quase não
publica endereço de pessoa**, e os poucos que publicam não são de personagem. Fica medido para
ninguém refazer:

**O que varri, por tubo próprio (raiz + `/contact` + `/team` + `/about` + `/over-ons` + `/press`
+ `/jobs` + `/careers`, e em parte deles também `/presskit`, `/crew`, `/studio`, `/impressum`,
`/colofon`):**

- **Os 51 estúdios holandeses** do `automacao/fila-gamedevmap-ch-fi-nl.csv` (a lista vai só de
  *Abbey Games* a *KeokeN*, porque o arquivo está **truncado em K** — anotado abaixo), **mais 15
  postos à mão** para cobrir o L–Z: Nixxes, Paladin, Ronimo, Triumph, Two Tribes, Total Mayhem,
  Triangle, Grendel, W!Games, IJsfontein, Gamious, KeokeN, Force Field, Vanguard e Sassybot.
- **Cerca de 40 casas de animação e VFX**, colhidas do índice `https://animation31.com/bedrijven/`
  (de onde extraí **199 domínios** do ecossistema holandês) e de busca: PostPanic, Pedri, Anikey,
  KLOMP!, il Luster, Job Joris & Marieke, Studio Smack, Colorbleed, Planet X, Frame Order,
  Ambassadors, GRID VFX, Beeldenfabriek, Foxmountain, The Drawing Room, Tiepes, Lukkien, Jagthund,
  Katananga, Studio Mad, Skelter, Bigfish, Dotolina, 3DHype, Alien Trick, 5AM, Studio Noord,
  Mr Beam, Spotted Bird, Ka-Ching Cartoons, Bewyrd, Manifest Animation e mais.

**O que voltou, e é pouco:**

| Achado | Veredito |
|---|---|
| `stein@paladinstudios.com` — **Stein Damen, Business Development** (https://www.paladinstudios.com/about) | **Publicado e vivo, mas é a cadeira errada.** Biz dev está ainda mais longe de personagem do que produção. Fica no banco, não vira carta. |
| `kela@appelmoes.games` | **Nome completo e cargo NÃO são publicados** — o site só traz o apelido "Kela" e o X `@KelaMakesGames`. Sem nome e sem cargo, não é ficha. |
| `anne@` / `jakob@` / `michiko@` / `Caya@beeldenfabriek.nl` — nomes e cargos publicados | **Arquitetura.** A própria página vende **"2D & 3D Floor Plans"** e "Coordinator Interior". Fora de escopo. |
| `bram@` e `twan@foxmountain.nl` — Bram e Twan van de Vossenberg | **Animação técnica e médica.** O menu deles é "Explanimation, Medische animatie, Technische animatie". Não é personagem. |
| `jiek@drawingroom.nl` — Jiek Weishut, Creative Agent | **Agência de design de marca e produto**, não animação. Fora. |
| `cathleen@` e `chris@tiepes.nl` | **Cargos não publicados**, casa de animação/foto pequena, sem sinal de 3D. |
| KLOMP!, Anikey | **Declaram 2D** com todas as letras: Anikey "specialise in traditional 2D digital animation". Fora da técnica. |
| Pedri Animation | `pedri.nl` responde **HTTP 200 com 604 bytes** de página de domínio parado. **Não há site.** |
| PostPanic | `www.postpanic.nl` **não resolve** (ENOTFOUND) e `postpanic.nl` volta 502 no túnel. **Não abri.** |
| Submarine | **FORA DOS LIMITES: a casa RECUSOU.** Em 27/08 o `studiotalent@submarine.nl` respondeu *"At this time, our open roles require candidates to be based within the Netherlands or Belgium."* Houve troca e o **Milo Cremer Eindhoven, Head of Animation Recruitment**, fechou com *"Happy to stay in touch!"*. **Não reabrir.** |
| il Luster, Studio Smack, Colorbleed, Planet X, Frame Order, Ambassadors, GRID VFX, Nixxes, Abbey, Grendel, Total Mayhem e o resto | **Só caixa** (`info@`, `office@`, `hello@`). O `/contact` da Ambassadors chega a nomear **Maurice (New Business)** e **Maryana (Marketing & PR)**, mas **só o primeiro nome e sem endereço** — não dá ficha. |

**Os diretórios holandeses, com veredito por tubo:**

| Fonte | Resultado | Veredito |
|---|---|---|
| `https://filmcommission.nl/database/animation-studios/animation-studio/` | **HTTP 500**, e `/database/` também **500** | **A base de estúdios de animação da Netherlands Film Commission está QUEBRADA do lado deles.** É o que seria o equivalente holandês do `animationireland.com`. Vale **uma** tentativa futura. |
| `https://dutchgameindustry.directory/` | **HTTP 200**, vivo e completo | **Não serve para esta frente:** abri a ficha de empresa `/company/iceberg` inteira e ela traz vagas, jogos, fundação e localização e **nenhum contato de pessoa**. |
| `https://dutchgamesassociation.nl/` | **HTTP 200** | Lista de membros vive atrás de `/dga-members-area/`. **Sem contato público.** |
| `https://animation31.com/bedrijven/` | **HTTP 200** | **Serve, e foi o que usei** — não publica contato, mas é o índice de domínios do setor. |
| `animationinthenetherlands.nl` | **NXDOMAIN**, medido em 14/09 | **Não existe.** Não retentei, e a rodada de 14/09 já mandou parar. |

**O que isso quer dizer para a próxima rodada holandesa:** a via de **email publicado de pessoa**
está fechada na Holanda por enquanto. O que sobra é (a) `sem-email` com nome e cargo, como a do
Koen Deetman; (b) esperar a base da Film Commission voltar; (c) o ATS, que é a via que o
`processados.csv` de 05/09 já tinha recomendado — **e que continua valendo, com a correção da
ficha da Gigglebug: "o site da casa não publica" não é o mesmo que "não existe endereço
publicado".**

### E a SUÉCIA saiu ZERO, e o motivo também é medido

Das quatro casas nórdicas, a Suécia foi a única sem ficha. Não foi por falta de tentativa:

- **Goodbye Kansas** (Estocolmo), **Important Looking Pirates** e **Sharkmob** (Malmö) — as três
  casas suecas com trabalho de criatura e personagem de verdade — **não publicam endereço de
  pessoa nenhum**. Varri raiz, `/team`, `/about`, `/contact`, `/studio`, `/people`, `/crew` e
  mais: a Goodbye Kansas devolve **`info@goodbyekansas.com` e `info@goodbyekansas.co.uk` em TODAS
  as rotas** (site de página única, toda rota devolve o mesmo HTML), a ILP devolve `info@` e
  `vfx@ilpvfx.com`, e a Sharkmob **não devolve email nenhum**. As três só falam por Teamtailor, e
  **as três já escreveram para o Vini** (`daniel.axelsson@goodbyekansas`,
  `eleonora.matrella@ilpvfx`, `josefina.havik@sharkmob`, todos recibos automáticos de Connect).
- No diretório nórdico, o que a Suécia oferece com nome e endereço é **2D, stop motion ou
  comissionado**: Dockhus (stop motion), LEE Film (2D), BCD Film (2D), Soja (comissionado),
  Allimator (uma pessoa só, e o endereço é `info@`). **Filmic Art**, **Brikk**, **The Chapel
  Films** e **Snowcloud** já estão na campanha.
- **Qvisten Animation está no TETO**: `hedda.toftner@qvisten.no` levou carta em **26/08** com
  follow-up em 02/09, e `rasmus@qvisten.no` levou carta em **03/09**. **Duas pessoas, teto da
  campanha atingido, casa encerrada** — e isso só apareceu porque o dedupe foi feito na caixa; o
  `pessoas.csv` só registrava o Rasmus.

### A FILA QUE SOBROU, medida e não usada

Do `https://nordicanimation.com/studios-producers/`, com **nome e endereço publicados**, sem
ficha e sem carta, para a próxima rodada não recomeçar do zero — **todos com MX a conferir antes
de virar ficha**: **Fridthjof Animation** (DK, Ronnie Fridthjof, `ronnie@fridthjof.com` — longas e
séries infantis; o site é **JavaScript puro** e só serve "This page requires JavaScript", então
não confirmei técnica); **Made By Us** (DK, Katrin Quist-Møller, `kqm@madebyus.dk`); **Sparre
Production** (DK, Irene Sparre, `irene@sparreproduction.dk`); **Fenomen Studios** (NO, Eirik
Smidesang Slåen, `ess@fenomen.no` — **atenção, e isto derruba a linha de 02/09 do
`processados.csv` que a deixou "pendente": abri `fenomen.no` e a casa é de TV, documentário,
podcast, reclame e evento, NÃO é animação**); **Klipp & Lim** (NO, Jøran Wærdahl); **Pink Zebra**
(NO, Ruth Dyson); **LØV Film** (NO, Lillian Løvseth); **Krystallplaneten** (NO, Merete Korsberg);
**Bivrost Film** (NO, Trond Jacobsen); **Kool Produktion** (NO, Frank Mosvold, endereço em
`online.no`, pessoal); **Rainy Day Productions** (NO, dois nomes e caixa `post@`); **Pyjama Films**
(FI, Terhi Väänänen); **Animagency** (FI, Tero Suomela); **Fiilin Good Films** (FI, Juha Fiilin);
**Sun In Eye** (FI, Metsämarja Aittokoski, **2D declarado**); **sleetfleet** (FI, Teemu Leppälä,
**CEO — é o único do diretório inteiro que publica o cargo junto do nome**). **Apparat Studio**
(NO) tem **Eirik Heldal** publicado e é a **segunda e última** possível da casa, já que Kristian
Berg é a primeira — **mas o cargo dele não está em lugar nenhum**: `apparat.no` responde 200 e o
conteúdo é montado por JavaScript, `/about` dá 404, e o nome "Heldal" **não aparece** no HTML
servido.

**Também fica anotado um defeito de arquivo:** `automacao/fila-gamedevmap-ch-fi-nl.csv` tem **51
linhas de Holanda e elas param em "KeokeN Interactive"**, ou seja a colheita do gamedevmap foi
**truncada na letra K** e nunca cobriu L–Z. Quem for refazer a Holanda pelo gamedevmap precisa
saber disso — eu supri o buraco à mão com 15 casas, mas não é a lista completa.

## RODADA DAS 15h35 DE 15/09 — JOE. AGENTE NÃO ESCREVE CARTA (a escrita do Gmail não está nas ferramentas dele).

**Rota pedida: Holanda primeiro, nórdicos depois, Reino Unido e Irlanda por último.** O que esta
rodada mediu: a Holanda continua fechada pela mesma parede de 15/09 03h40 (a base da Netherlands
Film Commission **ainda responde HTTP 500 hoje**, remedida nesta rodada), e a veia que entregou
foi de novo a nórdica — só que desta vez por **página de equipe do próprio estúdio**, não só pelo
diretório. Duas das fichas são a **segunda e última pessoa** de casas que já receberam carta em
11/09 e não responderam, que é exatamente a prioridade que o `BRIEF-JOE.md` manda seguir
(*"priorize quem já recebeu email e não respondeu: o estúdio já foi qualificado, só faltou chegar
em alguém"*) — e as duas vêm com ressalva de **cadência**, porque a primeira carta é de quatro
dias atrás.

### Eirik Heldal — **CEO & Producer** — Apparat Studio, Bergen, Noruega — **segunda e última da casa, e CORRIGE o registro de 14/09**

- **Email:** eirik.heldal@apparat.no · confiança **alta** · **PUBLICADO pela própria casa** ·
  fonte: https://apparat.studio/ , aberta nesta rodada. O rodapé da home traz, em texto visível,
  **"EIRIK HELDAL — CEO & Producer — phone: ... — e-mail: eirik.heldal@apparat.no"**. **NADA foi
  montado.** **MX conferido nesta rodada:** `ASPMX.L.GOOGLE.COM` e alternativos (Google Workspace,
  vivo).
- **CORREÇÃO DE REGISTRO, e é metade do motivo desta ficha existir:** a rodada de 14/09 18h45
  escreveu, sobre a Apparat, que *"Eirik Heldal publicado e é a segunda e última possível da casa,
  mas o cargo dele não está em lugar nenhum: `apparat.no` responde 200 e o conteúdo é montado por
  JavaScript, `/about` dá 404"*. **O cargo está publicado** — só não está em `apparat.no`, está em
  **`apparat.studio`**, que é o domínio do site (a casa separa site e email, armadilha que o
  `processados.csv` de 11/09 já tinha nomeado). É a mesma lição da Gigglebug de hoje de manhã:
  *"o domínio que você abriu não publica"* não é o mesmo que *"não existe publicado"*.
- **Por que ELE e não outro da casa:** a casa tem três pessoas conhecidas e **duas já estão
  mapeadas**: Kristian Berg (director and creative lead) **recebeu a carta em 11/09** e não
  respondeu. Sobra o Eirik, que é **CEO e produtor** — em casa desse porte é quem decide contratar
  e quem distribui trabalho, e o cargo é **complementar** ao do Kristian, que é o caso em que o
  `BRIEF-JOE.md` autoriza duas pessoas na mesma casa.
- **Gancho, com a frase do próprio estúdio entre aspas:** a home diz, na seção de animação,
  **"Character animation for world-class productions. By senior artists."**, e o perfil que a casa
  escreveu para o diretório nórdico completa: **"Located in Bergen, Norway, Apparat Studio is a
  versatile production and animation company known for high-quality work and senior-level
  expertise. We're a strong partner for international productions seeking collaboration and
  co-financing, with a particular focus on character animation"**
  (https://nordicanimation.com/studios-producers/ , aberta nesta rodada). O crédito publicado é
  **"Richard the Stork and the Mystery of the Great Jewel (2023) Animation Studio"**.
- **Fora dos EUA?** Sim — Noruega (EEE). **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu UMA thread** para `apparat.no OR Heldal OR
  "Apparat Studio"`: a carta de **11/09 às 21h26 para `kristian.berg@apparat.no`**, **uma
  mensagem só, sem resposta de ninguém**. `enviados.csv` confirma o mesmo envio. **Zero para
  `eirik.heldal@`.** A casa **não recusou** e o Eirik **nunca foi contatado**.
- **Ressalva honesta, e são três:** (1) **CADÊNCIA** — a casa recebeu carta há **quatro dias**, e
  escrever de novo tão perto é o que o briefing chama de queimar o estúdio; a leitura honesta é
  que esta carta **espere até por volta de 21/09**, e isso é decisão do maestro, não minha;
  (2) a própria carta de 11/09 registra que o site dizia haver **um só artista 3D na casa**, ou
  seja o assento de modelagem aqui é minúsculo e a porta realista é freela e indicação, não vaga;
  (3) Apparat é **produção e animação**, com metade do catálogo em live-action e conteúdo de
  palco (Alan Walker), então "character animation" é animação de movimento e **não prova que
  exista modelagem de personagem dentro de casa**.

### Espen Nordahl — **Head of VFX / VFX Supervisor** — Storm Studios, Oslo, Noruega — **segunda e última da casa**

- **Email:** nordahl@stormstudios.no · confiança **alta** · **PUBLICADO pela própria casa, com
  nome E cargo ao lado** · fonte: https://www.stormstudios.no/ , aberta e lida nesta rodada. O
  bloco `GET IN TOUCH` da **raiz** publica cinco pares de cargo, nome e endereço, e este é um
  deles: **"Head of VFX / VFX Supervisor — Espen Nordahl — nordahl@stormstudios.no"**. **NADA foi
  montado.**
- **Por que ELE e não outro da casa:** dos cinco publicados, dois são produção e negócio (Thomas
  Reppen, CEO / Executive Producer; Jessica-Rose Smith, Studio Manager / VFX Producer) e três são
  arte. O **Head of CG, Håvard Munkejord, já recebeu a carta em 11/09** e não respondeu — ele era
  o alvo certo e continua sendo, mas está gasto. Entre os dois que sobram, o **Head of VFX** manda
  no departamento inteiro e o **VFX Supervisor** (Ivar Rystad) responde por show; então Nordahl é
  a segunda e última pessoa desta casa, como o próprio registro de 10/09 já previa.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Storm Studios is a leading visual
  effects company in Scandinavia, specialising in high-end VFX for the global feature film and
  television industry"**, e a porta que a própria home abre: **"We are always looking for the best
  talents. If you want to be part of a creative team that pushes boundaries of what is possible,
  we would love to hear from you."** (as duas em https://www.stormstudios.no/ , lidas hoje).
- **Fora dos EUA?** Sim — Noruega (EEE). **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu DUAS threads** para `stormstudios OR "Storm
  Studios" OR Munkejord OR Nordahl`, e nenhuma é resposta humana: (a) a carta de **11/09 às
  21h27** para `havard@stormstudios.no`, **uma mensagem só, sem resposta**; (b) o recibo
  automático de **30/08** de `jobs@wix-forms.com`, *"Storm Studios - We have received your job
  application. Thank you!"*, que é o formulário do site e é robô, não pessoa. **Zero para
  `nordahl@`.** A casa **nunca recusou**.
- **Ressalva honesta, e a primeira é a que pode matar a ficha:** (1) **CADÊNCIA, e aqui ela é pior
  que na Apparat** — esta seria a **terceira aproximação em 16 dias** (formulário 30/08, carta
  11/09, esta), e duas delas na mesma semana; a leitura honesta é **segurar até depois de 20/09**,
  e quem decide é o maestro; (2) é **VFX de longa e série**, não animação de personagem
  estilizado: o encaixe existe (criatura e asset moram dentro do CG), mas o portfólio do Vini é
  estilizado e a casa mostra fotorrealismo; (3) o cargo é **Head of VFX**, ou seja o dono do
  departamento inteiro e não especificamente de assets — quem seria o alvo perfeito é o Head of
  CG, e esse já foi.

### Haukur Sigurjónsson — **lidera a produção e o braço sueco da casa (papel publicado; título formal não)** — GunHil, Reykjavík, Islândia — **casa nova**

- **Email:** haukur@gunhil.com · confiança **alta** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada, no bloco da GunHil:
  **`GunHil, Iceland | Haukur Sigurjónsson | haukur@gunhil.com | http://www.gunhil.com/`**.
  **NADA foi montado.** **MX conferido nesta rodada:** `gunhil-com.mail.protection.outlook.com`
  (Microsoft 365, vivo). Telefone existe na fonte e **não é registrado aqui**, por ser dado
  pessoal.
- **Por que ELE e não outro da casa:** a página `/about` do próprio estúdio, aberta hoje, nomeia
  três pessoas e reparte os papéis: **"GunHil is co-founded by Gunnar Karlsson and Hilmar
  Sigurdsson"**, e **"After formation, GunHil was soon joined by Haukur Sigurjonsson to lead
  production and operate our Swedish wing"**. A cadeira criativa é o **Gunnar Karlsson**, que
  *"visually created and co-directed"* o primeiro longa deles — **e ele não tem endereço publicado
  em lugar nenhum que eu tenha aberto**. O Haukur é o único dos três com endereço literal
  publicado, e quem lidera produção é quem sabe onde falta artista.
- **Gancho, com a frase do próprio estúdio entre aspas, e ela prova a técnica:** o `/about` diz
  que a dupla fundadora criou **"'The Lost Little Caterpillar' (2002) which was the first ever CGI
  Animated film made in Iceland"**, e sobre o longa: **"In 2018, GunHil released the animated
  feature film 'Ploey – You Never Fly Alone' to domestic success as well as being sold for
  theatrical distribution in over 70 countries"**, que **"holds the record for most attendees and
  biggest box-office revenue in the world of any Icelandic Film"**. O diretório acrescenta o que
  está aberto agora: **"GunHil has a number of properties at various stages of completion, from
  writing, through development to production"**, com **"Red Waters (feature, in development)"**.
- **Fora dos EUA?** Sim — Islândia (EEE). **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `"gunhil.com"` e zero para
  `tulipop OR gunhil OR tordenfilm OR sleetfleet OR fridthjof` e para `Sigurjonsson`. No
  repositório: **zero ocorrências de `gunhil`** em `pessoas.csv`, `enviados.csv`,
  `processados.csv`, `alvos.csv` e `docs/index.html`. **CASA NOVA, primeira pessoa.**
- **Ressalva honesta, e são quatro:** (1) **o cargo formal dele não é publicado** — o que existe é
  a frase *"to lead production and operate our Swedish wing"*, então a carta pode dizer que ele
  lidera produção, mas **não pode dar a ele um título** que a casa não escreveu; (2) ele opera o
  **braço sueco** e o telefone publicado é **+46**, ou seja pode nem estar em Reykjavík — a casa é
  islandesa, a pessoa talvez não; (3) o site **só publica a caixa `gunhil@gunhil.com`**, e o
  endereço de pessoa vem do diretório, que é fonte de terceiro (embora o texto do perfil seja
  escrito pela própria casa); (4) o único longa **entregue** é de **2018** e o novo está **em
  desenvolvimento**, então **não há prova de pipeline de personagem aberto hoje** — e em 2017 a
  casa foi vendida à Sagafilm e recomprada em 2023, o que é sinal de estrutura pequena e
  intermitente.

### Frank Mosvold — Kool Produktion, Noruega — **casa nova, longa 3D entregue, e o endereço é de provedor**

- **Email:** fmosvold@online.no · confiança **alta para a entrega** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada:
  **`Kool Produktion, Norway | Frank Mosvold | fmosvold@online.no |
  https://www.facebook.com/KoolProduktion/`**. **NADA foi montado.** **MX conferido nesta
  rodada:** `mx1c60/mx2c60/mx3c60/mx4c60.megamailservers.eu` (provedor vivo). Telefone existe na
  fonte e **não é registrado aqui**.
- **Por que ELE e não outro da casa:** é a **única** pessoa que a casa publica, e a casa é de uma
  pessoa só no papel do diretório. Não há dilema.
- **Gancho, com a frase do próprio estúdio entre aspas** (o texto do perfil é escrito pela própria
  casa): **"Kool Produktion AS is a Norwegian production house. The company creates content for
  children on all platforms. Kool Produktion's latest release was the animated feature film Ella
  Bella Bingo (released worldwide 2020). The next animated feature will be The Legend of Magnus
  the Good (currently in development)"**. O catálogo publicado ainda traz **"Ella Bella Bingo
  Racer (game, 2020)"**, ou seja a casa cruza longa e jogo com o mesmo elenco — que é exatamente
  a travessia do portfólio do Vini.
- **Fora dos EUA?** Sim — Noruega (EEE). **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `Mosvold OR "Kool Produktion" OR
  "Ella Bella"`. No repositório: **zero** em `enviados.csv`, `pessoas.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html`. **CASA NOVA.**
- **Ressalva honesta, e são quatro, a terceira é a que mais pesa:** (1) **o cargo dele não é
  publicado** em nenhuma fonte que abri — o diretório dá nome, telefone, email e link, e nenhum
  título; a carta **não pode chamá-lo de nada**; (2) **a casa não tem site**: `koolproduktion.no`
  responde **NXDOMAIN** na resolvedora pública do Google (`Status 3`), e o único link publicado é
  uma página de Facebook, então **não há segunda fonte** nem prova de casa viva por site;
  (3) **o endereço é de provedor de internet** (`online.no`, Telenor), não corporativo — entrega,
  mas é caixa pessoal, e caixa pessoal de produtor recebe menos triagem profissional do que um
  endereço de estúdio; (4) **a técnica não é dita pela casa**: *Ella Bella Bingo* é longa em CG,
  mas o perfil escreve só *"animated feature film"* e **eu não confirmei em fonte oficial quem
  animou**, nem se há qualquer produção em curso além do longa *"in development"*.

### Teemu Leppälä — **CEO** — sleetfleet, Helsinque, Finlândia — **a ficha mais fraca da rodada, e o endereço é CAIXA**

- **Email:** contact@sleetfleet.com · confiança **alta para a entrega, mas é CAIXA e não endereço
  de pessoa** · fontes, as duas abertas nesta rodada:
  https://nordicanimation.com/studios-producers/ , que publica **`sleetfleet, Finland | Teemu
  Leppälä, CEO | contact@sleetfleet.com`** — e é o **único** bloco do diretório inteiro que traz o
  **cargo** junto do nome —, e https://www.sleetfleet.com/ , cujo rodapé repete
  `contact@sleetfleet.com`. **NADA foi montado**, e em particular **não montei** `teemu@` nem
  `teemu.leppala@`, porque não existe um único endereço literal daquele domínio para provar
  padrão. **MX conferido nesta rodada:** `10 mail.sleetfleet.com` (servidor próprio, vivo).
- **Por que ELE e não outro da casa:** o site tem seção `TEAM` e **ela não nomeia ninguém** — só
  descreve o time em bloco (*"Sleetfleets team combines decades of expertise in gaming, creative
  industries, digitalization, education, and marine science"*). O único nome publicado em qualquer
  lugar é o do CEO, e em casa deste tamanho o CEO decide arte por falta de quem mais decida.
- **Gancho, com a frase do próprio estúdio entre aspas:** **"Sleetfleet's vision is to create
  highly valued, beloved, and licensed intellectual properties (IPs), including animated series.
  The Icecube and Icebreaker Snow series, based on the highly anticipated games, provide a
  cohesive experience that spans games, books, animated series, and more. These characters
  champion the mission of saving the Arctic"**, e do perfil no diretório: **"We're excited to
  announce an upcoming animated series starring our charismatic heroes, Ice Cube and Icebreaker
  Snow!"**. É uma casa cujo produto **são dois personagens**, o que dá gancho natural.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `sleetfleet` e zero para `Leppala`.
  No repositório, a **única** ocorrência de `sleetfleet` é a linha da rodada de 15/09 03h40 deste
  mesmo arquivo, que a listou na *fila que sobrou* e **não virou ficha nem carta**. **CASA NOVA.**
- **Ressalva honesta, e é por isso que eu digo que é a mais fraca:** (1) **o endereço é uma caixa
  `contact@`**, o oposto do que o Joe existe para fazer; (2) a casa é **minúscula e é IP, não
  produção** — games, livros e uma série *"in development"*, sem prova de equipe de arte interna
  nem de pipeline 3D; (3) o **cargo vem do diretório**, não do site da casa, e o site **não nomeia
  ninguém**, então se o CEO tiver mudado eu não teria como saber; (4) **se o maestro precisar
  cortar uma carta desta rodada, corte esta.**

### O QUE MORREU NESTA RODADA, com a medição, para ninguém repetir

| Alvo | O que foi medido hoje | Veredito |
|---|---|---|
| **Tulipop Studios (Islândia), Helga Árnadóttir, `helga@tulipop.com`** | Endereço **publicado** no diretório nórdico, **MX vivo** (Google Workspace), casa **nova**, e a dona é cofundadora. **Mas a página de produções da própria casa escreve a técnica:** *"Tulipop Tales, 52 x 7' **2D animated** series ... produced by Tulipop Studios. The production team comprises a strong line-up of Icelandic talent **in partnership with two strong animation studios, The Animation Band in Italy and Amuse Animation in Spain**"*, e *"Tulipop: Magical Seasons is a series of 30 minute high-quality **2D animated** films"* | **FORA DA TÉCNICA.** 2D e ainda por cima animado fora de casa. Não virou ficha, e **não deve ser reaberta** |
| **Fridthjof Animation (Dinamarca), Ronnie Fridthjof, `ronnie@fridthjof.com`** | Endereço publicado, MX vivo (MailChannels), cargo publicado pelo perfil (*"It is run by the experienced and Cannes Film festival winning film producer Ronnie Fridthjof"*). **O que derrubou:** `fridthjof.com` é bundle de JavaScript e serve só *"This page requires JavaScript to display"*, então **não há frase do site**; e o longa de 2025 (*Lotte & Totte: Min første ven*) aparece **produzido pela B-Water Animation Studios**, ou seja **a animação é feita fora** | **FILA, não ficha.** Sem técnica confirmada e sem assento de arte em casa |
| **Expanse (Oslo), Jonas Martin Larsen, Head of CG, `jonas@expanse.no`** | Era **a melhor pessoa da rodada**: cargo e endereço publicados na seção `People` do site, casa com *"3d animated featurefilm Tix – The lost childhood (in production, 2027)"* e *"around 500 shots with animated hero characters"* | **JÁ FOI.** `enviados.csv` e o painel mostram carta enviada em **11/09** para esse mesmo endereço. O dedupe salvou a rodada de repetir |
| **Gimpville (Oslo), Torgeir Sanders, `oslo@gimpville.no`** | O site publica **só `jobs@gimpville.no`**; o diretório dá o nome e a **caixa `oslo@`** | **JÁ FOI.** Carta em **28/08** e follow-up em **07/09** nessa caixa. E não há endereço de pessoa publicado para abrir uma segunda porta |
| **`a-film.dk`** | Procurei a A. Film dinamarquesa de animação. O domínio é de **um produtor de vídeo corporativo de uma pessoa só** (*"Jeg tilbyder ... reklamefilm, produktpræsentationer, brand storytelling"*), com `anders@a-film.dk` | **FALSO AMIGO**, junto de `chopchop`, `mpc.wd1`, `icon.wd3`, `remedy`, `rain`, `triumph`, `playground`, `upp`, `cat` e `federation` |
| **Jogos nórdicos: krillbite, sarepta, megapop, dirtybit, ravnstudio, henchmanandgoon, ghostship, triband, kongorange, playdead, sixthvowel** | Sondadas raiz + `/contact` + `/about` + `/team` + `/kontakt` + `/om-oss` + `/people` + `/studio` + `/crew` | **ZERO endereço de pessoa.** Só caixa (`business@`, `contact@`, `mail@`, `support@`). E `sixthvowel.com` devolve `medicalcenter@fortknoxbg.com`, ou seja **domínio parqueado ou sequestrado**, não é o estúdio |
| **VFX britânico: axisstudiosgroup, milk-vfx, unionvfx, jellyfishpictures, luxaeterna** | Mesmas oito rotas | **ZERO endereço de pessoa.** O único achado é `recruit@unionvfx.com`, que é caixa |
| **VFX nórdico e holandês: ghost.dk, rvx.is, chimneygroup, baconx, captainpanda, wearebind, motekentertainment, suncreature, jafilm** | Mesmas rotas | **Nada legível por `curl`.** `fido.se` devolve `info@goodbyekansas.com`, ou seja **a Fido é Goodbye Kansas hoje**, casa que já escreveu para o Vini |
| **`ravnstudio.com` e `fakegraphics.fi`** | O proxy de saída recusou: `connect_rejected` (9x) e `ws_closed_mid_exchange` (7x) | **NÃO CONFERIDO**, e isto **não é zero**. Ficam para outra rodada |
| **Holanda: `filmcommission.nl/database/animation-studios/animation-studio/`** | Remedido hoje: **HTTP 500**, igual a 15/09 03h40 | **Continua quebrado do lado deles.** A parede holandesa segue de pé e **esta rodada não abriu a Holanda** |

**A Storm Studios foi a única casa das varreduras de domínio que publicou pessoa, e ela já era
conhecida.** A lição de 10/09 se confirma pela terceira vez: **em site Wix e afins, quem publica
endereço é a RAIZ, não `/contact`** — foi por isso que a raiz da Storm devolveu cinco pares de
nome, cargo e endereço enquanto onze casas de jogos e cinco de VFX devolveram caixa.

### A FILA NÓRDICA, agora com o diretório inteiro lido e com o dedupe já feito

Extraí **os 48 endereços** que `https://nordicanimation.com/studios-producers/` publica e cruzei
os domínios com o repositório. O que sobra com **endereço publicado, sem ficha e sem carta**,
para a próxima rodada não recomeçar do zero:

- **Com sinal de 3D ou CG, que é onde vale gastar primeiro:** **Tordenfilm** (NO, Eric Vogel,
  `eric@tordenfilm.no` — catálogo com *The Absence of Eddy Table* e *Two Buddies and a Badger*;
  **o site não publica email nem nomeia ninguém**, e `/about` só diz *"We produce and co-produce
  premium quality feature films, drama series and animation"*, então o cargo dele **não está
  publicado**); **Krystallplaneten** (NO, Merete Korsberg, `merete@krystallplaneten.no` — o perfil
  diz **"Working across 2D animation, stop motion and 3D"**, mas o link do site no diretório está
  quebrado, escrito `http://Krystallplaneten/`); **Plastilin Media OY** (FI, Kirill Razumov —
  *Kid-e-Cats*, *Sonya from Toastville*, mas o endereço publicado é **`@yahoo.com`**).
- **Sem prova de 3D, e por isso abaixo:** Nørlum (DK, Claus Toksvig Kjaer, caixa `contact@` — e
  atenção, **`norlum`/`noerlum` já aparece no repositório**, inclusive na lista de rascunhos
  corrigidos de 11/09); Skjaldborn (DK, caixa); Ouros (DK, Rikke Planeta, `hello@` — o site
  publica os fundadores mas a casa é de motion e explainer); Compass Films (IS, Heather Millard —
  documentário); Kyka (FO/DK), Made By Us (DK), Sparre Production (DK, Irene Sparre — MX Google
  vivo, conferido hoje), LØV Film, Bivrost, Klipp & Lim (**2D e bonecos, declarado**), Rainy Day,
  Ulvenfilm (**2D declarado**), Trollfilm (**stop motion declarado**), Mikrofilm (caixa), UpNorth
  (endereço `@gmail.com`), Pink Zebra (caixa `info@`), Sun In Eye (**2D declarado**), Animagency,
  Fiilin Good Films, Pyjama Films (**2D declarado**), Allimator, BCD Film (**2D declarado**),
  Dockhus (**stop motion**), LEE Film (**2D**), Soja, Apparat Filmproduktion (SE, casa diferente
  da Apparat Studio da Noruega — **não confundir**).
- **Já gastas, para não reabrir:** Sagatoon, Pop Up Production, Den Siste Skilling, Maipo,
  Gigglebug, Wil Film (fichas de 15/09 03h40), Qvisten (**teto de duas atingido**), Anima Vitae,
  Brikk, Filmic Art, The Chapel Films, Snowcloud (já na campanha), Fenomen (**não é animação**,
  medido em 15/09), Expanse e Gimpville (**carta já enviada**), Storm e Apparat (fichas de hoje,
  segunda pessoa).


---

# RODADA DO JOE, 15/09 18h35 UTC — cinco fichas, e a Holanda continuou fechada

**Rota pedida era Holanda primeiro. Ela não abriu, e o motivo está medido na tabela do fim
desta seção.** O que rendeu foi o **diretório nórdico relido com filtro de técnica**, que a
rodada das 15h35 tinha deixado como fila sem conferir a técnica no site de cada casa. Conferir
o site mudou o veredito de metade delas, nos dois sentidos.

**Nenhuma das cinco pessoas abaixo tem carta. Nenhuma linha tem endereço montado.**

> ## ✅ AS CINCO ESTÃO ESCRITAS — 15/09 às 19h25, pelo maestro
>
> | Pessoa | Casa | Rascunho | O que a carta teve de resolver |
> |---|---|---|---|
> | **Tero Suomela** | Animagency, Vantaa | `r-1127406507327552130` | a casa é **também agência de talento**, então o fecho fixo da campanha é literalmente o serviço que ela vende; a carta **cita** a frase deles em vez de afirmar que fazem 3D |
> | **Alli Sadegiani** | Allimator, Estocolmo | `r-8122479825025277631` | ele **vende mentoria e feedback pagos**: a carta diz **na primeira linha** que não é pedido de feedback. Ele é animador e não contrata, então o pedido é o de apontar |
> | **Eric Vogel** | Tordenfilm, Oslo | `r-2302955756468033677` | **cargo não publicado**, então a carta não o chama de nada; a animação é feita fora (Qvisten), e a carta assume isso em voz alta |
> | **Bárður Mikladal** | Kyka, Ilhas Faroe | `r1854103396231644481` | o diretório escreve "Kyka, **Denmark**" e isso engana: as Faroe estão **fora da UE e de Schengen**, e a carta diz isso com todas as letras |
> | **Juha Fiilin** | Fiilin Good Films, Helsinque | `r9059581669478497500` | o convite do site pede **portfólio e estágio na mesma linha**, então a carta diz de frente que são dez anos e não pedido de estágio |
>
> Texto das cinco em `automacao/cartas-nordicos3-1509/` (`.txt` e `.html`).
> `confere-carta.py` no lote inteiro: **OK, o lote pode sair**, pior par de semelhança **37%**.
> As cinco linhas do `pessoas.csv` já trocaram o `PENDENTE-maestro-escreve` pelo ID do rascunho.

### Tero Suomela — **Creative Producer - Founder** — Animagency, Vantaa, Finlândia — **casa nova, e a ficha mais forte da rodada**

- **Email:** tero@animagency.fi · confiança **alta** · **PUBLICADO pela própria casa, com nome E
  cargo ao lado** · fonte: https://www.animagency.fi/contact , aberta e lida nesta rodada. O bloco
  `People` publica dois pares: **"Tero Suomela — Creative Producer - Founder — tero(at)animagency.fi"**
  e "Robert Niva — Producer — robert(at)animagency.fi". A página escreve `(at)` no lugar do arroba,
  que é ofuscação de texto e não montagem: o local e o domínio estão escritos por extenso.
  **NADA FOI MONTADO.** Segunda fonte, com o mesmo endereço: https://nordicanimation.com/studios-producers/ .
  **MX conferido nesta rodada:** `aspmx.l.google.com` e os quatro `alt` (Google Workspace, vivo).
  Telefone existe nas duas fontes e **não é registrado aqui**.
- **Por que ELE e não outro da casa:** a casa publica exatamente duas pessoas, e reparte os papéis
  ela mesma — o Robert Niva é **Producer** e o Tero é **Creative Producer E Founder**. Em casa deste
  tamanho o fundador é quem decide arte, e o BRIEF-JOE manda ir no fundador em casa de até 30
  pessoas. O Robert Niva fica como **segunda e última** pessoa possível desta casa.
- **Gancho, com a frase do próprio estúdio entre aspas, e aqui há dois:** o perfil escrito pela
  casa diz **"Animagency is a story-driven animation studio based in Korso, Finland, specializing
  in animated drama-comedy series. We are passionate about memorable characters, entertaining
  stories, and distinctive visual worlds. Working across both 2D and 3D animation, we often blend
  techniques with traditional animation and visual arts to create unique artistic styles"**, e o
  segundo é o que faz esta casa valer mais que o tamanho dela: **"Through our international
  network, Animagency also represents top animation talent, connecting productions with the right
  talents and crews for every project"**. Ou seja a casa **é também uma agência de talento de
  animação** — o pedido "se outra pessoa aí for a certa, me aponte" do fecho fixo da carta é
  literalmente o serviço que ela vende. O `/about` acrescenta **"a Finnish story-driven animation
  IP studio that connects 100% remotely the best talents into the most entertaining productions.
  We have produced over 1500 minutes of animated content"**, e a casa é **100% remota**, o que
  desarma em parte a conversa de visto.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. **A linha de realocação vale**, com a ressalva
  de que a casa opera remota e talvez nem precise dela.
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `animagency OR Suomela OR kyka OR
  Mikladal OR filmicart OR Knape OR apparatfilm` e **ZERO** para `"animagency.fi"`. No repositório:
  zero ocorrências de `tero@animagency.fi` e de `animagency` em `pessoas.csv`, `enviados.csv`,
  `processados.csv`, `alvos.csv` e `docs/index.html`. **CASA NOVA, primeira pessoa.**
- **Ressalva honesta, e são três:** (1) **o 3D é palavra da casa, não prova vista** — as séries
  creditadas (*Crazy – Crazier – Junior High*, *Pelurit*, *Bruno & Pjarta*, *Pasila 2.5*) são
  sitcom animada para a YLE e têm cara de 2D; o "2D and 3D" está no perfil escrito pela casa e eu
  **não vi um frame 3D**, porque a página `/productions` do site está praticamente vazia, com um
  único cartaz (*SUPERMARS*) e nenhum texto; (2) **a casa tem caixa própria para candidatura**,
  `talent(at)animagency.fi`, publicada ao lado dos endereços de pessoa — escrever ao fundador em
  vez da caixa é a aposta do Joe, mas é uma aposta, e o estúdio pode simplesmente redirecionar;
  (3) é casa **pequena e remota**, então não há assento fixo de modelagem: a porta realista é
  freela e a rede de talento dela, não vaga.

### Alli Sadegiani — **diretor, animador e animation supervisor; dono da casa** — Allimator, Estocolmo, Suécia — **casa nova, e o endereço é CAIXA**

- **Email:** info@allimator.com · confiança **alta para a entrega, mas é CAIXA e não endereço de
  pessoa** · fonte: https://nordicanimation.com/studios-producers/ , aberta nesta rodada, no bloco
  da Allimator: **`Allimator, Sweden | Alli Sadegiani | info@allimator.com`**. **NADA FOI MONTADO**,
  e em particular **não montei** `alli@` — o site tem página `contact` e ela é **só formulário**,
  sem um único endereço escrito, então não existe endereço literal daquele domínio para provar
  padrão nenhum. **MX conferido nesta rodada:** `mx1`–`mx4.mailpod16-cph3.g1i.one.com` (provedor
  one.com, vivo). Telefone existe na fonte e **não é registrado aqui**.
- **Por que ELE e não outro da casa:** **a casa é ele.** O `/about` do próprio site escreve
  **"ALLIMATOR is a studio run by Alli Sadegiani"**, e não há segunda pessoa em lugar nenhum.
  Não há dilema.
- **Por que esta ficha existe apesar de ser uma caixa, e é o argumento mais forte da rodada:**
  em **fevereiro de 2026** ele ganhou o **Annie Award de "Individual Outstanding Character
  Animation TV/Media"**, pela *Win or Lose* da Pixar — está escrito, com essa formulação exata, na
  lista de prêmios do `/about`, e o próprio cabeçalho do site diz **"BY DIRECTOR | ANNIE AWARD
  WINNING ANIMATOR ALLI SADEGIANI"**. É a única pessoa desta rodada cujo prêmio publicado tem a
  palavra **personagem** no nome.
- **Gancho, com a frase do próprio estúdio entre aspas:** o `/about` diz que ele é **"an Award
  winning Swedish director, Annie Award winning animator and animation supervisor who has
  contributed to Academy Award-winning films at Walt Disney Animation, DreamWorks Animation, and
  Pixar Animation Studios"**, com os créditos **"Win or Lose (2025), Luca (2021), Soul (2020), Toy
  Story 4 (2019), Incredibles 2 (2018), Piper (2016), Inside Out (2015) and The Good Dinosaur
  (2013)"**, e que **"Under the ALLIMATOR umbrella, Alli is developing several independent animated
  projects targeted towards an older audience"**. O perfil no diretório acrescenta o que está
  aberto agora: **"In June 2025, Alli attended Annecy MIFA to present a new slate of 3D animated
  shorts and long-form projects in development, seeking producers and co-producers"**.
- **Fora dos EUA?** Sim — Suécia, União Europeia. **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `allimator OR Sadegiani OR bivrost OR
  "Trond Jacobsen"` e **ZERO** para `"allimator.com"`. No repositório: zero ocorrências de
  `info@allimator.com` e o token `allimator` só aparece dentro do texto de dedupe de outra ficha.
  **CASA NOVA.**
- **Ressalva honesta, e são quatro:** (1) **o endereço é `info@`**, o oposto do que o Joe existe
  para fazer — vale porque numa casa de uma pessoa a caixa é a pessoa, mas é caixa;
  (2) **ele não contrata** — é um artista independente desenvolvendo projeto próprio, sem pipeline
  e sem assento de modelagem para oferecer; o valor dele é ser quem conhece quem contrata na Pixar,
  na Disney e na DreamWorks, e o fecho fixo da carta ("se outra pessoa aí for a certa, me aponte")
  é a única parte que faz sentido nesta carta; (3) **ele é animador, não modelador** — o ofício
  dele é movimento e o do Vini é escultura, superfície e groom, então "colega de ofício responde
  colega de ofício" vale só pela metade; (4) o site **vende mentoria e feedback pagos** (a página
  `contact` lista "MENTORSHIP - 30min Intro", "1h Single Feedback Session"), então há risco real de
  a carta ser lida como pedido de serviço grátis — **quem escrever precisa deixar claro que não é
  pedido de feedback**.

### Eric Vogel — **cargo NÃO publicado** — Tordenfilm, Oslo, Noruega — **casa nova, e é a única com longa 3D entregue**

- **Email:** eric@tordenfilm.no · confiança **alta** · **PUBLICADO** · fonte:
  https://nordicanimation.com/studios-producers/ , aberta nesta rodada, no bloco da Tordenfilm:
  **`Tordenfilm, Norway | Eric Vogel | eric@tordenfilm.no | http://www.tordenfilm.no/`**.
  **NADA FOI MONTADO.** **MX conferido nesta rodada:** `10 mail.countzero.no` (servidor próprio,
  vivo). Telefone existe na fonte e **não é registrado aqui**.
- **Por que ELE e não outro da casa:** é a **única** pessoa que existe publicada em qualquer fonte
  desta casa. O site da própria Tordenfilm **não nomeia ninguém** — o `/about` fala só no plural
  ("we produce and co-produce") e o `/contact`, aberto hoje, publica **apenas** `info@tordenfilm.no`
  e `faktura@tordenfilm.no`. Não há dilema porque não há alternativa.
- **Gancho, com a frase do próprio estúdio entre aspas:** o `/about` do site diz **"Tordenfilm is
  an independent production company located in Oslo, Norway, founded in 2003. Tordenfilm was the
  first production company to be initiated solely by graduates of the Norwegian National Film
  School in Lillehammer"** e **"We produce and co-produce premium quality feature films, drama
  series and animation for both the domestic and international markets"**, com o lema de abertura
  **"Stable geniuses, always with heart."** O perfil escrito pela casa no diretório dá o crédito
  que interessa: **"Their latest animated feature Two Buddies and a Badger 2 – The Great Big Beast
  (2020) was a major box office success, and was co-produced with Qvisten Animation"**, e
  **"Tordenfilm also produced the provocative and multi-award-winning short The Absence of Eddy
  Table (2016), which was based on the works of Dave Cooper and was Oscar qualified"**. O *Eddy
  Table* é o gancho bom para o Vini: é personagem 3D **estilizado e grotesco**, desenho de Dave
  Cooper levado a CG, que é exatamente a faixa do portfólio dele — e não fotorrealismo.
- **Fora dos EUA?** Sim — Noruega (EEE). **A linha de realocação vale inteira.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `tordenfilm OR Vogel OR krystallplaneten
  OR Korsberg OR sparreproduction OR "Irene Sparre"` e **ZERO** para `"tordenfilm.no"`. No
  repositório: zero ocorrências de `eric@tordenfilm.no`; o token `tordenfilm` aparece **uma** vez em
  `pessoas.csv` e é dentro do texto de dedupe da ficha da GunHil, não um envio. **CASA NOVA.**
- **Ressalva honesta, e a terceira é a que mais pesa:** (1) **o cargo dele não é publicado em lugar
  nenhum** — o diretório dá nome, telefone, email e link e **nenhum título**, e o site não nomeia
  ninguém; **a carta não pode chamá-lo de nada**; (2) **é produtora, não estúdio de animação** — o
  próprio texto diz "produce and co-produce", e a Tordenfilm faz também live-action e drama;
  (3) **a animação é feita FORA**: o longa 3D deles foi "co-produced with **Qvisten Animation**", ou
  seja quem tem o pipeline e o assento de modelagem é a Qvisten — **e a Qvisten já está no teto de
  duas pessoas da campanha**; a leitura honesta é que esta carta chega a quem **financia e
  encomenda** personagem, não a quem o esculpe, e vale por isso ou não vale; (4) **o catálogo
  animado está parado desde 2020**, então não há prova de produção de personagem viva hoje.

### Bárður Mikladal — **cargo NÃO publicado** — Kyka, Norðragøta, Ilhas Faroe — **casa nova, e é a única desta rodada que declara 3D E VFX E personagem na mesma frase**

- **Email:** hey@kyka.fo · confiança **alta para a entrega, mas é CAIXA e não endereço de pessoa** ·
  fontes, as duas abertas nesta rodada: https://nordicanimation.com/studios-producers/ , que publica
  **`Kyka, Denmark | Bárður Mikladal | Hey@kyka.fo | +298...`**, e https://kyka.fo/ , cujo rodapé
  repete `hey@kyka.fo` em texto puro. **NADA FOI MONTADO**, e em particular **não montei**
  `bardur@` nem `bm@`, porque não existe um único endereço literal daquele domínio para provar
  padrão. **MX conferido nesta rodada:** `aspmx.l.google.com` com prioridade 1 e os quatro `alt`
  (Google Workspace, vivo). Telefone existe nas duas fontes e **não é registrado aqui**.
- **Por que ELE e não outro da casa:** o site **não tem página de equipe que abra** — `/about` e
  `/contact` respondem **404** (as rotas de verdade são faroesas, `/um` e `/samskifti`), e o
  rodapé, que é a parte que carrega, publica endereço e telefone e **nenhum nome**. O único nome
  que existe publicado em qualquer lugar é o dele, no diretório. Em casa deste tamanho, é a pessoa.
- **Gancho, com a frase do próprio estúdio entre aspas, e ela é a melhor descrição técnica da
  rodada:** **"Kyka is a small animation and VFX studio based in the Faroe Islands, bringing
  stories to life through 2D/3D animation, motion design, and visual effects. We collaborate with
  both local and international partners and welcome co-productions that share our passion for
  culturally rooted and character-driven stories. Our ambition is to create more homegrown content
  for children and Faroese audiences – high-quality, thoughtful storytelling across shorts, TV
  series, and commissioned formats"**, com o catálogo **"ABC Moments (shorts 2023), Sakin (series
  2022), ABC (Commissioned 2021)"**. **"3D" e "character-driven" na mesma frase** é o que nenhuma
  outra casa desta rodada escreveu.
- **Fora dos EUA?** Sim — **Ilhas Faroe**, e aqui há uma sutileza que a carta precisa acertar: as
  Faroe são território da **Dinamarca** mas **estão fora da União Europeia e fora do Espaço
  Schengen**, com regime de imigração próprio. O diretório escreve a casa como "Kyka, Denmark" e
  isso é enganoso. **A linha de realocação vale**, mas **nenhuma carta pode sugerir que trabalhar
  lá é trabalhar na UE.**
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `animagency OR Suomela OR kyka OR
  Mikladal OR filmicart OR Knape OR apparatfilm` e **ZERO** para `"kyka.fo"`. No repositório: zero
  ocorrências de `hey@kyka.fo`, de `kyka` e de `Mikladal` em `pessoas.csv`, `enviados.csv`,
  `processados.csv`, `alvos.csv` e `docs/index.html`. **CASA NOVA.**
- **Ressalva honesta, e são cinco:** (1) **o endereço é uma caixa `hey@`**; (2) **o cargo dele não
  é publicado** em nenhuma fonte que abri — a carta **não pode dar a ele um título**; (3) **o site
  é quase todo em faroês** e as duas rotas em inglês que tentei deram 404, então **não li nenhuma
  página institucional da própria casa**: a descrição inteira acima vem do perfil no diretório, que
  é fonte de terceiro (ainda que o texto seja escrito pela casa); (4) a casa se descreve como
  **"small"** e o catálogo publicado são **três peças**, duas delas comissionadas — não há prova de
  equipe de arte interna nem de vaga; (5) **é o mercado mais periférico da campanha inteira**, com
  ~54 mil habitantes no país todo, então a chance de haver assento sênior de personagem é baixa
  mesmo com a técnica batendo.

### Juha Fiilin — **cargo NÃO publicado, mas a casa leva o nome dele** — Fiilin Good Films, Helsinque, Finlândia — **casa nova, e é a única que PEDE portfólio por escrito**

- **Email:** juha@fiilin.com · confiança **alta** · **PUBLICADO pela própria casa** · fontes, as
  duas abertas nesta rodada: https://www.fiilingoodfilms.com/about , cujo rodapé escreve, logo
  abaixo do convite **"Work with us."**, o endereço **`juha(@)fiilin.com`** — ofuscação de texto,
  com local e domínio por extenso —, e https://nordicanimation.com/studios-producers/ , que publica
  **`Fiilin Good Films, Finland | Juha Fiilin | juha@fiilin.com | https://www.fiilingoodfilms.com/`**.
  **NADA FOI MONTADO.** **MX conferido nesta rodada:** `10 mx1.dvn.fi` (provedor finlandês, vivo).
- **Atenção de método, e é a armadilha da Stunlock outra vez:** o **site é `fiilingoodfilms.com` e
  o email é `@fiilin.com`**, domínios diferentes. Qualquer endereço montado sobre o domínio do site
  teria quicado. O endereço certo é o do domínio curto, e ele está escrito nas duas fontes.
- **Por que ELE e não outro da casa:** o `/about` tem uma seção **"Meet the team"** e ela **não
  nomeia ninguém** — o texto embaixo do título diz só *"We collaborate across countries, time
  zones, and disciplines"*. O único nome publicado em qualquer lugar é o dele, a empresa leva o
  sobrenome dele, e a matéria de imprensa citada no próprio site atribui a fala à pessoa:
  **"Commenting on the project, Fiilin told Cineuropa"**. Não há dilema.
- **Gancho, com a frase do próprio estúdio entre aspas, e o primeiro é o motivo desta ficha
  existir:** a home fecha com **"Let's talk. About your day, your awesome story idea, your
  portfolio or your upcoming internship."** — **é a única casa desta rodada que pede portfólio por
  escrito**, e o pedido está a dois parágrafos do endereço dele. O segundo gancho é a frase de
  método: **"We design our stories from a strong concept — with character, premise, theme, and
  deeper purpose all integrated from the start"**, e a casa se descreve como **"genre-driven IP for
  tweens, teens and young adults across series, features, games and graphic novels"**, com serviço
  declarado de **"Game studio collaboration: Narrative, trailers, VO, music, art direction, and
  hybrid storytelling support"**. A fala do diretor sobre a série carro-chefe, publicada pelo
  próprio site, é sobre personagem: **"In Joy Eternal, we show a character struggling with her
  self-worth, mistakenly thinking it is tied to her achievements and failures"**.
- **Fora dos EUA?** Sim — Finlândia, União Europeia. **A linha de realocação vale inteira**, com a
  ressalva de que a casa se declara distribuída por **"Helsinki – Barcelona – London – Dublin – Los
  Angeles"**.
- **Dedupe, feito na caixa:** o **Gmail devolveu ZERO** para `fiilin OR "Joy Eternal" OR "Fiilin
  Good"` e **ZERO** para `"fiilin.com"`. No repositório: zero ocorrências de `juha@fiilin.com`,
  de `fiilin` e de `fiilingoodfilms` em `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `alvos.csv` e `docs/index.html`. **CASA NOVA.**
- **Ressalva honesta, e a segunda é a que pode matar a ficha:** (1) **o cargo dele não é publicado**
  — nem o site nem o diretório escrevem um título, e a única prova de que ele manda é a empresa
  levar o nome dele e a imprensa citá-lo como voz da casa; **a carta não pode dar a ele um título**;
  (2) **a técnica NÃO é dita em lugar nenhum**: o site fala em "animated", "anime-influenced",
  "motion comics" e "graphic novels" e **nunca escreve 3D nem CG** — esta é a casa desta rodada com
  **a prova mais fraca de pipeline 3D**, e pode ser inteiramente 2D; (3) é **desenvolvimento e IP,
  não produção** — o texto diz que ela "develops original IP" e "partners with studios, producers,
  and game developers", ou seja **a animação é feita por terceiros** e o assento de modelagem,
  se existir, não é dela; (4) o *"your portfolio"* do convite está dentro de um **formulário de
  contato**, e o formulário oferece "internship" na mesma linha — há risco de a carta de um sênior
  de dez anos cair no mesmo funil de estagiário.

### O QUE MORREU NESTA RODADA, com a medição, para ninguém repetir

**Cinco alvos foram investigados até o fim e mortos. Três deles morreram no DEDUPE DA CAIXA,
depois de eu já ter aberto o site e lido cargo e endereço — ou seja, o trabalho de detetive
estava certo e o alvo é que já tinha sido gasto.** Isso custou metade da rodada e a lição está
no fim desta tabela.

| Alvo | O que foi medido hoje | Veredito |
|---|---|---|
| **Piranha Bar (Dublin), Richard Chaney, `richard@piranhabar.ie`** | Página `/contact` publica **cinco** pares de nome, cargo e endereço, entre eles *"Richard Chaney — Partner \| Creative Head of Studio"*, cuja bio diz que ele *"leads the studio—inspiring our multidisciplinary team, **scouting emerging global talent**"* | **TETO ATINGIDO.** O Gmail devolveu **cinco threads**: carta para `richard@` em **03/09**, carta para `gavin.k@` (Founding Partner) em **06/09**, carta para `info@` em 26/08 com follow-up em 02/09, e dois recibos automáticos. **Duas pessoas já gastas, a casa está fechada pela regra do teto** |
| **Telegael (Galway), Morgan O'Brien, `morgan@telegael.com`** | `/our-team` publica **doze** pares de nome, cargo e endereço, e o bloco dele é o alvo perfeito: **"Head of Animation"**, com a bio dizendo que as responsabilidades cobrem *"Art Direction, IP Development ... including **Character Design**, Background Painting, Concept Development"* | **TETO ATINGIDO.** O Gmail devolveu **duas threads**: carta para `morgan@` em **06/09** com follow-up em 08/09, e carta para `cathy@` (Head of Production) em **11/09**. Nenhuma resposta, e nenhuma vaga aberta por essa porta |
| **Filmic / Filmic Art (Estocolmo), `andreas@filmic.se`** | Melhor encaixe técnico que eu vi hoje: `/who-we-are` escreve **"Character animation and storytelling are what we're passionate about"**, *"rigging and animation of **advanced 3D characters** or animals"*, *"cinematic trailers with **stylised characters**"*, com Clash Royale, Minecraft, Stellaris e Paradox no portfólio; `/contact` publica **Andreas Ibohm (Executive Producer)** e **Moa Thenstedt Åkerström (Producer)**, e a caixa de talento pede literalmente **"3D artist"** | **TETO ATINGIDO.** Gmail: carta para `andreas@filmic.se` em **03/09**, para `moa@filmic.se` em **06/09** e para `jobb@filmic.se` em 02/09 com follow-up em 07/09. **Quatro cartas nesta casa.** Fica o registro de método: o site é `filmicart.com` e o email é **`@filmic.se`** — armadilha da Stunlock, e o diretório nórdico ainda publica `jonathan@filmicart.com`, endereço que a casa **não** usa em lugar nenhum do próprio site |
| **Sparre Production (Copenhague), Irene Sparre, `irene@sparreproduction.dk`** | Tudo batia: endereço publicado, **MX Google vivo**, casa **nova**, cargo publicado pela casa (*"Irene Sparre / Founder, CEO, Producer"*), e a prova de CG mais forte da rodada — *"Sparre Production has – for Wil Film – over the last 8 years produced more than 3000 minutes of animated content for LEGO, Disney, Lucasfilm based on LEGO Ninjago® and LEGO Star Wars® franchises"* e **"Sparre Production is signatory to high-end CG productions"**; a equipe publicada tem **Character Designer**, dois Art Directors e dois Concept Artists | **A PRÓPRIA CASA PEDIU PARA NÃO SER PROCURADA.** A página `/contact`, aberta hoje, escreve: **"We are not currently accepting internship applications or unsolicited job enquiries. Any future opportunities will be announced through our website and social media channels."** Carta fria pedindo para entrar na lista **é** unsolicited job enquiry. Pela regra do BRIEF-JOE, quem pediu para não ser contatado está fora. **NÃO VIRA FICHA E NÃO DEVE SER REABERTA enquanto essa frase estiver no ar** |
| **Krystallplaneten (Tromsø), Merete Korsberg, `merete@krystallplaneten.no`** | Endereço e cargo publicados pela própria casa (`/people`: *"Merete Korsberg (OWNER/PRODUCER/CEO)"*, e o rodapé de todas as páginas repete o endereço), MX vivo, casa nova, e o perfil no diretório promete *"Working across 2D animation, stop motion and **3D**"* | **FORA DA TÉCNICA, e o site desmente o diretório.** A página `/productions`, aberta hoje, escreve a técnica projeto a projeto e **não há um único 3D**: *"KUNNSKAPENS SKOG ... **Style: digital 2D**"*, *"PEARL FISHERS ... **Style: stop motion**"*, *"ORIGIN OF MAN ... **Style: stop motion and glass table animation**"*. Ainda por cima ela é **co-produtora** no longa, cujo produtor principal é a Bautafilm sueca. **É a mesma morte da Tulipop, e é a prova de que o diretório nórdico não pode ser lido sem abrir o site** |

**Falsos amigos de token derrubados hoje, para a lista crescer:** **`motionmakers`** não é
estúdio de animação, é uma casa de **vídeo corporativo e estratégia de vídeo** com escritório em
Vilvoorde e Hilversum (*"our core business is video in all its forms"*), e o token "motion"
enganou; **`mrkaplin`** não é estúdio, é **um diretor freelance sozinho** (Robert Glassford, 3D
Art & Motion Director, representado pela Jelly London) — publica `rob@mrkaplin.com` mas não
contrata ninguém; **`paladinstudios`** existe e publica `stein@paladinstudios.com`, mas a primeira
linha do `/about` diz **"ANNOUNCEMENT: Our quest has ended, and Paladin has shut down operations
on May 1st 2024"** — **casa morta, endereço vivo**, que é a armadilha pior de todas porque a
varredura mecânica não vê a diferença.

### A LIÇÃO DE MÉTODO DESTA RODADA: O DEDUPE DE DOMÍNIO VEM ANTES DA INVESTIGAÇÃO, NÃO DEPOIS

Eu gastei Piranha Bar, Telegael e Filmic **inteiras** — abrir site, ler equipe, extrair cargo,
conferir técnica — **antes** de perguntar ao Gmail. As três já estavam no teto. Trabalho jogado
fora por ordem errada de operação.

**O conserto é barato e é este, e ele monta a peneira UMA vez por rodada:**

```sh
cat enviados.csv automacao/pessoas.csv automacao/processados.csv alvos.csv docs/index.html \
 | grep -ohiE '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}' | tr 'A-Z' 'a-z' \
 | sed 's/.*@//' | sort -u > /tmp/dominios_gastos.txt
```

Isso devolveu **953 domínios já tocados** nesta rodada, e `piranhabar.ie` e `telegael.com` estavam
**os dois lá dentro**. Depois é só `grep -vxFf /tmp/dominios_gastos.txt lista_candidatos.txt`
antes de abrir a primeira página. **A peneira de domínio é a primeira operação da rodada, não a
última**, e o Gmail continua sendo a confirmação final — foi ele, e só ele, que pegou a Filmic,
cujo domínio de email (`filmic.se`) não estava na lista porque o domínio do site é outro.

### A HOLANDA NÃO ABRIU, E AGORA ESTÁ MEDIDO POR QUE

A rota pedida era Holanda primeiro. **Ela rendeu ZERO pessoa nova**, e isto não é "não procurei":

| O que foi tentado | Resultado medido |
|---|---|
| **83 domínios holandeses** sondados em raiz + `/contact` + `/about` + `/team` + `/our-team` + `/people` + `/crew` + `/studio` + `/jobs` + `/careers` (animação, VFX e jogos) | **UM único endereço de pessoa em casa viável**, e ele já era conhecido: `bastiaan@polderanimation.com`. Todo o resto é caixa (`info@`, `hello@`, `office@`, `jobs@`) |
| **Política de privacidade e Impressum** em `/privacy`, `/privacy-policy`, `/privacybeleid`, `/impressum`, `/datenschutz`, `/legal`, `/legal-notice`, `/colofon`, `/disclaimer`, `/gdpr`, `/terms`, `/privacy-statement` nos **117 domínios novos** da rodada | **ZERO endereço de pessoa.** Só `dataprotection@`, `dpo@` e caixa. A veia do encarregado de dados, que rendeu a GIANTSTEP na Coreia, **não rende na Holanda nem no Reino Unido** |
| **Campo `recruiter-email` do Teamtailor** em `/`, `/careers`, `/careers/`, `/jobs`, `/career`, `/vacatures`, `/werken-bij` nos mesmos 117 | **ZERO ocorrências.** Confirma a medição de 07/09: a veia é rica mas rara |
| **`filmcommission.nl/database/animation-studios/`** | Não remedido hoje; seguia **HTTP 500** às 15h35 e às 03h40 |
| **Diretórios holandeses de animação** — `animationinthenetherlands.nl`, `dutchanimation.nl`, `holland-animation.nl`, `klik.amsterdam`, `nfpa.nl` | **Os cinco recusados pelo proxy de saída** com `CONNECT tunnel failed, response 502`. **Isto é NÃO CONFERIDO, não é zero**, e é a pista mais promissora que fica aberta: se houver um diretório holandês com a estrutura do `nordicanimation.com`, ele está atrás dessa parede |

**Leitura honesta:** a Holanda não tem veto escrito, tem **ausência de fonte**. As casas
holandesas de porte (Guerrilla, Nixxes, Vertigo, Abbey, Grendel, Ambassadors, il Luster) publicam
caixa e nada mais; as pequenas que publicam pessoa (Polder) **já receberam carta**. A próxima
rodada que for para a Holanda deve gastar o tempo **procurando o diretório**, não varrendo
domínio um a um — a varredura já foi feita e está medida acima.

### A FILA QUE SOBRA, com o dedupe já feito, para a próxima rodada não recomeçar do zero

**Nórdicos com endereço publicado, casa nova, sem carta e SEM FICHA** (todos com Gmail = zero
nesta rodada, e todos com a técnica **ainda não conferida no site da casa** — que é exatamente o
passo que matou a Krystallplaneten, então **confira antes de virar ficha**):

- **Apparat Filmproduktion** (SE, Johan Edström, `johan@apparatfilm.se`) — o perfil diz
  *"Techniques include 2D animation, stop motion, **CGI** and mixed media"*, mas também
  *"specializing in animation for **documentaries** and commissioned films"*; o site
  `apparatfilm.se` respondeu **HTTP 503** hoje, então **não há frase da casa**. **Não confundir com
  a Apparat Studio da Noruega**, que é outra casa e já tem ficha. Nota de dedupe: **Johan Edström é
  a MESMA pessoa** que aparece no diretório como Executive Producer da Chapel Films
  (`johan.edstrom@thechapelfilms.com`) — duas casas, uma pessoa, **não vale como duas cartas**.
- **Bivrost Film** (NO, Trond Jacobsen, `trond@bivrostfilm.no`, MX `mx.domeneshop.no` vivo) —
  Emmy e Contrechamp em Annecy, mas **nenhuma técnica declarada** e *My Favorite War* é 2D.
- **LØV Film** (NO, Lillian Løvseth, `lillian@loevfilm.no`) — **nenhuma técnica declarada**.
- **Fiilin Good Films** virou ficha nesta rodada; **Made By Us** (DK, 2D declarado),
  **Compass Films** (IS, *"full-service **2D** studio"*), **LEE Film**, **Pyjama**, **Soja**,
  **BCD Film**, **Sun In Eye** e **Ulvenfilm** (2D declarado), **Dockhus** e **Trollfilm** (stop
  motion declarado) estão **fora da técnica** e não devem ser reabertas.
- **Plastilin Media OY** (FI, Kirill Razumov) — endereço publicado é **`@yahoo.com`**, caixa
  pessoal de provedor; fica por último.

**Holanda, a pista que fica aberta e vale mais que a fila acima:** **Polder Animation** é
`3D character animation studio` declarado, tem **três** endereços de pessoa publicados em
`/about` e só **um** foi gasto — sobram `sander@` (Production Design/Set Design) e `jean-paul@`
(Technical Director/Rigger). **Não virou ficha hoje por dois motivos, e os dois precisam ser
respeitados:** o Bastiaan recebeu carta em **11/09**, ou seja há quatro dias, e escrever de novo
agora é a queimada de cadência que o briefing proíbe; e dos dois que sobram, o **Sander é design
de cenário, que é AMBIENTE e está vetado pela regra do Vini de 10/09**. O único candidato legítimo
é o **Jean-Paul Tossings**, e mesmo ele é TD e rigger, não decisor de arte de personagem.
**Decisão para depois de 20/09, e é do maestro.**


---

## RODADA DAS 21h35 DE 15/09/2026 — JOE, A PARTIR DO CENSO WIKIDATA DE ANIMAÇÃO

**De onde saiu:** `automacao/alvos-joe-wikidata.csv`, 167 estúdios de animação inéditos com site
oficial. **O aviso do maestro estava certo e foi o achado central da rodada:** o Wikidata
classifica por rótulo, e a lista é dominada por casas de **2D, stop motion e produção pura**. A
varredura automática de **153 domínios × até 20 caminhos** (`/contact`, `/about`, `/team`,
`/kontakt`, `/equipe`, `/impressum`, `/company`, `/people`, `/crew`, `/contacto`, `/a-propos`,
`/en/contact` …) devolveu **endereço de pessoa publicado em apenas cinco domínios da lista
inteira**. Por isso as fichas abaixo são poucas e várias são de caixa: **nenhum endereço foi
montado.**

---

### Gregory Zalcman — Producer — Take Five / Carbone 14, Bruxelas, Bélgica
- **Email:** `gregory@take-five.be` · confiança **alta** · fonte: **https://take-five.be/team**,
  aberta nesta rodada, bloco `TEAM`, que publica literalmente *"Gregory Zalcman / Producer /
  gregory@take-five.be"*. **NADA FOI MONTADO.** MX conferido nesta rodada por DNS: `take-five.be`
  responde `1 aspmx.l.google.com` e os quatro alt (Google Workspace, vivo); `carbone-14.be`
  responde `1 smtp.google.com`. Telefones existem na fonte e **não são registrados aqui**.
- **Por que ELE e não outra pessoa da casa:** a página publica **quatro** pessoas com nome, cargo
  e endereço — Gregory Zalcman (Producer), Alon Knoll (Producer), David Grançon (Producer /
  production manager) e Eric Jaminet (Production Accountant). Não há uma única pessoa de **arte**
  publicada, então a regra do `BRIEF-JOE` para casa pequena cai no sócio-produtor. **A prova de
  que é ele, e não outro dos quatro, é cruzada:** a página de contato da **Carbone 14**, o estúdio
  de animação da casa, publica **o mesmo número de telefone** que a página da Take Five imprime ao
  lado do nome do Gregory, e o **mesmo endereço postal** (Avenue Van Volxem 326A, Forest/Bruxelas).
  Quem atende pela Carbone 14 é ele. Alon Knoll fica como **SEGUNDA e última** possível.
- **Técnica CONFERIDA NO SITE, e é o motivo de esta ficha existir:** a home da Carbone 14 diz
  *"Carbone 14 is a Brussels-based 2D and 3D animation studio bringing films and series to life"*;
  o `/about` acrescenta *"The studio then turned to more ambitious projects, notably with Flow by
  Gints Zilbalodis, Carbone 14's first 3D feature film"* e *"this has led us to get involved in
  Nino Dino, a 78 x 7' preschool series developed by Folivari (France) and **animated in
  Blender**"*. 3D declarado **e** com dois títulos nomeados — não é palavra solta.
- **Gancho, com a frase do próprio estúdio entre aspas:** a Take Five escreve
  *"To support its growth, Take Five established Carbone 14, an animation studio designed to bring
  its projects to life"*, e o `/about` dela abre com *"Take Five was born from a simple yet
  powerful ambition: to produce works that evoke emotions and resonate with audiences"*. A ponte
  para o Vini é o **Nino Dino**: 78 episódios de pré-escolar em Blender é exatamente o tipo de
  produção que precisa de personagem que aguente anos de série sem quebrar.
- **Fora dos EUA?** Sim — Bélgica, União Europeia. A frase de realocação vale inteira.
- **Dedupe NA CAIXA, feito ANTES de abrir a primeira página:** `search_threads` por
  `"take-five.be" OR "take five" OR "image-cie.com" OR "Image Entertainment" OR "hydralab" OR
  "soulcage"` devolveu **`{}`**, zero threads; e por `"mexopolis" OR "pictak" OR "Gutierrez" OR
  "carbone-14" OR "Zalcman"` também **zero**. No repositório, `take-five` só aparece em
  `censo-wikidata.csv` e `alvos-joe-wikidata.csv` (listas, não envios), e `Zalcman` e `carbone-14`
  dão **zero ocorrências**. **CASA NOVA, primeira pessoa.**
- **Ressalva honesta:** (1) **a Take Five é PRODUTORA, não o estúdio** — quem tem o pipeline é a
  Carbone 14, e são duas pessoas jurídicas com números de IVA diferentes (`BE 0877.810.210` e
  `BE 0871.532.033`); a carta chega a quem financia, não a quem esculpe; (2) **os quatro nomes
  publicados são todos de PRODUÇÃO** — não existe Art Director, Head of Art nem CG Supervisor
  publicado em nenhuma das duas casas, então não há como cumprir o "personagem primeiro" no alvo,
  só no conteúdo da carta; (3) **o crédito de Flow é de co-produção**: o filme foi dirigido e em
  boa parte animado pelo próprio Zilbalodis com equipe mínima, e chamar a Carbone 14 de "a casa
  que fez Flow" seria exagero que um produtor percebe na primeira linha; (4) a casa é **2D e 3D**,
  com o 3D concentrado em dois títulos, e o grosso do catálogo (Last Door South, Vol au Vent,
  Boys Boys Boys) é 2D de autor; (5) a Carbone 14 publica **só `info@carbone-14.be`**, então o
  endereço desta ficha é o da produtora-mãe, não o do estúdio.

---

### Sunit Parekh — Director (é o único dos cinco da página `/directors` com endereço publicado) — hydralab, Copenhague, Dinamarca
- **Email:** `sunit@hydralab.com` · confiança **alta** · fonte: **https://cph.hydralab.com/contact**,
  aberta nesta rodada, onde o bloco do escritório imprime, em texto puro,
  *"Nytorv 17, 1 sal, 1450 København K, Danmark / Sunit Parekh, sunit@hydralab.com"*. O nome dele
  também está em **https://cph.hydralab.com/directors**, ao lado de Kim Hagen, Esben Tønnesen,
  Tonni Zinck e Tor Fruergaard. **NADA FOI MONTADO** — e em particular **não montei** endereço
  para nenhum dos outros quatro diretores, porque o único endereço literal daquele domínio além da
  caixa `cph@` é o dele. MX conferido nesta rodada por DNS: `10 smtp.google.com` (vivo).
- **Por que ELE e não outra pessoa da casa:** a casa publica exatamente **cinco** diretores e
  **um** endereço de pessoa, o dele, e o publica **junto do endereço postal do escritório**, que é
  a posição de quem responde pela operação de Copenhague. Os outros quatro não têm endereço em
  lugar nenhum do site, e escrever para eles exigiria montar — o que esta campanha já pagou caro
  para aprender a não fazer (dos 8 montados, **cinco quicaram**).
- **Gancho, com a frase do próprio estúdio entre aspas:** a home resume a casa em cinco palavras,
  *"animation, vfx, miniatures, software, robots"*, e o `/contact` desenvolve:
  *"From directing commercials and short films, executing high-end visual effects, to developing
  innovative software and technology, hydralab occupies many worlds - and its core mission, to
  remain broad, agile and ambitious, puts it in a unique position to understand visual
  communication and information."* O catálogo aberto por mim tem **Dreambuilders**, **The Gnome
  Movie**, **Gräns**, **Thelma**, **The Neon Demon**, **LEGO Replay** e **Along with the Gods** —
  ou seja, a casa senta em produção de personagem digital e criatura, mesmo sem dizer a palavra.
- **Fora dos EUA?** Sim — Dinamarca, União Europeia. A frase de realocação vale inteira.
- **Dedupe NA CAIXA, feito ANTES de abrir a primeira página:** `search_threads` por
  `"take-five.be" OR "take five" OR "image-cie.com" OR "Image Entertainment" OR "hydralab" OR
  "soulcage"` devolveu **`{}`**, zero threads, e `"Parekh"` também deu zero. No repositório,
  `hydralab` aparece em `garimpo-cgstudiomap.csv`, `censo-wikidata.csv` e
  `alvos-joe-wikidata.csv` — **as três são listas de prospecção, nenhuma é envio** — e `Parekh` dá
  **zero ocorrências**. **CASA NOVA, primeira pessoa.**
- **Ressalva honesta, e a primeira é séria:** (1) **a técnica 3D NÃO está escrita em lugar
  nenhum** — abri a home, o `/contact`, o `/directors` e o `/work` e a casa **nunca escreve 3D,
  CG, modelagem nem personagem**; o que me faz acreditar que há 3D ali são **títulos de projeto**
  (Dreambuilders é longa CG dinamarquês, Gräns tem criatura protética e digital), e **título não é
  descrição de técnica** — é exatamente o erro que derrubou a Krystallplaneten; (2) **"director"
  aqui é diretor de comercial e de curta, não cargo executivo nem de arte** — a página `/directors`
  não imprime um único título ao lado dos cinco nomes, então **a carta não pode chamá-lo de nada
  além do que a página diz**; (3) a casa é **publicidade, VFX e software**, com "robots" e
  "miniatures" na mesma frase — não é estúdio de animação de personagem, é uma casa larga, e o
  assento de modelagem sênior pode simplesmente não existir; (4) **não existe página de vagas**.

---

### Sebastian Runschke — Geschäftsführer (e, pelo texto da própria casa, quem faz a "kreative Leitung") — SERU Animation, Ludwigsburg + Hannover, Alemanha
- **Email:** `office@seru-film.com` · confiança **alta (entrega)** — **mas é CAIXA, não endereço
  de pessoa** · fonte: **https://www.seru-animation.com/impressum/**, aberta nesta rodada, que
  publica *"Vertreten durch: die persönlich haftende Gesellschafterin: SERU Verwaltungs-GmbH …
  diese vertreten durch den Geschäftsführer Dipl.-Ing. Sebastian Runschke"* e, logo abaixo,
  *"E-Mail: office@seru-film.com"*. **NADA FOI MONTADO.**
  **ARMADILHA DE DOMÍNIO, E ELA É GRAVE AQUI:** o site é **`seru-animation.com`** e o email é
  **`@seru-film.com`** — domínios diferentes. Qualquer endereço montado sobre o domínio do site
  (`s.runschke@seru-animation.com` e parentes) teria quicado. MX conferido nesta rodada por DNS:
  `redparrot-studios.com` e `soulcage-department.de` respondem `5 smtpin.rzone.de`; o de
  `seru-film.com` não foi consultado e **fica como pendência honesta**.
- **Por que ELE e não outra pessoa da casa:** o site **não tem página de equipe** e não nomeia
  mais ninguém. O `Über Uns` diz, sobre ele e sobre mais ninguém, que *"Bei den vorwiegend
  europäisch finanzierten Projekten übernimmt SERU unter der Leitung von Geschäftsführer Sebastian
  Runschke die gesamtheitliche Steuerung sämtlicher Arbeitsschritte und Bereiche innerhalb von
  Animationsfilmproduktionen, **sowie die kreative Leitung**, Planung und Durchführung der
  Arbeiten"* — ou seja, a própria casa escreve que a direção criativa é dele. Em casa deste porte
  o `BRIEF-JOE` manda ir no fundador, e aqui o fundador é também quem assume a arte por escrito.
- **Técnica CONFERIDA NO SITE:** o `Über Uns` diz *"SERU Animation GmbH & Co KG ist seit der
  Gründung im Jahr 2011 spezialisiert auf die Produktion von **Zeichentrick und CGI animierten
  Kinofilmen** und TV-Serien"*, e o menu de projetos lista **Die Häschenschule**, **Die
  Häschenschule 2 – Der Große Eierklau**, **Rabbit Academy**, **Die Heinzels**, **Die Heinzels 2**
  e **Meine Chaosfee & Ich** — longas de cinema em CGI, com elenco animal e criatura. **Isto não
  é 2D puro**, e é a casa desta rodada com mais metragem de personagem 3D no catálogo.
- **Gancho, com a frase do próprio estúdio entre aspas, e é o melhor da rodada:** a página
  `https://www.seru-animation.com/film-jobs/`, aberta nesta rodada, diz
  *"Gerade haben wir leider keine offenen Stellen zu besetzen. **Wir freuen uns dennoch immer über
  Initiativbewerbungen!**"* — a casa **pede candidatura espontânea por escrito**. E o `Über Uns`
  dá o segundo gancho, que é de padrão de qualidade: *"Produzent und Partner mit hohem
  qualitativem Anspruch an **Artwork und Design**"*, além de *"Mit ihrem Firmensitz und kreativen
  Basis in Ludwigsburg und einem eigenständigen Kreativteam und Studio in Hannover"* — há equipe
  de arte interna, não é só coordenação.
- **Fora dos EUA?** Sim — Alemanha, União Europeia. A frase de realocação vale inteira.
- **Dedupe NA CAIXA:** `search_threads` por `"seru-film" OR "seru-animation" OR "Runschke" OR
  "redparrot" OR "Red Parrot" OR "Keweloh" OR "Parekh" OR "Harder"` devolveu **cinco threads e
  NENHUMA é destas casas** — são Brink Helsinki, Gigglebug, Dead Astronauts e Golden Wolf, todas
  capturadas pela palavra inglesa *"harder"* dentro do corpo das cartas. **Falso positivo de
  token, conferido um a um.** No repositório, `seru` e `redparrot` só aparecem em
  `censo-wikidata.csv` e `alvos-joe-wikidata.csv` (listas), e `Runschke` e `Keweloh` dão **zero**.
  **CASA NOVA, primeira pessoa.**
- **Ressalva honesta:** (1) **o endereço é uma CAIXA `office@`**, o oposto do que o Joe existe
  para fazer; o site não publica **um único** endereço de pessoa; (2) a casa se descreve como
  **"Produzent und Partner"** que faz a *"gesamtheitliche Steuerung"* — coordenação de produção
  europeia com co-produtores, ou seja parte considerável da animação é feita **fora**; (3) o
  catálogo é **misto**: Die Häschenschule e Die Heinzels são CGI, mas *Der kleine Rabe Socke*,
  *Petronella Apfelmus* e *Simsala Grimm* são Zeichentrick (2D), e a página não diz qual técnica
  vai no próximo projeto; (4) **não há vaga aberta**, e a casa tem **botão próprio de
  Initiativbewerbung** — escrever ao Geschäftsführer contorna o funil que ela mesma pediu, e a
  carta precisa assumir isso em vez de fingir que não viu; (5) o MX de `seru-film.com` **não foi
  conferido nesta rodada**.

---

### Elmar Keweloh — representante legal da casa (o Impressum diz "Vertreten durch", sem cargo) — The Soulcage Department, Bremen, Alemanha
- **Email:** `info@soulcage-department.de` · confiança **alta (entrega)** — **mas é CAIXA, não
  endereço de pessoa** · fonte: **https://www.soulcage-department.de/3d-animationsstudio/**,
  aberta e lida por extenso nesta rodada; é a página `ÜBER UNS` e traz, no mesmo documento, o
  bloco de contato com `info@soulcage-department.de` e o Impressum com *"Vertreten durch: Elmar
  Keweloh, Wilhelm Landt"*. **NADA FOI MONTADO** — e em particular **não montei** `e.keweloh@`
  nem `elmar@`, porque **não existe um único endereço literal daquele domínio** além da caixa. MX
  conferido nesta rodada por DNS: `5 smtpin.rzone.de` (Strato, vivo). Telefone existe na fonte e
  **não é registrado aqui**. `/impressum/` e `/kontakt/` respondem **404** — o Impressum vive
  dentro do `ÜBER UNS`, e quem procurar pela rota canônica vai achar que a casa não tem.
- **Por que ELE e não outra pessoa da casa:** o site **não tem página de equipe** e não nomeia
  mais ninguém além dos dois representantes legais. Dos dois, Elmar Keweloh é o primeiro listado;
  **Wilhelm Landt fica como SEGUNDA e última** possível. Em casa deste tamanho o `BRIEF-JOE` manda
  ir no fundador.
- **Técnica CONFERIDA NO SITE, e esta é a melhor da rodada inteira:** o título da página é
  *"3D Animationsstudio • Animationsfilme • Character Design"* e o texto abre com três palavras que
  são praticamente o cargo do Vini — ***"Wir erschaffen Charakter."*** Segue:
  *"Seit 2002 entwickeln wir als spezialisiertes **3D-Animationsstudio** hochwertige visuelle
  Inhalte für die Werbebranche – mit Fokus auf **Charakteranimation**, visuelle Effekte und CGI"*
  e *"Ob markante **3D-Charaktere**, Cinematics, realitätsnahe VFX-Integration in Realfilm oder
  hochauflösende CGI-Stills – wir machen Ideen sichtbar"*. **Nenhuma outra casa desta rodada
  escreveu "personagem" e "3D" juntos três vezes na mesma página.**
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Wir erschaffen Charakter"* é o gancho,
  e o complemento é *"Unser Team verbindet technisches Know-how mit gestalterischer Leidenschaft"*.
  A lista de clientes publicada na mesma página tem Coca-Cola, Ferrero, Bayer, Dr. Oetker, Meta e
  Barclays — é publicidade de marca grande, onde mascote e personagem estilizado são o produto.
- **Fora dos EUA?** Sim — Alemanha, União Europeia. A frase de realocação vale inteira.
- **Dedupe NA CAIXA:** `search_threads` por `"…hydralab" OR "soulcage"` devolveu **`{}`**, zero
  threads, e a busca por `"Keweloh"` também deu zero (os cinco resultados daquela consulta eram
  falso positivo da palavra inglesa *harder*, conferidos um a um). No repositório, `soulcage` só
  aparece em `censo-wikidata.csv` e `alvos-joe-wikidata.csv` (listas), e `Keweloh` dá **zero**.
  **CASA NOVA, primeira pessoa.**
- **Ressalva honesta:** (1) **o endereço é uma CAIXA `info@`**, o oposto do que o Joe existe para
  fazer — vale porque é o único que a casa publica, mas é caixa; (2) **o CARGO NÃO É PUBLICADO**:
  o Impressum escreve apenas *"Vertreten durch"*, que é obrigação legal e não título, então **a
  carta não pode chamá-lo de Geschäftsführer, de fundador nem de diretor de arte**; (3) a casa é
  **publicidade**, não longa nem série — o ciclo é de comercial, o que costuma significar equipe
  enxuta e freela, não assento sênior fixo; (4) **não existe página de vagas** em lugar nenhum do
  site; (5) o `WORK` mostra o portfólio por cliente e **não credita função**, então não consigo
  provar que existe alguém dedicado a modelagem de personagem lá dentro.

---

### Jorge R. Gutiérrez — cofundador da Mexopolis (o site não imprime título; o texto o descreve dirigindo, escrevendo e desenhando) — Mexopolis, Estados Unidos
- **Email:** `jorge@mexopolis.com` · confiança **alta (endereço PUBLICADO)**, **com uma ressalva
  de idade que pode derrubar tudo — leia a ressalva 1** · fonte: **https://www.mexopolis.com/**,
  aberta nesta rodada; o bloco `E-mail` do rodapé publica, em texto puro, `jorge@mexopolis.com` e
  `sandra@mexopolis.com`. **NADA FOI MONTADO.** MX conferido nesta rodada por DNS:
  `10 dpmail03.doteasy.com` e `15 dpmailbu.doteasy.com` — **o domínio recebe email hoje**.
- **Por que ELE e não outra pessoa da casa:** a casa tem **duas** pessoas e as duas têm endereço
  publicado. Escolhi Jorge e não Sandra porque o próprio texto reparte os papéis: *"Jorge is
  directing, writing and designing The Book of Life"* enquanto *"Sandra is designing all the girl
  and cute characters"* — os dois são de personagem, mas quem decide o elenco inteiro e contrata é
  o diretor. **Sandra Equihua fica como SEGUNDA e última** possível.
- **Técnica:** o texto da casa diz que os dois *"have managed to blend their passion for
  over-the-top Mexican folk and popular culture with **digital animation techniques** to create
  **characters** and stories that dazzle the eye"*. Os longas dele — *The Book of Life* (Reel FX)
  e *Maya and the Three* (Netflix) — são **CG 3D estilizado com elenco enorme**, que é
  exatamente a faixa do portfólio do Vini: estilizado, não fotorrealismo.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Mexopolis is a production company
  founded in 1994 by Jorge R. Gutierrez and Sandra Equihua in Tijuana, Mexico. … Currently, the
  company is located wherever the couple live."* e o convite literal do rodapé: **"HELLO! Let's be
  friends! Drop us an email to get started!"** É uma casa que pede email por escrito.
- **Fora dos EUA?** **NÃO** — o site diz *"Dallas, Texas / USA"*. **A frase de realocação NÃO
  entra**, e a carta precisa tratar o patrocínio de visto com franqueza em vez de sugerir mudança.
- **Dedupe NA CAIXA:** `search_threads` por `"mexopolis" OR "pictak" OR "Gutierrez" OR
  "Gutiérrez" OR "carbone-14" OR "Zalcman"` devolveu **`{}`**, zero threads. No repositório,
  `mexopolis` só aparece em `censo-wikidata.csv` e `alvos-joe-wikidata.csv` (listas) e `Gutierrez`
  dá **zero**. **CASA NOVA, primeira pessoa.**
- **Ressalva honesta, e a primeira é a que decide:** (1) **O SITE ESTÁ CONGELADO EM 2013** — o
  rodapé diz *"© 1999 - 2013"* e o texto fala de *The Book of Life* como filme **em produção**,
  um longa que estreou em **2014**; ou seja, o endereço é publicado mas **a publicação tem treze
  anos**, e o MX vivo prova que o domínio recebe, **não** que a caixa dele ainda é lida; (2)
  **NENHUM CARGO É PUBLICADO** — a carta não pode chamá-lo de diretor da Mexopolis nem de nada
  além do que a página escreve; (3) **a Mexopolis NÃO CONTRATA modelador**: é a produtora pessoal
  de um casal, e a animação dos projetos dele é feita em **Reel FX**, **Tangent** e afins — o
  valor aqui é o mesmo do caso Allimator, é alguém que **conhece quem contrata**, então só o fecho
  fixo da carta faz sentido; (4) o texto diz que o filho de 4 anos está desenhando nas paredes —
  **esse filho hoje tem 17**, o que mede sozinho a idade da fonte; (5) ele é um nome grande e
  público, com agente e caixa cheia; a chance de resposta é baixa e a carta precisa ser curta.

---

### Dan Harder — dono da casa ("Sweatbox Animation is run by Dan Harder") — Sweatbox Animation ApS, Frederiksberg, Dinamarca
- **Email:** `info@sweatbox.dk` · confiança **alta (entrega)** — **mas é CAIXA, não endereço de
  pessoa** · fonte: **https://www.sweatbox.dk/about/**, aberta e lida por extenso nesta rodada;
  o bloco `Contact` no fim da página publica *"Sweatbox Animation ApS / Godthåbsvej 26B / 2000
  Frederiksberg / Email: info@sweatbox.dk / CVR: 21783609"*, e o mesmo documento abre com
  *"Sweatbox Animation is run by **Dan Harder**"*. **NADA FOI MONTADO** — e em particular **não
  montei** `dan@sweatbox.dk`, porque não existe um único endereço literal daquele domínio além da
  caixa. O rodapé diz **"2026"**, então o site está sendo mantido — o oposto do caso Mexopolis.
- **Por que ELE e não outra pessoa da casa:** o `/about` nomeia **treze** colaboradores (Thomas
  Dreyer, Anders Hald, Niels Bach, Tine Karrebæk, Ilan Hatukah, Doron Meir, Karsten Lund, Uffe
  Danielsen, Sara Koppel, Søren Itenov, Jeppe Kaas, Lasse Elkjær, Steffen Addington) e diz
  explicitamente que todos estão ligados à casa *"on a project-by-project basis"* — são freelas,
  não decisores. **A casa é o Dan Harder**, e a regra do `BRIEF-JOE` para casa de até 30 pessoas
  aponta para o dono.
- **Técnica CONFERIDA NO SITE:** o menu do site publica **`Character Design`** como uma das cinco
  seções (`Projects / Storyboard / Character Design / Animation / Commercials`), e o `/about` diz
  que entre os projetos próprios da casa está *"the **CGI feature Tivoli**"*, contrastado no mesmo
  período com *"the classically animated short To Bee or Not to Bee"* — ou seja **a própria casa
  separa o que é CGI do que é 2D**, e o longa é o CGI.
- **Gancho, com a frase do próprio estúdio entre aspas, e o nome da casa é o gancho:** o `/about`
  explica que *"the term Sweatbox comes from the room at the Disney studios where Walt used to
  review the animators' work"*, e fecha com *"the pursuit of the highest possible quality has
  always remained the priority, **regardless of style or medium**"*. Uma casa que se batizou com o
  nome da sala de revisão da Disney e que diz que a qualidade importa mais que o meio é uma casa
  que abre um portfólio. O terceiro gancho é operacional: a lista de colaboradores inclui
  *"computer graphics artists"* contratados **por projeto** — é assim que o Vini entraria.
- **Fora dos EUA?** Sim — Dinamarca, União Europeia. A frase de realocação vale, com a ressalva de
  que trabalho por projeto pode ser remoto e talvez nem precise dela.
- **Dedupe NA CAIXA:** `search_threads` por `"stormfilms" OR "Storm Films" OR "sweatbox" OR
  "Dan Harder" OR "campfireani" OR "Campfire Aniworks"` devolveu **`{}`**, zero threads. No
  repositório, `sweatbox` só aparece em `censo-wikidata.csv` e `alvos-joe-wikidata.csv` (listas).
  **CASA NOVA, primeira pessoa.**
- **Ressalva honesta:** (1) **o endereço é uma CAIXA `info@`** — vale porque numa casa de uma
  pessoa a caixa é a pessoa, mas é caixa; (2) **a casa é UMA PESSOA mais freelas** — não tem
  pipeline 3D próprio nem assento fixo, e a porta realista aqui é freela, não vaga; (3) **o grosso
  do catálogo é 2D clássico**: a casa nasceu em 1990 como *Dan Harder Animation* "providing
  classical animation", e os serviços vendidos são storyboard, character design e animação, **não
  modelagem nem groom**; (4) **o CGI Tivoli não tem data na página** e pode ser antigo — a casa
  não publica ano em nenhum projeto próprio; (5) o site não tem página de vagas.

---

### Fabian Berke — LookDev Supervisor — Red Parrot Studios, Colônia / Hamburgo / Stuttgart / Munique, Alemanha — **`sem-email`, e isso não é fracasso**
- **Email:** **NÃO EXISTE ENDEREÇO DE PESSOA PUBLICADO.** A linha entra como `sem-email`
  guardando **nome, cargo e estúdio**, como o briefing manda. A casa publica **uma única** caixa,
  `info@redparrot-studios.com`, repetida **idêntica** nos quatro escritórios — o que é prova de
  que **não há endereço por pessoa** a ser encontrado, e não apenas de que eu não achei.
  **NADA FOI MONTADO** — não montei `f.berke@`, `fabian@` nem `berke@`, porque **não existe um
  único endereço literal daquele domínio** que sirva de prova de padrão. MX conferido nesta rodada
  por DNS: `5 smtpin.rzone.de` (Strato, vivo).
- **Fonte, aberta nesta rodada:** **https://redparrot-studios.com/team/**, que publica nove
  pessoas com nome e cargo: Mohammad Farokhmanesh (Geschäftsführer, Produzent, Regisseur), Pia
  Wisgrill (VFX Producer/Projektmanagement), Maximilian Lippemeier (Produktionskoordination,
  Editor, Stoffentwicklung), Nicole Fuentes (Projektkoordinatorin), Konstantin Filippov (System
  Administrator, Technical Animator), Niclas Werres (Contentmanager, Compositing Artist),
  **Fabian Berke (LookDev Supervisor)**, Carlos Cursaro (Lead Lighting und LookDev Artist) e
  Franzi Roth (Projektmanagerin). Também aberta: **https://redparrot-studios.com/kontakt/**, que
  confirma a caixa única.
- **Por que ELE e não outra pessoa da casa:** dos nove, **seis são produção, coordenação ou TI**.
  Sobram três de ofício, e o `BRIEF-JOE` manda ir no mais alto do ofício certo: Konstantin
  Filippov é **Technical Animator**, que é rigging e está **fora da disciplina**; Carlos Cursaro é
  **Lead** de lighting e lookdev; **Fabian Berke é o SUPERVISOR de LookDev**, ou seja o cargo mais
  alto de superfície da casa — e superfície, textura e shading são metade do dia do Vini. **Não é
  lead de ambiente**, então a regra de 10/09 está respeitada. Mohammad Farokhmanesh
  (Geschäftsführer) fica como **SEGUNDA e última** possível.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Postproduction ist unsere Welt – von
  der Konzeption bis zur technischen Umsetzung."* A casa tem **página de Karriere** própria e
  quatro escritórios alemães.
- **Fora dos EUA?** Sim — Alemanha, União Europeia. A frase de realocação vale inteira.
- **Dedupe NA CAIXA:** `search_threads` por `"redparrot" OR "Red Parrot"` (dentro da consulta
  conjunta com SERU, Keweloh, Parekh e Harder) devolveu **cinco threads e nenhuma desta casa** —
  todas falso positivo da palavra inglesa *harder*, conferidas uma a uma. No repositório,
  `redparrot` e `Red Parrot` só aparecem em `censo-wikidata.csv` e `alvos-joe-wikidata.csv`
  (listas). **CASA NOVA.**
- **Ressalva honesta, e ela é a mais dura da rodada:** (1) **não há endereço para escrever** — sem
  um endereço de pessoa, esta ficha só vira carta se o maestro aceitar gastar a casa na caixa
  `info@`, e aí o alvo deixa de ser o Fabian; (2) **a casa não escreve 3D de personagem em lugar
  nenhum**: a autodescrição é *postprodução*, as seções são `Animation` e `VFX`, e **não abri
  prova de elenco de personagem** — o que existe são **cargos** (LookDev, Lighting, Technical
  Animator) que **implicam** pipeline 3D, e implicação não é prova; (3) LookDev não é modelagem
  nem escultura — é o vizinho do ofício do Vini, não o ofício dele; (4) é casa de **serviço de
  postprodução com quatro endereços e nove pessoas**, ou seja provavelmente muito freela por
  projeto, o que é porta e não assento.

---

### O QUE MORREU NESTA RODADA, E POR QUÊ — para a próxima rodada não reabrir

**O aviso do maestro se confirmou na prática.** Abri **43 estúdios à mão** da
`alvos-joe-wikidata.csv` (mais a varredura automática de **153 domínios × até 20 caminhos**,
cerca de 3.060 requisições) e a maioria **não faz 3D**. Nenhum destes deve voltar:

**Mortos por TÉCNICA — conferida no site, não no rótulo do Wikidata:**
- **Nørlum** (DK) — o site rotula os próprios projetos como *"2D animation"*. 2D puro.
- **A+C Studios** (UK) — **stop motion** declarado: claymation, papercraft, stop-frame.
- **Owl House Studios** (UK) — **a definição do próprio site desmente o rótulo**:
  *"3D Animation: **Layering of multiple 2D animated objects** to create a multi-dimensional
  movie"*. Isso é 2.5D, não CG.
- **Winding Snake Productions** (UK) — *"creatively driven **2D** animation studio"*.
- **Studio Huckepack** (DE) — *"big love for **2d** animation, quirky styles & storytelling"*.
- **Red Dog Culture House** (KR) — o cabeçalho do site é literalmente *"2D Animation Studio"*.
- **Studio Croma** (IT) — stop motion.
- **one and a half** (CY) — 2D de documentário; Yiannis Philiastides é Founder/Creative Director
  mas só há `info@`.
- **Global Mechanic** (CA) — **este é o caso Krystallplaneten desta rodada**: publica
  `bruce@globalmechanic.com` (Bruce Alcock, Creative Director & Owner) e
  `brodie@globalmechanic.com` (Chris Brodie, Executive Producer), dois endereços de pessoa
  prontos — **e a página de projeto derruba a ficha**: o *Jam Van* é *"a blend of multiple
  animation styles and live action"*, com personagens que são *"a mix of drawings and
  phototextures"* e stop-motion de papel feito pela parceira Dadomani. **Mixed media, não CG.**
  Se alguma rodada futura quiser gastar aqui, saiba que está gastando fora da disciplina.
- **Pictak Cie** (FR) — publica `xavier@pictak.fr` em `/` e `/contact`. Morre por técnica:
  Xavier Picard dirigiu *Moomin on the Riviera* e *Prince's Voyage*, **ambos 2D**, e o único
  projeto no site está *"IN DEVELOPMENT"* sem técnica declarada.

**Mortos por IDENTIDADE — o rótulo do Wikidata está errado sobre o que a casa é:**
- **Creative Beards** (NL) — *"2D and 3D **explanatory** animations, infographics"*. Vídeo
  explicativo corporativo, não personagem.
- **Unagi** (CA no Wikidata) — **falso amigo duplo**: é um *studio de communication* em **PARIS**,
  com motion design institucional e **podcast**. Nem o país nem o setor batem.
- **Image Entertainment Corporation** (CA) — publica `s.viau@image-cie.com` com o nome do fundador
  Sylvain Viau, **e é DISTRIBUIDORA**: *"s'est donnée pour mission de faire rayonner des films à
  fort potentiel sur le marché international"*. Não produz animação.
- **Animated Company** (UK) — *"**AI** Animation & VFX Studio"*.
- **Storm Films** (NO) — produtora de longa; o único endereço publicado é `mbg@stormfilms.no`,
  **sem nome ao lado**, e não há técnica declarada em página nenhuma que abriu.
- **ROI VISUAL** (KR) — licenciamento e IP (ROI TOYS, ROI BOOKS), só `license@`.
- **Zinkia** (ES), **Fifth Degree** (BG), **Doze Studio** (FR) — nenhuma pessoa publicada e
  nenhuma técnica de personagem declarada; a Doze é publicidade e identidade visual.

**Mortos por SITE/DOMÍNIO, medido hoje:**
- **Rovio Animation** (FI) — `rovioanimation.com` **não resolve DNS**. Domínio morto.
- **DogHead Animation Studio** (IT) — `dogheadanimaton.com` **não resolve DNS** (e note que o
  domínio publicado no Wikidata está grafado errado, sem o `i` de *animation*).
- **Blender Animation Studio** (NL) — `studio.blender.org` respondeu **HTTP 403**. Fica como
  **NÃO CONFERIDO**, não como morto: é 3D de verdade e é Holanda, a rota número um. **Vale
  retomar com outro caminho.**
- **Caribara Animation** (FR) — **HTTP 503**. Também **NÃO CONFERIDO**.
- **SAMG Entertainment** (KR), **TRIKK17** (DE), **Yapiko** (FR), **Timeless Films** (UK) —
  páginas servidas por JS, sem pessoa e sem técnica legível.

**Fora por TETO ou por já terem sido gastas — e a nWave é a lição da rodada:**
- **nWave Pictures** (BE) — **teto de duas atingido, e as DUAS QUICARAM**:
  `edillens@nwave.com` (28/08) e `cgrao@nwave.com` (03/09), as duas com
  *"Delivery Status Notification (Failure) — endereço não encontrado"*, mais uma candidatura
  espontânea via BambooHR em 11/07. **Os dois endereços eram MONTADOS por padrão de domínio.**
  É a regra dos 5 quicados em 8 acontecendo numa casa só. **Nunca mais.**
- **Giant Animation** (IE) — carta em 26/08 e follow-up em 02/09 para `hello@giant.ie`. Resta uma
  aproximação, mas a casa é 2D.
- **Aardman** (UK) — carta em 09/09 para `pauline.mallam@aardman.com`. Resta uma.
- **b.water Animation Studios** (DE/ES) — teto: carta em 26/08 e **resposta humana** de Idayra do
  Operations Department em 26/08. Casa já ativa, não reabrir a frio.

---

# RODADA DO JOE, 16/09 03h35 UTC — SEIS FICHAS, **TODAS COM ENDEREÇO PUBLICADO**, ZERO MONTADO

**A rodada foi pedida com uma prioridade só: ENDEREÇO PUBLICADO**, porque o lote do maestro está
travado por falta de endereço e não por falta de nome (doze das quinze fichas pendentes são
`sem-email`). **As seis abaixo têm endereço visto escrito literalmente, com a URL exata, e
nenhuma linha desta rodada tem endereço montado por padrão de domínio.**

**E a `alvos-joe-wikidata.csv` não foi o que rendeu — vale registrar por quê.** Recorrida com um
rastreador que, diferente da varredura de caminhos chutados de 15/09, **segue os links internos
reais** de cada site (`/contact`, `/team`, `/about`, `/impressum`, `/kontakt`, `/over-ons`,
`/jobs` …) e **decodifica `data-cfemail` do Cloudflare**, a lista de 167 casas devolveu endereço
de pessoa em pouquíssimos domínios, e **um só virou ficha** (MovieBrats). O que rendeu de verdade
foi **`automacao/garimpo-cgstudiomap.csv`**: 480 casas de CG/VFX/animação que o repositório já
conhecia por quadro de vaga e que **nunca receberam carta nenhuma**. São 4 das 6 fichas.

| Pessoa | Cargo | Casa | País | Endereço | Confiança |
|---|---|---|---|---|---|
| Kaj Steveman | CEO & Executive Producer | FABLEfx | Suécia | `kaj@fablefx.com` | alta, publicado |
| Nicolas Fuminier | Partner, Head of 3D & compositing | Studio Kippik | França | `nicolas@kippik.fr` | alta, publicado |
| Tom Schirdewahn | VP Art & Creative | MovieBrats Pictures | Alemanha | `tom@moviebratspictures.com` | alta, publicado |
| Jon Campfens | Co-founder / VFX Supervisor | Switch VFX & Animation | Canadá | `jonc@switchent.com` | alta, publicado |
| Bill Otomo | Directeur artistique / Auteur graphique | La Chouette Compagnie | França | `bill@chouettecie.com` | alta, publicado |
| Maarten Braaksma | Project Lead | Buckethead Entertainment | Holanda | `maarten@bucketheadentertainment.com` | alta, publicado |

---

### Kaj Steveman — **CEO & Executive Producer** — FABLEfx, Estocolmo, Suécia (com braço em Londres) — **a ficha mais forte da rodada, e a disciplina é literal**

- **Email:** `kaj@fablefx.com` · confiança **alta** · **PUBLICADO**, com nome e cargo na mesma
  linha, em **https://www.fablefx.com/contactus**, aberta nesta rodada: *"CONTACT Kaj Steveman -
  CEO & Executive Producer kaj@fablefx.com"*.
- **Por que ELE e não outra pessoa da casa:** a página de contato publica **duas** pessoas, e a
  outra é **James Prosser, Studio Director FABLEfx UK**, cujo endereço é
  `james.prosser@fablefx.co.uk` — **outro domínio**. Casa boutique e "cloud-based": pelo
  `BRIEF-JOE`, em casa pequena o alvo é o fundador/CEO, que responde ele mesmo. James Prosser fica
  como **SEGUNDA e última** possível. **Atenção de método:** o domínio do braço britânico é
  `fablefx.co.uk` e o do sueco é `fablefx.com` — é a armadilha da Stunlock outra vez, e é a prova
  de que **endereço literal vence padrão**: montar `james.prosser@fablefx.com` teria quicado.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"At FABLEfx, we specialise in digital
  animals. With VFX experience since the 1990s, we are experts in Creature FX. Our Digital Zoo
  features over 120 ready-to-use animal assets"*, e a frase que fecha o encaixe com o portfólio do
  Vini: *"We handle everything from **creature design, asset build** and animation to rendering and
  compositing, delivering photorealistic creations with true soul."* O slogan do site é **"Your
  Digital Zoo"**. Animal fotorrealista é **modelagem, escultura, superfície e PELO** — ou seja o
  **grooming em Houdini** entra aqui por direito, e não como enfeite.
- **A casa convida por escrito, e isso muda o tom da carta:** em
  **https://www.fablefx.com/careers** está *"Open Application — We are always looking for talented
  people so feel free to send in an open application to make us aware about what you could bring to
  the flock."* E no rodapé do contato: *"No open position and you still think you're a perfect
  match? Send your awesome reel to: careers@fablefx.com"*. A carta **não** deve ir para
  `careers@`: o endereço da pessoa existe e é melhor porta.
- **Fora dos EUA?** Sim — Suécia (Estocolmo), União Europeia, com sociedade britânica separada
  (FABLEfx UK LTD, Covent Garden). A frase fixa de realocação entra inteira.
- **Dedupe NA CAIXA:** `search_threads` por `fablefx OR "FABLEfx" OR Steveman` devolveu **zero**.
  No repositório, `fablefx` só aparece em dois lugares e **nenhum é carta**:
  `automacao/garimpo-cgstudiomap.csv` (08/09, checagem de quadro de vaga: *"a pagina de carreiras
  responde HTTP 200 mas o corpo tem apenas 290 caracteres… PRECISA DE NAVEGADOR"*) e
  `automacao/BRIEF-JHON.md` (07/09, o caso do **Airtable embutido** que não desenha campo pelo
  proxy). **A casa nunca recebeu carta. PRIMEIRA pessoa desta casa.**
- **Ressalva honesta:** (1) o cargo é **CEO e Executive Producer**, ou seja produção e negócio, não
  direção de arte — ele decide, mas não desenha; (2) a palavra **"Creature FX"** aparece na
  autodescrição e na ILM ela significa **simulação**, que está fora da disciplina do Vini — o que
  salva a ficha é a mesma página escrever *"creature design, asset build"* com todas as letras, e é
  **essa** parte que a carta deve citar, não a sigla; (3) o catálogo é **publicidade** (D&AD, Clio,
  Epica, LIA), não longa nem série, então é trabalho curto e por projeto; (4) o quadro de vagas
  monta em JavaScript e o formulário é **Airtable**, que já foi medido como ilegível por esta rede
  — **a carta é a única porta legível daqui**, e isso é argumento a favor dela.

---

### Nicolas Fuminier — **Partner, Head of 3D & compositing** — Studio Kippik, Paris, França — **a casa que escreve "Sculpting" na própria lista de ofícios**

- **Email:** `nicolas@kippik.fr` · confiança **alta** · **PUBLICADO** com nome e cargo no mesmo
  cartão, em **https://www.kippik.fr/about-us**, aberta nesta rodada. O HTML cru confirma o
  pareamento sem ambiguidade: `<div>Nicolas <br/>Fuminier</div><div>Partner</div><div>Head of 3D
  &amp; compositing</div><a href="mailto:nicolas@kippik.fr">`.
- **Por que ELE e não outra pessoa da casa:** a casa publica **três sócios, os três com endereço**
  — Anaëlle Moreau (Partner, **Head of animation**, `anaelle@kippik.fr`), Thomas Poulain (Partner,
  **Artistic director**, `thomas@kippik.fr`) e ele. **Nicolas é o chefe do 3D**, e o que o Vini faz
  — escultura, modelagem, textura e shading de personagem — mora inteiro debaixo desse cargo.
  Anaëlle é animação, que não é o ofício dele. Thomas Poulain fica como **SEGUNDA e última**
  possível, e é o alvo natural se o Nicolas não responder.
- **Gancho, com a frase do próprio estúdio entre aspas:** a lista de ofícios que a casa publica é
  literalmente *"Direction · Art direction · Production · **Character design** · Rigging ·
  Animation · Environment Design · **Sculpting** · **Texturing / Shading** · Rendering · Editing ·
  Grading"*, e ao lado dela: *"We are a parisian animation studio founded in 2012 by three former
  students of the Ecole Nationale Supérieure des Arts Décoratifs de Paris"* e *"To guarantee
  creative excellence, **we keep the whole production process internal**."* Essa última é o ponto
  de apoio da carta: pipeline interno quer dizer que o personagem é feito ali dentro, não
  terceirizado.
- **Fora dos EUA?** Sim — França (3 square de la Tour Maubourg, Paris 7e), União Europeia.
- **Dedupe NA CAIXA:** `search_threads` por `kippik` (na consulta conjunta com chouette, switchent
  e lagoonstudios) devolveu **zero**, e a busca por `Fuminier` também. No repositório, `kippik` só
  aparece em `automacao/garimpo-cgstudiomap.csv`, numa checagem de **quadro de vaga** de 08/09
  (*"Pagina de carreiras lida (mailto:jobs@kippik.fr): nenhum titulo da disciplina"*). **Nenhuma
  carta saiu para esta casa. PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) é casa **pequena** — três sócios e equipe enxuta, *"Our scale enables
  us to provide the upmost focus on each project"* — então não há assento fixo de character artist
  esperando; (2) o trabalho publicado é **animação autoral e publicidade**, não longa nem jogo, e o
  estilo é declarado *"handcrafted"*, o que costuma querer dizer estilizado e não fotorrealista;
  (3) existe `jobs@kippik.fr` publicado, e é preciso **não** usá-lo: a carta perde a pessoa;
  (4) o site data de 2023 no rodapé, então os três cargos podem ter mudado — o pareamento
  nome-cargo-endereço está no HTML de hoje, mas hoje é a data da página, não a da checagem de RH.

---

### Tom Schirdewahn — **VP Art & Creative** — MovieBrats Pictures, Berlim e Erfurt, Alemanha — **a única ficha que saiu da lista do Wikidata**

- **Email:** `tom@moviebratspictures.com` · confiança **alta** · **PUBLICADO** com nome, cargo e
  endereço no mesmo cartão de equipe, em **https://moviebratspictures.com/company**, aberta nesta
  rodada. HTML cru: `<div class="name">Tom Schirdewahn</div><div class="position">VP Art &
  Creative</div>…<a href="mailto:tom@moviebratspictures.com">`.
- **Por que ELE e não outra pessoa da casa:** a página publica **quatro** pessoas e três delas são
  negócio — Esther Friedrich (CEO/Producer), Alexander Weimer (Partner/Producer, e o endereço dele
  é a **caixa** `hello@`) e Uyen Gia Ha (Head of Marketing). **Tom Schirdewahn é o único cargo de
  ARTE da casa inteira**, e o título diz "VP **Art** & Creative". Não é lead de ambiente, então a
  regra de 10/09 está respeitada. Esther Friedrich fica como **SEGUNDA e última** possível.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"MovieBrats Pictures is an independent
  film production house with offices in Berlin and Erfurt, developing, producing, and co-producing
  commercially viable, high-quality feature films and serial content in both, live-action and
  animation."* E o projeto que dá o gancho de personagem: *"the **3D animated** fantasy comedy
  **THE DUMPLING QUEEN**, a co-production with China"*, cuja sinopse publicada em
  **https://moviebratspictures.com/projects/the-dumpling-queen/** diz que a protagonista vence a
  concorrência *"by **summoning magically animated food spirits** to help her run her kitchen"* —
  elenco de criaturas, que é exatamente o que o Vini modela. A mesma página marca a seção **Visual
  Development** e o projeto está em **Development**, que é a fase em que se escolhe quem faz o
  elenco.
- **Fora dos EUA?** Sim — Alemanha (Berlim e Erfurt), União Europeia. Frase de realocação inteira.
- **Dedupe NA CAIXA:** `search_threads` por `moviebrats OR moviebratspictures OR Schirdewahn`
  devolveu **zero**. No repositório há **uma** ocorrência, e ela **não é carta**: em 07/09 o agente
  europeu registrou a casa num lote de `checado-sem-vaga` em `automacao/processados.csv`
  (*"checados individualmente, sem vaga da disciplina ou fora do ramo"*), e o
  `europa-mr-reabertos-07-09.csv` guarda a leitura do domínio antigo `moviebrats.com`. **Conferi a
  identidade**, porque dois domínios parecidos já enganaram esta campanha nove vezes:
  `moviebrats.com` **redireciona para o mesmo site** e o rodapé dos dois é `© MovieBrats Pictures
  GmbH`. É a mesma casa, e ela **nunca recebeu carta**. PRIMEIRA pessoa.
- **Ressalva honesta:** (1) é **produtora**, não estúdio com pipeline próprio — *"developing,
  producing, and co-producing"* — e a Dumpling Queen é **co-produção com a China** (Huawen
  Pictures, Gravity Pictures), então a execução do 3D provavelmente acontece lá e não em Berlim;
  (2) o resto do catálogo é **live action** (ZOOLOGY, GEISTER, THE TUPILAQ) e o outro projeto
  animado, ADAM, é **2D/3D** dirigido pelo time de *I Lost My Body*, que é 2D; (3) a casa não tem
  página de vagas nenhuma — é carta de porta, não de vaga; (4) a foto do Tom no site tem caminho
  `wp-content/uploads/**2016**/07/`, ou seja o cartão dele está no ar há muito tempo — o cargo
  **pode estar desatualizado**, e cargo velho é pior que alvo nenhum.

---

### Jon Campfens — **Co-founder Switch VFX / VFX Supervisor** — Switch VFX & Animation, Toronto, Canadá — **e o Canadá é o país número um do BRIEF-JOE**

- **Email:** `jonc@switchent.com` · confiança **alta** · **PUBLICADO** no cartão dele em
  **https://www.switchent.com/about-us/**, aberta nesta rodada. HTML cru: `<h5>Jon Campfens</h5>
  <h6>Co-founder Switch VFX / VFX Supervisor</h6> … <a href="mailto:jonc@switchent.com">`.
- **Por que ELE e não outra pessoa da casa:** a casa publica **dois** fundadores, e o outro é
  **Pete Denomme, Executive Producer / CEO** (`peted@switchent.com`), que é produção. **Jon é o
  supervisor de VFX**, ou seja o lado de ofício, quem olha reel e decide quem entra num projeto.
  Pete Denomme fica como **SEGUNDA e última** possível.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Two Talents. One Switch."* e *"Our
  studio can imagine and engineer every aspect of a production pipeline to create original series
  that are inspiring and sought after PLUS we can do service work that is superior."* O gancho
  pessoal, e ele é verificável na própria bio publicada: Jon *"has spent three decades working in
  the film industry… worked with some of the most creative Directors including **Guillermo del
  Toro**, Norman Jewison, and **David Cronenberg**"*, com indicação ao Emmy e prêmio Gemini. A casa
  também paga o **Switch Scholarship** em cinco faculdades de Ontário e hospeda o **Animation
  Lounge** — é casa que fala com quem está chegando, e isso é argumento para a carta fria.
- **Fora dos EUA?** Sim — Canadá (128a Sterling Road, Toronto). **Canadá é o topo da ordem de
  país do `BRIEF-JOE`**, e é onde a carta precisa dizer de frente que ele precisa de patrocínio,
  porque é o item que o RH usa para cortar e o supervisor é quem atropela.
- **Dedupe NA CAIXA:** `search_threads` por `switchent OR "Switch VFX"` e por `Campfens` devolveu
  **zero** nas duas. No repositório, `switchent` só aparece em `automacao/garimpo-cgstudiomap.csv`,
  e a linha diz exatamente que a casa **não tem quadro de vagas achável**: *"MEDIDO 08/09: o site
  RESPONDE, mas nao achei pagina de carreiras. Varri os links da home, chutei 14 caminhos"*.
  **Nenhuma carta. PRIMEIRA pessoa.** E a ausência de quadro é justamente o caso em que a carta
  para pessoa é a única porta.
- **Ressalva honesta:** (1) o único recado de contratação que a casa publicou é *"Join Our
  Compositing Roster!"* — **composição, não personagem**, e a carta não pode fingir que é resposta
  a isso; (2) VFX Supervisor supervisiona o plano inteiro, não o elenco: não há prova publicada de
  que a casa faça **criatura ou personagem CG**, o que há é uma divisão de **Animation** com
  séries próprias; (3) o Canadá exige patrocínio e a campanha já levou veto escrito de autorização
  em casas canadenses; (4) `switchinfo@switchent.com` é a caixa geral e **não** deve ser usada.

---

### Bill Otomo — **Directeur artistique / Auteur graphique** — La Chouette Compagnie, Montreuil e Angoulême, França — **e o email mora em OUTRO domínio**

- **Email:** `bill@chouettecie.com` · confiança **alta** · **PUBLICADO** na seção *"La chouette
  équipe"* de **https://www.chouetteco.com/**, aberta e lida no HTML cru nesta rodada. O `mailto:`
  **envolve a foto dele** (`alt="bill.png"`), e o cartão ao lado traz *"Bill OTOMO"* com
  *"Directeur artistique"* e *"Auteur graphique"*.
- **ATENÇÃO, e é a lição de método desta ficha:** o site é **`chouetteco.com`** e **todos os
  endereços são `@chouettecie.com`**. Qualquer endereço montado sobre o domínio do site teria
  quicado. É a mesma armadilha da Stunlock, e é o motivo de esta campanha só aceitar endereço
  visto escrito.
- **Por que ELE e não outra pessoa da casa:** a página publica **dez** pessoas com nome e cargo, e
  **nove** endereços. Sylvain Dos Santos (Directeur de la création) e Mariam Hachmi (Directrice
  générale) são a chefia; Gaelle Autin e Charles Lefebvre aparecem como **Réalisateur/trice** e
  também directeur/trice artistique, mas **o Charles não tem endereço publicado**; Claire Sun é
  **Concept Artist** (2D); o resto é produção, jurídico, escrita e administração. **Bill Otomo é o
  diretor artístico com endereço publicado**, ou seja a cadeira que decide como o elenco de uma
  série CG se parece. Sylvain Dos Santos fica como **SEGUNDA e última** possível.
  *Como o pareamento foi feito, para ninguém ter de refazer:* o Wix embaralha a ordem do texto,
  então cruzei duas provas independentes — o `mailto:` está ancorado na **foto de cada pessoa**
  (`bill.png`, `claire.png`, `marie hermelin.png`…) e **a parte local de cada endereço é o primeiro
  nome**, único dentro da equipe (`bill`, `gaelle`, `claire`, `antoine`, `marie`, `brice`, `moira`,
  `sylvain`, `mariam`, `guillaume`).
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Fondée fin 2014, la Chouette compagnie
  développe, produit et exploite des séries d'animations en partenariat avec les principaux acteurs
  français et internationaux du secteur."* O catálogo é elenco puro: **DRONERS** (52 x 26'),
  **AZURO & la brigade des dragons** (52 x 11'), **LE MONDE SELON KEV**, **IMAGO**, e em 2026 a
  casa *"produit et livre **DRAGON STRIKER** pour **DISNEY+**, **DREAMLAND** pour ADN, **TAKI
  TANUKI** pour France Télévisions"*. Uma brigada de dragões e um *Dragon Striker* na Disney+ são,
  literalmente, criatura para modelar. A página ainda tem a seção **"envie de nous rejoindre?"** e
  um anúncio vivo (Head of International Sales), o que prova que a casa está contratando.
- **Fora dos EUA?** Sim — França (Montreuil e Angoulême), União Europeia.
- **Dedupe NA CAIXA:** `search_threads` por `chouette OR chouettecie` e por `Otomo` devolveu
  **zero** nas duas. No repositório, `chouette` aparece em `automacao/garimpo-cgstudiomap.csv`
  (08/09: *"a pagina de carreiras responde HTTP 200 mas o corpo tem apenas 409 caracteres… o quadro
  monta em JavaScript"*) e uma vez em `fila-remotegamejobs-estudios.csv`, que é **outra coisa**
  (`chouette.itch.io`, da *Jellyfish Parade*, nos Estados Unidos — falso amigo conferido e
  descartado). `chouettecie` não existe em lugar nenhum do repositório. **Nenhuma carta. PRIMEIRA
  pessoa.**
- **Ressalva honesta:** (1) a Chouette se descreve como quem **"développe, produit et exploite"** —
  é **produtora de séries**, e a fabricação do 3D costuma acontecer em estúdio parceiro, então a
  carta não pode afirmar que ela tem pipeline interno; (2) Bill Otomo é **autor gráfico e diretor
  artístico**, ou seja o lado **2D** do desenho de personagem, e o Vini é 3D — o encaixe é "quem
  decide como o personagem se parece", não "quem faz o mesmo que eu"; (3) a casa tem **dois
  endereços físicos** e é pequena; (4) a página não diz a técnica projeto a projeto, e foi
  exatamente isso que derrubou a Krystallplaneten — aqui o que sustenta o 3D é o formato das
  séries e as emissoras, não uma frase da casa dizendo "CGI".

---

### Maarten Braaksma — **Project Lead & Programmer (o estúdio é ele e mais um)** — Buckethead Entertainment VOF, Holanda — **a rota holandesa, e é a ficha mais fraca da rodada**

- **Email:** `maarten@bucketheadentertainment.com` · confiança **alta** · **PUBLICADO** no bloco de
  equipe da home, **https://www.bucketheadentertainment.com/**, aberta nesta rodada: o cartão traz
  *"Maarten Braaksma — Project Lead & Programmer"* e um `mailto:` direto ao lado dos links de
  LinkedIn e ArtStation dele.
- **Por que ELE e não outra pessoa da casa:** **é a única pessoa que a casa publica.** Casa de
  porte mínimo (VOF, a sociedade simples holandesa), onde o `BRIEF-JOE` manda ir no dono — e o
  próprio site diz, sobre ele, *"If you're doing business with someone, then it's with him."*
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Welcome to the Buckethead
  Entertainment web page! **Gameplay is king**"*, e o jogo deles, **RUMBLE**, é descrito assim:
  *"You're a beginning martial artist with the power to control stone. By striking poses inspired
  by real-life fighting sports, you can create attacks out of the earth beneath your feet. Test
  your skills and creativity in the online PVP arena!"* Jogo de luta em primeira pessoa é elenco:
  corpo, silhueta, material.
- **Fora dos EUA?** Sim — Holanda (a casa não publica cidade; publica só a forma jurídica,
  `Buckethead Entertainment VOF`). **Holanda é a rota número um desta rodada.**
- **Dedupe NA CAIXA:** `search_threads` por `buckethead OR Braaksma` devolveu **zero**. No
  repositório, `bucketheadentertainment` **não aparece em arquivo nenhum**. **CASA NOVA, PRIMEIRA
  pessoa.**
- **Ressalva honesta, e ela é a mais dura das seis:** (1) o cargo é **Project Lead & Programmer** —
  **não é arte**, e o `BRIEF-JOE` só o aceita porque em casa de duas pessoas o dono é quem decide;
  (2) a casa **não publica vaga nenhuma** e não tem página de carreiras; (3) o portfólio é
  **RopeRaid** (2019, AirConsole) e **RUMBLE**, com *"Release date: Soon™"* ainda escrito na home,
  ou seja o site está desatualizado; (4) o link de ArtStation do cartão dele aponta para a **home
  do ArtStation**, sem perfil, então não dá para conferir trabalho de arte nenhum ali; (5) a casa é
  de **gameplay**, e a própria manchete diz isso — arte de personagem não é o que ela vende.

---

### O QUE MORREU NESTA RODADA, com a medição, para a próxima não reabrir

**Mortos por TÉCNICA, conferida no site e não no rótulo:**
- **Fabelfjord** (NO, Tromsø) — chegou perto e caiu na regra da Krystallplaneten. Publica **dois**
  endereços de pessoa em `https://fabelfjord.squarespace.com/kontakt-1` (Endre Lund Eriksen,
  `endrele@`, e **Endre Skandfer, "Art director, regissør", `endres@fabelfjord.no`**), e o Skandfer
  tem bio forte: *"mer enn femten års bakgrunn fra animasjons-bransjen"*, ex-**Qvisten**, **Storm
  Studios** e **Mikrofilm**. **Mas o site inteiro não declara 3D nem CG em lugar nenhum**: a única
  ocorrência da palavra "3D" no domínio é *"Kortfilm i stereoskopisk 3D"*, que é estereoscopia de
  captação, não computação gráfica. Catálogo de curtas e livros ilustrados. **Endereço ótimo,
  técnica errada.**
- **MICO Studio** (KR) — o domínio `micostudio.com` hoje é o **MAGIC IMAGE Group**, e a página de
  capacidades diz *"2D 애니메이션 전통적인 2D 애니메이션 제작 전문"* (especialista em 2D tradicional),
  com o resto do site vendendo OTT, comércio e IA. Publica `ken@` e `stevejeon@`, mas é 2D.
- **Vizlab Studios** (DK, Viborg), **Good Job Studios** (DK), **Drawesome Films** (DK),
  **Helping Hand** (NO), **Shortcut** (NO), **Studio Kamp**, **Animal Motion** e **Studio Ranokel**
  (DE) — todos com endereço de pessoa publicado e **todos fora da disciplina**: a Vizlab é
  **concept art** (o time inteiro é Concept Artist, com link de ArtStation e nenhum email de
  artista publicado); a Good Job é *"animated illustration & soundtracks"*; a Drawesome é animação
  educativa 2D; a Helping Hand é um freela com *"AI Hybrid"* no menu; a **Shortcut Oslo** publica
  **dezoito** pessoas com nome, cargo e email, e **não há um único cargo de 3D** — é montagem, cor,
  som e ADR; a Studio Kamp é **sound design**; a Animal Motion é *"Freelance 2D Artist in Hamburg"*;
  a Studio Ranokel é ilustração.
- **Onirixel**, **Jokyo Images**, **Studio Raclette**, **Firm Studio**, **Les Androïds Associés**
  (FR) — os cinco publicam pessoa e os cinco são outra coisa: 3D de produto e institucional, color
  grading e evento, 3D de packshot e imobiliário, pós-produção de publicidade, e **previs**
  (a Androïds é *"a previs company"*, ou seja layout e câmera).

**Morto por VETO ESCRITO, e vale registrar a frase:**
- **Gimmick Visual Effects** (DK, Copenhague) — publica `keto@gimmick.dk` com nome e cargo (*"Ulla
  Keto, Studio Manager"*) e ainda convida artista: *"We are always looking for talented artists"*,
  pedindo Maya, Houdini ou Nuke. **Mas a mesma página escreve a condição: "Work permit for the EU
  is needed."** Isso é veto escrito de autorização, exatamente o que a campanha usa para descartar.
  Fica registrado com a frase para ninguém gastar carta aqui.

**Morto por IDENTIDADE, e os dois são falso amigo de rótulo:**
- **Gutsy** (FI) — o diretório promete o time de **Moominvalley**, que é CG. O site
  `gutsy.fi` é hoje **Gutsy Pictures**, produtora de TV em live action, e a própria bio da Katherine
  Senior diz que ela *"worked at Gutsy **Animations**"* no passado. Pior: a home avisa *"Gutsy
  Pictures does not accept unsolicited material."* **Casa errada e porta fechada por escrito.**
- **ICE VFX** — o `garimpo-cgstudiomap.csv` registra **Canadá**; a página de contato publica
  telefone **+52** e endereço na **Colonia Roma, Ciudad de México**. É **México**, não Canadá.
  Correção de dado, não ficha.
- **Karandash** (`krndsh.com`) — publica três endereços de pessoa com rubrica (CEO, vendas e
  **Career Opportunities**), mas é da **Ucrânia**, que não é Reino Unido, Irlanda, nórdico nem UE:
  **fora do escopo geográfico** escrito no `BRIEF-JOE`. A mesma página ainda tem lixo do tema
  (`techlink@qode.com`, um endereço em Brooklyn), o que é aviso de site montado sobre template.

**O que NÃO rendeu, com número, para não se repetir:**
- A **`alvos-joe-wikidata.csv` está praticamente esgotada**. Recorri as 167 casas com rastreador de
  links reais (não caminhos chutados) e decodificação de `data-cfemail`: das casas em país de rota
  preferida, **só Fabelfjord e Mistral Film Studio** (Düsseldorf, `keydel@mistralfilmstudio.com`,
  técnica não declarada) trouxeram endereço de pessoa inédito, e nenhuma das duas passou no filtro
  de técnica. **Uma única ficha saiu da lista inteira.**
- **546 casas de país de rota preferida** (Holanda, nórdicos, Alemanha, Áustria, Irlanda e Reino
  Unido) tiradas do `censo-wikidata.csv` **sem nenhuma aparição no repositório**, rastreadas por
  link interno: **87 com endereço de pessoa**, e quase todas são estúdio de jogo indie de uma a
  três pessoas, sem pipeline 3D. **Uma virou ficha** (Buckethead).
- **Varredura de `presskit()`** (`/press`, `/presskit`, `/press-kit`, `/pressroom` …) nas mesmas 546
  casas: **29 domínios com endereço de pessoa, zero da disciplina.** Foi assim que o Tim Remmers da
  Team Reptile apareceu em 12/09, então a veia existe — mas neste universo ela rendeu zero.
- **Curadoria alemã e austríaca de VFX e animação 3D** (Ambient Entertainment, Ulysses, RISE,
  Lavalabs, Scopas, Studio Rakete, NHB, Tempomedia, Cartoon-Film, Optix, Toon2Tango, Studio 100
  Media, Wunderwerk, Arx Anima, Neopixel, Sproing, Bongfish, Mi'pu'mi e mais): **zero endereço de
  pessoa novo**. A única coisa que apareceu foi `claudia.hennekemper@toon2tango.com`, na **política
  de privacidade** e no papel de encarregada de dados, não de arte.
- **A lista de membros da AG Animationsfilm** (`ag-animationsfilm.de/netzwerk/mitglieder`, 146
  links) é quase toda de **artista individual e casa de 2D ou stop motion**, e não de estúdio 3D.
  Rendeu as três mortes alemãs acima. Não vale outra rodada.

**A veia que rendeu, e é para repetir:** `automacao/garimpo-cgstudiomap.csv` tem **480 casas de
CG, VFX e animação com site vivo que nunca receberam carta nenhuma** — elas entraram no
repositório em 08/09 só para checar **quadro de vaga**, e o quadro é justamente o que quase
nenhuma delas publica de forma legível por `curl`. Quatro das seis fichas de hoje saíram dali.
**Sobram 35 do Canadá, 40 do Reino Unido, 27 da Dinamarca, 12 da Noruega, 8 da Suécia e 218 da
França ainda não lidas uma a uma.**

---

## RODADA DE 16/09 (Joe, tarde) — A VEIA QUE RENDEU FOI O `presskit()`, E ELA CORRIGE UM NEGATIVO DE 07/09

**O método desta rodada, em uma linha:** casa já qualificada pela campanha (carta em caixa
genérica, sem resposta) **mais os caminhos `/press`, `/presskit`, `/press-kit` e `/pressroom`**,
que NÃO estavam na varredura de 07/09 nem na de 10/09. Foi só isso que separou as duas fichas com
email desta rodada das dezenas de casas varridas sem resultado.

### Steffen Kabbelgaard — **Co-Owner, CEO & Game Director** — BetaDwarf Entertainment, Copenhague, Dinamarca — **nórdico, que é rota de frente**

- **Email:** `steffen@betadwarf.com` · confiança **alta** · **PUBLICADO pelo próprio estúdio** no
  `presskit()` dele, em **https://betadwarf.com/presskit**, aberto nesta rodada. A página traz duas
  coisas no mesmo documento: na seção **Team & Repeating Collaborator**, *"Steffen Kabbelgaard /
  Co-Owner, CEO, Game Director"*, e na seção **Contact**, sob a rubrica **Inquiries**, o endereço
  `steffen@betadwarf.com`. **Nada foi montado por padrão de domínio.**
- **Por que ELE e não outra pessoa da casa:** o presskit publica **nove** pessoas com cargo
  (Steffen Kabbelgaard; Kenneth Harder, Co-Owner/CTO/Lead Programmer; Kristian Klie, Gameplay
  Programmer; Alex Jørgensen, Animator; Peter Buje, Lead Designer; Christoffer Greulich, Producer;
  Alexander Karlsson, Technical Artist; **Stefan Greulich, Art Director**; Martin Prestegaard
  Lehnsdal, 3D Artist) e **um único endereço de pessoa**, o dele. O alvo de arte ideal seria o
  **Stefan Greulich, Art Director**, e a casa **não publica endereço dele**: ele fica como
  **SEGUNDA e última** possível, e hoje entraria como `sem-email`. Em casa desse porte o
  `BRIEF-JOE` manda ir no dono, e ele é dono, CEO e diretor de jogo ao mesmo tempo.
- **Gancho, com a frase do próprio estúdio entre aspas:** o presskit escreve que a casa
  *"is now fully focused on making **Minion Masters** - the best real time card game with co-op on
  PC and Console"*, e a home explica o que a casa é hoje: *"BetaDwarf is an ambitious venture
  company where we push the boundaries of co-op games to create lifelong friendships"*, com
  *"Friendshipping the world with co-op games"* como manchete. A origem, que é o melhor gancho
  humano e está escrita por eles: *"It all started in Copenhagen with a small group squatting in a
  university classroom for 7 months, getting discovered and moving in together for 3 years."*
  **O encaixe de personagem é o conteúdo do jogo, não uma suposição:** Minion Masters é um jogo de
  arena cujo produto é um **elenco de minions e masters estilizados**, e a `alvos.csv` da campanha
  já classificou a casa, em 06/09, como *"Casa de Minion Masters; elenco grande de personagens
  estilizados"*, encaixe **forte**.
- **Fora dos EUA?** Sim — Dinamarca (Schiller Office Hotel, Nannasgade 28, 2200 Copenhague N),
  União Europeia. A frase de realocação entra inteira, e a de patrocínio também.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 544 registra `info@betadwarf.com` em 06/09 com
  status `enviado`; `processados.csv` linhas 903, 904, 906 e 927 registram o quadro de BambooHR da
  casa, a candidatura espontânea mapeada campo a campo e o conserto do `apply_bamboohr.js` — a
  candidatura **não foi enviada**, morreu no reCAPTCHA de caixa. `pessoas.csv`: **zero** pessoa da
  BetaDwarf, e `steffen@betadwarf.com` não existe em arquivo nenhum do repositório. **NA CAIXA:**
  `search_threads` por `betadwarf OR Kabbelgaard OR "Minion Masters"` devolveu **uma** thread, e é
  a própria carta de 06/09 para `info@` — **sem resposta humana, sem bounce, sem recusa**. Esta é a
  **PRIMEIRA pessoa** da casa.
- **Ressalva honesta:** (1) o cargo é **CEO e Game Director, não arte** — quem decide a aparência
  do elenco é o Stefan Greulich, e é dele que falta o endereço; (2) o rodapé do site diz **©2021**
  e a página de carreiras diz *"No Available positions at this time"*, com estágio **não
  remunerado** como única porta escrita, então o presskit pode estar velho e o pareamento
  nome-cargo é de um documento sem data; (3) Minion Masters saiu em 2016 e a casa fala de
  *"OUR NEXT PROJECT"* sem dizer qual, ou seja não há prova pública de produção de elenco novo
  agora; (4) a casa é pequena e o dinheiro é de investidor (Square Enix, London Venture Partners,
  Makers Fund), o que aperta contratação sênior; (5) a porta de email da casa já foi usada uma vez
  em `info@`, então esta é a segunda batida no mesmo lugar, agora com nome.

---

### Philip Tibitoski — **CEO, Business Development** — Young Horses, Chicago, Estados Unidos — **e esta ficha CORRIGE um negativo escrito em 07/09**

- **Email:** `phil@younghorsesgames.com` · confiança **alta** · **PUBLICADO pelo próprio estúdio**
  no `presskit()` dele, em **https://younghorsesgames.com/press**, aberto nesta rodada. A mesma
  página pareia as duas coisas: na seção **Team & Repeating Collaborator**, *"Philip Tibitoski /
  CEO, Business Development"*, e na seção **Contact**, sob **Business Inquiries** e **Press
  Requests**, o endereço `phil@younghorsesgames.com`. **Nada foi montado.**
- **A correção de método, e é o achado mais reaproveitável do dia.** O `processados.csv` linha 1626
  guarda, da rodada do Joe de 07/09, esta frase: *"AMERICA DO NORTE DEU ZERO. Varridas raiz,
  /about, /team, /crew, /people, /contact, /leadership, /our-story, /founders, /who-we-are,
  /careers e politica de privacidade em Tippett, Pipeline Studios, ... **Young Horses**, Sunblink e
  Tic Toc: nenhuma publica endereco de pessoa, so caixa funcional."* **A conclusão estava errada
  para a Young Horses, e a causa é a lista de caminhos:** `/press` e `/presskit` não estavam nela.
  A casa publica endereço de pessoa **e** o time inteiro com cargo, e publica desde sempre.
  **Regra que sai daí: nenhum domínio se dá como "sem endereço de pessoa" sem ter tentado
  `/press`, `/presskit`, `/press-kit` e `/pressroom`.**
- **Por que ELE e não outra pessoa da casa:** o presskit publica **seis** nomes com cargo (Bria
  Davis, Community Director; Kevin Geisler, CFO/Programmer/Webmaster; **Chris Stallman, Lead
  Artist**; Philip Tibitoski, CEO/Business Development; Megan Varde, Environment Artist; Kevin
  Zuhn, Creative Director/Writer/Designer) e **um só endereço**, o do Phil, que serve de contato de
  negócio e de imprensa. O alvo de arte ideal é o **Chris Stallman, Lead Artist**, e a casa **não
  publica endereço dele**: fica como **SEGUNDA e última** possível, hoje em `sem-email`.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"As Young Horses we strive to push the
  boundaries of game design in order to create experiences that players have not seen before...
  Our goal is to create innovative, intelligent, and charming **entertainment** that can be enjoyed
  by both children and adults."* O encaixe de personagem é o catálogo: **Bugsnax** é um jogo cujo
  conteúdo é **um bestiário de criaturas estilizadas** (cada Bugsnak é um personagem modelado), e
  antes dele veio **Octodad**, que é um polvo num terno. A `alvos.csv` da campanha já registrou a
  casa como *"Chicago IL; games 3D cartoon (Bugsnax Octodad) com ~10 pessoas; full-time com
  relocation e opcao de remoto"*, encaixe **forte**.
- **Fora dos EUA?** **Não** — Chicago, Illinois. Pela regra fixa, a frase de realocação **não**
  entra nesta carta; o que entra é que a casa escreve, na própria página de vagas, que dá
  *relocation* e aceita remoto, e a linha de patrocínio precisa ser dita de frente porque o Vini
  não tem autorização para trabalhar nos EUA.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 193 registra `jobs@younghorsesgames.com` em
  02/09 com status `enviado`; `processados.csv` 1431 registra o rascunho de follow-up de 07/09 na
  mesma thread; `pessoas.csv`: **zero** pessoa da casa, e `phil@younghorsesgames.com` não existe em
  arquivo nenhum. **NA CAIXA:** `search_threads` por `younghorsesgames OR "Young Horses" OR
  Tibitoski OR Bugsnax` devolveu **uma** thread com **duas mensagens, as duas enviadas** (carta de
  02/09 e follow-up de 07/09), **sem resposta, sem bounce, sem recusa**. **PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) o cargo é **CEO e desenvolvimento de negócio, não arte**; (2) o mesmo
  endereço é o de **imprensa**, ou seja é uma caixa que recebe pitch todos os dias e onde carta
  fria tem chance real de ser lida como PR; (3) **Bugsnax saiu em 2020** e a casa tem cerca de dez
  pessoas — não há assento de personagem sênior esperando, e o presskit não tem data; (4) é
  **Estados Unidos**, o que significa patrocínio de visto numa casa pequena, que é exatamente o
  item que RH generalista usa para cortar; (5) a casa já levou carta **e** follow-up na mesma
  thread, então esta é a terceira batida, agora com nome.

---

### Brendan Taylor — **Founder & Visual Effects Supervisor** — Mavericks VFX, Toronto, Canadá — **`sem-email`, e a casa é NOVA na campanha**

- **Email:** **nenhum de pessoa.** Entra como **`sem-email`**, guardando nome, cargo e estúdio,
  exatamente como o `BRIEF-JOE` manda. O único endereço que a casa publica é
  `info@mavericks-vfx.com`, **caixa funcional vista publicada** no rodapé de todas as páginas
  (`https://mavericks-vfx.com/about`) — não é montada, mas também não é pessoa.
- **Nome e cargo PUBLICADOS pela própria casa** em **https://mavericks-vfx.com/about**, aberta nesta
  rodada, na seção **Our Team**: *"Brendan Taylor — Founder & Visual Effects Supervisor"*, ao lado de
  *"Paul DeOliveira — Creative Director"* e *"John Morch — Head of Technology"*. **Três nomes, é o
  time publicado inteiro.**
- **Por que ELE e não outra pessoa da casa:** dos três, o Paul DeOliveira (Creative Director) é o
  cargo de arte e fica como **SEGUNDA e última** possível; o John Morch é tecnologia. Escolhi o
  **fundador e supervisor de VFX** porque em casa desse porte é ele quem abre reel e decide quem
  entra num projeto, e porque o `BRIEF-JOE` manda ir no dono quando a casa é pequena.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Mavericks VFX is a Toronto-based studio
  of passionate filmmakers known for crafting high quality visual effects for film, TV shows,
  commercials… AND its softball team."* E a prova de disciplina está no menu do portfólio deles, não
  numa suposição minha: a página **https://mavericks-vfx.com/work/** organiza o trabalho em
  categorias e **uma delas é literalmente "Creatures"**, ao lado de *"Crowds"*, *"Set Extension &
  Action"*, *"Snow"* e *"Fire"*, sobre uma lista que inclui **The Handmaid's Tale (trabalho indicado
  ao Emmy em 2020)**, The Boys, The Expanse, What We Do In The Shadows, Halo e John Wick: Chapter 4.
  A página **/opportunities/** convida por escrito: *"We'd love to hear from you if you've got what
  it takes to join our team!"*
- **Fora dos EUA?** Sim — Canadá (Toronto). **Canadá é o país número um da ordem do `BRIEF-JOE`** e
  a carta tem de dizer de frente que o Vini precisa de patrocínio, porque é o item que o RH usa para
  cortar e o supervisor é quem atropela.
- **Dedupe, arquivos e caixa:** no repositório, `mavericks` só aparece em
  `automacao/garimpo-cgstudiomap.csv` (linha de 08/09, leitura de **quadro de vaga**:
  *"pagina de carreiras https://mavericks-vfx.com/opportunities/ lida por curl (483 caracteres...)"*)
  — **não é envio**. `pessoas.csv`, `enviados.csv`, `alvos.csv` e `PESSOAS-SEM-CARTA.md`:
  **zero**. **NA CAIXA:** `search_threads` por `mavericks OR "mavericks-vfx" OR "Brendan Taylor"`
  devolveu **zero**. **CASA NOVA, nunca recebeu carta nenhuma, PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) **não há endereço de pessoa** — a carta, se sair, sai para
  `info@mavericks-vfx.com` com o nome dele na abertura, e isso é uma via mais fraca; (2) a categoria
  *"Creatures"* é de **VFX de série de TV**, ou seja criatura de plano e double digital, **não
  elenco estilizado de animação**, que é onde o portfólio do Vini ganha; (3) a casa é pequena — três
  pessoas publicadas — e o quadro de `/opportunities/` monta por JavaScript (*"Powered by"*) e não
  lista vaga legível por `curl`, então não há vaga provada; (4) o rodapé marca **© 2026**, o que é
  bom sinal de site vivo, mas o prêmio que a página de About exibe é de **2018**.

---

### David Lipes — **Responsable de la protection des renseignements personnels (encarregado de dados)** — Budge Studios, Montréal, Canadá — **a ficha mais fraca da rodada, e está aqui com o motivo escrito**

- **Email:** `dave@budgestudios.ca` · confiança **alta** · **PUBLICADO com nome completo pela
  própria casa** em **https://budgestudios.ca/contact**, aberta nesta rodada. Texto literal da
  página: *"Responsable de la protection des renseignements personnels: **David Lipes** at
  dave@budgestudios.ca"*. **Nada foi montado.** É a veia da política de privacidade, a mesma que
  entregou o Sunho Park da GIANTSTEP em 07/09.
- **Por que ELE e não outra pessoa da casa:** porque **é a única pessoa com nome que a casa publica
  em todo o site**. A mesma página de contato só traz caixas funcionais — `jobs@`, `pr@`,
  `bizdev@`, `privacy@` e o Support — e as páginas `/about-us` e `/careers` não publicam uma única
  pessoa. Não existe Art Director nem Lead publicado para escolher.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"At Budge™, our mission is to thrill,
  educate and entertain children around the world through creative and innovative apps"*, e o pilar
  que interessa, escrito por eles: *"**Featuring the characters children know and love**, our apps
  are 100% fun approved by official kid playtesters."* O catálogo prova o 3D de personagem:
  **Bluey: Let's Play!** (finalista de iPad App of the Year 2024 e Editor's Choice 2023),
  **PAW Patrol Rescue World** (Kidscreen Best Game App 2023), **Hot Wheels Unlimited** (Kidscreen
  2022), **Barbie Dreamhouse Adventures** (Kidscreen 2019) e **My Little Pony: Harmony Quest**. A
  `alvos.csv` já tinha classificado a casa como *"Montreal QC; games apps infantis 3D com
  personagens licenciados (Bluey PAW Patrol Barbie Miraculous)"*, encaixe **forte**.
- **Fora dos EUA?** Sim — Canadá (5455 Avenue de Gaspé, Suite 540, Montréal). Canadá é o país
  número um da ordem do `BRIEF-JOE`, e a linha de patrocínio precisa estar na carta.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 205 registra `jobs@budgestudios.ca` em 02/09
  como `enviado`; `processados.csv` 389 registra a auto-resposta, e 1718 registra o quadro de
  **BambooHR token `budge`** com a vaga *"Artiste 3D Generaliste / 3D Artist Generalist"*, formulário
  preenchido inteiro e **nada enviado** porque o reCAPTCHA de caixa aparece depois do Submit.
  **E o registro que mais importa:** `processados.csv` 2012 mostra que `dave@budgestudios.ca` **já
  havia sido visto em 10/09**, numa varredura mecânica, como *"UM unico endereco de pessoa novo"* —
  e **nunca virou ficha nem linha de `pessoas.csv`**. Ou seja: o endereço não é descoberta minha, é
  achado abandonado que esta rodada está finalmente registrando com nome, cargo e fonte.
  `pessoas.csv`: **zero** pessoa da Budge. **NA CAIXA:** `search_threads` por `budgestudios OR
  "Budge Studios" OR Lipes` devolveu **uma** thread: a carta de 02/09 para `jobs@` e uma
  **auto-resposta automática** de `jobs+noreply@budgestudios.ca` (*"Nous prenons le temps de bien
  réviser chacune des applications"*). **Nenhuma pessoa respondeu, nenhuma recusa.** PRIMEIRA
  pessoa.
- **Ressalva honesta, e ela é a mais dura das quatro fichas:** (1) o cargo publicado é de
  **proteção de dados**, não de arte nem de recrutamento — é a via mais fraca que o `BRIEF-JOE`
  admite, e só se justifica porque a carta da campanha fecha pedindo direção (*"if someone else
  there is the right person for this, just point me"*), que é exatamente o que se pode esperar de um
  encarregado de dados; (2) os personagens da Budge são **licenciados** (Bluey, PAW Patrol, Barbie,
  Hot Wheels), então o estilo vem fechado no guia do licenciante e o trabalho é aplicar, não criar —
  é o oposto do que o portfólio do Vini mostra; (3) a casa **já tem porta viva e melhor**: o
  BambooHR com vaga de 3D Artist Generalist, que só trava no captcha, e o `jobs@` que respondeu
  automático; (4) o rodapé do site é **© 2016-2025**; (5) é jogo **mobile infantil**, não animação
  nem jogo de console, o que é o degrau mais baixo de encaixe entre as quatro fichas de hoje.

---

### O QUE MORREU NA RODADA DE 16/09, com a medição, para a próxima não reabrir

**Mortos com o endereço JÁ NA MÃO, o que é o tipo de morte mais caro e mais útil de registrar:**

- **M2 Film / M2 Animation** (Aarhus, DK) — casa **inédita** na campanha (zero em `pessoas.csv`,
  `enviados.csv`, `alvos.csv`), e ela publica **nome, cargo e email juntos**: a página de vagas
  `https://m2film.dk/job-type/current-vacancies/` escreve *"kontakte Head of Production **Ole
  Jørgensen** på oj@m2film.dk"*. **Morreu por escopo geográfico, e a prova está no rodapé do próprio
  site:** a divisão de animação, **M2 Animation, fica em BANGKOK** (30/1 Soi Sukhumvit 55), fora do
  escopo do `BRIEF-JOE`; a parte dinamarquesa é **filme publicitário** (*"Danmarks førende leverandør
  af reklamefilm"*), e a página `/people/` confirma: dos 40 e poucos nomes publicados, os de M2
  Animation são **produtor e diretor**, nenhum de personagem, e **nenhum com email**. Segundo motivo,
  também escrito por eles na mesma frase do Ole: *"Bemærk, at ansøgninger ikke modtages på denne
  mail"* — candidatura não é recebida nesse endereço. **Não gaste carta aqui.**
- **Autrechose** (Paris, FR) — publica em `https://www.autrechose.fr/contact/` *"Stéphane Bidault /
  Superviseur VFX / stef@autrechose.fr"*, com nome, cargo e endereço pareados, e ainda convida:
  *"AutreChose est toujours à la recherche de nouveaux infographistes de talent"*. **Morreu por
  técnica, pela regra da Krystallplaneten:** o site inteiro só diz *"effets spéciaux numériques"* e
  *"infographistes 2D & 3D"*, e as palavras **personnage, créature e character não aparecem em
  lugar nenhum** do domínio. Endereço ótimo, disciplina não provada.
- **Goodman Brothers** (Sydney, AU) — a home publica, sob *"Meet The Team"*, **Joel Goodman** com
  `joel@goodmanbrothers.com` e **Elliot Goodman** com `elliot@goodmanbrothers.com`, os dois pareados
  no `mailto:`. **Morreu por falta de CARGO publicado** (só o terceiro, "Alfie", tem título, "Client
  Services") **e por falta de prova de personagem**: a casa se descreve como *"a Sydney-based visual
  effects and post-production studio"* e o portfólio é um mural de vídeos sem disciplina escrita.
  É a mesma morte do `kela@appelmoes.games`: endereço existe, ficha não.
- **FIN Design + Effects** (Sydney, AU) — `emily@findesign.com.au` aparece de verdade no HTML, mas
  **só como segundo destinatário do `mailto:` de "Commercial Enquiries"**
  (`mailto:tvc@findesign.com.au, emily@findesign.com.au?subject=FIN%20VFX%20-%20TVC%20Enquiry`), sem
  nome e sem cargo. Não é ficha.
- **Morgana Studios** (Madrid, ES) — a política de privacidade publica `hernan@morganastudios.com` e
  nomeia o representante legal como **Miguel Cabañas Becerril**. **A parte local não corresponde ao
  nome publicado**, então não há pareamento: é endereço sem pessoa identificada.
- **Moonbug Entertainment** — `sruthi.dhulipala@moonbug.com` está publicado no site, e a própria
  linha diz o que ela é: *"Media Contact: Sruthi Dhulipala"*. Imprensa, não arte nem contratação.

**Barrados pelo dedupe, e cada um economizou uma carta:**

- **Global Mechanic** (Vancouver, CA) — a varredura de hoje reachou `bruce@globalmechanic.com`
  (Bruce Alcock, Creative Director & Owner) e `brodie@globalmechanic.com` (Chris Brodie, Executive
  Producer), pareados no `mailto:` do HTML. **Já foram achados e JÁ FORAM MORTOS em 15/09**, por
  técnica: mixed media, não CG (`processados.csv` 2483, *"o caso Krystallplaneten da rodada"*).
  Vancouver é a rota de frente do Vini e dói perder, mas a morte continua válida.
- **appelmoes games** (NL) — `kela@appelmoes.games` reapareceu na varredura do `/press`. Já está
  registrado neste arquivo como não-ficha: o site só publica o apelido "Kela", sem nome e sem cargo.
- **Juice / `j.studio`** (PL/SG) — `a.watras@j.studio` reapareceu na home. **Já está escrito na linha
  do Aditya Akolkar** em `pessoas.csv` como a segunda prova do formato do domínio. Casa com pessoa.
- **arx anima** (Viena, AT) — o `/about` publica o CORE Team com cargo (**Dunja Bernatzky**,
  Co-Founder/CEO/Head of IP; Kris Staber, COO; **Martin Hebestreit, Art Director Special Format**) e
  a casa faz **Talking Tom and Friends**, que é elenco 3D puro. **Não virou ficha porque o
  `talent@arxanima.com` JÁ RESPONDEU** em 03/09 (template mandando usar a página de carreiras) **e o
  Vini já respondeu essa thread** — a conversa é do Comunicador, e o único endereço novo é
  `md@arxanima.com`, caixa funcional sem nome. **Os dois nomes ficam guardados aqui** para quando
  aparecer endereço de pessoa.
- **Caribara Animation** (Paris/Annecy/Angoulême/Liège/**Montréal**) — era um dos **dois itens
  "NÃO CONFERIDOS"** que a rodada de 15/09 pediu para retomar. **Conferido agora, e o registro de
  domínio estava incompleto:** `https://caribara-animation.com` devolve **certificado SSL expirado**
  e `caribara.fr` devolve **403**; o site vivo é **`https://www.caribara-animation.com`**. A página
  `/studios/` publica o time dos cinco estúdios com nome e cargo (Fabien Baboz, Co-fondateur/CEO;
  **Florian Thouret, Directeur artistique / Réalisateur**; Stéphane Comparetti, Directeur technique;
  Michèle Paquin e Pascale Beaulieu, Responsables do estúdio de **Montréal**) e **ZERO email**. A
  técnica declarada é **2D em primeiro lugar** (*"expertise particulièrement reconnue en animation
  2D"*, cut-out e tradigital, Toonboom), com 3D como complemento, e cada estúdio tem **formulário
  próprio de candidatura espontânea** — isso é matéria da frente de formulário, não do Joe.
- O outro item "não conferido" de 15/09, o **Blender Studio**, **já tem pessoa** em `pessoas.csv`
  (Julien Kaspar, 14/09, `sem-email`). Não é reabertura.

**O que NÃO rendeu, com número, para ninguém repetir:**

- **`garimpo-cgstudiomap.csv`, a veia que rendeu quatro fichas em 15/09, secou nas rotas de frente.**
  Varri as **168** casas de Canadá, Reino Unido, Irlanda, nórdicos, Oceania e Bélgica que nunca foram
  tocadas, e depois **256** de França, Espanha, Polônia, Alemanha, Áustria e Luxemburgo, e **92** dos
  EUA — cada domínio em até 25 caminhos (`/team`, `/about`, `/crew`, `/people`, `/our-team`,
  `/contact`, `/studio`, `/privacy`, `/impressum`, `/press`, `/presskit`, `/leadership`, `/jobs` e
  mais), com decodificação de `data-cfemail` e um segundo nível de links internos. **Endereço de
  pessoa apareceu em cerca de 40 casas e NENHUMA passou no filtro de disciplina**: são casa de
  dailies e som (The Post Lounge, 8 endereços `nome.sobrenome@`), post house de cor e online (Nomad,
  Flavor, Picture Shop), viz de produto e barco (Pixlhut), previs (Proof), agência de publicidade
  (Epicure, Malherbe), motion design (BUCK, Golden Wolf) e CG automotivo (Rotor).
- **Universo de jogo do gamedevmap: 757 casas NOVAS e em escopo** de Holanda, nórdicos, Reino Unido,
  Escócia, Irlanda e Gales, varridas em 14 caminhos. **Cerca de 56 publicam endereço de pessoa, e
  quase todas são estúdio de uma a três pessoas sem pipeline 3D** — a mesma conclusão de 15/09, agora
  com número maior. Nenhuma virou ficha.
- **Casas já qualificadas pela campanha (carta em caixa genérica, sem resposta): 409 domínios**
  varridos em 24 caminhos, incluindo `/press` e `/presskit`. **Rendeu exatamente as duas fichas com
  email desta rodada** (BetaDwarf e Young Horses) e mais nada aproveitável. **É a melhor veia que
  sobrou, e o ganho vem do caminho novo, não do domínio novo.**
- **`presskit()` sobre os 577 domínios da `alvos.csv`**: 14 casas com presskit legível, **zero
  endereço de pessoa novo**.
- **Membros da Animation Ireland** (47 links, dez casas 3D abertas uma a uma: Brown Bag, Giant,
  Kavaleer, Lighthouse, Dulamán, Studio Meala, Igloo, Whackala, Curiosity, Distillery): **zero
  endereço de pessoa**, só `info@`/`hello@`.
- **Animação de Singapura**, que é escopo e estava inexplorada (One Animation/Oddbods, Tiny Island,
  Sparky, Mediafreaks, Robot Playground, Omens, Scrawl, Mighty Bear): **zero endereço de pessoa**.
- **Vancouver e Colúmbia Britânica** (Global Mechanic, Cloudhead, Archiact, Piranha Games, SkyBox
  Labs, East Side Games, Kano, IUGO, Bardel, Yeti Farm Creative): só caixa funcional, e **Bardel
  responde 403** ao `curl`. O único endereço de pessoa era o da Global Mechanic, já morto.
- **Campo `recruiter-email` do Teamtailor** testado em 10 domínios de casa que usa Teamtailor e
  renderiza no próprio site (Ankama, Krea Medie, CI Games, North Kingdom, Revolution, Nolimit City,
  Gears for Breakfast e outros): **zero**. Confirma o que o brief já dizia: veia rica mas raríssima.
- **Coreia do Sul** pela política de privacidade (Locus/`locusco.com`, Red Rover, Westworld, Studio
  Animal): só `info@`. A veia do encarregado de dados coreano segue valendo só para a GIANTSTEP.
- **Cartoon Forum** (`cartoon-media.eu/forum/projects/discover-the-projects`): a lista dos 75
  projetos **monta por JavaScript** e o `curl` não vê nem nome de casa nem email. **Não vale rodada
  sem navegador.**
- **Gnomon mudou de endereço:** o índice agora é `/news-and-events/events/` e no momento lista **um
  único evento**, *"Building Real-Time VFX for Borderlands 4"*, que é VFX em tempo real e não
  personagem. A barra `MORE EVENTS` do rodapé não existe mais nessa página. A veia da escola de arte
  está, hoje, vazia.

**A REGRA DE MÉTODO QUE SAI DESTA RODADA, e ela é reaproveitável:**
**nenhum domínio pode ser dado como "sem endereço de pessoa" sem ter tentado `/press`, `/presskit`,
`/press-kit` e `/pressroom`.** A varredura de 07/09 deu América do Norte como zero depois de testar
onze caminhos, e a Young Horses estava publicando nome, cargo e email de pessoa em `/press` o tempo
todo. O `presskit()` do Rami Ismail é um formato padronizado com seção **Team** (nome + cargo) e
seção **Contact** (endereço de pessoa) — é exatamente o que o Joe procura, num caminho fixo.

## MAESTRO, 16/09 14h40 UTC — cartas do lote da tarde escritas

- **Steffen Kabbelgaard (BetaDwarf):** rascunho `r-5321101601855303873`, gancho no presskit ("squatting in a
  university classroom", "fully focused on making Minion Masters"), frase de realocação inteira.
- **Philip Tibitoski (Young Horses):** rascunho `r938204193825327615`, gancho em Bugsnax como bestiário; casa
  americana, então sem a frase de realocação e com remoto e patrocínio ditos de frente.
- **David Lipes (Budge):** SEM carta, de propósito. Encarregado de proteção de dados não é alvo de carta de
  emprego; a porta da casa é o BambooHR `budge` (3D Artist Generalist), frente de formulário.
- **Brendan Taylor (Mavericks VFX):** fica `sem-email`, como a ficha diz.
Lote conferido pelo `confere-carta.py`: limpo, semelhança máxima 32%.

---

# RODADA DO JOE, 16/09 16h35 UTC — CINCO FICHAS, QUATRO COM ENDEREÇO PUBLICADO, E O DEDUPE DO GMAIL MATOU A MELHOR DELAS

**O método desta rodada, em três linhas.** (1) Percorri as **414 casas já qualificadas** pela campanha
(carta em caixa genérica em `enviados.csv`, status `enviado`, sem resposta, sem bounce, sem recusa, e
**sem pessoa** em `pessoas.csv`) nos quatro caminhos de `presskit()` mais `/team`, `/about`, `/studio`,
`/people`, `/crew`, `/contact`, `/impressum` e os `data.xml` do presskit — 22 caminhos, 9.108 URLs.
(2) Varri **389 domínios de casa de personagem** (linhas de `alvos.csv` e `garimpo-cgstudiomap.csv`
cuja observação diz personagem/character/criatura/estilizado) e **698 de rota de frente**
(Canadá, Reino Unido, Irlanda, Holanda, nórdicos), mais um **rastreador de segundo nível** que, em vez
de chutar caminho, **segue os links internos reais** de cada home (`team|about|people|crew|staff|studio|
contact|equipe|om-oss|over-ons|impressum|press|company|ansatte|…`, 2.387 links seguidos).
(3) Em tudo isso: decodificação de **entidades HTML no `mailto:`**, de **`data-cfemail` do Cloudflare** e
do campo `recruiter-email` do Teamtailor. **Zero endereço montado por padrão de domínio nesta rodada.**

**O número honesto:** 4.000 e poucas páginas lidas devolveram **1.031 endereços de aparência de pessoa**,
dos quais **467 inéditos no repositório**. Depois do filtro de disciplina (a casa tem de fazer personagem
3D) e do teto de duas pessoas por casa, sobraram **cinco fichas**. A conta é essa mesma: o gargalo não é
achar endereço, é achar endereço **de gente de arte, em casa de personagem, que ainda tem vaga na cota.**

---

### Guillaume Vialaneix — **Co-Director, Head of Animation** — Fabrique d'Images, Differdange, Luxemburgo — **a ficha mais forte da rodada, e o endereço estava ofuscado em entidades HTML**

- **Email:** `g.vialaneix@fabrique-d-images.com` · confiança **alta** · **PUBLICADO pelo próprio estúdio**
  na seção **OUR TEAM** de **https://www.fabrique-d-images.com/**, aberta nesta rodada. **Nada foi
  montado.** O endereço não aparece legível no texto: o `href` está escrito em **entidades HTML
  decimais** (`mailto:&#103;.&#118;ia&#108;aneix&#64;fab&#114;&#105;q&#117;&#101;-&#100;&#45;&#105;&#109;&#97;&#103;es.&#99;o&#109;`),
  e foi decodificado nesta rodada. É por isso que varredura antiga de `mailto` não viu esta casa: o
  regex de endereço não casa com entidade.
- **Como o pareamento nome-cargo-email foi PROVADO no HTML, e em duas vias independentes:** o cartão de
  cada pessoa é `[ícones com o mailto][<span class="member-name">Nome</span>][cargo]`, ou seja o `mailto`
  vem **imediatamente antes** do nome a que pertence. A sequência crua, em ordem, é: `jm.musique` →
  *"Jean Marie MUSIQUE / CEO and producer"*; `c.parisse` → *"Christine PARISSE / Ceo & Producer"*;
  `m.mertens` → *"Mark MERTENS / Producer"*; `y.czukor` → *"Yannick Czukor / Co-Director, Head of
  Production"*; **`g.vialaneix` → *"Guillaume Vialaneix / Co-Director, Head of Animation"***;
  `g.delazzer` → *"Geoffrey De Lazzer / Chief Financial Officer"*. A segunda via é a forma da parte
  local: **inicial do primeiro nome + sobrenome**, única para cada um dos seis. As duas vias dão a mesma
  resposta.
- **Por que ELE e não outra pessoa da casa:** dos seis publicados, quatro são negócio e produção (os dois
  CEOs produtores, o produtor Mark Mertens e o CFO) e o Yannick Czukor é **produção**. O Guillaume
  Vialaneix é o **único cargo de ofício criativo com endereço publicado**, e é **Co-Director** da casa,
  não empregado. Yannick Czukor fica como **SEGUNDA e última** possível. **Atenção de cota:** a carta de
  28/08 foi para `c.parisse@`, que é **endereço de pessoa**, então esta é a **segunda pessoa** da casa e
  a cota fecha aqui.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"FABRIQUE D'IMAGES was launched in 2002 in
  Luxembourg by two graphic designers, Christine Parisse and Jean-Marie Musique"*, e a frase que é o
  melhor gancho para um sênior de fora: *"Our programs are carried by a talented team of **more than 70
  people** whose field of expertise ranges from the most creative to the most technical, **from 2D to
  3D**, from the initial idea to the final image"*, com o diferencial que eles mesmos escrevem —
  *"The particularity of our studio is to have its **directors and artistic directors in-house** and to
  work on our original programs. Our artists are able to meet any challenge!"* O encaixe de personagem
  é o catálogo, não suposição minha: **THE LAST DINOSAUR** e **ARVIL THE LITTLE FALCON** e **DUDLEY**
  estão marcados *"in production"* em https://www.fabrique-d-images.com/our-projects/ , e o catálogo
  entregue traz **STITCH HEAD** (2025), **KLINCUS** e **DINO-MITE** (2024), **PERCY'S TIGER TALES**
  (2023), **MY FAIRY TROUBLEMAKER** (2022), **BAYALA** (2019) e **LUIS AND THE ALIENS** (2018) — dinossauro,
  falcão, monstrinho, tigre, fada e alienígena são elenco para esculpir.
- **A casa está CONTRATANDO agora, e isso muda o tom da carta:** https://www.fabrique-d-images.com/job-cards/
  lista, nesta rodada, *"JOB IN LUXEMBOURG : Technical Director"*, *"JOB IN LUXEMBOURG : Senior Production
  Manager / Line Producer"*, *"JOB IN LUXEMBOURG : Compositing Artist"*, *"JOB IN LUXEMBOURG : 2D Cut-out
  animator"* e *"JOB IN LUXEMBOURG : 2D Compositing Artist"*. **Nenhuma é de personagem**, então a carta
  não pode fingir responder a um anúncio: ela é carta de porta, e o pedido é o fechamento fixo da campanha.
- **Fora dos EUA?** Sim — Luxemburgo (115c, rue Emile Mark, L-4620 Differdange), União Europeia. A frase
  de realocação entra inteira e a de patrocínio também.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 135 registra `c.parisse@fabrique-d-images.com` em
  **28/08** como `enviado`; `alvos.csv` linha 112 classifica a casa como *"Differdange; The Picture Factory
  com ~70 artistas 2D/3D"*, encaixe **médio**, com fonte no guia oficial do Film Fund. `pessoas.csv`:
  **zero** pessoa da casa, e `g.vialaneix@` não existe em arquivo nenhum do repositório. **NA CAIXA:**
  `search_threads` por `fabrique-d-images OR "Fabrique d'Images" OR Vialaneix OR Parisse` devolveu **uma**
  thread com **duas mensagens, as duas enviadas** (carta de 28/08 e follow-up de 07/09 na mesma thread),
  **sem resposta humana, sem bounce, sem recusa**. Segunda pessoa da casa, e a última.
- **Ressalva honesta:** (1) a casa se descreve como quem *"develop, finance and produce"*, ou seja é
  **produtora** — é o mesmo caso da MovieBrats, e parte da fabricação pode acontecer em coprodução; (2) o
  cargo é **Head of Animation**, animação e não modelagem ou escultura, então o encaixe é "quem manda no
  elenco em movimento", não "quem contrata modelador"; (3) **duas das cinco vagas abertas são 2D cut-out
  e 2D compositing**, o que confirma que uma fatia grande do pipeline dela é 2D; (4) a casa **já levou
  carta e follow-up** no endereço de uma das donas, então esta é a terceira batida no mesmo domínio;
  (5) Luxemburgo é mercado pequeno e o incentivo fiscal local costuma vir com exigência de gasto local, o
  que aperta contratação de estrangeiro.

---

### Michael Brandstetter — **Design / 3D Animation / VFX / Post Production, e co-titular da casa no Impressum** — Digital Rain Studios, Viena, Áustria — **a casa escreve "character creation" ao lado do nome dele**

- **Email:** `m.brandstetter@digitalrain.at` · confiança **alta** · **PUBLICADO pelo próprio estúdio** em
  **três páginas diferentes** abertas nesta rodada: https://digitalrain.at/about.html ,
  https://digitalrain.at/contact.html e https://digitalrain.at/projects.html . **Nada foi montado.**
- **O pareamento, e ele é literal, sem inferência:** em `contact.html` o cartão dele diz, na ordem,
  *"Michael Brandstetter | Design | 3D Animation | VFX | Post Production | m.brandstetter@digitalrain.at |
  **your Partner for: design, character creation, general 3D production, animation, motion graphics**"*.
  Em `about.html` a bio é *"Design and visual direction expert, versatile artist with extensive expertise
  in 3D Workflows, industrial design, and post production finishing."* O **Impressum**
  (https://digitalrain.at/impressum.html) nomeia os três como responsáveis da casa sob
  *"Medieninhaber: Digital Rain Studios"*, o que confirma que ele é **dono e não empregado** — e dono não
  troca de casa, que é a defesa contra a armadilha do cargo desatualizado.
- **Por que ELE e não outra pessoa da casa:** a casa publica **três** pessoas, as três com endereço.
  Kristian Zazgornik é *"3D animation specialist... product visualization, simulation, rendering, motion
  graphics and VFX Pipelines"* e Thomas Brandstetter é *"VFX, 3D animation, motion capture, camera work"*.
  **O Michael é o único cuja linha de serviço escrita pela casa contém `character creation`, e o único com
  "visual direction" na bio.** Thomas Brandstetter fica como **SEGUNDA e última** possível (a bio dele
  cita *"character animation"*).
- **Gancho, com a frase do próprio estúdio entre aspas:** a casa se apresenta como
  *"a Vienna-based studio for visual artistry and precise craftsmanship with proven workflows and almost
  60 years of experience combined"* e *"a Vienna-based production house specializing in high-end visual
  effects, 3D animation, post production, and camera work"*. O serviço número **02** da lista deles é
  escrito assim: *"**Character Creation** — Concept, modeling, animation, motion capture and simulation"*,
  e o portfólio em https://digitalrain.at/projects.html tem **filtro próprio chamado "Character"**, ao lado
  de Product, VFX, 3D Animation, Design, Illustration e Games. O objeto social no Impressum repete:
  *"Gemeinsame Tätigkeit im Bereich: 3D Animation, **Character Creation**, VFX, Motion Graphics, Product
  Visualization, Design"*. A `alvos.csv` da campanha já tinha classificado a casa, com encaixe **forte**,
  como *"Estudio de animacao 3D em Viena com categoria Character no portfolio; trabalhos Any Buddies e Moso
  the moss"*.
- **Fora dos EUA?** Sim — Áustria (Thimiggasse 50, A-1180 Wien), União Europeia. Frase de realocação
  inteira e linha de patrocínio dita de frente.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 415 registra `office@digitalrain.at` em **02/09** como
  `enviado`; `alvos.csv` linha 359 traz a casa com encaixe **forte**. `pessoas.csv`: **zero** pessoa da
  casa, e `m.brandstetter@` não existe em arquivo nenhum do repositório. **NA CAIXA:** `search_threads` por
  `digitalrain OR "Digital Rain" OR Brandstetter OR Zazgornik` devolveu **uma** thread com **duas
  mensagens, as duas enviadas** (carta de 02/09 e follow-up de 07/09), **sem resposta, sem bounce, sem
  recusa**. **PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) a casa tem **três pessoas** e vende serviço por sócio (*"your Partner for"*) —
  não é estúdio com quadro de vagas, e não publica vaga nenhuma, então não há assento provado; (2) o peso
  do portfólio é **product visualization e publicidade**, com "character creation" como uma das seis
  linhas, não como o negócio principal; (3) o cargo dele não é um título de arte de personagem, é a
  descrição de um sócio generalista — o negrito da carta tem de ir para a palavra `character creation`
  que **eles** escreveram, e não para um cargo que não existe; (4) *"almost 60 years combined"* para três
  pessoas significa cerca de vinte anos cada, ou seja um trio sênior que faz tudo — contratar um sênior de
  fora é justamente o que casa desse porte evita; (5) a casa **já levou carta e follow-up**, então esta é
  a terceira batida no mesmo domínio.

---

### Ralph Kamp — **Chairman & CEO** — Timeless Films, Reino Unido — **casa INÉDITA na campanha, e o `mailto` está ancorado no cartão da pessoa**

- **Email:** `ralph@timelessfilms.co.uk` · confiança **alta** · **PUBLICADO pelo próprio estúdio** em
  **https://timelessfilms.co.uk/about**, aberta nesta rodada, no cartão dele da seção de equipe. **Nada
  foi montado.**
- **Pareamento provado no HTML:** cada cartão é `<...>Nome</...>` seguido do cargo e do botão **Send
  Email** cujo `href` é o `mailto`. A leitura crua, na ordem: `ralph@` logo após
  *"Ralph Kamp / **Chairman & CEO**"*; `rebecca@` após *"Rebecca Kamp / SVP Production & Marketing"*;
  `gareth@` após *"Gareth Kamp / SVP Distribution & Production"*; `jon@` após *"Jon Clifford / Head of
  Technical & Post Production"*; `jade@` após *"Jade Spinks / Contracts & Collections Manager"*. Cinco
  cartões, cinco endereços, cada parte local igual ao primeiro nome do cartão.
- **Por que ELE e não outra pessoa da casa:** é uma **empresa de família** e ele é o fundador e CEO —
  *"Established in 2009 by industry veteran Ralph Kamp (former CEO of Icon and Odyssey Entertainment)
  with his two children Rebecca and Gareth"*. Em casa desse porte o `BRIEF-JOE` manda ir no dono, que
  responde ele mesmo. O único outro cargo de ofício é **Jon Clifford, Head of Technical & Post
  Production**, e a bio dele diz que ele cuida de *"Post Production, technical & legal film delivery and
  international servicing"*, ou seja **entrega e não elenco**: fica como **SEGUNDA e última** possível.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Timeless Films is a leading independent
  production company specialising in the development, financing, production and distribution of
  **animated and family films**, giving it a unique position in the worldwide marketplace. It's a family
  business with an emphasis on family entertainment."* O encaixe de personagem é o catálogo, escrito por
  eles na mesma página: **WICKIE THE MIGHTY VIKING**, a sequência *"its **3D** sequel WICKIE AND THE
  TREASURE OF THE GODS"* e *"**3D CG animated feature** ANIMALS UNITED"*, com *"over $154m in total at
  the worldwide box office"*; depois *"the **CG animated DRAGON RIDER** from bestselling author Cornelia
  Funke"*; **JUSTIN AND THE KNIGHTS OF VALOUR (3D)** produzido junto com Antonio Banderas e a Kandor
  Graphics; **POSTMAN PAT: THE MOVIE (3D)**; **ROCK DOG** e as duas sequências (2022 e 2023);
  **MONSTER FAMILY** e **MONSTER FAMILY 2**; **PETS UNITED**; **JUNGLE BEAT: THE MOVIE**. Dragão, viking,
  cão roqueiro e família de monstros é elenco estilizado do começo ao fim. E a casa **produz por dentro**:
  a bio do Gareth diz que ele está *"heavily involved in the development and production of Timeless films
  **in house productions**"*, sendo a mais recente **SCROOGE: A CHRISTMAS CAROL**, que *"Netflix released
  in November 2022 and spent three consecutive weeks on their Global Top Ten Charts"*.
- **Fora dos EUA?** Sim — Reino Unido, que é rota de frente. **Ressalva de precisão: o site não publica
  endereço físico nenhum**; o que sustenta o país é o domínio `.co.uk`, a razão social britânica e o
  rodapé *"© Timeless Films 2026"*. Não escrevi cidade porque a casa não escreve.
- **Dedupe, arquivos e caixa:** procurei `timelessfilms` e `Timeless` em `enviados.csv`, `alvos.csv`,
  `automacao/pessoas.csv` e `automacao/garimpo-cgstudiomap.csv`: **zero em todos**. **NA CAIXA:**
  `search_threads` por `timelessfilms OR "Timeless Films" OR "Ralph Kamp" OR "Rock Dog" OR "Dragon Rider"`
  devolveu **zero**. **CASA NOVA, nunca recebeu carta nenhuma, PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) é **produtora e distribuidora**, não estúdio com pipeline — o 3D do catálogo
  foi feito por parceiros (Constantin Film, Kandor Graphics, Mack Animation/Ambient Entertainment), então
  quem contrata modelador provavelmente **não é ela**; é a mesma ressalva da MovieBrats e da Chouette, e
  aqui ela é mais forte porque a palavra "studio" não aparece em lugar nenhum; (2) o cargo é **Chairman &
  CEO**, negócio puro, e a bio dele é de financiamento e distribuição; (3) a casa **não publica página de
  vagas**, então não há vaga nem convite escrito; (4) o site **não publica endereço nem telefone**, o que
  é sinal de casa de escritório pequeno; (5) o catálogo mais recente citado é de **2023**, e não há
  projeto marcado como em produção hoje.

---

### Michał Amielańczyk — **Communication Manager** — Mechanistry, Polônia — **a casa tem o melhor encaixe de personagem da rodada e o pior cargo**

- **Email:** `miami@mechanistry.com` · confiança **alta** · **PUBLICADO pelo próprio estúdio** em
  **https://mechanistry.com/press**, aberta nesta rodada, em frase que pareia nome, cargo e endereço no
  mesmo período: *"Would you like to cover Timberborn? Contact our **Communication Manager Michał
  Amielańczyk** at: miami@mechanistry.com"*. **Nada foi montado**, e note que a parte local
  (`miami`) **não sai de nenhum padrão dedutível** do nome — é exatamente o caso que prova por que
  endereço literal vence padrão: qualquer montagem (`michal@`, `m.amielanczyk@`) teria quicado.
- **Por que ELE e não outra pessoa da casa:** porque **é a única pessoa com nome que a casa publica em
  todo o site**. `/`, `/press` e `/contact` só trazem `hello@mechanistry.com` e canais de comunidade
  (Discord, loja). Não existe Art Director nem Lead publicado para escolher.
- **Gancho, com a frase do próprio estúdio entre aspas:** a manchete da home é
  *"**Humans are gone. Will your beavers survive?**"* e a descrição é *"Timberborn is a **beaver
  city-building game** with a unique architecture system, wooden machinery, dams and water physics,
  available now on PC and macOS"*. A `alvos.csv` da campanha já tinha classificado a casa com encaixe
  **forte**, nestes termos: *"Casa de Timberborn; castores estilizados; carga clara de personagem"*.
  **E a casa está viva e em produção**, o que é raro nesta rodada: a própria página de imprensa lista
  release de **3 de setembro de 2026** (*"Timberborn's 1.1 Update Gives Beaver Engineers Even More Ways to
  Build, Dig, and Manage Their Settlements"*) e de **12 de março de 2026** (*"Lumberpunk City-Builder
  Timberborn Launches into 1.0"*).
- **Fora dos EUA?** Sim — Polônia, União Europeia. Frase de realocação inteira e patrocínio dito de frente.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 625 registra `hello@mechanistry.com` em **06/09** como
  `enviado`; `alvos.csv` linha 502 traz a casa com encaixe **forte**. `pessoas.csv`: **zero** pessoa da
  casa, e `miami@mechanistry.com` não existe em arquivo nenhum do repositório. **NA CAIXA:**
  `search_threads` por `mechanistry OR Timberborn OR Amielanczyk` devolveu **uma** thread, a própria carta
  de 06/09 para `hello@`, **sem resposta, sem bounce, sem recusa**. **PRIMEIRA pessoa.**
- **Ressalva honesta, e ela é a mais dura da rodada, com o contra-argumento escrito:** (1) o cargo é
  **comunicação e imprensa**, e a rodada de 16/09 de manhã **matou a Moonbug por exatamente isso**
  (`sruthi.dhulipala@moonbug.com`, *"Media Contact"*). Mantenho a ficha, e o motivo da diferença tem de
  ficar escrito para não virar precedente frouxo: a Moonbug é conglomerado de mídia com departamento de
  imprensa inteiro, enquanto a Mechanistry é casa de **uma dezena de pessoas** onde o gerente de
  comunicação senta ao lado de quem faz os castores, e onde a carta da campanha fecha pedindo **direção**
  (*"if someone else there is the right person for this, just point me"*) — encaminhar é literalmente o
  ofício dele. Ainda assim, **é o cargo mais fraco que o `BRIEF-JOE` admite**, e a ficha está aqui como a
  última da fila, não como a melhor; (2) o endereço é **caixa de imprensa**, ou seja recebe pitch de
  jornalista e de criador de conteúdo todos os dias, e carta fria de artista pode ser lida como PR; (3) a
  casa tem **um único jogo** e ele acabou de sair de 1.0 em março de 2026 — pós-lançamento é quando
  estúdio pequeno **encolhe** equipe de arte, não quando contrata sênior; (4) `/careers` não existe no
  site e não há vaga publicada; (5) castor de city-builder é personagem **pequeno na tela, em escala de
  jogo de construção**, o que usa menos escultura e groom do que o portfólio do Vini mostra.

---

### Ioana Șopov — **co-lead / Art Director** — Gummy Cat, Bucareste, Romênia — **`sem-email`, e o endereço de pessoa que a casa publica NÃO é dela**

- **Email:** **nenhum de pessoa identificada.** Entra como **`sem-email`**, guardando nome, cargo e
  estúdio, como o `BRIEF-JOE` manda.
- **Nome e cargo PUBLICADOS pela própria casa** em **https://www.gummycat.com/**, aberta nesta rodada, no
  bloco *"We are"*: *"**ioana șopov** / co-lead / **art director**"*, ao lado de *"Rareș Cinteză /
  co-lead / GAME DESIGN"* e *"Andrei Bogdan / LEAD PROGRAMMER"*. **Três nomes, é o time publicado
  inteiro, e ela é a cadeira de arte.**
- **O achado que NÃO virou endereço, e o motivo escrito:** o rodapé do site publica
  `rick@gummycat.com` (além do `hello@gummycat.com` do corpo), e `rick` **não corresponde a nenhum dos
  três nomes publicados**. Sem pareamento não há pessoa: é o mesmo caso da **Morgana Studios** de hoje de
  manhã (endereço publicado, pessoa não identificada) e do `kela@appelmoes.games`. **Não usar esse
  endereço como se fosse dela.**
- **Por que ELA e não outra pessoa da casa:** dos três, os outros dois são design de jogo e programação.
  Ela é **art director e co-dona** ao mesmo tempo, que é exatamente a cadeira que o `BRIEF-JOE` quer em
  casa pequena. Rareș Cinteză fica como **SEGUNDA e última** possível.
- **Gancho, com a frase do próprio estúdio entre aspas:** *"Gummy Cat is a **Romanian-based studio
  comprised of a few folks, keeping each other honest while we make cool video games**"*, e a linha de
  apresentação do site é *"Studio website for Gummy Cat Studio. Game development, graphic design, **art
  direction**"*. A `alvos.csv` já registrou a casa como *"Estudio romeno que oferece desenvolvimento;
  design grafico e direcao de arte"*, encaixe **médio**.
- **Fora dos EUA?** Sim — Romênia (2 Bulevardul Pierre de Coubertin, București), União Europeia.
- **Dedupe, arquivos e caixa:** `enviados.csv` linha 602 registra `hello@gummycat.com` em **06/09** como
  `enviado`; `alvos.csv` linha 539 traz a casa com encaixe **médio**. `pessoas.csv`: **zero** pessoa da
  casa. **NA CAIXA:** `search_threads` por `gummycat OR "Gummy Cat" OR Sopov OR "Bear and Breakfast"`
  devolveu **uma** thread, a própria carta de 06/09 para `hello@`, **sem resposta, sem bounce, sem
  recusa**. **PRIMEIRA pessoa.**
- **Ressalva honesta:** (1) **não há endereço de pessoa** — se a carta sair, sai para `hello@` com o nome
  dela na abertura, que é via mais fraca; (2) a página de vagas diz, literalmente, *"no job openings
  available"*, e a última vaga listada é de **OCT 2020: Project Manager**, ou seja a casa não contrata há
  cinco anos pelo que publica; (3) o site diz *"Check out our first game"* e **não nomeia o jogo em
  texto** (está só em imagem), então não consegui provar por leitura do domínio que o título é 3D
  estilizado — o registro de encaixe vem da `alvos.csv`, não de uma frase da casa, e isso é mais fraco do
  que a regra da Krystallplaneten exige; (4) são **três pessoas**, porte em que não existe assento de
  sênior; (5) o cargo dela é `art director` em **caixa baixa** no site, sem bio nenhuma, e não há prova
  publicada de que a casa faça personagem 3D em vez de 2D.

---

### O QUE MORREU NA RODADA DAS 16h35 DE 16/09, com a medição e a frase da fonte, para a próxima não reabrir

**Morto com o endereço, o nome E o cargo na mão, e é a morte mais caro da rodada:**

- **tinyBuild** (`tinybuild.com`, publisher com braço holandês em Roterdã, `alvos.csv` 420, encaixe
  **forte**) — a página **https://www.tinybuild.com/contact** publica, no cartão, *"**Creative Director |
  Tom Brien** | tom@tinybuild.com"* com bio *"Tom Brien grew up being an indie developer... At tinyBuild,
  he's **the creative drive behind our games**"*, e o `/about` publica *"Alex Nichiporchik | CEO |
  alex@tinybuild.com"* e *"Jaz Salati | CFO | jaz@tinybuild.com"*. Era a melhor ficha da rodada: cargo
  criativo, endereço literal, casa de personagem estilizado com ~100 pessoas. **MORREU NO DEDUPE DA
  CAIXA:** `search_threads` por `tinybuild OR Brien OR Nichiporchik` devolveu a thread da carta de 06/09
  para `jobs@` **com resposta humana de `olga.barlet@tinybuild.com` em 07/09**: *"Thank you for reaching
  out and sharing your resume with us... At the moment, we don't have any open positions that align with
  your..."*, e o Vini **já respondeu** essa thread. Casa que respondeu é do Comunicador, e recusa escrita
  fecha a porta. **Lição de método, e ela vale mais que a ficha perdida: o dedupe do Gmail tem de vir
  ANTES de escolher a pessoa, não depois de montar a ficha.**

**Mortos por DISCIPLINA, com endereço e pareamento perfeitos (a regra da Krystallplaneten e da
Autrechose), e nenhum deles deve virar carta:**

- **Super Spline Studios** (Leamington Spa, Reino Unido) — casa **inédita** na campanha (só aparece em
  `garimpo-cgstudiomap.csv` 843, leitura de quadro de 08/09, *"nao_encontrada"*), e é **exemplo perfeito
  da veia 2 desta rodada**: em https://supersplinestudios.com/about o `mailto` está **dentro do cartão da
  pessoa**, e o HTML cru pareia `aron@` com *"Aron Durkin | Co-Founder | Lead Animator"*, `eoin@` com
  *"Eoin Loughrey | Director | Lead Animator"* e `james@` com *"James Childs | Co-Founder | Lead
  Animator"*. A bio do Eoin até fala de personagem: *"started out at Blitz Games - bringing charm and
  appeal to **characters** such as Donald Duck, Puss in Boots and the infamous Jack Slate"*. **Morreu
  porque a casa não modela:** ela se descreve no próprio `<title>` como *"UK Games **Animation**
  Specialist Co-Development Partner"* e o serviço que ela publica é *"**Character rigging**, pipeline set
  up, implementation, scripts & tools"*. Animação e rigging não são a cadeira do Vini, e o `BRIEF-JOE` já
  manda tratar rigging como fora (a armadilha do "Creature TD"). `/open-positions/` responde **404**.
- **Haymaker VFX** (Gotemburgo, Suécia, com braço em Los Angeles) — https://haymakerfx.com/contact publica
  **oito** pessoas com nome, cargo e endereço, entre elas *"**Alex Hansson / CEO / Head of VFX** /
  alex.hansson@haymakerfx.com"*, e a página de estúdio ainda lista *"Magnus Engsfors | Creative Director"*
  e *"Pontus Mattsson | Head of Compositing"*. **Morreu por disciplina:** *"Haymaker VFX is a premiere
  visual effects studio"* para *"feature films, episodics, and commercials"*, e as palavras
  **character, creature e animal não aparecem em página nenhuma** que abri. Nórdico e dói perder.
- **Sparky Animation** (Singapura, que é escopo) — https://sparkyanim.com/our-work-2/ publica
  *"**Todd Ross** | todd@sparkyanim.com | **Head of Content Sales & Licen[sing]**"*, e a casa é CG de
  verdade: *"Sparky Animation has stamped its name on some of the best **CGI productions** emerging from
  Asia"*. **Morreu pelo cargo:** vendas e licenciamento, e a frase que o apresenta é literalmente
  *"For Content Sales, Licensing and Merchandising enquiries please contact"*. Corrige, com número, a
  linha de hoje de manhã que dava a animação de Singapura como zero: **há endereço de pessoa lá, só não
  de arte.**
- **Head Gear Animation** (Toronto, Canadá) — https://headgearanimation.com/contact publica
  *"Project requests & Inquiries: **Susan Armstrong** | susan@headgearanimation.com"*. **Morreu por
  técnica:** o menu de ofícios da casa é *"2D Animation | Stop Motion Animation | Live Action/Combo |
  Mixed Media"* — **não há 3D**.
- **Fort York VFX** (Toronto) — https://www.fortyork.tv/about publica quatro pessoas com cargo e endereço
  (*"Erin Kuttner | EP / Managing Director | erin@fortyork.tv"*, mais Valerie Moss, Armen Bunag e Katie
  Fowler, todos produção). **Morreu por técnica e cargo:** *"Fort York is a Toronto-based visual effects
  shop. We specialize in **colour grading, compositing, animation, motion design and graphics**"*.
- **Bacon X** (Frederiksberg, Copenhague) — https://baconx.com/contact publica `sophie@`, `zara@`,
  `lorene@`. **Morreu por técnica:** *"BACONX IS A CREATIVE STUDIO... SPECIALIZED IN DELIVERING BESPOKE,
  BREATHTAKING VISUAL EFFECTS AND **EXCEPTIONAL COLOR GRADING**"*, para *"FILM, ADVERTISING, TELEVISION,
  AND MUSIC VIDEOS"*.
- **RedLab** (Toronto) — https://redlabto.com/contact publica três donos com cargo, com o endereço
  **ofuscado pelo Cloudflare** e decodificado nesta rodada: Mark Stevens (Head of Sales/Owner), Walt
  Biljan (Colourist/Owner), Andy Hunter (Flame Artist/Owner). **Morreu por técnica:** *"top-tier
  **post-production** services"*.
- **Toast** (Helsinque) e **Studio Outo** (Oulu e Helsinque) — as duas publicam a equipe inteira com cargo
  e endereço (`toast.fi/people` dá nove pessoas, entre elas *"Vesa Vinni | VFX | vesku@toast.fi"*;
  `outo.fi` dá `jussi@`, `tero@`, `janne@`). **Morreram por técnica:** a Toast é *"Toast offers all **post
  production** services"* (cor, som, edição) e a Outo é *"**animaatiostudio**"* de animação e ilustração 2D.
- **Split VFX** (Islândia) e **Helping Hand** (Noruega) — `jon.mar@split.is` e `nils@helpinghand.as`.
  A Split é VFX e DIT de publicidade e série; a Helping Hand é um homem só: *"**Jeg heter Nils**, og driver
  Helping Hand sammen med håndplukkede frilansere"*. Nenhuma faz personagem.
- **Cute Newt** (Londres) — `george@cutenewt.com`, e o nome e o cargo estão publicados com uma credencial
  boa: *"It was founded by **George Wyman V**, who was the former **Art Director** for the hit game
  Starbound"*, hoje *"Founder, Director"*. **Morreu por técnica:** Starbound é **pixel 2D**, o jogo novo
  (*"Wildekin is a work in progress"*) não tem uma linha dizendo 3D, e `/dev-team` responde **404**.
- **Hammer & Ravens** (Tallinn, Estônia) — `emiliano@hammerandravens.com`, colhido do **`data.xml` do
  presskit()**, com endereço postal e tudo. **Morreu por técnica:** *"retro-inspired... twin-stick shooter
  with roguelite mechanics"*, 2D.
- **Bohemia Interactive** — `dusan.gregor@bistudio.com` e `pavel.krizka@bistudio.com` em `bohemia.net/press`.
  Contato de imprensa, e a casa é simulação militar realista (Arma, DayZ): **duas razões para não gastar
  carta**.
- **Curve Games** (Reino Unido) — `clare.hawkins@curvegames.com`, achado no presskit de
  `dungeonsofhinterberg.com`, e a própria linha diz o que é: *"**Press Contact**: Clare Hawkins"*. Editora,
  imprensa, e a casa do jogo é a Microbird, em Viena.
- **WildBrain** (Vancouver, que é a rota número um) e **Funcom** (Oslo) — as duas publicam endereço de
  pessoa em **release de imprensa** (`kathleen.persaud@`, `misha.harding@`, `louisa.danquah@`,
  `shaun.smith@wildbrain.com`; `magnussa@` e `nataschar@funcom.com`). **Morreram pela regra da Moonbug:**
  relações de mídia não é arte nem contratação. As duas casas **continuam abertas por outra porta** e a
  WildBrain é Vancouver, ou seja vale uma rodada com alvo de arte.
- **Emberstorm** (Alemanha) — `reka@emberstorm.de` parece pessoa e **não é**: REKA é o nome do jogo da
  casa. Não registrar como endereço de pessoa.
- **Cat-astrophe Games** — `michalis@cat-astrophe-games.com` está na home, e o bloco `FOUNDERS` nomeia
  *"Paweł Wojciechowicz | CEO"*; **`michalis` não pareia com nome nenhum publicado** e `/team` e `/about`
  devolvem corpo vazio ao `curl` (montam por JavaScript). Endereço sem pessoa identificada, igual à
  Morgana Studios.
- **Lost Again** (Tilburg, Holanda) e **Massive Galaxy** (Lisboa) — os dois têm `presskit()` legível e o
  contato do `data.xml` é **caixa**: `info@lostagain.nl` e `press-contact@massivegalaxy.com`.

**Barrados pelo dedupe, e cada um economizou uma carta:**

- **Alt.VFX** (Brisbane, Austrália) — a varredura profunda abriu `https://www.altvfx.com/the-team/`, que é
  a melhor página de equipe que vi hoje: **50 pessoas com cargo** e **14 `mailto` ancorados no cartão**,
  com o pareamento provável provado na ordem do HTML (`col@` ↔ *"Colin Renshaw | Founder / Director"*,
  `nick@` ↔ *"Nick Angus | Head of FX"*, `matt@` ↔ *"Matthew Chance | Head of 2D"* e assim por diante), e
  ainda lista vaga viva (*"LEAD ANIMATOR | Brisbane, Full time, Immediate Start"*). **A casa já está no
  teto:** `pessoas.csv` 103 tem **Colin Renshaw** (`col@altvfx.com`, carta enviada em 06/09) e 104 tem
  **Sam Lee, Head of Modelling**, como `sem-email`. Registro o que mudou e o que não: **Sam Lee e Jamie
  White (Head of 3D) continuam SEM endereço publicado** — os 14 endereços são de fundadores, produção,
  FX, 2D e operações.
- **Stardust Effects** (Oslo e Atenas) — `https://stardusteffects.com/about/who-we-are` publica cinco
  sócios com cargo e endereço, entre eles *"Tony Alamo | VFX Supervisor & Partner | tony@stardusteffects.no"*
  e *"Anette Gjertsen | Manager & Partner"*. **Teto batido:** `enviados.csv` 355 (`elena@`, 02/09) e 664
  (`kai@`, 06/09) já são **duas pessoas** da casa, e o Kai está em `pessoas.csv` 98.
- **Qvisten Animation** (Oslo) — a página de contato publica **onze** pessoas com cargo e endereço,
  inclusive *"Arnfinn Moseng | HEAD OF STUDIO"* e *"Fredrik Kiøsterud | CEO"*. **Teto batido:**
  `hedda.toftner@` (HR Manager) levou carta em 26/08 com follow-up e o `rasmus@` (Creative Director) está
  em `pessoas.csv` 8, com carta enviada em 03/09.
- **Eallin** (Praga, Bratislava e Estocolmo) — `eva.simonovicova@`, `jozef.elsik@`, `leos.vojtisek@` são
  novos, mas a casa já tem **duas** pessoas (`pessoas.csv` 16 e 106). **Teto batido.**
- **Brikk Animation** (Estocolmo) — reapareceu com `3d@brikk.se` e a equipe inteira; a casa já tem **três**
  pessoas em `pessoas.csv` (15, 147, 148). Fechada.
- **Magic Lab** (Praga) — `vladimir@magiclab.film` (CEF) e `andrea@magiclab.film` são novos; a casa já tem
  **duas** (Viktor Plch e Michal Krecek). **Teto batido**, e é a mesma casa que gerou o erro de duplicata
  de 07/09.
- **Freefolk** (Londres) — a página de contato publica **treze** pessoas com cargo e endereço, e eu li a
  lista inteira: são CEO, COO, business development, head of commercial production, produtores e PR.
  **Não há um cargo de arte ou de CG publicado**, e a Fi Kilroe (CEO) já está em `pessoas.csv` 189.
- **Blinkink** (Londres) — `alex.halley@`, `ellie.goodwin@` e `shiara.miranda@blinkink.co.uk` são novos, mas
  a casa já tem o Josef Byrne (`pessoas.csv` 83) e o resto da página `/about` é agente e representante de
  diretor (`hunkydoryus`, `wearebueno`, `softcitizen`, `freeagent`), não contratação.
- **Artifex Animation Studios / A.A. Studios** (Montréal) — `aastudios.ca/contact` publica
  *"Moon Marsolais, **Floor Manager**: mmarsolais@aavfx.com"* e *"Jake McBride, **IT/IO**:
  jmcbride@aavfx.com"*. **Nenhum é arte**, e o Marc Hall (dono e supervisor) já recebeu carta em 09/09.
- **La Chouette Compagnie** — os nove `@chouettecie.com` reapareceram na varredura; o Bill Otomo já é ficha
  desta manhã.
- **Kalla Gameworks** (Kuopio, Finlândia) — `https://kallagameworks.com/team` publica os seis com cargo e
  endereço, inclusive *"Timo Hakkarainen | **3D Artist** | timo.hakkarainen@kallagameworks.com"*. **Não é
  descoberta:** `alvos.csv` 579 já registra a casa com `janne.mikkola@kallagameworks.com` e encaixe
  **baixa** — *"Estudio pequeno (8 pessoas), um unico 3D Artist"*. É fila, não Joe.
- **Wonderlust Media** (Canadá, Nova Escócia) — publica *"Christian Rankin | Executive Producer |
  christian@wonderlustmedia.ca"* **e uma vaga viva de `Senior Art Director`, Full time**, cujo botão Apply
  é `mailto:ryan@wonderlustmedia.ca?subject=Senior%20Art%20Director`. **Não virou ficha do Joe** porque a
  casa é *"a passionate collective of designers and animators who love telling colorful and quirky
  stories"*, ou seja motion e design gráfico, a mesma morte da BUCK e da Golden Wolf. **Mas a vaga é
  canadense, é de direção de arte e se candidata por email publicado: isso é matéria da frente de
  formulário/portas, e fica registrado aqui de propósito.**

**O que NÃO rendeu, com número, para ninguém repetir:**

- **414 casas já qualificadas × 22 caminhos = 9.108 URLs.** Devolveu **144** endereços de aparência de
  pessoa, **134 inéditos**, e virou **duas fichas** (Digital Rain e Mechanistry) mais a morte da tinyBuild.
  Confirma a medição de hoje de manhã: é a melhor veia que sobrou, e ainda assim rende dois por rodada.
- **389 domínios de casa de personagem × 22 caminhos.** 174 endereços, 130 inéditos, **zero ficha**: o que
  aparece são agentes e representantes de diretor de publicidade (`grgdreps`, `beelinereps`,
  `littlebirdrep`, `hunkydoryus`) e produtores de post house.
- **698 domínios de rota de frente × 22 caminhos = 15.356 URLs.** 387 endereços, 264 inéditos, e o
  rendimento foi **post house**: a `company3.com` sozinha deu **vinte** endereços de pessoa, todos de
  produção e cor. Os únicos chefes de ofício de personagem em escopo que apareceram (Alt.VFX, Qvisten,
  Stardust) **já estavam no teto**.
- **Rastreador de segundo nível** (segue os links internos reais em vez de chutar caminho) em 640 domínios,
  2.387 links: **73 endereços que as três varreduras de caminho NÃO acharam**, ou seja cerca de **17% a
  mais**. Foi ele que abriu a equipe inteira da Alt.VFX e os sócios da Stardust. **Vale incorporar à
  rotina:** chutar caminho perde uma página em seis.
- **`presskit()` e `data.xml`**: presskit legível em cerca de vinte casas; contato de **pessoa** em duas
  (Hammer & Ravens e Massive Galaxy), as duas mortas. A veia que rendeu hoje de manhã **já foi colhida**.
- **Buscador por `curl` está fechado nesta máquina**, e isso limita a veia 3 (site pessoal de Lead/Head of
  Character achado por crédito): `html.duckduckgo.com` e `lite.duckduckgo.com` devolvem página **sem um
  único link de resultado** e `www.mojeek.com` devolve **384 bytes**. Pela ferramenta de busca, duas
  consultas devolveram página de portfólio de escola e Wikipédia, **zero site pessoal com email publicado**.
  **A veia 3 não morreu, mas ela não roda por varredura: precisa de nome vindo de crédito, um por vez.**
- **Página de mentor de escola de arte, estado de hoje:** `thinktankonline.ca/mentors` devolve **114
  bytes**, `thinktanktrainingcentre.com` dá **502** no proxy, `lostboys-studios.com/instructors` dá **406**.
  **`cgspectrum.com/mentors` abre** e publica bio com cargo e casa (*"Matteo is a **Senior Character and
  Creature Modeler at Framestore, London**"*, *"Jon currently works as a **Lead Character Technical Artist
  at Striking Distance Studios**"*, *"Since 2015, Anna has worked as a 3D character artist at Riot
  Games..."*). **Não virou ficha porque não há email** e as casas são grandes (Framestore e Riot já têm
  gente ou porta de portal), mas **é veia viva para uma rodada de `sem-email`** e está registrada aqui.

**AS DUAS REGRAS DE MÉTODO QUE SAEM DESTA RODADA:**

1. **Endereço escrito em ENTIDADE HTML dentro do `mailto:` é invisível para toda varredura de regex feita
   nesta campanha até hoje.** A Fabrique d'Images publica o `Co-Director, Head of Animation` com email há
   anos e nenhuma rodada viu, porque o `href` está em `&#103;.&#118;ia&#108;aneix&#64;...`. A regra de
   07/09 dizia procurar `data-cfemail` antes de dar um domínio como sem endereço; **ela agora tem uma
   segunda metade: decodificar entidade HTML no `href` também.**
2. **O dedupe do Gmail vem ANTES de escolher a pessoa.** A tinyBuild tinha cargo criativo, endereço
   literal e casa de personagem, e a casa já havia recusado por escrito em 07/09. Montar a ficha primeiro
   e conferir a caixa depois custa a rodada inteira de uma casa boa.

## MAESTRO, 16/09 17h20 UTC — lote das 16h35 escrito, quatro cartas

- **Guillaume Vialaneix (Fabrique d'Images):** rascunho `r8475083916284819541`, gancho nos diretores artísticos internos e nos três projetos em produção; diz que viu as cinco vagas de Luxemburgo e que nenhuma é de personagem.
- **Michael Brandstetter (Digital Rain):** rascunho `r1743173961458051563`, gancho no serviço "Character Creation" e no filtro Character do portfólio.
- **Ralph Kamp (Timeless Films):** rascunho `r7926989738467250603`, gancho no catálogo estilizado e na produção interna (Scrooge na Netflix).
- **Michał Amielańczyk (Mechanistry):** rascunho `r568634798453027820`, escrita como pedido de encaminhamento a quem manda na arte, porque o cargo é comunicação. Diferente do caso Budge: aqui é casa de dez pessoas e encaminhar é o ofício dele.
- Lote conferido pelo `confere-carta.py`: limpo, semelhança máxima 37%. Linha do Budge no `pessoas.csv` (campo com vírgula sem aspas) consertada.

## JOE, 16/09/2026 20h35 UTC — UMA FICHA COM ENDEREÇO PUBLICADO, E O RESTO DA RODADA É REGISTRO DE VEIA SECA

**Placar honesto: 1 pessoa com email PUBLICADO, abaixo da meta de 4 a 8.** A causa está medida e
escrita abaixo, e não é falta de tentativa: **as veias de varredura por domínio que este arquivo
já registrou como esgotadas continuam esgotadas**, e nesta rodada elas devolveram 63 domínios
abertos para **um** endereço de pessoa aproveitável. Nada foi inventado para fechar número.

### FICHA 1 — Bruce Alcock, Global Mechanic (Vancouver e Victoria, BC, Canadá)

- **Email: `bruce@globalmechanic.com` — PUBLICADO pela própria casa, confiança ALTA.** Não é
  montado por padrão de domínio: o nome dele **é** a âncora do `mailto:`.
- **URL exata aberta nesta rodada:** `https://www.globalmechanic.com/` (rodapé do site, presente
  em todas as páginas; reconferido também em `https://www.globalmechanic.com/design`). O HTML cru,
  colado como está:
  `<a href="mailto:bruce@globalmechanic.com?subject=From%20the%20GM%20Site"><strong>Bruce Alcock</strong></a><strong> </strong>Creative Director & Owner`
- **ARMADILHA PARA A PRÓXIMA RODADA:** `https://www.globalmechanic.com/contact` **existe e é a
  página 404 da casa** (*"We couldn't find the page you were looking for"*). Quem varrer só
  `/contact` escreve "casa sem endereço publicado" e erra — **os endereços moram no rodapé da
  home**, não em página de contato.
- **Por que ESSA pessoa e não outra da casa:** o site publica **exatamente duas** pessoas com
  endereço próprio — *"Bruce Alcock — Creative Director & Owner"* (`bruce@`) e *"Chris Brodie —
  Executive Producer"* (`brodie@`). A terceira linha do rodapé é **agente**, não a casa:
  *"U.S. Representation: Liz Shaw"*, `liz@lizlainereps.com`. Pela régua do brief para casa
  pequena, o alvo é **dono / diretor criativo**, não produção: o Brodie orça e agenda, o Alcock
  decide o look e quem desenha. **Chris Brodie fica como SEGUNDA e última pessoa possível desta
  casa**, com endereço já provado, se a primeira carta não voltar.
- **Gancho com a frase do próprio estúdio, entre aspas:** a home se apresenta como
  *"Design & animation since 2000"*, e a página `/design` divide o catálogo da própria casa em
  categorias cuja **primeira é `Character`** (*"Design | Character | Drawing | Kids | Mixed Media |
  Vector | Painting"*). É nessa palavra que a carta pega.
- **Casa fora dos EUA: SIM, Canadá (Vancouver e Victoria, BC).** A frase de realocação **entra**, e
  é a rota de prioridade 1 da campanha.
- **O que o Gmail devolveu no dedupe:** `mcp__Gmail__search_threads` com
  `globalmechanic.com OR "Global Mechanic" OR Alcock` devolveu **`{}`** — zero thread, nem enviada
  nem recebida. `pessoas.csv`, `enviados.csv` e `processados.csv`: **zero** ocorrência de
  `globalmechanic`; o único acerto do grep por "Global Mechanic" é um resumo de rodada de 15/09 que
  **não nomeia a casa**. Casa **inédita para a campanha inteira**, e ela estava parada em
  `automacao/alvos-joe-wikidata.csv` sem ninguém nunca ter aberto.
- **RESSALVA HONESTA, e ela é grande:** a Global Mechanic é **boutique de design e animação de
  publicidade, documentário e projeção**, com técnica declarada em mixed media, vetor e pintura —
  **não é casa de pipeline CG de personagem**. A categoria `Character` do `/design` é **desenho** de
  personagem, não prova de modelagem 3D. A casa é pequena, **não publica quadro de vagas** (não há
  `/careers`) e **não há uma linha sobre patrocínio de visto** — ou seja, ela entra pela prioridade
  geográfica de BC, não por patrocínio provado. O que sustenta a carta é o endereço de um dono
  acessível. Telefone publicado no rodapé **deliberadamente não registrado**, porque o repositório
  é público.

### O QUE FOI ABERTO E NÃO TINHA ENDEREÇO DE PESSOA (casa por casa, para ninguém repetir)

- **Vancouver / BC, que é a prioridade 1:** `skyboxlabs.com` (só `info@`, `careers@`, `media@`,
  `support@`, `businessdevelopment@` — e a casa é boa: *"grown to a studio of over 235 team
  members"*, NetEase, *"BC's Top Employers"*; **não publica um nome com cargo**),
  `giantant.ca` (só `newbiz@`; o `/about` lista **24 nomes SEM cargo nenhum** — *"Giant Ant is —
  Jay Grandin, Leah Nelson, Shawn Hight..."* — e a casa é motion design, morte da BUCK),
  `blackbirdinteractive.com`, `slickentertainment.com`, `athinkingape.com`, `hotheadgames.com`,
  `scanlinevfx.com`, `artifexstudios.com`, `iugo.ca`, `arcanastudio.com`,
  `eastsidegames.com` (só `jobs@eastsidegamestudio.com` e 12 caixas de `zendesk`).
- **PAREDE MEDIDA, não "casa sem site":** `www.bardel.ca` devolve **HTTP 403 com 103 bytes**,
  `server: cloudflare`, `ki-edge: v=28.5.0` — é Cloudflare barrando este túnel, e a Bardel é uma
  das maiores de Vancouver. `bardelentertainment.com` dá **502 no CONNECT**.
  `www.versatile.media` dá **erro de certificado** (`unable to get local issuer certificate`) mesmo
  com `--cacert /root/.ccr/ca-bundle.crt`. `ghost.dk` dá **`tlsv1 alert internal error`**.
  `www.filmgate.se` dá **connection reset**. `svenskanimation.se` dá **502 no CONNECT** e
  `www.animationdenmark.dk` tem **certificado que não casa com o host**. **Nenhuma dessas é
  "sem endereço": são NÃO CONFERIDAS, e cabem no navegador de tela.**
- **Nórdicos, Holanda e Reino Unido abertos sem pessoa:** `gimpville.no`, `ravnstudio.com`,
  `animaskin.no`, `blackstudios.se` (é blog de artigos, não estúdio), `tumblehead.com`,
  `kongorange.com`, `ghostship.dk`, `triband.co`, `krillbite.com`, `henchmanandgoon.com`,
  `megapop.no`, `dirtybit.com`, `antagonist.no`, `sarepta.studio`, `dockhouse.se`, `dupp.se`,
  `forestlight.se`, `sorenfleng.com`, `fridthjof.com`, `creativebeards.com`, `planetx.nl`,
  `illuster.nl`, `grendel-games.com`, `triangle-studios.com`, `wispfire.com`, `codeglue.com`,
  `gridvfx.com` (só `info@`), `baitstudio.com` (só `hello@`), `lupusfilms.com`, `beakus.com`,
  `kilogramme.co.uk` (só `mail@` e `freelancers@`), `spider-eye.com`, `bluebolt.tv`,
  `nvizible.com`, `fido.se`, `juice.fi`.
- **Resto da Europa e Canadá abertos sem pessoa:** `rise-fx.com`, `dwarfanimation.com`,
  `unitimage.com`, `supamonks.com`, `cube-creative.com`, `fortiche.com`, `mackevision.com`,
  `luxx.studio`, `lunanime.be`, `giantanimation.ie`, `andmapsandplans.com`, `bigbadboo.ca`,
  `carbotanimations.com`, `unagistudio.com` (o "endereço de pessoa" era o placeholder
  `utilisateur@domaine.com`), `sohovfx.com`, `spinvfx.com`, `folksvfx.com`, `obliquefx.com`,
  `yowzaanimation.com`, `tonicdna.com`, `lolavfx.com`, `bighteam.com`, `bigparkstudios.com`.

### ENDEREÇO ACHADO E MORTO, com o motivo de cada um (nenhum virou ficha, e isso é de propósito)

- **Head Gear Animation** (Toronto) — `susan@headgearanimation.com`, publicado com nome e função em
  `https://headgearanimation.com/contact`: *"Project requests & Inquiries: Susan Armstrong"*.
  **Morreu por técnica e por teto:** a própria casa lista as técnicas dela e **3D não está na
  lista** (*"2D Animation | Stop Motion Animation | Live Action/Combo | Mixed Media"*), e
  `pessoas.csv` já tem uma pessoa da casa.
- **Nørlum** (Viborg, DK) — `claus@` e `elena@noerlum.com` reapareceram. **Já registrado:** a
  Jericca Cleland levou carta em 11/09 e o **Claus Toksvig Kjær já está escrito neste arquivo como
  "a segunda e última pessoa possível"** e como *"sem prova de 3D"*. Não reabro.
- **Real by Fake** (Montréal) — `alejandro@` e `mjlachance@realbyfake.com` na home. A casa já tem
  uma pessoa em `pessoas.csv`; fica como **segunda pessoa possível**, com endereço provado, para
  uma rodada que precise dela.
- **Raynault VFX** (Montréal) — `jointheteam@raynault.com` parece pessoa e **não é**: é a caixa de
  recrutamento. Cuidado com o padrão.
- **Image Entertainment Corporation** (Magog, QC) — `s.viau@image-cie.com`, publicado com nome e
  cargo: *"Pour communiquer directement avec le fondateur Sylvain Viau"*. **Morreu porque não é
  estúdio:** a própria página diz que a empresa existe para *"faire rayonner des films à fort
  potentiel sur le marché international"*, distribuindo as produções da Iceworks Pictures. É
  distribuidora de direitos, não contrata artista.
- **Crafty Apes**, **Guru Studio**, **Ambassadors**, **9 Story / Portfolio Entertainment** — os
  endereços que parecem de pessoa são **departamentos** (`commercials@`, `pr@`,
  `business.affairs@`, `peopleandculture@`, `productionservices@`, `finance@`, `development@`,
  `distribution@`, `accessibility@`, `consumerproducts@`). Nenhum é nome de gente.
- **Sassybot** (Utrecht) — `johnny@alpha404.com` no `/contact`: **domínio de terceiro**, não da
  casa. Não registrar como endereço da Sassybot.
- **Nowhere** (Amsterdã) — `/team` entrega **15 endereços de pessoa** (`bart@`, `janneke@`,
  `michel@`, ...). **Não é estúdio de animação**: é casa de cultura e aluguel de estúdio
  (`/ruimtes/...`, `verhuur@nowhere.nl`). Falso amigo, anotado para não voltar.
- **Barnstorm VFX** — `andie@barnstormvfx.com` apareceu na varredura e **não se confirmou**: ao
  reabrir `/team` e procurar o contexto do endereço, o `grep` volta **vazio**, ou seja o endereço
  vem de bloco de script e **não há nome nem cargo pareados**. Sem pareamento não vira ficha.

### A REGRA DE MÉTODO QUE SAI DESTA RODADA, e ela é contra mim mesmo

**Regex de desofuscação com `\s+at\s+` e `\s*\.\s*` FABRICA ENDEREÇO QUE NÃO EXISTE.** Minha
primeira varredura reportou `lise@mikrofilm.no` como endereço publicado da Mikrofilm (Oslo). Fui
conferir na fonte: `https://mikrofilm.no/contact` e `https://mikrofilm.no/people` devolvem **a
mesma casca de SPA, 44.635 bytes, com um único `mailto:` — `post@mikrofilm.no`** — e a string
`lise` **não aparece uma única vez** no HTML (`grep -ci lise` = **0**). O endereço tinha sido
**montado pelo meu próprio padrão solto**, a partir de texto qualquer com a palavra "at". Isso é
exatamente o que o brief proíbe: inventar endereço e chamar de verificado.
**A regra:** desofuscação só vale nas formas **delimitadas** (`[at]`, `(at)`, `{at}`, `[dot]`,
`(dot)`, entidade HTML no `href`, `data-cfemail`). A forma solta `nome at dominio ponto tld`
**não** entra em varredura automática — se existir, se lê no olho, na página. O script desta
rodada foi corrigido antes de qualquer ficha ser escrita, e nenhuma ficha saiu do padrão solto.

> **Maestro, 16/09 21h05 UTC:** carta do **Bruce Alcock (Global Mechanic)** escrita e gravada como rascunho `r2057132272551792358` (224 palavras, `confere-carta.py` limpo; sai pelo Apps Script do Vini). **Apparat (Eirik Heldal) e Storm Studios (Espen Nordahl) ficam seguradas até 21/09** pela ressalva de cadência das próprias fichas: as duas casas receberam carta em 11/09 e a Storm ainda tem formulário de 30/08. Marcadas no `pessoas.csv` como `PENDENTE-maestro-escreve-a-partir-de-21-09`.

---

## FICHA NOVA — JHON A, 16/09 às 21h20 UTC: **Secret Level Studios** (Letchworth Garden City, Reino Unido)

**Porta:** a caixa que a própria vaga designa, `jobs@secretlevelstudios.com`, com o assunto que
a casa escreve no botão: `Art Lead / Director Application`. **Não é formulário** (zero `<form>`
na página), e é por isso que ela vem como ficha e não como candidatura.

| Campo | Valor |
|---|---|
| **Email e confiança** | `jobs@secretlevelstudios.com` — **alta**: está no corpo da vaga *e* no `href` do botão Apply |
| **Fonte, aberta por mim hoje** | `https://www.secretlevelstudios.com/jobs/art-director` (e a lista em `https://www.secretlevelstudios.com/careers`) |
| **Vaga** | **Art Lead / Art Director (Character Art)**, full-time, híbrido, Letchworth Garden City |
| **Fora dos EUA?** | Sim, Reino Unido — cabe a frase de realocação do briefing |
| **Régua de veto** | URL final, **7.020 caracteres**, cinco acertos e **os cinco falso positivo**: `based in Letchworth Garden City` (sede) e quatro `hybrid` (modelo de trabalho). **Zero** frase de autorização, residência, nacionalidade ou idioma |
| **Dedupe** | `grep` de `secret level` e `secretlevel` em `enviados.csv`, `processados.csv`, `docs/index.html` e `pessoas.csv`: **zero**. Gmail (`secretlevelstudios OR "Secret Level"`): **nenhuma thread da casa**. Casa e vaga inéditas |

**Por que esta casa e não outra:** é a única porta de **personagem nomeada** que apareceu nesta
rodada inteira em casa nova, e o texto dela é o ofício dele inteiro. O gancho, literal:

> *"We are looking for someone with a strong background in stylised 3D art, particularly
> character art, who is comfortable taking assets all the way from concept through to
> implementation in Unity."*

e, nas responsabilidades:

> *"Design and create 3D stylized characters from concept through to final game implementation.
> Model, texture, rig, skin and animate hero characters and key assets."*

**O que a casa pede por escrito na candidatura**, e a carta tem de responder às duas coisas:
*"Send your CV and portfolio to jobs@secretlevelstudios.com. Please include your current
location and confirm that you're happy with our hybrid working model."* O modelo é **dois dias
por semana no escritório (terça e quarta) e três remotos**.

**Ressalva honesta, e ela é tripla:**
1. O cargo é **liderança** (Art Lead / Art Director) e o bloco *highly desirable* pede
   experiência anterior como Art Lead, Art Director, Lead Artist **ou Senior Artist**. Ele tem a
   última, mais cinco anos de Senior na E-Line, professor e fundador da própria escola, que é a
   resposta de liderança que o `BRIEF-JHON` manda dar. Não inventar título que ele não teve.
2. A vaga pede **rig, skin e animação** de personagem junto da modelagem. Animação não é a força
   dele, e isso se diz em vez de se esconder.
3. A vaga **não diz uma palavra sobre patrocínio de visto**, e o híbrido exige presença semanal
   em Letchworth. O visto precisa ser aberto na carta, não deixado para a entrevista.

> **Maestro, 16/09 22h05 UTC:** carta da **Secret Level Studios (Art Lead / Art Director, Character Art)** escrita e gravada como rascunho `r-8873142809096571374`, com o assunto que a casa exige (`Art Lead / Director Application`), 232 palavras, `confere-carta.py` limpo, localização atual e aceite do híbrido escritos como a vaga pede, ressalvas de animação e de visto ditas. O endereço entrou em `ASSUNTO_PROPRIO_PERMITIDOS` do `envia-rascunhos.gs` (anexa CV e carta): **o Vini precisa colar a versão nova do script no Apps Script antes de rodar `enviarRascunhos()`**, senão este rascunho fica parado por assunto fora do padrão.

---

## JOE, 17/09/2026 00h35 UTC — MUDANÇA DE MÉTODO: DIRETÓRIO DE ASSOCIAÇÃO E SITE QUE TROCOU DE DOMÍNIO

**O que esta rodada mudou.** A ordem era abandonar a varredura por domínio de casa pequena (ontem: 63
domínios abertos, 1 endereço) e trocar por crédito, palestra e rodapé de paper. Fiz as três e digo o
placar de cada uma **antes** das fichas, porque duas delas deram zero e isso é informação:

- **Crédito de jogo (MobyGames):** `www.mobygames.com/company/...` e `/search/` devolvem **HTTP 403 com
  5.4 KB** para este túnel. Não é falta de página, é bloqueio. Sem crédito de jogo nesta rodada.
- **Palestra (GDC):** `schedule.gdconf.com/speaker` devolve **403 / 5.430 bytes**;
  `schedule2026.gdconf.com` dá **502 no CONNECT**. Lista de palestrante do GDC está fechada aqui.
- **Rodapé de paper:** `s2025.siggraph.org` e `s2026.siggraph.org` abrem (200), mas
  **`dl.acm.org` devolve 403** e é lá que moram os PDFs com email de autor. `diglib.eg.org` abre e é
  quase só academia. `digipro.org` responde **342 bytes** (casca). A veia existe, mas o caminho até o
  PDF passa pela ACM, que está barrada neste túnel. **Não gaste a próxima rodada tentando pela ACM.**
- **`recruiter-email` do Teamtailor:** varrido em **73 domínios** nórdicos, britânicos e holandeses
  (`/`, `/careers`, `/jobs`, `/career`, `/work-with-us`, `/join-us`). Apareceu em **um**, e é o que já
  estava registrado desde 07/09: `marina.jonsdottir@starbreeze.com`. Confirma o que o brief diz: a veia
  é rica e **rara**, serve de teste barato, nunca de varredura.
- **Impressum alemão**, que o brief marcava como "o mais promissor ainda não minerado: varrido em **22
  domínios** de casas alemãs, austríacas e suíças (`/impressum`, `/datenschutz`, `/legal-notice`,
  `/imprint`, `/kontakt`, `/legal`). Devolveu **zero endereço de pessoa** — só `newbiz@` e `work@` da
  Woodblock. A lei alemã obriga a nomear a pessoa responsável, mas **não obriga a publicar o email dela**,
  e as casas publicam `info@`. **A veia do impressum pode sair da lista de promessas.**

**O que RENDEU foram duas coisas, e as duas são repetíveis:**

1. **Diretório de associação setorial** (`nordicanimation.com/studios-producers/`), que pareia
   **estúdio + nome + email** em quarenta e nove endereços numa página só. Já tinha sido minerado em
   15/09, mas **não até o fim**: sobraram casas inteiras sem ficha.
2. **Site que trocou de domínio**, que é a armadilha inversa da Stunlock. Ver a ficha da Filmic.

### FICHA 1 — Andreas Ibohm, Filmic Animation (Estocolmo, Suécia)

- **Email: `andreas@filmic.se` — PUBLICADO pela própria casa, com nome E cargo ao lado, confiança ALTA.**
  Nada montado: o endereço está em texto visível, imediatamente abaixo do nome e do título.
- **URLs exatas abertas nesta rodada:** `https://filmic.se/en/contact/` e `https://filmic.se/en/about/`
  (o bloco se repete nas duas). O trecho, na ordem em que a página imprime:
  `Business | Andreas Ibohm | Executive Producer | andreas@filmic.se`, e logo depois
  `Moa Thenstedt Åkerström | Producer | moa@filmic.se`.
- **A ARMADILHA DE DOMÍNIO, e ela é o achado de método desta ficha.** O diretório da Nordic Animation
  publica esta casa como *"Filmic Art, Sweden — Jonathan Knape — `jonathan@filmicart.com`"*. **Não use
  esse endereço.** `https://www.filmicart.com/` **redireciona para `https://filmic.se/en/`**: a casa
  mudou de nome comercial (hoje assina **Filmic Animation**) e de domínio de email. `filmicart.com` é o
  domínio antigo, e um endereço nele é exatamente o tipo de chute que produziu as 17 devoluções de 07/09.
  É a Stunlock ao contrário: lá o site era `stunlock.com` e o email `@stunlockstudios.com`; aqui o
  diretório carrega o domínio velho e o site carrega o novo. **Regra: quando o diretório e o site
  discordarem do domínio, o site manda.**
- **Por que ESSA pessoa e não outra da casa:** a casa publica **exatamente duas** pessoas com endereço,
  e as duas são de negócio e produção. O Andreas Ibohm é **Executive Producer**, ou seja o degrau mais
  alto publicado; a Moa Thenstedt Åkerström é **Producer** e fica como **SEGUNDA e última** pessoa
  possível. Não há endereço publicado de diretor de arte, e o site diz que a direção de arte é
  **interna** (*"in-house art direction"*), sem nomear ninguém. Casa de vinte estações, então cabe na
  régua de casa pequena do brief, onde produtor executivo e dono respondem eles mesmos.
- **Gancho, com a frase do próprio estúdio entre aspas:** a página de serviços escreve que o time faz
  *"photo-realistic 3D modeling and lighting or rigging and animation of advanced 3D characters or
  animals"*, e a casa se apresenta como *"an award winning animation production company, founded in
  Sweden in 2007"* com força em *"managing large, technical, and highly creative projects in 3D and 2D"*.
  O portfólio de clientes citado pela própria home tem **Clash Royale, Minecraft e Paradox Interactive**,
  ou seja **trailer de jogo**, que é onde personagem estilizado aparece.
- **Casa fora dos EUA: SIM, Suécia (Estocolmo, Gamla Stan).** A frase de realocação **entra**.
- **O que o Gmail devolveu no dedupe:** a busca `madebyus OR compassfilms OR "Made By Us" OR "Compass
  Films" OR dockhus OR leefilm OR "Filmic Art" OR Tulipop` devolveu **uma** thread, e ela é da Filmic:
  carta fria em **02/09 para `jobb@filmic.se`** e follow-up em **07/09 para o mesmo endereço**. As duas
  foram para **CAIXA funcional**, não para pessoa: ou seja a casa tem **zero pessoa** contatada e o
  Andreas é a **primeira**, com uma vaga de cota ainda livre depois dele. Em `pessoas.csv` a string
  `filmicart` só aparece **dentro do texto de dedupe de outra ficha** (a rodada de 15/09 pesquisou e não
  escreveu ficha); `andreas@filmic.se` e `filmic.se` **não** aparecem em `pessoas.csv`,
  `processados.csv` nem `docs/index.html`.
- **RESSALVA HONESTA, e são quatro:** (1) a casa é de **publicidade e trailer**, não de longa de
  animação nem de pipeline de personagem de filme; o personagem aparece a serviço de marca.
  (2) O cargo é **produção**, não arte: o Andreas não é o par de ofício dele, é quem decide contratar.
  (3) A casa **já recebeu duas mensagens** na caixa `jobb@` e não respondeu nenhuma, então a terceira
  mensagem precisa reconhecer isso em vez de fingir primeiro contato — **a carta é o terceiro toque na
  mesma casa**, e por isso tem que ir para a pessoa e não para a caixa. (4) A própria página de Talent
  lista o que a casa procura (*"an experienced Producer, Junior Producer, 3D artist, Comp Artist, 2D
  Animator, Game Capture Artist, Editor or Illustrator"*): diz **3D artist**, e **não** diz character
  artist. Telefones publicados ao lado dos dois nomes **deliberadamente não registrados**, porque o
  repositório é público.

### FICHA 2 — Josh Robinson, Time Based Arts (Londres, Shoreditch, Reino Unido) — SEGUNDA E ÚLTIMA DESTA CASA

- **Email: `josh@time-based-arts.com` — PUBLICADO pela própria casa, com nome E cargo na mesma linha,
  confiança ALTA.** Caixa individual, não funcional. Nada montado.
- **URL exata aberta nesta rodada:** `https://www.timebasedarts.co.uk/contact`, que **redireciona para
  `https://www.time-based-arts.com/contact`** (outra confirmação da regra de domínio desta rodada: o
  domínio `.co.uk` é vitrine, o domínio de email é `time-based-arts.com`). A página imprime seis pessoas,
  nesta ordem, cada nome seguido do cargo e do endereço:
  `Harry Jones / Talent Enquiries / jobs@`, `Tom Johnson / Managing Director / tom@`,
  **`Josh Robinson / Deputy Managing Director / EP / josh@`**,
  `Dan Kreeger / Executive Colour Producer / dan.kreeger@`, `Sian Jenkins / Head of Production / sian@`,
  `Georgie Evans / New Business / georgie.evans@`.
- **Por que ESSA pessoa e não outra da casa, e a escolha aqui é entre dois:** o **Tom Johnson (MD) já
  recebeu** a carta fria em 06/09 e o follow-up em 08/09, sem resposta, então a cota desta casa fecha com
  **esta segunda pessoa e mais nenhuma**. Das cinco restantes, a Sian Jenkins é produção, o Dan Kreeger é
  **cor** (nada a ver com personagem), a Georgie Evans é comercial, e o **Harry Jones** é o nome que a casa
  põe em `Talent Enquiries` — mas o endereço dele é `jobs@`, **caixa compartilhada**, e a carta ficaria
  onde a campanha já sabe que não é lida. Sobra o **Josh Robinson, Deputy Managing Director / EP**: é o
  segundo degrau da casa, tem caixa individual publicada, e num estúdio deste porte é quem realmente
  redistribui um email que o MD não respondeu. **Registro útil para o maestro: `jobs@time-based-arts.com`
  tem dono com nome, Harry Jones**, e isso serve se algum dia a via de caixa for usada.
- **Gancho com a frase do próprio estúdio, entre aspas:** a página de contato abre convidando
  *"Feel free to call or email to discuss who we are, what we do and how we can help collaborate on a
  project, or even if you'd just like..."*, e o menu do site declara as quatro frentes da casa:
  **`VFX | Grading | Archive | Art Practice`**. A carta de 06/09 para o Tom já usou a frase da página
  About sobre querer ouvir artista 2D ou 3D; **a carta nova precisa usar outra frase**, e a de
  `Art Practice` é a que ainda está livre.
- **Casa fora dos EUA: SIM, Reino Unido (Londres).** A frase de realocação **entra**.
- **O que o Gmail devolveu no dedupe:** `time-based-arts OR "Time Based Arts" OR timebasedarts` devolveu
  **exatamente uma thread**, com **duas mensagens, as duas ENVIADAS pela campanha** para
  `tom@time-based-arts.com` (06/09 e follow-up de 08/09) e **nenhuma resposta**. Ou seja: a casa **não
  recusou**, **ninguém de lá respondeu** (a thread é do Joe, não do Comunicador), e `josh@` **não aparece**
  em `pessoas.csv`, `processados.csv` nem `docs/index.html`. `processados.csv` confirma o histórico em duas
  linhas de 06 e 07/09.
- **RESSALVA HONESTA, e são quatro:** (1) a casa é **pós-produção de publicidade** — VFX e color grading —
  e **não nomeia pipeline de personagem** em lugar nenhum do site; o encaixe é indireto e a carta não pode
  fingir o contrário. (2) É a **terceira mensagem** da campanha para esta casa em onze dias; duas já foram
  ignoradas, e a honestidade da abertura é o que evita soar como spam de insistência. (3) O cargo é de
  **gestão e produção executiva**, não de arte: o Josh não abre ZBrush, ele encaminha. (4) A cota fecha
  aqui: **se esta carta não voltar, a Time Based Arts sai da fila de pessoas**, e a única via restante é
  `jobs@` com o nome do Harry Jones. Telefone publicado na página **deliberadamente não registrado**,
  porque o repositório é público.

### FICHA 3 — Ronnie Fridthjof, Fridthjof Animation (Dinamarca) — E ELA CORRIGE A FICHA DE ONTEM

- **Email: `ronnie@fridthjof.com` — PUBLICADO, confiança ALTA.** Não é montado: o endereço está escrito
  no diretório da associação, imediatamente depois do nome dele.
- **URL exata aberta nesta rodada:** `https://nordicanimation.com/studios-producers/`. O bloco, na ordem
  crua em que a página imprime: *"Fridthjof Animation"* → *"Fridthjof Animation is a production company
  that develops and produces animated feature films and TV-series for kids."* → *"Lotte og Totte"* →
  **`Fridthjof Animation, Denmark` → `Ronnie Fridthjof` → telefone → `ronnie@fridthjof.com` →
  `http://www.fridthjof.com/`**. O endereço vem **rodeado pelo nome da casa, pelo nome da pessoa e pelo
  site da casa**, nessa sequência, que é o mesmo pareamento das fichas nórdicas de 15/09.
- **ISTO CORRIGE O REGISTRO DE ONTEM.** A rodada de 16/09 às 20h35 listou `fridthjof.com` entre os
  domínios *"abertos sem pessoa"*. O motivo agora está medido: `https://www.fridthjof.com/` devolve **200
  com 2,2 MB e apenas quatro linhas de texto** — *"Bundled Page | This page requires JavaScript to
  display. | F | Unpacking..."*. É **SPA que não renderiza por `curl`**, não casa sem endereço publicado.
  **Regra que sai daí: "domínio sem endereço" só vale quando o HTML tem texto; página que só diz
  "requires JavaScript" é NÃO CONFERIDA, e o endereço dela pode estar publicado em diretório de
  associação, como está aqui.**
- **Por que ESSA pessoa e não outra da casa:** o diretório publica **um único nome** para esta casa, e é o
  dele; a casa **leva o nome dele** (Fridthjof), ou seja é o dono. Pela régua do brief para casa pequena,
  dono e fundador vêm primeiro e costumam responder eles mesmos. Não há segunda pessoa publicada em
  nenhuma das duas fontes, então **não existe segunda opção para esta casa hoje**.
- **Gancho com a frase do próprio diretório sobre a casa, entre aspas:** *"Fridthjof Animation is a
  production company that develops and produces animated feature films and TV-series for kids"*, com
  *"Lotte og Totte"* como o título que a própria entrada destaca.
- **Casa fora dos EUA: SIM, Dinamarca.** A frase de realocação **entra**, e é prioridade 2 (nórdicos).
- **O que o Gmail devolveu no dedupe:** `"Striking Distance" OR strikingdistance OR "Jon Robins" OR
  fridthjof` devolveu **`{}`**, zero thread. Em `pessoas.csv` a string `fridthjof` aparece **só dentro do
  texto de dedupe de outra ficha** (a rodada de 15/09 pesquisou o nome e não escreveu ficha nenhuma);
  `ronnie@fridthjof.com` **não** aparece em `pessoas.csv`, `processados.csv` nem `docs/index.html`.
  **Casa inédita para a campanha inteira.**
- **RESSALVA HONESTA, e é a mais pesada das três fichas:** (1) **a técnica não está confirmada.** Nem o
  diretório nem o site (que não renderiza) dizem se a casa é **2D ou 3D**, e o título que ela destaca,
  *Lotte og Totte*, é de tradição de livro ilustrado dinamarquês — há chance real de ser **2D**, e 2D é o
  que matou a Head Gear no registro de ontem. **A carta tem de perguntar em vez de afirmar**, e se a
  resposta for 2D a casa sai da fila. (2) **O cargo dele não está publicado**: nome, telefone, email e
  site, sem título; ele é tratado aqui como dono por causa do nome da empresa, o que é inferência razoável
  e **não** é fato publicado. (3) É **produtora que desenvolve e produz**, não necessariamente estúdio com
  pipeline interno; pode terceirizar a animação, e nesse caso não contrata artista. Telefone publicado
  **deliberadamente não registrado**, porque o repositório é público.

### FICHA 4 — Jon Robins, Striking Distance Studios — **SEM-EMAIL**, e a linha vale assim

- **Email: NENHUM. `confianca = sem-email`.** Nada foi montado. Isto não é fracasso: a linha guarda
  **nome + cargo + estúdio** para a rodada que achar o endereço.
- **URL exata aberta nesta rodada:** `https://www.cgspectrum.com/mentors` (437 KB, HTTP 200). O texto,
  literal: *"Jon currently works as a **Lead Character Technical Artist at Striking Distance Studios**
  where he loves solving problems and helping teams in as many ways as he can."*, e o campo `Known for`
  do cartão dele diz **`Marvel's Avengers`**.
- **Por que ESSA pessoa e não outra da casa:** é o **único nome de departamento de personagem** que a
  página de mentores entrega numa casa que a campanha nunca tocou. A página é rica em nome e cargo (foi
  ela que devolveu Matteo Sala, *Senior Character and Creature Modeler* da Framestore em Londres, e Anna
  Beganskaya, 3D character artist), mas essas duas casas **já estão no teto de duas pessoas** (Framestore:
  Lizi Bedford e Glenn Melenhorst; Riot: três). Striking Distance está em zero.
- **Gancho, e a honestidade aqui importa:** o gancho **não é do estúdio**, é da bio do próprio mentor, e
  ela é o que existe: *"where he loves solving problems and helping teams in as many ways as he can"* —
  uma pessoa que se descreve assim é a que responde um email pedindo direção. O crédito comum é
  **Marvel's Avengers**, que a página dele imprime.
- **Casa fora dos EUA: NÃO.** Striking Distance Studios é dos **Estados Unidos** (San Ramon, Califórnia),
  então **a frase de realocação NÃO entra** e o assunto de autorização de trabalho tem de ser dito de
  frente, porque nos EUA é a pergunta que mata a conversa.
- **O que o Gmail devolveu no dedupe:** `"Striking Distance" OR strikingdistance OR "Jon Robins" OR
  fridthjof` devolveu **`{}`**. Em `pessoas.csv` o único acerto de *"Striking Distance"* é **dentro da
  ficha do Glauco Longhi** (Santa Monica Studio, 12/09), que menciona a casa de passagem: **não é pessoa
  desta casa**. Zero em `processados.csv` e `docs/index.html`. **Casa inédita.**
- **RESSALVA HONESTA, e são quatro:** (1) **sem email não há carta**, e o endereço não foi achado em
  nenhuma fonte pública nesta rodada; **não monte `jrobins@` nem `jon.robins@`** porque não há um único
  endereço daquele domínio visto publicado para servir de prova de padrão. (2) O cargo é **Character
  Technical Artist**, ou seja **rigging e ferramentas**, não escultura nem superfície: ele é colega de
  departamento, não par de ofício, e a carta tem de pedir **indicação**, não vaga. (3) A casa é **dos EUA
  e a prioridade da rodada era Vancouver, nórdicos, Holanda e Reino Unido** — esta linha entra como
  estoque, no fim da fila. (4) A fonte é **página de escola**, não do estúdio, e página de escola
  envelhece: o cargo está escrito no presente (*"currently works"*), mas **não há data na página**, então
  a confirmação de que ele continua na casa **não foi feita** e tem de ser feita antes de qualquer carta.

### FICHA 5 — Sofie Edvardsson, Soja (Estocolmo e Tjörn, Suécia)

- **Email: `sofie@soja.se` — PUBLICADO pela própria casa, com nome E cargo no mesmo cartão, confiança
  ALTA.** Caixa individual. Nada montado.
- **URL exata aberta nesta rodada:** `https://www.soja.se/om-oss`. A página publica **três** pessoas, cada
  uma com nome, cargo e endereço, nesta ordem crua: `Simon Österhof / Producent / simon@soja.se`,
  **`Sofie Edvardsson / Creative Director / sofie@soja.se`**, `Jakob Nyström / Animation Lead /
  jakob@soja.se`. Conferido também em `https://www.soja.se/kontakt`, que só publica `hej@soja.se` e
  `jobb@soja.se` — **quem varrer só `/kontakt` conclui "casa sem endereço de pessoa" e erra**, porque as
  três pessoas moram em `/om-oss` (e `/about` e `/contact` em inglês devolvem **404**, o que engana a
  varredura: o site é em sueco e os caminhos são `om-oss` e `kontakt`).
- **Por que ESSA pessoa e não outra da casa:** dos três, o Simon Österhof é **produtor** (e a página de
  contato diz explicitamente que quem atende o telefone é *"producent-Simon"*, ou seja é a porta
  comercial) e o Jakob Nyström é **Animation Lead**, que é animação e não modelagem. A **Sofie
  Edvardsson é Creative Director**, o único cargo de **chefia criativa** publicado, e é exatamente o alvo
  que o brief manda escolher em casa pequena: quem viu o portfólio e quer a pessoa, não o RH e não o
  produtor. **Jakob Nyström fica como SEGUNDA e última** pessoa possível, com endereço já provado, se a
  primeira carta não voltar.
- **Gancho com a frase do próprio estúdio, entre aspas:** a casa se apresenta como *"en kreativ
  animationsstudio som funnits sedan 2010"* e diz ter construído *"en djup verktygslåda och en bred
  palett"* (uma caixa de ferramentas profunda e uma paleta larga). E o detalhe que serve de ponte para o
  ofício dele: a própria página de contato lista o vocabulário da casa como
  *"Animation, motion design, explainer, **karaktärsanimation**, voiceover"* — **karaktärsanimation**,
  animação de personagem, escrita pela casa.
- **Casa fora dos EUA: SIM, Suécia (Estocolmo e Tjörn, perto de Gotemburgo).** A frase de realocação
  **entra**, e é prioridade 2 (nórdicos).
- **O que o Gmail devolveu no dedupe:** `soja.se OR Soja OR Osterhof OR Edvardsson OR "Sofie Edvardsson"`
  devolveu **`{}`**, zero thread, nem enviada nem recebida. `grep -ic` de `soja|Edvardsson|Osterhof|
  Nystrom` em `pessoas.csv`, `processados.csv` e `docs/index.html`: **0, 0 e 0**. **Casa inédita para a
  campanha inteira**, e ela veio do diretório da Nordic Animation, que em 15/09 foi minerado só em parte.
- **RESSALVA HONESTA, e são quatro:** (1) a casa é de **comunicação, explainer e motion design** — as
  palavras dela são *"engagera, motivera, förklara eller utbilda"* — e **não** é pipeline de personagem
  3D; a palavra `karaktärsanimation` aparece num **glossário de termos**, não como capacidade declarada,
  e isso é bem mais fraco do que um crédito. (2) Não há **nenhuma** menção a 3D, escultura, groom ou
  look dev no site; o trabalho visível é animação e motion. (3) A casa **não anuncia vaga**: o que a
  página de contato oferece é **estágio** (*"Vi erbjuder praktikplatser när det är möjligt"*), com
  `jobb@soja.se` reservado para isso, e estágio não serve para um sênior de dez anos. (4) O site é **em
  sueco** e a carta vai em inglês; casa pequena sueca costuma trabalhar em inglês sem problema, mas isso
  não está escrito em lugar nenhum e é suposição. Telefones publicados ao lado dos três nomes
  **deliberadamente não registrados**, porque o repositório é público.

### O DEDUPE NA CAIXA SALVOU UMA FICHA ERRADA, E É O ACHADO MAIS IMPORTANTE DESTA RODADA

A primeira ficha que eu tinha pronta era **Arnfinn Moseng, HEAD OF STUDIO da Qvisten Animation**
(`arnfinn.moseng@qvisten.no`, publicado com nome e cargo em `https://www.qvisten.no/contact`, junto de
onze pessoas da casa). **Ela foi jogada fora, e o motivo é a regra do dedupe na caixa.**

`pessoas.csv` tem **uma** pessoa da Qvisten (Rasmus A. Sivertsen, Creative Director, carta de 03/09). Pela
planilha, sobrava uma vaga de cota. **A caixa diz outra coisa:** `mcp__Gmail__search_threads` com
`qvisten OR Moseng OR arnfinn ...` devolveu **duas threads enviadas**, para **duas pessoas diferentes**:

1. `hedda.toftner@qvisten.no` — carta fria em **26/08** e follow-up em **02/09**;
2. `rasmus@qvisten.no` — carta em **03/09**.

Hedda Toftner é **HR Manager** da casa, ou seja **pessoa com nome**, não caixa funcional — e ela **não
está em `pessoas.csv`**. Com ela a Qvisten está em **DUAS pessoas** e **a cota da campanha fechou**. Se eu
tivesse conferido só a planilha, esta rodada teria produzido a terceira carta para a mesma casa.

**A regra, escrita para a próxima rodada:** `pessoas.csv` **não é** o registro completo de quem recebeu
carta. Cartas escritas antes do arquivo existir, ou por outra frente da campanha, só aparecem no
**`in:sent` do Gmail**. **Teto de duas por casa se conta no Gmail, por DOMÍNIO, não no CSV.**

### CASAS ABERTAS NESTA RODADA SEM ENDEREÇO DE PESSOA APROVEITÁVEL (para ninguém repetir)

Varredura de `/team`, `/crew`, `/about`, `/people`, `/our-team`, `/about-us`, `/studio`, `/contact`,
`/company`, `/staff`, `/who-we-are` e `/leadership` em **124 domínios** de casas de animação, jogos e VFX
das regiões de prioridade, mais `/impressum`, `/datenschutz`, `/legal-notice`, `/imprint`, `/kontakt` e
`/legal` em 22 domínios de língua alemã.

- **Nórdicos:** `suncreature.com`, `copenhagenbombay.com`, `jafilm.dk`, `m2film.dk`, `sweatbox.dk`,
  `bacon.dk`, `firstflightfilms.dk`, `astafilm.dk`, `nicedrawings.dk`, `maipo.no` (só `maipo@maipo.no`),
  `tordenfilm.no` (só `faktura@`), `zigzag.se` (só `Emailanimation@zigzag.se`, que é rótulo grudado no
  endereço), `pennfilm.se`, `filmtecknarna.se`, `hobbyfilm.se` (só `talk@` e `Invoice@`),
  `animavitae.com`, `gigglebug.com`, `pyjamafilms.com`, `densisteskilling.no`, `ilpvfx.com` (só `vfx@`),
  `goodbyekansas.com`, `cinenicfilm.se` (três endereços de pessoa, mas é produtora de **live-action** e
  documentário).
- **Holanda:** `submarine.nl` (só `studiotalent@`), `studiopupil.com` (só `dario@`, **já é ficha de
  13/09**), `polderanimation.nl`, `a-film.com`, `klaar.nl`, `jobjorisenmarieke.nl`, `studiosmack.nl`,
  `pedri.nl`, `frameorder.com`, `guerrilla-games.com`, `nixxes.com`, `abbeygames.com`, `ronimo.nl`,
  `triumphstudios.com`, `spellbound.nl`.
- **Reino Unido e Irlanda:** `blue-zoo.co.uk`, `aardman.com`, `jellyfishpictures.co.uk`,
  `milk-vfx.com` (o `data-cfemail` **foi decodificado** e dá `info@`, `recruitment@` e `newbusiness@`, os
  três genéricos), `axisstudiosgroup.com` (cfemail decodificado = `info@`),
  `lighthousestudios.ie` (cfemail decodificado = `info@`), `oneofus.co.uk`, `territorystudio.com` (só
  `newprojects@`, `nyc@`, `sf@`, `bcnstaff@`), `paintingpractice.com`, `nexusstudios.com` (só `eps@`,
  `oc@`, `prmarketing@`), `passion-pictures.com` (o endereço que parece de pessoa é
  `passiondoccvs@thetalentmanager.com`, **domínio de terceiro**), `coffeeandtv.co.uk`,
  `aproductions.co.uk`, `wildseedstudios.com`, `sixteensouth.tv` (só `rights@` e `website@`),
  `mackinnonandsaunders.com`, `studiogobo.com`, `brownbagfilms.com` (só `explore.animation@`,
  `infobali@`, `infotoronto@`), `cartoonsaloon.ie` (só `festivals@`), `boulder-media.com`, `jam-media.com`,
  `pinkkongstudios.com`, `kavaleer.com`, `factory.uk.com`, `eyeanimation.co.uk`, `dogeatdogfilms.co.uk`,
  `secondhomestudios.co.uk`, `flickerpix.com`, `treehouserepublic.com`, `dailymadness.ie`, `distillery.ie`,
  `themill.com`, `unit.tv`, `finish.co.uk`, `blinkink.co.uk`, `strangebeast.tv`, `electrictheatre.tv`,
  `calon.tv`, `aplusc.tv`, `owlhousestudios.com`, `windingsnake.com`, `spiteyourface.com`,
  `creativeassembly.com`, `frontier.co.uk`, `splashdamage.com`, `sumo-digital.com`, `d3tltd.com`,
  `coatsink.com`, `roll7.com`, `dlalastudios.com`, `payloadstudios.com`, `hutch.io`, `fireproofgames.com`,
  `mediamolecule.com`, `ninjatheory.com`, `rare.co.uk`.
- **Canadá:** `wildbrain.com`, `yetifarm.ca`, `stellarcreative.tv`, `copperheart.ca`, `jamfilled.com`,
  `sinkingship.ca`, `mrxfx.com`, `cvdvfx.com`, `edfilms.net`, `atelieranimation.ca`, `modusfx.com`,
  `alchemy24.ca`, `fakestudio.tv`, `boatrocker.com` (só `humanresources@`), `windsunsky.com` (só
  `connect@`), `wowunlimited.com`, `nelvana.com`, `klei.com` (só `indiebox@` e `livesupport@`),
  `piranhagames.com` (só duas caixas de `zendesk`), `beamdog.com`, `inflexiongames.com`, `ludia.com` (só
  `Business@`), `frimastudio.com` (só `medias@`), `redbarrelsgames.com`, `panachedigitalgames.com`,
  `sabotagestudio.com` (só `bugs@`), `thunderlotusgames.com` (só `business@`), `tributegames.com`,
  `digitalextremes.com`, `capybaragames.com`, `drinkboxstudios.com`, `snowedin.ca`, `otherocean.com`,
  `arcproductions.com`, `turnipandduck.com`.
- **Língua alemã, pelo `impressum`:** `rise-fx.com`, `trixter.de`, `pixomondo.com`, `mackevision.com`,
  `sehsucht.de`, `chimneygroup.com`, `infected.de`, `unexpected.de`, `luxx.studio`,
  `slaughterhouse-fx.de`, `studio-rakete.de`, `scanlinevfx.com`, `arx-anima.com`, `neopolis.tv`,
  `studio100animation.net`, `lumatic.eu`, `mokkomedia.de`, `grid-vfx.com`, `kaiserkoi.de`, `tridigital.de`,
  `maximdigital.de`. **Só a `woodblock.tv` devolveu algo, e era `newbiz@` e `work@`.**

### ENDEREÇO ACHADO E DESCARTADO, com o motivo de cada um

- **Dockhus Animation** (Trollhättan, SE) — `mikael@dockhus.com` (Mikael Lindbom), publicado no diretório
  da Nordic Animation. **Morreu por técnica, e a casa é explícita:** `dockhusanimation.com/en/` lista o que
  ela oferece como *"2D animation | Stop motion | Cutout"*. **Zero 3D.** É a armadilha da Head Gear.
- **LEE Film** (Estocolmo, SE) — `linda@leefilm.se`, publicado **com cargo** no site da própria casa
  (*"Producer | Linda Hambäck | Email: linda@leefilm.se"*, em `https://leefilm.se/`). **Morreu por
  técnica:** o catálogo é *The Ape Star*, *Gordon & Paddy* e *Who's who?*, ou seja **2D e stop-motion**.
  Fica registrado com endereço provado para o caso de aparecer projeto 3D. A mesma página avisa
  *"We have no possiblites to read and comment new scripts or ideas that are sent to us"* — **isso é sobre
  roteiro, não sobre candidatura**, e não conta como veto.
- **Tulipop Studios** (Reykjavík, IS) — `helga@tulipop.com` (Helga Árnadóttir) no diretório. **Morreu por
  técnica declarada:** `tulipopstudios.com` escreve que *Tulipop: Magical Seasons* é
  *"high-quality **2D** animated films"*.
- **Compass Films** (Reykjavík, IS) — `heather@compassfilms.is` no diretório. **Morreu porque não é
  estúdio:** o site diz ser *"a leading, award-winning film and television production company"*
  co-fundada por produtores, que também *"offers servicing for international productions, supporting
  logistics, financing and production arrangements in Iceland"*. É produção e serviços, com animação
  como uma linha entre outras; o site publica só `info@compassfilms.is`.
- **Made By Us** (Copenhague, DK) — `kqm@madebyus.dk` (Katrin Quist-Møller) no diretório. **Morreu porque
  é casa de conceito:** *"et uafhængigt koncept- og produktionshus"*, com live-action, factual e
  documentário; o site **não publica endereço nenhum**.
- **Storm Films** (Oslo, NO) — `mbg@stormfilms.no` **não vira ficha**: o endereço só existe dentro do
  bloco de dados estruturados (`"legalName":"Nedre gate 7d","email":"mbg@stormfilms.no"`) e **não há nome
  nem cargo pareados** em lugar nenhum; o site é SPA e `/team`, `/about-us` e `/crew` **são a página 404
  da casa**. É o caso Barnstorm de ontem: sem pareamento não vira ficha.
- **Animated Company** (Londres, UK) — `douglas@animatedcompany.com` apareceu na varredura e **não se
  confirma**: ao reabrir, o `grep` pelo endereço volta **vazio** no HTML visível. E a casa se descreve no
  `<title>` como *"AI Animation & VFX Studio"*, o que a tira da fila por si só.
- **Plastilin Media** (Imatra, FI) e **UpNorth Film** (Oslo, NO) — os endereços publicados no diretório são
  `kirilllr@yahoo.com` e `mmotovska@gmail.com`, **caixas pessoais de provedor gratuito**, não endereço
  institucional. Não registrados como via de contato de estúdio.
- **Sphere Media / Sphere Animation / Oasis Animation** (Montréal, CA) — a varredura de
  `oasisanimation.com/contact` devolveu **doze** `data-cfemail`, e a decodificação deu endereços com
  forma de pessoa (`bdube@`, `mdastous@`, `rchasse@`, `rmouchawar@`, `drozon@`, `rfaour@` em
  `sphere-media.com` e **`jbeauchemin@sphereanimation.com`**). **Não virou ficha por dois motivos:**
  (1) a página de contato do grupo publica **só** `info@`, `carrieres@`, `communications@` e `projets@`,
  e os endereços de pessoa **não estão pareados com nome nem cargo** em nenhuma página que eu tenha
  conseguido abrir; (2) o próprio grupo descreve a Sphère Animation como
  *"l'un des plus importants studios d'animation numérique **2D** au Canada"* — **2D**. Anotado com
  cuidado porque **`oasisanimation.com` passou a devolver 403 de Cloudflare** depois da varredura
  (bloqueio por taxa, não parede permanente): quem voltar, vá devagar e por uma URL só.
- **Karrot Animation** (Londres) — `chris@wearekarrot.com` reapareceu em
  `karrotanimation.com/contact`. **Já está em `pessoas.csv` desde 07/09** e ainda sem carta. Não é nome
  novo; o que esta rodada acrescenta é a confirmação de que o endereço **continua publicado** e de que o
  domínio de email (`wearekarrot.com`) é **diferente** do domínio do site (`karrotanimation.com`).
- **Icon Creative Studio** (Vancouver) e **Timeless Films** (UK) — `carson@iconcreativestudio.com` e
  `ralph@timelessfilms.co.uk` reconfirmados publicados, e **as duas casas já têm essa pessoa** em
  `pessoas.csv` (08/09 e 16/09). Não são nomes novos.

### AS TRÊS PAREDES DESTA RODADA, medidas

| Fonte | O que devolveu | Leitura |
|---|---|---|
| `www.mobygames.com/company/...` e `/search/` | **403, 5.4 KB** | crédito de jogo **não** sai por aqui neste túnel |
| `schedule.gdconf.com/speaker` | **403, 5.430 bytes** | lista de palestrante do GDC fechada |
| `schedule2026.gdconf.com` | **502 no CONNECT** | idem |
| `dl.acm.org/doi/proceedings/...` | **403, 5.5 KB** | é onde moram os PDFs de SIGGRAPH e DigiPro com email de autor |
| `digipro.org` | **200 com 342 bytes** | casca |
| `ca.linkedin.com/in/...` | **HTTP 999** | LinkedIn público **não abre** por fetch; já era decisão do Vini não usar LinkedIn para casa grande, e agora nem serve para confirmar cargo |
| `diglib.eg.org` | 200, 476 KB | abre, mas é quase só academia |
| `s2025.siggraph.org` / `s2026.siggraph.org` | 200 | abrem, mas o PDF com rodapé de autor está na ACM |

### UMA ARMADILHA DE VARREDURA QUE EU MESMO PISEI, e a correção do script

Meu primeiro passe aceitou qualquer resposta com **mais de 800 bytes** como "página existe". **Errado:**
a página 404 de Squarespace e de Webflow devolve **40 KB a 180 KB** com o rodapé e o bloco de dados
estruturados inteiros, e **derrama endereço**. Foi assim que `mbg@stormfilms.no` e
`douglas@animatedcompany.com` entraram na minha lista de candidatos: os dois vieram de páginas **404**
(`stormfilms.no/team`, `animatedcompany.com/about`). **A correção: antes de acreditar num endereço, procure
no texto limpo as frases `We couldn't find the page`, `Page not found` e `404` — se estiverem lá, a
página não existe e o endereço veio do rodapé, sem nome e sem cargo.** Nenhuma ficha desta rodada saiu de
página 404.

### VANCOUVER E BC, A PRIORIDADE 1, FECHOU EM ZERO — E O MOTIVO É NOMEÁVEL

A ordem da rodada era achar nome de arte com cargo na **SkyBox Labs** (Burnaby, 235 pessoas, NetEase) por
crédito de jogo, palestra ou artigo, e o mesmo em Blackbird, The Coalition, Relic, Kabam, Phoenix Labs,
EA Motive, Behaviour e Beenox. **Não saiu uma pessoa, e não é por falta de tentativa: as três fontes de
nome que essas casas usam estão fechadas neste túnel ao mesmo tempo** — MobyGames (403), GDC (403/502) e
LinkedIn (999). Sem elas, o que resta é o site do estúdio, e a rodada de ontem já mediu que
`skyboxlabs.com` publica cinco caixas funcionais e **nenhum nome com cargo**.

**O que a próxima rodada deve tentar em Vancouver, em ordem, porque eu não tentei estes:**
1. **Crédito no YouTube:** o crédito final do trailer e do vídeo de lançamento costuma listar o time de
   personagem inteiro com cargo, e `youtube.com` não está barrado.
2. **80.lv e ArtStation Magazine por busca de texto**, procurando o nome do estúdio no corpo do artigo em
   vez de no título; ArtStation está em Cloudflare, mas `80.lv` abriu na busca desta rodada.
3. **Press release da própria casa** (`skyboxlabs.com/news`), que em anúncio de projeto novo às vezes cita
   o diretor de arte pelo nome.
4. **Duas casas de BC que esta rodada NÃO conseguiu conferir e que não são parede:** `cvdvfx.com` e
   `stellarcreative.tv` abriram e não publicam pessoa; mas `bardel.ca` (403 Cloudflare),
   `versatile.media` (erro de certificado) e `scanlinevfx.com` continuam pendentes de **navegador de
   tela**, não de `curl`. A Bardel é uma das maiores de Vancouver e segue **não conferida**, não fechada.

### PLACAR HONESTO DA RODADA

**Cinco pessoas novas**, dentro da faixa de 4 a 8, sendo **quatro com endereço PUBLICADO e confiança
ALTA** (Filmic, Time Based Arts, Fridthjof, Soja) e **uma `sem-email`** (Striking Distance).
**Nenhum endereço montado por padrão de domínio. Nenhum inventado.**
Por região: **Suécia 2, Reino Unido 1, Dinamarca 1, Estados Unidos 1 (sem-email)**.
**Vancouver e BC: zero**, com o motivo medido acima. **Holanda: zero.**
Uma ficha foi **descartada pelo dedupe na caixa** (Qvisten, que já estava no teto de duas) e **seis
endereços publicados foram descartados por técnica ou por não serem estúdio** (Dockhus, LEE Film,
Tulipop, Compass, Made By Us, Sphere/Oasis).

> **Maestro, 17/09 01h25 UTC:** lote de quatro cartas escrito e gravado em rascunho (`confere-carta.py` limpo, pior par do lote 38%): Andreas Ibohm / Filmic Animation `r1295132988803354840`; Josh Robinson / Time Based Arts `r8492986745259918271` (a carta diz que o Tom não respondeu e que esta é a última tentativa); Ronnie Fridthjof / Fridthjof Animation `r-6682290126727102652` (a carta pergunta se as produções são 3D, porque a técnica não está confirmada); Sofie Edvardsson / Soja `r9001855112013796033`. Jon Robins (Striking Distance) fica `sem-email`. Saem pelo Apps Script do Vini.


---

## JOE, 17/09/2026 04h35 UTC — A VEIA QUE RENDEU FOI A **PÁGINA DE DETALHE DO DIRETÓRIO IRLANDÊS ATÉ O FIM** MAIS UM ACHADO EM VANCOUVER

**O que esta rodada fez de diferente.** A ordem trazia três veias. Digo o placar de cada uma **antes**
das fichas, porque uma delas é veia nova de verdade e duas deram zero:

1. **Nomes de casa novos do Jhon A (Triggerfish, Dulaman, Whackala, Stiuideo Fia e os outros dos 14):**
   RENDEU. Mas não pelo site deles: rendeu pela **página de detalhe do diretório**
   `animationireland.com/studios/<slug>/`, que é a mesma veia de 14/09 e que **nunca tinha sido lida
   até o fim** — as 47 páginas foram abertas naquele dia, mas os slugs da **página 2** do índice
   (`/studios/page/2/`) e as casas novas entradas depois **ficaram fora**. Abri as 47 de novo e os 21
   slugs inéditos, e o bloco `studio_contacts` do HTML entrega `[<h4>Nome</h4>][<p class="c_role">
   cargo</p>][mailto:]` colado, sem ambiguidade.
2. **Rodapé de paper e palestra fora da ACM:** não gastei a rodada nisso, porque a rodada de 00h35 já
   mediu a ACM em 403 e o caminho até o PDF passa por lá. Ver a nota de método no fim.
3. **Crédito de 80.lv / ArtStation Magazine / Animation Magazine para Vancouver:** **ZERO, e medido.**
   `80.lv/?s=SkyBox+Labs` responde **200 com 173 KB e nenhum link de artigo no HTML** (a busca é
   client-side, igual ao `/jobs?search=` do Hitmarker), e `animationmagazine.net/?s=...` responde
   **403 com 919 bytes**. Vancouver **não saiu por imprensa** nesta rodada — saiu por site de estúdio,
   e a ficha do Timbre Games abaixo é a prova de que ainda há casa de BC nunca aberta.

**VEIA NOVA, e ela corrige uma linha escrita duas vezes neste repositório.** O `processados.csv` de
11/09 e de 14/09 diz que `animationuk.org/members` *"monta a lista por JavaScript e o curl só vê
patrocinador, então só serve com navegador"*. **Está errado por identificador, não por parede:** o
site é WordPress e o tipo de post `members` tem `rest_base` **`organisations`**, ou seja a lista sai
inteira por `curl`, sem navegador:

```
curl -sS "https://www.animationuk.org/wp-json/wp/v2/types"                  # revela rest_base
curl -sS "https://www.animationuk.org/wp-json/wp/v2/organisations?per_page=100&page=N"
```

Três páginas, **107 domínios de membro** com `membership_section` (Animation Member, Facilities
Member, Supporter) e `website_main`. **67 deles não têm uma menção em todo o repositório.** O
rendimento honesto de endereço, porém, é o mesmo da varredura de casa pequena: varri 24 dos 67 (os de
animação e VFX) em onze caminhos cada e **não saiu um endereço de pessoa** — só `hello@`, `info@`,
`office@`, `enquiries@` e, na Atelier 11, um `production@hazimation.com` que é **domínio de
terceiro**. **A veia rende NOME DE CASA e universo novo, não endereço.** A lista dos 67 fica no
relatório da rodada, e quem voltar deve ir por diretório de associação com página de detalhe (o
irlandês), não por varredura de site.

### FICHA 1 — Vanessa Robinson, Little Moon Animation (Dublin, Irlanda)

- **Email: `vanessa@littlemoonanimation.com` — PUBLICADO, confiança ALTA, e confirmado por TRÊS vias
  independentes.** Nada montado.
  1. **`mailto:` cru no diretório**, colado ao nome e ao cargo:
     `<h4>Vanessa Robinson</h4> <p class="c_role"> Creative Producer </p> <p class="email"> <a href="mailto:vanessa@littlemoonanimation.com">`
  2. **Site da própria casa**, na forma ofuscada **delimitada** (que é a única que o brief autoriza
     desofuscar): `Creative Producer Vanessa Robinson Contact email: vanessa (at) littlemoonanimation (dot) com`
  3. **A caixa está VIVA e isso veio da caixa do Vini:** a carta de 02/09 para `jobs@` recebeu
     auto-resposta enviada de **`vanessa+canned.response@littlemoonanimation.com`**. O `+tag` é da
     conta dela, ou seja o servidor confirma que a parte local `vanessa` existe e responde.
- **URLs exatas abertas nesta rodada:** `https://www.animationireland.com/studios/little-moon/` ,
  `https://www.littlemoonanimation.com/contact` , `https://www.littlemoonanimation.com/about` e
  `https://www.littlemoonanimation.com/jobs`. Nenhuma é página 404: procurei `Page not found` e
  `We couldn't find the page` no texto limpo das quatro e não aparece.
- **Por que ESSA pessoa e não outra da casa:** o `/about` publica a chefia inteira — *"Meet The
  Executive Team: Vanessa Robinson, Co-Founder & CEO; Eoghan Garvey, Co-Founder & CCO; David
  McCamley, Creative Director; Lisa O'Connor, Development Producer"* — e **ela é a única com endereço
  publicado**, além de ser cofundadora, que é a cadeira que o `BRIEF-JOE` manda procurar em casa
  pequena. **David McCamley (Creative Director) fica como SEGUNDA e última pessoa da casa**, no dia em
  que um endereço dele aparecer publicado; não montei nada para ele.
  Registro de divergência de cargo: o diretório a chama **Creative Producer** e o site da casa a
  chama **Co-Founder & CEO**. Pela regra de 00h35, **o site manda**.
- **Gancho com a frase do próprio estúdio, entre aspas:** o `/about` escreve
  *"Little Moon Animation is an award winning **CG** animation studio dedicated to creating compelling
  projects **full of character** and imaginative story"*, e o diretório marca a técnica da casa como
  **`Skills in... 3D`** — é a única casa irlandesa do diretório inteiro cuja lista de técnica é **só
  3D**, sem 2D ao lado. A produção nomeada pela própria casa é *Fia's Fairies*, 26 x 5' para o RTÉjr.
- **Fora dos EUA: SIM, Irlanda / UE.** A frase de realocação **entra**.
- **O que o Gmail devolveu no dedupe:** `littlemoonanimation OR "Little Moon" OR Robinson OR "Fia's
  Fairies"` devolveu **três threads**, e só uma é da casa: a carta de **02/09 para
  `jobs@littlemoonanimation.com`** e a auto-resposta descrita acima. **Zero carta para pessoa, zero
  resposta humana, zero recusa, zero bounce.** Pelo teto contado no `in:sent` por domínio, a casa está
  em **uma mensagem, para caixa genérica**, e Vanessa Robinson é a **primeira pessoa com nome**. Em
  `pessoas.csv` a casa não tem ninguém (o único acerto de `littlemoon` no arquivo está **dentro** do
  texto de dedupe de outra ficha de 14/09); `docs/index.html` só registra o `jobs@`.
- **RESSALVA HONESTA:** (1) o cargo é **produção e negócio** (Creative Producer / CEO), não arte — quem
  decide o look é o David McCamley, e é dele que não há endereço; (2) `/jobs` diz **"No results found"**
  e a única vaga arquivada é *Social Media Manager (Part-time)* de junho de 2025, ou seja **não há vaga
  de personagem**, é carta de porta; (3) a casa já recebeu uma candidatura espontânea em 02/09 e a
  auto-resposta diz *"We always look forward to going through applications"* — então a carta tem de
  reconhecer que ela já mandou currículo antes, em vez de se apresentar como primeiro contato;
  (4) o catálogo é **pré-escolar** (*Fia's Fairies*, aprendizado de irlandês), onde personagem é
  simples e groom e escultura pesam pouco, o oposto do que o portfólio dele mostra; (5) a chefia
  publicada tem quatro pessoas, porte que raramente abre assento sênior.

### FICHA 2 — Sean Mullen, Giant Animation (Dublin, Irlanda)

- **Email: `sean@giant.ie` — PUBLICADO, confiança ALTA.** O `mailto:` cru do diretório vem colado ao
  nome e ao cargo dele:
  `<h4>Sean Mullen</h4> <p class="c_role"> Creative Director </p> <p class="email"> <a href="mailto:sean@giant.ie">`
- **URLs exatas abertas nesta rodada:** `https://www.animationireland.com/studios/giant-animation-studios/` ,
  `https://www.giantanimation.ie/` , `https://www.giantanimation.ie/about` e
  `https://www.giantanimation.ie/careers`.
- **ARMADILHA DE DOMÍNIO, e é a da Stunlock ao contrário, dentro de casa:** o site é
  **`giantanimation.ie`** e o email é **`@giant.ie`**. A rodada de 16/09 20h35 listou
  `giantanimation.ie` entre os domínios *"abertos sem pessoa"* e **não estava errada**: o site publica
  só `hello@giant.ie`. Quem tem nome e cargo pareados é o **diretório**, e é ele que entrega os três
  endereços de pessoa da casa. Endereço montado sobre o domínio do site teria quicado.
- **Por que ESSA pessoa e não outra da casa:** o diretório publica **três** pessoas, todas com
  endereço — *Alex Sherwood, CEO / Head of Development* (`alex@`), *Ben Harper, Managing Director*
  (`ben@`) e *Sean Mullen, Creative Director* (`sean@`). Pela régua do brief, negócio e
  desenvolvimento ficam atrás do **cargo de ofício criativo**, que é o dele. **Alex Sherwood fica como
  SEGUNDA e última pessoa possível desta casa**, com endereço já provado.
- **Gancho com a frase do próprio estúdio, entre aspas:** a home diz
  *"Giant Animation is an independent **CG** animation studio dedicated to creating and producing
  world class content for TV and film"*, e o `/about` diz *"With **three full CG pipelines** and
  scalability for up to **250+ crew**, we're always ready to tackle any new challenge head on"*. O
  diretório marca a técnica como **`Skills in... 2D, 3D, Interactive, VFX`**.
- **Fora dos EUA: SIM, Irlanda / UE.** A frase de realocação **entra**.
- **O que o Gmail devolveu no dedupe:** `giant.ie OR giantanimation OR "Giant Animation" OR Mullen`
  devolveu **UMA thread com duas mensagens, as duas ENVIADAS para `hello@giant.ie`** (carta fria de
  **26/08** e follow-up de **02/09**), **sem resposta, sem bounce e sem recusa**. Pelo teto contado no
  `in:sent` por domínio, a casa está em **zero pessoa** e Sean Mullen é a **primeira**.
  `pessoas.csv`: zero pessoa da casa; `sean@giant.ie` é inédito no repositório inteiro.
- **RESSALVA HONESTA:** (1) `https://www.giantanimation.ie/careers` existe e está **vazia** — o título
  é *CURRENT JOB OPENINGS* e abaixo não há vaga nenhuma, só o endereço da casa; então isto é carta de
  porta e não resposta a anúncio; (2) é a **terceira mensagem** para a mesma casa em três semanas, e as
  duas anteriores foram ignoradas — a carta tem de dizer isso, não fingir primeiro contato;
  (3) *Creative Director* numa casa de serviço quer dizer direção de série, não necessariamente
  departamento de personagem, e o site **não nomeia** supervisor de personagem, groom nem look dev;
  (4) o catálogo é TV e conteúdo infantil por encomenda, onde o assento de escultura e groom é raro;
  (5) o "250+ crew" é **capacidade**, não tamanho atual — a casa é bem menor que isso quando não há
  série em produção.

### FICHA 3 — Joe Nickolls, Timbre Games (Vancouver, BC, Canadá) — **A PRIORIDADE 1 SAIU DO ZERO**

- **Email: `joe@timbregames.com` — PUBLICADO pela própria casa, confiança ALTA.** É o `href` do único
  botão de contato do site, embaixo do bloco *"Let's Talk Games."*. HTML cru:
  `<a href="mailto:joe@timbregames.com?" ... > Email Us! </a>`
- **URL exata aberta nesta rodada:** `https://timbregames.com` (home, 612 KB). Também abri
  `https://timbregames.com/about` e `https://timbregames.com/contact` (as duas 200) e
  `https://timbregames.com/careers`, `/jobs` e `/team` (as três **404**).
- **Pareamento, dito com honestidade:** o endereço **não** está impresso ao lado do nome dele. O que
  prova o par é que o site publica **um único endereço** e, no mesmo documento, o bloco *Leadership
  Team* nomeia quatro pessoas, e **o único Joe é ele**: *"Joe Nickolls, Co-Founder & President"*. A
  parte local `joe` é do primeiro nome do cofundador, e não há segundo Joe em nenhuma página. Isso é
  endereço **literal publicado**, não padrão de domínio montado — mas é o botão geral da casa, que por
  acaso é a caixa de uma pessoa, e isso está dito.
- **Por que ESSA pessoa e não outra da casa:** o *Leadership Team* publica quatro — *Joe Nickolls,
  Co-Founder & President*; *Geoff Coates, Co-Founder & Creative Director*; *Campbell Dixon, Technical
  Director*; *Kyle Jensen, Lead Designer*. **O alvo de ofício seria o Geoff Coates**, cuja bio diz
  *"Geoff's been making games for over 30 years in Vancouver, mostly as **Art Director at EA, Relic,
  Capcom**, and other studios, before starting Timbre with Joe in 2020"* — **e dele não há um único
  endereço publicado, então nada foi montado.** Fica como **SEGUNDA e última pessoa possível**, e a
  carta para o Joe deve pedir exatamente isso: ser apontado para o Geoff.
- **Gancho com a frase do próprio estúdio, entre aspas:** a bio dele termina em
  *"His superpower: **Knowing everyone in the games industry**"*, e a casa escreve como valor número 3
  *"**Creative Leadership** — Senior game, art, and tech direction from people who've shipped at
  scale"*. É o fecho fixo da campanha (guardar o nome, encaminhar, ou apontar um nome) escrito pela
  própria casa.
- **Fora dos EUA: SIM, Canadá (Vancouver, BC).** A frase de realocação **entra**, e esta é a **rota de
  prioridade 1 da campanha**, que fechou em zero nas duas rodadas anteriores.
- **O que o Gmail devolveu no dedupe:** `timbregames OR "Timbre Games" OR Nickolls OR Coates` devolveu
  **`{}`** — zero thread, nem enviada nem recebida. `pessoas.csv`, `enviados.csv`, `processados.csv`,
  `docs/index.html` e `alvos.csv`: **zero** ocorrência de `timbre` e de `nickolls`. **Casa inédita para
  a campanha inteira**, e é a primeira casa de BC aberta desde a Global Mechanic.
- **RESSALVA HONESTA, e ela é pesada:** (1) **o site é de uma página só e as subpáginas estão
  inacabadas** — `/contact` é o gabarito do Squarespace com *"(555) 555-5555"* e
  *"email@example.com"*, e `/about` ainda traz o texto de exemplo de uma consultoria (*"Meet Tina...
  Bloom Coaching"*). Isso indica casa em reconstrução, não operação em regime; (2) **não há `/careers`
  nem `/jobs`** (os dois 404) e nenhuma vaga publicada; (3) a casa se descreve como *"a small,
  focused team"* e a seção de jogos é *"Games We've Worked On"*, ou seja **trabalho em jogo de
  outros**, sem título próprio lançado nomeado no site; (4) **não há uma palavra sobre personagem 3D,
  escultura, groom ou look dev** — o vocabulário é prototipagem, ferramentas e iteração, e o encaixe do
  portfólio dele vem da cadeira de direção de arte do Geoff, não de pipeline provado;
  (5) o cargo do alvo é **presidente**, negócio puro, e a carta só se justifica porque o pedido é
  direção e indicação; (6) o rodapé diz **© 2025** e nada no site está datado de 2026, então
  *"continua na casa hoje"* está sustentado pelo próprio site e não por fonte com data desta semana.
  Telefone do gabarito deliberadamente não registrado (e nem é real).

### FICHA 4 — Stuart Forrest, Triggerfish Animation Studios (Galway, Irlanda; Manchester, Reino Unido) — **SEM-EMAIL, e a linha vale assim**

- **NOME E CARGO PUBLICADOS, SEM ENDEREÇO. `confianca = sem-email`, e nada foi montado.** O bloco
  `studio_contacts` do diretório publica **uma única pessoa e ela vem sem a parte de email**, ao
  contrário de todas as outras casas da mesma página. HTML cru:
  `<h4>Stuart Forrest</h4> <p class="c_role"> CEO </p> </div>` — não existe `<p class="email">` no
  cartão dele. O único endereço da página é `hello@triggerfish.com`, caixa genérica.
- **URL exata aberta nesta rodada:** `https://www.animationireland.com/studios/triggerfish/`.
- **PAREDE MEDIDA, e ela explica por que o endereço não veio:** `https://www.triggerfish.com/` ,
  `/contact` , `/about` , `/team` e `/careers` devolvem todas **HTTP 202 com 169 a 176 bytes**, e o
  corpo é um redirecionamento para captcha:
  `<meta http-equiv="refresh" content="0;/.well-known/sgcaptcha/?r=%2F&y=ipr:...">`. É **captcha de
  borda**, e burlar captcha é proibido. A casa fica **não conferida pelo site**, não "sem endereço".
- **Por que ESSA pessoa:** é a **única** pessoa que a casa publica no diretório, e é o CEO. Não há
  segunda pessoa para escolher.
- **Por que a linha vale mesmo sem email, e é o achado de escopo da rodada:** o diretório coloca a
  Triggerfish **dentro da Irlanda** e escreve o endereço postal da casa —
  *"F2 CREW Building, Cluain Mhuire Wellpark Road Galway H91 8K85 IRELAND"* — e o texto dela diz
  *"is a world-renowned animation company with studios in **Cape Town, Manchester** and **Galway**"*.
  Ou seja: **duas das três casas estão no escopo da campanha** (Irlanda e Reino Unido), e a Cidade do
  Cabo, que está fora, é só a matriz. E o catálogo é **CG de longa e série**, escrito por eles:
  *"Adventures in Zambezia"*, *"Khumba"*, *"Seal Team (Netflix)"*, *"Kiya and the Kimoja Heroes
  (Disney Junior, eOne)"* e *"the Disney+ anthology Kizazi Moto: Generation Fire"*, mais os especiais
  *Stick Man*, *The Snail and the Whale*, *Revolting Rhymes*, *The Highway Rat* e *Zog* para a Magic
  Light Pictures e a BBC. É uma das casas de personagem 3D mais fortes que a campanha tocou fora dos
  Estados Unidos, e ela é **inédita**.
- **Fora dos EUA: SIM** (Irlanda e Reino Unido; a matriz é África do Sul, fora do escopo).
- **O que o Gmail devolveu no dedupe:** `triggerfish OR "Stuart Forrest" OR Khumba OR Zambezia`
  devolveu **UMA thread, e ela não é da casa**: é a carta de 11/09 para **Wayne Thornley**, da
  Revelator (Dublin), cuja própria carta cita *Adventures in Zambezia* e *Seal Team* — ele é **ex-
  Triggerfish**, o que é dado útil e não duplicata. **Zero thread da Triggerfish**, zero em
  `pessoas.csv`, `enviados.csv` e `docs/index.html`; no `processados.csv` a única ocorrência é a lista
  dos 14 domínios do Jhon A de hoje.
- **RESSALVA HONESTA:** (1) **sem endereço, não há carta possível** — e é proibido montar
  `stuart@triggerfish.com` ou `sforrest@`, porque nenhum endereço daquele domínio foi visto publicado;
  (2) o cargo é **CEO de grupo com três países**, o leitor menos provável de responder email frio;
  (3) o email da casa (`hello@`) é caixa genérica e gastar a única porta dela num `hello@` seria
  exatamente o que o brief proíbe em casa grande; (4) a contratação dessa casa provavelmente se faz
  pela Cidade do Cabo, que está **fora do escopo**, e nada no diretório diz que Galway ou Manchester
  contratam artista; (5) o site está atrás de captcha, então **não confirmei por segunda fonte** que
  ele continua CEO — a foto do diretório é de 2020.
- **O que a próxima rodada deve tentar nesta casa, e eu não tentei:** o site abre em navegador de
  tela (o captcha é de borda, não bloqueio permanente), e a página de careers deles costuma listar
  vaga por estúdio. Vale também procurar o endereço publicado em **press release** e em **página de
  palestrante de festival** (Annecy e Cartoon Forum), porque um CEO que fala em painel costuma ter
  contato de imprensa nomeado.

### O DEDUPE MATOU DUAS FICHAS QUE EU JÁ TINHA PRONTAS, E AS DUAS LIÇÕES SÃO DIFERENTES

**1. Boulder Media morreu na CAIXA, e não na planilha.** Eu tinha `Paul.O'Flanagan@bouldermedia.tv`
pronto, **publicado em texto visível E no `href`** do diretório (o apóstrofo do sobrenome está dentro
do `mailto:` e não corta o link, ao contrário do que a nota de 14/09 registrou), com o cargo
*Creative Director* colado, numa casa cuja técnica declarada é **2D, 3D e VFX**. **A carta não sai:**
`mcp__Gmail__search_threads` por `bouldermedia OR "Boulder Media" OR Comerford OR Tyrrell OR
"O'Flanagan"` devolveu uma thread com **três mensagens**, e a do meio é **resposta humana da própria
Gillian Comerford, de 15/09**: *"We currently are not hiring for 3D character work and have no 3D on
our slate for the rest of the year, please do stay tuned to our careers page"*. Pessoa que respondeu
é do Comunicador, e a casa disse por escrito que **não tem 3D na grade até o fim do ano**. Boulder
sai da fila do Joe. Fica registrado, para quem voltar: **o endereço do Paul O'Flanagan existe e está
publicado**, e a correção da nota de 14/09 vale por si.

**2. Cantilever Media eu quase reabri, e a ficha antiga estava certa.** O diretório publica
`andrew@cantilevermedia.ie` e `andrea@cantilevermedia.ie` em `mailto:` cru, e eu tinha isso como
"correção da linha `sem-email` de 14/09". **Fui ler a linha antiga inteira antes de escrever, e ela já
tinha medido o que eu não tinha:** o domínio **`cantilevermedia.ie` é NXDOMAIN** nos quatro tipos de
registro, com autoridade do registro `.ie`, e o controle (`cantilever.media`, o domínio do site)
resolve normal. Endereço publicado em domínio que não existe **não é endereço**. A linha continua
`sem-email` e **não a toquei**. A lição de método: **antes de "corrigir" ficha antiga, leia a ficha
antiga até o fim** — a minha correção seria um retrocesso. (O site `cantilever.media` também não
ajuda: devolve 202 KB de casca com **174 caracteres** de texto e zero `mailto:`.)

### CASAS ABERTAS NESTA RODADA SEM ENDEREÇO DE PESSOA APROVEITÁVEL (para ninguém repetir)

- **Irlanda e Irlanda do Norte, pelas 47 páginas de detalhe do diretório + 8 sites:** `curiosity-studio`
  (só `hello@`), `distillery-films` (Jonathan Clarke, Producer, com **`info@`** no lugar do endereço
  dele), `dreamlogicstudios` (2D+3D, três nomes — Brian Willis, Kealan O'Rourke, Stephen Smith — e
  **zero** endereço; `dreamlogic.ie` só publica `info@`), `enter-yes` (Vicki Rock e Kris Kelly, sem
  endereço; site só `studio@`), `maverick-films` (Zoe Doyle e Deirdre Lyons Doyle, sem endereço),
  `pioneertown-productions` (Jonathan Loughran e **Will Sliney**, sem endereço, e o site nem responde),
  `score-draw-media` (**sete** nomes com cargo, inclusive *Hannah Dorman, Concept and Background
  Artist*, e **nenhum** endereço), `algorithm` (Nick Linders MD e **Cormac Murray, Head of Animation**,
  só `info@algorithm.ie`), `ink-and-light` (2D+3D+stop motion, Tamsin Lyons e Leevi Lemmetty, sem
  endereço — já é linha `sem-email` de 14/09), `jam-media` (já é `sem-email` de 14/09),
  `lighthouse-studios` (**nenhuma** pessoa publicada).
- **Casas irlandesas com endereço de pessoa que eu NÃO usei, e o motivo de cada uma:**
  **Igloo Animations** (`paul@iglooanimations.com`, Paul Dowling, Producer) — a casa declara
  *"2D | Mixed Media | Puppets | Stop Motion | VFX"*, **zero 3D**, é a armadilha da Head Gear;
  **Studio Meala** (`stephen@studiomeala.com`, Stephan Fagan, MD) — o site escreve
  *"specialising in high-end **2D** animation"* e a lista de serviços dela vai de storyboard a
  *2D Animation*, sem 3D; **Paper Panther** (`carol@paperpanther.ie`, Carol Freeman, Founder &
  Director) — *"an award-winning animation studio specialising in **stopmotion**"*;
  **Studio 9** (`joe (at) studio9.ie` e `john (at) studio9.ie`, os dois cofundadores, em forma
  delimitada no próprio site) — a casa é de *"short animations that Engage, Explain and Excite"*,
  vídeo explicativo, sem prova de 3D nem de personagem; **Lazy Sunday** (`artem@lazysunday.ie`,
  Artem Vasiliev, CEO) — é *"a new creative label"* de 2024 que desenvolve e produz, animação **e**
  live-action, sem pipeline próprio; **Whackala** (2D declarado, e os cargos publicados são
  *Numero Uno*, *Big Cheese* e *The Gaffer*, sem endereço de pessoa); **Dúlamán Studios** (casa nova,
  publica **Magenta Muraca, Art Director**, mas **nenhum** endereço, e a própria casa escreve
  *"built with love for **2D** animation"*); **Trinity Motion Pictures** (`conor@trinitypictures.ie`,
  outro domínio que não o do site — armadilha registrada — mas Conor Harrington é
  *"producer and financier"* e o `/about` ainda tem o gabarito do Wix vivo na página, com
  *"Name | Information on person | info@mysite.com"*); **Piranha Bar**, **Atomic Cartoons** e **Zoic**:
  **teto de duas pessoas já fechado** (a Piranha tem Richard Chaney 03/09 e Gavin Kelly 06/09, e o
  texto dela é o melhor gancho de personagem 3D da Irlanda, o que dói).
- **Reino Unido, os 24 domínios novos vindos do `wp-json` da Animation UK** (onze caminhos cada,
  `mailto:` + `data-cfemail` + formas delimitadas): `bomperstudio.com`, `rustymonkey.com`,
  `lightrunnerstudio.com`, `madmicrobe.com`, `kinobino.com`, `lightboat.media`, `8lions.com`,
  `animation-associates.co.uk`, `viridianfx.co.uk`, `dupevfx.com` (só `HELLO@`),
  `magiclightpictures.com` (só `office@`, **e é a casa do Stick Man e do Zog**),
  `rumpusanimation.com` (`hello@`, `jobs@`), `brighton-zoo.co.uk`, `lilcritterworkshop.tv`,
  `noodleandcaboodle.tv`, `sparklegoose.com` (`honk@`), `tentaclemedia.co.uk`, `walkinghouse.uk`,
  `yamination.com`, `midasvfx.com`, `primaryvfx.com`, `tpovfx.com`, `magicdustvfx.com`,
  `atelier11.co.uk` (o endereço que parece de pessoa é `production@hazimation.com`, **domínio de
  terceiro**). **Zero endereço de pessoa em 24 casas.**
- **Vancouver / BC e Canadá, 20 domínios:** `atomiccartoons.com` (o único endereço de pessoa é
  `Julia@finchmedia.net`, **agência de imprensa de fora**, e a casa já está no teto),
  `mainframe.ca` (só `info@`), `bronstudios.com`, `braceyourselfgames.com`, `phoenixlabs.com`,
  `thecoalitionstudio.com`, `basaltvfx.com`, `sealevelstudios.com`, `wizardstudios.ca`,
  `roadhouseinteractive.com`, `kabam.com`, `iugo.ca`, `titmouse.net` (só `fan@`, `festivals@`,
  `tours@`), `distilleryvfx.com` (só `info@` e `jobs@`), `klei.com` (as duas caixas de suporte já
  conhecidas), `relic.com` (só `info@` e `media@`), `megalomedia.com` (só caixas de **casting** de
  reality), `digibc.org` (**403**), `zoicstudios.com` (rico em endereço de pessoa e **no teto de
  quatro**).

### AS PAREDES DESTA RODADA, medidas

| Fonte | O que devolveu | Leitura |
|---|---|---|
| `80.lv/?s=SkyBox+Labs` | **200 com 173 KB e zero link de artigo** | a busca é client-side; a veia de 80.lv **não se lê por `curl`** pela página de busca |
| `animationmagazine.net/?s=...` | **403, 919 bytes** | fechada a este túnel |
| `www.triggerfish.com` e quatro caminhos | **202 com 169-176 bytes**, refresh para `/.well-known/sgcaptcha/` | captcha de borda; proibido burlar, casa **não conferida** |
| `digibc.org/members` e `/member-directory` | **403, 103 bytes** | a associação de tecnologia e criativos da BC está fechada aqui |
| `sparkcgsociety.org` | **502 no CONNECT** | |
| `sparkanimation.org` | **certificado expirado** | não é "site morto", é certificado |
| `mifa-annecy.com` | **502 no CONNECT** | o mercado do Annecy não abre; `annecyfestival.com` abre (200, 88 KB) |
| `cartoon-media.eu` | 200, mas **não há diretório de membros** | confirma a nota de 11/09 |
| `animationuk.org/wp-json/wp/v2/members` | **404 `rest_no_route`** | o caminho certo é **`/organisations`** |

### PLACAR HONESTO DA RODADA

**Quatro pessoas novas**, no piso da faixa de 4 a 8: **três com endereço PUBLICADO e confiança ALTA**
(Little Moon, Giant Animation, Timbre Games) e **uma `sem-email`** (Triggerfish).
**Nenhum endereço montado por padrão de domínio. Nenhum inventado.**
Por região: **Irlanda 2, Canadá/Vancouver-BC 1, Irlanda+Reino Unido 1 (`sem-email`)**.
**Vancouver e BC saiu do zero** depois de duas rodadas em branco, e saiu por **site de estúdio de
casa nunca aberta**, não por imprensa. **Holanda: zero** (não foi alvo desta rodada). **Nórdicos:
zero** (não foi alvo).
Duas fichas prontas foram **jogadas fora pelo dedupe** (Boulder Media, por resposta humana com veto
escrito de 3D; Cantilever Media, porque a ficha antiga já provava NXDOMAIN) e **oito endereços
publicados foram descartados por técnica 2D/stop-motion ou por não serem estúdio** (Igloo, Studio
Meala, Paper Panther, Studio 9, Lazy Sunday, Trinity, e as duas caixas de terceiro da Atelier 11 e da
Atomic).
**Veia nova documentada:** `animationuk.org/wp-json/wp/v2/organisations` (107 membros, 67 inéditos no
repositório) — **rende universo de casa, não endereço**, medido em 24 domínios com zero pessoa.

> **Maestro, 17/09 05h00 UTC:** lote de três cartas escrito e gravado em rascunho (`confere-carta.py` limpo, pior par 38%): Vanessa Robinson / Little Moon `r8699692104500084818` (a carta diz que o CV já foi ao `jobs@` em 02/09 e que não é primeiro contato); Sean Mullen / Giant Animation `r6091812572875862381` (a carta diz que o `hello@` foi escrito duas vezes sem resposta e que esta é a última tentativa); Joe Nickolls / Timbre Games `r-4328626659316485405` (Vancouver, pede encaminhamento em vez de vaga). Stuart Forrest (Triggerfish) fica `sem-email`. Saem pelo Apps Script do Vini.
