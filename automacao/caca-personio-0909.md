# CAÇA PERSONIO E FAMÍLIAS DE SLUG — 09/09

**Resultado curto e honesto: ZERO vagas novas para a fila.**

A troca de fonte de slug funcionou e funcionou muito: onde a rodada anterior mediu **80 chutes e
80 erros (80/80 em 307)**, os nomes tirados do `STUDIOS` e do `PORTAIS` acertaram **52 inquilinos
vivos no Personio, 21 quadros vivos no JazzHR, 19 no Factorial e 6 no Traffit**. A hipótese do
enunciado está confirmada com número: **derivar slug de lista real descobre; chutar não descobre.**

Mas descobrir inquilino não é descobrir vaga. Dos **385 anúncios** que esses 98 quadros vivos
serviram, **1 passou a disciplina** — 3D Artist Generalist, Modelling & Texturing, da Chimera
Entertainment — e essa uma é **onsite em Cebu, nas Filipinas**, fora do escopo por escrito.
A fila é zero, e as três seções finais explicam por quê com as armadilhas que eu medi.

O ganho real da rodada não é fila: são **cinco armadilhas de método novas**, todas medidas, na
seção 5. Duas delas invalidam parcialmente o protocolo que a campanha vinha usando.

---

## 1. Placar

### 1.1 Fonte dos slugs

| Etapa | Número |
|---|---|
| Linhas do array `STUDIOS` de `docs/index.html` | **680** |
| Linhas do array `PORTAIS` de `docs/index.html` | **775** |
| Nomes limpos únicos (sem parênteses, sem sufixo após ` - `, sem acento) | **1.088** |
| **Variantes de slug geradas** | **2.889** |

Regra de variante, por nome: tudo junto e minúsculo; com hífen entre palavras; sem os sufixos
`studio/studios/games/game/entertainment/interactive/animation/vfx/productions/media/inc/ltd/llc/gmbh/group/company/the/and`;
e a sigla das iniciais quando o nome tem três ou mais palavras (com e sem os sufixos).
**As duas grafias, colada e hifenizada, foram testadas em todas as famílias**, como manda o
precedente `warhorse-studios` contra `warhorsestudios`.

### 1.2 Requisições

| Família | Padrão sondado | Requisições | Vivos | Discriminador medido |
|---|---|---|---|---|
| **Personio** | `https://<slug>.jobs.personio.com/xml` | 2.889 | **52** | 200 = inquilino vivo · **404 = inquilino vivo, feed desligado** · 307 = não existe |
| **JazzHR** | `https://<slug>.applytojob.com/apply` | 2.899 | **21** | 200 com tamanho ≠ 79.750 = vivo · **200/79.750 = conta morta** · 302 = não existe |
| **Factorial** | `https://<slug>.factorialhr.com/` | 2.889 | **19** | 200 = vivo · 302 = vivo em domínio de país · 404 = não existe |
| **Traffit** | `https://<slug>.traffit.com/career` | 5.068 conexões / 2.889 resultados | **6** | 301 = vivo · 503 = não existe |
| **eRecruiter** | — | 4 (só calibragem) | **0** | **não é sondável por slug**, ver 5.5 |
| | **TOTAL** | **≈ 13.760** | **98** | |

Códigos crus, por família:

- **Personio** — 200: 41 · 404: 11 · 307: 2.836 · 000: 1 (`rebellion`, DNS não resolve)
- **JazzHR** — 200: 46, dos quais **24 são "JazzHR - Inactive Career Page"** (79.750 bytes exatos)
  e 1 quase-igual (`cloudimperium`, 79.751) · 302: 2.852
- **Factorial** — 200: 7 · 302: 12 · 404: 2.869 · 000: 1 (`paradoxinteractive`)
- **Traffit** — 301: 6 · 503: 2.883

### 1.3 Funil

| Etapa | Número |
|---|---|
| Quadros vivos encontrados | **98** |
| **Vagas totais servidas por esses quadros** | **385** |
| — Personio, feed XML (28 feeds com conteúdo) | 207 |
| — Personio, quadros de feed desligado (11 inquilinos) | 21 |
| — JazzHR (21 quadros) | 157 |
| — Factorial (19 inquilinos) | **0** |
| — Traffit (6 inquilinos) | **0** |
| Batem a disciplina **pelo título** | **21** |
| Abertas e lidas em **TEXTO INTEGRAL** | **13** |
| **Passaram a disciplina depois de ler o corpo** | **1** |
| **Dentro do escopo geográfico** | **0** |
| Passaram a régua de vinte termos | **0** (nenhuma chegou lá) |
| Passaram o dedupe | **0** |
| Passaram o teste dos três tiros | **0** |

**A fila é zero.** Não invento fila.

---

## 2. A fila

**VAZIA.** Nenhuma vaga passou disciplina + escopo + régua + dedupe + três tiros.

O que existe, e que a próxima rodada deve saber que existe, são **três portas espontâneas vivas e
inéditas por id**, em casas que a campanha já conhece. Elas não são fila porque **candidatura
espontânea não tem disciplina** — não há anúncio para passar pelo filtro 1 —, mas as três portas
foram medidas com os três tiros e as três funcionam. Ficam registradas, não promovidas.

### Porta espontânea 1 — Chimera Entertainment (Munique)

| Campo | Valor |
|---|---|
| **Estúdio** | Chimera Entertainment GmbH (Angry Birds Epic/Evolution, Songs of Silence) |
| **Cargo** | *speculative application (f/m/d)* — espontânea, sem disciplina declarada |
| **Cidade/País** | Munique, **Alemanha** (DE - Munich Office) |
| **Formato** | Full-time, Permanent employee, presencial em Munique |
| **Requisição** | **150955** |
| **Faixa publicada** | não publica |
| **URL COMPLETA DE CANDIDATURA** | `https://chimera-entertainment.jobs.personio.com/job/150955/apply` |

**Régua de vinte termos — 3 casamentos, os 3 falsos positivos:**

- `based in` → "Chimera Entertainment is a creative and independent game development studio
  **based in** the heart of Munich." — **falso positivo**, é o endereço do estúdio.
- `relocat` → "**Relocat**ion Support to Munich" — **falso positivo e favorável**, oferece
  ajuda de mudança.
- `within the` → "we want to expand our success **within the** coolest industry in the world" —
  **falso positivo**, ruído puro, é frase de marketing.

**Nenhum veto escrito.** O anúncio diz o contrário: "Didn't find a role that fits? Apply anyway!"

**Dedupe por id `150955`:** `docs/index.html` **0** · `enviados.csv` **0** ·
`automacao/processados.csv` **0** · `automacao/FILA-DO-VINI.md` **0**.
**Ressalva:** o id é inédito, a CASA não é — "Chimera" dá idx=2, env=1, proc=4.

**Três tiros:**

| Tiro | Código | Tamanho |
|---|---|---|
| 1. `Accept: */*` | **200** | 110.272 |
| 2. `Accept: text/html` + UA de navegador | **200** | 110.272 |
| 3a. **Controle**, id inventado `999999999` | **404** | 17.491 |
| 3b. **Controle**, inquilino inventado | **307** | 8.902 |

Duas 200, sem 302 para o site do estúdio; os dois controles discriminam por código E por tamanho.
**É porta.**

### Porta espontânea 2 — Outplay Entertainment (Dundee)

| Campo | Valor |
|---|---|
| **Estúdio** | Outplay Entertainment Ltd (maior dev móvel independente do Reino Unido) |
| **Cargo** | *Speculative Applications* — espontânea |
| **Cidade/País** | Dundee, **Escócia, Reino Unido** |
| **Formato** | não declarado no anúncio |
| **Requisição** | **CS3Wh2** |
| **Faixa publicada** | não publica |
| **URL COMPLETA DE CANDIDATURA** | `https://outplayentertainment.applytojob.com/apply/CS3Wh2/` |

**Régua — 3 casamentos, os 3 falsos positivos:**

- `based in` → "Founded in 2010 and **based in** Dundee, Outplay Entertainment is the largest
  independent mobile developer in the UK." — **falso positivo**, endereço do estúdio.
- `relocat` → "Are you willing to **relocat**e? / Yes / No" — **falso positivo**, é campo de
  formulário, pergunta e não exigência.
- `only` → "The personal data you provide will **only** be processed in accordance with our
  privacy policy." — **falso positivo**, cláusula de privacidade. Confirma o que o enunciado já
  antecipava: `only` sozinho não descarta nada.

**Nenhum veto escrito.**

**Dedupe por id `CS3Wh2`:** index **0** · enviados **0** · processados **0** · fila **0**.
Casa conhecida (`Outplay` idx=1, proc=1), id inédito.

**Três tiros:**

| Tiro | Código | Tamanho |
|---|---|---|
| 1. `Accept: */*` | **200** | 109.716 |
| 2. `Accept: text/html` + UA | **200** | 109.716 |
| 3a. **Controle**, id inventado `ZZ9zzQ` | **410** | 91.051 |
| 3b. **Controle**, inquilino inventado | **302** | 0 |

**É porta**, e o JazzHR ainda dá um bônus: o controle de id devolve **410**, ou seja a família
**discrimina vaga morta**, coisa que o Workday cru não faz. Vale como verificador barato.

### Porta espontânea 3 — DM BOŚ / bossa.pl — **DESCARTADA, colisão de nome**

`bossa.traffit.com` responde 301 e serve um formulário espontâneo vivo
(`/public/form/a/5003d805963ac8c48b50954ccda5c9694363593d`, três tiros 200/200 contra controle
404/1.372). **Não é a Bossa Studios.** O rodapé aponta para `bossa.pl`, `facebook.com/bossafx` e
`linkedin.com/company/dm-bos-s.a.`: é a corretora polonesa Dom Maklerski BOŚ. Fica registrada
como colisão medida, não como porta da campanha.

---

## 3. As 13 lidas em texto integral, e por que 12 caíram

Ordem: as que chegaram mais perto primeiro.

| # | Casa / cargo | Onde caiu | Motivo, com a frase |
|---|---|---|---|
| 1 | **Chimera Entertainment — 3D Artist Generalist, Modelling & Texturing** (`2628421`) | **ESCOPO** | Disciplina **passa inteira**: "Your focus will be on **modelling and texturing**, with a mix of **characters, props**, and other production assets". Mas: "You will work **onsite from our Cebu office**" — Cebu, **Filipinas**. Ásia só Coreia do Sul e Singapura. Fora. Dedupe do id era 0/0/0/0; morreu no escopo, não no dedupe. |
| 2 | **Aesir Interactive — Art Lead** (`2385017`) | **DEDUPE** e disciplina | `docs/index.html` **1** · `enviados.csv` **1** · `processados.csv` **3** · fila **0**. **Já enviada.** E o corpo desqualificaria de todo jeito: "This role is fundamentally **management-driven**... **Rather than operational creation**, your role is to define scope, guide execution" — é gestão de produção de arte, não modelagem. Régua: 3 falsos positivos (`relocat` = "Relocation support if needed" que é oferta; `located in` = "Located in Munich, Germany" que é endereço; `within the` = "within the department"). Faixa publicada: **66.000–78.000 €/ano**. |
| 3 | **Aesir Interactive — Technical Art Lead** (`2754909`) | **DISCIPLINA** | Id inédito (0/0/0/0), Munique + remoto, faixa **66.000–85.000 €/ano**, régua limpa. Mas é engenharia: "You own the **performance budget**... Every week you report **frame rate, memory and load times** per hardware target". Materiais e shaders aparecem numa lista que inclui "animation systems, UI, VFX, audio integration, procedural content, and the **tooling**". Arte técnica e engenharia pura não contam. |
| 4 | **L'Atelier Animation — Généraliste 3D (IA Focus)** (`duiYR7Gpp5`), Montreal | **DISCIPLINA, pelo corpo** | O título é da disciplina em cheio e o corpo não é: "**Intégrer des outils d'IA** dans les workflows de production... Éventuellement **ajuster (fine-tuning) ou déployer des modèles de machine learning**... Excellentes compétences en matière de **dépannage et de débogage**". É engenharia de pipeline com ML. Também é "Temporary / **Entry Level**". Ver armadilha 5.4. |
| 5 | **Stellar Creative Lab — Crowd Artists** (`IaRPzUt4uQ`), B.C., Canadá | **DISCIPLINA + VETO ESCRITO** | Disciplina: é simulação de multidão, "balance **technical simulation skills**... deep experience with background **crowd simulation**". CFX/simulação não conta. E há **veto escrito real**, único da rodada: `eligib` → "**Eligibility: You must be legally eligible to work in Canada.**" Não é bloco de benefícios nem ação afirmativa: é linha de elegibilidade própria. Casam ainda `work permit` e `resident` ("priority will be given to BC **Resident**s") no mesmo sentido restritivo. |
| 6 | **Lightbox Animation Studios — Mid/Senior CFX Artist** (`2316473`), remoto | **DISCIPLINA** | CFX puro: "strong knowledge of the behavior of different **cloths**, weights and falls". Régua: só `within the` em "Works **within the** established pipeline", falso positivo. Dedupe: `docs/index.html` **1**. |
| 7 | **RWS Global — Manager, Scenic & Props Design** (`63PDRY4bSO`), Milton Keynes | **DISCIPLINA** | "Props" enganou o título: é cenografia física de espetáculo ao vivo — "Place of Work: UK HQ, Mill Court, Milton Keynes", "During **Install** Schedule: as needed averaging 10 hour day". Não é modelagem 3D. Casaria `days in the office` ("Mobile, **3 days in the office**, 2 days remote"), que seria falso positivo de híbrido. |
| 8 | **MILK — Art Director** (`1113543`), Colônia | **DISCIPLINA** | Agência de publicidade, não estúdio 3D: "Aufbau von **Print- und Online-Werbemitteln**... Versierter Umgang mit allen gängigen Grafikprogrammen (**Adobe Creative Suite**)". Design gráfico 2D. |
| 9 | **MILK — Senior Art Director** (`1113525`), Colônia | **DISCIPLINA** | Mesma casa, mesmo motivo. |
| 10 | **Trixter — Speculative Job Application** (`2785192`), Munique/Berlim | **PORTA MORTA** | Casa de VFX de verdade e id inédito, mas ver 5.1: o feed lista, a página 307 para `personio.com`. Não é porta. |
| 11 | **Cosmico — General Application** (`2022617`), Milão | **NÃO É EMPRESA** | Inquilino de **demonstração** do Personio. O corpo é Lorem ipsum e assina: "The **Demo Data Ltd.** is a fictional company created by Personio to familiarise you with our software." Ver 5.2. |
| 12 | **Chimera Entertainment — speculative** (`150955`) | passou | Registrada acima como porta espontânea 1. |
| 13 | **Outplay Entertainment — Speculative** (`CS3Wh2`) | passou | Registrada acima como porta espontânea 2. |

**Descartadas pelo título, sem leitura integral** (as 8 restantes das 21): Chimera *Senior
Technical Artist - 3D & Unity* (arte técnica), Deck13 *Lead VFX Artist* e *Senior VFX Artist*
(VFX em tempo real), Popcore *Motion Designer 2D/3D* (motion design), Obsidian Entertainment
*Senior Concept Artist* (concept 2D), Flying Bark *Animation Director* e *Lighting Key Color
Script Artist* (animação e iluminação/cor), Stellar *Background Painters & Concept Artists*
(pintura, exclusão explícita da régua de disciplina).

---

## 4. Padrões de URL confirmados nesta rodada

Para as próximas rodadas não terem que remedir.

| Família | Feed / quadro | Vaga | **Formulário** | Controle que discrimina |
|---|---|---|---|---|
| **Personio** | `https://<slug>.jobs.personio.com/xml` | `.../job/<id>` | **`.../job/<id>/apply`** | id falso → **404** · inquilino falso → **307** |
| **JazzHR** | `https://<slug>.applytojob.com/apply` | — | **`.../apply/<token>/`** | id falso → **410** · inquilino falso → **302** |
| **Factorial** | `https://<slug>.factorialhr.com/` | `.../job_posting/<slug-id>` | `.../apply/<slug-id>` | slug falso → **301** |
| **Traffit** | `https://<slug>.traffit.com/career` | (JS) | `.../public/form/a/<hash 40 hex>` | hash falso → **404** |
| **eRecruiter** | — | — | `https://form.erecruiter.pl/form/<32 hex>` | **não sondável**, ver 5.5 |

**Correção do registro de 08/09 sobre o Personio.** O relatório anterior deu o formulário como
`/job/<id>?apply`. **Está errado por um salto:** `?apply` devolve **307** e só então redireciona
para `/job/<id>/apply`. Medido na Chimera: `?apply` → 307, `Location: .../job/150955/apply`.
Quem sondar com `?apply` e a regra "307 = não existe" **descarta vaga viva**. A URL canônica é
com barra.

**Domínios de país do Factorial**, revelados pelos 302 e que nenhum registro da campanha tinha:
`.factorial.es` · `.factorial.it` · `.factorial.mx` · `.factorialhr.co` · `.factorialhr.pt` ·
`.factorialhr.de`. Sondar só `.factorialhr.com` **perde 12 dos 19 inquilinos vivos**. O 302
entrega o domínio certo de graça no `Location`.

---

## 5. Armadilhas de método medidas hoje

### 5.1 O feed do Personio mente — vaga no XML com página 307

**Esta é a descoberta mais séria da rodada, e ela corrige a regra que a campanha usa desde 08/09.**

O registro de 08/09 diz que o feed do Personio é "limpo, sem captcha" e trata 200 no feed como
quadro vivo. Medido hoje na **Trixter**:

| URL | Código | Tamanho |
|---|---|---|
| `trixter.jobs.personio.com/xml` | **200** | 1.218 (traz `<id>2785192</id>`) |
| `trixter.jobs.personio.com/job/2785192` | **307 → personio.com** | 21.249 |
| `trixter.jobs.personio.com/job/2785192/apply` | **307 → personio.com** | 16.422 |
| **Controle**, id falso no mesmo inquilino | **404** | 16.262 |

Três tentativas seguidas, mesmo resultado, e não é limite de taxa: o `/xml` do mesmo inquilino
continuava devolvendo 200 no mesmo instante. O controle **discrimina** (404 contra 307), o que
prova que o 307 não é casca genérica — é a resposta específica de "esta vaga não está publicada".

**Regra nova: um id que aparece no feed do Personio não é vaga viva.** O feed precisa ser
confirmado abrindo `/job/<id>/apply`. Isso é o irmão exato do que a campanha mediu em 07/09 no
skillshot.pl e no Google Forms — 200 não é vida —, agora dentro da família que o registro
anterior tratava como confiável.

### 5.2 O Personio serve inquilinos de DEMONSTRAÇÃO com 200 e feed cheio

**Dez dos 41 "200" do Personio são contas de demonstração**, não empresas. Elas devolvem feed XML
válido, com posições, ids e escritórios — e o corpo é Lorem ipsum assinado
"The Demo Data Ltd. is a fictional company created by Personio".

Slugs afetados: `bbg` · `ssm` · `boxelware` · `kaiko` · `sandbox` · `epg` · `etg` · `hpe` ·
`100` · `acs`. Assinatura: **as mesmas três a seis vagas em todos**, "SEO Marketing Manager",
"Social Media (Werkstudent)", "Initiativbewerbung (Festanstellung)", "Fahrer/in",
"Junior IT-Sicherheitsberater". Confirmado por `grep` de `Lorem ipsum` dentro dos XML: de 3 a 9
ocorrências em cada.

**Regra:** antes de contar um inquilino Personio como quadro, `grep -i "lorem ipsum\|demo data"`
no feed. Custa um comando. Sem isso, esta rodada teria reportado 41 quadros vivos em vez de 31.

### 5.3 O JazzHR devolve 200 para conta MORTA — e são 24 de 46

Mais da metade dos "200" do JazzHR são **contas encerradas**, e o código não denuncia:
`<title>JazzHR - Inactive Career Page</title>`, "This account is no longer active",
**79.750 bytes exatos em todas**.

Entre elas, nomes que teriam virado manchete falsa numa rodada apressada: `blizzard`,
`epicgames`, `king`, `cloudimperiumgames`, `distillery`, `monsters`, `pipeline`, `midnightworks`.
O controle de inquilino inventado dá **302**, não 200 — então **o teste de dois tiros clássico
aprova essas 24**. Só o tamanho fixo as separa.

**Regra:** no JazzHR, vivo é 200 **com tamanho diferente de 79.750**. É o caso inverso do HiBob
de 08/09: lá o tamanho idêntico entre real e falso invalidava o teste; aqui o tamanho idêntico
entre os falsos é justamente o que os identifica.

### 5.4 Título da disciplina com corpo de outra disciplina

Três casos hoje, e nenhum se resolve pelo título:

- **L'Atelier Animation, "Généraliste 3D"** — corpo é integração de IA, ferramentas procedurais
  e *fine-tuning* de modelos de machine learning.
- **RWS Global, "Manager, Scenic & Props Design"** — "props" é cenografia física de espetáculo.
- **Stellar Creative Lab, "Crowd Artists"** — "artist" é simulação de multidão.

E o inverso também: **Aesir "Art Lead"**, que soa como liderança de arte da disciplina, diz por
escrito "**Rather than operational creation**". **O filtro de disciplina não pode rodar no título.**
Dos 21 títulos plausíveis, só 1 sobreviveu à leitura do corpo — **taxa de mortalidade de 95%**.

### 5.5 O eRecruiter não é sondável por slug, e isso é definitivo

Medido, não suposto: `https://<slug>.erecruiter.pl/` devolve **000** (o DNS não resolve) tanto
para slug real quanto para inventado — não há subdomínio por locatário. As URLs públicas da
família são `https://form.erecruiter.pl/form/<32 hex>` e `https://system.erecruiter.pl/...`, e
essa última exige OIDC (302 para `auth.erecruiter.pl/connect/authorize`). **O hash não é
derivável de nome nenhum.**

O eRecruiter sai da lista de "não testadas" e entra na de **estruturalmente não sondáveis**, junto
com as famílias de hash opaco (JotForm, Tally, Google Forms). Para elas a única via é a inversa
que o registro de 08/09 já apontou: abrir a página de carreiras do estúdio e ver o que ela embute.

### 5.6 Sigla de iniciais é a variante mais barulhenta — e não rendeu nada

Das quatro regras de variante, a sigla foi a que mais gerou 200 e a que menos rendeu. **Todos** os
acertos por sigla são colisão com empresa alheia:

| Sigla | Veio de | Quem respondeu de verdade |
|---|---|---|
| `buf` | BUF (VFX, Montreal/Paris) | rede de **óticas** em Hannover (Augenoptiker) |
| `asg` | *Avalanche Studios Group* | escritório de **auditoria fiscal** em Hamburgo |
| `bis` | — | **escola internacional** em Haimhausen |
| `bve` | — | **gestão imobiliária** em Hamburgo |
| `cas` | — | consultoria **SAP** |
| `gcs` | — | eletrônica suíça em Zurique/Stockach |
| `hps` | — | escritório fiscal em Herford |
| `mgs` | — | *Münchner Gesellschaft für Stadterneuerung* |
| `rms` | — | *Radio Marketing Service* |
| `obsidian` (Personio) | Obsidian Entertainment | **Obsidian Digital**, agência dinamarquesa de SEO |
| `chimera` (JazzHR) | Chimera Entertainment | **Chimera Enterprises International**, empreiteira de defesa da DARPA |
| `squeeze` | Squeeze Studio (animação, Quebec) | **Squeeze Massage**, rede de spas |
| `playground` | Playground Games | **cassino** com vagas de *Sous Chef* e *Cocktail Server* |
| `tendril` | Tendril (animação, Toronto) | SaaS com vagas de *Sales Development Representative* |
| `bossa` | Bossa Studios | corretora polonesa **DM BOŚ** |
| `rumble` | — | grupo de **jornais** de Dortmund, 49 vagas |
| `valve` | Valve | inquilino com uma vaga só, "Opportunistic" |

**A sigla merece continuar sendo gerada** — é barata e o 307/503 mata quase tudo —, **mas nenhum
200 por sigla pode ser contado como quadro do estúdio sem conferir o `<title>` do quadro.** Foi
exatamente essa conferência que evitou reportar "achamos o quadro da Obsidian, da Blizzard e da
Playground" nesta rodada.

### 5.7 O 404 do Personio NÃO é "não existe" — e é onde estavam as casas boas

O enunciado dá a regra "307 = não existe, 200 = quadro vivo" e ela está certa nas duas pontas.
Mas há um terceiro código no meio, e ele quase passou batido: **404 no `/xml` significa inquilino
vivo com o feed XML desligado.** Onze slugs caíram aí, e ao abrir a raiz `https://<slug>.jobs.personio.com/`
os **onze responderam 200 com quadro renderizado**:

`chimera-entertainment` (Jobs at Chimera Entertainment GmbH) · `lightbox-animation-studios`
(Jobs at Lightbox Animation) · `limbic-entertainment` · `milk` · `bluebackpack` · `obsidian` ·
`mad` · `union` · `rms` · `sfs` · `fds`.

**As duas casas mais relevantes da rodada inteira estavam nesse grupo** — a Chimera, que deu a
única vaga da disciplina e a porta espontânea 1, e a Lightbox. Se eu tivesse tratado 404 como
morte, teria reportado zero com menos informação e teria dito que a Chimera não usa Personio.

**Regra: todo 404 no `/xml` precisa de um segundo tiro na raiz do quadro.**

### 5.8 Ruído medido nos dois termos novos da régua

`within the` e `only` foram desenhados para obrigar a ler, e foi o que fizeram: **casaram 5 vezes
e nas 5 são falso positivo** — "within the department", "within the coolest industry",
"works within the established pipeline", "specialist in only one narrow area", "will only be
processed in accordance with our privacy policy". Zero veto.

Em compensação, o buraco que eles vieram tapar continua sem aparecer: **nenhum anúncio desta
rodada trouxe o padrão "Remote within the UK"** da Pretty Cool Games. Os dois termos ficam
justificados como custo baixo de leitura, mas a rodada não os validou na prática.

O único veto escrito da rodada veio de um termo **antigo** (`eligib`, na Stellar Creative Lab),
e ele é o contraexemplo direto do falso positivo já catalogado — `eligib` normalmente é benefício
ou ação afirmativa, e aqui era uma linha "Eligibility:" própria. **`eligib` não pode ser
descartado no automático; a frase tem que ser lida.**

### 5.9 Erro operacional meu: script sobrescrito no meio da varredura

Registro honesto de custo. Durante a varredura do Traffit o meu `probe.sh` **foi sobrescrito por
outro processo** com um script de formato diferente. O resultado: **2.179 das 2.884 linhas do
Traffit saíram corrompidas** (`PLAIN=000`, porque o segundo script interpretou "traffit" como URL),
e eu precisei refazer 2.184 slugs. Custo: 5.068 conexões para 2.889 resultados, quase o dobro.

**Lição:** script de varredura em diretório compartilhado precisa de nome com prefixo próprio.
Refiz com `vini_probe_tf.sh` e o segundo passe saiu limpo. Não afeta os números finais — os 2.889
resultados do Traffit são todos de execução válida —, mas afeta o custo e vale escrito.

---

## 6. O que a rodada prova sobre a hipótese do enunciado

**A hipótese está certa e o número é grande.**

| | Slugs chutados (08/09) | Slugs derivados do painel (hoje) |
|---|---|---|
| Sondas no Personio | 80 | 2.889 |
| Inquilinos vivos | **0** | **52** |
| Taxa de acerto | **0,0%** | **1,8%** |

E ela está certa nas outras três famílias também: 21 no JazzHR, 19 no Factorial, 6 no Traffit,
todos a partir de nome que já estava no `docs/index.html`. **A via de derivar slug de lista real
descobre inquilino, e descobre em escala.**

O que ela **não** faz é descobrir vaga. Os 98 quadros vivos serviram 385 anúncios e produziram
**uma** da disciplina, fora do escopo. O gargalo desta campanha não está mais em achar quadro —
está em que os quadros das casas certas estão vazios. **Factorial e Traffit renderam 25 inquilinos
vivos e ZERO vagas somadas**, incluindo casas boas como Black Forest Games, 34BigThings, Chibig e
Illusorium Studios, todas com quadro montado e nenhuma requisição aberta.

**Recomendação para a próxima rodada:** os 98 slugs vivos desta varredura estão medidos e são
estáveis. Revarrer **só esses 98**, semanalmente, custa 98 requisições em vez de 13.760, e é onde
uma vaga nova vai aparecer primeiro. A varredura larga não precisa ser refeita tão cedo.

---

## 7. Os 98 inquilinos vivos, para a próxima rodada não remedir

**Personio, feed 200 e relevantes** (5): `aesir` · `deck13` · `bongfish` · `popcore` ·
`trixter` (feed vivo, página morta — ver 5.1)

**Personio, feed 404 e quadro vivo** (11): `chimera-entertainment` · `lightbox-animation-studios` ·
`limbic-entertainment` · `milk` · `bluebackpack` · `obsidian` · `mad` · `union` · `rms` · `sfs` · `fds`

**Personio, feed vazio (72 bytes), inquilino vivo sem vaga** (13): `airbornstudios` · `amber` ·
`bandainamcomobile` · `bks` · `cag` · `carbon` · `cisc` · `daedalic` · `gdg` · `lighthouse` ·
`milford` · `paramount` · `vstep`

**Personio, demonstração — IGNORAR** (10): `bbg` · `ssm` · `boxelware` · `kaiko` · `sandbox` ·
`epg` · `etg` · `hpe` · `100` · `acs`
**Personio, colisão — IGNORAR** (2): `asg` · `bis` · `bve` · `cas` · `circus` · `gcs` · `hps` ·
`mgs` · `rumble` · `spectral` · `buf` · `valve` · `cosmico`

**JazzHR, quadro vivo** (21): `afp` · `big` · `chimera` · `cloudimperium` · `cyber` · `fas` ·
`flyingbarkproductions` · `latelieranimation` · `nextlevelgames` · `noodlecake` · `obsidian` ·
`osg` · `outplayentertainment` · `playableworlds` · `playground` · `rpm` · `rws` · `squeeze` ·
`stellarcreativelab` · `tendril` · `zoicstudios`
*Relevantes de fato*: `flyingbarkproductions`, `latelieranimation`, `nextlevelgames`,
`noodlecake`, `obsidian` (Obsidian Entertainment), `outplayentertainment`, `playableworlds`,
`stellarcreativelab`, `zoicstudios`.

**Factorial, inquilino vivo, ZERO vagas** (19): `black-forest-games` · `gamehouse` · `nbg` ·
`nexus` · `trs` · `ume` · `wws` · `34bigthings` (.it) · `chibig` (.co) · `copernicus` (.es) ·
`fireproof` (.mx) · `illusorium-studios` (.es) · `mago-production` (.es) · `lbs` (.it) ·
`sas` (.es) · `acs` (.es) · `goodjob` (.pt) · `usert38` (.es) · `vea` (.de)
*Relevantes*: `black-forest-games`, `34bigthings`, `chibig`, `illusorium-studios`.
**Pista lateral:** o quadro da Illusorium não lista vaga e aponta em texto para
`https://www.illusoriumstudios.com/careers` — é a porta de verdade dessa casa, não conferida aqui.

**Traffit, inquilino vivo, ZERO vagas** (6): `ansharstudios` · `arsthanea` · `boombit` ·
`bossa` (colisão) · `trust` · `wbs`
