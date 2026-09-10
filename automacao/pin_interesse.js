// Pinpoint, rota REGISTER YOUR INTEREST (/register-your-interest/new).
//
// Por que nao serve o apply_pinpoint.js: aquele preenche a candidatura a uma VAGA, cujos campos
// se chamam application_form[application][...]. O banco de interesse usa outro prefixo,
// job_seeker_form[job_seeker][...], e tem uma coisa que o outro nao tem: COMBOBOX de verdade.
// Locations, Departments, "Are you a...", "Where did you hear about this position?" e
// "Are you willing to relocate for the role?" sao campos de texto que abrem lista; o <select>
// irmao existe mas vem escondido, e escrever nele direto e a armadilha do BambooHR de hoje,
// onde selectOption falhava em silencio. Aqui se digita, espera a lista e ESCOLHE, e depois se
// confere o que ficou escrito na tela.
//
// Uso: VINI_TEL='...' sh hb_run.sh pin_interesse.js <respostas.json> <slug> [--submit]
const {chromium}=require('playwright'); const fs=require('fs');
const [ansFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname;
for(const k of Object.keys(A.texto||{})) if(A.texto[k]==='__TEL__'){
  if(!process.env.VINI_TEL){ console.error('[erro] o arquivo pede __TEL__ e falta VINI_TEL'); process.exit(1); }
  A.texto[k]=process.env.VINI_TEL;
}
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2800},locale:'en-US',
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 p.on('request',r=>{ if(r.method()==='POST') log('[pedido POST]', r.url().slice(0,110)); });
 p.on('requestfailed',r=>{ if(r.method()==='POST') log('[pedido POST FALHOU]', r.url().slice(0,110), r.failure()&&r.failure().errorText); });
 p.on('response',async r=>{ if(r.request().method()==='POST'){ log('[rede POST]', r.status(), r.url().slice(0,110)); } });
 try{
  await p.goto(A.url,{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(8000);
  for(const t of ['Accept all','Accept All','Accept','Allow all','I agree']){
    const e=await p.$('button:has-text("'+t+'")'); if(e&&await e.isVisible().catch(()=>false)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }

  for(const [sel,v] of Object.entries(A.texto||{})){
    const el=await p.$(sel); if(!el){ log('NAO ACHEI o campo',sel); continue; }
    // MEDIDO NA ROCKSTEADY EM 10/09, e este e o pior defeito que o modo seco ja pegou.
    // O campo de LinkedIn do Pinpoint, #job_seeker_form_linkedin_url, e
    // <input type="hidden">: existe no DOM, entao o $() acha e NAO cai no "NAO ACHEI".
    // Mas type() nao escreve em campo escondido, e o pior nao e o campo ficar vazio: o
    // FOCO CONTINUA NO CAMPO ANTERIOR, entao os 42 caracteres da URL do LinkedIn foram
    // digitados dentro do TELEFONE, que passou de 14 para 56 caracteres. Enviar assim
    // entregaria ao estudio um telefone lixo e nenhum LinkedIn, e o log antigo so dizia
    // "(NAO ENTROU NADA)" na linha do LinkedIn, sem nunca ligar uma coisa na outra.
    // Campo escondido se preenche pelo DOM, com os eventos que o Rails escuta, e nunca
    // pelo teclado. E depois se tira o foco, para nao vazar no proximo campo.
    const escondido=await el.evaluate(e=>e.type==='hidden'||e.offsetParent===null&&getComputedStyle(e).display==='none').catch(()=>false);
    if(escondido){
      await el.evaluate((e,val)=>{ e.value=val;
        e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); }, String(v)).catch(()=>{});
      const lidoH=await el.evaluate(e=>e.value).catch(()=>'');
      log('campo',sel,'ESCONDIDO, preenchido pelo DOM =>', lidoH===String(v)? '('+lidoH.length+' chars) CONFERE' : '!! NAO CONFERE, NAO ENVIE');
      continue;
    }
    await el.scrollIntoViewIfNeeded().catch(()=>{});
    await el.click({force:true}).catch(()=>{}); await el.fill('').catch(()=>{});
    await el.type(String(v),{delay:3}).catch(()=>{});
    await el.evaluate(e=>e.blur()).catch(()=>{});
    const lido=await el.inputValue().catch(()=>'');
    log('campo',sel, lido.length? '('+lido.length+' chars) '+lido.slice(0,50) : '(NAO ENTROU NADA)');
  }

  if(A.cv){ const fi=await p.$('input[type=file]');
    if(fi){ await fi.setInputFiles(D+'/'+A.cv); await p.waitForTimeout(9000); log('CV anexado', A.cv); } else log('NAO ACHEI input de arquivo'); }

  // COMBOBOX: clicar, digitar, esperar a lista, escolher a opcao cujo texto casa.
  // Combo por TITULO da pergunta, e nao por indice: no Pinpoint o indice do slot muda quando
  // uma pergunta CONDICIONAL entra (a da Fenris so revela "Would you need a VISA sponsorship"
  // depois que a localizacao e respondida). Achar pelo titulo sobrevive a isso.
  const acharPorTitulo=async(titulo)=>await p.evaluate(t=>{
    const h=[...document.querySelectorAll('input[name$="[title]"]')].find(e=>(e.value||'').trim().toLowerCase()===t.trim().toLowerCase());
    if(!h) return null;
    const m=h.name.match(/answers_attributes\]\[(\d+)\]/); if(!m) return null;
    // MEDIDO NA FENRIS EM 09/09, e foi o que derrubou o envio: o servidor recusou com
    // "Answers boolean answer can't be blank". A pergunta de visto NAO e caixa de texto, e
    // BOOLEANA, entao o campo dela nao se chama _text_answer e sim _boolean_answer, e o
    // controle e um par de radios Yes/No. Montar o id sempre como _text_answer achava um
    // campo que nao existe, o combo era pulado com "NAO ACHEI", e o formulario ia incompleto.
    // Agora eu devolvo o SLOT e digo que forma de resposta existe de verdade naquele slot.
    const base='job_seeker_form_job_seeker_answers_attributes_'+m[1];
    const pre='job_seeker_form[job_seeker][answers_attributes]['+m[1]+']';
    const achaRadios=()=>[...document.querySelectorAll('input[type=radio]')]
        .filter(e=>(e.name||'').startsWith(pre)).map(e=>({id:e.id, valor:e.value}));
    const radios=achaRadios();
    for(const suf of ['text_answer','boolean_answer','choice_answer','answer']){
      if(document.getElementById(base+'_'+suf)) return {tipo:'campo', id:base+'_'+suf, slot:m[1]};
    }
    if(radios.length) return {tipo:'radio', radios, slot:m[1]};
    return null;
  }, titulo);

  for(const c of (A.combos||[])){
    let sel=c.sel;
    if(c.titulo){ const achado=await acharPorTitulo(c.titulo);
      if(!achado){ log('NAO ACHEI a pergunta pelo titulo:', JSON.stringify(c.titulo)); continue; }
      if(achado.tipo==='radio'){
        // Pergunta booleana: nao ha lista para abrir, ha dois radios. Clico o que casa com a
        // resposta pedida e leio de volta o que ficou marcado, que e o unico teste que vale.
        const alvo=String(Array.isArray(c.valores)?c.valores[0]:c.valores);
        // MEDIDO NA FENRIS EM 10/09: os radios booleanos do Pinpoint nao valem "Yes" e "No",
        // valem "true" e "false". Casar pela primeira letra fazia "Yes" nao achar nada e a
        // pergunta obrigatoria ficava em branco, que e exatamente o "boolean answer can't be
        // blank" que o servidor devolveu ontem. A traducao e explicita, nunca por aproximacao:
        // num campo de formulario de emprego, chute vira resposta falsa.
        const comoBooleano={yes:'true', no:'false', sim:'true', 'nao':'false', true:'true', false:'false'}[alvo.toLowerCase()];
        const escolha=achado.radios.find(r=>String(r.valor).toLowerCase()===alvo.toLowerCase())
                   || (comoBooleano && achado.radios.find(r=>String(r.valor).toLowerCase()===comoBooleano));
        log('pergunta', JSON.stringify(c.titulo), 'e BOOLEANA no slot', achado.slot,
            '| radios oferecidos:', JSON.stringify(achado.radios.map(r=>r.valor)));
        if(!escolha){ log('!! nenhum radio casa com', JSON.stringify(alvo), ', NAO ENVIE'); continue; }
        const r=await p.$('#'+escolha.id.replace(/([^\w-])/g,'\\$1'));
        if(r){ await r.scrollIntoViewIfNeeded().catch(()=>{}); await r.check({force:true}).catch(async()=>{ await r.click({force:true}).catch(()=>{}); }); }
        const marcado=r? await r.isChecked().catch(()=>false) : false;
        log('combo',c.rotulo||c.titulo,'| pedi',JSON.stringify(alvo),'| radio',JSON.stringify(escolha.valor),
            marcado?'| MARCADO, CONFERE':'| !! NAO MARCOU, NAO ENVIE');
        continue;
      }
      sel='#'+achado.id; log('pergunta', JSON.stringify(c.titulo), 'esta no slot', sel); }
    const el=await p.$(sel); if(!el){ log('NAO ACHEI o combo',sel); continue; }
    for(const alvo of (Array.isArray(c.valores)?c.valores:[c.valores])){
      await el.scrollIntoViewIfNeeded().catch(()=>{});
      await el.click({force:true}).catch(()=>{});
      await p.waitForTimeout(700);
      await el.fill('').catch(()=>{});
      await el.type(String(alvo).slice(0,14),{delay:70}).catch(()=>{});
      await p.waitForTimeout(1800);
      // MEDIDO NA FENRIS EM 09/09: ha combo deste ATS que NAO abre a lista digitando, so com
      // seta para baixo. Sem isto, "What is your current location?" e "Are you a..." voltavam
      // lista VAZIA e o campo ficava em branco na leitura final, sem erro nenhum na tela.
      if(!(await p.$$('[role=option], li[id*="option"]')).length){
        await p.keyboard.press('ArrowDown').catch(()=>{}); await p.waitForTimeout(1700); }
      let opcoes=await p.$$('[role=option], li[id*="option"], div[class*="option"]:not([class*="options"])');
      // Se digitar nao abriu lista, abre sem filtro: ha combo que so lista no clique.
      if(!opcoes.length){ await el.fill('').catch(()=>{}); await el.click({force:true}).catch(()=>{}); await p.waitForTimeout(1600);
        opcoes=await p.$$('[role=option], li[id*="option"], div[class*="option"]:not([class*="options"])'); }
      const textos=[];
      for(const o of opcoes){ const t=((await o.innerText().catch(()=>''))||'').replace(/\s+/g,' ').trim(); if(t) textos.push(t); }
      log('   lista oferecida:', JSON.stringify(textos.slice(0,14)));
      // CASAMENTO EXATO PRIMEIRO. O prefixo sozinho escolheu "Fenris Creations Employee" quando
      // eu pedi "Fenris Creations Website" (09/09), que seria AFIRMAR uma indicacao inexistente.
      // Prefixo curto e chute; num campo de formulario de emprego, chute vira mentira.
      let escolhido=null, idx=-1;
      idx=textos.findIndex(t=>t.toLowerCase()===String(alvo).toLowerCase());
      if(idx<0) idx=textos.findIndex(t=>t.toLowerCase().startsWith(String(alvo).toLowerCase()));
      if(idx<0 && String(alvo).length>=8) idx=textos.findIndex(t=>t.toLowerCase().includes(String(alvo).toLowerCase()));
      if(idx>=0){ await opcoes[idx].click({force:true}).catch(()=>{}); escolhido=textos[idx]; }
      else if(c.aceitaAproximado && textos.length){ await opcoes[0].click({force:true}).catch(()=>{}); escolhido=textos[0]+' (aproximado, autorizado no arquivo)'; }
      await p.waitForTimeout(1200);
      // CONFERENCIA NA TELA, e ela existe por um erro medido em 09/09: pedi "Other" na pergunta
      // de localizacao e o clique caiu em "USA/Canada". O log dizia "escolhi Other" porque olhava
      // o texto da OPCAO que eu mandei clicar, nao o que o controle passou a mostrar. Num
      // formulario de emprego isso nao e bug de log, e resposta falsa entregue ao estudio.
      // MEDIDO EM 10/09: ler so o innerText do contentor devolvia STRING VAZIA em sete dos oito
      // combos, e o alarme "NAO CONFERE" era falso. Neste ATS o valor escolhido nao fica no
      // texto da caixa: fica no value do proprio input, ou na option selecionada do <select>
      // irmao escondido, ou num chip fora do contentor. Entao a leitura tenta as tres, nesta
      // ordem, e so declara vazio se as tres vierem vazias.
      const naTela=await el.evaluate(e=>{
        const v=(e.value||'').trim();
        if(v) return v;
        const form=e.closest('form')||document;
        const nome=(e.name||e.id||'').replace(/_text_answer$/,'');
        for(const s of form.querySelectorAll('select')){
          const mesmo=(s.name||s.id||'').includes(nome)|| (nome&&nome.includes((s.name||s.id||'')));
          if(!mesmo) continue;
          const sel=[...s.selectedOptions].map(o=>(o.textContent||'').trim()).filter(Boolean).join(', ');
          if(sel) return sel;
        }
        const box=e.closest('[class*="container"]')||e.closest('[class*="control"]')||e.parentElement;
        const t=box? (box.innerText||'').replace(/\s+/g,' ').trim() : '';
        if(t) return t.slice(0,80);
        const pai=box&&box.parentElement;
        return pai? (pai.innerText||'').replace(/\s+/g,' ').trim().slice(0,80) : '';
      }).catch(()=>'');
      const bate = naTela.toLowerCase().includes(String(alvo).toLowerCase().replace(/\?$/,''));
      log('combo',c.rotulo||sel,'| pedi',JSON.stringify(alvo),'| cliquei em',JSON.stringify(escolhido||'(NADA)'),'| a TELA mostra',JSON.stringify(naTela),bate?'| CONFERE':'| !! NAO CONFERE, NAO ENVIE');
    }
  }

  // aceite obrigatorio, pelo rotulo e nunca por varredura cega
  for(const cb of await p.$$('input[type=checkbox]')){
    const rot=await cb.evaluate(e=>{ const l=e.id&&document.querySelector('label[for="'+CSS.escape(e.id)+'"]'); return ((l&&l.innerText)||e.getAttribute('aria-label')||(e.parentElement&&e.parentElement.innerText)||'').replace(/\s+/g,' ').trim(); }).catch(()=>'');
    if(/allow us to process|process your personal|consent|i agree/i.test(rot) && !/do not|opt.?out|marketing/i.test(rot)){
      await cb.check({force:true}).catch(async()=>{ await cb.click({force:true}).catch(()=>{}); });
      log('aceite marcado:', rot.slice(0,70), '=>', await cb.isChecked().catch(()=>'?'));
    }
  }

  await p.waitForTimeout(1200);
  // leitura de volta imediatamente antes do clique
  for(const sel of Object.keys(A.texto||{})){ const v=await p.$eval(sel,e=>e.value).catch(()=>null);
    log('  leitura final',sel,'=>', v===null?'(CAMPO SUMIU)': (String(v).trim()? String(v).length+' chars':'(VAZIO)')); }
  const obrig=await p.evaluate(()=>[...document.querySelectorAll('input[required],select[required],textarea[required]')].map(e=>({
    n:e.name||e.id, tipo:e.type, ok: e.type==='checkbox'? e.checked : !!(e.value||'').trim()})));
  log('  obrigatorios:',JSON.stringify(obrig));
  await p.screenshot({path:D+'/pin_'+slug+'_pre.png',fullPage:true}).catch(()=>{});
  log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
  if(!SUBMIT){ log('MODO SECO, nada enviado'); await b.close(); return; }

  const sb=await p.$('button[type=submit], button:has-text("Submit")');
  if(!sb){ log('!! nao achei o Submit'); await b.close(); return; }
  await sb.scrollIntoViewIfNeeded().catch(()=>{}); await p.waitForTimeout(900);
  const cx=await sb.boundingBox().catch(()=>null); log('caixa do Submit:',JSON.stringify(cx));
  if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{}); else await sb.click({force:true}).catch(()=>{});
  await p.waitForTimeout(16000);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  await p.screenshot({path:D+'/pin_'+slug+'_post.png',fullPage:true}).catch(()=>{});
  const ok=/thank you|thanks|registered|received|we'll be in touch|we will be in touch|success|interest has been/i.test(txt);
  log(ok?'RESPOSTA POSITIVA NA TELA':'NAO CONFIRMADA','| url:',p.url());
  log('TEXTO:',txt.slice(0,900));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'/pin_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
