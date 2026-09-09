// Homerun (multi-aba, AngularJS). uso: node apply_homerun.js <respostas.json> <slug> [--submit]
// json: {"url":"...","texto":{"#id":"valor"},"perguntas":{"2372108":"texto"},
//        "simnao":{"2372204":"yes"},"cv":"Vini_Cavalcanti_CV.pdf"}
const { chromium } = require('playwright'); const fs = require('fs');
const [ansFile, slug, flag] = process.argv.slice(2); const SUBMIT = flag === '--submit';
const A = JSON.parse(fs.readFileSync(ansFile)); const D = __dirname;
// O telefone NUNCA fica escrito no arquivo de respostas: o repositorio e PUBLICO e o
// valida-dashboard.sh pegou o numero por extenso num ans_*.json em 09/09. O arquivo traz
// o marcador __TEL__ e o valor vem da variavel VINI_TEL, que mora no doc privado do Drive.
for (const k of Object.keys(A.texto || {})) {
  if (A.texto[k] === '__TEL__') {
    if (!process.env.VINI_TEL) { console.error('[erro] o arquivo pede __TEL__ e falta a variavel VINI_TEL'); process.exit(1); }
    A.texto[k] = process.env.VINI_TEL;
  }
}
const log = (...a) => console.log('[' + slug + ']', ...a);
(async () => {
  const b = await chromium.launch({ headless: false, proxy: { server: 'http://127.0.0.1:18080' }, args: ['--no-sandbox', '--ignore-certificate-errors'] });
  const ctx = await b.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1400, height: 2200 }, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36', locale: 'en-US' });
  const p = await ctx.newPage();
  p.on('response', r => { if (r.request().method() === 'POST') log('[rede]', r.status(), r.url().slice(0, 110)); });
  try {
    await p.goto(A.url, { waitUntil: 'domcontentloaded', timeout: 120000 }); await p.waitForTimeout(5000);
    for (const t of ['Accept all', 'Accept', 'Alles accepteren', 'Accepteren', 'Akkoord', 'I agree']) {
      const e = p.getByRole('button', { name: new RegExp('^' + t + '$', 'i') }).first();
      if (await e.count().catch(() => 0)) { await e.click().catch(() => { }); await p.waitForTimeout(1200); break; }
    }
    const typeInto = async (sel, v) => {
      const e = await p.$(sel); if (!e) { log('NAO ACHEI', sel); return; }
      await e.scrollIntoViewIfNeeded().catch(() => { });
      await e.click({ force: true }).catch(() => { });
      await e.fill('').catch(() => { });
      await p.keyboard.type(String(v), { delay: 4 });
      const lido = await e.inputValue().catch(() => '');
      log('campo', sel, lido.length ? '(' + lido.length + ' chars) ' + lido.slice(0, 60) : '(NAO ENTROU NADA)');
    };
    // CV primeiro (upload por AJAX pode redesenhar)
    if (A.cv) {
      const fi = await p.$('input[type=file]#resume_files, input[type=file]');
      if (fi) { await fi.setInputFiles(D + '/' + A.cv); await p.waitForTimeout(6000); log('CV anexado', A.cv); }
      else log('NAO ACHEI input de arquivo');
    }
    for (const [sel, v] of Object.entries(A.texto || {})) await typeInto(sel, v);
    // ir para a aba de perguntas
    for (let step = 0; step < 4; step++) {
      const nx = p.locator('button.tab-control.next:visible').first();
      if (!(await nx.count().catch(() => 0))) break;
      const label = (await nx.innerText().catch(() => '')).trim();
      // NUNCA clicar no botao de ENVIO dentro do laco de navegacao: na Total Mayhem o
      // "Verzend je sollicitatie" tem a MESMA classe tab-control next dos botoes "Volgende",
      // e em modo seco isso disparou um POST de verdade (voltou 400 so porque faltava o
      // consentimento). Parar aqui e deixar o envio para o bloco --submit.
      if (/verzend|verstuur|submit|send|envoyer|absenden/i.test(label)) { log('cheguei no botao de ENVIO ->', label, '(nao clico aqui)'); break; }
      await nx.click().catch(() => { }); await p.waitForTimeout(2500);
      log('avancei ->', label);
      for (const [qid, v] of Object.entries(A.perguntas || {})) {
        const e = await p.$('#questions-' + qid);
        if (e && await e.isVisible().catch(() => false)) await typeInto('#questions-' + qid, v);
      }
      for (const [qid, val] of Object.entries(A.simnao || {})) {
        const btns = await p.$$('button.answer-button.yes-no[name="questions[' + qid + ']"]');
        for (const btn of btns) {
          const t = ((await btn.innerText().catch(() => '')) || '').trim().toLowerCase();
          const alvo = val === 'yes' ? ['ja', 'yes'] : ['nee', 'no'];
          if (alvo.includes(t)) { await btn.click().catch(() => { }); await p.waitForTimeout(600); log('simnao', qid, '=>', t); break; }
        }
        const sel = await p.$$eval('button.answer-button.yes-no[name="questions[' + qid + ']"]', bs => bs.filter(b => /selected/.test(b.className)).map(b => b.innerText.trim())).catch(() => []);
        log('   conferido', qid, 'selecionado =', JSON.stringify(sel));
      }
    }
    // CONSENTIMENTO. O input real e escondido por CSS e quem aparece na tela e um <i class="checkbox">
    // irmao dele, dentro do <label>. check({force}) marca o input sem o AngularJS ver nada e o envio
    // volta 400. O que funciona e clicar no <i> visivel e CONFERIR o .checked depois.
    const marcaConsent = async () => {
      for (const cb of await p.$$('input[type=checkbox][name=consent]')) {
        if (await cb.evaluate(e => e.checked)) continue;
        const icon = await cb.evaluateHandle(e => e.parentElement && e.parentElement.querySelector('i.checkbox'));
        const el = icon && icon.asElement();
        if (el && await el.isVisible().catch(() => false)) { await el.click().catch(() => { }); await p.waitForTimeout(500); continue; }
        if (await cb.isVisible().catch(() => false)) { await cb.check({ force: true }).catch(() => { }); continue; }
        const id = await cb.getAttribute('id');
        if (id) { const l = await p.$('label[for="' + id + '"]'); if (l && await l.isVisible().catch(() => false)) { await l.click().catch(() => { }); await p.waitForTimeout(500); } }
      }
    };
    await marcaConsent(); await p.waitForTimeout(600); await marcaConsent();
    const marcados = await p.$$eval('input[type=checkbox][name=consent]', cs => cs.map(c => c.checked)).catch(() => []);
    log('consent marcado =', JSON.stringify(marcados));
    // MEDIDO NA USTWO EM 09/09: lista VAZIA nao e o mesmo que caixa DESMARCADA, e o aviso
    // antigo tratava as duas do mesmo jeito. A ustwo simplesmente NAO TEM caixa de
    // consentimento, e o "*** ATENCAO ***" ia fazer uma rodada futura abortar um envio bom.
    // E a mesma familia de defeito de sempre: quando o verificador acusa falha, o primeiro
    // suspeito e o verificador.
    if (!marcados.length) log('nao existe caixa de consentimento neste formulario, entao nao ha o que marcar');
    else if (!marcados.some(Boolean)) log('*** ATENCAO: a caixa de consentimento EXISTE e ficou DESMARCADA, o envio vai voltar 400 ***');
    await p.waitForTimeout(1500);
    await p.screenshot({ path: D + '/hr_' + slug + '_pre.png', fullPage: true });
    log('captura hr_' + slug + '_pre.png');
    const captcha = await p.$$eval('iframe', fs => fs.map(f => f.src).filter(s => /recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(() => []);
    log('captcha iframes:', JSON.stringify(captcha));
    if (!SUBMIT) { log('MODO SECO — nada enviado'); await b.close(); return; }
    const sb = p.locator('button[type=submit]:visible, input[type=submit]:visible').first();
    log('botao envio count', await sb.count().catch(() => 0), 'texto', await sb.innerText().catch(() => ''));
    await sb.click().catch(e => log('falha no clique', e.message.slice(0, 80)));
    await p.waitForTimeout(12000);
    await p.screenshot({ path: D + '/hr_' + slug + '_post.png', fullPage: true });
    const txt = await p.evaluate(() => document.body.innerText.replace(/\n{2,}/g, '\n').slice(0, 2500));
    log('URL final', p.url()); log('TELA:\n' + txt);
  } catch (e) { log('ERRO', e.message.slice(0, 300)); try { await p.screenshot({ path: D + '/hr_' + slug + '_err.png', fullPage: true }); } catch { } }
  await b.close();
})();
