// LANE NOVA (17/09): GOOGLE FORMS como formulario de candidatura.
// Muitos estudios pequenos de animacao e jogos publicam a candidatura num Google Form
// (forms.gle/... ou docs.google.com/forms/d/e/<id>/viewform). A familia NAO TEM CAPTCHA,
// serve tudo no HTML, e a prova de envio e forte: POST para .../formResponse + a URL final
// virando /formResponse + o texto do servidor "Your response has been recorded".
//
// Uso: cd /home/user/apply && sh hb_run.sh gform_apply.js ans_<casa>.json <slug> [ENVIAR]
//   ensaio (sem ENVIAR): percorre as secoes preenchendo, le de volta cada tela e PARA antes do
//     Submit final. Prints gf_<slug>_seco_p<N>.png
//   com ENVIAR: igual, e no fim clica Submit e registra a prova. Print gf_<slug>_envio.png
//
// ARMADILHAS MEDIDAS, todas do proprio Google Forms:
//  1. Os inputs NAO tem name="entry.N" no DOM. O name so e amarrado por JavaScript no envio.
//     Logo NAO existe seletor por entry id: a unica ancora e o TEXTO do enunciado dentro do
//     div[role=listitem]. Casar por texto normalizado (minuscula, sem espaco duplo).
//  2. O FORMULARIO PODE TER SECOES (page break). A primeira tela mostra so parte das perguntas
//     e o resto aparece depois do botao Next. Medido na Mighty Yeti: 10 de 19 perguntas na tela 1.
//     Preencher so a primeira tela e concluir "pergunta nao achada" e ler o formulario pela metade.
//  3. Pergunta de tipo 7 (GRID de radio) tem VARIAS LINHAS, cada uma obrigatoria por conta
//     propria, e o div[role=listitem] e UM SO para a grade inteira. A linha se acha pelo
//     rotulo dela dentro da grade.
//  4. Radio com opcao "Outro" usa data-value="__other_option__" e, depois do clique, aparece
//     um input[aria-label="Other response"] que tambem precisa ser preenchido.
//  5. O botao Submit e um div[role=button], nunca <button>. Idem Next/Back.
//  6. A GRADE PODE SER DE CHECKBOX e nao de radio, e aparentar a mesma coisa na tela. Medido na
//     Fabrique d'Images: o FB_PUBLIC_LOAD_DATA_ classifica como tipo 7 igual a grade de radio,
//     mas o DOM serve div[role=group] com div[role=checkbox] e data-answer-value, e nao
//     div[role=radiogroup] com div[role=radio]. Procurar so radiogroup devolve "linha nao
//     achada" numa grade que esta ali na tela.
//  7. SECAO POR RESPOSTA: o Google Forms pula secoes conforme a resposta. Na Fabrique d'Images,
//     responder "Remote Only" na primeira tela faz a pergunta de trabalho presencial nunca
//     aparecer, e a resposta preparada para ela fica pendente sem que nada esteja errado.
//     Pendencia no fim NAO e defeito automatico: pode ser secao que a rota nao visitou.
const {chromium}=require('playwright');
const fs=require('fs');
const P=require('./pessoal.json');
// Substituicao de marcador: o ans_<casa>.json pode ir para o repositorio PUBLICO, entao o
// telefone e o endereco NUNCA aparecem nele. Escreva @TEL@, @TELDIG@, @EMAIL@, @PORTFOLIO@,
// @LINKEDIN@, @SITE@, @CIDADE@, @PAIS@ e o script troca pelo valor de pessoal.json, que mora
// fora do repositorio.
const _P=require('./pessoal.json');
const _MAP={'@TEL@':_P.telefone_internacional,'@TELDIG@':_P.telefone_digitos,'@EMAIL@':_P.email,'@PORTFOLIO@':_P.portfolio,'@LINKEDIN@':_P.linkedin,'@SITE@':_P.site,'@CIDADE@':_P.cidade,'@PAIS@':_P.pais};
const _troca=o=>{ if(typeof o==='string'){ let s=o; for(const k in _MAP) s=s.split(k).join(_MAP[k]); return s; }
  if(Array.isArray(o)) return o.map(_troca);
  if(o&&typeof o==='object'){ const r={}; for(const k in o) r[k]=_troca(o[k]); return r; }
  return o; };
const ANS=_troca(JSON.parse(fs.readFileSync(process.argv[2],'utf8')));
const SLUG=process.argv[3]||'casa';
const ENVIAR=(process.argv[4]||'')==='ENVIAR';
const L=(...a)=>console.log('[gform:'+SLUG+']',...a);

(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'});
 const p=await ctx.newPage();
 p.on('dialog',async d=>{ L('[dialogo]',d.type(),d.message()); await d.accept().catch(()=>{}); });
 const reqs=[],falhas=[],resps=[];
 p.on('request',r=>{ if(r.method()!=='GET') reqs.push([r.method(),r.url()]); });
 p.on('requestfailed',r=>falhas.push([r.method(),r.url(),(r.failure()||{}).errorText]));
 p.on('response',r=>{ if(r.request().method()!=='GET') resps.push([r.status(),r.url()]); });
 p.on('framenavigated',f=>{ if(f===p.mainFrame()) L('[nav]',f.url()); });

 await p.goto(ANS.url,{timeout:120000,waitUntil:'domcontentloaded'});
 await p.waitForTimeout(3500);
 // ARMADILHA: forms.gle redireciona para docs.google.com e o redirect pode chegar TARDE,
 // destruindo o contexto no meio do preenchimento. Esperar a URL parar de mudar.
 for(let k=0,u=p.url();k<8;k++){ await p.waitForTimeout(1200); if(p.url()===u) break; u=p.url(); }
 L('URL inicial:',p.url());
 L('titulo:',await p.title());
 if(/closedform/i.test(p.url())){ L('!! FORMULARIO FECHADO pelo Google (closedform). Nada a fazer.'); await b.close(); return; }

 const acharLi=async alvo=>{
   const idx=await p.evaluate(a=>{
     const n=s=>(s||'').toLowerCase().replace(/\s+/g,' ').trim();
     const lis=[...document.querySelectorAll('div[role=listitem]')];
     let i=lis.findIndex(li=>{ const h=li.querySelector('div[role=heading]');
       return n((h?h.innerText:li.innerText).split('\n')[0])===n(a); });
     if(i<0) i=lis.findIndex(li=>{ const h=li.querySelector('div[role=heading]');
       return n((h?h.innerText:li.innerText)).includes(n(a)); });
     return i;
   },alvo);
   if(idx<0) return null;
   return (await p.$$('div[role=listitem]'))[idx];
 };
 // ARMADILHA MEDIDA NA JUMBLA: o Google Forms pode NAVEGAR sozinho no meio do preenchimento
 // (o forms.gle resolve para docs.google.com com ?usp=send_form e a pagina se recarrega), e
 // qualquer page.evaluate em curso morre com "Execution context was destroyed". Isso NAO e
 // defeito do formulario: e so esperar a pagina assentar e refazer a busca.
 const acharLiR=async alvo=>{
   for(let k=0;k<3;k++){
     try{ return await acharLi(alvo); }
     catch(e){ L('[renav] contexto destruido procurando',alvo.slice(0,30),'- esperando e refazendo'); await p.waitForTimeout(3000); }
   }
   return null;
 };

 const pendentes={texto:{...(ANS.texto||{})},radio:{...(ANS.radio||{})},dropdown:{...(ANS.dropdown||{})},grid:{...(ANS.grid||{})},checkbox:{...(ANS.checkbox||{})}};
 const todasVoltas=[];
 let pagina=0;

 while(true){
  pagina++;
  const mapa=await p.evaluate(()=>{
    const out=[];
    document.querySelectorAll('div[role=listitem]').forEach((li,idx)=>{
      const h=li.querySelector('div[role=heading]');
      const txt=((h?h.innerText:li.innerText)||'').split('\n')[0];
      const t=[];
      if(li.querySelector('textarea')) t.push('paragrafo');
      else if(li.querySelector('input.whsOnd')) t.push('texto');
      const rg=li.querySelectorAll('div[role=radiogroup]').length;
      if(rg===1) t.push('radio'); else if(rg>1) t.push('grid:'+rg);
      if(li.querySelector('div[role=listbox]')) t.push('dropdown');
      if(li.querySelectorAll('div[role=checkbox]').length) t.push('checkbox');
      out.push([idx,txt,t.join('+')]);
    });
    return out;
  });
  L(`--- TELA ${pagina}: ${mapa.length} perguntas`);
  mapa.forEach(m=>L('   #'+m[0],'['+m[2]+']',JSON.stringify((m[1]||'').slice(0,72))));

  if(pagina===1 && ANS.email!==false){
    const em=await p.$('input[type=email][aria-label="Your email"], input[type=email]');
    if(em){ await em.click({timeout:8000}).catch(()=>{}); await em.fill(''); await em.type(ANS.email||P.email,{delay:12}); L('email do cabecalho preenchido'); }
  }

  for(const [q,v] of Object.entries(pendentes.texto)){
    const li=await acharLiR(q); if(!li) continue;
    await li.scrollIntoViewIfNeeded().catch(()=>{});
    const e=await li.$('textarea')||await li.$('input.whsOnd');
    if(!e){ L('!! sem campo dentro de:',q); continue; }
    await e.click({timeout:10000}).catch(()=>{});
    await e.fill('').catch(()=>{});
    await e.type(String(v),{delay:5});
    L('texto ok:',q.slice(0,48)); delete pendentes.texto[q];
  }
  for(const [q,v] of Object.entries(pendentes.radio)){
    const li=await acharLiR(q); if(!li) continue;
    await li.scrollIntoViewIfNeeded().catch(()=>{});
    let alvo=v,outro=null;
    if(typeof v==='object'){ alvo=v.valor||'__other_option__'; outro=v.outro; }
    const r=await li.$(`div[role=radio][data-value="${alvo}"]`);
    if(!r){ L('!! opcao nao achada:',q,'->',alvo); continue; }
    await r.click({timeout:10000}).catch(async()=>{ await r.evaluate(x=>x.click()); });
    await p.waitForTimeout(350);
    if(outro!=null){
      const oi=await li.$('input[aria-label="Other response"], input.Hvn9fb');
      if(oi){ await oi.click({timeout:8000}).catch(()=>{}); await oi.fill(''); await oi.type(String(outro),{delay:10}); }
      else L('!! campo Other response nao apareceu em:',q);
    }
    L('radio ok:',q.slice(0,48),'->',outro!=null?('Outro: '+outro):alvo); delete pendentes.radio[q];
  }
  for(const [q,v] of Object.entries(pendentes.dropdown||{})){
    const li=await acharLiR(q); if(!li) continue;
    await li.scrollIntoViewIfNeeded().catch(()=>{});
    const lb=await li.$('div[role=listbox]');
    if(!lb){ L('!! sem listbox em:',q); continue; }
    await lb.click({timeout:10000}).catch(async()=>{ await lb.evaluate(x=>x.click()); });
    await p.waitForTimeout(700);
    // o popup de opcoes fica DENTRO do proprio listbox; escopo obrigatorio para nao
    // pegar a lista de outro dropdown da mesma tela
    const op=await lb.$(`div[role=option][data-value="${v}"]`);
    if(!op){ L('!! opcao de dropdown nao achada:',q,'->',v); await p.keyboard.press('Escape').catch(()=>{}); continue; }
    await op.click({timeout:10000}).catch(async()=>{ await op.evaluate(x=>x.click()); });
    await p.waitForTimeout(400);
    L('dropdown ok:',q.slice(0,48),'->',v); delete pendentes.dropdown[q];
  }
  for(const [q,linhas] of Object.entries(pendentes.grid)){
    const li=await acharLiR(q); if(!li) continue;
    await li.scrollIntoViewIfNeeded().catch(()=>{});
    let feitas=0;
    for(const [rot,op] of Object.entries(linhas)){
      const r=await li.evaluate((el,[rot,op])=>{
        const n=s=>(s||'').toLowerCase().replace(/\s+/g,' ').trim();
        const grupos=[...el.querySelectorAll('div[role=radiogroup], div[role=group]')];
        for(const g of grupos){
          // ARMADILHA DE ROTULO (custou tres ensaios na Fabrique d'Images): o div[role=group] da
          // linha pode NAO ter aria-label. Nesse caso o rotulo e a PRIMEIRA LINHA do innerText do
          // PROPRIO grupo; subir para o pai pega a pergunta inteira ou a fila de colunas
          // (Junior Mid Expert) e nenhuma linha casa nunca.
          let lab=g.getAttribute('aria-label')||'';
          if(!n(lab)) lab=((g.innerText||'').split('\n')[0])||'';
          if(!n(lab)){ let s=g.parentElement;
            for(let k=0;k<3&&s;k++,s=s.parentElement){ if(n(s.innerText)){ lab=s.innerText.split('\n')[0]; break; } } }
          if(!n(lab).includes(n(rot))) continue;
          const cand=[...g.querySelectorAll('div[role=radio], div[role=checkbox]')];
          const c=cand.find(x=>n(x.getAttribute('data-value'))===n(op))
                ||cand.find(x=>n(x.getAttribute('data-answer-value'))===n(op))
                ||cand.find(x=>n(x.getAttribute('aria-label')).includes(n(op)));
          if(!c) return 'opcao-nao-achada';
          c.click(); return 'ok';
        }
        const amostra=[...el.querySelectorAll('div[role=checkbox], div[role=radio]')].slice(0,6)
          .map(x=>'al='+JSON.stringify(x.getAttribute('aria-label'))+' dv='+JSON.stringify(x.getAttribute('data-value'))+' dav='+JSON.stringify(x.getAttribute('data-answer-value')));
        const rots=grupos.map(g=>JSON.stringify(g.getAttribute('aria-label')||(g.innerText||'').split('\n')[0]));
        return 'linha-nao-achada | grupos='+grupos.length+' rotulos='+rots.join(', ')+' | celulas: '+amostra.join(' ;; ');
      },[rot,op]);
      if(r==='ok') feitas++;
      L('   grade',q.slice(0,26),'/',rot.slice(0,32),'->',op,'=',r);
      await p.waitForTimeout(160);
    }
    if(feitas) delete pendentes.grid[q];
  }
  for(const [q,ops] of Object.entries(pendentes.checkbox)){
    const li=await acharLiR(q); if(!li) continue;
    for(const op of ops){
      const c=await li.$(`div[role=checkbox][data-answer-value="${op}"], div[role=checkbox][aria-label="${op}"]`);
      if(!c){ L('!! opcao de checkbox nao achada:',q,op); continue; }
      await c.click({timeout:8000}).catch(()=>{});
    }
    L('checkbox ok:',q.slice(0,48)); delete pendentes.checkbox[q];
  }

  await p.waitForTimeout(500);
  const volta=await p.evaluate(()=>{
    const out=[];
    const cab=document.querySelector('input[type=email]');
    if(cab&&cab.value) out.push(['(email)','texto',cab.value]);
    document.querySelectorAll('div[role=listitem]').forEach(li=>{
      const h=li.querySelector('div[role=heading]');
      const q=((h?h.innerText:li.innerText)||'').split('\n')[0].slice(0,52);
      const t=li.querySelector('textarea'), i=li.querySelector('input.whsOnd');
      if(t) out.push([q,'paragrafo',(t.value||'').slice(0,70)+((t.value||'').length>70?'...('+t.value.length+')':'')]);
      else if(i) out.push([q,'texto',i.value]);
      const g=li.querySelectorAll('div[role=radiogroup]').length||li.querySelectorAll('div[role=checkbox]').length;
      if(g){ const mk=[...li.querySelectorAll('div[role=radio][aria-checked=true],div[role=checkbox][aria-checked=true]')].map(x=>x.getAttribute('aria-label')||x.getAttribute('data-value')||x.getAttribute('data-answer-value'));
        out.push([q,`radio/grid ${mk.length}/${g}`,mk.join(' ;; ').slice(0,400)]); }
      const o=li.querySelector('input[aria-label="Other response"]');
      if(o&&o.value) out.push([q,'outro',o.value]);
    });
    return out;
  });
  L(`=== LEITURA DE VOLTA, TELA ${pagina} ===`);
  volta.forEach(v=>L('   ',String(v[1]).padEnd(16),'|',v[0],'=',JSON.stringify(v[2])));
  todasVoltas.push([pagina,volta]);
  await p.screenshot({path:`gf_${SLUG}_seco_p${pagina}.png`,fullPage:true}).catch(()=>{});

  const next=await p.$('div[role=button]:has-text("Next"), div[role=button]:has-text("Próxima"), div[role=button]:has-text("Avançar")');
  const submit=await p.$('div[role=button]:has-text("Submit"), div[role=button]:has-text("Enviar")');
  if(next && !submit){
    await next.scrollIntoViewIfNeeded().catch(()=>{});
    try{ await next.click({timeout:12000}); }catch(e){ L('Next: clique normal falhou, indo por DOM'); await next.evaluate(x=>x.click()); }
    await p.waitForTimeout(2500);
    if(pagina>12){ L('!! mais de 12 telas, abortando por seguranca'); break; }
    continue;
  }
  if(submit){
    const faltam=Object.keys(pendentes.texto).length+Object.keys(pendentes.radio).length+Object.keys(pendentes.dropdown).length+Object.keys(pendentes.grid).length+Object.keys(pendentes.checkbox).length;
    L('ULTIMA TELA. Respostas do arquivo que nunca acharam pergunta:',faltam);
    if(faltam){ L('   pendentes:',JSON.stringify({...pendentes.texto,...pendentes.radio,...pendentes.dropdown}).slice(0,240),Object.keys(pendentes.grid)); }
    if(!ENVIAR){ L('ENSAIO: nada enviado. Confira os prints gf_'+SLUG+'_seco_p*.png e rode de novo com ENVIAR.'); await b.close(); return; }
    reqs.length=0; resps.length=0; falhas.length=0;
    const urlAntes=p.url();
    await submit.scrollIntoViewIfNeeded().catch(()=>{});
    try{ await submit.click({timeout:15000}); }
    catch(e){ L('clique normal falhou:',e.message.slice(0,200)); await submit.evaluate(x=>x.click()).catch(er=>L('clique por DOM tambem falhou:',String(er).slice(0,160))); }
    await p.waitForTimeout(6000);
    for(let k=0;k<10;k++){ if(/formResponse/.test(p.url())) break; await p.waitForTimeout(1200); }
    const urlDepois=p.url();
    const corpo=await p.evaluate(()=>document.body?document.body.innerText:'').catch(()=>'');
    L('=== PROVA ===');
    L('URL antes :',urlAntes);
    L('URL depois:',urlDepois);
    L('POSTs     :'); reqs.forEach(r=>L('   ',r[0],r[1].slice(0,150)));
    L('RESPOSTAS :'); resps.forEach(r=>L('   ',r[0],r[1].slice(0,150)));
    if(falhas.length){ L('FALHAS    :'); falhas.forEach(f=>L('   ',f[0],f[1].slice(0,120),f[2])); }
    L('TEXTO DO SERVIDOR:',JSON.stringify(corpo.slice(0,400)));
    L('VEREDITO: postOk='+resps.some(r=>/formResponse/.test(r[1])&&r[0]>=200&&r[0]<400),'urlOk='+/formResponse/.test(urlDepois));
    await p.screenshot({path:`gf_${SLUG}_envio.png`,fullPage:true}).catch(()=>{});
    await b.close(); return;
  }
  L('!! nem Next nem Submit nesta tela; abortando');
  break;
 }
 await b.close();
})().catch(e=>{ console.error('[gform] ERRO',e); process.exit(1); });
