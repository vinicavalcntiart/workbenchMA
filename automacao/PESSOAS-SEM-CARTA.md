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
