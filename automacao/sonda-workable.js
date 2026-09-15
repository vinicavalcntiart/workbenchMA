// SONDA WORKABLE PELO NAVEGADOR — a lane Workable e a UNICA da campanha ainda NAO CONFERIDA,
// e o motivo medido em 15/09 e estrangulamento por IP: 429 em controle nas duas pontas, 429 em
// tres requisicoes isoladas com 20s de intervalo, e 429 de novo DUAS HORAS depois. Tudo isso
// foi medido por `curl`.
//
// A PERGUNTA QUE ISTO MEDE, e que ninguem mediu ainda: o 429 e do ENDERECO DE IP ou do CLIENTE?
// Se for do IP, o navegador tambem leva 429 e a lane continua NAO CONFERIDA, com a causa agora
// provada nas duas vias. Se for do cliente (curl sem TLS de Chrome, sem cookie, sem sec-ch-ua),
// o navegador abre e a lane inteira volta para a automacao — e ela importa porque leva portas
// de formulario de verdade (Moonbug, Lighthouse Games, One Of Us) que hoje estao na mao do Vini.
//
// Mede as DUAS vias na MESMA sessao de navegador, que e o que separa medicao de suposicao:
//   (a) a pagina publica do quadro, que e como um humano chega;
//   (b) a API que o proprio quadro chama, feita de dentro da pagina (mesma origem, mesmo cookie).
//
//   cd /home/user/apply && sh hb_run.sh wk_nav.js
const {chromium} = require('playwright');
const ALVOS = ['oneofus', 'lighthousegames', 'moonbug'];
const log = (...a) => console.log('[wk]', ...a);

(async () => {
  const b = await chromium.launch({proxy: {server: 'http://127.0.0.1:18080'},
    args: ['--no-sandbox', '--ignore-certificate-errors']});
  const ctx = await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 1600},
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
    locale: 'en-US'});
  const p = await ctx.newPage();

  for (const slug of ALVOS) {
    const codigos = [];
    const ouvinte = r => { const u = r.url();
      if (/workable\.com/.test(u)) codigos.push(r.status() + ' ' + u.split('?')[0].slice(0, 96)); };
    p.on('response', ouvinte);
    let status = '(sem resposta)';
    try {
      const r = await p.goto('https://apply.workable.com/' + slug + '/',
        {waitUntil: 'domcontentloaded', timeout: 90000});
      status = r ? String(r.status()) : '(nulo)';
    } catch (e) { status = 'ERRO ' + e.message.split('\n')[0].slice(0, 70); }
    // espero CONTEUDO e nunca o relogio: o quadro do Workable e SPA e pinta as vagas depois
    await p.waitForSelector('li[data-ui="job"], [data-ui="job-title"], h1', {timeout: 25000}).catch(() => {});
    const texto = await p.innerText('body').catch(() => '');
    const limpo = texto.replace(/\s+/g, ' ').trim();

    // a API de dentro da pagina: mesma origem, entao leva o cookie que a navegacao acabou de ganhar
    const api = await p.evaluate(async (s) => {
      try {
        const r = await fetch('/api/v1/widget/accounts/' + s + '?details=true',
                              {headers: {'Accept': 'application/json'}});
        const t = (await r.text()).slice(0, 200).replace(/\s+/g, ' ');
        return r.status + ' :: ' + t;
      } catch (e) { return 'ERRO ' + String(e.message).slice(0, 80); }
    }, slug).catch(e => 'ERRO ' + e.message.slice(0, 60));

    const vagas = await p.$$eval('li[data-ui="job"], [data-ui="job-title"]',
      els => els.map(e => (e.innerText || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 12))
      .catch(() => []);

    log('==== ' + slug);
    log('  navegacao HTTP:', status);
    log('  respostas workable:', codigos.slice(0, 5).join(' | ') || '(nenhuma)');
    log('  API de dentro da pagina:', String(api).slice(0, 180));
    log('  vagas lidas na tela:', vagas.length, JSON.stringify(vagas.slice(0, 6)));
    log('  parede visivel?', /too many requests|rate limit|429|verify you are human|cloudflare|attention required/i.test(limpo));
    log('  texto:', limpo.slice(0, 220));
    p.off('response', ouvinte);
    await p.waitForTimeout(3000);
  }
  await b.close();
})();
