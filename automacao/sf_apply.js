// SuccessFactors (career site SAP, marca /brandUrl) - CRIA CONTA e CANDIDATA.
// MEDIDO em 16/09 na Rising Sun Pictures (careers.rsp.com.au, company=artistesfo):
//  (1) O botao "Apply now" e um DROPDOWN-TOGGLE. O link de verdade e #applyOption--manual,
//      dentro do <ul id="unifyApplyNowButtonListDropDown">.
//  (2) O SF serve TRES COPIAS do bloco de botoes (variantes de layout) e a PRIMEIRA e
//      INVISIVEL. Seletor por id pega a invisivel e page.click() estoura 15s de timeout.
//      Todo clique aqui e feito no DOM filtrando por offsetParent.
//  (3) A pagina de conta e "Career Opportunities: Create an Account", campos fbclc_*.
//      A senha tem regra propria: 8 a 18 caracteres, maiuscula + minuscula + numero ou
//      pontuacao, sem espaco.
//  (4) O aceite de privacidade e um BOTAO que abre modal; o hidden fbclc_dpcsId so ganha
//      valor depois do aceite, e sem ele o Create Account volta com erro.
// Sessao: contexto PERSISTENTE em prof_<marca>, para a conta criada valer na rodada seguinte.
// Uso: sh hb_run.sh sf_apply.js <url-do-anuncio> <marca> <etapa> [ENVIAR]
//   etapa = conta | form
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const URLJOB=process.argv[2], MARCA=process.argv[3]||'sf', ETAPA=process.argv[4]||'conta';
const ENVIAR=process.argv.includes('ENVIAR');
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
const C=JSON.parse(fs.readFileSync('/home/user/apply/cred.json','utf8'));
const SENHA=(C[MARCA+'_sf']&&C[MARCA+'_sf'].senha)||C.padrao_campanha;
const RESP=fs.existsSync('/home/user/apply/ans_'+MARCA+'.json')?JSON.parse(fs.readFileSync('/home/user/apply/ans_'+MARCA+'.json','utf8')):{};
const log=(...a)=>console.log('['+MARCA+']',...a);
(async()=>{
 const ctx=await abrirPerfil('/home/user/apply/prof_'+MARCA,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1400,height:1200},locale:'en-US',userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=ctx.pages()[0]||await ctx.newPage();
 const rede=[];
 p.on('response',r=>{ const u=r.url(); if(/rsp|career|apply|application|jobs2web/i.test(u)&&r.request().method()!=='GET') rede.push(r.status()+' '+r.request().method()+' '+u.slice(0,160)); });
 const cookies=async()=>{
   for(let v=0;v<3;v++){
     const c=await p.evaluate(()=>{
       const a=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>{
         const t=(x.innerText||'').toLowerCase().replace(/\s+/g,' ').trim();
         return !!x.offsetParent && /^(accept all cookies|accept all|accept cookies|accept|allow all)$/.test(t);
       });
       if(!a.length) return null; a[0].click(); return (a[0].innerText||'').trim();
     });
     if(c){ log('cookies:',c); await p.waitForTimeout(1200); } else break;
   }
 };
 const dump=async(tag,curto)=>{
   await p.waitForTimeout(2000);
   const d=await p.evaluate(()=>{
     const vis=e=>!!e.offsetParent;
     const campos=[...document.querySelectorAll('input,select,textarea')].filter(vis).map(e=>({
       t:e.tagName, ty:e.type||'', n:e.name||'', id:e.id||'',
       v:(e.type==='password'?'***':(e.value||'').slice(0,50)),
       req:e.required||e.getAttribute('aria-required')==='true',
       lab:(()=>{ let l=e.labels&&e.labels[0]?e.labels[0].innerText:''; if(!l&&e.getAttribute('aria-label'))l=e.getAttribute('aria-label');
         if(!l){const w=e.closest('div,td,li,fieldset'); if(w)l=(w.innerText||'').split('\n')[0];} return (l||'').replace(/\s+/g,' ').trim().slice(0,110); })(),
       opts:e.tagName==='SELECT'?[...e.options].map(o=>o.value+'|'+o.text).slice(0,40):undefined
     }));
     const bt=[...document.querySelectorAll('button,a[role=button],input[type=submit],input[type=button],a.btn')].filter(vis)
       .map(e=>((e.innerText||e.value||'')+'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<80);
     const erros=[...document.querySelectorAll('.error,.alert,[class*=error],[role=alert]')].filter(vis)
       .map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<300);
     return {url:location.href,titulo:document.title,campos,bt:[...new Set(bt)].slice(0,40),
       erros:[...new Set(erros)].slice(0,12),texto:((document.body&&document.body.innerText)||'').replace(/\s*\n\s*/g,' | ').slice(0,3000)};
   });
   log('== '+tag+' ==',d.url);
   log('  titulo:',d.titulo);
   if(!curto){ log('  CAMPOS ('+d.campos.length+'):'); d.campos.forEach(c=>log('   ',JSON.stringify(c))); }
   log('  BOTOES:',JSON.stringify(d.bt));
   if(d.erros.length) log('  ERROS/ALERTAS:',JSON.stringify(d.erros));
   log('  TEXTO:',d.texto);
   await p.screenshot({path:'sf_'+MARCA+'_'+tag+'.png'}).catch(()=>{});
   return d;
 };
 const clicaTexto=async(re)=>p.evaluate(rx=>{
   const r=new RegExp(rx,'i');
   const a=[...document.querySelectorAll('button,a,input[type=submit],input[type=button],[role=button]')]
     .filter(x=>!!x.offsetParent && r.test(((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim()));
   if(!a.length) return null; a[0].click(); return ((a[0].innerText||a[0].value||'')+'').trim().slice(0,60);
 },re.source||re);
 // MEDIDO: o contexto persistente NAO guarda a sessao do SF entre rodadas (cookie de
 // sessao puro), entao toda rodada que nao for de criar conta tem de LOGAR.
 const login=async()=>{
   const ok=await p.evaluate(()=>{
     const vis=e=>!!e.offsetParent;
     const u=[...document.querySelectorAll('input[type=text],input[type=email]')].filter(vis)
       .filter(e=>/email/i.test((e.name||'')+(e.id||'')+((e.labels&&e.labels[0]&&e.labels[0].innerText)||'')));
     const w=[...document.querySelectorAll('input[type=password]')].filter(vis);
     if(!u.length||!w.length) return null;
     return {user:u[0].id||u[0].name, pwd:w[0].id||w[0].name};
   });
   if(!ok){ log('login: sem campos'); return false; }
   log('login: campos',JSON.stringify(ok));
   const sel=k=>(ok[k].match(/^[A-Za-z][\w-]*$/)?'#'+ok[k]:'[name="'+ok[k]+'"]');
   await p.fill(sel('user'),P.email); await p.fill(sel('pwd'),SENHA);
   log('login: Sign In ->',await clicaTexto(/^sign in$/));
   await p.waitForTimeout(9000);
   return true;
 };
 try{
  await p.goto(URLJOB,{timeout:120000,waitUntil:'domcontentloaded'});
  await cookies();
  // abre o dropdown e entra no apply manual
  log('toggle:',await p.evaluate(()=>{const b=[...document.querySelectorAll('#unifyApplyNowTopButton')].filter(x=>!!x.offsetParent);
    if(!b.length) return 'sem toggle visivel'; b[0].click(); return 'ok';}));
  await p.waitForTimeout(1800);
  log('manual:',await p.evaluate(()=>{const a=[...document.querySelectorAll('#applyOption--manual')].filter(x=>!!x.offsetParent);
    if(!a.length) return 'sem link visivel'; a[0].click(); return 'ok';}));
  await p.waitForTimeout(9000);
  await cookies();
  let d=await dump('p1');

  if(ETAPA==='conta'){
    // MEDIDO: com contexto limpo o apply cai direto em "Create an Account"; com cookie de
    // visita anterior cai em "Career Opportunities: Sign In", que traz o link
    // "Create an account to apply for our career opportunities."
    if(!d.campos.some(c=>c.n==='fbclc_userName')){
      const cr=await clicaTexto(/create an account/);
      log('link criar conta:',cr);
      if(cr){ await p.waitForTimeout(8000); await cookies(); d=await dump('p1b'); }
    }
    if(!d.campos.some(c=>c.n==='fbclc_userName')){
      log('NAO e a tela de criar conta. Nada feito.'); await ctx.close(); return;
    }
    await p.fill('#fbclc_userName',P.email);
    await p.fill('#fbclc_emailConf',P.email);
    await p.fill('#fbclc_pwd',SENHA);
    await p.fill('#fbclc_pwdConf',SENHA);
    await p.fill('#fbclc_fName',P.nome);
    await p.fill('#fbclc_lName',P.sobrenome);
    await p.selectOption('#fbclc_country','BR').catch(async()=>{await p.selectOption('#fbclc_country',{label:'Brazil'});});
    // alerta de vaga da propria casa: interesse verdadeiro e serve a campanha
    await p.check('#fbclc_emailEnabled').catch(()=>{});
    // aceite de privacidade
    const pv=await clicaTexto(/data privacy statement/);
    log('privacidade, botao:',pv);
    if(pv){ await p.waitForTimeout(3500);
      const ac=await clicaTexto(/^(i agree|agree|accept|i accept|ok)$/);
      log('privacidade, aceite:',ac); await p.waitForTimeout(2500); }
    const dp=await p.evaluate(()=>{const e=document.querySelector('#fbclc_dpcsId'); return e?e.value:'(sem campo)';});
    log('fbclc_dpcsId depois do aceite:',JSON.stringify(dp));
    await p.screenshot({path:'sf_'+MARCA+'_conta_pre.png'}).catch(()=>{});
    if(!ENVIAR){ log('MODO SECO: nao cliquei Create Account.'); await dump('conta_seco',true); await ctx.close(); return; }
    log('Create Account:',await clicaTexto(/^create account$/));
    await p.waitForTimeout(12000);
    await dump('conta_pos');
  }

  if(ETAPA==='form'){
    if(/sign in/i.test(d.titulo)){ await login(); await cookies(); d=await dump('p1_logado',true); }
    // A pagina de candidatura do SF ("/portalcareer") monta em JS e fica em "Loading..."
    // por vários segundos; e o formulario pode morar em IFRAME. Espera longa e dump de
    // TODOS os frames.
    for(let v=0;v<10;v++){
      const t=await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').trim());
      if(t && !/^\s*(Loading\.\.\.)?/.test(t.slice(0,12))===false && t.length>400) break;
      await p.waitForTimeout(4000);
    }
    await p.waitForTimeout(5000);
    log('expandir:',await clicaTexto(/^expand all sections$/));
    await p.waitForTimeout(7000);
    await dump('form_estado');
    // PICKLIST DO SF, estrutura medida: <input id="N:_input" aria-owns="M:_listSelect">
    // com o botao <button id="N:_selectButton"> ao lado. LICAO: ler "[role=option] visivel"
    // SEM ESCOPO devolve a lista de PAISES em todos os campos (o popup do primeiro fica no
    // DOM). A leitura certa e DENTRO do container apontado por aria-owns.
    const ids=await p.evaluate(()=>[...document.querySelectorAll('input[id$=":_input"]')].filter(e=>!!e.offsetParent).map(e=>e.id));
    log('picklists:',JSON.stringify(ids));
    for(const id of ids){
      const n=id.split(':')[0];
      await p.evaluate(n=>{const b=document.querySelector('[id="'+n+':_selectButton"]'); if(b) b.click();},n);
      await p.waitForTimeout(1800);
      const r=await p.evaluate((id)=>{
        const e=document.getElementById(id);
        const own=e.getAttribute('aria-owns');
        const c=document.getElementById(own)||document.querySelector('[id="'+own+'"]');
        const its=c?[...c.querySelectorAll('li,[role=option],tr,div')].map(x=>(x.innerText||'').replace(/\s+/g,' ').trim())
          .filter(t=>t&&t.length<120):['(sem container '+own+')'];
        return {id,lab:(e.getAttribute('aria-label')||'').slice(0,90),own,opts:[...new Set(its)].slice(0,30)};
      },id).catch(e=>({id,erro:e.message}));
      log('  PICK',JSON.stringify(r));
      await p.keyboard.press('Escape').catch(()=>{});
      await p.waitForTimeout(700);
    }
  }

  if(ETAPA==='prova'){
    // PROVA DEPOIS DE RECARREGAR: a lista de candidaturas da propria conta, em
    // Job Management > Jobs Applied.
    for(let v=0;v<12;v++){
      const est=await p.evaluate(()=>({pwd:!!document.querySelector('input[type=password]'),
        home:/Career Opportunities: (Home|Apply)/i.test(document.title)}));
      if(est.home) break;
      if(est.pwd){ await cookies(); await login(); await p.waitForTimeout(6000); break; }
      await p.waitForTimeout(3000);
    }
    await p.goto('https://career17.sapsf.com/careers?company=artistesfo',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(7000);
    log('Job Management:',await clicaTexto(/job management/));
    await p.waitForTimeout(8000);
    let dd=await dump('prova_jm',true);
    log('aba Jobs Applied:',await clicaTexto(/applied/));
    await p.waitForTimeout(8000);
    await dump('prova_aplicadas');
  }

  if(ETAPA==='preenche'){
    // LICAO: decidir "e tela de login?" pelo TITULO falha - a pagina pode estar a meio
    // carregamento e o titulo vir vazio, e o script segue sem logar. O sinal certo e o
    // campo de senha existir.
    for(let v=0;v<12;v++){
      const est=await p.evaluate(()=>({
        pwd:!!document.querySelector('input[type=password]'),
        form:[...document.querySelectorAll('button,a')].some(x=>!!x.offsetParent&&/^expand all sections$/i.test((x.innerText||'').trim()))
      }));
      if(est.form) break;
      if(est.pwd){ log('tela de login detectada pelo campo de senha'); await cookies(); await login(); await p.waitForTimeout(6000); break; }
      await p.waitForTimeout(3000);
    }
    // MEDIDO: depois do login a pagina fica em "Loading..." e o TITULO ainda e
    // "Career Opportunities: <vaga>"; so quando o formulario monta ele vira
    // "Apply for <vaga> (<id>)". Barrar pelo titulo cedo mata a rodada sem motivo.
    let pronto=false;
    for(let v=0;v<15;v++){
      pronto=await p.evaluate(()=>/Apply for/i.test(document.title)||
        [...document.querySelectorAll('button,a')].some(x=>!!x.offsetParent&&/^expand all sections$/i.test((x.innerText||'').trim())));
      if(pronto) break;
      await p.waitForTimeout(4000);
    }
    d=await dump('pre_logado',true);
    if(!pronto){ log('NAO estou na pagina de candidatura (esperei 60s). Parando.'); await ctx.close(); return; }
    log('expandir:',await clicaTexto(/^expand all sections$/));
    await p.waitForTimeout(8000);

    // ANEXOS: os botoes "Upload a Resume" / "Attach a Cover Letter" abrem modal; o
    // input[type=file] e OCULTO, entao setInputFiles direto nele (sem clique) e o caminho
    // que nao depende de modal. Se nao houver file input, cai no clique + modal.
    // ANEXO DO SF, estrutura medida em 16/09 e nada obvia: o que se clica NAO tem texto.
    // O bloco e <div id="N:_attachWrapper"> com:
    //   <span id="N:_ariaAttachLabel"> = o rotulo ("Upload a Resume  Required")
    //   <span role="button" id="N:_attachIcon" class="addAttachments"> = o BOTAO (icone +),
    //        sem innerText e com aria-labelledBY (nao aria-label)
    // Por isso casar botao por texto ou por aria-label devolve NADA. A rota certa: achar o
    // _ariaAttachLabel pelo texto, tirar o numero N do id e clicar em N:_attachIcon.
    // O clique abre o seletor NATIVO de arquivo -> page.waitForEvent('filechooser').
    // Prova do upload: o div N:_attachSuccess perde a classe displayNone.
    const anexa=async(re,arq)=>{
      const n=await p.evaluate(rx=>{
        const r=new RegExp(rx,'i');
        const l=[...document.querySelectorAll('[id$="_ariaAttachLabel"]')]
          .find(x=>r.test((x.innerText||x.textContent||'')));
        return l?l.id.split(':')[0]:null;
      },re);
      if(!n){ log('anexo ['+re+']: SEM rotulo'); return false; }
      const fcp=p.waitForEvent('filechooser',{timeout:25000}).catch(()=>null);
      const cl=await p.evaluate(n=>{
        const b=document.querySelector('[id="'+n+':_attachIcon"]');
        if(!b) return 'sem icone'; b.click(); return 'icone clicado';
      },n);
      log('anexo ['+re+'] id='+n+':',cl);
      const fc=await fcp;
      if(fc){ await fc.setFiles(arq); log('  filechooser: arquivo posto'); }
      else{
        let alvo=null;
        for(const f of [p,...p.frames()]){
          const fis=await (f.$$?f.$$('input[type=file]'):Promise.resolve([])).catch(()=>[]);
          if(fis&&fis.length){ alvo=fis[fis.length-1]; break; }
        }
        if(!alvo){ log('  SEM filechooser e SEM input de arquivo'); return false; }
        await alvo.setInputFiles(arq); log('  input[type=file]: arquivo posto');
      }
      await p.waitForTimeout(12000);
      const est=await p.evaluate(n=>{
        const s=document.querySelector('[id="'+n+':_attachSuccess"]');
        const lab=document.querySelector('[id="'+n+':_attachDownloadLabelLink"]');
        const err=[...document.querySelectorAll('[class*=error]')].filter(x=>!!x.offsetParent)
          .map(x=>(x.innerText||'').trim()).filter(t=>t&&t.length<200);
        return {sucesso:s?!/displayNone/.test(s.className):null, nome:lab?(lab.innerText||'').trim():null, err:err.slice(0,3)};
      },n);
      log('  estado do anexo:',JSON.stringify(est));
      return true;
    };
    await anexa('upload a resume',P.cv);
    await anexa('attach a cover letter',P.carta);
    await p.screenshot({path:'sf_'+MARCA+'_anexos.png'}).catch(()=>{});

    // TEXTO
    const txt={
      address:P.endereco1, city:P.cidade, zip:P.cep, cellPhone:P.telefone_internacional,
      custAvailability:RESP.disponibilidade, custCountryCitizenship:RESP.cidadania,
      custCurrentLocation:RESP.localizacao, custLinkedInURL:P.linkedin, custReelPortfolio:P.portfolio
    };
    for(const k in txt){
      if(txt[k]==null) continue;
      const ok=await p.evaluate(([n,v])=>{
        const e=document.querySelector('[name="'+n+'"]'); if(!e) return 'sem campo';
        e.focus(); e.value=v;
        e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));
        e.blur(); return e.value;
      },[k,txt[k]]);
      log('texto',k,'=>',JSON.stringify(ok));
      await p.waitForTimeout(400);
    }

    // PICKLISTS por ROTULO (o id numerico muda de sessao para sessao; casar por
    // aria-label e o que se sustenta)
    const pick=async(reLab,valor)=>{
      const id=await p.evaluate(rx=>{
        const r=new RegExp(rx,'i');
        const e=[...document.querySelectorAll('input[id$=":_input"]')].filter(x=>!!x.offsetParent)
          .find(x=>r.test(x.getAttribute('aria-label')||''));
        return e?e.id:null;
      },reLab);
      if(!id){ log('pick',reLab,'=> SEM CAMPO'); return; }
      const n=id.split(':')[0];
      await p.evaluate(n=>{const b=document.querySelector('[id="'+n+':_selectButton"]'); if(b) b.click();},n);
      await p.waitForTimeout(1800);
      const r=await p.evaluate(([id,v])=>{
        const e=document.getElementById(id), own=e.getAttribute('aria-owns');
        const c=document.querySelector('[id="'+own+'"]'); if(!c) return 'sem container';
        const it=[...c.querySelectorAll('li,[role=option],a,div')]
          .find(x=>(x.innerText||'').replace(/\s+/g,' ').trim()===v);
        if(!it) return 'opcao nao achada';
        it.click(); return 'clicado';
      },[id,valor]);
      await p.waitForTimeout(2500);
      const lido=await p.evaluate(id=>{const e=document.getElementById(id); return e?(e.value||e.getAttribute('title')||''):'';},id);
      log('pick',reLab,'=>',r,'| lido:',JSON.stringify(lido));
    };
    await pick('State/Province','Other');
    await pick('able to relocate',RESP.realocacao||'Yes');
    await pick('immigration or work permit',RESP.patrocinio||'Yes');
    await pick('target annual salary',RESP.faixa_salarial);

    // ACEITE
    const ack=await p.evaluate(()=>{
      const e=document.querySelector('[name="custAppAcknowledgement"]'); if(!e) return 'sem campo';
      if(!e.checked) e.click(); return e.checked;
    });
    log('acknowledgement:',ack);
    await p.waitForTimeout(1500);
    await p.screenshot({path:'sf_'+MARCA+'_pre.png',fullPage:true}).catch(()=>{});
    const antes=await dump('pre_envio',true);
    log('LEITURA DE VOLTA antes do envio:');
    for(const c of (await p.evaluate(()=>[...document.querySelectorAll('input,textarea')].filter(e=>!!e.offsetParent)
        .map(e=>({n:e.name||e.id,v:e.type==='checkbox'?String(e.checked):((e.value||e.getAttribute('title')||'').slice(0,60))}))))) log('   ',JSON.stringify(c));

    if(!ENVIAR){ log('MODO SECO: nao cliquei Apply.'); await ctx.close(); return; }
    // O par de botoes do rodape sai no innerText como "SaveApply". MEDIDO: nao sao <button>
    // nem <a> - o seletor por tag devolveu "sem botao Apply" e a rodada foi perdida. Aqui se
    // varre QUALQUER no folha com o texto exato e, se nao achar, se despeja o HTML do rodape.
    const ap=await p.evaluate(()=>{
      const cand=[...document.querySelectorAll('*')].filter(x=>{
        if(x.children.length) return false;
        return /^apply$/i.test(((x.innerText||x.textContent||'')+'').replace(/\s+/g,' ').trim());
      });
      if(!cand.length) return 'sem botao Apply';
      const alvo=cand[cand.length-1];
      let clicavel=alvo;
      for(let k=0;k<4&&clicavel;k++){
        if(clicavel.onclick||clicavel.getAttribute&&(clicavel.getAttribute('role')==='button'||clicavel.tagName==='BUTTON'||clicavel.tagName==='A')) break;
        clicavel=clicavel.parentElement;
      }
      (clicavel||alvo).click();
      return 'clicado em '+((clicavel||alvo).tagName)+'#'+((clicavel||alvo).id||'')+' ('+cand.length+' candidatos)';
    });
    if(ap==='sem botao Apply'){
      const h=await p.evaluate(()=>{
        const n=[...document.querySelectorAll('*')].filter(x=>!x.children.length&&/save/i.test(x.innerText||''))[0];
        if(!n) return '(nao achei nem o Save)';
        let w=n; for(let k=0;k<5&&w.parentElement;k++) w=w.parentElement;
        return w.outerHTML.slice(0,2500);
      });
      log('DIAG rodape:',h);
    }
    log('APPLY:',ap);
    await p.waitForTimeout(15000);
    const pos=await dump('pos_envio');
    await p.screenshot({path:'sf_'+MARCA+'_enviado.png',fullPage:true}).catch(()=>{});
    // PROVA DEPOIS DE RECARREGAR: a lista de candidaturas da propria conta
    await p.goto('https://career17.sapsf.com/careers?company=artistesfo',{timeout:90000,waitUntil:'domcontentloaded'}).catch(()=>{});
    await p.waitForTimeout(8000);
    await dump('minhas_candidaturas');
  }
  log('REDE (nao-GET):'); rede.slice(-25).forEach(r=>log('  ',r));
 }catch(e){ log('ERRO:',e.message); await p.screenshot({path:'sf_'+MARCA+'_erro.png'}).catch(()=>{}); }
 await ctx.close();
})();
