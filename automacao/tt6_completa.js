// TEAMTAILOR CONNECT, ROTA NOVA E QUE FUNCIONA (medida em 16/09, terceiro turno):
// O CADASTRO E QUE DA A SESSAO. O link "Log in to Connect" do email NAO abre sessao em 15
// locatarios desta campanha, e isso ficou provado com quatro hipoteses testadas e descartadas:
//   - prazo do link (pedido e aberto em 40s: igual);
//   - banner de cookie (aceito antes da leitura: igual);
//   - clique cego em button[type=submit] na pagina de confirmacao (removido: igual);
//   - link pedido DENTRO do proprio navegador, na MESMA sessao persistente que o abriu
//     (teste que faltava, feito agora na Goodgame: igual).
// E a sonda fechou a questao: depois de abrir o link, TODO caminho /connect/* (dashboard,
// profile, profile/settings, resume, questions/start) redireciona para /connect, a tela de
// inscricao "What interests you?". Ou seja nao ha sessao nenhuma, e nao e leitura errada de
// uma tela so.
// O QUE FUNCIONA: refazer a INSCRICAO, que e um formulario de DOIS passos e termina logado:
//   passo 1: radio candidate[department_id] + botao "Continue"
//   passo 2: input candidate[email] + CAIXA DE TERMOS (sem ela o servidor devolve "Terms must
//            be accepted") + botao "Connect"
// Logo depois disso a sessao esta posta e /connect/profile/settings serve o formulario.
// Uso: sh hb_run.sh tt6_completa.js <arquivo com "host|regex-do-departamento" por linha> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const CASAS=fs.readFileSync(process.argv[2],'utf8').split('\n').map(x=>x.trim()).filter(x=>x&&!/^#/.test(x))
  .map(l=>{const [h,d]=l.split('|'); return {host:h.trim(), dep:(d||'art').trim()};});
const SUBMIT=process.argv.includes('ENVIAR');
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
const PITCH='Senior 3D character artist, 10+ years on stylized characters for animation and games.';
// LISTA DE PERMISSAO de locais (cidades e paises). Escopo da campanha: Europa, America do
// Norte, Oceania e Brasil, mais remoto. O que nao estiver aqui NAO se marca.
const OK_LOCAL=new RegExp('\\b('+[
 'remote','anywhere','worldwide','hybrid','flexible','work from home',
 'united kingdom','uk','england','scotland','wales','northern ireland','ireland','london','brighton','manchester','liverpool','leeds','bristol','cambridge','oxford','guildford','brighton','sheffield','newcastle','glasgow','edinburgh','dundee','belfast','dublin','galway','walsall','leamington',
 'france','paris','lyon','marseille','montpellier','bordeaux','toulouse','nantes','lille','angouleme','annecy','valence','roubaix',
 'germany','deutschland','berlin','hamburg','munich','munchen','cologne','koln','frankfurt','stuttgart','dusseldorf','leipzig','dresden','bremen','hannover','karlsruhe','ludwigsburg','mainz','nuremberg',
 'spain','madrid','barcelona','valencia','seville','malaga','bilbao','las palmas','tenerife','zaragoza',
 'portugal','lisbon','lisboa','porto','braga','coimbra',
 'italy','milan','milano','rome','roma','turin','torino','bologna','florence','napoli',
 'netherlands','amsterdam','rotterdam','utrecht','the hague','hilversum','eindhoven','breda',
 'belgium','brussels','bruxelles','liege','antwerp','ghent','gent','leuven','charleroi',
 'luxembourg','switzerland','zurich','geneva','lausanne','basel','lugano',
 'austria','vienna','wien','graz','salzburg','linz',
 'denmark','copenhagen','kobenhavn','aarhus','odense','frederiksberg','viborg',
 'sweden','stockholm','gothenburg','goteborg','malmo','skovde','umea','uppsala','linkoping','karlshamn','lund','vasteras',
 'norway','oslo','bergen','trondheim','stavanger',
 'finland','helsinki','espoo','tampere','turku','oulu','kotka',
 'iceland','reykjavik',
 'poland','warsaw','warszawa','krakow','cracow','wroclaw','poznan','gdansk','lodz','katowice','bydgoszcz','rzeszow',
 'czech','czechia','prague','praha','brno','ostrava',
 'slovakia','bratislava','kosice','hungary','budapest','szeged',
 'romania','bucharest','bucuresti','cluj','timisoara','iasi',
 'bulgaria','sofia','plovdiv','varna','burgas',
 'croatia','zagreb','split','slovenia','ljubljana','maribor',
 'serbia','belgrade','beograd','novi sad','nis',
 'greece','athens','thessaloniki','cyprus','nicosia','limassol','malta','valletta','gzira','sliema','msida','stgiles',
 'estonia','tallinn','tartu','latvia','riga','lithuania','vilnius','kaunas',
 'ukraine','kyiv','kiev','lviv','kharkiv','odesa',
 'canada','toronto','vancouver','montreal','montréal','quebec','ottawa','calgary','edmonton','winnipeg','halifax','victoria','kelowna',
 'united states','usa','u.s.','los angeles','san francisco','san diego','seattle','austin','new york','brooklyn','chicago','boston','portland','burbank','glendale','culver city','santa monica','irvine','atlanta','miami','orlando','denver','salt lake city','las vegas','philadelphia','washington','raleigh','madison','san rafael','emeryville','novato','baltimore','detroit','minneapolis','dallas','houston','phoenix','pittsburgh',
 'australia','sydney','melbourne','brisbane','adelaide','perth','canberra','gold coast',
 'new zealand','auckland','wellington','christchurch',
 'brazil','brasil','sao paulo','são paulo','rio de janeiro','recife','olinda','porto alegre','curitiba','belo horizonte','brasilia','florianopolis'
].join('|')+')\\b','i');
let slug='';
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 // CONTEXTO PERSISTENTE, um por casa: a sessao do cadastro e a UNICA chance de completar o
 // perfil (o link de email nao autentica em 15 de 19 locatarios), entao o cookie dela nao
 // pode morrer com o processo. Assim uma rodada seguinte ainda entra logado.
 for(const casa of CASAS){
 slug=casa.host.split('.')[0];
 const ctx=await abrirPerfil('/home/user/apply/prof_tt_'+slug,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1280,height:1500},locale:'en-US',userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=ctx.pages()[0]||await ctx.newPage();
 const base='https://'+casa.host;
 const rede=[];
 p.on('response',r=>{ if(r.request().method()!=='GET'&&/connect/.test(r.url())) rede.push(r.status()+' '+r.request().method()+' '+r.url().replace(base,'')); });
 const cookies=async()=>{
   for(let v=0;v<3;v++){
     const c=await p.evaluate(()=>{
       const a=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>{
         const t=(x.innerText||'').toLowerCase().replace(/\s+/g,' ').trim();
         return !!x.offsetParent && /^(accept all cookies|accept all|accept cookies|accept|allow all|i accept|got it|ok|aceptar todas las cookies|aceptar todas|aceptar cookies|aceptar|permitir todas|aceitar todos os cookies|aceitar todos|aceitar|godkänn alla|godkänn alla cookies|godta alle|tillad alle|hyväksy kaikki|alle akzeptieren|alle cookies akzeptieren|akzeptieren|tout accepter|accepter tout|accepter|accetta tutti|alles accepteren)$/.test(t);
       });
       if(!a.length) return null; a[0].click(); return (a[0].innerText||'').trim().slice(0,40);
     });
     if(c){ log('   cookies aceitos:',JSON.stringify(c)); await p.waitForTimeout(1500); return true; }
     await p.waitForTimeout(900);
   }
   return false;
 };
 try{
  // ---------- INSCRICAO (e ela que da a sessao) ----------
  await p.goto(base+'/connect',{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3500); await cookies();
  const dep=await p.evaluate(rx=>{
    const re=new RegExp(rx,'i');
    const r=[...document.querySelectorAll('input[name="candidate[department_id]"]')];
    const rot=x=>((x.labels&&x.labels[0]&&x.labels[0].innerText)||(x.closest('label')?x.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim();
    const alvo=r.find(x=>re.test(rot(x)));
    if(!alvo) return {erro:'departamento nao achado',opcoes:r.map(rot).slice(0,25)};
    alvo.click(); return {rotulo:rot(alvo),value:alvo.value,total:r.length};
  },casa.dep);
  log('   departamento:',JSON.stringify(dep));
  // VARIANTE MEDIDA (Liquid Swords): ha locatario cujo Connect NAO tem passo de
  // departamento - a lista vem VAZIA e o formulario comeca direto no e-mail. Nesse caso
  // seguir e correto; parar seria perder a porta. Se ha lista e nada casou, para: marcar
  // departamento errado e pior que nao marcar.
  if(dep.erro && (dep.opcoes||[]).length){ log('   PARANDO nesta casa: ha departamentos e nenhum casou'); await ctx.close(); continue; }
  if(dep.erro){ log('   sem passo de departamento neste locatario: sigo para o e-mail'); }
  await p.waitForTimeout(1500);
  log('   Continue:',JSON.stringify(await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button,input[type=submit]')].filter(x=>!!x.offsetParent)
      .filter(x=>/^(continue|continuar|next|siguiente|suivant|fortsätt|weiter|volgende)$/i.test(((x.innerText||x.value||'')+'').trim()));
    if(!b.length) return null; b[0].click(); return ((b[0].innerText||b[0].value||'')+'').trim();})));
  await p.waitForTimeout(4000); await cookies();
  // MEDIDO na Anima (locatario em espanhol): o rotulo do botao NAO e "Continue" e sim
  // "Continuar", e com o seletor so em ingles o script ficava no passo 1 e tentava escrever
  // e-mail numa tela que nao tem o campo (fill estourou 30s). Os botoes passaram a casar em
  // varios idiomas, e aqui se ESPERA o campo em vez de assumir que ele existe.
  const em=await p.waitForSelector('#candidate_email, input[name="candidate[email]"]',{timeout:20000}).catch(()=>null);
  if(!em){ log('   SEM campo de email no passo 2; tela:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,180)))); await ctx.close(); continue; }
  await em.fill(P.email); await p.waitForTimeout(500);
  // AS DUAS CAIXAS: a de TERMOS e obrigatoria (o servidor devolve "Terms must be accepted"),
  // e a de contato direto e interesse verdadeiro dele.
  const cxs=await p.evaluate(()=>[...document.querySelectorAll('input[type=checkbox]')].filter(x=>!!x.offsetParent)
    .map(x=>{ if(!x.checked) x.click();
      return {n:x.name||x.id,rot:((x.labels&&x.labels[0]&&x.labels[0].innerText)||(x.closest('label')?x.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim().slice(0,70),marcado:x.checked};}));
  log('   caixas:',JSON.stringify(cxs));
  if(!SUBMIT){ log('   MODO SECO: nao cliquei Connect'); await p.screenshot({path:'tt6_'+slug+'_seco.png',fullPage:true}).catch(()=>{}); await ctx.close(); continue; }
  log('   Connect:',JSON.stringify(await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button,input[type=submit]')].filter(x=>!!x.offsetParent)
      .filter(x=>/^(connect|conectar|conectarse|connecter|anslut|verbinden)$/i.test(((x.innerText||x.value||'')+'').trim()));
    if(!b.length) return null; b[0].click(); return ((b[0].innerText||b[0].value||'')+'').trim();})));
  await p.waitForTimeout(8000); await cookies();
  log('   depois do Connect, url:',p.url().replace(base,''),'| tela:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,170))));

  // ---------- PERFIL ----------
  await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000); await cookies(); await p.waitForTimeout(800);
  if(!await p.$('#candidate_first_name')){
    const t=await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,160));
    log('SEM SESSAO (o perfil nao serve formulario). Tela:',JSON.stringify(t));
    await ctx.close(); continue;
  }
  log('SESSAO ABERTA (#candidate_first_name existe)');
  // LICAO MEDIDA NA ANIMA (16/09): o banner de cookies em ESPANHOL nao casava com a lista de
  // botoes (so tinha ingles e sueco), o banner cobriu a pagina e TODO campo voltou VAZIO na
  // leitura de volta - com o log dizendo que escreveu. Se o campo nao confirma, tenta aceitar
  // cookie de novo e repete uma vez antes de desistir.
  const preenche=async(sel,val)=>{
    for(let tent=0;tent<2;tent++){
      const el=await p.$(sel); if(!el) return null;
      await el.fill('').catch(()=>{}); await el.type(val,{delay:20}).catch(()=>{}); await p.waitForTimeout(400);
      const lido=await p.$eval(sel,x=>x.value).catch(()=>'');
      if((lido||'').trim()) return lido;
      log('   campo',sel,'voltou VAZIO: aceito cookie e tento de novo');
      await cookies(); await p.waitForTimeout(1200);
    }
    return '';
  };
  log('   nome:',JSON.stringify(await preenche('#candidate_first_name',P.nome)));
  log('   sobrenome:',JSON.stringify(await preenche('#candidate_last_name',P.sobrenome)));
  {
   const lido=await preenche('#candidate_phone',P.telefone_internacional);
   const so=v=>(v||'').replace(/\D/g,'');
   log('   telefone: digitos batem =>',so(lido)===so(P.telefone_internacional),'| +55 =>',(lido||'').trim().startsWith('+55'));
  }
  const end=await p.$('#candidate_location');
  if(end){
    const jaTem=await p.$eval('#candidate_location',x=>x.value);
    if(!jaTem){
      await end.fill(''); await end.type('Olinda, Pernambuco',{delay:60});
      await p.waitForTimeout(3500);
      const op=await p.evaluate(()=>{
        const c=[...document.querySelectorAll('[role="option"],.pac-item,li')].filter(x=>!!x.offsetParent&&/olinda/i.test(x.innerText||''));
        if(!c.length) return null; c[0].click(); return (c[0].innerText||'').replace(/\s+/g,' ').trim().slice(0,70);
      });
      log('   sugestao de endereco:',JSON.stringify(op));
      await p.waitForTimeout(1200);
    } else log('   endereco ja gravado:',JSON.stringify(jaTem));
  }
  // LOCAIS por PERMISSAO (ver regra 2 no topo)
  const locais=await p.evaluate(rx=>{
    const re=new RegExp(rx,'i');
    const ins=[...document.querySelectorAll('input[type=checkbox][name*="location"]')];
    return ins.map(i=>{
      const rot=((i.labels&&i.labels[0]&&i.labels[0].innerText)||i.getAttribute('aria-label')||
        (i.closest('label')?i.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim();
      const permitido=re.test(rot);
      if(permitido&&!i.checked) i.click();
      if(!permitido&&i.checked) i.click();
      return {rot:rot.slice(0,40),permitido,marcado:i.checked};
    });
  },OK_LOCAL.source);
  log('   LOCAIS (permissao):',JSON.stringify(locais));
  log('   avisar de vagas novas:',await p.evaluate(()=>{const s=document.querySelector('#candidate_subscribe'); if(s&&!s.checked)s.click(); return s?s.checked:null;}));
  if(!SUBMIT){ log('MODO SECO no perfil'); }
  else{
    const bt=await p.$('form[action*="/connect/profile"] button[type=submit]')||await p.$('button[type=submit]');
    if(bt){ await bt.click({force:true,timeout:15000}).catch(e=>log('   submit perfil:',e.message.split('\n')[0])); await p.waitForTimeout(6000); }
    await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(4000);
    const conf=await p.evaluate(()=>({n:(document.querySelector('#candidate_first_name')||{}).value,
      s:(document.querySelector('#candidate_last_name')||{}).value,
      t:((document.querySelector('#candidate_phone')||{}).value||'').replace(/\D/g,'').length,
      e:(document.querySelector('#candidate_location')||{}).value}));
    log('   PERFIL RELIDO DEPOIS DE RECARREGAR:',JSON.stringify(conf));
  }

  // ---------- CV ----------
  await p.goto(base+'/connect/resume',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3500); await cookies();
  const fi=await p.$('input[type=file]');
  if(!fi) log('   sem campo de arquivo em /connect/resume');
  else if(SUBMIT){
    await fi.setInputFiles(P.cv); await p.waitForTimeout(4000);
    const bt2=await p.$('button[type=submit]');
    if(bt2){ await bt2.click({force:true,timeout:15000}).catch(()=>{}); await p.waitForTimeout(7000); }
    await p.goto(base+'/connect/resume',{timeout:90000,waitUntil:'domcontentloaded'});
    await p.waitForTimeout(3000);
    log('   CV RELIDO DEPOIS DE RECARREGAR:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,180))));
  }

  // ---------- QUESTIONARIO ----------
  await p.goto(base+'/connect/questions/start',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3000); await cookies();
  const entrada=await p.evaluate(()=>{
    const b=[...document.querySelectorAll('button,a')].filter(x=>!!x.offsetParent && /let.s go|get started|start|begin/i.test(x.innerText||''));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim().slice(0,30);
  });
  log('   QUESTIONARIO, entrada:',JSON.stringify(entrada));
  await p.waitForTimeout(4000);
  const naoSei=[]; let ultimo='';
  for(let sl=0; sl<30; sl++){
    await cookies();
    const est=await p.evaluate(()=>{
      const vis=e=>!!e.offsetParent;
      const h=[...document.querySelectorAll('h1,h2,h3,legend,label')].filter(vis)
        .map(x=>(x.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<200);
      return {path:location.pathname,
        titulo:h[0]||'', cabecalhos:h.slice(0,4),
        texto:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,300),
        campos:[...document.querySelectorAll('input,textarea,select')].filter(vis).map(e=>({
          tag:e.tagName,type:e.type||'',name:e.name||'',id:e.id||'',val:(e.value||'').slice(0,40),
          rot:((e.labels&&e.labels[0]&&e.labels[0].innerText)||e.getAttribute('aria-label')||e.placeholder||
              (e.closest('label')?e.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim().slice(0,90)}))};
    });
    if(est.path===ultimo && sl>0){ log('   QUESTIONARIO parou de avancar em',est.path); break; }
    ultimo=est.path;
    if(/dashboard|thank/i.test(est.path+' '+est.texto.slice(0,60))){ log('   QUESTIONARIO FIM em',est.path); break; }
    log('   QSLIDE',sl,est.path,'|',JSON.stringify(est.titulo),'|',JSON.stringify(est.campos.map(c=>c.type+':'+(c.rot||c.name)).slice(0,10)));

    const alvo=(est.titulo+' '+est.cabecalhos.join(' ')+' '+est.texto).toLowerCase();
    // 1) ENDERECO do questionario: nao se toca (regra 1 no topo)
    // 2) slide de LOCAIS
    if(/\/locations/.test(est.path)||/where (do|would) you (want|like) to work|work location/.test(alvo)){
      const l=await p.evaluate(rx=>{
        const re=new RegExp(rx,'i');
        const ins=[...document.querySelectorAll('input[type=checkbox][name*="location"],input[type=checkbox][name*="Location"]')];
        return ins.map(i=>{
          const rot=((i.labels&&i.labels[0]&&i.labels[0].innerText)||i.getAttribute('aria-label')||
            (i.closest('label')?i.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim();
          const ok=re.test(rot);
          if(ok&&!i.checked) i.click();
          if(!ok&&i.checked) i.click();
          return {rot:rot.slice(0,40),ok,marcado:i.checked};
        });
      },OK_LOCAL.source);
      log('     locais do slide (permissao):',JSON.stringify(l));
    }
    // 3) slide de CV
    else if(/\/resume/.test(est.path)){
      const f=await p.$('input[type=file]');
      if(f&&SUBMIT){ await f.setInputFiles(P.cv); await p.waitForTimeout(3500); log('     CV posto no slide'); }
    }
    // 4) dados basicos e pitch e perguntas numeradas
    else {
      for(const c of est.campos){
        const r=(c.rot+' '+c.name+' '+est.titulo).toLowerCase();
        // ENDERECO: NUNCA (regra 1)
        if(/address|location|city|where do you live|place/.test(r) && !/checkbox/.test(c.type)){ log('     PULADO de proposito (endereco):',JSON.stringify(c.rot||c.name)); continue; }
        let v=null;
        if(c.type==='checkbox'||c.type==='radio'){
          const rot=c.rot.toLowerCase();
          const q=alvo;
          let marcar=null;
          if(/software|tool|program|application|which.*(use|know)|skills/.test(q))
            marcar=/^(maya|autodesk maya|zbrush|substance|substance painter|substance designer|houdini|marvelous|marvelous designer|3ds max|blender|unreal|unity|photoshop|nuke|mudbox|topogun|uvlayout|arnold|redshift|substance 3d)/.test(rot);
          else if(/role|position|title|job|looking for|interested in|discipline|department|area/.test(q))
            marcar=/(character|3d artist|3d|modeling|modelling|modeler|modeller|game art|art|animation)/.test(rot)&&!/(concept|2d|ui|ux|tech|programmer|engineer|producer|qa|marketing|sound|audio|writer|designer \(game\)|level)/.test(rot);
          else if(/type of (employment|contract|work)|employment type|availability/.test(q))
            marcar=/(full.?time|permanent|contract|freelance|remote|on.?site|hybrid|relocat)/.test(rot);
          else if(/europe|eu citizen|right to work|authori[sz]ed|work permit|visa/.test(q))
            marcar=/^(no|nej|non)$/.test(rot.trim());   // a verdade: ele nao tem permissao na UE/EUA
          if(marcar===null){ naoSei.push(est.path+' | '+est.titulo+' | opcao: '+c.rot); continue; }
          const feito=await p.evaluate(([n,id,rot,quer])=>{
            const el=id?document.getElementById(id):null;
            const e=el||[...document.querySelectorAll('input[name="'+n+'"]')].find(x=>{
              const t=((x.labels&&x.labels[0]&&x.labels[0].innerText)||'').replace(/\s+/g,' ').trim();
              return t===rot;});
            if(!e) return 'sem campo';
            if(quer&&!e.checked) e.click();
            if(!quer&&e.checked) e.click();
            return e.checked;
          },[c.name,c.id,c.rot,marcar]);
          log('     opcao',JSON.stringify(c.rot),'=>',marcar?'MARCAR':'deixar','| ficou:',feito);
          continue;
        }
        if(/portfolio|website|reel|artstation|work sample|link to your work|showreel/.test(r)) v=P.portfolio;
        else if(/linkedin/.test(r)) v=P.linkedin;
        else if(/years|how long|experience/.test(r)&&/\d|year/.test(r)) v='10';
        else if(/pitch|about you|tell us|short.*(intro|bio)|summar/.test(r)) v=PITCH;
        else if(/first name/.test(r)) v=P.nome;
        else if(/last name|surname/.test(r)) v=P.sobrenome;
        else if(/phone|mobile/.test(r)) v=P.telefone_internacional;
        else if(/e-?mail/.test(r)) v=P.email;
        else if(/notice|when can you start|available from/.test(r)) v='Negotiable, around two months from an offer.';
        else if(/salary|compensation|rate/.test(r)) v='Open to aligning with your band for the role.';
        else if(/role|position|title/.test(r)) v='Senior 3D Character Artist';
        if(v===null){ if(c.type!=='hidden'&&c.type!=='submit'){ naoSei.push(est.path+' | '+est.titulo+' | campo: '+(c.rot||c.name)); } continue; }
        const lido=await p.evaluate(([id,n,val])=>{
          const e=(id?document.getElementById(id):null)||document.querySelector('[name="'+n+'"]');
          if(!e) return 'sem campo';
          e.focus(); e.value=val;
          e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));
          return (e.value||'').slice(0,50);
        },[c.id,c.name,v]);
        log('     campo',JSON.stringify(c.rot||c.name),'=>',JSON.stringify(/phone/.test(r)?'(telefone)':lido));
      }
    }
    if(!SUBMIT){ log('     MODO SECO: nao avanco o slide'); break; }
    const av=await p.evaluate(()=>{
      const b=[...document.querySelectorAll('button,a,input[type=submit]')].filter(x=>!!x.offsetParent)
        .filter(x=>/^(next|continue|save|submit|done|finish|skip)$/i.test(((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim()));
      if(!b.length) return null;
      const pref=b.find(x=>/^(next|continue|save|submit|done|finish)$/i.test(((x.innerText||x.value||'')+'').trim()))||b[0];
      pref.click(); return ((pref.innerText||pref.value||'')+'').trim();
    });
    log('     avancar:',JSON.stringify(av));
    if(!av) break;
    await p.waitForTimeout(3500);
  }
  if(naoSei.length){ log('   PERGUNTAS QUE EU NAO RESPONDI (sem chute):'); naoSei.slice(0,20).forEach(x=>log('     -',x)); }

  // ---------- PROVA FINAL, DEPOIS DE RECARREGAR ----------
  await p.goto(base+'/connect/dashboard',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000); await cookies();
  log('   PROVA /connect/dashboard:',JSON.stringify(await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,220))));
  await p.goto(base+'/connect/questions/start',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000);
  log('   PROVA /connect/questions/start depois de recarregar:',JSON.stringify(await p.evaluate(()=>({path:location.pathname,txt:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,260)}))));
  await p.screenshot({path:'tt6_'+slug+'.png',fullPage:true}).catch(()=>{});
  log('   REDE nao-GET:',JSON.stringify(rede.slice(-14)));
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
 }
})();
