// Jobvite. uso: node apply_jobvite.js <urlDaVagaApply> <slug> <ans.json> [--submit]
// PRIMEIRA FAMILIA JOBVITE DA CAMPANHA, mapeada em 08/09 na DNEG.
// ARMADILHA 1: o curl e o WebFetch nao passam no jobs.jobvite.com neste ambiente (o agente de
// Toronto registrou bloqueio de egresso), mas o NAVEGADOR passa e devolve 200. Nao registre
// Jobvite como porta morta so porque o curl falhou.
// ARMADILHA 2: /apply abre um PORTAO DE CONSENTIMENTO antes do formulario. E preciso escolher a
// regiao no select jv-country-select e seguir; so entao os campos montam.
// ARMADILHA 3, e ela decide o desenho do preenchedor: os atributos name do Jobvite sao
// ALEATORIOS POR SESSAO (input-yCcsXfwX, input-yAcsXfwV...). Preencher por name e impossivel:
// o que serve para a proxima vaga e casar pelo TEXTO DO ROTULO. Por isso o arquivo de
// respostas deste ATS e uma lista de pares [regex do rotulo, resposta].
const {chromium}=require('playwright'); const {abrirLocal}=require('./navegador'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname+'/';
const log=(...a)=>console.log('['+slug+']',...a);
const setv=async(p,sel,val)=>{ const el=await p.$(sel); if(!el) return false;
  await el.scrollIntoViewIfNeeded().catch(()=>{});
  await el.evaluate((e,v)=>{const proto=e.tagName==='TEXTAREA'?HTMLTextAreaElement:HTMLInputElement;
    const d=Object.getOwnPropertyDescriptor(proto.prototype,'value'); if(d&&d.set)d.set.call(e,v); else e.value=v;
    e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); e.dispatchEvent(new Event('blur',{bubbles:true}));},val);
  return true; };
const dump=async(p,tag)=>{
  const c=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null)
    .map(e=>({n:e.name||e.id||'',t:e.type||e.tagName,req:!!(e.required||e.getAttribute('aria-required')==='true'),v:(e.value||'').slice(0,35),
      lab:((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim().slice(0,60)})));
  log('=== CAMPOS ('+tag+'):',c.length,'==='); c.forEach(x=>log('   ',JSON.stringify(x)));
  const err=await p.evaluate(()=>[...new Set([...document.querySelectorAll('[class*="error"],[role="alert"],[class*="invalid"]')].filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<140))]);
  if(err.length){ log('=== VALIDACAO ('+tag+') ==='); err.forEach(e=>log('   !',e)); }
  return c; };
(async()=>{
 const b=await abrirLocal({headless:false});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2600},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-GB'})).newPage();
 try{
  await p.goto(url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(7000);
  for(const s of ['button:has-text("Accept")','#onetrust-accept-btn-handler']){ const el=await p.$(s); if(el){ await el.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }
  // portao de consentimento
  const sel=await p.$('#jv-country-select, select[name="jv-country-select"]');
  if(sel){
    const opts=await sel.$$eval('option',os=>os.map(o=>o.textContent.trim()));
    log('opcoes do portao:',JSON.stringify(opts));
    const quer=A.regiao||'Other';
    const alvo=opts.find(o=>new RegExp(quer,'i').test(o))||opts.find(o=>o&&!/select/i.test(o));
    await sel.selectOption({label:alvo}); log('portao =>',alvo);
    await p.waitForTimeout(1200);
    const seg=p.locator('button, input[type=submit], a').filter({hasText:/continue|next|proceed|submit|accept|agree/i}).first();
    if(await seg.count()){ await seg.click({timeout:10000}).catch(e=>log('portao seguir',e.message.split('\n')[0])); }
    await p.waitForTimeout(7000);
  } else log('sem portao de consentimento');
  log('url apos portao:',p.url().slice(0,130));
  await dump(p,'depois do portao');
  // preenche por ROTULO, nao por name
  const porRotulo=async(rot)=>p.evaluateHandle(r=>{
    const re=new RegExp(r,'i');
    const es=[...document.querySelectorAll('input,select,textarea')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null);
    for(const e of es){
      const lab=((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim();
      if(re.test(lab)) return e;
    }
    return null;
  },rot);
  for(const [rot,v] of (A.campos||[])){
    const h=await porRotulo(rot); const el=h.asElement();
    if(!el){ log('MISSING rotulo:',rot); continue; }
    const tag=await el.evaluate(e=>e.tagName);
    const tipo=await el.evaluate(e=>e.type||'');
    if(tipo==='checkbox'){
      // ARMADILHA MEDIDA EM 08/09: sem este ramo o setv escreve o VALOR DE TEXTO dentro da
      // caixa, a leitura de volta mostra v:"sim" parecendo preenchida, e a caixa fica
      // DESMARCADA. Consentimento desmarcado reprova o envio e o sintoma parece parede.
      await el.check({force:true}).catch(async()=>{ await el.click({force:true}); });
      log('caixa',rot.slice(0,40),'marcada:',await el.isChecked().catch(()=>'?'));
      await p.waitForTimeout(300); continue;
    }
    if(tag==='SELECT'){
      const opts=await el.$$eval('option',os=>os.map(o=>(o.textContent||'').trim()));
      const re=new RegExp('^\\s*'+String(v).replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\s*$','i');
      let alvo=opts.find(o=>re.test(o))||opts.find(o=>new RegExp(String(v),'i').test(o));
      if(!alvo){ log('SEM OPCAO para',rot,'quis',v,'| tinha:',JSON.stringify(opts.slice(0,14))); continue; }
      await el.selectOption({label:alvo});
      await el.evaluate(e=>e.dispatchEvent(new Event('change',{bubbles:true})));
      log('select',rot.slice(0,42),'=>',alvo);
    } else {
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.evaluate((e,val)=>{const proto=e.tagName==='TEXTAREA'?HTMLTextAreaElement:HTMLInputElement;
        const d=Object.getOwnPropertyDescriptor(proto.prototype,'value'); if(d&&d.set)d.set.call(e,val); else e.value=val;
        e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); e.dispatchEvent(new Event('blur',{bubbles:true}));},String(v));
      log('fill',rot.slice(0,42),'=>',String(v).slice(0,45));
    }
    await p.waitForTimeout(350);
  }
  // anexos: o input de arquivo do Jobvite nao tem name estavel, e pode estar ESCONDIDO atras
  // de um botao de anexar. Procura o botao primeiro, depois o input, inclusive invisivel.
  if((A.anexos||[]).length){
    const bot=p.locator('button, a, label').filter({hasText:/attach|upload|resume|cv|curriculum/i}).first();
    if(await bot.count()){ await bot.click({timeout:8000}).catch(e=>log('botao anexar',e.message.split('\n')[0])); await p.waitForTimeout(2500); log('cliquei no botao de anexar'); }
    const todos=await p.$$('input[type=file]');
    log('inputs de arquivo no DOM (visiveis ou nao):',todos.length);
  }
  // CORRIGIDO 18/09 22h45: a versao antiga jogava TODO arquivo de "anexos" no els[0]. Com dois
  // arquivos (CV e carta) o segundo sobrescrevia o primeiro no MESMO input, e o campo do outro
  // ficava vazio -- a tela do Rippling dizia "Cover letter No files added" depois do clique e
  // isso parecia reset do formulario. Cada arquivo vai para o input do seu indice.
  for(let ai=0; ai<(A.anexos||[]).length; ai++){
    const f=A.anexos[ai];
    const els=await p.$$('input[type=file]');
    if(!els.length){ log('MISSING input de arquivo para',f); break; }
    const alvo=els[Math.min(ai,els.length-1)];
    await alvo.setInputFiles(D+f).catch(e=>log('upload',e.message.split('\n')[0]));
    const nm=await alvo.evaluate(e=>e.files&&e.files.length?e.files[0].name+' '+e.files[0].size+'B':'(ZERO ARQUIVO)').catch(()=>'?');
    log('arquivo',ai,'=>',f,'| input',Math.min(ai,els.length-1),'de',els.length,'| leitura de volta:',nm);
    await p.waitForTimeout(5000);
  }
  for(const [n,f] of Object.entries(A.arquivos||{})){
    const els=await p.$$(`input[type=file][name="${n}"], input[type=file]#${n}`);
    if(!els.length){ log('MISSING arquivo',n); continue; }
    await els[els.length-1].setInputFiles(D+f).catch(e=>log('upload',e.message.split('\n')[0]));
    log('arquivo',n,'=>',f); await p.waitForTimeout(4000);
  }

  // ==== ACRESCENTADO 18/09 22h55 (Jhon A), MEDIDO NO RIPPLING DA BLIND SQUIRREL ====
  // POR QUE: o porRotulo acima casa por e.labels[0], aria-label e placeholder. O Rippling NAO
  // associa <label for> nas perguntas de questionario: o texto da pergunta e um DIV IRMAO, e o
  // dump devolve lab:"" em quatro campos OBRIGATORIOS. Sem isto o log diz "MISSING rotulo" e o
  // formulario reprova no envio por campo vazio, com cara de parede de ATS.
  // "blocos": [ {"pergunta":"regex do texto da pergunta","valor":"texto a digitar"},
  //             {"pergunta":"regex","opcao":"regex do texto da opcao"} ]
  // O container e escolhido pelo .last() do filtro hasText, que e o ancestral MAIS INTERNO
  // (ordem do documento), e o valor entra sempre com LEITURA DE VOLTA.
  for(const b of (A.blocos||[])){
    // CORRIGIDO 18/09 23h05, depois de 8 BLOCOS FALHAREM: o .last() do filtro hasText devolve o
    // ancestral mais interno, que no Rippling e o DIV DE TEXTO DA PERGUNTA, sem input nenhum
    // dentro. O sintoma ("BLOCO sem campo") e identico a "pergunta nao existe na tela". O
    // container precisa casar DUAS condicoes: o texto da pergunta E conter o alvo.
    const cont = b.opcao!==undefined
      ? p.locator('div,fieldset,section,li').filter({hasText:new RegExp(b.pergunta,'i')}).filter({hasText:new RegExp(b.opcao.replace(/[\^$]/g,''),'i')}).last()
      : p.locator('div,fieldset,section,li').filter({hasText:new RegExp(b.pergunta,'i')}).filter({has:p.locator('input,textarea')}).last();
    if(!(await cont.count().catch(()=>0))){ log('BLOCO nao achado:',b.pergunta.slice(0,45)); continue; }
    if(b.opcao!==undefined){
      const alvo=cont.getByText(new RegExp(b.opcao,'i')).last();
      if(!(await alvo.count().catch(()=>0))){ log('BLOCO sem opcao',b.pergunta.slice(0,32),'quis',b.opcao); continue; }
      await alvo.scrollIntoViewIfNeeded().catch(()=>{});
      await alvo.click({force:true,timeout:10000}).catch(e=>log('clique da opcao falhou',e.message.split('\n')[0]));
      await p.waitForTimeout(500);
      log('bloco RADIO',b.pergunta.slice(0,38),'=>',b.opcao);
    } else {
      // "n": indice do input dentro do bloco. Precisa existir porque um bloco pode ter varios:
      // o telefone do Rippling tem [seletor de pais, numero] e a data tem [dia, mes, ano].
      const todos=cont.locator('input[type=text],input:not([type]),textarea');
      const qtd=await todos.count().catch(()=>0);
      if(!qtd){ log('BLOCO sem campo',b.pergunta.slice(0,45)); continue; }
      const el=todos.nth(b.n||0);
      log('  (bloco',b.pergunta.slice(0,28),'tem',qtd,'inputs, uso o',b.n||0,')');
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.click({force:true}).catch(()=>{});
      await el.fill(String(b.valor)).catch(async()=>{ await el.type(String(b.valor),{delay:4}).catch(()=>{}); });
      const lido=await el.inputValue().catch(()=>'');
      log('bloco CAMPO',b.pergunta.slice(0,38),'=>',lido.length?('('+lido.length+' chars) '+lido.slice(0,60)):'(NAO ENTROU NADA)');
      await p.waitForTimeout(350);
    }
  }

  // ACRESCENTADO 18/09 22h47: CAMPO DE AUTOCOMPLETE. Hipotese medida na Blind Squirrel: o
  // Location do Rippling vem autopreenchido pela geolocalizacao como TEXTO, nao como opcao
  // escolhida, e o validador proprio do ATS pode recusar em silencio. "auto": [{"rotulo":
  // "regex do rotulo ou aria-label","texto":"o que digitar","opcao":"regex da sugestao"}]
  for(const a of (A.auto||[])){
    const h=await p.evaluateHandle(r=>{
      const re=new RegExp(r,'i');
      const es=[...document.querySelectorAll('input')].filter(e=>e.type!=='hidden'&&e.offsetParent!==null);
      for(const e of es){
        const lab=((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'').replace(/\s+/g,' ').trim();
        if(re.test(lab)) return e;
      }
      return null;
    },a.rotulo);
    const el=h.asElement();
    if(!el){ log('AUTO rotulo nao achado:',a.rotulo); continue; }
    await el.scrollIntoViewIfNeeded().catch(()=>{});
    await el.click({force:true}).catch(()=>{});
    await el.fill('').catch(()=>{});
    await el.type(String(a.texto),{delay:110}).catch(e=>log('AUTO digitacao',e.message.split('\n')[0]));
    await p.waitForTimeout(3500);
    const sug=await p.$$eval('[role=option], [role=listbox] *, li',es=>es.filter(e=>e.offsetParent!==null)
      .map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<90).slice(0,12)).catch(()=>[]);
    log('AUTO sugestoes para',a.texto,':',JSON.stringify(sug));
    let clicou=false;
    const alvo=p.locator('[role=option]').filter({hasText:new RegExp(a.opcao||a.texto,'i')}).first();
    if(await alvo.count().catch(()=>0)){ await alvo.click({force:true}).catch(()=>{}); clicou=true; }
    if(!clicou){ await el.press('ArrowDown').catch(()=>{}); await p.waitForTimeout(400); await el.press('Enter').catch(()=>{}); }
    await p.waitForTimeout(1500);
    log('AUTO',a.rotulo,'=> leitura de volta:',await el.inputValue().catch(()=>'?'),'| por opcao:',clicou);
  }
  await p.waitForTimeout(1500);
  await dump(p,'preenchido');
  await p.screenshot({path:D+'jv_'+slug+'.png',fullPage:true});
  const cap=await p.evaluate(()=>({frames:[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(s=>/captcha|challenges|turnstile/i.test(s)),widgets:document.querySelectorAll('.g-recaptcha,[data-sitekey],.h-captcha,.cf-turnstile').length}));
  log('captcha antes do clique:',JSON.stringify(cap));
  if(!SUBMIT){ log('MODO SECO — nada enviado'); await b.close(); return; }
  p.on('response',async r=>{ if(r.request().method()==='POST'&&!/analytics|track|sentry|doubleclick|google/i.test(r.url())){
    log('  RES',r.status(),r.url().slice(0,120));
    try{ const t=await r.text(); if(t&&t.length<600) log('    body:',t.replace(/\s+/g,' ').slice(0,300)); }catch(e){} } });
  const bots=await p.evaluate(()=>[...document.querySelectorAll('button,input[type=submit],input[type=button],a[role=button]')]
    .filter(e=>e.offsetParent!==null).map(e=>({txt:((e.innerText||e.value||'').trim()).slice(0,40),tipo:e.tagName+'/'+(e.type||'')})));
  log('BOTOES NA TELA:',JSON.stringify(bots));
  // ACRESCENTADO 18/09 23h12 (Jhon A): o laco do assistente abaixo procura o botao por uma
  // REGEX FIXA de rotulos de Jobvite, e no Rippling o botao de envio se chama "Apply". O log
  // disse "sem Next e sem envio no passo 1 - parei" com um BUTTON/submit escrito Apply na tela:
  // ou seja, o preenchimento inteiro foi feito e NADA foi enviado, e isso NAO e parede de ATS.
  // Quando "botao" vem no ans.json, clique-o por texto exato antes de tentar o assistente.
  if(A.botao){
    const bx=p.locator('button[type=submit], button').filter({hasText:new RegExp('^\\s*'+A.botao+'\\s*$','i')}).last();
    if(await bx.count().catch(()=>0)){
      await bx.scrollIntoViewIfNeeded().catch(()=>{});
      await p.waitForTimeout(1200);
      // CORRIGIDO 18/09 22h40: o click({force}) do locator NAO enviou. O log de 23h15 mostra
      // zero POST para ats.rippling.com e a tela voltando a "Cover letter No files added", com
      // os 17 campos cheios na leitura de volta e captcha zero. O apply_own.js ja tinha pago
      // esta licao: em formulario que escuta evento de mouse de verdade, clique sintetico com
      // force nao conta. Clique pelas COORDENADAS da caixa do botao, e so caia no force se o
      // botao nao tiver caixa.
      // DIAGNOSTICO 18/09 22h45: antes de culpar porteiro, pergunte se o botao esta DESABILITADO.
      // Clique em botao disabled nao gera POST e o sintoma e identico a Turnstile invisivel.
      const est=await bx.evaluate(e=>({dis:e.disabled,aria:e.getAttribute('aria-disabled'),
        tipo:e.type,form:!!e.form,valido:e.form?e.form.checkValidity():null,
        invalidos:e.form?[...e.form.querySelectorAll(':invalid')].map(x=>(x.name||x.id||x.tagName)+'/'+(x.type||'')).slice(0,10):[]})).catch(e=>({err:e.message}));
      log('estado do botao antes do clique:',JSON.stringify(est));
      const arqs=await p.$$eval('input[type=file]',es=>es.map(e=>e.files&&e.files.length?e.files[0].name:'(vazio)')).catch(()=>[]);
      log('inputs de arquivo antes do clique:',JSON.stringify(arqs));
      const cx=await bx.boundingBox().catch(()=>null);
      log('clicando no botao declarado:',A.botao,'| caixa:',JSON.stringify(cx));
      if(cx){ await p.mouse.move(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{});
              await p.waitForTimeout(250);
              await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(e=>log('clique de mouse falhou',e.message.split('\n')[0])); }
      else await bx.click({force:true,timeout:20000}).catch(e=>log('clique falhou',e.message.split('\n')[0]));
      await p.waitForTimeout(25000);
      log('url pos-clique:',p.url());
      const t2=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
      log('tela pos-clique:',t2.slice(0,1200));
      const erros=await p.$$eval('[class*="error"],[role="alert"],[class*="invalid"]',es=>[...new Set(es.filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<160))]).catch(()=>[]);
      log('erros na tela pos-clique:',JSON.stringify(erros));
    } else log('botao declarado NAO existe na tela:',A.botao);
  }
  // ARMADILHA 4: o Jobvite da DNEG e um ASSISTENTE DE VARIOS PASSOS. A primeira tela nao tem
  // botao de envio nenhum, so "Next". Procurar Submit ali e concluir que nao ha porta e erro:
  // avance pelos Next, preenchendo o que aparecer, ate o botao de envio existir.
  for(let passo=1; passo<=5; passo++){
    const bots=await p.evaluate(()=>[...document.querySelectorAll('button,input[type=submit],input[type=button],a[role=button]')]
      .filter(e=>e.offsetParent!==null).map(e=>((e.innerText||e.value||'').trim()).slice(0,40)));
    log('passo '+passo+' | botoes:',JSON.stringify(bots));
    // campos novos deste passo, preenchidos pelo mesmo mapa de rotulos
    for(const [rot,v] of (A.campos||[])){
      const h=await porRotulo(rot); const el=h.asElement(); if(!el) continue;
      const jaTem=await el.evaluate(e=>!!e.value); if(jaTem) continue;
      const tag=await el.evaluate(e=>e.tagName);
      const tipo=await el.evaluate(e=>e.type||'');
      if(tipo==='checkbox'){
        // ARMADILHA: sem este ramo o setv escreve o VALOR DE TEXTO dentro da caixa e a leitura
        // de volta mostra v:"sim" parecendo preenchido, com a caixa DESMARCADA. Consentimento
        // desmarcado reprova o envio e o sintoma parece parede.
        await el.check({force:true}).catch(async()=>{ await el.click({force:true}); });
        log('caixa',rot.slice(0,40),'marcada:',await el.isChecked().catch(()=>'?'));
        await p.waitForTimeout(300); continue;
      }
      if(tag==='SELECT'){
        const opts=await el.$$eval('option',os=>os.map(o=>(o.textContent||'').trim()));
        const alvo=opts.find(o=>new RegExp('^\\s*'+String(v)+'\\s*$','i').test(o))||opts.find(o=>new RegExp(String(v),'i').test(o));
        if(alvo){ await el.selectOption({label:alvo}); await el.evaluate(e=>e.dispatchEvent(new Event('change',{bubbles:true}))); log('  passo',passo,'select',rot.slice(0,34),'=>',alvo); }
      } else {
        await el.evaluate((e,val)=>{const proto=e.tagName==='TEXTAREA'?HTMLTextAreaElement:HTMLInputElement;
          const d=Object.getOwnPropertyDescriptor(proto.prototype,'value'); if(d&&d.set)d.set.call(e,val); else e.value=val;
          e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); e.dispatchEvent(new Event('blur',{bubbles:true}));},String(v));
        log('  passo',passo,'fill',rot.slice(0,34));
      }
      await p.waitForTimeout(250);
    }
    // ORDEM IMPORTA, e errei isso em 08/09: preencher SEMPRE antes de procurar o botao de
    // envio. O passo 2 da DNEG ja nasce com "Send Application" na tela e TRES obrigatorios
    // vazios (salario, disponibilidade, link do portfolio). Checar o botao primeiro fazia o
    // script enviar em branco e voltar com "The above information is required".
    // :visible e obrigatorio. Sem ele o locator casa um botao de envio ESCONDIDO no DOM,
    // count() passa, o clique estoura em timeout e o script pula o Next achando que enviou.
    const env=p.locator('button:visible, input[type=submit]:visible, input[type=button]:visible')
      .filter({hasText:/send application|submit application|^\s*(submit|send)\s*$/i}).first();
    if(await env.count()){
      await dump(p,'passo '+passo+', antes do envio');
      const vazios=await p.evaluate(()=>[...document.querySelectorAll('input,select,textarea')]
        .filter(e=>e.offsetParent!==null&&(e.required||e.getAttribute('aria-required')==='true')&&!e.value&&e.type!=='file')
        .map(e=>((e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.name||e.id||'?').replace(/\s+/g,' ').trim().slice(0,60)));
      log('obrigatorios vazios no passo do envio:',JSON.stringify(vazios));
      await p.screenshot({path:D+'jv_'+slug+'_antes_envio.png',fullPage:true});
      await env.click({timeout:20000}).catch(e=>log('envio',e.message.split('\n')[0]));
      log('CLIQUEI NO ENVIO no passo',passo);
      await p.waitForTimeout(4000);
      await dump(p,'logo depois do envio');
      break;
    }
    const nx=p.locator('button:visible, input[type=button]:visible').filter({hasText:/^\s*(Next|Continue)\s*$/i}).first();
    if(!(await nx.count())){ log('sem Next e sem envio no passo',passo,'- parei'); break; }
    await nx.click({timeout:20000}).catch(e=>log('next',e.message.split('\n')[0]));
    await p.waitForTimeout(6000);
    const err=await p.evaluate(()=>[...new Set([...document.querySelectorAll('[class*="error"],[role="alert"]')].filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<130))]);
    if(err.length) log('  validacao no passo '+passo+':',JSON.stringify(err.slice(0,8)));
  }
  for(let i=0;i<12;i++){ await p.waitForTimeout(5000);
    const t=(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ');
    // PROVA ESTRITA. "Thank you for considering a career at DNEG" e o texto de ABERTURA do
    // formulario e casou com uma regex frouxa em 08/09, produzindo falso positivo de envio.
    if(/application (has been )?(received|submitted|sent)|thank you for (applying|your application)|we have received your application|votre candidature a/i.test(t)){
      log('CONFIRMACAO em t+'+((i+1)*5)+'s:',t.slice(0,260)); break; } }
  const desafio=await p.evaluate(()=>[...document.querySelectorAll('iframe')].filter(f=>/bframe|hcaptcha|challenges/i.test(f.src||'')).filter(f=>{const r=f.getBoundingClientRect();return r.width>50&&r.height>50;}).length);
  log('DESAFIO VISIVEL depois do clique:',desafio);
  log('url final:',p.url().slice(0,140));
  log('tela final:',(await p.innerText('body').catch(()=>'')).replace(/\s+/g,' ').slice(0,400));
  await p.screenshot({path:D+'jv_'+slug+'_enviado.png',fullPage:true});
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'jv_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
