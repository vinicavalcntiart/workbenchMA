// Despeja os campos de um formulario PROPRIO (nao ATS): nome, tipo, rotulo, obrigatoriedade e
// opcoes de select/radio. Serve para escrever o arquivo de respostas sem adivinhar nada.
// Uso: sh hb_run.sh dump_form.js <url> [seletor-do-botao-que-abre-o-form]
const {chromium}=require('playwright');
const [url,abrir]=process.argv.slice(2);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2200},
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'})).newPage();
 await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'}); await p.waitForTimeout(4000);
 for(const t of ['Accept all','Accept All','Accept','Alle akzeptieren','Akzeptieren','Allow all','Got it','I agree']){
   const e=await p.$(`button:has-text("${t}"), a:has-text("${t}")`); if(e&&await e.isVisible().catch(()=>false)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
 if(abrir){ const e=await p.$(abrir); if(e){ await e.click().catch(()=>{}); await p.waitForTimeout(3000); } }
 for(let i=0;i<10;i++){ await p.mouse.wheel(0,2000); await p.waitForTimeout(500); }
 await p.waitForTimeout(2000);
 const campos=await p.evaluate(()=>{
   const rot=e=>{
     let l='';
     if(e.id){ const x=document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if(x) l=x.innerText.trim(); }
     if(!l&&e.closest('label')) l=e.closest('label').innerText.trim();
     if(!l&&e.getAttribute('placeholder')) l='(placeholder) '+e.getAttribute('placeholder');
     if(!l&&e.getAttribute('aria-label')) l='(aria) '+e.getAttribute('aria-label');
     if(!l&&e.parentElement) l=(e.parentElement.innerText||'').trim().slice(0,80);
     return l.replace(/\s+/g,' ').slice(0,110);
   };
   const out=[];
   document.querySelectorAll('form').forEach((f,fi)=>{
     out.push({form:fi, action:f.getAttribute('action')||'', metodo:f.getAttribute('method')||'', campos:
       [...f.querySelectorAll('input,select,textarea')].map(e=>({
         tag:e.tagName.toLowerCase(), tipo:e.type||'', name:e.name||'', id:e.id||'',
         obrig:e.required||e.getAttribute('aria-required')==='true',
         rotulo:rot(e),
         opcoes:e.tagName==='SELECT'?[...e.options].map(o=>o.text.trim()).slice(0,40):undefined,
         valor:(e.type==='checkbox'||e.type==='radio')?e.value:undefined
       }))});
   });
   return out;
 });
 console.log(JSON.stringify(campos,null,1));
 const t=(await p.evaluate(()=>document.body.innerText)).replace(/\s+/g,' ');
 console.log('--- CAPTCHA? ---', /recaptcha|hcaptcha|turnstile|cf-challenge/i.test(await p.content())?'ha script de captcha no html':'nenhum script de captcha no html (o veredito e o clique)');
 console.log('--- TEXTO (500) ---', t.slice(0,500));
 await p.screenshot({path:'form_dump.png',fullPage:true});
 await b.close();
})();
