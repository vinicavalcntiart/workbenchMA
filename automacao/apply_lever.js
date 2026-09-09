// Lever filler. Uso: node apply_lever.js <applyUrl> <slug> <answers.json> [--submit]
const {chromium}=require('playwright'); const fs=require('fs');
const [url,slug,ansFile,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit'; const A=JSON.parse(fs.readFileSync(ansFile));
const CV='/tmp/claude-0/-home-user-workbenchMA/98c8eec1-87ea-55f1-bd77-423c5af62326/scratchpad/apply/Vini_Cavalcanti_CV.pdf';
// O telefone NUNCA fica escrito aqui: o repositorio e publico e o valida-dashboard.sh
// pegou este arquivo com o numero por extenso. Vem da variavel VINI_TEL, e o valor mora
// no documento privado do Drive 'CAMPANHA - dados pessoais dos formularios'.
const TEL=process.env.VINI_TEL;
if(!TEL){ console.error('[erro] falta a variavel de ambiente VINI_TEL com o telefone dele'); process.exit(1); }
const log=(...a)=>console.log(`[${slug}]`,...a);
(async()=>{
 const b=await chromium.launch({proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const ctx=await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1280,height:2400},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',locale:'en-US'});
 const p=await ctx.newPage();
 try{
  await p.goto(url,{timeout:120000,waitUntil:'networkidle'}).catch(()=>{}); await p.waitForSelector('input[name=name]',{timeout:60000});
  await p.setInputFiles('input[name=resume]',CV); for(let i=0;i<12;i++){ await p.waitForTimeout(3000); const t=(await p.$eval('.application-question.resume',e=>e.innerText).catch(()=>'')).replace(/\s+/g,' '); if(/Success/i.test(t)){ log('resume parsed'); break; } if(i===11) log('resume parse status:',t.slice(0,80)); }
  await p.fill('input[name=name]','Vini Cavalcanti'); await p.fill('input[name=email]','contact@vinicavalcanti.art');
  if(await p.$('input[name=phone]')) await p.fill('input[name=phone]',TEL);
  if(await p.$('input[name=org]')) await p.fill('input[name=org]','E-Line Media');
  // LOCAL, e este campo derrubou uma candidatura inteira em silencio na Avalanche (09/09).
  // O "Current location" do Lever e AUTOCOMPLETE ESTRUTURADO: o que vale nao e o texto
  // digitado no #location-input, e o input[name=location] escondido, que so recebe valor
  // quando uma SUGESTAO e escolhida. A versao antiga digitava o endereco inteiro (nenhuma
  // sugestao casava), apertava Escape, e depois "consertava" com .fill() no campo VISIVEL.
  // Resultado: a tela parecia preenchida, input[name=location] ficava VAZIO, e o clique no
  // Submit nao gerava POST nenhum, sem erro na tela. Isso e indistinguivel de parede de
  // captcha, e foi por pouco que nao virou "o Lever e parede" no registro da campanha.
  // O jeito certo: digitar POUCO (so a cidade), esperar a lista, ESCOLHER, e conferir o
  // campo escondido.
  const loc=await p.$('#location-input');
  if(loc){
    const valeu=async()=>(await p.$eval('input[name=location]',e=>e.value).catch(()=>''))||'';
    for(const termo of ['Olinda','Recife','Olinda, Brazil']){
      await loc.click().catch(()=>{});
      await loc.fill('').catch(()=>{});
      await loc.type(termo,{delay:90});
      await p.waitForTimeout(3500);
      let items=await p.$$('.dropdown-container li, .location-dropdown li, ul[role=listbox] li, li[role=option]');
      log('local: digitei', JSON.stringify(termo), '| sugestoes:', items.length);
      if(items.length){
        await items[0].click().catch(async()=>{ await p.keyboard.press('ArrowDown'); await p.keyboard.press('Enter'); });
        await p.waitForTimeout(1800);
      } else {
        await p.keyboard.press('ArrowDown').catch(()=>{});
        await p.keyboard.press('Enter').catch(()=>{});
        await p.waitForTimeout(1800);
      }
      const v=await valeu();
      if(v){ log('local ACEITO pelo campo estruturado =>', v); break; }
      log('local ainda vazio no input[name=location], tentando outro termo');
    }
    if(!(await valeu())) log('!! ATENCAO: input[name=location] continua VAZIO; o envio vai falhar em silencio');
  }
  for(const [k,v] of Object.entries(A.urls||{})){ const el=await p.$(`input[name="urls[${k}]"]`); if(el) { await el.fill(v); log('url',k); } else log('no url field',k); }
  if(A.comments && await p.$('textarea[name=comments]')) await p.fill('textarea[name=comments]',A.comments);
  for(const q of A.cards){
    const name=q.name; const esc=name.replace(/([\[\]])/g,'\\$1');
    if(q.type==='radio'||q.type==='checkbox'){ const el=await p.$(`input[name="${name}"][value="${q.value}"]`); if(el){ const lab=await p.$(`label:has(input[name="${name}"][value="${q.value}"])`); try{ if(lab) await lab.click({timeout:8000}); else await el.click({force:true,timeout:8000}); }catch(e){ await el.evaluate(x=>{x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));}); } log(q.type,q.label,'=>',q.value,'checked=',await el.isChecked()); } else log('MISSING',q.label,q.value); }
    else if(q.type==='select'){ const el=await p.$(`select[name="${name}"]`); if(el){ await el.selectOption({label:q.value}); log('select',q.label,'=>',q.value); } else log('MISSING select',q.label); }
    else { const el=await p.$(`input[name="${name}"], textarea[name="${name}"]`); if(el){ await el.fill(q.value); log('text',q.label); } else log('MISSING text',q.label); }
  }
  // consent checkboxes
  for(const c of (A.checks||[])){ const el=await p.$(c); if(el) { await el.check().catch(()=>{}); log('checked',c);} }
  await p.waitForTimeout(800); await p.screenshot({path:`filled_${slug}.png`,fullPage:true});
  if(!SUBMIT){ log('DRY RUN done'); await b.close(); return; }
  p.on('response',async r=>{ if(r.request().method()==='POST' && !/hcaptcha|challenge-platform|snowplow/.test(r.url())){ let t=''; try{t=(await r.text()).slice(0,300);}catch(e){} log('POST-RES',r.status(),r.url().slice(0,100),t.replace(/\s+/g,' ')); } });
  p.on('requestfailed',r=>{ if(r.method()==='POST') log('POST-FAILED',r.url().slice(0,100),r.failure()&&r.failure().errorText); });
  const cb=await p.$('a:has-text("dismiss"), button:has-text("accept"), a:has-text("accept")'); if(cb) await cb.click().catch(()=>{});
  // TERCEIRA VEZ QUE A MESMA COISA ACONTECE (GoHire, BambooHR e agora Lever): p.click() num
  // botao fora da area visivel NAO dispara nada e NAO levanta erro, e o resultado vira
  // "NOT CONFIRMED" sem nenhum POST na rede, que e indistinguivel de parede de captcha.
  // Rolar ate o botao e clicar por coordenada e o que separa os dois diagnosticos.
  // Antes de clicar, LER o que de fato ficou nos obrigatorios. O campo de local do Lever e um
  // autocomplete estruturado: digitar sem escolher sugestao pode deixar o campo "preenchido"
  // aos olhos e invalido para o servidor, e nesse caso o Submit nao gera POST nenhum.
  const obrig=await p.evaluate(()=>{
    const out={};
    for(const n of ['name','email','phone','location','org']){
      const e=document.querySelector(`input[name="${n}"]`);
      out[n]= e ? ((e.value||'(VAZIO)')+(e.getAttribute('aria-invalid')==='true'?' [INVALIDO]':'')) : '(AUSENTE)';
    }
    const r=document.querySelector('input[name=resume]');
    out.resume = r && r.files && r.files.length ? r.files[0].name : '(SEM ARQUIVO)';
    out.invalidos=[...document.querySelectorAll('[aria-invalid="true"],.error,.invalid')].map(e=>(e.getAttribute('name')||e.innerText||'').trim().slice(0,40)).filter(Boolean).slice(0,6);
    return out;
  });
  log('leitura de volta dos obrigatorios:', JSON.stringify(obrig));
  const sb=await p.$('#btn-submit');
  if(sb){
    await sb.scrollIntoViewIfNeeded().catch(()=>{});
    await p.waitForTimeout(900);
    const cx=await sb.boundingBox().catch(()=>null);
    log('caixa do #btn-submit:', JSON.stringify(cx), '| habilitado:', await sb.isEnabled().catch(()=>'?'));
    if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{});
    else await sb.click({force:true}).catch(()=>{});
  } else log('!! #btn-submit nao existe');
  await p.waitForTimeout(15000);
  // captcha challenge?
  const chal=await p.$$eval('iframe',fs=>fs.filter(f=>/hcaptcha|recaptcha/i.test(f.src)&&f.offsetParent!==null&&f.getBoundingClientRect().height>100).length);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  const ok=/application has been submitted|thank you for applying|thanks for applying|application submitted|we have received|your application was submitted/i.test(txt) || /thanks|confirmation/i.test(p.url());
  const errs=await p.$$eval('[class*="error"]',els=>els.filter(e=>e.offsetParent!==null).map(e=>e.innerText.trim().slice(0,80)).filter(Boolean));
  await p.screenshot({path:`result_${slug}.png`,fullPage:true});
  log(ok?'SUBMITTED OK':'NOT CONFIRMED','| captcha challenge visible:',chal,'| url:',p.url(),'| errs:',JSON.stringify(errs.slice(0,6)),'| text:',txt.slice(0,250));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:`err_${slug}.png`,fullPage:true}).catch(()=>{}); }
 await b.close();
})();
