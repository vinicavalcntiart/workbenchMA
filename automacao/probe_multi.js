// sonda varias portas numa sessao so de navegador. uso: node probe_multi.js <url1> <url2> ...
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2200},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-GB'});
 for(const url of process.argv.slice(2)){
  const p=await ctx.newPage();
  console.log('\n===================================\n=== '+url);
  try{
   const r=await p.goto(url,{timeout:90000,waitUntil:'domcontentloaded'});
   console.log('  HTTP',r&&r.status(),'| url final:',p.url().slice(0,120));
   await p.waitForTimeout(7000);
   for(const s of ['button:has-text("Accept")','#onetrust-accept-btn-handler','button:has-text("Agree")']){
     const el=await p.$(s); if(el){ await el.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
   const t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
   console.log('  titulo:',(await p.title().catch(()=>'')).slice(0,90));
   console.log('  texto:',t.slice(0,260));
   const apply=await p.evaluate(()=>[...document.querySelectorAll('a,button')].filter(e=>e.offsetParent!==null&&/apply|postuler|candidat/i.test(e.innerText||'')).map(e=>((e.innerText||'').trim().slice(0,40))+' -> '+(e.href||'(botao)')).slice(0,6));
   console.log('  botoes de candidatura:',JSON.stringify(apply));
   const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null)
     .map(e=>({n:e.name||e.id||'',t:e.type||e.tagName,req:!!(e.required||e.getAttribute('aria-required')==='true'),
       lab:((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,55)})));
   console.log('  campos visiveis:',campos.length);
   campos.slice(0,22).forEach(c=>console.log('    ',JSON.stringify(c)));
   const cap=await p.evaluate(()=>({
     frames:[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(s=>/captcha|challenges|datadome|turnstile/i.test(s)),
     widgets:[...document.querySelectorAll('.g-recaptcha,[data-sitekey],.h-captcha,.cf-turnstile')].length,
     scripts:[...document.querySelectorAll('script')].map(s=>s.src||'').filter(s=>/captcha|turnstile|datadome/i.test(s)).slice(0,3)}));
   console.log('  captcha no HTML (SEM VEREDITO, so o clique da):',JSON.stringify(cap));
  }catch(e){ console.log('  ERRO:',e.message.split('\n')[0]); }
  await p.close();
 }
 await b.close();
})();
