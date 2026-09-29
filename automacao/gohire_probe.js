// Sonda do GoHire, familia de ATS nova para a campanha (achada em 09/09 pela caca de
// agregadores, na Makeshift Software). O curl devolve 200 e ZERO campo: a pagina e casca e o
// formulario so existe depois do clique em "Apply Now". Lembrete do brief: 200 no curl de SPA
// e a casca, nao a porta, e quem da veredito e o clique.
// Uso: sh hb_run.sh gohire_probe.js <url>
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},locale:'en-US',
  userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'});
 const p=await ctx.newPage();
 await p.goto(process.argv[2],{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
 await p.waitForTimeout(6000);

 // MEDIDO EM 09/09: o botao do GoHire nao e <a> nem <button>, e um <div onclick="apply()">,
 // e a funcao apply() chama gohire("open", <id>, "") do widget widget.gohire.io. O formulario
 // abre num IFRAME, entao ler so o frame principal devolve "sem campos" e da falso negativo.
 const bt=p.locator('[onclick*="apply"], a:has-text("Apply Now"), button:has-text("Apply Now")').first();
 if(await bt.count().catch(()=>0)){ await bt.click({force:true}).catch(()=>{}); console.log('cliquei no Apply Now'); }
 await p.waitForTimeout(4000);
 // Se o clique nao abriu nada, chama a funcao do widget direto.
 const idVaga=(process.argv[2].match(/-(\d+)\/?$/)||[])[1];
 if(idVaga) await p.evaluate(id=>{ try{ if(typeof gohire==='function') gohire('open', Number(id), ''); }catch(e){} }, idVaga).catch(()=>{});
 await p.waitForTimeout(9000);
 console.log('URL depois do clique:', p.url());
 for(const f of p.frames()) console.log('  frame:', f.url().slice(0,140));

 // O alvo passa a ser o frame que TEM campo, e nao o principal.
 // O frame principal traz SEIS campos do widget de traducao do Google, todos invisiveis, e
 // um corte por quantidade caia neles antes de chegar no formulario. O criterio certo e o
 // ENDERECO: o formulario do GoHire vive em app.gohire.io/widget/<hash>/<id>.
 let alvo=p.mainFrame();
 for(const f of p.frames()){
   if(/app\.gohire\.io\/widget\//.test(f.url())){ alvo=f; console.log('  frame do formulario:', f.url().slice(0,140)); break; }
 }
 const campos=await alvo.evaluate(()=>{
   const out=[];
   document.querySelectorAll('input,select,textarea').forEach(e=>{
     if(e.type==='hidden') return;
     const id=e.id||e.name||'';
     let lab='';
     if(e.id){ const l=document.querySelector('label[for="'+CSS.escape(e.id)+'"]'); if(l) lab=l.innerText.trim(); }
     if(!lab){ const l=e.closest('label'); if(l) lab=l.innerText.trim(); }
     if(!lab){ const w=e.closest('div,li,fieldset'); if(w) lab=(w.innerText||'').trim().slice(0,90); }
     const r=e.getBoundingClientRect();
     out.push({id, name:e.name, tag:e.tagName, type:e.type, req:e.required, visivel:r.width>0&&r.height>0,
               lab:lab.replace(/\s+/g,' ').slice(0,110),
               opcoes: e.tagName==='SELECT' ? [...e.options].map(o=>o.text.trim()).slice(0,14) : undefined});
   });
   return out;
 });
 campos.forEach(c=>console.log(JSON.stringify(c)));

 // Paredes: so o que esta DE FATO no DOM depois do clique conta.
 const paredes=await alvo.evaluate(()=>({
   recaptcha: !!document.querySelector('.g-recaptcha, iframe[src*="recaptcha"]'),
   hcaptcha:  !!document.querySelector('.h-captcha, iframe[src*="hcaptcha"]'),
   turnstile: !!document.querySelector('iframe[src*="challenges.cloudflare.com"]'),
   forms: document.querySelectorAll('form').length,
 }));
 console.log('PAREDES NO DOM:', JSON.stringify(paredes));
 await p.screenshot({path:'gohire_probe.png',fullPage:true}).catch(()=>{});
 await b.close();
})();
