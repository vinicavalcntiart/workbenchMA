// Diagnostico: lista TODO botao/link/submit visivel no slide indicado do questionario Connect.
// Nasceu porque o avanco do ultimo slide ("Pitch yourself") devolveu null: a lista de rotulos
// aceitos (next|continue|save|submit|done|finish|skip) nao cobria o rotulo real da casa.
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const HOST=process.argv[2], ROTA=process.argv[3]||'/connect/questions/pitch';
const slug=HOST.split('.')[0];
(async()=>{
 const ctx=await abrirPerfil('/home/user/apply/prof_tt_'+slug,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1280,height:1500},locale:'en-US'});
 const p=ctx.pages()[0]||await ctx.newPage();
 await p.goto('https://'+HOST+ROTA,{timeout:90000,waitUntil:'domcontentloaded'});
 await p.waitForTimeout(4000);
 console.log(JSON.stringify(await p.evaluate(()=>({
   path:location.pathname,
   texto:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,500),
   botoes:[...document.querySelectorAll('button,a,input[type=submit],[role=button]')].map(x=>({
     tag:x.tagName,vis:!!x.offsetParent,txt:((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim().slice(0,50),
     type:x.type||'',cls:(x.className||'').toString().slice(0,60),href:(x.getAttribute('href')||'').slice(0,60),
     form:x.form?(x.form.getAttribute('action')||'')+' '+(x.form.getAttribute('method')||''):''})),
   forms:[...document.querySelectorAll('form')].map(f=>({action:f.getAttribute('action'),method:f.getAttribute('method')}))
 })),null,1));
 await p.screenshot({path:'ttq_bot_'+slug+'.png',fullPage:true}).catch(()=>{});
 await ctx.close();
})();
