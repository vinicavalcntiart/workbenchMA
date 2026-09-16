// Typeform. A ARMADILHA que barrou 08/09 e que quebrou a minha v1: TODOS os
// [data-qa^="blocktype-"] devolvem getBoundingClientRect().top = 0, porque o
// deslocamento visual mora dentro do bloco. Escolher "o bloco com top mais perto de 0"
// pega SEMPRE O PRIMEIRO, e a resposta cai na pergunta errada (ou em nenhuma).
// O que funciona: os blocos se ACUMULAM no DOM na ordem das perguntas, entao a ativa e a
// de indice = quantas ja foram respondidas. E o Typeform mantem o FOCO no campo da ativa,
// entao texto se digita pelo teclado, nunca clicando (clicar erra de bloco).
// Uso: sh hb_run.sh tf_fill2.js <url> <respostas.json> [ENVIAR]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,ansFile]=process.argv.slice(2); const SUBMIT=process.argv.includes('ENVIAR');
const A=JSON.parse(fs.readFileSync(ansFile,'utf8'));
const ORDEM=A.ordem;
const log=(...a)=>console.log('[tf]',...a);
const norm=s=>(s||'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').replace(/\s+/g,' ').trim();
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:900},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 const feitas=[];
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(8000);
  const st=await p.$('[data-qa="start-button"]'); if(st){ await st.click(); await p.waitForTimeout(4500); }
  const leBloco=async i=>p.evaluate(idx=>{
    const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
    if(idx>=bl.length) return {fim:true,total:bl.length};
    const e=bl[idx];
    const tit=e.querySelector('[data-qa^="block-title"]');
    const tipo=(e.getAttribute('data-qa')||'').split(' ')[0].replace('blocktype-','');
    const esc=[...e.querySelectorAll('[data-qa^="choice"], label')].map(x=>(x.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean);
    return {total:bl.length,tipo,titulo:(tit&&tit.innerText||'').replace(/\s+/g,' ').trim(),escolhas:esc};
  },i);
  for(let idx=0; idx<ORDEM.length; idx++){
    let a=await leBloco(idx);
    for(let e=0; e<6 && a.fim; e++){ await p.waitForTimeout(2500); a=await leBloco(idx); }
    if(a.fim){ log('bloco',idx,'nao apareceu; total no DOM:',a.total); break; }
    const esperada=ORDEM[idx];
    if(!norm(a.titulo).includes(norm(esperada))){
      log('PERGUNTA FORA DE ORDEM. esperava',JSON.stringify(esperada),'e vi',JSON.stringify(a.titulo),'| PARANDO sem responder');
      break;
    }
    const r=A.perguntas[esperada];
    log('idx',idx,'|',a.tipo,'|',a.titulo.slice(0,64));
    if(r.texto!==undefined){
      const fok=await p.evaluate(idx=>{
        const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        const i=bl[idx]&&bl[idx].querySelector('input:not([type=hidden]), textarea');
        if(!i) return 'sem campo';
        if(document.activeElement!==i) i.focus();
        return document.activeElement===i ? 'focado' : 'nao focou';
      },idx);
      if(fok!=='focado'){ log('  foco:',fok,'| PARANDO'); break; }
      await p.keyboard.press('Control+a').catch(()=>{});
      await p.keyboard.type(r.texto,{delay:28});
      await p.waitForTimeout(500);
      const lido=await p.evaluate(idx=>{ const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')]; const i=bl[idx].querySelector('input:not([type=hidden]), textarea'); return i?i.value:''; },idx);
      log('  leitura de volta:',JSON.stringify(lido.slice(0,95)));
      if(norm(lido)!==norm(r.texto)){ log('  NAO BATE, parando'); break; }
    }
    if(r.opcoes){
      for(const alvo of r.opcoes){
        const res=await p.evaluate(([idx,t])=>{
          const n=s=>(s||'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').replace(/\s+/g,' ').trim();
          const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
          const e=bl[idx]; if(!e) return 'sem bloco';
          const c=[...e.querySelectorAll('[data-qa^="choice"], label, [role="checkbox"], [role="radio"]')];
          let hit=c.find(x=>n(x.innerText)===n(t));
          if(!hit) hit=c.find(x=>n(x.innerText).replace(/^[a-z] /,'')===n(t));
          if(!hit) hit=c.find(x=>n(x.innerText).includes(n(t)));
          if(!hit) return 'NAO ACHEI|'+c.map(x=>(x.innerText||'').replace(/\s+/g,' ').trim().slice(0,40)).join(' // ');
          hit.click();
          return 'cliquei|'+(hit.innerText||'').replace(/\s+/g,' ').trim().slice(0,60)+'|aria='+(hit.getAttribute('aria-checked')||hit.getAttribute('data-qa')||'');
        },[idx,alvo]);
        log('  opcao',JSON.stringify(alvo),'=>',res.slice(0,220));
        if(res.startsWith('NAO ACHEI')||res==='sem bloco'){ log('  PARANDO em vez de chutar opcao'); await b.close(); return; }
        await p.waitForTimeout(800);
      }
      if(r.outro){
        const ok=await p.evaluate(([idx,t])=>{
          const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
          const i=bl[idx]&&bl[idx].querySelector('input[type=text], textarea');
          if(!i) return false; i.focus(); return document.activeElement===i;
        },[idx,r.outro]);
        if(ok){ await p.keyboard.type(r.outro,{delay:28}); log('  Other =>',JSON.stringify(r.outro.slice(0,60))); }
        else log('  sem campo Other');
      }
      // confere o que ficou marcado
      const marcado=await p.evaluate(idx=>{
        const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        return [...bl[idx].querySelectorAll('[aria-checked="true"], [data-qa$="-selected"], input:checked')].map(x=>(x.innerText||x.value||'').replace(/\s+/g,' ').trim().slice(0,45));
      },idx);
      log('  MARCADO de fato:',JSON.stringify(marcado));
    }
    feitas.push([a.titulo.slice(0,58), r.texto!==undefined?r.texto.slice(0,48):JSON.stringify(r.opcoes)]);
    const antes=a.total;
    const okb=await p.$$('[data-qa^="ok-button-visible"]');
    if(okb.length) await okb[okb.length-1].click().catch(()=>{}); else await p.keyboard.press('Enter');
    await p.waitForTimeout(3200);
    let dep=await leBloco(idx+1);
    if(dep.fim && idx+1<ORDEM.length){
      await p.keyboard.press('Enter'); await p.waitForTimeout(3200);
      dep=await leBloco(idx+1);
      if(dep.fim){ log('NAO AVANCOU depois de',JSON.stringify(a.titulo.slice(0,60)),'| total no DOM:',dep.total,'| PARANDO'); await p.screenshot({path:'tf_travou.png',fullPage:true}); break; }
    }
  }
  await p.screenshot({path:'tf_final.png',fullPage:true});
  log('FEITAS',feitas.length,':',JSON.stringify(feitas));
  const sub=await p.$('[data-qa="submit-button"], button:has-text("Submit")');
  log('Submit presente:',!!sub);
  if(SUBMIT && sub && feitas.length===ORDEM.length){
    await sub.click().catch(()=>{});
    await p.waitForTimeout(10000);
    log('DEPOIS DO SUBMIT | url:',p.url().slice(0,160));
    log('TEXTO:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,600));
    await p.screenshot({path:'tf_enviado.png',fullPage:true});
  } else if(SUBMIT) log('NAO CLIQUEI: respondidas',feitas.length,'de',ORDEM.length,'| submit presente:',!!sub);
  else log('MODO SECO');
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
