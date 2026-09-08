// Dayforce HCM (jobs.dayforcehcm.com). Uso: node apply_dayforce.js <urlDaVaga> <slug> <ans.json> [--submit]
// PRIMEIRO ATS DESSA FAMILIA NA CAMPANHA, mapeado em 08/09 na Eidos-Montreal.
// Fluxo: /jobs/<id> -> Apply -> /apply?flowSelection=true -> "Apply without an Account"
//        -> /apply/manualApplication -> modal de Privacy Notice -> assistente de TRES passos.
// ARMADILHA 1: o modal fecha com SAVE, nao com Next. O Next fica ATRAS do modal e da timeout.
// ARMADILHA 2, medida em 08/09 e cara: os identificadores do Dayforce sao ID e NAO name. Selecionar
// por [name="..."] devolve null em TODOS os campos, o preenchedor loga MISSING na lista inteira e a
// rodada parece parede quando o formulario esta ali, montado e visivel. Selecione por #id.
// ARMADILHA 3: o bloco Personal Information e um sub-formulario com botao UPDATE proprio. Sem
// clicar Update, o Next nao avanca e o clique morre em timeout.
// ARMADILHA 4, medida em 08/09: el.fill() PINTA o campo mas nao avisa o framework. A validacao
// segue dizendo "required" com o texto na tela e a leitura de volta diz VAZIO com razao.
// Use o setter nativo mais input/change/blur, que e o mesmo remedio do setv do workable2.
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile));
const D='/tmp/claude-0/-home-user-workbenchMA/98c8eec1-87ea-55f1-bd77-423c5af62326/scratchpad/apply/';
const log=(...a)=>console.log(`[${slug}]`,...a);

// setter nativo: o unico jeito de um input controlado aceitar valor de robo.
const setv=async(p,sel,val)=>{
  const el=await p.$(sel); if(!el){ log('MISSING',sel); return false; }
  await el.scrollIntoViewIfNeeded().catch(()=>{});
  await el.evaluate((e,v)=>{
    const proto = e.tagName==='TEXTAREA'?HTMLTextAreaElement:HTMLInputElement;
    const d = Object.getOwnPropertyDescriptor(proto.prototype,'value');
    if(d&&d.set) d.set.call(e,v); else e.value=v;
    e.dispatchEvent(new Event('input',{bubbles:true}));
    e.dispatchEvent(new Event('change',{bubbles:true}));
    e.dispatchEvent(new Event('blur',{bubbles:true}));
  },val);
  return true;
};

(async()=>{
 const b=await chromium.launch({proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1300,height:2600},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-CA'});
 const p=await ctx.newPage();

 // ARMADILHA 6, medida em 08/09: os combos do Dayforce sao rc-select (o mesmo motor do
 // Ant Design; o id "rc_select_1" da tela entrega). A lista NAO fica dentro do campo, e
 // desenhada num portal no fim do body, e a busca so acontece com digitacao de teclado.
 // Selecionar por [role=option] generico devolve lista vazia e a rodada parece parede.
 const OPT_SEL='[class*="select-item-option"], .rc-virtual-list-holder-inner > div, [class*="select-dropdown"] [role="option"], [role="option"], li[id*="option"]';
 async function pick(id, want){
   const sel=`#${id}, [name="${id}"]`;
   const el=await p.$(sel); if(!el){ log('MISSING combo',id); return false; }
   const tag=await el.evaluate(e=>e.tagName);
   if(tag==='SELECT'){
     const opts=await el.$$eval('option',os=>os.map(o=>({v:o.value,t:(o.textContent||'').trim()})));
     const re=new RegExp(want,'i'); const hit=opts.find(o=>re.test(o.t));
     if(!hit){ log('combo',id,'sem opcao para',want,'| tinha:',JSON.stringify(opts.slice(0,15))); return false; }
     await el.selectOption({label:hit.t}).catch(async()=>{ await el.selectOption(hit.v); });
     await el.evaluate(e=>e.dispatchEvent(new Event('change',{bubbles:true})));
     log('combo SELECT',id,'=>',hit.t); return true;
   }
   const readOpts=async()=>p.$$eval(OPT_SEL,
     es=>[...new Set(es.filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<80))]);
   // as alternativas separadas por | sao uma ORDEM DE PREFERENCIA, nao um regex solto.
   // Com um regex unico o find devolve a primeira opcao da LISTA que casa com qualquer
   // alternativa: em 08/09 isso escolheu "Other" tendo "Company Website" disponivel, e o
   // "Other" abriu um campo obrigatorio novo (Additional Details) que travou o Next.
   const prefs=want.split('|');
   const acha=opts=>{ for(const pref of prefs){ const r=new RegExp(pref,'i'); const c=opts.find(o=>r.test(o)); if(c) return c; } return null; };
   const termos=[''].concat(prefs.map(t=>t.replace(/[\\^$]/g,'').slice(0,8)));
   for(const termo of termos){
     await el.scrollIntoViewIfNeeded().catch(()=>{});
     await el.click({timeout:8000}).catch(()=>{});
     await p.waitForTimeout(900);
     if(termo){ await p.keyboard.type(termo,{delay:90}); await p.waitForTimeout(1500); }
     let opts=await readOpts();
     if(!opts.length){ await p.keyboard.press('ArrowDown'); await p.waitForTimeout(900); opts=await readOpts(); }
     const choice=acha(opts);
     if(choice){
       await p.locator(`${OPT_SEL} >> text="${choice}"`).first().click({timeout:6000})
         .catch(async()=>{ await p.keyboard.press('Enter'); });
       await p.waitForTimeout(700);
       log('combo LISTA',id,'=>',choice,`(busca: "${termo||'sem digitar'}")`); return true;
     }
     log('  combo',id,'busca',JSON.stringify(termo),'nao casou | visiveis:',JSON.stringify(opts.slice(0,12)));
     if(!opts.length){
       // ainda cego: mostra o que existe de dropdown na pagina, para parar de adivinhar
       const dd=await p.$$eval('[class*="dropdown"],[class*="menu"]',es=>es.filter(e=>e.offsetParent!==null)
         .map(e=>({cls:(e.className||'').toString().slice(0,70),txt:(e.innerText||'').replace(/\s+/g,' ').slice(0,120)})).slice(0,5));
       log('  dropdowns visiveis:',JSON.stringify(dd));
     }
     await p.keyboard.press('Escape').catch(()=>{});
     await p.waitForTimeout(400);
   }
   log('combo',id,'FALHOU para',want); return false;
 }

 // despeja TODO campo visivel com rotulo e obrigatoriedade, mais o texto de validacao.
 // E assim que se descobre o que o bloco "Additional Details" quer, sem adivinhar.
 async function dump(tag){
   const campos=await p.$$eval('input,select,textarea',es=>es.filter(e=>e.type!=='hidden'&&e.offsetParent!==null).map(e=>{
     const lab=(e.labels&&e.labels[0]?e.labels[0].innerText:'')||e.getAttribute('aria-label')||e.placeholder||'';
     return {id:e.id||'', tipo:e.type||e.tagName, req:!!(e.required||e.getAttribute('aria-required')==='true'), val:(e.value||'').slice(0,40), lab:lab.replace(/\s+/g,' ').trim().slice(0,70)};
   }));
   log(`=== CAMPOS VISIVEIS (${tag}): ${campos.length} ===`);
   campos.forEach(c=>log('   ',JSON.stringify(c)));
   const erros=await p.$$eval('[class*="error"],[class*="invalid"],[role="alert"]',
     es=>[...new Set(es.filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').replace(/\s+/g,' ').trim()).filter(t=>t&&t.length<160))]);
   if(erros.length){ log(`=== VALIDACAO (${tag}) ===`); erros.forEach(e=>log('   !',e)); }
   return campos;
 }

 try{
  await p.goto(url.replace(/\/?$/,'')+'/apply/manualApplication?applicationSource=Manual',{waitUntil:'domcontentloaded',timeout:90000});
  await p.waitForTimeout(6000);
  for(const s of ['button:has-text("Accept")','#onetrust-accept-btn-handler']){ const el=await p.$(s); if(el){ await el.click().catch(()=>{}); await p.waitForTimeout(1200); break; } }
  const cb=await p.$('input[type=checkbox]');
  if(cb){ await cb.click({force:true}).catch(()=>{}); log('caixa da politica:',await cb.isChecked().catch(()=>'?')); }
  const save=await p.$('button:has-text("Save")');
  if(save){ await save.click({timeout:15000}).catch(e=>log('save',e.message.split('\n')[0])); log('cliquei Save do modal'); }
  else log('ATENCAO: nao achei o botao Save do modal');
  // ESPERA MEDIDA EM 08/09: os campos so MONTAM depois que o modal fecha. Sem esta espera,
  // o preenchedor roda cedo, todos os campos voltam MISSING e a rodada parece parede.
  await p.waitForSelector('#jobPostingApplication_personalInfo_email',{timeout:45000})
    .then(()=>log('formulario montou'))
    .catch(()=>log('ATENCAO: o formulario nao montou em 45s'));
  await p.waitForTimeout(1500);

  await dump('antes de preencher');

  // ARMADILHA 5, a mais cara de todas, medida em 08/09: o upload do CV dispara o PARSE do
  // curriculo, e o parse REESCREVE o bloco Personal Information inteiro. Preencher antes de
  // subir o arquivo apaga tudo que nao esteja no CV: na rodada das 15h sobreviveram email,
  // firstName e lastName (que o parser leu do PDF) e morreram confirmEmail, linkedIn, city e
  // telefone. Por isso os ARQUIVOS VAO PRIMEIRO, e so depois o texto e os combos.
  for(const [n,f] of Object.entries(A.arquivos||{})){
    const els=await p.$$(`input#${n}, input[name="${n}"]`);
    if(!els.length){ log('MISSING arquivo',n); continue; }
    await els[els.length-1].setInputFiles(D+f).catch(e=>log('upload',e.message.split('\n')[0]));
    log('arquivo',n,'=>',f,'( inputs com esse name:',els.length,')');
    await p.waitForTimeout(5000);
  }
  await p.waitForTimeout(4000);
  await dump('depois do parse do CV');

  // combos antes do texto: cada escolha de rc-select redesenha o bloco.
  for(const [n,v] of Object.entries(A.combo||{})){ await pick(n,String(v)); await p.waitForTimeout(600); }

  // TELEFONE, regra do documento privado: com seletor de pais separado ("Country dialing
  // code", que aqui e o rc_select_1), o campo do numero leva SO OS DIGITOS. Repetir o +55
  // faz a validacao recusar. Sem o seletor, vai o formato internacional.
  const temDDI=!!(await p.$('#rc_select_1'));
  const tel=temDDI?(process.env.VINI_TEL_DIG||''):(process.env.VINI_TEL_INTL||process.env.VINI_TEL||'');
  if(tel){ A.texto=Object.assign({},A.texto,{'jobPostingApplication_personalInfo_mobilePhone':tel}); log('seletor de DDI presente:',temDDI,'-> telefone no formato',temDDI?'so digitos':'internacional'); }

  for(const [n,v] of Object.entries(A.texto||{})){
    const ok=await setv(p,`#${n}, [name="${n}"]`,String(v));
    if(ok) log('fill',n,'=>',String(v).slice(0,45));
    await p.waitForTimeout(250);
  }
  // segunda passada: campos que so NASCEM depois de uma escolha de combo (ex.: o
  // "Additional Details" que o Dayforce abre quando a origem escolhida e "Other").
  // Nao existem no primeiro dump, entao precisam de uma rodada propria.
  for(const [n,v] of Object.entries(A.texto2||{})){
    if(!(await p.$(`#${n}, [name="${n}"]`))) { log('texto2',n,'nao apareceu, nao era necessario'); continue; }
    await setv(p,`#${n}, [name="${n}"]`,String(v));
    log('fill (2a passada)',n,'=>',String(v).slice(0,45));
    await p.waitForTimeout(250);
  }
  await p.waitForTimeout(1500);
  await p.screenshot({path:`df_${slug}_p1.png`,fullPage:true});
  const rb=await p.evaluate(ns=>ns.map(n=>{const e=document.getElementById(n)||document.querySelector(`[name="${n}"]`);return [n, e?(e.value||'(VAZIO)').slice(0,50):'(NAO ENCONTRADO)'];}),
    Object.keys(A.texto||{}).concat(Object.keys(A.combo||{})));
  rb.forEach(([n,v])=>log('  leitura de volta',n,'=>',v));

  const upd=await p.$('button:has-text("Update")');
  if(upd){ await upd.scrollIntoViewIfNeeded().catch(()=>{}); await upd.click({timeout:15000}).catch(e=>log('update',e.message.split('\n')[0])); log('cliquei Update do bloco pessoal'); await p.waitForTimeout(4000); }
  else log('sem botao Update no bloco pessoal');

  await dump('depois do Update');

  // ARMADILHA 7: o Update COLAPSA o bloco pessoal num resumo so de leitura e redesenha a
  // pagina inteira. Um handle de Next pego antes disso clica sem erro e sem efeito. Pegue o
  // botao DEPOIS do Update, e confirme a virada pelo texto do passo, nao pela URL: o
  // assistente e uma SPA e a URL nao muda entre Candidate Info, Questionnaire e Submit.
  const noPasso1=async()=>/Personal Information|Import Resume/i.test(await p.innerText('body').catch(()=>''));
  for(let t=1;t<=3;t++){
    const nx=p.locator('button:has-text("Next")').last();
    if(!(await nx.count())){ log('sem botao Next na tentativa',t); break; }
    await nx.scrollIntoViewIfNeeded().catch(()=>{});
    await nx.click({timeout:20000}).catch(e=>log('next',e.message.split('\n')[0]));
    await p.waitForTimeout(6000);
    if(!(await noPasso1())){ log('avancou para o passo 2 na tentativa',t); break; }
    log('ainda no passo 1 depois da tentativa',t);
  }
  log('url apos Next:',p.url());
  const t2=(await p.innerText('body')).replace(/\s+/g,' ');
  log('=== TEXTO DA TELA APOS NEXT ===');
  log(t2.slice(0,2200));
  await dump('passo 2');

  // QUESTIONARIO: os radios do Dayforce nao tem id, so um value numerico (29, 30, 31...)
  // que muda de vaga para vaga. Por isso a resposta e casada por TEXTO da pergunta mais
  // TEXTO da opcao, e nao pelo value: fica auditavel no arquivo de respostas e continua
  // valendo em outro estudio da mesma familia.
  // A pergunta de autorizacao de trabalho e respondida com a VERDADE, sempre.
  if((A.radios||[]).length){
    const raio=await p.evaluate(()=>[...document.querySelectorAll('input[type=radio]')].map(r=>{
      const lab=((r.labels&&r.labels[0]?r.labels[0].innerText:'')||r.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim();
      let ctx='',n=r; for(let i=0;i<12&&n;i++){ n=n.parentElement; if(n&&(n.innerText||'').length>ctx.length) ctx=n.innerText; }
      return {val:r.value,lab,ctx:ctx.replace(/\s+/g,' ').trim().slice(0,110)};
    }));
    log('=== RADIOS COM CONTEXTO ==='); raio.forEach(r=>log('   ',JSON.stringify(r)));
  }
  for(const [pergunta,resposta] of (A.radios||[])){
    const alvo=await p.evaluate(([qre,are])=>{
      const rq=new RegExp(qre,'i'), ra=new RegExp(are,'i');
      const rs=[...document.querySelectorAll('input[type=radio]')];
      for(const r of rs){
        const lab=((r.labels&&r.labels[0]?r.labels[0].innerText:'')||r.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim();
        if(!ra.test(lab)) continue;
        let n=r, achou=false;
        for(let i=0;i<12&&n;i++){ n=n.parentElement; if(n&&rq.test((n.innerText||'').replace(/\s+/g,' '))){ achou=true; break; } }
        if(achou){ r.setAttribute('data-alvo','1'); return lab.slice(0,60); }
      }
      return null;
    },[pergunta,resposta]);
    if(!alvo){ log('RADIO nao encontrado:',pergunta,'/',resposta); continue; }
    await p.click('input[type=radio][data-alvo="1"]',{force:true}).catch(e=>log('radio',e.message.split('\n')[0]));
    const marcado=await p.$eval('input[type=radio][data-alvo="1"]',e=>e.checked).catch(()=>'?');
    await p.evaluate(()=>document.querySelectorAll('[data-alvo]').forEach(e=>e.removeAttribute('data-alvo')));
    log('radio',JSON.stringify(pergunta),'=>',alvo,'| marcado:',marcado);
    await p.waitForTimeout(400);
  }
  if((A.radios||[]).length){
    await p.screenshot({path:`df_${slug}_q.png`,fullPage:true});
    // passo 3: a tela de Submit, onde mora o captcha
    for(let t=1;t<=2;t++){
      const nx=p.locator('button:has-text("Next")').last();
      if(!(await nx.count())) break;
      await nx.scrollIntoViewIfNeeded().catch(()=>{});
      await nx.click({timeout:20000}).catch(e=>log('next q',e.message.split('\n')[0]));
      await p.waitForTimeout(6000);
      if(!/Questionnaire 1 of/i.test(await p.innerText('body').catch(()=>''))){ log('avancou para o passo 3 na tentativa',t); break; }
      log('ainda no questionario depois da tentativa',t);
    }
    const t3=(await p.innerText('body')).replace(/\s+/g,' ');
    log('=== TEXTO DO PASSO 3 ===');
    log(t3.slice(0,1600));
    await dump('passo 3');
    const capt=await p.evaluate(()=>({
      frames:[...document.querySelectorAll('iframe')].map(f=>f.src||'').filter(s=>/recaptcha|hcaptcha|turnstile|challenges/i.test(s)).length,
      widgets:document.querySelectorAll('.g-recaptcha,[data-sitekey],.h-captcha,.cf-turnstile').length}));
    log('CAPTCHA no passo 3:',JSON.stringify(capt));
    await p.screenshot({path:`df_${slug}_p3.png`,fullPage:true});

    // aceite obrigatorio antes do Submit
    const ack=await p.$('#jobPostingApplication_userAcknowledged, input[type=checkbox][id*="cknowledg"]');
    if(ack){ await ack.click({force:true}).catch(e=>log('ack',e.message.split('\n')[0]));
      log('aceite marcado:',await ack.isChecked().catch(()=>'?')); await p.waitForTimeout(1000); }
    else log('ATENCAO: nao achei a caixa de aceite');

    if(SUBMIT){
      const antes=p.url();
      const sb=p.locator('button:has-text("Submit")').last();
      await sb.scrollIntoViewIfNeeded().catch(()=>{});
      await sb.click({timeout:25000}).catch(e=>log('submit',e.message.split('\n')[0]));
      await p.waitForTimeout(12000);
      // um desafio VISIVEL depois do clique e o padrao do Workable. Se aparecer, para aqui:
      // desafio nao se burla, a vaga vira item da fila do Vini.
      const desafio=await p.evaluate(()=>{
        const fr=[...document.querySelectorAll('iframe')].filter(f=>/recaptcha\/api2\/bframe|hcaptcha.*challenge|challenges\.cloudflare/i.test(f.src||''));
        return fr.filter(f=>{const r=f.getBoundingClientRect();return r.width>50&&r.height>50;}).length;
      });
      const dep=(await p.innerText('body')).replace(/\s+/g,' ');
      const prova=(dep.match(/[^.]*\b(thank you|application (has been )?(submitted|received)|successfully submitted|we have received)\b[^.]*/i)||[])[0]||'';
      log('DESAFIO VISIVEL depois do Submit:',desafio);
      log('url antes:',antes); log('url depois:',p.url());
      log('PROVA DE ENVIO (texto na tela):',prova||'(nenhuma)');
      log('trecho da tela depois do Submit:',dep.slice(0,700));
      await p.screenshot({path:`df_${slug}_enviado.png`,fullPage:true});
    }
  }
  await p.screenshot({path:`df_${slug}_p2.png`,fullPage:true});
  if(!SUBMIT){ log('DRY RUN: parei antes de enviar'); await b.close(); return; }
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:`df_err_${slug}.png`,fullPage:true}).catch(()=>{}); }
 await b.close();
})();
