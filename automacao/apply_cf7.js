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
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador');
const fs = require('fs');
const [url, slug, ansFile, flag] = process.argv.slice(2);
const SUBMIT = flag === '--submit';
const D = __dirname;
const A = JSON.parse(fs.readFileSync(ansFile, 'utf8'));
const log = (...a) => console.log('[' + slug + ']', ...a);

(async () => {
  const b = await abrirLocal({headless:false});
  const ctx = await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 2200}, acceptDownloads: true,
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36', locale: 'en-US'});
  const p = await ctx.newPage();
  // A MENSAGEM NA TELA NAO DISTINGUE A CAUSA, e o JSON distingue. Medido em 16/09 na Gigantic
  // Duck: o CF7 usa O MESMO texto padrao ("There was an error trying to send your message.
  // Please try again later.") para `spam`, que e o reCAPTCHA v3 reprovando a sessao por
  // pontuacao, e para `mail_failed`, que e o servidor de email DELES falhando. As duas coisas
  // pedem acoes opostas: a primeira o Vini resolve com o navegador dele, a segunda nao se
  // resolve com navegador nenhum porque o formulario esta quebrado para todo mundo. O campo
  // `status` da resposta REST diz qual e, com todas as letras, entao ele e escutado aqui.
  const respostasCF7 = [];
  p.on('response', async r => {
    if (!/contact-form-7\/v1\/contact-forms\/\d+\/feedback/.test(r.url())) return;
    let corpo = '';
    try { corpo = await r.text(); } catch (e) { corpo = '(ilegivel)'; }
    respostasCF7.push({http: r.status(), corpo: corpo.slice(0, 900)});
  });
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

    // 25/09 (Frima): o botao pode ser <button class="wpcf7-submit"> SEM type, que e submit por padrao
    // e nao casa com [type="submit"]; a classe wpcf7-submit e a marca do proprio CF7.
    const sb = await p.$('form.wpcf7-form input[type="submit"]:visible, form.wpcf7-form button[type="submit"]:visible, form.wpcf7-form .wpcf7-submit:visible');
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
    // 21/09 (David Grette, CF7 6.1.7): a classe de sucesso passou a ser so `sent` (sem `wpcf7-mail-sent-ok`),
    // e o script deu FALSO NEGATIVO com o servidor devolvendo status mail_sent e 'Done!'. Veredito agora:
    // status REST mail_sent OU classe mail-sent-ok OU classe `sent` isolada. (Portado da copia de
    // /home/user/apply para esta, a do repositorio, em 25/09: as duas tinham divergido.)
    const restOk = respostasCF7.some(r => /"status"\s*:\s*"mail_sent"/.test(r.corpo));
    const ok = restOk || /wpcf7-mail-sent-ok/.test(cls) || /(^|\s)sent(\s|$)/.test(cls);
    log(ok ? 'SUBMITTED OK' : 'NAO ENVIADO', '| classe:', cls, '| mensagem:', msg, '| campos invalidos:', JSON.stringify(invalidos));
    // O VEREDITO LITERAL. MEDIDO EM 16/09 NA GIGANTIC DUCK: a resposta REST nem sempre e
    // capturada (o tema pode usar admin-ajax), MAS o CF7 carimba o status na CLASSE DO
    // FORMULARIO, e essa classe e tao literal quanto o JSON: `wpcf7-form spam` e `spam` com
    // todas as letras, e nao inferencia. Entao a classe entra como fonte de veredito, ao lado
    // do JSON, e o "NAO CONFERIDO" fica so para quando NENHUM dos dois aparecer.
    const statusClasse = (/wpcf7-form\s+(mail-sent-ok|mail-sent-ng|spam|validation-errors|aborted|unaccepted|payment-required)/.exec(cls) || [])[1] || '';
    if (statusClasse) log('STATUS LITERAL NA CLASSE DO FORMULARIO:', statusClasse);
    if (statusClasse === 'spam') log('   => SPAM: e o reCAPTCHA v3 reprovando a SESSAO por pontuacao, nao o preenchimento. No navegador dele a pontuacao e outra, e a porta vale o clique.');
    if (statusClasse === 'mail-sent-ng') log('   => MAIL-SENT-NG: quem falhou foi o servidor de EMAIL DELES. Navegador nenhum conserta isso, e a rota certa e o email da casa.');
    for (const r of respostasCF7) {
      let st = '(sem status no corpo)';
      try { st = JSON.parse(r.corpo).status || st; } catch (e) {}
      log('RESPOSTA REST DO CF7: HTTP', r.http, '| status literal:', st);
      log('   corpo:', r.corpo.replace(/\s+/g, ' ').slice(0, 300));
      if (st === 'spam') log('   => SPAM: e o reCAPTCHA v3 reprovando a SESSAO por pontuacao. No navegador dele a pontuacao e outra, e a porta vale o clique.');
      if (st === 'mail_failed') log('   => MAIL_FAILED: quem falhou foi o servidor de EMAIL DELES, nao o captcha. Navegador nenhum conserta isso, e a rota certa e o email da casa.');
      if (st === 'validation_failed') log('   => VALIDATION_FAILED: falta campo. A validacao roda ANTES da checagem de spam, entao isto NAO diz nada sobre o captcha.');
    }
    if (!respostasCF7.length) log('NENHUMA resposta REST capturada: este CF7 pode ser antigo (admin-ajax) ou o envio nem saiu. Se a classe trouxe status, ele basta.');
    if (!ok && !invalidos.length && !respostasCF7.length && !statusClasse) log('NEM campo invalido, NEM resposta REST, NEM status na classe: NAO CONFERIDO. Nao conclua pontuacao sem veredito literal.');
  } catch (e) {
    log('ERR', e.message.split('\n')[0]);
    await p.screenshot({path: `err_${slug}.png`, fullPage: true}).catch(() => {});
  }
  await b.close();
})();
