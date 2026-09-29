// Dump de formulario proprio (Wix, WordPress, Apps Script). Uso: sh hb_run.sh own_dump.js <url>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(9000);
 for(const f of p.frames()){
   const n=await f.evaluate(()=>document.querySelectorAll('input,select,textarea').length).catch(()=>0);
   if(!n) continue;
   console.log('=== frame',f.url().slice(0,90),'| campos',n);
   const c=await f.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].map(e=>({
     id:e.id,name:e.name,tipo:e.type,vis:e.offsetParent!==null||e.type==='file',req:e.required||e.getAttribute('aria-required')==='true',
     ph:e.placeholder||'', al:e.getAttribute('aria-label')||'',
     rot:((document.querySelector('label[for="'+CSS.escape(e.id||'x')+'"]')||e.closest('label')||e.closest('div')||{}).innerText||'').replace(/\s+/g,' ').trim().slice(0,80),
     op:e.tagName==='SELECT'?[...e.options].map(o=>o.text.trim()).slice(0,10):undefined}))).catch(()=>[]);
   c.forEach(x=>console.log('   ',JSON.stringify(x)));
   console.log('   BOTOES:',JSON.stringify(await f.evaluate(()=>[...document.querySelectorAll('button,[role=button],input[type=submit]')].filter(e=>e.offsetParent!==null).map(e=>((e.innerText||e.value)+'').replace(/\s+/g,' ').trim().slice(0,35)).filter(Boolean).slice(0,15)).catch(()=>[])));
 }
 console.log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
 await p.screenshot({path:'own_dump.png',fullPage:true}).catch(()=>{});
 await b.close();
})().catch(e=>console.log('ERR',e.message));
