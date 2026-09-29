// FLUXO GENERICO DE WORKDAY, com tudo que a campanha mediu ate 09/09/2026.
// Uso: sh hb_run.sh wd_geral.js <host> <site> <jobpath> <slug> [ENVIAR]
//
// Armadilhas que este script ja evita, todas medidas em formulario real:
//  1. Country vem com um valor DE VERDADE (United States of America), nao com "Select One";
//     por isso a troca de pais e forcada em vez de pulada.
//  2. Trocar o Country REDESENHA nome, endereco e fonte e apaga o que ja foi escrito:
//     ordem obrigatoria e pais -> combos -> texto por ultimo.
//  3. Depois da troca para Brazil existem DOIS inputs com o id name--legalName--lastName;
//     o primeiro e Mother's Family Name e o SEGUNDO e o Family Name obrigatorio.
//  4. Os CHIPS ja escolhidos tambem tem role=option (data-automation-id="selectedItem"), entao ler
//     [role=option] mistura opcao com resposta antiga: o chip "Ganji" apareceu como unica opcao do
//     Prefix e do codigo de pais. Opcao de verdade e data-automation-id="menuItem".
//  5. "How Did You Hear About Us" e uma ARVORE, nao uma lista: clicar no item de nivel 1 troca a
//     lista pelos filhos em vez de escolher, e o Workday marca um filho sozinho. Sem comparar a
//     lista antes e depois do clique, a resposta gravada foi "Ganji", um quadro chines.
//  6. Reentrar em /apply/useMyLastApplication com rascunho aberto apaga o CV do passo 2;
//     para retomar, a rota e /apply.
//  7. Pergunta de pretensao salarial costuma ser textarea SEM rotulo ligado, achavel so pelo
//     id que comeca com secondaryQuestionnaire--.
//  8. O campo "beecatcher" e armadilha para robo e fica sempre vazio.
//  9. O ROTULO do campo de pais MUDA de locatario para locatario: a Disney de Londres escreve
//     "Country*" e a Disney do Canada escreve "Country / Region*". Um gate por texto de rotulo
//     pulou o passo 1 inteiro em silencio e o formulario devolveu nove campos obrigatorios vazios,
//     sem uma linha de log dizendo o porque. O sinal confiavel e a PRESENCA do elemento
//     #country--country, nunca a frase escrita ao lado dele.
// 10. Alguns locatarios tem "Prefix" obrigatorio, que nao existe em outros. Por isso ele e achado
//     pelo ROTULO e nao por id fixo, e nao encontra-lo nao e erro.
// 11. O passo 1 renderiza DEPOIS de quinze segundos; sem esperar pelo campo, o corpo vem so com
//     "Save and Continue" e a rodada gasta uma iteracao a toa.
// 12. "Please select your gender" e obrigatorio na Disney do Canada apesar do texto dizer que a
//     secao e voluntaria.
const {chromium}=require('playwright');
const fs=require('fs');
const C=require('./cred.json');
const [host,site,jobpath,slug]=process.argv.slice(2);
const enviar=(process.argv[6]||'')==='ENVIAR';
const estado='wdst_'+slug+'.json';
const CV='/home/user/apply/Vini_Cavalcanti_CV.pdf';
const SITES=['https://www.artstation.com/viniciuscavalcanti','https://www.linkedin.com/in/vinicavalcnti/','https://vinicavalcanti.com'];
const D={tel:process.env.VINI_TEL||'', rua:process.env.VINI_RUA||'', cep:process.env.VINI_CEP||'', cidade:'Olinda'};
const SAL=process.env.VINI_SAL||'Open to aligning with your band for the role.';
const txt=async p=>(await p.innerText('body')).replace(/\n{2,}/g,'\n');
const passo=async p=>{ const m=(await txt(p)).match(/current step (\d) of (\d)/); return m?{n:+m[1],de:+m[2]}:{n:0,de:0}; };
const limpa=a=>a.map(x=>x.trim()).filter(x=>x && !/\(\+/.test(x));

// MEDIDO no DOM da Disney do Canada em 09/09, e vale para todo Workday: os CHIPS ja escolhidos
// tambem carregam role=option, so que com data-automation-id="selectedItem". Ler [role=option]
// mistura opcao com resposta antiga, e foi assim que o chip "Ganji" apareceu como unica opcao do
// Prefix e do codigo de pais. Opcao de menu de verdade tem data-automation-id="menuItem".
// E preciso aceitar as DUAS formas: o menu da fonte marca cada item com menuItem, enquanto o de
// grau e o de genero so tem role=option. Ler so menuItem devolveu lista VAZIA nos dois, e a
// consequencia foi um grau falso ficar gravado e o passo 4 travar tres vezes. O que nao pode
// entrar de jeito nenhum e o chip ja escolhido, que tambem carrega role=option.
const OPC='[data-automation-id="menuItem"], [role=option]:not([data-automation-id="selectedItem"])';
async function clicaOpcao(p, nome){
  const esc=nome.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const exato=p.locator(OPC).filter({hasText:new RegExp('^'+esc+'$')});
  if(await exato.count().catch(()=>0)){ await exato.first().click({force:true}).catch(()=>{}); return true; }
  const contem=p.locator(OPC).filter({hasText:nome});
  if(await contem.count().catch(()=>0)){ await contem.first().click({force:true}).catch(()=>{}); return true; }
  return await p.getByRole('option',{name:nome,exact:true}).first().click({force:true}).then(()=>true).catch(()=>false);
}

// Regras mais especificas primeiro: a busca para no primeiro trecho que casa.
const RESP=[
 // A Disney do Canada marca "Please select your gender" com asterisco de OBRIGATORIO no meio de
 // um bloco que se apresenta como voluntario, e sem resposta o passo 4 nao passa. Na duvida sobre
 // dado pessoal dele, a preferencia e a opcao que nao revela nada; so se ela nao existir e que
 // entra a resposta verdadeira.
 ['please select your gender', ['I do not wish to answer','I don\'t wish to answer','Decline','Prefer not','Do not wish','Male']],
 ['evidence of your identity', ['No']],
 ['authorisation to work', ['No']],
 ['star citizen community', ['No']],
 ['willing to relocate', ['Yes']],
 ['valid passport', ['Yes']],
 ['legally eligible to work', ['No']],
 ['legally authorized to work', ['No']],
 ['ever worked for', ['No']],
 ['relative or person with whom', ['No']],
 ['close personal relationship', ['No']],
 ['require sponsorship', ['Yes']],
 ['now or in the future require', ['Yes']],
 ['consent to the use of your personal information', ['Yes']],
 ['previously been employed', ['No']],
 ['worked previously with', ['No']],
 ['previously worked', ['No']],
 ['worked for us before', ['No']],
 ['applied to', ['No']],
 ['ever been employed', ['No']],
 ['currently employed by', ['No']],
 ['currently working for', ['No']],
 ['have you worked for', ['No']],
 ['as a contractor', ['No']],
 ['are you related', ['No']],
 ['18 years', ['Yes']],
 ['other locations', ['Yes']],
 ['english fluency', ['Fluent','Native','Advanced','Professional','Full professional']],
 ['level of english', ['Fluent','Native','Advanced','Professional','Full professional']],
];

// ENTRAR numa conta que ja existe no locatario.
// MEDIDO na Netflix em 09/09: [data-automation-id="click_filter"] e o LINK "Sign In", nao o botao
// de enviar. Preencher e depois clicar nele TROCA o formulario de Create Account para Sign In e
// apaga o que foi escrito, e o passo 1 fica parado em Create Account sem nenhuma mensagem de erro.
// A ordem certa e: trocar o formulario primeiro, escrever depois, enviar por ultimo.
async function logar(p, C){
  // click_filter e o link de TROCA, e ele existe nos dois formularios: no Create Account leva para
  // Sign In, e no Sign In leva de volta para Create Account. Clicar sem olhar em qual formulario se
  // esta faz o pendulo e nunca entra. O sinal de que a tela e a de cadastro e o campo de confirmar
  // senha, que so existe la.
  // Trocar de formulario e ESPERAR a troca acontecer. Medido na Netflix em 09/09: clicar no link
  // e preencher em seguida escreve no formulario velho, o envio nao acontece e a tela fica parada
  // em Create Account sem erro nenhum. O sinal de que a troca terminou e o campo de confirmar
  // senha SUMIR, entao espera-se por ele e nao por um tempo fixo.
  for(let t=1; t<=3; t++){
    if(!(await p.$('input[data-automation-id="verifyPassword"]'))) break;
    const link=await p.$('[data-automation-id="click_filter"]');
    if(!link) break;
    console.log('  tela era Create Account, trocando para Sign In (tentativa '+t+')');
    await link.click({force:true}).catch(()=>{});
    await p.waitForSelector('input[data-automation-id="verifyPassword"]',{state:'detached',timeout:20000}).catch(()=>{});
    await p.waitForTimeout(2500);
  }
  if(await p.$('input[data-automation-id="verifyPassword"]')){
    console.log('  !! nao consegui sair da tela de Create Account'); return;
  }
  await p.fill('input[data-automation-id="email"]', C.email).catch(e=>console.log('  email',e.message.slice(0,40)));
  await p.waitForTimeout(700);
  await p.fill('input[data-automation-id="password"]', C.padrao_campanha).catch(e=>console.log('  senha',e.message.slice(0,40)));
  await p.waitForTimeout(700);
  let bt=await p.$('[data-automation-id="signInSubmitButton"]');
  // O id do botao muda de locatario para locatario; o texto nao. Procura-se o BOTAO de envio, e
  // nunca o link de troca, que tambem se chama Sign In e levaria de volta ao pendulo.
  if(!bt) bt=await p.$('button[type=submit]:has-text("Sign In"), form button:has-text("Sign In")');
  if(bt) await bt.click({force:true}).catch(()=>{});
  else await p.keyboard.press('Enter').catch(()=>{});
  await p.waitForTimeout(16000);
  console.log('  apos login, passo', JSON.stringify(await passo(p)));
}

async function combo(p, sel, escolhas, nome, forcar){
  // ARMADILHA MEDIDA na Cloud Imperium: se o menu anterior ainda esta aberto, a leitura de
  // [role=option] devolve as opcoes DELE. Por isso fecha tudo antes de abrir o proximo.
  await p.keyboard.press('Escape').catch(()=>{}); await p.waitForTimeout(1200);
  const bt=await p.$(sel); if(!bt) return false;
  const atual=(await bt.innerText().catch(()=>'')).trim();
  if(!forcar && atual && !/select one|^$/i.test(atual)){ console.log('  ', nome, 'ja tinha:', atual.slice(0,40)); return true; }
  await bt.click({force:true}); await p.waitForTimeout(2800);
  const acha=ops=>{ for(const e of escolhas){ const a=ops.find(o=>o.toLowerCase()===e.toLowerCase())||ops.find(o=>o.toLowerCase().startsWith(e.toLowerCase())); if(a) return a; } return null; };
  let ops=limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
  let alvo=acha(ops);
  // MEDIDO na Netflix em 09/09: o menu ANTERIOR pode nao ter sido descartado do DOM ainda, e ai a
  // leitura devolve um resto dele (o campo Estado leu "LinkedIn", que era a fonte recem escolhida).
  // Lista curta demais e sinal disso, entao vale uma segunda leitura com o menu fechado antes.
  if(!alvo && ops.length<=2){
    await p.keyboard.press('Escape').catch(()=>{}); await p.waitForTimeout(3000);
    await bt.click({force:true}).catch(()=>{}); await p.waitForTimeout(3000);
    ops=limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
    alvo=acha(ops);
    if(alvo) console.log('   ', nome, 'so apareceu na segunda leitura');
  }
  if(!alvo){ console.log('   !! nao casou', nome, '|', ops.slice(0,20).join(' / ').slice(0,250)); await p.keyboard.press('Escape'); return false; }
  await clicaOpcao(p,alvo);
  await p.waitForTimeout(2500); console.log('  ', nome, '=>', alvo); return true;
}

// Menu achado pelo ROTULO, para campos que existem em uns locatarios e nao em outros (Prefix).
// Sobe pelos ancestrais recolhendo o texto de cada nivel e testa TODOS, porque o pai imediato do
// botao costuma conter so "Select One" e o rotulo mora um ou dois niveis acima.
async function comboRotulo(p, rotulo, escolhas){
  await p.keyboard.press('Escape').catch(()=>{}); await p.waitForTimeout(1000);
  const re=new RegExp('^'+rotulo, 'i');
  for(const bt of await p.$$('button[aria-haspopup="listbox"]')){
    const niveis=await bt.evaluate(e=>{ const r=[]; let n=e.parentElement; for(let i=0;i<5&&n;i++){ r.push((n.innerText||'').replace(/\s+/g,' ').trim()); n=n.parentElement; } return r; }).catch(()=>[]);
    if(!niveis.some(x=>re.test(x))) continue;
    const atual=(await bt.innerText().catch(()=>'')).trim();
    if(atual && !/select one/i.test(atual)){ console.log('  ', rotulo, 'ja tinha:', atual.slice(0,30)); return true; }
    await bt.click({force:true}); await p.waitForTimeout(2600);
    const ops=limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
    let alvo=null;
    for(const e of escolhas){ alvo=ops.find(o=>o.toLowerCase()===e.toLowerCase())||ops.find(o=>o.toLowerCase().startsWith(e.toLowerCase())); if(alvo) break; }
    if(!alvo){ console.log('   !! nao casou', rotulo, '|', ops.slice(0,20).join(' / ').slice(0,220)); await p.keyboard.press('Escape').catch(()=>{}); return false; }
    await clicaOpcao(p,alvo);
    await p.waitForTimeout(2200); console.log('  ', rotulo, '=>', alvo); return true;
  }
  console.log('  ', rotulo, 'nao existe neste formulario');
  return false;
}

async function fonte(p){
  // Alguns locatarios usam multiselect ("1 item selected, X") e outros um select simples, em que
  // o valor aparece direto e aquela frase nunca existe. A checagem serve para os dois: basta que
  // a pergunta nao esteja mais em "Select One" nem vazia.
  // MEDIDO na Disney do Canada em 09/09: o multiselect vazio nao escreve "Select One", escreve
  // "0 items selected". Isso passava nos tres testes abaixo e a funcao dizia "ja respondida" sem
  // abrir o menu uma vez. O erro custou duas tentativas de envio, e cada erro de validacao do
  // Workday RE-RENDERIZA o passo 1 e apaga nome, endereco e telefone ja escritos. Ou seja: um
  // multiselect lido errado apaga o formulario inteiro.
  const ok=async()=>{
    const c=((await txt(p)).match(/How Did You Hear About Us\?\*?\s*\n?([^\n]*)/)||['',''])[1].trim();
    if(/^0 items selected/i.test(c)) return false;
    if(/1 item selected/.test(c)) return true;
    return !!c && !/^select one$/i.test(c) && !/^\*?$/.test(c);
  };
  // Rotulo REALMENTE selecionado: "1 item selected, Ganji" tem que ser lido como "Ganji".
  const rotuloSel=async()=>{
    const c=((await txt(p)).match(/How Did You Hear About Us\?\*?\s*\n?([^\n]*)/)||['',''])[1].trim();
    const m=c.match(/\d+\s+items?\s+selected,\s*(.+)$/i);
    return (m?m[1]:c).trim();
  };
  // MEDIDO em 09/09 na Disney do Canada: clicar no PAI da cascata ("Job Board") fez o Workday
  // gravar um FILHO qualquer, e o que ficou gravado foi "Ganji", um quadro de empregos chines em
  // que ele nunca entrou. A checagem antiga dizia "respondida" e a resposta era mentira. Dai esta
  // lista do que e VERDADE para ele: qualquer outra coisa e para apagar, nunca para aceitar.
  const VERDADE=/linkedin|job board|search engine|internet|social media|company (web)?site|career site|other/i;
  const bom=async()=>{ if(!(await ok())) return false; return VERDADE.test(await rotuloSel()); };
  if(await bom()) return true;
  const src=await p.$('#source--source');
  if(!src){ console.log('   !! fonte obrigatoria mas #source--source nao existe neste locatario'); return false; }

  // Apagar chip errado, ESCOPADO ao container da fonte. Em 08/09 uma remocao de chip sem escopo
  // apagou o codigo de pais do telefone; por isso o container e RECUSADO se contiver o telefone.
  const limparChips=async()=>p.evaluate(()=>{
    const b=document.querySelector('#source--source'); if(!b) return -1;
    let c=b.parentElement;
    for(let i=0;i<3&&c;i++){
      if(c.querySelector('[data-automation-id="DELETE_charm"], button[aria-label^="Delete"]')) break;
      c=c.parentElement;
    }
    if(!c) return 0;
    if(c.querySelector('#phoneNumber--countryPhoneCode')) return -2;
    const bs=[...c.querySelectorAll('[data-automation-id="DELETE_charm"], button[aria-label^="Delete"]')];
    bs.forEach(x=>x.click());
    return bs.length;
  });
  const sujo=await rotuloSel();
  if(sujo && !/^0 items/i.test(sujo) && !/^select one$/i.test(sujo)){
    console.log('   fonte trazia valor nao aprovado:', JSON.stringify(sujo), '| chips removidos:', await limparChips());
    await p.waitForTimeout(2000);
  }

  // CASCATA, com o comportamento MEDIDO no DOM em 09/09: clicar num item de nivel 1 NAO seleciona,
  // ele TROCA a lista pelos filhos daquela categoria (clicar em "Job Board" devolveu 51job, 58.com,
  // Glassdoor, Indeed...). Quem confunde descer com escolher le o estado "Expanded" como se fosse
  // resposta e aceita o filho que o Workday marca sozinho. A regra segura e comparar a lista:
  // se ela MUDOU depois do clique, desceu um nivel; se nao mudou ou sumiu, foi selecao.
  const opcoes=async()=>limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
  // A lista de cada nivel e VIRTUALIZADA: o nivel 2 do Job Board renderiza de "51job" ate
  // "Hellowork" e para ali, entao LinkedIn existe e nao aparece na leitura.
  // Como se chega a um item que a janela virtual nao desenhou, MEDIDO em 09/09:
  //  - rolar por scrollTop nao funciona: os ancestrais tem scrollHeight igual ao clientHeight,
  //    porque a janela e desenhada pelo componente e nao pelo overflow do navegador;
  //  - a roda do mouse sozinha nao move nada;
  //  - LIMPAR a caixa de busca e digitar nela devolve o menu para a raiz, perdendo o nivel;
  //  - o que move e DIGITAR direto no teclado, sem tocar em campo nenhum: o menu leva a lista
  //    ate o trecho do alfabeto correspondente e continua no mesmo nivel.
  const digitar=async(termo)=>{ await p.keyboard.type(termo,{delay:150}); await p.waitForTimeout(3200); };
  const apagar=async(n)=>{ for(let i=0;i<n;i++) await p.keyboard.press('Backspace'); await p.waitForTimeout(2200); };

  // "Social Media" vem ANTES de "Job Board" de proposito: a lista de quadros de emprego tem
  // centenas de nomes e a janela virtual so desenha catorze, enquanto a de redes sociais cabe
  // inteira numa janela. E LinkedIn e rede social, entao a resposta continua sendo verdade.
  // ARMADILHA 13, MEDIDA NA BLIZZARD EM 09/09: nem todo locatario usa cascata. O
  // xboxgaming/Blizzard_External_Careers mostra uma lista PLANA de 25 opcoes, com LinkedIn,
  // Company Website, Indeed, Glassdoor, Art Station e Other TODAS no nivel 1, sem treeitem,
  // sem menuItem e sem caixa de busca. A escolha de nivel 1 so procurava CATEGORIA
  // ("Social Media", "Job Board", "Search Engine"), nenhuma existe aqui, entao a funcao
  // concluia "nivel 1 nao oferece resposta verdadeira", saia sem responder, e o Workday
  // reprovava o passo 1 inteiro por campo obrigatorio vazio. Agora, quando o nivel 1 nao
  // tem categoria, ele aceita a FOLHA verdadeira ali mesmo.
  //
  // De onde sai a ordem de preferencia: da variavel WD_FONTE, e isso e de proposito. A fonte
  // e um campo de VERDADE, nao de conveniencia: vaga achada por alerta do LinkedIn responde
  // LinkedIn, vaga achada por agregador (Grackle, Hitmarker, RemoteGameJobs) responde Other,
  // porque nenhum locatario lista esses agregadores pelo nome. Sem a variavel, o padrao
  // continua sendo o de antes, LinkedIn primeiro.
  const PREF_PLANA=(process.env.WD_FONTE||'linkedin').toLowerCase()==='other'
    ? [/^other$/i, /^company website$/i, /^linkedin$/i]
    : [/^linkedin$/i, /^company website$/i, /^other$/i];
  const folhaPlana=(ops)=>{
    for(const re of PREF_PLANA){ const a=ops.find(o=>re.test(o.trim())); if(a) return a; }
    return null;
  };
  const escolhe=(ops,nivel)=> nivel===1
    ? (ops.find(o=>/^social media$/i.test(o)) || ops.find(o=>/social media/i.test(o)) ||
       ops.find(o=>/^job board$/i.test(o)) || ops.find(o=>/job board/i.test(o)) ||
       ops.find(o=>/search engine|internet/i.test(o)) ||
       folhaPlana(ops))
    : (ops.find(o=>/^linkedin$/i.test(o)) || ops.find(o=>/linkedin/i.test(o)) ||
       ops.find(o=>/^other job board$/i.test(o)) || ops.find(o=>/^other/i.test(o)));
  await src.click({force:true}); await p.waitForTimeout(3000);
  let nivel=1;
  while(nivel<=3){
    let ops=await opcoes();
    if(!ops.length) break;
    console.log('   fonte nivel '+nivel+':', ops.slice(0,12).join(' / ').slice(0,220));
    // Nivel 1 e categoria; do nivel 2 em diante sao quadros com nome proprio, e ali so LinkedIn
    // e verdade. Nunca cair no ops[0]: era esse "primeiro da lista" que respondia por ele.
    let pref=escolhe(ops,nivel);
    if(!pref && nivel>1){
      // O teclado so mexe na lista DEPOIS que ela recebe foco; sem isto, digitar nao move nada.
      for(let i=0;i<5;i++) await p.keyboard.press('ArrowDown');
      await p.waitForTimeout(1500);
      for(const termo of ['linked','other job','other']){
        console.log('   nivel '+nivel+' nao mostra a opcao; digitando', JSON.stringify(termo));
        await digitar(termo);
        ops=await opcoes();
        console.log('   lista apos digitar:', ops.slice(0,8).join(' / ').slice(0,180));
        pref=escolhe(ops,nivel);
        if(pref) break;
        await apagar(termo.length);
      }
    }
    if(!pref){ console.log('   !! nivel '+nivel+' nao oferece resposta verdadeira'); break; }
    const antes=ops.join('|');
    await clicaOpcao(p,pref);
    console.log('   fonte =>', pref);
    await p.waitForTimeout(3200);
    const depois=(await opcoes()).join('|');
    if(!depois || depois===antes) break;  // nao desceu: o clique foi escolha
    nivel++;
  }
  await p.keyboard.press('Escape').catch(()=>{}); await p.waitForTimeout(2000);
  const r=await bom(); console.log('   fonte respondida:', r, '| valor:', JSON.stringify(await rotuloSel())); return r;
}

async function perguntas(p){
  for(const bt of await p.$$('button[aria-haspopup="listbox"]')){
    const rot=await bt.evaluate(e=>{ let n=e.parentElement, t=''; for(let i=0;i<6&&n;i++){ t=(n.innerText||'').replace(/\s+/g,' ').trim(); if(t.length>25) break; n=n.parentElement; } return t.slice(0,300); }).catch(()=>'');
    const atual=(await bt.innerText().catch(()=>'')).trim();
    const regra=RESP.find(r=>rot.toLowerCase().includes(r[0]));
    if(!regra) continue;
    if(atual && !/select one/i.test(atual)){ console.log('   ja respondido:', regra[0], '=>', atual.slice(0,30)); continue; }
    await bt.click({force:true}); await p.waitForTimeout(2200);
    const ops=limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
    let alvo=null;
    for(const pref of regra[1]){ alvo=ops.find(o=>o.toLowerCase()===pref.toLowerCase())||ops.find(o=>o.toLowerCase().startsWith(pref.toLowerCase())); if(alvo) break; }
    if(!alvo){ console.log('   !! sem opcao para', regra[0], '|', ops.join(' / ').slice(0,200)); await p.keyboard.press('Escape'); continue; }
    await clicaOpcao(p,alvo);
    await p.waitForTimeout(1800); console.log('   respondido:', regra[0], '=>', alvo);
  }
  // RADIOS. A Cloud Imperium faz "Have you worked previously with CIG" como par Yes/No de
  // radio, nao como listbox, e um tratador que so olha listbox passa direto dizendo que
  // respondeu tudo enquanto o servidor recusa por campo obrigatorio vazio.
  const radios=await p.$$('input[type=radio]');
  const grupos={};
  for(const r of radios){
    const info=await r.evaluate(e=>{
      const l=e.id&&document.querySelector('label[for="'+CSS.escape(e.id)+'"]');
      const rot=((l&&l.innerText)||e.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim();
      let n=e.parentElement, ctx='';
      for(let i=0;i<7&&n;i++){ ctx=(n.innerText||'').replace(/\s+/g,' ').trim(); if(ctx.length>30) break; n=n.parentElement; }
      return {rot, ctx: ctx.slice(0,300), nome: e.name||''};
    }).catch(()=>({rot:'',ctx:'',nome:''}));
    const chave=info.nome||info.ctx.slice(0,80);
    (grupos[chave]=grupos[chave]||[]).push({el:r, ...info});
  }
  for(const [chave,itens] of Object.entries(grupos)){
    const ctx=(itens[0].ctx||'').toLowerCase();
    const regra=RESP.find(r=>ctx.includes(r[0]));
    if(!regra) continue;
    let jaMarcado=false;
    for(const i of itens){ if(await i.el.isChecked().catch(()=>false)) jaMarcado=true; }
    if(jaMarcado){ console.log('   radio ja marcado:', regra[0]); continue; }
    const querido=regra[1][0];
    const alvoIt=itens.find(i=>new RegExp('^'+querido+'$','i').test(i.rot)) || itens.find(i=>new RegExp('^'+querido,'i').test(i.rot));
    if(!alvoIt){ console.log('   !! sem radio', querido, 'para', regra[0], '| rotulos:', itens.map(i=>i.rot).join(' / ').slice(0,120)); continue; }
    await alvoIt.el.check({force:true}).catch(async()=>{ await alvoIt.el.click({force:true}).catch(()=>{}); });
    await p.waitForTimeout(900);
    console.log('   radio respondido:', regra[0], '=>', alvoIt.rot);
  }
  // CAMPOS DE TEXTO com pergunta propria da casa. O rotulo costuma NAO estar ligado por for=,
  // entao a busca vai pelo texto em volta do campo.
  const TEXTO=[
   ['salary expectation', SAL],
   ['expected annual salary', SAL],
   ['notice period', 'Within 30 days of an offer.'],
   ['entertainment and/or online gaming media', 'I founded and teach at my own online character art school, where I publish teaching content. I am not involved in gaming media, streaming or press.'],
   ['portfolio/showreel', 'https://www.artstation.com/viniciuscavalcanti'],
   ['linkedin url', 'https://www.linkedin.com/in/vinicavalcnti/'],
   ['provide your linkedin', 'https://www.linkedin.com/in/vinicavalcnti/'],
   ['requires a password', 'No password: the portfolio and all links are public.'],
  ];
  for(const campo of await p.$$('textarea, input[type=text]')){
    const rot=await campo.evaluate(e=>{
      const l=e.id&&document.querySelector('label[for="'+CSS.escape(e.id)+'"]');
      let t=((l&&l.innerText)||e.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim();
      if(t.length<8){ let n=e.parentElement; for(let i=0;i<5&&n;i++){ const c=(n.innerText||'').replace(/\s+/g,' ').trim(); if(c.length>15){ t=c; break; } n=n.parentElement; } }
      return t.slice(0,260);
    }).catch(()=>'');
    const regra=TEXTO.find(r=>rot.toLowerCase().includes(r[0]));
    if(!regra) continue;
    const v=await campo.inputValue().catch(()=>'');
    if(!v){ await campo.fill(regra[1]); await p.waitForTimeout(500); console.log('   texto:', regra[0], '=>', regra[1].slice(0,45)); }
  }
  // DATA. "How soon can you start?" e um campo de data em tres caixas (MM, DD, YYYY), nao um
  // texto. Trinta dias a partir de hoje, que e a resposta padrao da campanha.
  const corpo=await txt(p);
  if(/how soon can you start|when can you start|available to start/i.test(corpo)){
    const d=new Date(Date.now()+30*24*3600*1000);
    const mm=String(d.getMonth()+1).padStart(2,'0'), dd=String(d.getDate()).padStart(2,'0'), yyyy=String(d.getFullYear());
    const partes=[['dateSectionMonth-input',mm],['dateSectionDay-input',dd],['dateSectionYear-input',yyyy]];
    let escreveu=0;
    for(const [aid,val] of partes){
      const el=await p.$('input[data-automation-id="'+aid+'"]');
      if(!el) continue;
      const atual=await el.inputValue().catch(()=>'');
      if(!atual){ await el.fill(val); await p.waitForTimeout(400); escreveu++; }
    }
    if(escreveu) console.log('   data de inicio preenchida:', mm+'/'+dd+'/'+yyyy);
  }
  const ta=await p.$('textarea[id^="secondaryQuestionnaire--"]');
  if(ta && !(await ta.inputValue())){ await ta.fill(SAL); console.log('   salario preenchido'); }
  for(const c of await p.$$('input[type=checkbox]')){
    const rot=await c.evaluate(e=>{ const l=e.id&&document.querySelector('label[for="'+CSS.escape(e.id)+'"]'); return ((l&&l.innerText)||e.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim(); }).catch(()=>'');
    if(/I have read and I agree|I certify|I accept|I agree to|agree to the above|consent to the terms|read and consent|terms\s*(and|&)\s*conditions|privacy (notice|policy)/i.test(rot) && !(await c.isChecked().catch(()=>false))){ await c.check({force:true}).catch(()=>{}); console.log('   aceite marcado'); }
  }
}

(async()=>{
 const b=await chromium.launch({proxy:{server:'http://127.0.0.1:18080'},args:['--no-sandbox','--ignore-certificate-errors']});
 const opts={ignoreHTTPSErrors:true,viewport:{width:1400,height:2200},userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'};
 if(fs.existsSync(estado)) opts.storageState=estado;
 const ctx=await b.newContext(opts);
 const p=await ctx.newPage();
 const base='https://'+host+'/en-US/'+site+'/job/'+jobpath;
 await p.goto(base+'/apply/applyManually',{timeout:90000,waitUntil:'domcontentloaded'});
 await p.waitForTimeout(15000);
 // O passo 1 chega depois: sem esperar por um campo de verdade, a primeira iteracao le um corpo
 // com "Save and Continue" e nada mais, e conclui que o formulario nao tem campo nenhum.
 await p.waitForSelector('#country--country, #source--source, input[data-automation-id="email"]',{timeout:90000}).catch(()=>{});
 const ot=await p.$('#onetrust-accept-btn-handler'); if(ot&&await ot.isVisible().catch(()=>false)){ await ot.click({force:true}).catch(()=>{}); await p.waitForTimeout(2000); }

 // ENTRAR, se o locatario ja tem conta (medido na Eyeline: e o mesmo locatario da Netflix, entao
 // Create Account devolve "ja existe" e a tela vira a de login).
 if(!(await p.$('[data-automation-id="createAccountSubmitButton"]')) && await p.$('[data-automation-id="click_filter"]')){
   console.log('== entrando com a conta que ja existe no locatario');
   await logar(p, C);
   console.log('  apos login, passo', JSON.stringify(await passo(p)));
   if(/wrong email address or password|might be locked/i.test(await txt(p))){
     console.log('  !! login recusado, parando sem tentar de novo para nao arriscar bloqueio');
     await b.close(); return;
   }
   if((await passo(p)).n===0){
     await p.goto(base+'/apply/applyManually',{timeout:90000,waitUntil:'domcontentloaded'});
     await p.waitForTimeout(14000);
     console.log('  reabri a candidatura, passo', JSON.stringify(await passo(p)));
   }
 }

 // conta, se pedida
 if(await p.$('[data-automation-id="createAccountSubmitButton"]')){
   console.log('== criando conta no locatario');
   await p.fill('input[data-automation-id="email"]', C.email);
   await p.fill('input[data-automation-id="password"]', C.padrao_campanha);
   const vp=await p.$('input[data-automation-id="verifyPassword"]'); if(vp) await vp.fill(C.padrao_campanha);
   for(const c of await p.$$('input[type=checkbox]')) await c.check({force:true}).catch(()=>{});
   await p.click('[data-automation-id="createAccountSubmitButton"]',{force:true}).catch(()=>{});
   await p.waitForTimeout(15000);
   let t=await txt(p);
   console.log('  resposta do cadastro:', t.replace(/\n/g,' | ').slice(0,220));
   // Se o locatario ja tem conta, o Workday devolve a tela de login. Detecte pela PRESENCA do
   // botao de login, nao pela frase, que muda de locatario para locatario.
   if(await p.$('[data-automation-id="click_filter"]')){
     console.log('  conta ja existe neste locatario, entrando');
     await logar(p, C);
     t=await txt(p);
     if(/wrong email address or password|might be locked/i.test(t)){
       console.log('  !! login recusado. Parando sem tentar de novo, para nao arriscar bloqueio.');
       await b.close(); return;
     }
     if((await passo(p)).n===0){
       await p.goto(base+'/apply/applyManually',{timeout:90000,waitUntil:'domcontentloaded'});
       await p.waitForTimeout(15000);
     }
   }
   console.log('  apos conta, passo', JSON.stringify(await passo(p)));
 }

 let ultimo=-1, repetiu=0;
 for(let it=1; it<=10; it++){
   const s=await passo(p);
   if(s.n===ultimo){ repetiu++; } else { repetiu=0; ultimo=s.n; }
   if(repetiu>=2){ console.log('!!! travou no passo '+s.n+' tres vezes, parando sem enviar'); break; }
   console.log('\n### passo '+s.n+' de '+s.de);
   if(s.n===0){ console.log((await txt(p)).slice(0,1200)); break; }
   const t=await txt(p);

   if(await p.$('#country--country')){
     await combo(p,'#country--country',['Brazil'],'pais',true);
     await p.waitForTimeout(12000);
     await fonte(p);
     await comboRotulo(p,'Prefix',['Mr.','Mr','Mx.','Mx']);
     await combo(p,'#address--countryRegion',['Pernambuco'],'estado');
     await combo(p,'#phoneNumber--phoneType',['Mobile','Home Mobile','Cell','Personal Mobile','Home Phone'],'tipo de telefone');
     await combo(p,'#phoneNumber--countryPhoneCode',['Brazil (+55)','Brazil'],'codigo do pais');
     await p.waitForTimeout(3000);
     const sob=p.locator('input#name--legalName--lastName');
     const n=await sob.count();
     if(n>=2){ await sob.nth(0).fill(''); await sob.nth(1).fill('Cavalcanti'); } else if(n===1){ await sob.first().fill('Cavalcanti'); }
     for(const [sel,v] of [['#name--legalName--firstName','Vini'],['#address--addressLine1',D.rua],['#address--city',D.cidade],['#address--postalCode',D.cep],['#phoneNumber--phoneNumber',D.tel]]){
       const e=await p.$(sel); if(e && v){ await e.fill(v); await p.waitForTimeout(450); }
     }
     const cid=await p.$('#address--city'); if(cid) console.log('   cidade lida de volta:', await cid.inputValue());
     console.log('   nome/endereco/telefone escritos por ultimo');
   }

   if(/Resume\/CV|Upload a file/i.test(t)){
     if(!/Successfully Uploaded/i.test(t)){
       const fi=await p.$('input[type=file]');
       if(fi){ await fi.setInputFiles(CV); await p.waitForTimeout(10000); console.log('   CV:', /Successfully Uploaded/i.test(await txt(p))?'Successfully Uploaded':'nao confirmado'); }
     } else console.log('   CV ja estava');
     let urls=await p.$$('input[id^="webAddress-"]');
     if(!urls.length){
       for(let k=0;k<SITES.length;k++){ const lista=await p.$$('[data-automation-id="add-button"]'); if(!lista.length) break; await lista[lista.length-1].click({force:true}).catch(()=>{}); await p.waitForTimeout(3500); }
       urls=await p.$$('input[id^="webAddress-"]');
     }
     for(let k=0;k<urls.length && k<SITES.length;k++){ if(!(await urls[k].inputValue())){ await urls[k].fill(SITES[k]); await p.waitForTimeout(450); } }
     console.log('   sites:', urls.length);
     if(!(await p.$('input[id$="--schoolName"]'))){
       const adds=await p.$$('[data-automation-id="add-button"]');
       if(adds.length>=2){ await adds[1].click({force:true}); await p.waitForTimeout(4000); }
     }
     const esc=await p.$('input[id$="--schoolName"]');
     if(esc && !(await esc.inputValue())){ await esc.fill('Universidade Catolica de Pernambuco'); }
     const deg=await p.$('button[id$="--degree"]');
     // Nao basta preencher o que esta vazio: um rascunho anterior pode ter deixado um grau FALSO
     // gravado, e ai o certo e trocar. Grau suspeito = certificado, diploma, ou mestrado concluido.
     const grauAtual=deg?(await deg.innerText()).trim():'';
     const grauSuspeito=/certificate|diploma/i.test(grauAtual) ||
                        (/master/i.test(grauAtual) && /complete/i.test(grauAtual) && !/incomplete|in progress/i.test(grauAtual));
     if(grauSuspeito) console.log('   grau gravado e suspeito, trocando:', grauAtual);
     if(deg && (/select one/i.test(grauAtual) || grauSuspeito)){
       await deg.click({force:true}); await p.waitForTimeout(2500);
       const ops=limpa(await p.locator(OPC).allInnerTexts().catch(()=>[]));
       // NUNCA mestrado concluido: o mestrado esta em andamento.
       // CORRIGIDO em 09/09 na Disney do Canada: a regra antiga punha "post grad" ACIMA de
       // bachelor e escolheu "Post Graduate Certificate", que e um diploma que ele NAO tem.
       // Certificado e diploma nao sao sinonimo de grau, entao saem da lista; o que ele tem
       // concluido e a graduacao, e o mestrado em andamento vem sempre primeiro.
       console.log('   graus oferecidos:', ops.join(' | ').slice(0,400));
       const alvo = ops.find(o=>/master/i.test(o) && /(in progress|incomplete|not complete|pursuing|ongoing)/i.test(o)) ||
                    ops.find(o=>/bachelor/i.test(o) && !/not complete|incomplete/i.test(o)) ||
                    ops.find(o=>/university degree completed/i.test(o)) ||
                    ops.find(o=>/(licenciat|graduacao|undergraduate)/i.test(o) && !/incomplete|not complete/i.test(o));
       if(alvo){ await clicaOpcao(p,alvo); console.log('   grau =>', alvo); }
       else { console.log('   graus:', ops.join(' | ').slice(0,300)); await p.keyboard.press('Escape'); }
       await p.waitForTimeout(2000);
     }
   }

   await perguntas(p);
   await p.screenshot({path:'wdg_'+slug+'_p'+s.n+'.png',fullPage:true}).catch(()=>{});
   if(s.n===s.de){ console.log('>>> REVIEW'); break; }
   const nb=p.locator('[data-automation-id="pageFooterNextButton"]').first();
   if(!(await nb.count())){ console.log('sem Next'); break; }
   await nb.click({force:true}); await p.waitForTimeout(14000);
   const err=(await txt(p)).match(/Errors? Found[\s\S]{0,300}/i);
   if(err) console.log('!!! ERRO:', err[0].replace(/\n/g,' | ').slice(0,300));
 }

 const rev=await txt(p);
 console.log('\n===== REVIEW ====='); console.log(rev.slice(0,5000));
 await p.screenshot({path:'wdg_'+slug+'_review.png',fullPage:true}).catch(()=>{});
 const grau=(rev.match(/Degree\s*\n([^\n]+)/)||[])[1]||'';
 // Certificado e diploma de pos entram aqui porque ele NAO tem nenhum dos dois: a regra antiga
 // so olhava mestrado concluido e deixou passar "Post Graduate Certificate" na Disney do Canada.
 const mentiraGrau=(/master/i.test(grau) && /complete/i.test(grau) && !/incomplete|in progress/i.test(grau))
                   || /certificate|diploma/i.test(grau);
 const autorizacao=(rev.match(/legally (authorized|eligible)[^\n]*\n([^\n]+)/i)||[])[2]||'';
 const mentiraAut=/^yes/i.test(autorizacao.trim());
 // A fonte tambem e declaracao: se a revisao mostrar um quadro de empregos em que ele nunca
 // entrou, isso e informacao falsa no formulario e vale como reprovacao.
 const fonteRev=(rev.match(/How Did You Hear About Us\?\s*\n([^\n]+)/i)||[])[1]||'';
 const mentiraFonte=!!fonteRev && !/linkedin|job board|search engine|internet|social media|company (web)?site|career site|other|referral/i.test(fonteRev);
 console.log('CONFERENCIA -> grau:', grau||'(sem)', '| autorizacao legal:', autorizacao||'(sem pergunta)', '| fonte:', fonteRev||'(sem)');
 if(mentiraGrau||mentiraAut||mentiraFonte) console.log('!!! CONFERENCIA REPROVOU: grau falso?', mentiraGrau, '| autorizacao falsa?', mentiraAut, '| fonte falsa?', mentiraFonte);
 if(enviar && !mentiraGrau && !mentiraAut && !mentiraFonte){
   await p.locator('button:has-text("Submit")').first().click({force:true}).catch(async()=>{ await p.locator('[data-automation-id="pageFooterNextButton"]').first().click({force:true}).catch(()=>{}); });
   await p.waitForTimeout(18000);
   console.log('URL APOS SUBMIT:', p.url());
   console.log((await txt(p)).slice(0,2200));
   await p.screenshot({path:'wdg_'+slug+'_enviado.png',fullPage:true}).catch(()=>{});
 } else console.log(enviar?'NAO ENVIADO: a conferencia reprovou':'(ensaio)');
 await ctx.storageState({path:estado});
 await b.close();
})();
