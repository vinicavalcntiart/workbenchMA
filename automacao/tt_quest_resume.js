// RETOMA o QUESTIONARIO do Teamtailor Connect numa casa cuja CONTA JA EXISTE, usando o
// contexto persistente /home/user/apply/prof_tt_<slug>.
//
// POR QUE EXISTE. Em 20/09 as 02h3x o tt6_completa.js fechou conta, perfil e CV na ForthStar
// e MORREU no avanco do slide 0 para o slide 1 com "Execution context was destroyed, most
// likely because of a navigation". A causa nao e a pagina: e o proprio clique. O Teamtailor
// navega DENTRO do page.evaluate que clica em Next, entao o contexto de execucao some antes
// de a funcao retornar e o Playwright levanta excecao mesmo com o clique tendo funcionado.
// Tratar essa excecao como FALHA joga fora um avanco que aconteceu.
//
// REGRA QUE FICA: clique que navega tem que ser feito com o erro de contexto destruido
// TRATADO COMO SUCESSO PROVAVEL, e a prova de avanco e a MUDANCA DE PATHNAME lida depois,
// nunca o retorno do evaluate.
//
// Uso: sh hb_run.sh tt_quest_resume.js <host> [ENVIAR]
const {chromium}=require('playwright'); const {abrirLocal,abrirPerfil}=require('./navegador'); const fs=require('fs');
const HOST=process.argv[2]; const SUBMIT=process.argv.includes('ENVIAR');
if(!HOST){ console.log('falta o host'); process.exit(1); }
const slug=HOST.split('.')[0];
const P=JSON.parse(fs.readFileSync('/home/user/apply/pessoal.json','utf8'));
const PITCH='Senior 3D character artist, 10+ years on stylized characters for animation and games.';
const OK_LOCAL=/\b(remote|anywhere|worldwide|hybrid|flexible|work from home|united kingdom|uk|england|scotland|wales|northern ireland|ireland|london|brighton|manchester|liverpool|leeds|bristol|cambridge|oxford|guildford|sheffield|newcastle|glasgow|edinburgh|dundee|belfast|dublin|galway|walsall|leamington|france|paris|lyon|germany|berlin|hamburg|munich|spain|madrid|barcelona|portugal|lisbon|italy|milan|rome|netherlands|amsterdam|belgium|brussels|sweden|stockholm|malmo|denmark|copenhagen|norway|oslo|finland|helsinki|poland|warsaw|krakow|canada|toronto|vancouver|montreal|ottawa|united states|usa|los angeles|new york|seattle|austin|australia|sydney|melbourne|new zealand|auckland|brazil|brasil|olinda|recife)\b/i;
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const ctx=await abrirPerfil('/home/user/apply/prof_tt_'+slug,{headless:false,args:['--disable-blink-features=AutomationControlled'],ignoreHTTPSErrors:true,viewport:{width:1280,height:1500},locale:'en-US',userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'});
 const p=ctx.pages()[0]||await ctx.newPage();
 const base='https://'+HOST; const rede=[];
 p.on('response',r=>{ if(r.request().method()!=='GET'&&/connect/.test(r.url())) rede.push(r.status()+' '+r.request().method()+' '+r.url().replace(base,'')); });
 const cookies=async()=>{ try{ await p.evaluate(()=>{
     const a=[...document.querySelectorAll('button,a,[role=button]')].filter(x=>!!x.offsetParent&&/^(accept all cookies|accept all|accept cookies|accept|allow all|i accept|got it|ok)$/i.test((x.innerText||'').trim()));
     if(a.length) a[0].click();}); }catch(e){} };
 const ev=async(fn,arg)=>{ try{ return await p.evaluate(fn,arg); }catch(e){ return {__erro:e.message.split('\n')[0]}; } };
 try{
  // 1) SESSAO
  await p.goto(base+'/connect/profile/settings',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3500); await cookies();
  if(!await p.$('#candidate_first_name')){
    log('SEM SESSAO. Tela:',JSON.stringify(await ev(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,200))));
    await ctx.close(); return;
  }
  log('SESSAO ABERTA (#candidate_first_name existe)');
  // 2) QUESTIONARIO
  await p.goto(base+'/connect/questions/start',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(3000); await cookies();
  log('entrada:',JSON.stringify(await ev(()=>{
    const b=[...document.querySelectorAll('button,a')].filter(x=>!!x.offsetParent&&/let.s go|get started|^start$|begin|resume|continue/i.test(x.innerText||''));
    if(!b.length) return null; b[0].click(); return (b[0].innerText||'').trim().slice(0,30);})));
  await p.waitForTimeout(4000);
  const naoSei=[]; const visitados=[];
  for(let sl=0; sl<30; sl++){
    await cookies();
    const est=await ev(()=>{
      const vis=e=>!!e.offsetParent;
      const h=[...document.querySelectorAll('h1,h2,h3,legend,label')].filter(vis).map(x=>(x.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<200);
      return {path:location.pathname,titulo:h[0]||'',cabecalhos:h.slice(0,4),
        texto:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,300),
        campos:[...document.querySelectorAll('input,textarea,select')].filter(vis).map(e=>({
          tag:e.tagName,type:e.type||'',name:e.name||'',id:e.id||'',val:(e.value||'').slice(0,40),
          rot:((e.labels&&e.labels[0]&&e.labels[0].innerText)||e.getAttribute('aria-label')||e.placeholder||(e.closest('label')?e.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim().slice(0,90)}))};
    });
    if(est.__erro){ log('  leitura do slide falhou:',est.__erro,'- espero e releio'); await p.waitForTimeout(3000); continue; }
    if(/dashboard|thank/i.test(est.path+' '+est.texto.slice(0,60))){ log('QUESTIONARIO FIM em',est.path); break; }
    const jaVisto=visitados.filter(x=>x===est.path).length;
    if(jaVisto>=2){ log('QUESTIONARIO parou de avancar em',est.path); break; }
    visitados.push(est.path);
    log('QSLIDE',sl,est.path,'|',JSON.stringify(est.titulo),'|',JSON.stringify(est.campos.map(c=>c.type+':'+(c.rot||c.name)).slice(0,12)));
    const alvo=(est.titulo+' '+est.cabecalhos.join(' ')+' '+est.texto).toLowerCase();
    if(/\/locations/.test(est.path)||/where (do|would) you (want|like) to work|work location/.test(alvo)){
      log('  locais:',JSON.stringify(await ev(rx=>{
        const re=new RegExp(rx,'i');
        return [...document.querySelectorAll('input[type=checkbox][name*="location"],input[type=checkbox][name*="Location"]')].map(i=>{
          const rot=((i.labels&&i.labels[0]&&i.labels[0].innerText)||i.getAttribute('aria-label')||(i.closest('label')?i.closest('label').innerText:'')||'').replace(/\s+/g,' ').trim();
          const ok=re.test(rot);
          if(ok&&!i.checked) i.click(); if(!ok&&i.checked) i.click();
          return {rot:rot.slice(0,40),ok,marcado:i.checked};});},OK_LOCAL.source)));
    } else if(/\/resume/.test(est.path)){
      const f=await p.$('input[type=file]');
      if(f&&SUBMIT){ await f.setInputFiles(P.cv); await p.waitForTimeout(3500); log('  CV posto no slide'); }
    } else {
      for(const c of (est.campos||[])){
        const r=(c.rot+' '+c.name+' '+est.titulo).toLowerCase();
        if(/address|location|city|where do you live|place/.test(r)&&!/checkbox/.test(c.type)){ log('  PULADO de proposito (endereco):',JSON.stringify(c.rot||c.name)); continue; }
        if(c.type==='checkbox'||c.type==='radio'){
          const rot=c.rot.toLowerCase(); const q=alvo; let marcar=null;
          if(/software|tool|program|application|which.*(use|know)|skills/.test(q))
            marcar=/^(maya|autodesk maya|zbrush|substance|substance painter|substance designer|houdini|marvelous|marvelous designer|3ds max|blender|unreal|unity|photoshop|nuke|mudbox|topogun|uvlayout|arnold|redshift|substance 3d)/.test(rot);
          else if(/role|position|title|job|looking for|interested in|discipline|department|area/.test(q))
            marcar=/(character|3d artist|3d|modeling|modelling|modeler|modeller|game art|art|animation)/.test(rot)&&!/(concept|2d|ui|ux|tech|programmer|engineer|producer|qa|marketing|sound|audio|writer|level)/.test(rot);
          else if(/type of (employment|contract|work)|employment type|availability/.test(q))
            marcar=/(full.?time|permanent|contract|freelance|remote|on.?site|hybrid|relocat)/.test(rot);
          else if(/europe|eu citizen|right to work|authori[sz]ed|work permit|visa/.test(q))
            marcar=/^(no|nej|non)$/.test(rot.trim());
          if(marcar===null){ naoSei.push(est.path+' | '+est.titulo+' | opcao: '+c.rot); continue; }
          const feito=await ev(([n,id,rot2,quer])=>{
            const el=id?document.getElementById(id):null;
            const e=el||[...document.querySelectorAll('input[name="'+n+'"]')].find(x=>(((x.labels&&x.labels[0]&&x.labels[0].innerText)||'').replace(/\s+/g,' ').trim())===rot2);
            if(!e) return 'sem campo';
            if(quer&&!e.checked) e.click(); if(!quer&&e.checked) e.click();
            return e.checked;},[c.name,c.id,c.rot,marcar]);
          log('  opcao',JSON.stringify(c.rot),'=>',marcar?'MARCAR':'deixar','| ficou:',JSON.stringify(feito));
          continue;
        }
        let v=null;
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
        const lido=await ev(([id,n,val])=>{
          const e=(id?document.getElementById(id):null)||document.querySelector('[name="'+n+'"]');
          if(!e) return 'sem campo';
          e.focus(); e.value=val; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));
          return (e.value||'').slice(0,60);},[c.id,c.name,v]);
        log('  campo',JSON.stringify(c.rot||c.name),'=>',JSON.stringify(/phone/.test(r)?'(telefone)':lido));
      }
    }
    if(!SUBMIT){ log('  MODO SECO: nao avanco o slide'); break; }
    // AVANCO: o clique navega DENTRO do evaluate. Erro de contexto destruido = clique deu certo.
    const antes=est.path;
    const av=await ev(()=>{
      const b=[...document.querySelectorAll('button,a,input[type=submit]')].filter(x=>!!x.offsetParent)
        .filter(x=>/^(next|continue|save|submit|done|finish|all done|complete|skip)$/i.test(((x.innerText||x.value||'')+'').replace(/\s+/g,' ').trim()));
      if(!b.length) return null;
      const pref=b.find(x=>/^(next|continue|save|submit|done|finish|all done|complete)$/i.test(((x.innerText||x.value||'')+'').trim()))||b[0];
      pref.click(); return ((pref.innerText||pref.value||'')+'').trim();});
    if(av&&av.__erro){ log('  avancar: evaluate morreu com',JSON.stringify(av.__erro),'- isso costuma ser NAVEGACAO, confiro pelo pathname'); }
    else log('  avancar:',JSON.stringify(av));
    await p.waitForLoadState('domcontentloaded',{timeout:30000}).catch(()=>{});
    await p.waitForTimeout(3500);
    const depois=await ev(()=>location.pathname);
    log('  pathname antes/depois:',antes,'->',JSON.stringify(depois));
    if(av===null&&!(av&&av.__erro)) break;
  }
  if(naoSei.length){ log('PERGUNTAS QUE EU NAO RESPONDI (sem chute):'); naoSei.slice(0,20).forEach(x=>log('  -',x)); }
  await p.goto(base+'/connect/dashboard',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000); await cookies();
  log('PROVA /connect/dashboard:',JSON.stringify(await ev(()=>((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,260))));
  await p.goto(base+'/connect/questions/start',{timeout:90000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(4000);
  log('PROVA /connect/questions/start depois de recarregar:',JSON.stringify(await ev(()=>({path:location.pathname,txt:((document.body&&document.body.innerText)||'').replace(/\s+/g,' ').slice(0,300)}))));
  await p.screenshot({path:'ttq_'+slug+'.png',fullPage:true}).catch(()=>{});
  log('REDE nao-GET:',JSON.stringify(rede.slice(-16)));
 }catch(e){ log('ERRO',e.message.split('\n')[0]); }
 await ctx.close();
})();
