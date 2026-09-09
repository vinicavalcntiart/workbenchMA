// Sonda o oneclick-ui do SmartRecruiters. O sr_apply.js chegou nesta URL e leu tela VAZIA:
// zero campo, zero botao, zero texto. Isso hoje ja apareceu tres vezes (GoHire, Pinpoint,
// Jobvite) e quase sempre significa uma de duas coisas: o formulario vive num IFRAME, ou o
// SPA ainda nao tinha montado quando a leitura aconteceu. Este script separa as duas.
// Uso: sh hb_run.sh sr_one.js <url> <slug>
const {chromium}=require('playwright');
const [URL,SLUG]=process.argv.slice(2);
const log=(...a)=>console.log('['+SLUG+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2400},acceptDownloads:true,
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'})).newPage();
 p.on('response',r=>{ const u=r.url(); if(/api|graphql|oneclick|publication/i.test(u) && r.status()>=400) log('RESP', r.status(), u.slice(0,140)); });
 await p.goto(URL,{timeout:120000,waitUntil:'domcontentloaded'}).catch(e=>log('goto',e.message.split('\n')[0]));
 for(let i=0;i<10;i++){
   await p.waitForTimeout(4000);
   const n=await p.evaluate(()=>document.querySelectorAll('input,select,textarea').length).catch(()=>0);
   const txt=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
   log('tentativa',i,'| campos no frame principal:',n,'| chars de texto:',txt.length,'| url:',p.url().slice(0,120));
   if(n>0||txt.length>200) break;
 }
 for(const t of ['Accept All','Accept all','Accept Cookies','Aceitar','Accept']){
   const e=await p.$(`button:has-text("${t}")`); if(e){ await e.click().catch(()=>{}); log('cookie:',t); await p.waitForTimeout(2000); break; }
 }
 log('FRAMES:');
 for(const f of p.frames()) log('   ', f.url().slice(0,150), '| campos:', await f.evaluate(()=>document.querySelectorAll('input,select,textarea').length).catch(()=>'?'));
 // escolhe o frame com mais campos, mas registra a url, porque o GoHire ensinou que
 // "mais campos" pode ser o frame errado (seis inputs invisiveis do Google Translate)
 let alvo=p.mainFrame(), max=-1;
 for(const f of p.frames()){ const n=await f.evaluate(()=>document.querySelectorAll('input,select,textarea').length).catch(()=>0); if(n>max){max=n;alvo=f;} }
 log('frame escolhido:',alvo.url().slice(0,150),'com',max,'campos');
 const campos=await alvo.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].map(e=>({
   id:e.id,n:e.name,t:e.type,req:e.required||e.getAttribute('aria-required')==='true',vis:e.offsetParent!==null||e.type==='file',
   val:(e.value||'').slice(0,40),
   lab:((document.querySelector('label[for="'+CSS.escape(e.id||'x')+'"]')||e.closest('label')||e.closest('div')||{}).innerText||'').replace(/\s+/g,' ').trim().slice(0,110),
   opts:e.tagName==='SELECT'?[...e.options].map(o=>o.text.trim()).slice(0,12):undefined}))).catch(e=>[{erro:e.message}]);
 campos.forEach(c=>log('  ',JSON.stringify(c)));
 log('botoes:',JSON.stringify(await alvo.evaluate(()=>[...document.querySelectorAll('button,a[role=button],input[type=submit]')].filter(e=>(e.innerText||e.value||'').trim()).map(e=>((e.innerText||e.value)+'').trim().slice(0,40)).slice(0,25)).catch(()=>[])));
 log('TEXTO:',((await alvo.evaluate(()=>document.body.innerText).catch(()=>''))||'').replace(/\s+/g,' ').slice(0,900));
 await p.screenshot({path:'sr_one_'+SLUG+'.png',fullPage:true}).catch(()=>{});
 await b.close();
})().catch(e=>console.log('ERR',e.message));
