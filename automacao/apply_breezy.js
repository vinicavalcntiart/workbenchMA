// apply_breezy.js - candidatura na familia BREEZY (<slug>.breezy.hr/p/<id>/apply)
// Uso: cd /home/user/apply && sh hb_run.sh apply_breezy.js <respostas.json> <slug> [--submit]
//
// POR QUE ESTE ARQUIVO EXISTE (e nao e mais um script solto):
// O BRIEFING registra em 18/09 que "o comando de disparo da FILA-DO-VINI chama apply_breezy.js,
// que NAO EXISTE em /home/user/apply. Quem seguisse a receita ao pe da letra perderia a rodada."
// Duas candidaturas de Breezy sairam pelo apply_own.js (Playdead 06/09, Wonder Works 19/09), e as
// duas pagaram a mesma armadilha da familia, que o apply_own.js NAO resolve:
//
//   O BREEZY PARSEIA O CV E SOBRESCREVE CAMPO JA DIGITADO (medido na Playdead: cSummary digitado
//   com 248 caracteres, lido de volta com 704). O apply_own.js preenche "campos" ANTES de
//   "arquivos", ou seja na ordem exatamente errada. Aqui o ANEXO VAI PRIMEIRO, espera o parse, e
//   so depois os campos sao digitados. E TODO campo e lido de volta depois do parse.
//
// E as outras duas marcas da familia, medidas antes:
//   - hp_7f2b e HONEYPOT da PLATAFORMA (mesmo nome na Playdead e na Wonder Works): fica VAZIO,
//     e este script FALHA ALTO se algo escreveu nele.
//   - prova de envio: POST em app.breezy.hr/api/apply/<id> (204) + URL /apply/submitted +
//     "Application Submitted". Texto de tela NUNCA e o veredito sozinho.
const { chromium } = require('playwright');
const fs = require('fs');
const [ansFile, slug, flag] = process.argv.slice(2);
const SUBMIT = flag === '--submit';
const A = JSON.parse(fs.readFileSync(ansFile, 'utf8'));
const D = __dirname;
const L = (...a) => console.log('[' + slug + ']', ...a);

// O repositorio e publico: valor sensivel nunca entra no JSON de respostas.
const PESSOAL = (() => { try { return JSON.parse(fs.readFileSync(D + '/pessoal.json', 'utf8')); } catch (e) { return {}; } })();
for (const k of Object.keys(A.campos || {})) {
  if (A.campos[k] === '__TEL__') {
    const t = process.env.VINI_TEL || PESSOAL.telefone_internacional;
    if (!t) { console.error('[erro] pede __TEL__ e nao ha telefone'); process.exit(1); }
    A.campos[k] = t;
  }
  if (A.campos[k] === '__ENDERECO__') {
    const e1 = process.env.VINI_END || PESSOAL.endereco1;
    if (!e1) { console.error('[erro] pede __ENDERECO__ e nao ha endereco'); process.exit(1); }
    A.campos[k] = e1;
  }
}

(async () => {
  const b = await chromium.launch({
    headless: false,
    proxy: { server: process.env.APPLY_PROXY || process.env.HTTPS_PROXY },
    args: ['--no-sandbox', '--ignore-certificate-errors'],
  });
  const ctx = await b.newContext({
    ignoreHTTPSErrors: true, viewport: { width: 1400, height: 2400 }, locale: 'en-US',
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
  });
  const p = await ctx.newPage();

  // Licao de 10/09 na Keen: sem tratador de dialogo o Playwright responde CANCELAR e o envio
  // morre sem deixar rasto.
  p.on('dialog', async d => { L('[dialogo]', d.type(), d.message().slice(0, 120)); await d.accept().catch(() => {}); });
  const posts = [];
  p.on('request', r => { if (r.method() === 'POST') { posts.push(r.url()); L('[POST pedido]', r.url().slice(0, 120)); } });
  p.on('requestfailed', r => { if (r.method() === 'POST') L('[POST FALHOU]', r.url().slice(0, 120), r.failure() && r.failure().errorText); });
  p.on('response', async r => {
    if (r.request().method() !== 'POST') return;
    if (/analytics|sentry|gtag|facebook|bugsnag|doubleclick/i.test(r.url())) return;
    let t = ''; try { t = (await r.text()).slice(0, 200); } catch (e) {}
    L('[POST resposta]', r.status(), r.url().slice(0, 110), t.replace(/\s+/g, ' '));
  });
  p.on('framenavigated', f => { if (f === p.mainFrame()) L('[navegou]', f.url().slice(0, 130)); });

  try {
    await p.goto(A.url, { waitUntil: 'domcontentloaded', timeout: 120000 });
    await p.waitForTimeout(7000);
    for (const t of ['Accept', 'Accept All', 'I agree', 'Got it', 'OK']) {
      const e = p.getByRole('button', { name: new RegExp('^' + t + '$', 'i') }).first();
      if (await e.count().catch(() => 0)) { await e.click().catch(() => {}); await p.waitForTimeout(1000); break; }
    }

    // ---------- 1. MEDICAO DO PORTEIRO, antes de qualquer digitacao ----------
    // "sem captcha no HTML" nao basta: o v3 injeta o script depois do carregamento. Aqui se mede
    // o DOM vivo (iframe de anchor/bframe), o objeto global e a chave de site.
    const porteiro = await p.evaluate(() => {
      const ifr = [...document.querySelectorAll('iframe')].map(f => ({ src: (f.src || '').slice(0, 160), h: Math.round(f.getBoundingClientRect().height) }));
      const html = document.documentElement.outerHTML;
      const marca = t => (html.match(new RegExp(t, 'gi')) || []).length;
      return {
        iframes_captcha: ifr.filter(f => /recaptcha|hcaptcha|turnstile|datadome|arkose/i.test(f.src)),
        iframes_total: ifr.length,
        grecaptcha_global: typeof window.grecaptcha,
        hcaptcha_global: typeof window.hcaptcha,
        turnstile_global: typeof window.turnstile,
        marcas: { recaptcha: marca('recaptcha'), hcaptcha: marca('hcaptcha'), turnstile: marca('turnstile'), sitekey: marca('sitekey'), datadome: marca('datadome') },
        scripts_terceiros: [...document.querySelectorAll('script[src]')].map(s => s.src).filter(s => /captcha|challenge|datadome|perimeterx/i.test(s)),
      };
    });
    L('PORTEIRO:', JSON.stringify(porteiro));
    const desafio = porteiro.iframes_captcha.filter(f => f.h > 100);
    if (desafio.length) { L('!! PAREDE DE DESAFIO VISIVEL:', JSON.stringify(desafio), '- nao insisto'); await b.close(); return; }

    // ---------- 2. O ANEXO VEM PRIMEIRO (a armadilha da familia) ----------
    for (const [sel, arq] of Object.entries(A.arquivos || {})) {
      const el = await p.$(sel);
      if (!el) { L('!! nao achei o campo de arquivo', sel); continue; }
      await el.setInputFiles(D + '/' + arq).catch(e => L('falha no anexo', sel, e.message.split('\n')[0]));
      // No Personio o input e LIMPO depois do upload; no Breezy ele fica. Por isso a prova aqui
      // e DUPLA: o input e o pedido de upload na rede.
      const nm = await p.$eval(sel, e => (e.files && e.files.length) ? e.files[0].name + ' ' + e.files[0].size + 'B' : '(ZERO ARQUIVO)').catch(() => '?');
      L('anexo', sel, '=>', nm);
      await p.waitForTimeout(12000); // o parse do CV precisa terminar ANTES de digitar
      const up = posts.filter(u => /upload/i.test(u));
      L('pedidos de upload vistos:', JSON.stringify(up.map(u => u.slice(0, 110))));
    }

    // ---------- 3. SELECTS (com o cardapio impresso, porque rotulo se adivinha errado) ----------
    for (const [sel, alvo] of Object.entries(A.selects || {})) {
      const el = await p.$(sel);
      if (!el) { L('!! select ausente', sel); continue; }
      const opts = await p.$eval(sel, e => [...e.options].map(o => o.text));
      L('select', sel, 'cardapio:', JSON.stringify(opts.slice(0, 40)));
      const re = new RegExp(alvo, 'i');
      const escolha = opts.find(o => re.test(o));
      if (!escolha) { L('!! nenhuma opcao casa', alvo); continue; }
      await el.selectOption({ label: escolha }).catch(() => {});
      L('select', sel, '=>', escolha, '| lido de volta:', await el.inputValue().catch(() => '?'));
    }

    // ---------- 4. CAMPOS DE TEXTO, digitados de verdade ----------
    for (const [sel, v] of Object.entries(A.campos || {})) {
      const el = await p.$(sel);
      if (!el) { L('!! campo ausente', sel); continue; }
      await el.scrollIntoViewIfNeeded().catch(() => {});
      await el.click({ force: true }).catch(() => {});
      await el.fill('').catch(() => {});
      await el.type(String(v), { delay: 2 }).catch(() => {});
      const lido = await el.inputValue().catch(() => '');
      L('campo', sel, lido.length ? '(' + lido.length + ' chars)' : '(NAO ENTROU NADA)');
    }
    for (const sel of (A.marcar || [])) {
      const el = await p.$(sel); if (!el) { L('!! nao achei', sel); continue; }
      await el.check({ force: true }).catch(async () => { await el.click({ force: true }).catch(() => {}); });
      L('marcar', sel, '=>', await p.$eval(sel, e => e.checked).catch(() => '?'));
    }

    // ---------- 5. LEITURA DE VOLTA DE TUDO + HONEYPOT ----------
    await p.waitForTimeout(1500);
    let vazio = false;
    for (const [sel, v] of Object.entries(A.campos || {})) {
      const lido = await p.$eval(sel, e => e.value).catch(() => null);
      if (lido === null || !String(lido).trim()) { L('  LEITURA FINAL', sel, '=>', lido === null ? '(CAMPO SUMIU)' : '(VAZIO)'); vazio = true; continue; }
      const igual = String(lido).trim() === String(v).trim();
      L('  LEITURA FINAL', sel, '=>', String(lido).length, 'chars |', igual ? 'IDENTICO ao que mandei' : 'DIFERENTE (o ATS mexeu): ' + String(lido).slice(0, 90));
    }
    const isca = await p.$eval('input[name^=hp_]', e => ({ name: e.name, val: e.value })).catch(() => null);
    L('honeypot:', JSON.stringify(isca));
    if (isca && isca.val) { L('!! PARE: a isca foi preenchida'); await b.close(); return; }
    await p.screenshot({ path: D + '/bz_' + slug + '_pre.png', fullPage: true }).catch(() => {});
    if (vazio) { L('!! PARE: obrigatorio vazio na leitura final'); await b.close(); return; }
    if (!SUBMIT) { L('MODO SECO: nada enviado.'); await b.close(); return; }

    // ---------- 6. ENVIO, e a prova e do SERVIDOR ----------
    const alvoPost = new RegExp('app\\.breezy\\.hr/api/apply/' + (A.id || ''));
    let provaRede = null;
    p.on('response', r => { if (alvoPost.test(r.url())) provaRede = r.status() + ' ' + r.url(); });
    const sb = await p.$(A.botao_sel || 'button[type=submit], input[type=submit]');
    if (!sb) { L('!! nao achei o botao de envio'); await b.close(); return; }
    await sb.scrollIntoViewIfNeeded().catch(() => {});
    L('botao:', JSON.stringify(await sb.boundingBox().catch(() => null)), '| rotulo:', (await sb.innerText().catch(() => '')).trim().slice(0, 40));
    await sb.click({ force: true }).catch(e => L('clique falhou:', e.message.split('\n')[0]));

    // Licao de 11/09 no Greenhouse: esperar pela PROVA, nunca pelo relogio. Fechar o navegador
    // com o envio em curso mata o pedido.
    let ok = false;
    for (let i = 0; i < 45; i++) {
      await p.waitForTimeout(2000);
      const u = p.url();
      const t = (await p.innerText('body').catch(() => '')).replace(/\s+/g, ' ');
      if (provaRede || /\/apply\/submitted/.test(u) || /Application Submitted|has been submitted successfully/i.test(t)) {
        L('PROVA aos', (i + 1) * 2, 's | rede:', provaRede, '| url:', u);
        L('TEXTO DA TELA:', t.slice(0, 700));
        ok = true; break;
      }
      if (/A response is required|is required/i.test(t) && i > 3) L('aviso de obrigatorio na tela aos', (i + 1) * 2, 's');
    }
    await p.screenshot({ path: D + '/bz_' + slug + '_post.png', fullPage: true }).catch(() => {});
    if (!ok) {
      L('NAO CONFIRMADO. url:', p.url());
      L('TEXTO:', (await p.innerText('body').catch(() => '')).replace(/\s+/g, ' ').slice(0, 1200));
      L('POSTs vistos:', JSON.stringify(posts.map(u => u.slice(0, 110))));
    }
  } catch (e) {
    L('ERR', e.message.split('\n')[0]);
    await p.screenshot({ path: D + '/bz_' + slug + '_err.png', fullPage: true }).catch(() => {});
  }
  await b.close();
})();
