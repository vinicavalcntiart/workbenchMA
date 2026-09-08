// Recruitee generico. uso: node apply_recruitee.js <ans.json> <slug> [--submit]
// ans.json: {"url":"...","texto":{"<nomeDoCampo>":"valor"},"radios":{"<id da pergunta>":"Yes|No"},"cover":true}
const {chromium}=require('playwright'); const fs=require('fs');
const [ansFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname+'/';
// TELEFONE NUNCA NO CODIGO: o repositorio e PUBLICO e a porta do valida-dashboard.sh reprova.
// Passe por ambiente: VINI_TEL='<formato internacional>' sh hb_run.sh apply_recruitee5.js ...
// Regra do documento privado: com seletor de pais separado, so os digitos; com campo unico, o
// formato internacional. Aqui o Recruitee ja traz um seletor proprio que vem com +1.
const B={name:'Vini Cavalcanti',email:'contact@vinicavalcanti.art',phone:process.env.VINI_TEL||''};
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2600},locale:'en-US'})).newPage();
 try{
  await p.goto(A.url,{timeout:120000,waitUntil:'domcontentloaded'});
  await p.waitForTimeout(8000);
  const typeIn=async(sel,val,lbl)=>{
    const el=await p.$(sel); if(!el){log('SEM CAMPO',lbl||sel);return false;}
    await el.click(); await el.fill(''); await el.type(String(val),{delay:12});
    const got=await el.inputValue(); log('escrito',lbl||sel,'=>',got.length,'chars');
    return got.length>0;
  };
  await typeIn('[name="candidate.name"]',B.name,'name');
  await typeIn('[name="candidate.email"]',B.email,'email');
  await typeIn('[name="candidate.phone"]',A.phone||B.phone,'phone');
  await p.setInputFiles('[name="candidate.cv"]',D+'Vini_Cavalcanti_CV.pdf'); await p.waitForTimeout(4000);
  if(await p.$('[name="candidate.coverLetterFile"]')){
    await p.setInputFiles('[name="candidate.coverLetterFile"]',D+'Vini_Cavalcanti_Cover_Letter.pdf').catch(e=>log('cover:',e.message.slice(0,60)));
    await p.waitForTimeout(3000);
  }
  for(const [k,v] of Object.entries(A.texto||{})){
    await typeIn(`[name="candidate.openQuestionAnswers.${k}.content"]`,v,k);
  }
  for(const [k,v] of Object.entries(A.radios||{})){
    const loc=p.locator(`input[name="candidate.openQuestionAnswers.${k}.flag"]`);
    const n=await loc.count(); let done=false;
    for(let i=0;i<n;i++){
      const id=await loc.nth(i).getAttribute('id');
      let lab='';
      if(id) lab=await p.locator(`label[for="${id.replace(/"/g,'')}"]`).first().innerText().catch(()=>'');
      if(!lab) lab=(i===0?'Yes':'No');
      if(lab.trim().toLowerCase()===String(v).toLowerCase()){
        if(id) await p.locator(`label[for="${id.replace(/"/g,'')}"]`).first().click({force:true}).catch(async()=>{await loc.nth(i).check({force:true});});
        else await loc.nth(i).check({force:true});
        done=true; break;
      }
    }
    if(!done){ log('RADIO nao casou',k,v); }
    const chosen=await p.evaluate(k=>{const e=document.querySelector(`input[name="candidate.openQuestionAnswers.${k}.flag"]:checked`);if(!e)return null;const l=document.querySelector('label[for="'+CSS.escape(e.id)+'"]');return l?l.innerText.trim():e.value;},k);
    log('radio',k,'ficou =>',chosen);
  }
  // selects (openQuestionAnswers.N.content como <select>)
  for(const [k,v] of Object.entries(A.selects||{})){
    await p.selectOption(`select[name="candidate.openQuestionAnswers.${k}.content"]`,{label:v}).catch(e=>log('select',k,e.message.slice(0,50)));
  }
  // ARMADILHA MEDIDA EM 08/09, e ela custou o diagnostico inteiro da familia Recruitee:
  // o arquivo de respostas ja trazia as chaves radiosContent e flags, e o preenchedor
  // NAO TRATAVA NENHUMA DAS DUAS. Ignorava em silencio, o formulario reprovava na
  // validacao ("This field is required and can not be left empty") e a rodada anterior
  // leu isso como parede de captcha. Nao era captcha: era campo obrigatorio vazio.
  // radiosContent: radio cujo VALUE e o proprio texto do rotulo, sob .content
  for(const [k,v] of Object.entries(A.radiosContent||{})){
    const sel=`input[name="candidate.openQuestionAnswers.${k}.content"]`;
    const n=await p.locator(sel).count();
    let ok=false;
    for(let i=0;i<n;i++){
      const val=await p.locator(sel).nth(i).getAttribute('value');
      if((val||'').trim().toLowerCase()===String(v).trim().toLowerCase()){
        const id=await p.locator(sel).nth(i).getAttribute('id');
        if(id) await p.locator(`label[for="${id}"]`).first().click({force:true}).catch(async()=>{await p.locator(sel).nth(i).check({force:true});});
        else await p.locator(sel).nth(i).check({force:true});
        ok=true; break;
      }
    }
    if(!ok){
      const vals=await p.locator(sel).evaluateAll(es=>es.map(e=>e.value));
      log('radioContent NAO CASOU',k,'quis',v,'| opcoes:',JSON.stringify(vals));
    } else log('radioContent',k,'=>',v);
  }
  // flags: consentimentos que sao pergunta aberta, sem id e sem label
  for(const k of (A.flags||[])){
    const sel=`input[name="candidate.openQuestionAnswers.${k}.flag"]`;
    const n=await p.locator(sel).count();
    if(!n){ log('flag NAO EXISTE',k); continue; }
    await p.locator(sel).first().check({force:true}).catch(async e=>{
      const id=await p.locator(sel).first().getAttribute('id');
      if(id) await p.locator(`label[for="${id}"]`).first().click({force:true});
      else log('flag',k,e.message.split('\n')[0]);
    });
    const st=await p.locator(sel).first().isChecked().catch(()=>'?');
    log('flag',k,'marcada:',st);
  }
  // consentimentos
  const cbs=await p.$$('input[type=checkbox][name*="consent"]');
  for(const c of cbs){ const id=await c.getAttribute('id');
    if(id) await p.locator(`label[for="${id}"]`).first().click({force:true}).catch(async()=>{await c.check({force:true});});
    else await c.check({force:true}); }
  log('consentimentos marcados:',cbs.length);
  await p.waitForTimeout(1500);
  await p.screenshot({path:D+'filled_'+slug+'.png',fullPage:true});
  const capt=await p.evaluate(()=>[...document.querySelectorAll('iframe')].map(f=>f.src).filter(s=>/captcha/i.test(s)).length);
  log('iframes de captcha:',capt);
  // LER A VALIDACAO ANTES DE CLICAR: campo obrigatorio vazio produz exatamente o mesmo
  // sintoma de parede (tela nao muda, campos continuam preenchidos, nenhum email chega).
  const errosAntes=await p.evaluate(()=>[...new Set([...document.querySelectorAll('*')]
    .filter(e=>e.children.length===0&&e.offsetParent!==null)
    .map(e=>(e.innerText||'').trim())
    .filter(t=>/required|can not be left empty|cannot be empty|obrigat/i.test(t)&&t.length<120))]);
  log('validacao ANTES do envio:',JSON.stringify(errosAntes));
  const vazios=await p.evaluate(()=>[...document.querySelectorAll('input[required],select[required],textarea[required]')]
    .filter(e=>e.offsetParent!==null&&!e.value&&e.type!=='file'&&e.type!=='checkbox'&&e.type!=='radio')
    .map(e=>e.name||e.id));
  log('obrigatorios ainda vazios:',JSON.stringify(vazios));
  if(!SUBMIT){ log('MODO SECO — nada enviado'); await b.close(); return; }
  p.on('request',r=>{ if(r.method()==='POST'&&!/google|linkedin|indeed|analytics/i.test(r.url())) log('  REQ',r.url().slice(0,120)); });
  p.on('response',async r=>{ if(r.request().method()==='POST'&&!/google|linkedin|indeed|analytics|checksiteconfig/i.test(r.url())){ log('  RES',r.status(),r.url().slice(0,120)); try{log('    body:',(await r.text()).slice(0,250));}catch(e){} } });
  await p.locator('button:has-text("Send")').last().click();
  // MEDICAO NOVA DE 08/09: em 07/09 o captcha do Recruitee (captcha-base.recruiteecdn.com,
  // widget tipo hsw, PROVA DE TRABALHO e nao desafio humano) travou por 15s e por 120s sem a
  // tela mudar. O dossie registrou que ha um botao "Skip" SOBREPOSTO, mas nunca diz que ele
  // foi clicado. Skip e afordancia do proprio site, nao burla: se aparecer desafio HUMANO
  // (imagem, hCaptcha, "select all"), o script para e nao tenta resolver.
  for(let i=0;i<15;i++){
    await p.waitForTimeout(6000);
    const t=await p.innerText('body').catch(()=>'');
    if(/thank you|received|success/i.test(t)){ log('CONFIRMACAO NA TELA em t+'+((i+1)*6)+'s'); break; }
    // desafio humano? entao para.
    const humano=await p.evaluate(()=>{
      const fr=[...document.querySelectorAll('iframe')].filter(f=>/hcaptcha.*challenge|recaptcha\/api2\/bframe|challenges\.cloudflare/i.test(f.src||''));
      const grandes=fr.filter(f=>{const r=f.getBoundingClientRect();return r.width>50&&r.height>50;});
      const txt=/select all images|click the shape|verify you are human|choisissez|escolha todas/i.test(document.body.innerText||'');
      return grandes.length+(txt?1:0);
    });
    if(humano){ log('DESAFIO HUMANO APARECEU em t+'+((i+1)*6)+'s. Parando: desafio nao se burla.'); break; }
    if(i===0||i===2){
      const est=await p.evaluate(()=>({
        capIframes:[...document.querySelectorAll('iframe')].filter(f=>/captcha/i.test(f.src||'')).map(f=>f.src.slice(0,90)),
        botoes:[...document.querySelectorAll('button,a,[role=button]')].filter(e=>e.offsetParent!==null).map(e=>(e.innerText||'').trim()).filter(t=>t&&t.length<28).slice(0,20)
      }));
      log('estado do captcha em t+'+((i+1)*6)+'s:',JSON.stringify(est));
      // clica o Skip, se ele existir, na pagina ou dentro de um frame do captcha
      let clicou=false;
      const skipPg=p.locator('button, a, [role=button]').filter({hasText:/^\s*Skip\s*$/}).first();
      if(await skipPg.count()){ await skipPg.click({force:true,timeout:8000}).then(()=>{clicou=true}).catch(e=>log('skip pagina',e.message.split('\n')[0])); }
      if(!clicou){
        for(const f of p.frames()){
          if(!/captcha/i.test(f.url())) continue;
          const sf=f.locator('button, a').filter({hasText:/^\s*Skip\s*$/}).first();
          if(await sf.count()){ await sf.click({force:true,timeout:8000}).then(()=>{clicou=true}).catch(e=>log('skip frame',e.message.split('\n')[0])); }
          if(clicou) break;
        }
      }
      log('cliquei no Skip:',clicou);
    }
  }
  const r=await p.evaluate(()=>({url:location.href,txt:document.body.innerText.replace(/\s+/g,' ').slice(0,900)}));
  log('RESULTADO',JSON.stringify(r));
  await p.screenshot({path:D+'result_'+slug+'.png',fullPage:true});
 }catch(e){log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'err_'+slug+'.png',fullPage:true}).catch(()=>{});}
 await b.close();
})();
