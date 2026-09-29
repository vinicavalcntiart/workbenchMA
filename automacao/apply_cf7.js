// Contact Form 7 (WordPress). Uso:
//   sh hb_run.sh apply_cf7.js <url> <slug> <respostas.json> [--submit]
//
// O CF7 e o formulario proprio mais comum de estudio pequeno. Tres coisas que ele faz e que
// enganam quem so olha a tela:
//  1. O envio e AJAX: a URL nao muda, e a prova de envio e a faixa `.wpcf7-response-output`
//     com a classe do formulario virando `sent`. Esperar troca de pagina da falso negativo.
//  2. O erro dele MENTE sobre a causa: quando o reCAPTCHA v3 reprova a sessao por pontuacao,
//     a mensagem e a generica "There was an error trying to send your message", igual a de
//     campo faltando. Por isso este script imprime, alem da mensagem, a LISTA de campos que o
//     proprio CF7 marcou como invalidos (`.wpcf7-not-valid-tip`): se ela vier VAZIA e a
//     mensagem for de erro, o problema nao e o preenchimento, e a pontuacao.
//  3. Tem `_wpcf7_recaptcha_response` escondido: v3 de pontuacao, que nao desenha desafio.
//     Isso nao e captcha de desafio e nao se burla nada; so se registra o veredito.
//
// O telefone, quando o formulario pedir, vem da variavel de ambiente VINI_TEL. Nunca escrito
// aqui: este repositorio e publico.
const {chromium} = require('playwright');
const fs = require('fs');
const [url, slug, ansFile, flag] = process.argv.slice(2);
const SUBMIT = flag === '--submit';
const D = __dirname;
const A = JSON.parse(fs.readFileSync(ansFile, 'utf8'));
const log = (...a) => console.log('[' + slug + ']', ...a);

(async () => {
  const b = await chromium.launch({headless: false, proxy: {server: 'http://127.0.0.1:18080'}, args: ['--no-sandbox', '--ignore-certificate-errors']});
  const ctx = await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 2200}, acceptDownloads: true,
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36', locale: 'en-US'});
  const p = await ctx.newPage();
  try {
    await p.goto(url, {timeout: 120000, waitUntil: 'domcontentloaded'});
    await p.waitForTimeout(4000);
    for (const t of ['Accept all', 'Accept All', 'Accept', 'Allow all', 'I agree', 'Got it']) {
      const e = await p.$(`button:has-text("${t}"), a:has-text("${t}")`);
      if (e && await e.isVisible().catch(() => false)) { await e.click().catch(() => {}); await p.waitForTimeout(1200); break; }
    }
    await p.waitForSelector('form.wpcf7-form', {timeout: 45000});
    // rolar ate o fim porque varios temas so montam o formulario na rolagem
    for (let i = 0; i < 6; i++) { await p.mouse.wheel(0, 1800); await p.waitForTimeout(400); }

    for (const [name, val] of Object.entries(A.selects || {})) {
      const el = await p.$(`form.wpcf7-form select[name="${name}"]`);
      if (!el) { log('SELECT NAO ACHADO', name); continue; }
      const opts = await el.$$eval('option', os => os.map(o => o.text.trim()));
      const alvo = opts.find(o => new RegExp(val, 'i').test(o));
      if (!alvo) { log('OPCAO NAO ACHADA', name, '| queria', val, '| opcoes', JSON.stringify(opts)); continue; }
      await el.selectOption({label: alvo});
      log('select', name, '=>', alvo);
    }
    for (const [name, val] of Object.entries(A.texto || {})) {
      const el = await p.$(`form.wpcf7-form [name="${name}"]`);
      if (!el) { log('CAMPO NAO ACHADO', name); continue; }
      await el.fill(String(val));
      log('preenchido', name, '=>', String(val).slice(0, 60));
    }
    for (const [name, arq] of Object.entries(A.arquivos || {})) {
      const el = await p.$(`form.wpcf7-form input[type="file"][name="${name}"]`);
      if (!el) { log('CAMPO DE ARQUIVO NAO ACHADO', name); continue; }
      await el.setInputFiles(D + '/' + arq).catch(e => log('falha no anexo', name, e.message.slice(0, 60)));
      log('anexado', name, '=>', arq);
    }
    for (const sel of (A.marcar || [])) {
      const el = await p.$(`form.wpcf7-form ${sel}`);
      if (el) { await el.check({force: true}).catch(() => {}); log('marcado', sel); }
    }

    await p.waitForTimeout(1200);
    await p.screenshot({path: `filled_${slug}.png`, fullPage: true});
    const rb = await p.evaluate(() => [...document.querySelectorAll('form.wpcf7-form [name]')]
      .filter(e => !/^_wpcf7/.test(e.name) && e.type !== 'submit' && e.type !== 'hidden')
      .map(e => [e.name, e.type === 'file' ? (e.files && e.files.length ? e.files[0].name : '(VAZIO)') : (e.value || '(VAZIO)')]));
    for (const [n, v] of rb) log('  leitura de volta', n, '=>', String(v).slice(0, 70));

    if (!SUBMIT) { log('DRY RUN'); await b.close(); return; }

    const sb = await p.$('form.wpcf7-form input[type="submit"]:visible, form.wpcf7-form button[type="submit"]:visible');
    if (!sb) { log('SEM BOTAO DE ENVIO VISIVEL'); await b.close(); return; }
    await sb.click();
    // O CF7 responde por AJAX; 40 s cobre upload de anexo grande.
    for (let i = 0; i < 40; i++) {
      const cls = await p.$eval('form.wpcf7-form', e => e.className).catch(() => '');
      if (/wpcf7-(mail-sent-ok|mail-sent-ng|validation-errors|spam|aborted)/.test(cls)) break;
      await p.waitForTimeout(1000);
    }
    await p.waitForTimeout(2000);
    await p.screenshot({path: `result_${slug}.png`, fullPage: true});
    const cls = await p.$eval('form.wpcf7-form', e => e.className).catch(() => '');
    const msg = (await p.$eval('.wpcf7-response-output', e => e.innerText).catch(() => '')).replace(/\s+/g, ' ');
    const invalidos = await p.$$eval('.wpcf7-not-valid-tip', es => es.map(e => (e.closest('[class*="wpcf7-form-control-wrap"]') || {}).dataset?.name || e.innerText.trim()));
    const ok = /wpcf7-mail-sent-ok/.test(cls);
    log(ok ? 'SUBMITTED OK' : 'NAO ENVIADO', '| classe:', cls, '| mensagem:', msg, '| campos invalidos:', JSON.stringify(invalidos));
    if (!ok && !invalidos.length) log('NENHUM campo foi marcado invalido: isso aponta reprovacao por PONTUACAO do reCAPTCHA v3, nao preenchimento. No navegador do Vini a pontuacao e outra.');
  } catch (e) {
    log('ERR', e.message.split('\n')[0]);
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}).catch(() => {});
  }
  await b.close();
})();
