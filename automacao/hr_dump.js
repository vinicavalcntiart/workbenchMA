// Dump dos campos de um formulario Homerun, aba por aba. O Homerun e AngularJS multi-aba:
// os campos das perguntas so existem no DOM depois de avancar de aba, entao ler a primeira
// tela e concluir "formulario simples" e o erro classico aqui.
// Uso: sh hb_run.sh hr_dump.js <url do /apply>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2400},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:120000});
 await p.waitForTimeout(6000);
 for(const t of ['Accept all','Accept','I agree','Allow all']){
   const e=p.getByRole('button',{name:new RegExp('^'+t+'$','i')}).first();
   if(await e.count().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1200); break; }
 }
 const dump=async(quando)=>{
   const campos=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].map(e=>({
     id:e.id,name:e.name,tipo:e.type,vis:e.offsetParent!==null||e.type==='file',req:e.required,
     rot:((document.querySelector('label[for="'+(e.id||'x').replace(/"/g,'')+'"]')||e.closest('label')||e.closest('.form-group,.question,div')||{}).innerText||'').replace(/\s+/g,' ').trim().slice(0,95)
   })).filter(c=>c.vis||c.tipo==='file'));
   console.log('--- campos', quando, '---');
   campos.forEach(c=>console.log('   ',JSON.stringify(c)));
   const bot=await p.evaluate(()=>[...document.querySelectorAll('button')].filter(e=>e.offsetParent!==null).map(e=>({
     txt:(e.innerText||'').replace(/\s+/g,' ').trim().slice(0,40), cls:(e.className||'').toString().slice(0,55), name:e.name||''})));
   console.log('   BOTOES:',JSON.stringify(bot.slice(0,18)));
 };
 await dump('aba 1');
 for(let i=0;i<4;i++){
   const nx=p.locator('button.tab-control.next:visible').first();
   if(!(await nx.count().catch(()=>0))) break;
   const label=(await nx.innerText().catch(()=>'')).trim();
   if(/verzend|verstuur|submit|send|envoyer|absenden/i.test(label)){ console.log('cheguei no botao de ENVIO ->',label,'(nao clico)'); break; }
   await nx.click().catch(()=>{}); await p.waitForTimeout(3000);
   await dump('aba '+(i+2)+' (depois de "'+label+'")');
 }
 console.log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
 await p.screenshot({path:'hr_dump.png',fullPage:true}).catch(()=>{});
 await b.close();
})().catch(e=>console.log('ERR',e.message));
