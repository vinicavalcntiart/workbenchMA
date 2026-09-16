// Typeform — QUARTA geração, e a que finalmente casa com o que o DOM faz.
// AS QUATRO ARMADILHAS, todas medidas (as duas últimas em 16/09):
// 1) Todo [data-qa^="blocktype-"] tem getBoundingClientRect().top = 0 (o deslocamento
//    visual mora dentro do bloco), então "o bloco de topo" é sempre o primeiro. (08/09)
// 2) O ok-button e o input do bloco seguinte NÃO são acionáveis pelo Playwright: click
//    estoura 30s de timeout. Quem avança é o Enter do TECLADO. (16/09, 15h20)
// 3) A ordem das perguntas do formulário NÃO é a do array "ordem" do dossiê (o dossiê é
//    de 08/09 e o formulário mudou): casar por POSIÇÃO responde na pergunta errada.
//    Aqui se casa por TÍTULO, e título sem chave no dossiê PARA o script. (16/09, 15h35)
// 4) A ARMADILHA QUE MATOU AS TRÊS TENTATIVAS ANTERIORES: o DOM guarda uma JANELA
//    DESLIZANTE de três blocos e DESCARTA os já respondidos. Depois de responder duas
//    perguntas, o bloco de índice 0 é a pergunta 2 e não a 1. Logo "índice = quantas já
//    foram respondidas" é falso a partir da terceira pergunta, e era por isso que o foco
//    caía em bloco errado e voltava para o body (ativo=-1).
//    O SINAL CERTO E ÚNICO: o bloco ATIVO é o que CONTÉM document.activeElement — input
//    nas perguntas de texto, FIELDSET nas de múltipla escolha.
// Uso: sh hb_run.sh tf_fill7.js <url> <respostas.json> [ENVIAR]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,ansFile]=process.argv.slice(2); const SUBMIT=process.argv.includes('ENVIAR');
const A=JSON.parse(fs.readFileSync(ansFile,'utf8'));
const log=(...a)=>console.log('[tf]',...a);
const norm=s=>(s||'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').replace(/\s+/g,' ').trim();
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:900},
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',locale:'en-US'});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'webdriver',{get:()=>undefined});});
 const p=await ctx.newPage();
 const feitas=[]; let fimNatural=false;
 // le o bloco ATIVO (o que contem o activeElement)
 const ativo=()=>p.evaluate(()=>{
   const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
   const ae=document.activeElement;
   let i=bl.findIndex(e=>e.contains(ae));
   if(i<0) i=bl.length-1;           // sem foco: o ultimo do DOM e o mais novo
   const e=bl[i]; if(!e) return {vazio:true,total:bl.length};
   const t=e.querySelector('[data-qa^="block-title"]');
   const tipo=(e.getAttribute('data-qa')||'').split(' ')[0].replace('blocktype-','');
   const esc=[...e.querySelectorAll('[role="radio"],[role="checkbox"]')].map(x=>(x.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean);
   const inp=e.querySelector('input:not([type=hidden]), textarea');
   const cnt=e.querySelector('[data-qa="question-header-counter"]');
   return {i,total:bl.length,tipo,contador:cnt?(cnt.getAttribute('aria-label')||cnt.innerText):'',
           titulo:(t&&t.innerText||'').replace(/\s+/g,' ').trim(),
           escolhas:esc, temCampo:!!inp, focado: !!inp && document.activeElement===inp,
           valor: inp?inp.value:null};
 });
 const escreve=async(i,txt)=>{
   let a=await ativo();
   if(!a.focado){
     await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
       const x=bl[i]&&bl[i].querySelector('input:not([type=hidden]), textarea'); if(x){x.scrollIntoView({block:'center'});x.focus();}},i);
     await p.waitForTimeout(700); a=await ativo();
   }
   if(!a.focado) return {ok:false,motivo:'campo do bloco ativo nao aceitou foco'};
   await p.keyboard.press('Control+a').catch(()=>{});
   await p.keyboard.type(txt,{delay:26}); await p.waitForTimeout(500);
   const dep=await ativo();
   return {ok: norm(dep.valor||'')===norm(txt), lido:dep.valor};
 };
 const avanca=async tituloAntes=>{
   // o radio de escolha unica do Typeform AVANCA SOZINHO. Apertar Enter antes de conferir
   // pularia a pergunta seguinte sem resposta, que e o erro mais caro que existe aqui.
   await p.waitForTimeout(2000);
   {const a0=await ativo(); if(norm(a0.titulo)!==norm(tituloAntes)) return {ok:true,a:a0,auto:true};}
   for(let t=0;t<4;t++){
     await p.keyboard.press('Enter'); await p.waitForTimeout(3200);
     const a=await ativo();
     if(norm(a.titulo)!==norm(tituloAntes)) return {ok:true,a};
     if(t===1){
       const ok=await p.$$('[data-qa^="ok-button-visible"]');
       if(ok.length) await ok[ok.length-1].click({force:true,timeout:6000}).catch(()=>{});
       await p.waitForTimeout(3000);
       const a2=await ativo(); if(norm(a2.titulo)!==norm(tituloAntes)) return {ok:true,a:a2};
     }
   }
   return {ok:false,a:await ativo()};
 };
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(9000);
  const st0=await p.$('[data-qa="start-button"]');
  if(st0){ await st0.click({force:true,timeout:15000}).catch(()=>{}); await p.waitForTimeout(5000); log('start clicado'); }
  const chaves=Object.keys(A.perguntas); const usadas=new Set();
  for(let passo=0; passo<24; passo++){
    let a=await ativo();
    if(a.vazio||!a.titulo){ log('sem bloco ativo | total',a.total,'| PARANDO'); break; }
    const t=norm(a.titulo);
    let chave=chaves.filter(k=>!usadas.has(k)).find(k=>t.includes(norm(k)))
           || chaves.filter(k=>!usadas.has(k)).find(k=>norm(k).includes(t)&&t.length>8);
    if(!chave){
      const obrig=/\*/.test(a.titulo);
      log('TITULO SEM RESPOSTA NO DOSSIE:',JSON.stringify(a.titulo),'| tipo',a.tipo,'| obrigatoria:',obrig,'| escolhas',JSON.stringify(a.escolhas));
      if(obrig){ log('PARANDO: e obrigatoria e eu nao chuto resposta'); break; }
      log('OPCIONAL: deixo EM BRANCO (nao chutar) e sigo, para mapear o resto do formulario');
      const av0=await avanca(a.titulo);
      log('  pulei a opcional | avancou:',av0.ok,'| agora:',(av0.a.titulo||'').slice(0,60));
      if(!av0.ok){
        const sub0=await p.$('[data-qa="submit-button"], button:has-text("Submit")');
        if(sub0){ fimNatural=true; log('  Submit na tela: fim natural'); }
        break;
      }
      continue;
    }
    usadas.add(chave); const r=A.perguntas[chave];
    log('passo',passo,'| bloco',a.i,'/',a.total,'|',a.contador,'|',a.tipo,'|',a.titulo.slice(0,64),'=> chave',JSON.stringify(chave));
    if(r.texto!==undefined){
      const e=await escreve(a.i,r.texto);
      log('  leitura de volta:',JSON.stringify((e.lido||'').slice(0,110)));
      if(!e.ok){ log('  NAO CONFIRMOU O TEXTO',e.motivo||'','| PARANDO'); break; }
    }
    if(r.opcoes){
      log('  escolhas na tela:',JSON.stringify(a.escolhas));
      for(const alvo of r.opcoes){
        const res=await p.evaluate(([i,t])=>{
          const n=s=>(s||'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').replace(/\s+/g,' ').trim();
          const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')]; const e=bl[i];
          if(!e) return 'sem bloco';
          const c=[...e.querySelectorAll('[role="radio"],[role="checkbox"]')];
          let hit=c.find(x=>n(x.innerText)===n(t)) || c.find(x=>n(x.innerText).replace(/^[a-z] /,'')===n(t)) || c.find(x=>n(x.innerText).includes(n(t)));
          if(!hit) return 'NAO ACHEI|'+c.map(x=>(x.innerText||'').replace(/\s+/g,' ').trim().slice(0,40)).join(' // ');
          hit.click(); return 'cliquei|'+(hit.innerText||'').replace(/\s+/g,' ').trim().slice(0,55);
        },[a.i,alvo]);
        log('  opcao',JSON.stringify(alvo),'=>',res.slice(0,240));
        if(res.startsWith('NAO ACHEI')||res==='sem bloco'){ log('  PARANDO em vez de chutar'); await b.close(); return; }
        await p.waitForTimeout(1200);
        // se a pergunta era de ESCOLHA UNICA disfarçada, o Typeform avança no primeiro
        // clique; continuar clicando marcaria opção na PERGUNTA SEGUINTE. Confere e para.
        const ag=await ativo();
        if(norm(ag.titulo)!==norm(a.titulo)){ log('  a tela JA AVANCOU depois desta opcao (escolha unica): nao marco as demais'); break; }
      }
      if(r.outro){
        const ok=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
          const x=bl[i]&&bl[i].querySelector('input[type=text], textarea'); if(!x) return false; x.focus(); return document.activeElement===x;},a.i);
        if(ok){ await p.keyboard.type(r.outro,{delay:26}); await p.waitForTimeout(400);
          const lido=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
            const x=bl[i].querySelector('input[type=text], textarea'); return x?x.value:'';},a.i);
          log('  Other leitura de volta:',JSON.stringify(lido.slice(0,80)));
        } else log('  sem campo Other (nao chutei)');
      }
      const marcado=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        return [...bl[i].querySelectorAll('[aria-checked="true"], [data-checked="true"], input:checked')].map(x=>(x.innerText||x.value||'').replace(/\s+/g,' ').trim().slice(0,45));},a.i);
      log('  MARCADO de fato:',JSON.stringify(marcado));
      if(!marcado.length) log('  ATENCAO: nada aparece marcado na leitura de volta');
    }
    feitas.push([a.titulo.slice(0,60), r.texto!==undefined?r.texto.slice(0,46):JSON.stringify(r.opcoes)]);
    const av=await avanca(a.titulo);
    log('  avancou:',av.ok,'| agora:',(av.a.titulo||'').slice(0,60));
    if(!av.ok){
      const sub=await p.$('[data-qa="submit-button"], button:has-text("Submit")');
      if(sub){ fimNatural=true; log('  nao ha proxima pergunta e o Submit esta na tela: fim natural'); }
      else { await p.screenshot({path:'tf7_travou.png',fullPage:true}); log('  TRAVOU sem Submit | PARANDO'); }
      break;
    }
  }
  await p.screenshot({path:'tf7_final.png',fullPage:true});
  log('FEITAS',feitas.length,':',JSON.stringify(feitas));
  const sub=await p.$('[data-qa="submit-button"], button:has-text("Submit")');
  log('Submit presente:',!!sub,'| fim natural:',fimNatural);
  if(SUBMIT && sub && fimNatural && feitas.length>=10){
    await sub.click({force:true,timeout:15000}).catch(e=>log('erro submit',e.message.split('\n')[0]));
    await p.waitForTimeout(12000);
    log('DEPOIS DO SUBMIT | url:',p.url().slice(0,180));
    log('TEXTO DO SERVIDOR:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,700));
    await p.screenshot({path:'tf7_enviado.png',fullPage:true});
  } else if(SUBMIT) log('NAO CLIQUEI: feitas',feitas.length,'| submit:',!!sub,'| fim natural:',fimNatural,
      '(a trava do fim natural existe porque na rodada das 16h eu cliquei Submit com a pergunta 18 obrigatoria em branco: o servidor nao aceitou e a tela ficou no formulario, ou seja envio nenhum)');
  else log('MODO SECO');
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await b.close();
})();
