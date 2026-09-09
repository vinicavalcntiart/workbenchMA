// Preenchedor de formulario proprio em WIX. Uso: sh hb_run.sh apply_wix.js <respostas.json> <slug> [--submit]
//
// Duas coisas medidas que este script existe para tratar:
// 1. O Wix nao usa name= nos campos: o id e um uuid gerado e o unico rotulo estavel e o
//    aria-label. Entao o casamento e POR aria-label, nunca por seletor fixo.
// 2. Ha DOIS input[type=file] identicos, ambos rotulados "Upload File" no DOM. Qual e o
//    curriculo e qual e a carta so se sabe pelo texto da SECAO em volta. Foi exatamente a
//    armadilha do BambooHR em 09/09, onde o primeiro campo era a carta e o obrigatorio era o
//    CV. Aqui o script LE o texto em volta de cada um e diz no log onde pos cada arquivo.
const {chromium}=require('playwright'); const fs=require('fs');
const [ansFile,slug,flag]=process.argv.slice(2); const SUBMIT=flag==='--submit';
const A=JSON.parse(fs.readFileSync(ansFile)); const D=__dirname;
const log=(...a)=>console.log('['+slug+']',...a);
(async()=>{
 const b=await chromium.launch({headless:false,proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const p=await (await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1400,height:2600},locale:'en-US',acceptDownloads:true,
   userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'})).newPage();
 p.on('response',async r=>{ if(r.request().method()==='POST'&&!/recaptcha|sentry|analytics|beat|bi\.wix/i.test(r.url())){ let t=''; try{t=(await r.text()).slice(0,200);}catch(e){} log('[rede POST]',r.status(),r.url().slice(0,110),t.replace(/\s+/g,' ')); } });
 try{
  await p.goto(A.url,{waitUntil:'domcontentloaded',timeout:120000}); await p.waitForTimeout(9000);
  for(const t of ['Accept','Accept All','I agree','Allow all']){ const e=p.getByRole('button',{name:new RegExp('^'+t+'$','i')}).first();
    if(await e.count().catch(()=>0)){ await e.click().catch(()=>{}); await p.waitForTimeout(1500); break; } }

  // ORDEM MEDIDA NA GLINDA EM 09/09, e ela custou uma tentativa de envio: o upload de arquivo
  // do Wix REDESENHA o formulario e LIMPA os campos de texto ja digitados. Na primeira tentativa
  // o log mostrou os campos preenchidos, o anexo subiu, e o clique no Submit devolveu
  // "Enter a first name. Enter a last name. Enter an email address" com o formulario em branco.
  // Nada foi enviado, porque a validacao do proprio Wix barrou antes. O conserto e a ordem:
  // ANEXO PRIMEIRO, texto depois, e leitura de volta de tudo imediatamente antes do clique.
  // COMO SE SABE QUAL CAMPO E QUAL, e as duas tentativas que falharam antes desta.
  // (1) Subir parentes ate o MAIOR texto pega a secao inteira, que cita 'Cover Letter' E
  //     'Resume*' juntos: os dois campos casaram com 'cover' e a carta foi anexada duas vezes.
  // (2) Parar no MENOR ancestral que cita um rotulo so tambem falha, porque neste Wix os dois
  //     input[type=file] sao IRMAOS no mesmo container: nao existe ancestral que separe.
  // O que separa e a POSICAO NO DOCUMENTO: acho os elementos-rotulo cujo texto proprio e
  // exatamente 'Cover Letter' ou 'Resume', e para cada campo de arquivo pego o rotulo mais
  // proximo ANTES dele. Isso continua valendo se a casa inverter a ordem dos dois campos.
  const fis=await p.$$('input[type=file]');
  log('input[type=file] encontrados:',fis.length);
  const rotulos=await p.evaluate(()=>{
    const out=[];
    document.querySelectorAll('*').forEach((e,idx)=>{
      if(e.children.length>1) return;
      const t=(e.textContent||'').replace(/\s+/g,' ').trim();
      if(/^cover\s*letter\s*\*?$/i.test(t)) out.push({tipo:'carta', t});
      else if(/^(resume|cv|curriculum vitae)\s*\*?$/i.test(t)) out.push({tipo:'cv', t});
    });
    return out;
  });
  log('rotulos de anexo achados na pagina:', JSON.stringify(rotulos));
  for(let i=0;i<fis.length;i++){
    const tipo=await fis[i].evaluate(e=>{
      const alvos=[...document.querySelectorAll('*')].filter(x=>{
        if(x.children.length>1) return false;
        const t=(x.textContent||'').replace(/\s+/g,' ').trim();
        return /^cover\s*letter\s*\*?$/i.test(t) || /^(resume|cv|curriculum vitae)\s*\*?$/i.test(t);
      });
      let melhor=null;
      for(const a of alvos){
        // 2 = o rotulo vem ANTES do campo no documento
        if(a.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) melhor=a;
      }
      if(!melhor) return '';
      const t=(melhor.textContent||'').trim();
      return /cover/i.test(t) ? 'carta' : 'cv';
    }).catch(()=>'');
    let arq=null;
    if(tipo==='carta' && A.carta) arq=A.carta;
    else if(tipo==='cv' && A.cv) arq=A.cv;
    else if(A.cv && i===fis.length-1) arq=A.cv;   // sem rotulo, o CV vai no ULTIMO, que e o obrigatorio
    log('  campo de arquivo',i,'| rotulo mais proximo antes dele:',JSON.stringify(tipo||'(nenhum)'),'| vou anexar:',arq||'(nenhum)');
    if(arq){ await fis[i].setInputFiles(D+'/'+arq).catch(e=>log('  falha ao anexar',e.message.slice(0,60))); await p.waitForTimeout(3500); }
  }
  // radio por aria-label
  for(const r of (A.radios||[])){
    const el=await p.$('input[type=radio][aria-label="'+r+'"]');
    if(el){ await el.scrollIntoViewIfNeeded().catch(()=>{}); await el.check({force:true}).catch(async()=>{ await el.click({force:true}).catch(()=>{}); });
      log('radio',JSON.stringify(r),'marcado =',await el.isChecked().catch(()=>'?')); }
    else log('NAO ACHEI o radio', JSON.stringify(r));
  }
  // arquivos: identifica pela SECAO em volta, nunca pela ordem cega
  // campos de texto por aria-label
  for(const [rotulo,valor] of Object.entries(A.campos||{})){
    const el=await p.$('[aria-label="'+rotulo+'"]');
    if(!el){ log('NAO ACHEI o campo', JSON.stringify(rotulo)); continue; }
    await el.scrollIntoViewIfNeeded().catch(()=>{});
    await el.click({force:true}).catch(()=>{});
    await el.fill('').catch(()=>{});
    await el.type(String(valor),{delay:3}).catch(()=>{});
    const lido=await el.inputValue().catch(()=>'');
    log('campo',JSON.stringify(rotulo), lido.length? '('+lido.length+' chars) '+lido.slice(0,55) : '(NAO ENTROU NADA)');
  }
  await p.waitForTimeout(1500);
  // leitura de volta pelo NOME DO ARQUIVO no corpo, porque contar input mente (medido no Greenhouse)
  const nomes=[A.cv,A.carta].filter(Boolean);
  const visto=await p.evaluate(ns=>{ const t=document.body.innerText; return ns.filter(n=>t.includes(n)); },nomes);
  log('arquivos visiveis na pagina depois do upload:',JSON.stringify(visto));
  // LEITURA DE VOLTA FINAL, imediatamente antes do clique. Sem ela o envio vai com campo
  // apagado e a tela devolve erro de validacao que parece parede.
  let vazio=false;
  for(const rotulo of Object.keys(A.campos||{})){
    const v=await p.$eval('[aria-label="'+rotulo+'"]',e=>e.value).catch(()=>null);
    if(v===null){ log('  leitura final', JSON.stringify(rotulo), '=> (CAMPO SUMIU)'); vazio=true; continue; }
    if(!v.trim()){ log('  leitura final', JSON.stringify(rotulo), '=> (VAZIO)'); vazio=true; continue; }
    log('  leitura final', JSON.stringify(rotulo), '=>', v.length, 'chars');
  }
  if(vazio) log('!! PARE: campo obrigatorio vazio na leitura final. O Wix limpa campo quando redesenha.');
  await p.screenshot({path:D+'/wix_'+slug+'_pre.png',fullPage:true}).catch(()=>{});
  log('captcha iframes:',JSON.stringify(await p.$$eval('iframe',fs=>fs.map(f=>f.src).filter(s=>/recaptcha|hcaptcha|turnstile|datadome/i.test(s))).catch(()=>[])));
  if(!SUBMIT){ log('MODO SECO, nada enviado'); await b.close(); return; }

  // Submit por COORDENADA. Botao fora da area visivel nao dispara nada e nao levanta erro:
  // aconteceu tres vezes em 09/09 (GoHire, BambooHR, Lever) e vira "NAO CONFIRMADA" sem POST,
  // que e indistinguivel de parede de captcha.
  const sb=await p.$('button:has-text("Submit"), [role=button]:has-text("Submit")');
  if(!sb){ log('!! nao achei o botao Submit'); await b.close(); return; }
  await sb.scrollIntoViewIfNeeded().catch(()=>{}); await p.waitForTimeout(900);
  const cx=await sb.boundingBox().catch(()=>null);
  log('caixa do Submit:',JSON.stringify(cx));
  if(cx) await p.mouse.click(cx.x+cx.width/2, cx.y+cx.height/2).catch(()=>{});
  else await sb.click({force:true}).catch(()=>{});
  await p.waitForTimeout(15000);
  const txt=(await p.innerText('body')).replace(/\s+/g,' ');
  const chal=await p.$$eval('iframe',fs=>fs.filter(f=>/hcaptcha|recaptcha/i.test(f.src)&&f.getBoundingClientRect().height>100).length).catch(()=>0);
  await p.screenshot({path:D+'/wix_'+slug+'_post.png',fullPage:true}).catch(()=>{});
  const ok=/thank you|thanks for|submitted|received|we'll be in touch|we will be in touch|success/i.test(txt);
  log(ok?'ENVIADA (confirmar pelo texto abaixo)':'NAO CONFIRMADA','| desafio visivel:',chal,'| url:',p.url());
  log('TEXTO:',txt.slice(0,600));
 }catch(e){ log('ERR',e.message.split('\n')[0]); await p.screenshot({path:D+'/wix_'+slug+'_err.png',fullPage:true}).catch(()=>{}); }
 await b.close();
})();
