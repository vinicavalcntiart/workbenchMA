// Teamtailor CONNECT (banco de talentos), passo 1 do cadastro.
// Escrito em 16/09 porque os modelos antigos (hampa_dep_fix2.js, beffio_ok.js) morreram com
// o conteiner. As armadilhas medidas da lane estao tratadas aqui:
//  1) A CAIXA DE CONSENTIMENTO TEM UM GEMEO ESCONDIDO com o MESMO name (input hidden value=0).
//     querySelector devolve o escondido, o clique nao marca nada e a leitura diz false para
//     sempre. Aqui se usa querySelectorAll + find(type==='checkbox').
//  2) SEM CONSENTIMENTO o formulario NAO cria conta: ele vira LOGIN e devolve a tela mansa
//     "If we find a Connect account, a sign in link will be sent", que parece sucesso e nao e.
//     Por isso o script RECUSA enviar se existir caixa de consentimento e ela nao ficar marcada.
//  3) Cargo e RADIO (candidate[role_id]) e so aparece depois de escolher o departamento; os
//     cargos de outros departamentos ficam no DOM com data-for-department de outro id, e casar
//     por TEXTO sem filtrar por departamento pega o "Artist" do departamento errado.
//  4) Antes de dar por feito, RELE .checked no MESMO input, pelo value, nunca por rotulo.
// Uso: sh hb_run.sh apply_tt_connect.js <url-do-connect> <slug> <departamento> <cargo|-> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador');
const [url,slug,dep,cargo]=process.argv.slice(2);
const SUBMIT=process.argv.includes('ENVIAR');
const EMAIL='contact@vinicavalcanti.art';
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await abrirLocal({headless:false,args:['--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1400},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 p.on('response',async r=>{ if(r.request().method()!=='GET'&&r.status()>=400) log('[rede]',r.status(),r.url().slice(0,110)); });
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(5000);
  for(const t of ['Accept all cookies','Accept all','Accept']){ const e=await p.$(`button[aria-label="${t}"], button:has-text("${t}")`); if(e&&await e.isVisible().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
  // 1) DEPARTAMENTO
  const rdep=await p.evaluate(d=>{
    const n=s=>(s||'').toLowerCase().replace(/\s+/g,' ').trim();
    const ins=[...document.querySelectorAll('input[name="candidate[department_id]"]')];
    const alvo=ins.find(i=>{const l=i.closest('label'); return l&&n(l.innerText)===n(d);}) || ins.find(i=>{const l=i.closest('label'); return l&&n(l.innerText).includes(n(d));});
    if(!alvo) return {erro:'departamento nao achado',opcoes:ins.map(i=>({v:i.value,t:n(i.closest('label')&&i.closest('label').innerText)}))};
    alvo.closest('label').click();
    return {value:alvo.value};
  },dep);
  if(rdep.erro){ log('DEPARTAMENTO:',rdep.erro,JSON.stringify(rdep.opcoes)); await b.close(); return; }
  await p.waitForTimeout(2000);
  const depOk=await p.evaluate(v=>{const i=document.querySelector(`input[name="candidate[department_id]"][value="${v}"]`); return i&&i.checked;},rdep.value);
  log('departamento',dep,'value',rdep.value,'| checked =>',depOk);
  if(!depOk){ log('departamento NAO marcou; parando'); await b.close(); return; }
  // 2) CARGO, filtrado pelo departamento escolhido
  if(cargo && cargo!=='-'){
    const rc=await p.evaluate(([c,depv])=>{
      const n=s=>(s||'').toLowerCase().replace(/\s+/g,' ').trim();
      const ins=[...document.querySelectorAll(`input[name="candidate[role_id]"][data-for-department="${depv}"]`)];
      const alvo=ins.find(i=>{const l=i.closest('label'); return l&&n(l.innerText)===n(c);}) || ins.find(i=>{const l=i.closest('label'); return l&&n(l.innerText).includes(n(c));});
      if(!alvo) return {erro:'cargo nao achado no departamento',opcoes:ins.map(i=>({v:i.value,t:n(i.closest('label')&&i.closest('label').innerText)}))};
      alvo.closest('label').click();
      return {value:alvo.value};
    },[cargo,rdep.value]);
    if(rc.erro){ log('CARGO:',rc.erro,JSON.stringify(rc.opcoes)); await b.close(); return; }
    await p.waitForTimeout(1500);
    const cOk=await p.evaluate(v=>{const i=document.querySelector(`input[name="candidate[role_id]"][value="${v}"]`); return i&&i.checked;},rc.value);
    log('cargo',cargo,'value',rc.value,'| checked =>',cOk);
    if(!cOk){ log('cargo NAO marcou; parando'); await b.close(); return; }
  }
  // 3) CONTINUE
  const cont=await p.$('[data-connect--signup-form-target="departmentsButton"], button[data-action*="signup-form#continue"]');
  if(cont){ await cont.click().catch(()=>{}); await p.waitForTimeout(3000); log('cliquei em continuar'); }
  // 4) EMAIL
  // O seletor generico input.element-to-focus PEGOU UMA CAIXA DE MARCAR na Princess Bento e
  // na Raw Fury (fill num checkbox estoura). Filtra por tipo antes de usar.
  const em=await p.evaluateHandle(()=>{
    const cands=[...document.querySelectorAll('input')].filter(i=>i.type==='email'||(i.type==='text'&&/email/i.test((i.name||'')+' '+(i.id||'')+' '+(i.placeholder||''))));
    if(cands.length) return cands[0];
    const outro=[...document.querySelectorAll('input.element-to-focus')].find(i=>i.type==='email'||i.type==='text');
    return outro||null;
  }).then(h=>h.asElement());
  if(!em){ log('campo de email NAO achado depois do continue'); await p.screenshot({path:'ttc_'+slug+'_semmail.png',fullPage:true}); await b.close(); return; }
  await em.click().catch(()=>{}); await em.fill(EMAIL);
  const lido=await em.inputValue().catch(()=>'');
  log('email lido de volta:',lido);
  if(lido!==EMAIL){ log('email nao bate; parando'); await b.close(); return; }
  // 5) CONSENTIMENTO (armadilha do gemeo escondido)
  const cons=await p.evaluate(()=>{
    const out=[];
    for(const nome of ['candidate[consent_given]','candidate[consent_given_future_jobs]']){
      const todos=[...document.querySelectorAll(`input[name="${nome}"]`)];
      const cb=todos.find(x=>x.type==='checkbox');
      if(!cb){ out.push([nome,'ausente na pagina']); continue; }
      if(!cb.checked){ const l=cb.closest('label'); if(l) l.click(); else cb.click(); }
      out.push([nome, cb.checked?'MARCADA':'NAO MARCOU']);
    }
    return out;
  });
  log('consentimento:',JSON.stringify(cons));
  if(cons.some(([,s])=>s==='NAO MARCOU')){ log('CAIXA EXISTE E NAO MARCOU: isso vira LOGIN em vez de cadastro. PARANDO.'); await b.close(); return; }
  await p.screenshot({path:'ttc_'+slug+'_pre.png',fullPage:true});
  if(!SUBMIT){ log('MODO SECO'); await b.close(); return; }
  const sub=await p.$('[data-connect--form-target="submit"], button[type=submit]');
  if(!sub){ log('botao de envio nao achado'); await b.close(); return; }
  await sub.click().catch(()=>{});
  await p.waitForTimeout(9000);
  const txt=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
  log('URL:',p.url().slice(0,150));
  log('TELA:',txt.slice(0,600));
  if(/if we find a connect account/i.test(txt)) log('ATENCAO: tela de LOGIN, nao de cadastro. Isso NAO e candidatura.');
  await p.screenshot({path:'ttc_'+slug+'_pos.png',fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
