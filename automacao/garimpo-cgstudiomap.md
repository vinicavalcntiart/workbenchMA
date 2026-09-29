# Garimpo cgstudiomap.org — rodada de 08/09/2026

Arquivo companheiro: `automacao/garimpo-cgstudiomap.csv` (889 linhas de dados).
Rodada de **levantamento apenas**. Nenhum e-mail, rascunho ou formulário foi tocado. Nenhum arquivo compartilhado foi editado. Nenhum navegador foi aberto (`pgrep -c chrome` = 0 no início; todo o trabalho saiu de `curl` e WebFetch).

---

## 1. A fonte designada está MORTA. Evidência medida, não suposta

**cgstudiomap.org não existe mais como diretório de estúdios.** O domínio foi perdido e hoje serve redirecionamento para spam. Medições de 08/09/2026:

| O que pedi | Resultado |
|---|---|
| `GET https://cgstudiomap.org/` (sem `-L`) | **HTTP/2 301**, `location: https://samuelcheng.info/`, `server: cloudflare` |
| `GET https://www.cgstudiomap.org/` | **HTTP/2 301**, mesmo `location: https://samuelcheng.info/` |
| Seguindo o redirect (`-L`) | **HTTP 200** em `https://precisionconcretecoatings.net/` (o destino final gira: outra medição caiu em `samuelcheng.info`, cujo `<title>` é `MANTRA62 - Masuk Dunia Game Online Gratis Tanpa Top Up Pertama`) |
| `GET https://cgstudiomap.org/page/website.directory` (rota do diretório Odoo) | **HTTP 200**, mas o corpo é o mesmo site de concreto — a rota não existe mais |

Ou seja: qualquer path do domínio devolve 301 para um destino de spam rotativo. Não é bloqueio, não é 403 de User-Agent, não é falha de `http://` simples — usei `https://` e User-Agent de Chrome em todas as chamadas, conforme as lições da campanha.

### Os outros domínios da marca também não servem

| Domínio | Resultado |
|---|---|
| `cgstudiomap.site` e `www.cgstudiomap.site` | **HTTP 200**, mas é página de **parking**. `<title>` = `cgstudiomap.site - cgstudiomap Resources and Information.`, com o atributo `data-adblockkey` no `<html>` — assinatura clássica de domínio estacionado |
| `cgstudiomap.site/studios-list/` (o path que o buscador ainda indexa como "List of CG Studios") | **HTTP 200** servindo **a mesma página de parking**, não a lista. `sitemap.xml` e `sitemap_index.xml` devolvem **HTTP 440** com corpo vazio. O resultado de busca é um snapshot velho do índice, não conteúdo vivo |
| `cgstudiomap.net`, `cgstudiomap.io` | **HTTP 000** — `connect_rejected` pelo proxy de egresso |

### Tentativas de recuperar o acervo histórico, e por que falharam

- **Wayback Machine**: bloqueado neste ambiente. `web.archive.org/cdx/...` devolve **HTTP 403 — "Host not in allowlist: web.archive.org"**. Pelo WebFetch, `archive.org` devolve `EGRESS_BLOCKED`. Não é o site que está fora, é a política de rede desta sessão.
- **timetravel.mementoweb.org**: HTTP 000, sem resposta.
- **Código-fonte do projeto**: o repositório existe (`M4rtine/cgstudiomap`, "old version of CG Studio Map - based on odoo", arquivado de fato desde 2021). Varri os CSV do repo: são **apenas fixtures do Odoo** (planos de contas, bancos, `ir.model.access`). **Não há nenhum dump dos estúdios** — o acervo vivia no banco de produção, que morreu com o domínio.
- Busca por espelhos/scrapes publicados: nada (`extension:json` com "cgstudiomap" no GitHub: 0 resultados).

**Conclusão honesta: da fonte designada, o número de estúdios extraíveis hoje é ZERO.** Não há paginação a descobrir porque não há listagem. Não inventei nenhum estúdio nem nenhuma URL a partir dela.

---

## 2. O que fiz em vez de entregar rodada vazia

Fui atrás do **sucessor funcional vivo** da mesma categoria — mapa/diretório de estúdios de CG — e encontrei o **mapa de estúdios do 3DVF**, `https://3dvf.com/en/studio/`. É o mesmo tipo de fonte (diretório geolocalizado de estúdios de VFX, animação e games, com ficha por estúdio).

**Cruzei antes de gastar tempo: a campanha nunca tocou nele.** Rodei o scanner nos arrays de `docs/index.html` (`PORTAIS` 736, `STUDIOS` 665) e busquei `cgstudiomap`, `3dvf`, `studiomap`, `studio map`, `world map`: **0 ocorrências de cada**. Fonte inédita para a campanha, tanto a morta quanto a substituta.

**Tudo que segue é do 3DVF, e está rotulado como tal.** Não estou passando um pelo outro.

---

## 3. Como paginei a fonte substituta — o parâmetro exato

A listagem HTML de `/en/studio/` **não serve para paginar**: o grid é JetEngine e chega vazio por `curl` (busquei o slug `arcade-vfx` no HTML da listagem: **0 ocorrências**). Quem tenta paginar pelo HTML conclui que a fonte tem zero itens.

O caminho certo é a **REST API do WordPress**, e o tipo de conteúdo se chama `studio` (confirmado em `/wp-json/wp/v2/types`, que lista `studio` com `rest_base: studio`):

```
https://3dvf.com/wp-json/wp/v2/studio?per_page=100&page=N
```

- **Parâmetro de paginação: `page=`, com `per_page=100`** (o máximo aceito).
- **Total dado pelo próprio servidor**, não estimado: cabeçalho **`x-wp-total: 1064`** e **`x-wp-totalpages: 11`**.
- **Fiz o teste de mudança que a campanha exige**: `page=1` começa em `arcade-vfx`; `page=2` começa em `the-yard-vfx`. **Os itens mudam** — o parâmetro está certo. Baixei as 11 páginas e conferi: 1064 registros baixados, **1064 únicos por id**, batendo exatamente com o `x-wp-total`.

**Armadilha registrada para a campanha:** a REST API **não** devolve país nem cidade (os campos são `id, slug, link, title` e uns metadados de escola vazios). País e cidade só existem na ficha individual `/en/studio/<slug>/`, sob os rótulos `Countries`/`Cities` — ou, nas fichas sem tradução, sob **`Pays`/`Villes`** em francês, com o botão de site rotulado `Voir le site` em vez de `Website`. Meu primeiro extrator perdeu ~40% dos estúdios por não tratar o francês. Corrigido e revalidado. **Baixei as 1064 fichas individuais: 1064 ok, 0 erro.**

Também existe `bureaux` (escritórios) com `x-wp-total: 1201`, e um CPT `offres-emploi` — este último devolve **`x-wp-total: 0`**, ou seja, o quadro de vagas do próprio 3DVF está vazio pela API e não rendeu nada.

---

## 4. Os números

| Medida | Valor |
|---|---|
| Estúdios que a fonte substituta tem no total | **1064** (confirmado pelo `x-wp-total`) |
| Fichas individuais baixadas com sucesso | **1064** (0 erro) |
| **Em escopo geográfico** | **889** |
| Já estavam na campanha | **221** |
| **NOVOS para a campanha** | **668** |
| Novos com site publicado (alvos varríveis) | 647 |
| Fora de escopo | 175 |
| Zona cinza, não contada no escopo duro (Suíça, Mônaco, México) | 15 |
| Sem país legível na ficha | 47 |

Fora de escopo por regra: Índia (33), Argentina (33), Japão (19), Brasil (16), além de Vietnã, Malásia, Turquia, China, Ucrânia, Equador, Chile, Bolívia, Marrocos, Egito, Madagascar, Israel e afins. Índia, Brasil e Japão foram cortados como manda o briefing.

**Distribuição dos 889 em escopo:** França 286, Canadá 158, EUA 145, Reino Unido 104, Dinamarca 41, Austrália 32, Suécia 32, Espanha 25, Noruega 20, Finlândia 19, Polônia 18, Nova Zelândia 14, Bélgica 9, Islândia 6, Luxemburgo 3, Alemanha 3, Áustria 3, Singapura 3, Irlanda 3, Hungria 2, Coreia do Sul 2, Bulgária 1, Chéquia 1, Eslováquia 1, Itália 1, Países Baixos 1, Romênia 1.

**Sobre o cruzamento (221 já conhecidos):** casei por **domínio do site** (176 casos, o critério forte) e por **nome normalizado** (45 casos, exigindo chave normalizada com 6+ caracteres para evitar colisão). O casamento por nome ainda pode ter falso positivo — vi `Alt-Studio` casando com `Alt.VFX` e `Artifex Studios` com `Artifex Animation Studios`, que provavelmente são casas distintas. **Na dúvida o CSV marca como já conhecido, o que empurra o número de novos para baixo, não para cima.** 668 é piso, não teto.

---

## 5. Vagas vivas da disciplina, com link direto e busca literal de veto

Método: nos 647 novos com site, li a home, procurei link de carreiras e assinatura de ATS; onde achei ATS consultei a **API pública** dele (Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters, Workable, BambooHR, Breezy, Teamtailor, Personio). Cobertura real: **24 com ATS detectado, 184 com página de carreiras lida, 83 com home que não respondeu**. As 20 candidatas brutas foram verificadas **uma a uma na mão** — a maioria era falso positivo (frase solta de requisito, não título de vaga). Sobraram 6.

Em cada uma baixei o texto e rodei a **busca literal dos 11 termos**: `authoriz`, `eligib`, `sponsor`, `work permit`, `must be based`, `LMIA`, `days a week`, `French`, `français`, `bilingue`, `resident`.

### ALTA — disciplina do Vini, vaga datada

**1. Massive Entertainment (Ubisoft) — Lead Character Artist — Malmö, Suécia**
`https://www.massive.se/job/lead-character-artist-744000144027102/`
**Veto: NENHUM dos 11 termos.** Anúncio integral baixado e lido (3.839 caracteres). É personagem 3D puro: "Produce and deliver quality 3D assets for the game (Character Art, NPCs, weapons and gear, Cinematic assets)", pede "Several years of experience with Character/3D-Art", "Ability to realize characters from concepts and Art Director briefs" e ferramentas "Maya, 3Ds MAX, ZBrush, Blender, Substance". É The Division 2. O quadro do estúdio tem 7 vagas, e esta é a única da disciplina. **Melhor achado da rodada.**

**2. Gradient Effects — 3D Modeler — Los Angeles, EUA**
`https://www.gradientfx.com/jobs/` (candidatura em `https://gradientfx.com/application/`)
**Veto: NENHUM dos 11 termos**, buscados no bloco da vaga E na página inteira. Pede "Expert knowledge of Maya, ZBrush, Mud Box", "Expert knowledge of Photoshop, Mari" e "Strong knowledge and experiences in materials/shader/look development" — modelagem, textura e look dev, exatamente o pipeline dele. As únicas restrições escritas são "NO PHONE CALLS" e "Walk-in applications will not be accepted".

### ALTA de disciplina, mas NÃO é vaga datada

**3. Jungler — 3D Look Dev, 3D Modeling Characters, 3D Surfacing, Groom Artist — La Plaine St-Denis, França**
`https://www.jungler.tv/jobs`
**Veto: NENHUM dos 11 termos.** Sendo honesto sobre o que isto é: a página diz "To complete our teams, we are looking for different profiles" e lista ~28 perfis, cada um com botão Apply próprio. É **captação permanente por perfil, não anúncio datado**. Quatro dos perfis são cheios da disciplina dele. Vale como porta aberta, não como vaga com prazo.

### MÉDIA — ambiente (prioridade média pela regra)

**4. GFactory — 3D Environment Artist Mid/Senior — França (remoto freelancer)**
`https://www.the-gfactory.com/fr/jobs/`
**Veto: 1 termo aparece — `french` — mas é falso positivo**, no trecho "Gfactory is a french art outsourcing studio founded in 2011". Não há exigência de idioma. Contexto que pesa mais: é posição **freelance remota**, não formato fixo.

**5. Foxie Ventures — Environment Artist — Adelaide, Austrália, Full Time**
`https://www.foxieventures.com/jobs/`
**Veto: NENHUM dos 11 termos.** O quadro rotula as posições como "Express Interest", então o grau de "vaga aberta agora" é incerto.

**6. 37Degrees Studio — Senior Matte Painter / Environment Artist — Wellington, Nova Zelândia**
`https://37degrees-studio.com/careers/`
**Veto: NENHUM dos 11 termos, mas leia isto antes de gastar tempo:** o texto diz literalmente "Operating fully in-office from Wellington NZ" e manda o candidato incluir no e-mail "your visa situation for working in New Zealand". Não é veto escrito da lista, mas é restrição presencial declarada. Candidatura por e-mail com assunto em formato fixo. O outro cargo do quadro é Matte Painter, que é 2D e fora da disciplina.

---

## 6. O que travou, dito sem maquiagem

1. **A fonte designada morreu.** Evidência acima. Sem Wayback (bloqueado pela política de rede desta sessão) não há como reconstruir o acervo dela.
2. **A maior limitação da caça a vagas foi a proibição de navegador, e ela é grande.** Os quadros dos estúdios grandes são SPA que montam a lista por JavaScript: `curl` traz o esqueleto e nenhuma vaga. Verifiquei e falhei em ler, um por um: **Scanline VFX, RISE, Firesprite, Frontier, Remedy, Avalanche Studios, Folks VFX, Beenox, Raynault, Skydance** — todos novos e em escopo, todos com quadro ilegível sem navegador. Housemarque expõe Greenhouse (`boards.greenhouse.io/housemarque`) e a API respondeu **0 vagas** de verdade. **Esses estúdios são o melhor lote para a próxima rodada, quando o navegador estiver livre.**
3. **83 dos 647 sites novos não responderam ao `curl`** dentro do timeout de 20s. Estão marcados `nao_verificado` no CSV, não `nao`.
4. **`nao_encontrada` no CSV não quer dizer "não tem vaga".** Quer dizer que li a página de carreiras ou a API do ATS e não vi título da disciplina — e se o quadro for JS, eu não veria mesmo que houvesse. Só `sim` é afirmação medida.
5. **Cobertura real do rastreio de vagas: 208 dos 668 novos** (24 via API de ATS + 184 via HTML de carreiras). Os outros 460 continuam por verificar. **Não estou reportando 668 estúdios rastreados.**
6. O quadro de vagas do próprio 3DVF (`offres-emploi`) devolve `x-wp-total: 0` e não rendeu nada.

## 7. Dicionário do CSV

`tem_vaga_disciplina` tem três estados, e a diferença importa:
- **`sim`** — vaga confirmada, anúncio baixado, busca de veto rodada. 6 linhas.
- **`nao_encontrada`** — página de carreiras ou API do ATS lida, nenhum título da disciplina. Pode ser quadro em JS. 179 linhas.
- **`nao_verificado`** — não varrido nesta rodada: já conhecido pela campanha, sem site, home fora do ar, ou sem link de carreiras identificável. 704 linhas.

A coluna `observacao` sempre termina com `| ficha:` e a URL da ficha do estúdio no 3DVF, para conferência.
