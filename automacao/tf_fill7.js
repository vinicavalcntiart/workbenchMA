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
 const feitas=[]; let fimNatural=false; const ULTIMO={n:0}; const PROXIMO={a:null};
 // le o bloco ATIVO (o que contem o activeElement)
 // ARMADILHA 8, e ela substitui todas as heuristicas de foco: cada bloco carrega
 // [data-qa="question-header-counter"] com aria-label "Question N of T". O bloco ATIVO e o
 // de MAIOR N presente no DOM - o mais novo. Isso e imune a janela deslizante, a foco que
 // volta para o body e a pular pergunta opcional (medido as 17h05, quando pular a opcional
 // 13 fez a deteccao por activeElement VOLTAR para o bloco 12, o do upload).
 // O BLOCO ATIVO E O QUE CONTEM document.activeElement (input nas perguntas de texto,
 // FIELDSET nas de escolha). MEDIDO as 17h15, depois de tentar o contador "Question N of T":
 // escolher pelo contador NAO serve, porque o DOM ja traz o bloco SEGUINTE montado como
 // fantasma - com titulo e contador certos, mas com um input em que nem o teclado, nem o
 // clique forcado, nem o setter nativo do React escrevem (leitura de volta vazia nos tres).
 // O contador fica so no log, para conferencia humana.
 const ativo=(ultimoN=0)=>p.evaluate(ultimoN=>{
   const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
   const num=e=>{const c=e.querySelector('[data-qa="question-header-counter"]');
     if(!c) return -1; const m=(c.getAttribute('aria-label')||c.innerText||'').match(/(\d+)/); return m?+m[1]:-1;};
   const ae=document.activeElement;
   let i=bl.findIndex(e=>e.contains(ae));
   if(i<0){ let melhor=Infinity;
     bl.forEach((e,k)=>{const n=num(e); if(n>ultimoN && n<melhor){melhor=n;i=k;}}); }
   if(i<0) i=bl.length-1;
   const e=bl[i]; if(!e) return {vazio:true,total:bl.length};
   const t=e.querySelector('[data-qa^="block-title"]');
   const tipo=(e.getAttribute('data-qa')||'').split(' ')[0].replace('blocktype-','');
   const esc=[...e.querySelectorAll('[role="radio"],[role="checkbox"]')].map(x=>(x.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean);
   const inp=e.querySelector('input:not([type=hidden]), textarea');
   const cnt=e.querySelector('[data-qa="question-header-counter"]');
   const nAtual=num(e);
   return {i,total:bl.length,tipo,n:nAtual,contador:cnt?(cnt.getAttribute('aria-label')||cnt.innerText):'',
           titulo:(t&&t.innerText||'').replace(/\s+/g,' ').trim(),
           escolhas:esc, temCampo:!!inp, focado: !!inp && document.activeElement===inp,
           valor: inp?inp.value:null};
 });
 const escreve=async(i,txt)=>{
   let a=await ativo(ULTIMO.n);
   // ARMADILHA 6, medida às 16h50: DEPOIS DO UPLOAD DE ARQUIVO o foco fica no botão OK e o
   // bloco seguinte ainda está entrando em animação, então uma única tentativa de foco
   // falha. Quatro tentativas, com scroll, focus e clique forçado, cada uma conferida.
   for(let t=0; t<4 && !a.focado; t++){
     await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
       const x=bl[i]&&bl[i].querySelector('input:not([type=hidden]), textarea'); if(x){x.scrollIntoView({block:'center'});x.focus();}},i);
     await p.waitForTimeout(900); a=await ativo(ULTIMO.n);
     if(a.focado) break;
     try{
       const bloco=(await p.$$('[data-qa^="blocktype-"]'))[i];
       const inp=bloco && await bloco.$('input:not([type=hidden]), textarea');
       if(inp) await inp.click({force:true,timeout:5000});
     }catch(e){}
     await p.waitForTimeout(900); a=await ativo(ULTIMO.n);
   }
   if(!a.focado){
     // ULTIMO RECURSO, e ele é legítimo porque a PROVA vem da leitura de volta: o Typeform
     // encaminha o teclado para a pergunta ativa mesmo quando o activeElement é o fieldset
     // ou o botão OK do bloco (é o que acontece logo depois do upload de arquivo).
     await p.keyboard.type(txt,{delay:26}); await p.waitForTimeout(700);
     let cego=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
       const x=bl[i]&&bl[i].querySelector('input:not([type=hidden]), textarea'); return x?x.value:'';},i);
     log('  digitei no cego e li de volta:',JSON.stringify(cego.slice(0,110)));
     if(norm(cego)===norm(txt)) return {ok:true,lido:cego,motivo:'escrita no cego'};
     // ARMADILHA 9: o Typeform e React e o input e CONTROLADO. Quando o teclado nao chega
     // no campo, o jeito que funciona e o setter NATIVO de value mais um evento 'input'
     // que borbulha - e isso que o onChange do React escuta. Mexer em .value direto nao
     // serve: o React sobrescreve na renderizacao seguinte.
     cego=await p.evaluate(([i,txt])=>{
       const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
       const x=bl[i]&&bl[i].querySelector('input:not([type=hidden]), textarea');
       if(!x) return '';
       const proto = x.tagName==='TEXTAREA'?window.HTMLTextAreaElement.prototype:window.HTMLInputElement.prototype;
       const set=Object.getOwnPropertyDescriptor(proto,'value').set;
       set.call(x,txt);
       x.dispatchEvent(new Event('input',{bubbles:true}));
       x.dispatchEvent(new Event('change',{bubbles:true}));
       return x.value;
     },[i,txt]);
     await p.waitForTimeout(700);
     const conf=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
       const x=bl[i]&&bl[i].querySelector('input:not([type=hidden]), textarea'); return x?x.value:'';},i);
     log('  setter nativo + evento input | leitura de volta:',JSON.stringify(conf.slice(0,110)));
     return {ok: norm(conf)===norm(txt), lido:conf, motivo:'foco nao colou; setter nativo do React'};
   }
   await p.keyboard.press('Control+a').catch(()=>{});
   await p.keyboard.type(txt,{delay:26}); await p.waitForTimeout(500);
   const dep=await ativo(ULTIMO.n);
   return {ok: norm(dep.valor||'')===norm(txt), lido:dep.valor};
 };
 // ARMADILHA 10, a mais traicoeira de todas e a que custou seis rodadas: "o titulo mudou"
 // NAO prova que a tela avancou. O DOM traz o bloco SEGUINTE montado como FANTASMA, com
 // titulo e contador certos, e foi isso que me fez achar que o upload de CV tinha avancado
 // para a pergunta 13 quando a tela ainda estava na 12 esperando o OK do arquivo. Prova de
 // avanco que vale: o document.activeElement passa a estar DENTRO de um bloco cujo numero
 // de pergunta e MAIOR que o da pergunta que eu acabei de responder.
 const focoEm=nAtual=>p.evaluate(nAtual=>{
   const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
   const num=e=>{const c=e.querySelector('[data-qa="question-header-counter"]');
     if(!c) return -1; const m=(c.getAttribute('aria-label')||c.innerText||'').match(/(\d+)/); return m?+m[1]:-1;};
   const i=bl.findIndex(e=>e.contains(document.activeElement));
   return {i, n: i>=0?num(bl[i]):-99, avancou: i>=0 && num(bl[i])>nAtual};
 },nAtual);
 const avanca=async(tituloAntes,nAtual)=>{
   await p.waitForTimeout(2200);
   {const f=await focoEm(nAtual); if(f.avancou) return {ok:true,a:await ativo(),auto:true,n:f.n};}
   for(let t=0;t<5;t++){
     await p.keyboard.press('Enter'); await p.waitForTimeout(3200);
     let f=await focoEm(nAtual);
     if(f.avancou) return {ok:true,a:await ativo(),n:f.n};
     if(t===1||t===3){
       const ok=await p.$$('[data-qa^="ok-button-visible"]');
       if(ok.length) await ok[ok.length-1].click({force:true,timeout:6000}).catch(()=>{});
       await p.waitForTimeout(3000);
       f=await focoEm(nAtual);
       if(f.avancou) return {ok:true,a:await ativo(),n:f.n};
     }
     log('   ainda na mesma pergunta (foco no bloco',f.i,'n=',f.n,')');
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
    let a=PROXIMO.a || await ativo(ULTIMO.n); PROXIMO.a=null;
    if(a.vazio||!a.titulo){ log('sem bloco ativo | total',a.total,'| PARANDO'); break; }
    if(a.tipo==='statement'){
      log('passo',passo,'| bloco de TEXTO (statement):',a.titulo.slice(0,60),'| so avanco');
      // o statement nao tem numero de pergunta confiavel (medido: ele devolve o mesmo
      // contador da pergunta 1), entao aqui o Enter vai sem prova de numero e a prova vem
      // da leitura do bloco na volta do laco.
      await p.keyboard.press('Enter'); await p.waitForTimeout(3000);
      await p.keyboard.press('Enter').catch(()=>{}); await p.waitForTimeout(2500);
      const dps=await ativo();
      log('  depois do statement o bloco ativo e:',(dps.titulo||'').slice(0,60),'| tipo',dps.tipo);
      if(dps.tipo==='statement'){ log('  continua no statement | PARANDO'); break; }
      PROXIMO.a=dps;
      continue;
    }
    const t=norm(a.titulo);
    let chave=chaves.filter(k=>!usadas.has(k)).find(k=>t.includes(norm(k)))
           || chaves.filter(k=>!usadas.has(k)).find(k=>norm(k).includes(t)&&t.length>8);
    if(!chave){
      const obrig=/\*/.test(a.titulo);
      log('TITULO SEM RESPOSTA NO DOSSIE:',JSON.stringify(a.titulo),'| tipo',a.tipo,'| obrigatoria:',obrig,'| escolhas',JSON.stringify(a.escolhas));
      if(obrig){ log('PARANDO: e obrigatoria e eu nao chuto resposta'); break; }
      log('OPCIONAL: deixo EM BRANCO (nao chutar) e sigo, para mapear o resto do formulario');
      if(a.n>0) ULTIMO.n=a.n;
      const av0=await avanca(a.titulo, a.n||0);
      log('  pulei a opcional | avancou:',av0.ok,'| agora:',(av0.a.titulo||'').slice(0,60));
      if(av0.ok) PROXIMO.a=av0.a;
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
      if(!e.ok){
        const obrig=/\*/.test(a.titulo);
        log('  NAO CONFIRMOU O TEXTO',e.motivo||'','| obrigatoria:',obrig);
        if(obrig){ log('  PARANDO: obrigatoria sem confirmacao'); break; }
        // ARMADILHA 7: o bloco de tipo "website" da Caribara nao aceita foco nem escrita
        // no cego (quatro modos tentados, leitura de volta vazia nas quatro). Como o campo
        // e OPCIONAL, sigo com ele EM BRANCO e registro - preencher as vinte obrigatorias
        // vale mais que travar numa opcional, e o link do portfolio ja vai no texto de
        // motivacao.
        log('  OPCIONAL: sigo com o campo EM BRANCO e registro a perda');
        if(a.n>0) ULTIMO.n=a.n;
        feitas.push([a.titulo.slice(0,60),'EM BRANCO (campo nao aceitou escrita)']);
        const avb=await avanca(a.titulo, a.n||0);
        log('  pulei a opcional | avancou:',avb.ok,'| agora:',(avb.a.titulo||'').slice(0,60));
        if(avb.ok) PROXIMO.a=avb.a;
        if(!avb.ok){ const s2=await p.$('[data-qa="submit-button"], button:has-text("Submit")');
          if(s2){fimNatural=true;} break; }
        continue;
      }
    }
    if(r.arquivo!==undefined){
      const bloco=(await p.$$('[data-qa^="blocktype-"]'))[a.i];
      const fi=bloco && await bloco.$('input[type=file]');
      if(!fi){ log('  NAO ACHEI input[type=file] no bloco | PARANDO'); break; }
      await fi.setInputFiles(r.arquivo);
      await p.waitForTimeout(6000);
      const nome=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        return (bl[i].innerText||'').replace(/\s+/g,' ').trim().slice(0,220);},a.i);
      log('  arquivo anexado; o bloco agora diz:',JSON.stringify(nome));
      if(!/pdf|Vini/i.test(nome)){ log('  o bloco NAO mostra o arquivo anexado | PARANDO'); break; }
    }
    if(r.digitos!==undefined){
      // ARMADILHA 5, medida às 16h35 no formulário da Caribara: o bloco de DATA tem TRÊS
      // inputs (MM, DD, YYYY pelo "structure" do próprio modelo do formulário) e eles NÃO
      // se encadeiam: digitar "11162026" seguido preenche só o primeiro e o resto cai no
      // chão ("11||" na leitura de volta). Cada input se foca e se preenche separadamente,
      // pelo maxLength de cada um.
      const campos=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        return [...bl[i].querySelectorAll('input:not([type=hidden])')].map((x,k)=>({k,max:x.maxLength>0?x.maxLength:0}));},a.i);
      log('  campos do bloco:',JSON.stringify(campos));
      let resto=r.digitos;
      for(const c of campos){
        if(!resto) break;
        // o ultimo campo leva TODO o resto (o ano tem quatro digitos e o maxLength vem 0)
        const ultimo = (c.k===campos[campos.length-1].k);
        const n = ultimo ? resto.length : (c.max>0?c.max:2);
        const pedaco = resto.slice(0,n); resto = resto.slice(n);
        const ok=await p.evaluate(([i,k])=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
          const x=[...bl[i].querySelectorAll('input:not([type=hidden])')][k];
          if(!x) return false; x.scrollIntoView({block:'center'}); x.focus(); return document.activeElement===x;},[a.i,c.k]);
        if(!ok){ log('  nao consegui focar o campo',c.k,'| PARANDO'); resto='FALHOU'; break; }
        await p.keyboard.type(pedaco,{delay:110});
        await p.waitForTimeout(500);
      }
      if(resto==='FALHOU') break;
      await p.waitForTimeout(600);
      const lido=await p.evaluate(i=>{const bl=[...document.querySelectorAll('[data-qa^="blocktype-"]')];
        return [...bl[i].querySelectorAll('input:not([type=hidden])')].map(x=>x.value).join('|');},a.i);
      log('  digitado',JSON.stringify(r.digitos),'| leitura de volta dos campos:',JSON.stringify(lido));
      const so=(lido.match(/[0-9]/g)||[]).join('');
      const alvo=(r.digitos.match(/[0-9]/g)||[]).join('');
      if(so!==alvo){ log('  OS DIGITOS NA TELA NAO SAO OS QUE EU DIGITEI | PARANDO'); break; }
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
        const ag=await ativo(ULTIMO.n);
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
    if(a.n>0) ULTIMO.n=a.n;
    feitas.push([a.titulo.slice(0,60), r.texto!==undefined?r.texto.slice(0,46):JSON.stringify(r.opcoes)]);
    const av=await avanca(a.titulo, a.n||0);
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
