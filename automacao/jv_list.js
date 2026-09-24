// Lista o quadro do Jobvite. Existe porque jobs.jobvite.com devolve 200 e a MESMA casca de SPA
// para /search, /jobs.rss e qualquer outra rota: o curl le 119 KB e enxerga ZERO vaga. Terceira
// familia do dia em que "200 no curl" nao quer dizer "li o quadro" (GoHire e Pinpoint foram as
// outras). Aqui a lista so existe depois do JavaScript rodar.
const {chromium}=require('playwright'); const {abrir}=require('./navegador_kernel');
(async()=>{
 const b=await abrir({nome:'jv_list'}); // stealth sempre ligado (regra do Vini, 24/09)
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},locale:'en-US',
  userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{timeout:120000,waitUntil:'domcontentloaded'}).catch(e=>console.log('goto',e.message.slice(0,60)));
 await p.waitForTimeout(9000);
 const vagas=await p.evaluate(()=>[...document.querySelectorAll('a[href*="/job/"]')].map(a=>({
   t:(a.innerText||'').replace(/\s+/g,' ').trim().slice(0,90),
   loc:((a.closest('tr,li,div')||{}).innerText||'').replace(/\s+/g,' ').trim().slice(0,120),
   u:a.href})).filter(x=>x.t));
 const pat=/character|sculpt|groom|look ?dev|texture|surfacing|modell?er|modeling|3d art|3d gener|environment artist/i;
 console.log('vagas no quadro:',vagas.length);
 vagas.filter(v=>pat.test(v.t)).forEach(v=>console.log(' |',v.t,'|',v.loc.slice(0,70),'|',v.u));
 await b.close();
})();
