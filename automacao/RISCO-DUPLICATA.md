# Lista de vigilância: 29 estúdios com entrada ABERTA e outra JÁ ENVIADA

Levantada em 07/09 às 22h20, direto do array PORTAIS do `docs/index.html`, cruzando nome de
estúdio normalizado (sem acento, sem sufixo `Studios`/`Games`/`Entertainment`/`Interactive`/
`Inc`/`Ltd`/`Animation`/`VFX`/`Pictures`, cortando no primeiro parêntese, hífen ou vírgula).

## O que esta lista é, e o que ela NÃO é

**Não são 29 erros.** A esmagadora maioria é legítima: casa grande publica várias requisições
diferentes, e ter uma enviada não impede as outras. A Netflix tem oito entradas abertas e uma
enviada, e são vagas distintas. A Sony Imageworks tem sete enviadas e uma aberta.

**É a lista dos lugares onde o erro de hoje pode acontecer de novo.** Duas vezes em 07/09 a
campanha mandou candidatura repetida:

- **Union VFX, 16h15** — eu mesmo, pulando a garra, porque o envio nasceu de uma resposta
  humana e a pressa foi maior. Outro agente já tinha aplicado no mesmo dia.
- **UPP de Praga, à noite** — um agente recebeu HTTP 200, **não leu o corpo** (que dizia
  `{"success":true,...}`), não marcou `done=true`, a entrada ficou aberta, e outro agente
  mandou de novo horas depois.

O padrão é sempre o mesmo: **o estúdio já foi trabalhado, a entrada continua aberta, e quem
chega depois lê "aberta" como "por fazer".**

## A regra, em uma linha

**Nesta lista, o dedupe é pela REFERÊNCIA DA REQUISIÇÃO, nunca pelo nome do estúdio nem pelo
título da vaga.** Antes de enviar em qualquer casa daqui, abra a entrada `done=true` do mesmo
estúdio e confirme que é **outra requisição**. Casa bilíngue publica a mesma vaga em dois
idiomas: Ubisoft, Larian, Gameloft, Sloclap, Skydance Madrid e Rodeo FX já enganaram nosso
dedupe assim.

E confira o **Gmail**, sempre: a garra não enxerga envio que não foi registrado no painel.
Em 07/09 apareceram três envios reais assim — Larian (recibo do Lever às 04h35), Cosmico
(email às 01h08) e REALTIME UK (candidatura listada no painel do Teamtailor apesar da tela
ter voltado vazia).

## A lista (abertas | enviadas)

| Estúdio | Abertas | Enviadas |
|---|---|---|
| Atomic Cartoons | 1 | 1 |
| Behaviour Interactive | 3 | 1 |
| Blizzard Entertainment | 1 | 2 |
| Bulkhead Interactive | 2 | 2 |
| Digic Pictures | 2 | 4 |
| Disney Television Animation | 1 | 1 |
| DNEG | 1 | 1 |
| Electronic Arts | 1 | 5 |
| Epic Games | 2 | 4 |
| FIN Design + Effects | 2 | 1 |
| Funcom | 1 | 1 |
| Funday Games | 1 | 1 |
| ICON Creative Studio | 1 | 1 |
| Kabam | 1 | 1 |
| Loonshot Games | 1 | 1 |
| Netflix Animation Studios | 8 | 1 |
| Plumeria Studio | 1 | 1 |
| Riot Games | 2 | 2 |
| Santa Monica Studio | 4 | 1 |
| Scopely | 1 | 2 |
| Side | 1 | 1 |
| Sony Pictures Imageworks | 1 | 7 |
| Swaybox Studios | 1 | 1 |
| TAT Productions | 1 | 3 |
| Techland | 2 | 1 |
| thatgamecompany | 1 | 1 |
| Triband | 1 | 1 |
| Ubisoft Montréal | 2 | 1 |
| Vine FX | 1 | 1 |

## Quatro que já têm veredito escrito e NÃO devem ser reabertas

- **Ubisoft Montréal, Senior Character Artist de Rainbow Six Siege** — o Vini **já foi
  recusado** nesta requisição em 02/09. A armadilha que escondeu isso foi o título localizado
  em francês e inglês.
- **thatgamecompany** — o anúncio diz "We are unable to sponsor", e a vaga virou `Remote - US`
  sem Canadá.
- **Vine FX** — veto de residência escrito no anúncio.
- **Disney Television Animation, Location Design Lead e Background Paint Lead** — são
  disciplinas que ele não tem, e a ressalva da regra 14 manda não enviar.

## Como refazer este levantamento

```
python3 - <<'PY'
import io,re,unicodedata
t=io.open("docs/index.html",encoding="utf-8").read()
i=t.index("const PORTAIS = [");j=t.index("].map",i)
L=[l for l in t[i:j].split("\n") if l.strip().startswith("[")]
def nome(l):
    m=re.match(r'\s*\["([^"]+)"',l)
    if not m: return None
    n=re.split(r'\s*[\(\-–]|,', m.group(1))[0]
    n=unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()
    n=re.sub(r'\b(studios?|games?|entertainment|interactive|inc|ltd|animation|vfx|pictures|the)\b','',n)
    return re.sub(r'[^a-z0-9]','',n)
feitos={};abertos={}
for l in L:
    n=nome(l)
    if not n or len(n)<4: continue
    (feitos if ",true," in l else abertos).setdefault(n,[]).append(l)
for n in sorted(set(abertos)&set(feitos)):
    print(n,len(abertos[n]),len(feitos[n]))
PY
```
