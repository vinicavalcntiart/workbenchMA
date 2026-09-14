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
