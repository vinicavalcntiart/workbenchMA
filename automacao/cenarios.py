#!/usr/bin/env python3
"""Monte Carlo da campanha do Vini. Rodar: python3 automacao/cenarios.py
Dados observados sao reais (31/08). Taxas nao observadas entram como priors
explicitos, com incerteza, nao como numero fixo."""
import random, statistics as st

N = 40000
random.seed(7)

# ---- OBSERVADO em 31/08 ----
EMAILS_ENTREGUES = 148
RESPOSTAS_HUMANAS = 12       # 10 recusas + 2 em andamento
PORTAIS_CONFIRMADOS = 33
ENTREVISTAS = 0
SILENCIOSOS = EMAILS_ENTREGUES - RESPOSTAS_HUMANAS   # 136 sem resposta
FOLLOWUPS = 90               # onda de 02/09 + 04/09

def beta(a, b):
    x = random.gammavariate(a, 1); y = random.gammavariate(b, 1)
    return x / (x + y)

def binom(n, p):
    if n <= 0 or p <= 0: return 0
    return sum(1 for _ in range(int(n)) if random.random() < p)

def rodar(nome, pi_email_a, pi_email_b, pi_portal_a, pi_portal_b,
          oferta_a, oferta_b, lift_followup):
    ents, ofs = [], []
    for _ in range(N):
        # taxa de resposta por email: posterior Beta a partir do observado
        p_resp = beta(1 + RESPOSTAS_HUMANAS, 1 + SILENCIOSOS)
        # follow-up reanima parte dos silenciosos
        novas_resp = binom(FOLLOWUPS, p_resp * lift_followup)
        total_resp = RESPOSTAS_HUMANAS + novas_resp
        # resposta -> entrevista (prior: nao observado ainda)
        p_int_email = beta(pi_email_a, pi_email_b)
        e1 = binom(total_resp, p_int_email)
        # portal -> entrevista direta (ATS costuma pular a resposta humana)
        p_int_portal = beta(pi_portal_a, pi_portal_b)
        e2 = binom(PORTAIS_CONFIRMADOS, p_int_portal)
        ent = e1 + e2
        # entrevista -> oferta
        of = binom(ent, beta(oferta_a, oferta_b))
        ents.append(ent); ofs.append(of)
    p_ent = sum(1 for e in ents if e >= 1) / N
    p_of  = sum(1 for o in ofs if o >= 1) / N
    med_e = st.median(ents); med_o = st.mean(ofs)
    p90 = sorted(ents)[int(N*0.9)]
    print(f"{nome:<14} entrevistas: media {st.mean(ents):.2f}  mediana {med_e:.0f}  p90 {p90}")
    print(f"{'':<14} P(>=1 entrevista) {p_ent*100:5.1f}%   P(>=1 oferta) {p_of*100:5.1f}%   ofertas esperadas {med_o:.2f}")
    return p_ent, p_of

print("=" * 74)
print("CENARIOS DA CAMPANHA  |  base: 148 emails entregues, 12 respostas, 33 portais")
print("=" * 74)
print()
# priors: (resposta->entrevista), (portal->entrevista), (entrevista->oferta), lift do follow-up
pess = rodar("Pessimista",  1, 24,  1, 79,  1, 9,  0.30)   # 4% / 1.25% / 10%
base = rodar("Base",        2, 18,  2, 48,  2, 6,  0.50)   # 10% / 4% / 25%
otim = rodar("Otimista",    3, 12,  3, 27,  3, 4,  0.70)   # 20% / 10% / 43%
print()
print("=" * 74)
print("ALAVANCAS: o que cada esforco extra muda no cenario BASE")
print("=" * 74)

def alavanca(nome, extra_portais=0, extra_emails=0, mult_qualidade=1.0):
    global PORTAIS_CONFIRMADOS, EMAILS_ENTREGUES, SILENCIOSOS
    ofs = 0
    for _ in range(N):
        p_resp = beta(1 + RESPOSTAS_HUMANAS, 1 + SILENCIOSOS)
        novas = binom(FOLLOWUPS, p_resp * 0.5) + binom(extra_emails, p_resp)
        total_resp = RESPOSTAS_HUMANAS + novas
        e1 = binom(total_resp, beta(2, 18) * mult_qualidade)
        e2 = binom(PORTAIS_CONFIRMADOS + extra_portais, beta(2, 48) * mult_qualidade)
        ent = e1 + e2
        if binom(ent, beta(2, 6)) >= 1: ofs += 1
    print(f"{nome:<46} P(>=1 oferta) {ofs/N*100:5.1f}%")

alavanca("nada muda (base)")
alavanca("+10 candidaturas de portal", extra_portais=10)
alavanca("+30 candidaturas de portal", extra_portais=30)
alavanca("+50 estudios novos por email", extra_emails=50)
alavanca("mesmo volume, so vagas com encaixe real (x1.8)", mult_qualidade=1.8)
alavanca("+30 portais E so encaixe real", extra_portais=30, mult_qualidade=1.8)

print()
print("=" * 74)
print("QUANDO O SILENCIO VIRA EVIDENCIA (atualizacao bayesiana da conversao)")
print("=" * 74)
# prior base: resposta -> entrevista ~ Beta(2,18), media 10%
a, b = 2, 18
marcos = [("hoje: 12 respostas, 0 entrevistas", 12),
          ("apos follow-up: ~20 respostas, 0", 20),
          ("em 30 dias: ~30 respostas, 0", 30),
          ("em 60 dias: ~45 respostas, 0", 45)]
for nome, n in marcos:
    pa, pb = a, b + n
    media = pa / (pa + pb)
    print(f"{nome:<40} conversao estimada cai para {media*100:4.1f}%")
