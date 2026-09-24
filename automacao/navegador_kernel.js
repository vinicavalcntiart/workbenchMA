// Navegador remoto da campanha (Kernel), SEMPRE em modo stealth. Versao Node dos
// scripts apply_*.js, *_dump.js e afins. A versao Python e navegador_kernel.py.
//
// REGRA DO VINI, 24/09: todo navegador desta campanha nasce com stealth ligado e com o
// proxy padrao do stealth ligado. Nao existe versao sem stealth, nao se desliga o proxy.
// Nenhum script chama chromium.launch() por conta propria: chama abrir() daqui. O gancho
// de commit (automacao/valida-stealth.sh) recusa qualquer launch fora deste arquivo.
//
// CAPTCHA: se a pagina mostrar "Just a moment", "One more step", Turnstile ou parecido,
// NAO se clica em nada. Chama esperarDesafio(page) e deixa o resolvedor embutido do Kernel
// trabalhar. Se depois de 3 minutos ainda estiver na parede, e reputacao de IP: registra
// 'bloqueado' e segue.
//
// CHAVE: KERNEL_API_KEY no ambiente. Nunca no repositorio.
//
// USO (o corpo dos scripts nao muda: b.newContext(), b.newPage(), b.close() continuam):
//   const {abrir, esperarDesafio} = require('./navegador_kernel');
//   const b = await abrir({nome: 'apply_lever'});
//   ... 
//   await b.close();   // fecha o Playwright E derruba a sessao no Kernel
'use strict';
const {chromium} = require('playwright');

const STEALTH = true;          // fixo. Nao e parametro de proposito.
const API = 'https://api.onkernel.com';
const TIMEOUT_PADRAO = 300;    // s de inatividade ate o Kernel derrubar a sessao
const ESPERA_DESAFIO = 180;    // s que se espera o solver antes de dar 'bloqueado'
const DESAFIO = /one more step|just a moment|security check|security verification|verify you are human/i;

function chave() {
  const k = process.env.KERNEL_API_KEY;
  if (!k) {
    console.error('[navegador_kernel] KERNEL_API_KEY nao esta no ambiente. Exporte a chave antes de rodar; ela nunca vai para o repositorio.');
    process.exit(1);
  }
  return k;
}

async function api(method, path, body) {
  const r = await fetch(API + path, {
    method,
    headers: {Authorization: `Bearer ${chave()}`, 'Content-Type': 'application/json'},
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!r.ok) throw new Error(`[navegador_kernel] Kernel ${method} ${path} -> HTTP ${r.status}: ${(await r.text()).slice(0, 300)}`);
  return r.status === 204 ? null : r.json();
}

// Cria a sessao no Kernel. Stealth sempre ligado, proxy padrao do stealth sempre ligado.
async function criarSessao({nome, startUrl, headless = true, timeoutSeconds = TIMEOUT_PADRAO} = {}) {
  const body = {stealth: STEALTH, headless, timeout_seconds: timeoutSeconds,
                telemetry: {browser: {captcha: {enabled: true}}}};
  if (nome) body.name = `${nome}-${Date.now().toString(36)}`;
  if (startUrl) body.start_url = startUrl;
  return api('POST', '/browsers', body);
}

async function derrubarSessao(sessionId) {
  try { await api('DELETE', `/browsers/${sessionId}`); }
  catch (e) { console.error(String(e.message || e)); }
}

// Liga o Playwright a uma sessao ja criada (pelo Kernel, pelo MCP ou por criarSessao).
// Devolve o Browser do Playwright com close() remendado para tambem derrubar a sessao.
async function conectar(cdpWsUrl, sessionId) {
  const b = await chromium.connectOverCDP(cdpWsUrl);
  const fecharOriginal = b.close.bind(b);
  b.close = async () => {
    try { await fecharOriginal(); } finally { if (sessionId) await derrubarSessao(sessionId); }
  };
  b.kernelSessionId = sessionId || null;
  return b;
}

async function abrir(opts = {}) {
  const s = await criarSessao(opts);
  console.error(`[navegador_kernel] sessao ${s.session_id} stealth ligado, proxy padrao ligado`);
  return conectar(s.cdp_ws_url, s.session_id);
}

// Espera o desafio sumir sozinho. Nao clica. 'livre' ou 'bloqueado'.
async function esperarDesafio(page, limite = ESPERA_DESAFIO, passo = 5) {
  const fim = Date.now() + limite * 1000;
  while (Date.now() < fim) {
    let corpo = '';
    try { corpo = await page.locator('body').innerText({timeout: passo * 1000}); } catch (_) {}
    if (corpo && !DESAFIO.test(corpo) && corpo.length > 200) return 'livre';
    await page.waitForTimeout(passo * 1000);
  }
  return 'bloqueado';
}

module.exports = {abrir, conectar, criarSessao, derrubarSessao, esperarDesafio, STEALTH};

if (require.main === module) {
  (async () => {
    const url = process.argv[2] || 'https://jobs.lever.co/larian';
    const b = await abrir({nome: 'teste-stealth', startUrl: url});
    try {
      const page = b.contexts()[0].pages()[0] || await b.newPage();
      if (!page.url().startsWith('http')) await page.goto(url, {waitUntil: 'domcontentloaded'});
      console.log(url, '->', await esperarDesafio(page), '|', await page.title());
    } finally { await b.close(); }
  })().catch(e => { console.error(e); process.exit(1); });
}
