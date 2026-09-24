// Variante do apply_gohire.js para o caso medido em 20/09 na Hidden Acorn: o clique no Submit
// FUNCIONA, o botao entra em SPINNER, e os 14s de espera do script original terminam ANTES da
// resposta chegar. Resultado: log "NAO CONFIRMADA" com a candidatura em voo. Esta variante
// (1) espera pela RESPOSTA do POST /apply em vez de por tempo fixo, e (2) so declara veredito
// depois de o spinner sair.
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador'); const fs=require('fs');
const [url,slug,coverFile]=process.argv.slice(2);
const D=__dirname; const TEL=process.env.VINI_TEL;
const B={first:'Vini',last:'Cavalcanti',email:'contact@vinicavalcanti.art',tel:TEL,cv:D+'/Vini_Cavalcanti_CV.pdf'};
const carta=fs.readFileSync(coverFile,'utf8').trim();
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await abrirLocal({headless:false});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1000},acceptDownloads:true,locale:'en-US',
  userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'});
 const p=await ctx.newPage();
 const respostas=[];
 p.on('response', async r=>{ try{ const u=r.url(); if(r.request().method()!=='GET' && /api\.gohire\.io/.test(u)){
    let body=''; try{ body=(await r.text()).slice(0,300); }catch(_){}
    respostas.push([r.status(),u.slice(0,90),body]); log('[rede]',r.status(),u.slice(0,90),body.slice(0,160)); } }catch(_){} });
 await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'}).catch(()=>{});
 await p.waitForTimeout(6000);
 const bt=p.locator('[onclick*="apply"]').first();
 if(await bt.count().catch(()=>0)) await bt.click({force:true}).catch(()=>{});
 await p.waitForTimeout(9000);
 let f=null; for(const fr of p.frames()) if(/app\.gohire\.io\/widget\//.test(fr.url())) { f=fr; break; }
 if(!f){ log('!! formulario nao abriu'); await b.close(); return; }
 const põe=async(s,v)=>{ const e=await f.$(s); if(e) await e.fill(v).catch(()=>{}); };
 await põe('#first-name',B.first); await põe('#last-name',B.last); await põe('#email',B.email);
 const el=await f.$('#phone'); if(el){ await el.fill(''); await el.type('+55'+B.tel,{delay:60}); await p.waitForTimeout(1500); }
 log('bandeira =>', await f.evaluate(()=>{const e=document.querySelector('.iti__selected-flag .iti__flag');return e?e.className.replace('iti__flag','').trim():'(sem)';}).catch(()=>'?'));
 const an=await f.$('#attach'); if(an) await an.setInputFiles(B.cv).catch(()=>{});
 await p.waitForTimeout(4000);
 for(const t of await f.$$('textarea')){
   const rot=await t.evaluate(e=>{let s='';if(e.id){const l=document.querySelector('label[for="'+CSS.escape(e.id)+'"]');if(l)s=l.innerText;}return (s||e.placeholder||'').trim().slice(0,60);}).catch(()=>'');
   if(/cover|motiva|why|message/i.test(rot)) { await t.fill(carta).catch(()=>{}); log('carta em',JSON.stringify(rot)); }
 }
 await p.waitForTimeout(1500);
 const leitura=await f.evaluate(()=>{const o={};document.querySelectorAll('input:not([type=hidden]),textarea').forEach((e,i)=>{const k=e.id||e.name||('c'+i);o[k]=e.type==='file'?(e.files&&e.files.length?e.files[0].name:'(VAZIO)'):((e.value||'').slice(0,50)||'(VAZIO)');});return o;});
 log('leitura de volta:',JSON.stringify(leitura));
 const env=f.locator('div.gh-widget-btn.primary-btn').filter({hasText:/^\s*Submit\s*$/i}).first();
 await env.scrollIntoViewIfNeeded().catch(()=>{});
 await p.waitForTimeout(600);
 // ESPERAR A RESPOSTA, nao o relogio. Isso e o conserto.
 const espera=p.waitForResponse(r=>/api\.gohire\.io\/apply/.test(r.url()), {timeout:120000}).catch(()=>null);
 await env.click({force:true}).catch(()=>{});
 const r=await espera;
 if(r){ let bd=''; try{bd=(await r.text()).slice(0,400);}catch(_){}
   log('RESPOSTA DO /apply =>', r.status(), bd); }
 else log('!! nenhuma resposta de /apply em 120s');
 await p.waitForTimeout(8000);
 const erros=await f.evaluate(()=>[...document.querySelectorAll('[class*="error" i],[class*="invalid" i]')].map(e=>(e.innerText||'').trim()).filter(Boolean).slice(0,8)).catch(()=>[]);
 if(erros.length) log('erros:',JSON.stringify(erros));
 const txt=(await f.evaluate(()=>document.body.innerText).catch(()=>'')).replace(/\s+/g,' ');
 await p.screenshot({path:D+'/final_'+slug+'.png',fullPage:false}).catch(()=>{});
 log('TEXTO FINAL DO FRAME:', txt.slice(0,400));
 log('RESPOSTAS DE API:', JSON.stringify(respostas.map(x=>[x[0],x[1],x[2].slice(0,120)])));
 await b.close();
})();
