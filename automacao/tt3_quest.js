// TEAMTAILOR CONNECT, etapa 2 COMPLETA: perfil + CV + QUESTIONARIO, numa sessao por link.
// Herda tudo que foi medido em 16/09 e esta escrito no topo de tt2_completa.js:
//  - o link /connect/session/confirm/<uuid>/<token> E a sessao; a URL CONTINUA sendo essa
//    depois de aberta, e barrar por URL e erro (gastou sete links na rodada anterior);
//  - a prova de sessao e #candidate_first_name existir em /connect/profile/settings;
//  - o banner de cookies COBRE a pagina em algumas casas e tem de ser aceito DEPOIS DE CADA
//    navegacao, por TEXTO do botao;
//  - o campo de telefone REFORMATA o que se digita: conferir DIGITOS e o prefixo +55, nunca
//    igualdade de texto;
//  - nenhum clique cego em button[type=submit] fora de formulario conhecido.
// O QUE ESTE SCRIPT ACRESCENTA: responde o wizard /connect/questions/*, que a campanha vinha
// deixando em branco. Regras duras do questionario, todas vindas de medicao de 07 e 11/09:
//  (1) NUNCA se digita no campo de ENDERECO do questionario: a lista de sugestoes do mapa
//      abre POR CIMA do botao Next e o clique cai na lista (o wizard entrou em laco por
//      quatro telas). O endereco ja foi gravado em /connect/profile/settings.
//  (2) A lista de LOCAIS e por PERMISSAO, nunca por proibicao: o rotulo e a CIDADE e nao o
//      pais, entao uma lista de proibicao por pais deixou passar Bengaluru, Amman, Dubai e
//      Abu Dhabi. Aqui so se marca o que casa com a lista de permissao; o que nao casa fica
//      como estava e SAI NO LOG com o nome, para a decisao ser auditavel.
//  (3) As caixas do banner de COOKIE ja foram marcadas como se fossem locais de trabalho.
//      So se mexe em input[name="location_ids[]"] / [name*="location"].
//  (4) Pergunta que o script nao souber responder com a VERDADE fica em branco e vai para o
//      log; nada de chute. Na GOALS a resposta de "Do you live in Europe?" foi NAO, que e a
//      verdade e custa.
// Uso: sh hb_run.sh tt3_quest.js <arquivo-com-um-link-por-linha> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const LINKS=fs.readFileSync(process.argv[2],'utf8').split('\n').map(x=>x.trim()).filter(x=>/^https/.test(x));
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
 const b=await abrirLocal({headless:false,args:['--disable-blink-features=AutomationControlled']});
 for(const link of LINKS){
 slug=new URL(link).hostname.split('.')[0];
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:1500},locale:'en-US',
   userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=await ctx.newPage();
 const base=new URL(link).origin;
 const rede=[];
 p.on('response',r=>{ if(r.request().method()!=='GET'&&/connect/.test(r.url())) rede.push(r.status()+' '+r.request().method()+' '+r.url().replace(base,'')); });
 const cookies=async()=>{
   for(let v=0;v<3;v++){
     const c=await p.evaluate(()=>{
       const a=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>{
         const t=(x.innerText||'').toLowerCase().replace(/\s+/g,' ').trim();
         return !!x.offsetParent && /^(accept all cookies|accept all|accept cookies|accept|allow all|i accept|got it|ok|aceptar todas las cookies|aceptar todas|aceptar cookies|aceptar|permitir todas|aceitar todos os cookies|aceitar todos|aceitar|godkänn alla|godkänn alla cookies|godta alle|tillad alle|hyväksy kaikki|alle akzeptieren|akzeptieren|tout accepter|accepter|accetta tutti|alles accepteren)$/.test(t);
       });
       if(!a.length) return null; a[0].click(); return (a[0].innerText||'').trim().slice(0,40);
     });
     if(c){ log('   cookies aceitos:',JSON.stringify(c)); await p.waitForTimeout(1500); return true; }
     await p.waitForTimeout(900);
   }
   return false;
 };
 try{
  await p.goto(link,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4500);
  await cookies();
  const bot=await p.$('a[href*="/connect/dashboard"]');
  if(bot){ await bot.click({force:true,timeout:8000}).catch(()=>{}); await p.waitForTimeout(3000); }

  // ---------- PERFIL ----------
  await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000); await cookies(); await p.waitForTimeout(800);
  if(!await p.$('#candidate_first_name')){
    const t=await p.evaluate(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,160));
    log('SEM SESSAO (o perfil nao serve formulario). Tela:',JSON.stringify(t));
    await ctx.close(); continue;
  }
  log('SESSAO ABERTA (#candidate_first_name existe)');
  const preenche=async(sel,val)=>{
    const el=await p.$(sel); if(!el) return null;
    await el.fill(''); await el.type(val,{delay:20}); await p.waitForTimeout(300);
    return await p.$eval(sel,x=>x.value);
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
  await p.screenshot({path:'tt3_'+slug+'.png',fullPage:true}).catch(()=>{});
  log('   REDE nao-GET:',JSON.stringify(rede.slice(-14)));
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
 }
 await b.close();
})();
