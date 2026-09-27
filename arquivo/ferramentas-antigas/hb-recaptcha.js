// Half Breaks: o board do Greenhouse carrega reCAPTCHA ou nao? Sem enviar nada.
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador');
const urls=process.argv.slice(2);
(async()=>{
 const b=await abrirLocal({headless:false});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1000}});
 for(const u of urls){
  const p=await ctx.newPage(); const hits=[];
  p.on('request',r=>{ if(/recaptcha|hcaptcha|turnstile|datadome/i.test(r.url())) hits.push(r.url().split('?')[0]); });
  await p.goto(u,{timeout:120000,waitUntil:'networkidle'}).catch(()=>{});
  await p.waitForTimeout(4000);
  const dom=await p.evaluate(()=>({g:typeof window.grecaptcha, frames:[...document.querySelectorAll('iframe')].map(f=>f.src).filter(s=>/recaptcha|hcaptcha/i.test(s)).length}));
  console.log(u.replace('https://job-boards.greenhouse.io/','').slice(0,60),'| pedidos antibot:',[...new Set(hits)].length,'| grecaptcha:',dom.g,'| iframes:',dom.frames);
  await p.close();
 }
 await b.close();
})();
