#!/usr/bin/env python3
"""Navegador remoto da campanha (Kernel), SEMPRE em modo stealth.

REGRA DO VINI, 24/09: neste repositorio o navegador do Kernel nasce com stealth ligado e
com o proxy padrao do stealth ligado. Nao existe versao sem stealth e nao se desliga o
proxy. Quem precisar de navegador remoto usa `abrir()` daqui e nunca chama
`Kernel().browsers.create(...)` direto, porque e ai que alguem esquece o stealth.

O QUE O STEALTH FAZ E O QUE NAO FAZ, medido em 24/09 no artstation.com/jobs:
- Passa a checagem de JavaScript do Cloudflare que devolvia 403 ao curl.
- Traz um resolvedor de Turnstile embutido. A telemetria registra 'captcha_solve_result'
  com status 'success' a cada 20 segundos. Se a pagina mostrar "One more step" ou
  "Just a moment", NAO se mexe nela: espera-se com `esperar_desafio()` ate o navegador
  resolver sozinho (regra do Vini, 24/09).
- Nao garante que o Cloudflare aceite a sessao. No ArtStation ele aceitou o token e
  desafiou de novo, em ciclo, e a tela nomeia o IP do proxy. Isso e reputacao de IP,
  nao defeito do solver. Registra-se como 'bloqueado' e segue-se a vida.

CHAVE: vem de KERNEL_API_KEY no ambiente. Nunca no repositorio. Sem a chave, `abrir()`
falha na hora com mensagem clara, em vez de deixar o SDK explodir mais adiante.

USO:
    from navegador_kernel import abrir, esperar_desafio, fechar
    sessao = abrir(nome="caca-artstation", start_url="https://www.artstation.com/jobs")
    # Playwright, se instalado:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(sessao.cdp_ws_url)
        page = browser.contexts[0].pages[0]
        estado = esperar_desafio(page)   # 'livre' ou 'bloqueado'
    fechar(sessao)
"""
import os
import re
import sys
import time

STEALTH = True          # fixo. Nao e parametro de proposito.
TIMEOUT_PADRAO = 300    # segundos de inatividade ate o Kernel derrubar a sessao
ESPERA_DESAFIO = 180    # segundos que se espera o solver antes de dar 'bloqueado'

_DESAFIO = re.compile(r"one more step|just a moment|security check|verify you are human", re.I)


def _cliente():
    if not os.environ.get("KERNEL_API_KEY"):
        sys.exit("navegador_kernel: KERNEL_API_KEY nao esta no ambiente. "
                 "Exporte a chave antes de rodar; ela nunca vai para o repositorio.")
    from kernel import Kernel  # pip install kernel
    return Kernel()


def abrir(nome=None, start_url=None, headless=True, timeout_seconds=TIMEOUT_PADRAO):
    """Cria uma sessao de navegador com stealth ligado. Devolve o objeto da sessao
    (campos uteis: session_id, cdp_ws_url)."""
    extra = {}
    if nome:
        extra["name"] = nome
    if start_url:
        extra["start_url"] = start_url
    return _cliente().browsers.create(
        stealth=STEALTH,
        headless=headless,
        timeout_seconds=timeout_seconds,
        telemetry={"browser": {"captcha": {"enabled": True}}},
        **extra,
    )


def fechar(sessao):
    """Derruba a sessao. Sempre chamar no fim: sessao viva custa e nao serve a ninguem."""
    _cliente().browsers.delete_by_id(sessao.session_id)


def esperar_desafio(page, limite=ESPERA_DESAFIO, passo=5):
    """Espera o desafio do Cloudflare ou Turnstile sumir sozinho. Nao clica em nada.
    Devolve 'livre' se a pagina abriu, 'bloqueado' se estourou o tempo."""
    fim = time.time() + limite
    while time.time() < fim:
        try:
            corpo = page.locator("body").inner_text(timeout=passo * 1000)
        except Exception:
            corpo = ""
        if corpo and not _DESAFIO.search(corpo) and len(corpo) > 200:
            return "livre"
        page.wait_for_timeout(passo * 1000)
    return "bloqueado"


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.artstation.com/jobs"
    s = abrir(nome="teste-stealth", start_url=url)
    print("sessao", s.session_id, "stealth ligado, proxy padrao ligado")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.connect_over_cdp(s.cdp_ws_url)
            page = b.contexts[0].pages[0]
            print(url, "->", esperar_desafio(page))
    finally:
        fechar(s)
