# Reconciliação Teamtailor — 11/09

Agente de reconciliação de registro. **Nada foi enviado, nenhum rascunho criado, nenhum navegador aberto, e o `enviados.csv` NÃO foi editado.** Só leitura e conferência.

## Método e números medidos

| Medida | Valor |
|---|---|
| Threads retornadas por `from:teamtailor-mail.com` | **133** (3 páginas: 50 + 50 + 33; paginado até `nextPageToken` sumir) |
| `resultCountEstimate` que o Gmail devolveu na 1ª página | 201 — **é estimativa, e estava errada**; a última página trouxe 33 e encerrou |
| Slugs únicos com recibo | **66** |
| Slugs da lista de 89 que na verdade já foram enviados (falsos livres) | **26** |
| Slugs com recibo e sem nenhuma linha no `enviados.csv` | **10** |
| Slugs dos 89 que sobraram sem recibo | 63 → **15 estúdios confirmados**, 3 duvidosos, 4 slugs inválidos, 41 falsos amigos |

**Ressalva honesta sobre a premissa.** A regra do briefing ("todo envio pelo Teamtailor gera recibo") vale na direção que interessa, mas a volta não é limpa: um recibo de `no-reply@<slug>.teamtailor-mail.com` é confirmação automática de candidatura pelo portal; um recibo de **pessoa nomeada** (`fulano@<slug>.teamtailor-mail.com`) pode ser um recrutador **respondendo a uma carta fria**, não prova de envio por portal. Marquei essa diferença onde ela muda a conclusão. Em todos os 10 buracos ela não muda o veredito — não existe linha nenhuma para aquelas casas, por portal ou por email, então o registro está furado de qualquer jeito.

---

## 1. Razão de recibos — 66 slugs

`no-reply` na coluna de remetente = havia confirmação automática de portal na caixa. Data = a **mais antiga** vista para aquele slug (UTC).

| # | slug | data mais antiga | remetente exemplo |
|---|---|---|---|
| 1 | 10chambers | 2026-09-06 | no-reply@10chambers.teamtailor-mail.com |
| 2 | airshipinteractive | 2026-09-06 | no-reply@airshipinteractive.teamtailor-mail.com |
| 3 | ankama | 2026-09-07 | merabai.yasmine@ankama.teamtailor-mail.com |
| 4 | arrowheadgs | 2026-09-07 | no-reply@arrowheadgs.teamtailor-mail.com |
| 5 | awaceb | 2026-09-11 | philippe.crifo@awaceb.teamtailor-mail.com |
| 6 | axolotgamesab | 2026-09-07 | info@axolotgamesab.teamtailor-mail.com |
| 7 | beffio | 2026-09-06 | tom.lassota@beffio.teamtailor-mail.com |
| 8 | beyondframesentertainment | 2026-09-06 | ace-st-germain@beyondframesentertainment.teamtailor-mail.com |
| 9 | blackkitestudios | 2026-08-30 | angus.edhouse@blackkitestudios.teamtailor-mail.com |
| 10 | bulkheadinteractive | 2026-09-07 | no-reply@bulkheadinteractive.teamtailor-mail.com |
| 11 | cigames | 2026-09-06 | lucie.piskova@cigames.teamtailor-mail.com |
| 12 | coffeestainstudios | 2026-09-06 | no-reply@coffeestainstudios.teamtailor-mail.com |
| 13 | creepyjar | 2026-09-06 | alicja.lewandowska@creepyjar.teamtailor-mail.com |
| 14 | embarkstudios | 2026-09-07 | terri-kim-bell@embarkstudios.teamtailor-mail.com |
| 15 | envarstudio | 2026-09-07 | soledad.trejo@envarstudio.teamtailor-mail.com |
| 16 | erepublik | 2026-09-11 | template-manager-can-be-deleted@erepublik.teamtailor-mail.com |
| 17 | facepunch | 2026-09-11 | facepunch-hiring-team@facepunch.teamtailor-mail.com |
| 18 | fatshark | 2026-09-06 | no-reply@fatshark.teamtailor-mail.com |
| 19 | foolstheory | 2026-09-07 | lukasz.plandowski@foolstheory.teamtailor-mail.com |
| 20 | framebreak | 2026-09-06 | frame-break-team@framebreak.teamtailor-mail.com |
| 21 | funcom | 2026-09-06 | no-reply@funcom.teamtailor-mail.com |
| 22 | fundaygames | 2026-09-07 | sabine.wilki@fundaygames.teamtailor-mail.com |
| 23 | gameboost | 2026-09-09 | jenny.osterlund@gameboost.teamtailor-mail.com |
| 24 | ghostship | 2026-09-07 | no-reply@ghostship.teamtailor-mail.com |
| 25 | gigglebug | 2026-08-27 | sanni.vainio@gigglebug.teamtailor-mail.com |
| 26 | goals | 2026-09-11 | peter.kjellberg@goals.teamtailor-mail.com |
| 27 | goodbyekansas | 2026-09-02 | no-reply@goodbyekansas.teamtailor-mail.com |
| 28 | hampastudio | 2026-09-06 | alessandro.sarno@hampastudio.teamtailor-mail.com |
| 29 | ilogos | 2026-09-06 | no-reply@ilogos.teamtailor-mail.com |
| 30 | ilpvfx | 2026-09-02 | eleonora.matrella@ilpvfx.teamtailor-mail.com |
| 31 | invisiblewalls-demo | 2026-09-06 | no-reply@invisiblewalls-demo.teamtailor-mail.com |
| 32 | ioi | 2026-09-06 | no-reply@ioi.teamtailor-mail.com |
| 33 | ironbirdcreationsspolkaakcyjna | 2026-09-07 | aleksandra@ironbirdcreationsspolkaakcyjna.teamtailor-mail.com |
| 34 | keengamesdemo | 2026-09-06 | no-reply@keengamesdemo.teamtailor-mail.com |
| 35 | kindabrave | 2026-09-11 | therese.nas@kindabrave.teamtailor-mail.com |
| 36 | lastarrowgames | 2026-09-11 | becki.leggatt@lastarrowgames.teamtailor-mail.com |
| 37 | lightheartentertainment | 2026-09-11 | janne.kaitila@lightheartentertainment.teamtailor-mail.com |
| 38 | madbox | 2026-09-11 | mariana.kita@madbox.teamtailor-mail.com |
| 39 | mindark | 2026-09-11 | madeleine@mindark.teamtailor-mail.com |
| 40 | moodvisuals | 2026-09-07 | jesper.andersen@moodvisuals.teamtailor-mail.com |
| 41 | neongiant | 2026-09-11 | claes-af-buren@neongiant.teamtailor-mail.com |
| 42 | paradox-interactive | 2026-09-06 | karl.lakner@paradox-interactive.teamtailor-mail.com |
| 43 | pfx | 2026-09-06 | weronika.kozlowska@pfx.teamtailor-mail.com |
| 44 | pixiongames | 2026-09-11 | tamara.slavskaya@pixiongames.teamtailor-mail.com |
| 45 | playagames | 2026-09-06 | no-reply@playagames.teamtailor-mail.com |
| 46 | playerunknownproductions | 2026-09-07 | no-reply@playerunknownproductions.teamtailor-mail.com |
| 47 | radicalforge | 2026-09-02 | no-reply@radicalforge.teamtailor-mail.com |
| 48 | rawpowergames | 2026-09-06 | no-reply@rawpowergames.teamtailor-mail.com |
| 49 | realtime | 2026-08-27 | ethan.clark@realtime.teamtailor-mail.com |
| 50 | resolutiongames | 2026-09-07 | no-reply@resolutiongames.teamtailor-mail.com |
| 51 | sandboxinteractive | 2026-09-08 | annie.ngo@sandboxinteractive.teamtailor-mail.com |
| 52 | sharkmob | 2026-09-07 | no-reply@sharkmob.teamtailor-mail.com |
| 53 | sloclap | 2026-09-07 | no-reply@sloclap.teamtailor-mail.com |
| 54 | snowprintstudios | 2026-09-07 | no-reply@snowprintstudios.teamtailor-mail.com |
| 55 | starbreeze | 2026-09-07 | no-reply@starbreeze.teamtailor-mail.com |
| 56 | starstable | 2026-09-06 | linnea.tegelberg@starstable.teamtailor-mail.com |
| 57 | stunlocksstudios | 2026-09-06 | helena.toresson@stunlocksstudios.teamtailor-mail.com |
| 58 | sybo | 2026-09-07 | no-reply@sybo.teamtailor-mail.com |
| 59 | tacticaladventures | 2026-09-06 | guidi-rontani-armand@tacticaladventures.teamtailor-mail.com |
| 60 | thegang | 2026-09-11 | sven-robin.skog@thegang.teamtailor-mail.com |
| 61 | triband | 2026-09-06 | vera.schwarz@triband.teamtailor-mail.com |
| 62 | twinharbour | 2026-09-06 | margarita.kremholler@twinharbour.teamtailor-mail.com |
| 63 | untoldstdfg1324556 | **2026-07-11** | recruitment@untoldstdfg1324556.teamtailor-mail.com |
| 64 | vinefx | 2026-09-07 | leah.chapman@vinefx.teamtailor-mail.com |
| 65 | vividgamessa | 2026-09-11 | sylwia.polaczyk@vividgamessa.teamtailor-mail.com |
| 66 | wetaworkshop | 2026-09-02 | no-reply@wetaworkshop.teamtailor-mail.com |

---

## 2. Falsos livres — 26 dos 89 JÁ FORAM ENVIADOS

**Esta é a seção que importa.** Nenhum destes pode entrar em fila de envio. A lista de 89 estava com **29% de contaminação**.

### 2a. Match exato do slug (22) — zero ambiguidade

| slug na lista dos 89 | data do recibo | remetente |
|---|---|---|
| awaceb | 2026-09-11 | philippe.crifo@awaceb… |
| axolotgamesab | 2026-09-07 | info@axolotgamesab… |
| beyondframesentertainment | 2026-09-06 | ace-st-germain@beyondframesentertainment… |
| blackkitestudios | 2026-08-30 | angus.edhouse@blackkitestudios… |
| bulkheadinteractive | 2026-09-07 | no-reply@bulkheadinteractive… |
| coffeestainstudios | 2026-09-06 | no-reply@coffeestainstudios… |
| embarkstudios | 2026-09-07 | terri-kim-bell@embarkstudios… |
| envarstudio | 2026-09-07 | soledad.trejo@envarstudio… |
| fatshark | 2026-09-06 | no-reply@fatshark… |
| foolstheory | 2026-09-07 | lukasz.plandowski@foolstheory… |
| fundaygames | 2026-09-07 | sabine.wilki@fundaygames… |
| gigglebug | 2026-08-27 | sanni.vainio@gigglebug… |
| ilpvfx | 2026-09-02 | eleonora.matrella@ilpvfx… |
| playagames | 2026-09-06 | no-reply@playagames… |
| radicalforge | 2026-09-02 | no-reply@radicalforge… |
| **snowprintstudios** | **2026-09-07** | no-reply@snowprintstudios… (o caso que você já tinha achado) |
| **stunlocksstudios** | **2026-09-06** | helena.toresson@stunlocksstudios… (já corrigido por você, linha 519) |
| tacticaladventures | 2026-09-06 | guidi-rontani-armand@tacticaladventures… |
| twinharbour | 2026-09-06 | margarita.kremholler@twinharbour… |
| untoldstdfg1324556 | 2026-07-11 | recruitment@untoldstdfg1324556… |
| vinefx | 2026-09-07 | leah.chapman@vinefx… |
| **paradoxinteractive** | 2026-09-06 | karl.lakner@**paradox-interactive**… — mesmo slug, só o hífen difere |

### 2b. Match por variação de grafia (4) — confirmados, não são duvidosos

| slug na lista dos 89 | slug do recibo | data | por que é o mesmo |
|---|---|---|---|
| envar | envarstudio | 2026-09-07 | prefixo; e **`envar` também não tem linha nenhuma no CSV** — não existem duas casas |
| ghostshipgames | ghostship | 2026-09-07 | Ghost Ship Games; o CSV já tem a linha "Ghost Ship Games" de 07/09 |
| goodbyekansasstudios | goodbyekansas | 2026-09-02 | Goodbye Kansas Studios; CSV tem "Goodbye Kansas Studios" de 26/08 |
| sybogames | sybo | 2026-09-07 | SYBO; CSV tem a linha "SYBO" de 07/09 (Copenhague e Londres) |

---

## 3. Buracos no `enviados.csv` — 10 slugs com recibo e ZERO linha

Conferi os **66** slugs com recibo contra o CSV inteiro, com grep case-insensitive por prefixos progressivos do slug. **55 têm linha, 10 não têm, 1 falso alarme corrigido** (veja a nota abaixo).

Linhas prontas para colar, no formato de referência da **linha 519** (`data,estudio,email,assunto,status` com status `portal-enviado`), que é a forma que você mesmo usou ao reconstruir a Stunlock. Data = a do recibo mais antigo.

```
2026-08-27,Gigglebug Entertainment,-,"Teamtailor gigglebug - ENVIO EXISTE, registro faltava: recibo de Sanni Vainio em 27/08 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-08-30,Black Kite Studios,-,"Teamtailor blackkitestudios - ENVIO EXISTE, registro faltava: recibo de Angus Edhouse em 30/08 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-02,ILP VFX,-,"Teamtailor ilpvfx - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 06/09 e recibo de Eleonora Matrella em 02/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-02,Radical Forge,-,"Teamtailor radicalforge - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 02/09 e recibo de Alex Whittle em 02/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-06,Coffee Stain Studios,-,"Teamtailor coffeestainstudios - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 06/09 e recibo de Maria Sjoman em 06/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-06,Fatshark,-,"Teamtailor fatshark - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 06/09 e recibo de Rachel Raschke em 06/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-06,Frame Break,-,"Teamtailor framebreak - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 07/09 e recibo do Frame Break Team em 06/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-06,Raw Power Games,-,"Teamtailor rawpowergames - ENVIO EXISTE, registro faltava: recibo automatico no-reply em 06/09 e recibo de Craig McHugh em 06/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-07,Envar Studio,-,"Teamtailor envarstudio - ENVIO EXISTE, registro faltava: recibo de Soledad Trejo em 07/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
2026-09-07,Vine FX,-,"Teamtailor vinefx - ENVIO EXISTE, registro faltava: recibo de Leah Chapman em 07/09 (linha reconstruida em 11/09 por reconciliacao de caixa de entrada)",portal-enviado
```

### Grau de certeza, por buraco

**Seis com recibo automático `no-reply@` — candidatura por portal é fato:** `coffeestainstudios`, `fatshark`, `framebreak`, `ilpvfx`, `radicalforge`, `rawpowergames`.

**Quatro só com remetente nomeado — o envio existe, mas o canal é incerto:** `blackkitestudios`, `envarstudio`, `gigglebug`, `vinefx`. Aqui o recibo pode ser um recrutador respondendo a carta fria em vez de confirmação de portal. **Mesmo assim são buracos**: o grep não acha *nenhuma* linha para essas quatro casas, nem de portal nem de email. Se você souber que foi carta fria, troque o status para `enviado` e ajuste o assunto — a data e a existência do contato estão provadas de qualquer forma.

### Falso alarme que eu corrigi antes de reportar

Meu primeiro passo de grep varria prefixos de no mínimo 5 caracteres, o que pulou silenciosamente os três slugs curtos. Refiz na mão:

- **`ioi`** → tem a linha 608 (`2026-09-06,Ioi,ioi@ioi.dk,…,enviado`). **Ressalva:** essa linha é de **email**, e existe recibo `no-reply@ioi` de 06/09, que é portal. Pode faltar uma linha de *portal* para a IOI, com a de email ficando de pé. Não incluí nas dez porque a casa está registrada; vale sua decisão.
- **`pfx`** → tem a linha 130 (`2026-08-28,PFX,info@pfx.tv`). Recibo só de pessoa nomeada. Registrado.
- **`sybo`** → tem a linha 701 (`2026-09-07,SYBO,-,"Connect (banco de talentos) Copenhague e Londres…`). Registrado.

O mesmo varredor também gerou três casamentos errados que eu conferi e descartei: `black` batendo em "Black Forest Games", `frame` batendo em "Keyframe Digital Productions", e `funcom` batendo dentro do email `hr@about-fun.com`. A Funcom tem linha própria de verdade (595).

### Nota sobre o formato do arquivo

O `enviados.csv` tem **duas formas convivendo**: as linhas recentes (as ~15 últimas, e a maioria de 11/09) têm **8 colunas** (`data,estudio,assunto,local,canal,url,status,notas`), enquanto a linha 519 e as 48 linhas com status `portal-enviado` usam **5 colunas**. Escrevi as dez acima em 5 colunas para casar com a linha 519, que é a sua própria correção de hoje e o precedente mais próximo. Se você preferir a forma de 8 colunas, elas precisam ser reescritas — não fiz a conversão porque isso é decisão sua, não minha.

---

## 4. Fila limpa de verdade

Dos 89: 26 são falsos livres (seção 2) → sobram 63. Verifiquei a identidade de cada um dos 63 com uma consulta (`https://<slug>.teamtailor.com`, seguindo o redirect que o próprio Teamtailor devolve; WebSearch só quando o domínio caiu).

### 4a. FILA LIMPA — 15 slugs, estúdio de jogos/animação/VFX confirmado

| slug | o que é |
|---|---|
| capsulestudio | Capsule Studio — animação digital ("we create stories within digital worlds") |
| captureage | CaptureAge — dev de jogos, parceira da World's Edge na franquia Age of Empires |
| goodgamestudios | Goodgame Studios — dev de jogos free-to-play (web e mobile), Hamburgo |
| houseofhow | House of How Games — estúdio de jogos, Bothell (EUA) + Boden (Suécia) |
| keplerinteractive | Kepler Interactive — publisher de jogos, foco declarado em direção de arte |
| liquidswords | Liquid Swords — estúdio de jogos, Estocolmo, action-RPG open world (fundado por Christofer Sundberg) |
| newmoonproduction | New Moon Production — estúdio de jogos do grupo Stillfront |
| ofmstudios | OFM Studios — estúdio de jogos do grupo Stillfront |
| opusmajor | Opus Major — estúdio de jogos ("shaping an entertainment studio") |
| princessbento | Princess Bento — **estúdio de animação 2D de ponta**, Melbourne (Princess Pictures + Bento Box) |
| rawfury | Raw Fury — publisher de jogos independente |
| stillfrontgroup | Stillfront Group — grupo de jogos, 1.400+ pessoas |
| swiftgames | Swift Games — dev de jogos |
| tapnation | TapNation — publisher francês de jogos mobile |
| territorystudio | Territory Studio — **motion design e VFX** para cinema, jogos e marcas |

**Alerta de sobreposição, antes de você enfileirar:** `stillfrontgroup`, `newmoonproduction`, `ofmstudios` e `twinharbour` (esta já enviada em 06/09) são todas do **mesmo grupo Stillfront**. Quatro candidaturas ao mesmo guarda-chuva em poucos dias podem ler como disparo automático. Sugiro espaçar ou escolher.

### 4b. DUVIDOSOS — 3, não decidi sozinho

| slug | o que achei | por que está em dúvida |
|---|---|---|
| aonic | Aonic — tech/gaming sueca, plataformas de engajamento para jogos mobile e consumer insights | É do setor de jogos mas **não é estúdio de produção**; não deve ter cadeira de artista de personagem. Provavelmente descarte, mas é você quem decide |
| grace | Grace (gracestudio.se) — estúdio criativo digital sueco, comerciais e brand content | Faz produção visual, mas não se descreve como jogos, animação ou VFX. Fronteira |
| lingokids | Lingokids — plataforma de entretenimento infantil / edtech | Publica conteúdo animado, mas o site não declara produção de animação in-house. Fronteira |

### 4c. SLUGS INVÁLIDOS — 4, o endereço Teamtailor não existe (HTTP 404)

| slug | o que é | recomendação |
|---|---|---|
| fundagames | 404 | **Quase certo que é erro de digitação de `fundaygames`** — que tem recibo de 07/09 e linha no CSV. Tratar como já enviado, não como fila |
| paradoxplaza | 404 | Paradox usa `paradox-interactive`, **já enviada em 06/09**. Tratar como já enviado |
| gamecan | 404 no Teamtailor | Gamecan **é** estúdio de jogos de verdade (Pärnu, Estônia, Unreal), mas a porta deles é `gamecan.eu/career`, não Teamtailor. Vale a pena, por outro canal |
| minogames | 404 no Teamtailor | Mino Games **é** estúdio de jogos mobile de verdade (Montreal), mas a porta é `minogames.com/careers`. Vale a pena, por outro canal |

### 4d. FALSOS AMIGOS — 41 não-estúdios, descartar

Cada um verificado individualmente. Os que mais enganam vêm primeiro.

| slug | o que realmente é |
|---|---|
| **axis** | **Consultoria e staffing de TI na Noruega** (axissolutions.no). **NÃO é a Axis Studios de animação** — a armadilha é forte |
| **rhino** | Redireciona para `blue.tuolavoro.com`, **agência de trabalho temporário italiana**. **NÃO é a Rhino Entertainment** |
| **chopchop** | **Rede sueca de fast-food asiático** (work.chopchop.se) — o que você já tinha achado, confirmado |
| **firefly** | **Proteção industrial contra incêndio** há 50+ anos. Não é Firefly nenhuma de mídia |
| **starship** | **Starship Technologies**, robôs autônomos de entrega |
| **stim** | Sociedade sueca de **direitos autorais de música**, sem fins lucrativos |
| **seven** | Baar — **serviços domésticos** e gestão de despesas do lar |
| **sweet** | "Smart" — **agência de emprego** (reposição de gôndola, balcão de café, catering) |
| **revolution** | REV — **agência de emprego italiana** (armazém, telefonia, aluguel de veículos) |
| above | Above Agency — agência escandinava de inovação (estratégia, design, tecnologia) |
| avantis | Avantis Group — engenharia marítima e industrial |
| bica | Bica — TI, auditoria e dados |
| butter | All Gravy — HR-tech para trabalhadores de turno |
| chief | Chief — consultoria de tecnologia e liderança |
| clickoutmedia | ClickOut Media — marketing multicanal, SEO e mídia paga |
| curio | Curio Group — tecnologia educacional |
| dare | Dare — **trading de energia** e commodities |
| delve | Delve Interim & Search — recrutamento executivo sueco |
| doktor | Doktor.se — saúde, telemedicina e clínicas |
| eclipse | Eclipse Sverige AB — recrutamento em finanças e contabilidade |
| fortis | Fortis (Malta) — outsourcing de telecom e vendas |
| fuse | FUSE — insurtech no Sudeste Asiático |
| genius | Genius (Paris) — consultoria de marketing e digital |
| graft | Graft — recrutamento generalista |
| groundcontrol | Ground Control — manutenção externa e biodiversidade |
| habitat | HEALTH CITY — saúde, ~500 pessoas, fundada em 2012 |
| homa | hôma — **varejo físico em Portugal**. Não é a Homa Games francesa |
| infinity | Infinity — call tracking e analytics digital |
| kinetic | Kinetic Software — software de gestão para universidades e venues |
| life | Life Sverige — maior rede varejista de saúde do Nordics |
| lunar | Lunar — banco digital licenciado nos Nordics |
| neat | Neat — hardware de videoconferência |
| osome | Osome — fintech para empreendedores |
| parkerschauffeurs | Parkers Chauffeurs — transporte executivo e VIP |
| salt | Salt — bootcamp de engenharia de software, Estocolmo |
| sunday | Sunday — tecnologia para hospitalidade e restaurantes |
| sweetspot | Sweetspot — plataforma de comércio para **golfe** |
| tribes | TRIBES — recrutamento executivo boutique |
| unleash | Unleash — plataforma open-source de feature flags (devtools), Oslo |
| waypoint | Waypoint Port Services — agência portuária marítima |
| yonder | Yonder — fintech, cartão de crédito com recompensas |

---

## Conferência aritmética

```
89  slugs na lista "livre"
-26 falsos livres (já enviados)          seção 2
=63 sem recibo
    -15 fila limpa (estúdios confirmados)  4a
    - 3 duvidosos                          4b
    - 4 slugs inválidos                    4c
    -41 falsos amigos                      4d
    = 0  ✓

66  slugs com recibo
-56 com linha no CSV                     seção 3
=10 buracos                              seção 3  ✓
```

Os 56 se compõem assim: 55 achados pelo varredor automático, **menos** `blackkitestudios` e `framebreak` (casamentos errados, viraram buracos), **mais** `ioi`, `pfx` e `sybo` (slugs de 3 letras que o varredor pulou e eu conferi na mão). 55 − 2 + 3 = **56**. E 56 + 10 = 66.

## Causa raiz, em uma frase

Deduplicar por **nome da casa** dentro do CSV falha em três pontos ao mesmo tempo: o nome no CSV não é o slug (`Stunlock Studios` ≠ `stunlocksstudios`, `Ghost Ship Games` ≠ `ghostship`), a linha pode nunca ter sido escrita (os 10 buracos), e a lista de entrada pode ter grafias divergentes do próprio slug (`paradoxinteractive` vs `paradox-interactive`, `envar` vs `envarstudio`). A chave de dedupe tem que ser o **slug do domínio de recibo**, e a razão tem que ser a caixa de entrada — foi assim que os 26 apareceram.
