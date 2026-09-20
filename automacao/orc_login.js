// ORACLE RECRUITING CLOUD, FASE 1: autenticacao por CODIGO DE USO UNICO no e-mail.
//
// Medido em 20/09 na Virtuos/Black Shamrock (site CX_1, requisicao 2283): a rota /job/<id>/apply
// e 404; quem serve o formulario e /job/<id>, e o botao chama "APPLY NOW". Ele leva a
// /job/<id>/apply/email com TRES campos: primary-email, HONEYPOT chamado "honey-pot" e a caixa
// obrigatoria legal-disclaimer-checkbox. Zero captcha (grecaptcha/hcaptcha/turnstile undefined,
// zero iframe, zero marca no outerHTML).
//
// O HONEYPOT E VISIVEL AO SELETOR e se chama "honey-pot": qualquer varredura cega de
// input[type=text] o preenche e a candidatura morre em silencio. Aqui ele e lido de volta para
// PROVAR que ficou vazio, e o script PARA se nao estiver.
//
// Uso: sh hb_run.sh orc_login.js <url da vaga> <tag>
//      escreva o codigo em /home/user/apply/code_<tag>.txt quando needcode_<tag>.txt aparecer.
const {chromium}=require('playwright'); const fs=require('fs');
const URL=process.argv[2], TAG=process.argv[3]||'orc';
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
const log=(...a)=>console.log('['+TAG+']',...a);
(async()=>{
 const ctx=await chromium.launchPersistentContext('/home/user/apply/prof_oracle_'+TAG,{
   headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   ignoreHTTPSErrors:true,viewport:{width:1400,height:1600},locale:'en-US',
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const p=ctx.pages()[0]||await ctx.newPage();
 const rede=[]; p.on('response',r=>{ if(r.request().method()!=='GET') rede.push(r.status()+' '+r.request().method()+' '+r.url().split('/').slice(-1)[0].slice(0,60)); });
 const tela=async n=>log(n,JSON.stringify(await p.evaluate(()=>({url:location.href.slice(-70),
   txt:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,320),
   campos:[...document.querySelectorAll('input,textarea,select')].filter(e=>!!e.offsetParent).map(e=>({t:e.type||e.tagName,n:e.name||e.id,
     rot:((e.labels&&e.labels[0]&&e.labels[0].innerText)||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,60)})),
   bot:[...document.querySelectorAll('button')].filter(e=>!!e.offsetParent).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim().slice(0,30)).filter(Boolean)})))); 
 try{
  await p.goto(URL,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(8000);
  log('APPLY NOW:',JSON.stringify(await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button,a')].filter(x=>!!x.offsetParent&&/^apply( now)?$/i.test((x.innerText||'').trim()));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim();})));
  await p.waitForTimeout(8000);
  await tela('TELA DE EMAIL');
  const em=await p.$('#primary-email, input[name="primary-email"], input[type=email]');
  if(!em){ log('sem campo de email'); await ctx.close(); return; }
  await em.fill(P.email); await p.waitForTimeout(600);
  // caixa de termos: as tres formas do brief (label irmao, label pai, clique direto)
  log('termos:',JSON.stringify(await p.evaluate(()=>{
    const c=[...document.querySelectorAll('input[type=checkbox]')].filter(x=>!!x.offsetParent);
    const out=[];
    for(const i of c){
      if(!i.checked){ const l=i.id?document.querySelector('label[for="'+i.id+'"]'):null;
        if(l) l.click(); else if(i.closest('label')) i.closest('label').click(); else i.click(); }
      out.push({n:i.name||i.id,marcado:i.checked});
    } return out;})));
  // PROVA de que o honeypot ficou vazio
  const hp=await p.evaluate(()=>{const h=document.querySelector('#honey-pot, input[name="honey-pot"]'); return h?{achado:true,valor:h.value}:{achado:false};});
  log('HONEYPOT:',JSON.stringify(hp));
  if(hp.achado && (hp.valor||'').length){ log('PARANDO: honeypot preenchido'); await ctx.close(); return; }
  log('NEXT:',JSON.stringify(await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button')].filter(x=>!!x.offsetParent&&/^(next|continue)$/i.test((x.innerText||'').trim()));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim();})));
  await p.waitForTimeout(9000);
  await tela('DEPOIS DO NEXT');
  fs.writeFileSync('/home/user/apply/needcode_'+TAG+'.txt',new Date().toISOString());
  log('ESPERANDO code_'+TAG+'.txt (ate 8 min)');
  let codigo=null;
  for(let i=0;i<96;i++){
    const f='/home/user/apply/code_'+TAG+'.txt';
    if(fs.existsSync(f)){ const v=fs.readFileSync(f,'utf8').trim(); if(/^\d{4,10}$/.test(v)){ codigo=v; break; } }
    await p.waitForTimeout(5000);
  }
  if(!codigo){ log('codigo nao chegou'); await p.screenshot({path:'orc_'+TAG+'_semcodigo.png',fullPage:true}).catch(()=>{}); await ctx.close(); return; }
  log('codigo recebido, digitando');
  // ARMADILHA MEDIDA em 20/09: o campo do codigo NAO e um campo, sao SEIS inputs type=number
  // chamados pin-code-1..pin-code-6, um por digito. Escrever o codigo inteiro cai no primeiro
  // e o VERIFY nao avanca, SEM MENSAGEM DE ERRO NENHUMA na tela. Digito a digito, e lido de volta.
  const pins=await p.$$('input[id^="pin-code-"], input[name^="pin-code-"]');
  if(pins.length>=codigo.length){
    for(let i=0;i<codigo.length;i++){ await pins[i].click().catch(()=>{}); await pins[i].fill(codigo[i]).catch(()=>{}); await p.waitForTimeout(150); }
  } else {
    const ci=await p.$('input[type=text]:not([name="honey-pot"]), input[type=tel], input[inputmode=numeric]');
    if(ci) await ci.fill(codigo);
  }
  await p.waitForTimeout(800);
  log('LEITURA DE VOLTA dos digitos:',JSON.stringify(await p.evaluate(()=>
    [...document.querySelectorAll('input[id^="pin-code-"],input[name^="pin-code-"]')].map(x=>x.value).join(''))));
  log('VERIFY:',JSON.stringify(await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button')].filter(x=>!!x.offsetParent&&/^(verify|next|continue|submit|confirm)$/i.test((x.innerText||'').trim()));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim();})));
  await p.waitForTimeout(12000);
  await tela('DEPOIS DO CODIGO');
  await p.screenshot({path:'orc_'+TAG+'_logado.png',fullPage:true}).catch(()=>{});
  log('REDE nao-GET:',JSON.stringify(rede.slice(-14)));
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
})();
