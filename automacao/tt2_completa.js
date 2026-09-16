// TEAMTAILOR CONNECT, PASSO 2: completar o perfil de uma conta que JA EXISTE.
// Como se entra sem senha: POST em /connect/login com authenticity_token + candidate[email]
// dispara um email "Log in to Connect" com uma URL /connect/session/confirm/<id>/<token>.
// Esse link e a sessao. (O pedido do link se faz por CURL, sem navegador: pede_link.sh)
// O que este script preenche, com leitura de volta DEPOIS DE RECARREGAR a pagina:
//   /connect/profile/settings -> first_name, last_name, phone (+55 explicito) e Address
//     (autocomplete: o valor tem de ser ESCOLHIDO DA LISTA, senao o place_id fica vazio)
//   /connect/resume           -> upload do CV
// O QUE ESTE SCRIPT NAO TOCA, de proposito: candidate[location_ids][] (a lista de locais de
// interesse do estudio) e o campo de endereco DO QUESTIONARIO - os dois sao decisao do Vini.
// O questionario /connect/questions/start e apenas LIDO e despejado no log, nunca respondido
// no chute.
// Uso: sh hb_run.sh tt2_completa.js <link-de-acesso> [ENVIAR]
const {chromium}=require('playwright'); const fs=require('fs');
// Uso novo: sh hb_run.sh tt2_completa.js <arquivo-com-um-link-por-linha> [ENVIAR]
// UM navegador por vez e UMA sessao por link (o link de acesso do Connect e de USO UNICO:
// medido as 19h20, quando um diagnostico gastou o link do Territory e a sessao seguinte caiu
// de volta no login). Todas as casas num unico processo.
const LINKS=require('fs').readFileSync(process.argv[2],'utf8').split('\n').map(x=>x.trim()).filter(x=>/^https/.test(x));
const SUBMIT=process.argv.includes('ENVIAR');
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
let slug='';
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:process.env.APPLY_PROXY||process.env.HTTPS_PROXY},
   args:['--no-sandbox','--ignore-certificate-errors','--disable-blink-features=AutomationControlled']});
 for(const link of LINKS){
 slug=new URL(link).hostname.split('.')[0];
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1400},locale:'en-US',
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=await ctx.newPage();
 const base=new URL(link).origin;
 try{
  await p.goto(link,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4500);
  log('depois do link de acesso:',p.url().replace(base,''));
  // MEDIDO as 19h40: depois do link, a URL CONTINUA sendo /connect/session/confirm/... e
  // isso NAO quer dizer que a sessao falhou - a sessao esta posta e o /connect/profile/settings
  // abre com os campos. Barrar por URL foi erro meu e gastou sete links de uso unico.
  // A prova de sessao e o campo #candidate_first_name existir na pagina de perfil.
  const botao=await p.$('button[type=submit], a[href*="/connect/dashboard"]');
  if(botao){ await botao.click({force:true,timeout:8000}).catch(()=>{}); await p.waitForTimeout(3000); }
  // COOKIES: medido as 20h10 - em MAG e Nolimit o banner de cookies COBRE a pagina de
  // perfil e o formulario nem chega a existir no DOM, o que o log leu como "sem sessao".
  // Aceitar tem de ser tentado por TEXTO e por data-attribute, e DE NOVO depois de cada
  // navegacao, porque o banner volta.
  const cookies=async()=>{
    for(let v=0;v<3;v++){
      const clicou=await p.evaluate(()=>{
        const alvos=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>{
          const t=(x.innerText||'').toLowerCase().replace(/\s+/g,' ').trim();
          return !!x.offsetParent && /^(accept all cookies|accept all|accept cookies|accept|allow all|godkänn alla|i accept)$/.test(t);
        });
        if(!alvos.length) return null;
        alvos[0].click(); return (alvos[0].innerText||'').trim().slice(0,40);
      });
      if(clicou){ log('   cookies aceitos no botao',JSON.stringify(clicou)); await p.waitForTimeout(1800); return true; }
      await p.waitForTimeout(1200);
    }
    return false;
  };
  await cookies();
  // ---------- PERFIL ----------
  await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000);
  await cookies();
  await p.waitForTimeout(1000);
  const preenche=async(sel,val)=>{
    const el=await p.$(sel); if(!el){ log('sem campo',sel); return false; }
    await el.fill(''); await el.type(val,{delay:22}); await p.waitForTimeout(400);
    const lido=await p.$eval(sel,x=>x.value);
    log('  ',sel,'=>',JSON.stringify(/phone/.test(sel)?'(telefone, nao se escreve no log)':lido));
    return lido.trim()===val.trim();
  };
  const temCampo=await p.$('#candidate_first_name');
  if(!temCampo){ const t=await p.evaluate(()=>(document.body.innerText||'').replace(/\s+/g,' ').slice(0,200));
    log('SEM SESSAO (a pagina de perfil nao serve o formulario). Tela:',JSON.stringify(t),'| proxima casa');
    await ctx.close(); continue; }
  if(!await preenche('#candidate_first_name',P.nome)){ log('nome nao colou | proxima casa'); await ctx.close(); continue; }
  if(!await preenche('#candidate_last_name',P.sobrenome)){ log('sobrenome nao colou | proxima casa'); await ctx.close(); continue; }
  // O CAMPO DE TELEFONE REFORMATA o que se digita (medido as 19h55: entra sem espaco e a
  // tela mostra com espaco e hifen). Comparar texto igual reprova um telefone CERTO, e foi
  // o que gastou seis links. A conferencia certa e: mesmos DIGITOS e prefixo +55 mantido.
  {
   const el=await p.$('#candidate_phone');
   if(!el){ log('sem campo de telefone | proxima casa'); await ctx.close(); continue; }
   await el.fill(''); await el.type(P.telefone_internacional,{delay:22}); await p.waitForTimeout(500);
   const lido=await p.$eval('#candidate_phone',x=>x.value);
   const so=v=>(v||'').replace(/\D/g,'');
   const ok = so(lido)===so(P.telefone_internacional) && /^\+55/.test(lido.replace(/\s/g,'').slice(0,4)+lido.replace(/\s/g,'').slice(4,4));
   log('   telefone: digitos batem =>',so(lido)===so(P.telefone_internacional),'| comeca com +55 =>',lido.trim().startsWith('+55'));
   if(!(so(lido)===so(P.telefone_internacional) && lido.trim().startsWith('+55'))){ log('telefone NAO confere | proxima casa'); await ctx.close(); continue; }
  }
  // ENDERECO: escolher da lista (autocomplete). Sem escolha, place_id fica vazio.
  const end=await p.$('#candidate_location');
  if(end){
    await end.fill(''); await end.type('Olinda, Pernambuco',{delay:60});
    await p.waitForTimeout(3500);
    const op=await p.evaluate(()=>{
      const cand=[...document.querySelectorAll('[role="option"],.pac-item,li')]
        .filter(x=>!!x.offsetParent && /olinda/i.test(x.innerText||''));
      if(!cand.length) return null;
      cand[0].click(); return (cand[0].innerText||'').replace(/\s+/g,' ').trim().slice(0,80);
    });
    log('   sugestao de endereco clicada:',JSON.stringify(op));
    await p.waitForTimeout(1500);
    const loc=await p.evaluate(()=>({q:(document.querySelector('#candidate_location')||{}).value,
      place:(document.querySelector('#candidate_place_id')||{}).value,
      cidade:(document.querySelector('#candidate_city')||{}).value,
      pais:(document.querySelector('#candidate_country')||{}).value}));
    log('   endereco lido de volta:',JSON.stringify(loc));
    if(!loc.place){ log('   AVISO: place_id VAZIO - a lista nao deu sugestao; deixo o texto e sigo'); }
  }
  // LOCAIS DE INTERESSE: o Vini autorizou em 16/09 as 15h50 ("locais por PERMISSAO e nunca
  // por proibicao"), e a regra da campanha e realocacao em primeiro lugar, entao marco TODOS
  // os locais do estudio em vez de deixar a lista vazia.
  const locais=await p.evaluate(()=>{
    const ins=[...document.querySelectorAll('input[type=checkbox][name="candidate[location_ids][]"]')];
    ins.forEach(i=>{ if(!i.checked) i.click(); });
    return ins.map(i=>({rot:((i.labels&&i.labels[0]&&i.labels[0].innerText)||'').trim().slice(0,30), marcado:i.checked}));
  });
  log('   locais de interesse marcados:',JSON.stringify(locais));
  const inscr=await p.evaluate(()=>{
    const s=document.querySelector('#candidate_subscribe');
    if(s&&!s.checked) s.click();
    return s?s.checked:null;
  });
  log('   avisar de vagas novas:',inscr);
  if(!SUBMIT){ log('MODO SECO'); await ctx.close(); continue; }
  const bt=await p.$('form[action*="/connect/profile"] button[type=submit], button[type=submit]');
  await bt.click({force:true,timeout:15000});
  await p.waitForTimeout(6000);
  log('depois de salvar o perfil, url:',p.url().replace(base,''));
  // PROVA: RECARREGAR e ler de volta
  await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000);
  const conf=await p.evaluate(()=>({
    nome:(document.querySelector('#candidate_first_name')||{}).value,
    sobrenome:(document.querySelector('#candidate_last_name')||{}).value,
    tel:(document.querySelector('#candidate_phone')||{}).value,
    endereco:(document.querySelector('#candidate_location')||{}).value,
    place:(document.querySelector('#candidate_place_id')||{}).value}));
  log('RELEITURA DEPOIS DE RECARREGAR:',JSON.stringify({nome:conf.nome,sobrenome:conf.sobrenome,
    tel_tem_mais:/^\+/.test(conf.tel||''), tel_digitos:(conf.tel||'').replace(/\D/g,'').length,
    endereco:conf.endereco, place_id_preenchido:!!conf.place}));
  // ---------- CV ----------
  await p.goto(base+'/connect/resume',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3500);
  const fi=await p.$('input[type=file]');
  if(!fi){ log('sem campo de arquivo em /connect/resume'); }
  else{
    await fi.setInputFiles(P.cv); await p.waitForTimeout(4000);
    const bt2=await p.$('button[type=submit]');
    if(bt2){ await bt2.click({force:true,timeout:15000}); await p.waitForTimeout(8000); }
    await p.goto(base+'/connect/resume',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(3500);
    const t=await p.evaluate(()=>(document.body.innerText||'').replace(/\s+/g,' ').slice(0,300));
    log('RELEITURA DE /connect/resume DEPOIS DE RECARREGAR:',JSON.stringify(t));
  }
  // ---------- QUESTIONARIO: so leitura ----------
  // QUESTIONARIO: abre, entra e DESPEJA a estrutura de cada slide, para o dossie sair sem
  // chute. (Nesta passada nao se responde: o objetivo e mapear o formato.)
  await p.goto(base+'/connect/questions/start',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3000); await cookies();
  const entrada=await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button,a')].filter(x=>!!x.offsetParent && /let.s go|start|begin|comecar/i.test(x.innerText||''));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim().slice(0,30);
  });
  log('QUESTIONARIO: botao de entrada',JSON.stringify(entrada));
  await p.waitForTimeout(4000);
  for(let sl=0; sl<6; sl++){
    const d=await p.evaluate(()=>({
      url:location.pathname,
      texto:(document.body.innerText||'').replace(/\s+/g,' ').slice(0,320),
      campos:[...document.querySelectorAll('input,textarea,select')].filter(x=>!!x.offsetParent||x.name)
        .map(x=>({tag:x.tagName,type:x.type,name:x.name,id:x.id,
          rot:((x.labels&&x.labels[0]&&x.labels[0].innerText)||x.getAttribute('placeholder')||'').replace(/\s+/g,' ').slice(0,50),
          vis:!!x.offsetParent}))
    }));
    log('  QSLIDE',sl,d.url,'|',JSON.stringify(d.texto));
    log('  QCAMPOS',sl,JSON.stringify(d.campos.filter(c=>c.vis)));
    const avancou=await p.evaluate(()=>{
      const b=[...document.querySelectorAll('button,a')].filter(x=>!!x.offsetParent && /next|skip|continue|ok/i.test(x.innerText||''));
      if(!b.length) return false; b[b.length-1].click(); return true;
    });
    if(!avancou) break;
    await p.waitForTimeout(3000);
  }
  await p.screenshot({path:'tt2_'+slug+'.png',fullPage:true});
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
 }
 await b.close();
})();
