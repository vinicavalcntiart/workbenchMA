// LEITURA DO QUADRO DAYFORCE DA CINESITE / IMAGE ENGINE / L'ATELIER ANIMATION / TRIXTER.
//
// POR QUE ESTE, E POR QUE COM NAVEGADOR. O locatario `cinesite` foi achado em 15/09 as 20h pela
// sonda automacao/sonda-dayforce.sh, e o proprio portal declara a razao social:
// "Cinesite | Image Engine Design | L'Atelier Animation | Trixter" — QUATRO casas num quadro so.
// A Image Engine de Vancouver e hoje item de MAO da campanha, presa na parede de plataforma do
// BambooHR, entao este pode ser um SEGUNDO caminho para a MESMA casa.
//
// O endereco das vagas NAO foi chutado: foi achado lendo o pacote JavaScript do portal (17
// arquivos, 3 MB), depois de 16 chutes de caminho darem 404. E este:
//     POST https://jobs.dayforcehcm.com/api/geo/<locatario>/jobposting/search
// Ele EXISTE — um GET devolve 405 Method Not Allowed, que e metodo errado e nao ausencia — mas
// devolve 403 Forbidden para curl, INCLUSIVE com os cookies do proprio portal. Falta um token
// que so o navegador monta. Por isso a leitura se faz DE DENTRO DA PAGINA, que e o mesmo truque
// que fechou a medicao do Workable hoje de manha.
//
// O QUE ESTE ROTEIRO NAO FAZ: enviar. Ele so LE e imprime. Envio e decisao de outra passada,
// depois da regua de veto no anuncio inteiro e do dedupe no minuto do clique.
//
//   cd /home/user/apply && sh hb_run.sh df_cinesite.js
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador');
const LOC = process.argv[2] || 'cinesite';
const log = (...a) => console.log('[df]', ...a);

(async () => {
  const b = await abrirLocal();
  const ctx = await b.newContext({ignoreHTTPSErrors: true, viewport: {width: 1280, height: 1800},
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',
    locale: 'en-US'});
  const p = await ctx.newPage();

  // escuto TODA resposta da propria API: se a pagina ja faz a busca sozinha, a resposta dela
  // e a fonte mais confiavel que existe, melhor do que eu remontar a chamada na mao.
  const capturas = [];
  p.on('response', async r => {
    const u = r.url();
    if (!/jobposting|\/api\/geo\//i.test(u)) return;
    let corpo = '';
    try { corpo = await r.text(); } catch (e) { corpo = '(ilegivel)'; }
    capturas.push({url: u.slice(0, 110), status: r.status(), tam: corpo.length, corpo});
  });

  try {
    await p.goto('https://jobs.dayforcehcm.com/en-US/' + LOC + '/CANDIDATEPORTAL',
      {waitUntil: 'domcontentloaded', timeout: 120000});
    // espero CONTEUDO e nunca o relogio: o portal e SPA e as vagas so pintam depois da busca
    await p.waitForSelector('a[href*="JobDetails"], [data-automation*="job"], h1, main',
      {timeout: 45000}).catch(() => log('ATENCAO: nada do portal apareceu em 45s'));
    await p.waitForTimeout(6000);
    log('titulo:', (await p.title()).slice(0, 90));
    log('url final:', p.url().slice(0, 110));

    log('respostas da API capturadas durante a carga:', capturas.length);
    for (const c of capturas) log('   ', c.status, c.tam + 'b', c.url);

    // se a pagina nao buscou sozinha, faco a busca DE DENTRO DELA, com a mesma origem e a
    // mesma sessao. O corpo segue o formato que o proprio pacote monta.
    const daPagina = await p.evaluate(async (loc) => {
      const tenta = async (corpo) => {
        try {
          const r = await fetch('/api/geo/' + loc + '/jobposting/search', {
            method: 'POST', headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
            body: JSON.stringify(corpo), credentials: 'include'});
          const t = await r.text();
          return {status: r.status, tam: t.length, amostra: t.slice(0, 3000)};
        } catch (e) { return {status: 'ERRO', amostra: String(e.message).slice(0, 120)}; }
      };
      const corpos = [
        {},
        {careerSiteXRefCode: 'CANDIDATEPORTAL', pageNumber: 1, pageSize: 100},
        {careerSiteXRefCode: 'CANDIDATEPORTAL', cultureId: 'en-US', pageNumber: 1, pageSize: 100,
         keyword: '', locations: [], departments: []},
      ];
      const saida = [];
      for (const c of corpos) saida.push({enviado: JSON.stringify(c).slice(0, 90), ...(await tenta(c))});
      return saida;
    }, LOC).catch(e => [{status: 'ERRO', amostra: e.message.slice(0, 120)}]);

    log('== busca feita de DENTRO da pagina');
    for (const r of daPagina) log('   corpo', r.enviado, '->', r.status, r.tam ? r.tam + 'b' : '',
      String(r.amostra || '').replace(/\s+/g, ' ').slice(0, 260));

    // e o que a TELA mostra, que e a prova mais simples de todas
    const tela = (await p.innerText('body').catch(() => '')).replace(/\s+/g, ' ');
    log('texto da tela:', tela.slice(0, 700));
    const links = await p.$$eval('a[href]', as => as.map(a => a.getAttribute('href'))
      .filter(h => h && /job/i.test(h)).slice(0, 40)).catch(() => []);
    log('links com "job" na pagina:', links.length, JSON.stringify(links.slice(0, 15)));
    await p.screenshot({path: 'df_' + LOC + '.png', fullPage: true}).catch(() => {});
  } catch (e) {
    log('ERRO', e.message.split('\n')[0].slice(0, 160));
    await p.screenshot({path: 'df_err.png', fullPage: true}).catch(() => {});
  }
  await b.close();
})();
