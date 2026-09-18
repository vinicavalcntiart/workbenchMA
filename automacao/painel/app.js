/* Painel da campanha, versao 2 (19/09/2026). Fonte: automacao/painel/app.js.
   Nao edite este codigo dentro do docs/index.html: rode python3 automacao/painel/monta-painel.py.
   Tudo aqui deriva dos arrays de dados do bloco anterior; nada e escrito a mao. */
"use strict";
const $ = sel => document.querySelector(sel);
const esc = t => String(t == null ? "" : t).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const css = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim() || "#888";
const fmtBR = d => { const [y,m,dd] = String(d).slice(0,10).split("-"); return dd+"/"+m; };
const SEMANA = ["dom","seg","ter","qua","qui","sex","sáb"];
const diaSem = iso => SEMANA[new Date(String(iso).slice(0,10)+"T12:00:00Z").getUTCDay()];
const normName = x => String(x).toLowerCase().normalize("NFD").replace(/[^a-z0-9]/g,"").slice(0,12);
const hojeISO = () => new Date().toISOString().slice(0,10);
const META_DIA = (typeof META === "object" && META) ? META : {formularios:10, personagem:5};

/* ---------- estado guardado no navegador ---------- */
const KEY = "campanha-vini-status-v1", PKEY = "campanha-portais-v1", SEC_KEY = "campanha-secoes-v2", KIT_STUDIO_KEY = "campanha-kit-studio-v1";
let progress = {}, applied = {};
try { progress = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch(e){ progress = {}; }
try { applied = JSON.parse(localStorage.getItem(PKEY) || "{}") || {}; } catch(e){ applied = {}; }
const saveProgress = () => { try { localStorage.setItem(KEY, JSON.stringify(progress)); } catch(e){} };
const saveApplied = () => { try { localStorage.setItem(PKEY, JSON.stringify(applied)); } catch(e){} };
const stageOf = s => progress[s.email] || s.stage || "aguardando";
const isApplied = p => !!(p.done || applied[p.url]);

/* ---------- derivados de STUDIOS ---------- */
const LOTE_ULTIMO = Object.values(LOTE_DATA).sort().pop();
const dataDoLote = b => LOTE_DATA[b] || LOTE_ULTIMO;
const LOTES = (() => { const m = new Map(); STUDIOS.forEach(s => m.set(s.batch, (m.get(s.batch)||0)+1));
  return [...m.entries()].sort((a,b)=>a[0]-b[0]).map(([b,n]) => [b===0 ? "Pré-campanha" : "Lote "+b, n, dataDoLote(b)]); })();
const ENVIOS = STUDIOS.length;
const ESTUDIOS_EMAIL = new Set(STUDIOS.map(s => s.email.trim().toLowerCase())).size;
const SEGUNDAS_VIAS = ENVIOS - ESTUDIOS_EMAIL;
const CAIXA_GENERICA = new Set(["info","jobs","careers","career","hr","contact","hello","recruiting","recruitment","recruit","talent","talents","apply","work","people","office","team","studio","hi","mail","admin","general","hiring","art","production","business","enquiries","inquiries","enquiry","submissions","submission","join","joinus","jobb","reception","press","support","hey","email","us"]);
const ehPessoa = e => { const u = String(e).split("@")[0].toLowerCase().replace(/[._-]/g,""); return u.length > 0 && !CAIXA_GENERICA.has(u) && !/^(jobs|careers|hr|info|contact|hello|talent)\d*$/.test(u); };
const ESTUDIOS_PESSOA = new Set(STUDIOS.filter(s=>ehPessoa(s.email)).map(s=>s.email.trim().toLowerCase())).size;
const EMAILS_PRE = STUDIOS.filter(s=>s.batch===0).length;
const EMAILS_CAMPANHA = ENVIOS - EMAILS_PRE;
const EMAILS_LOG = EMAILS_PRE + DAILY.reduce((a,d)=>a+(d[1]||0),0);
const DELIV = {
  ok:      {label:"Entregue", color:"--good"},
  conf:    {label:"Entregue · confirmação automática", color:"--good"},
  reenvio: {label:"Reenviado (email corrigido)", color:"--warn"},
  bounce:  {label:"Bounce, sem email válido", color:"--crit"},
  rascunho:{label:"Rascunho pronto (aguardando envio)", color:"--line-2"},
  fechado: {label:"Estúdio encerrou as atividades", color:"--crit"}
};
const STAGES = ["aguardando","respondeu","conversa","entrevista","oferta","recusado"];
const STAGE_LABEL = {aguardando:"Aguardando", respondeu:"Respondeu", conversa:"Em conversa", entrevista:"Entrevista", oferta:"Oferta", recusado:"Recusado"};
const STAGE_PILL = {respondeu:"blue", conversa:"acc", entrevista:"good", oferta:"good", recusado:"crit", aguardando:"mute"};
// A etapa e livre no dado: as rodadas do Joe escrevem texto longo no sexto campo quando a linha
// e uma pessoa achada. So as seis etapas conhecidas contam como etapa; o resto e "aguardando".
const stageKnown = s => STAGES.includes(stageOf(s)) ? stageOf(s) : "aguardando";
function counts(){
  const delivered = CONTACTED.filter(s=>s.delivery!=="bounce").length;
  const st = k => CONTACTED.filter(s=>stageKnown(s)===k).length;
  const conv = st("respondeu")+st("conversa")+st("entrevista")+st("oferta");
  const rec = st("recusado");
  return {delivered, resp:conv+rec, conv, aberto:st("respondeu"), ent:st("entrevista")+st("oferta"), off:st("oferta"), rec,
    aguard: CONTACTED.filter(s=>s.delivery!=="bounce" && stageKnown(s)==="aguardando").length,
    bounce: CONTACTED.filter(s=>s.delivery==="bounce").length, drafts: STUDIOS.length - CONTACTED.length};
}
function followUpVence(s){ const d = new Date(dataDoLote(s.batch)+"T12:00:00Z"); d.setUTCDate(d.getUTCDate()+7); return d; }
function followUpAberto(s){ if(["bounce","rascunho","fechado"].includes(s.delivery)) return false; return stageKnown(s)==="aguardando" && !FOLLOWUP_PRONTO.has(s.email); }
function followUpDevido(s){ return followUpAberto(s) && followUpVence(s) - Date.now() <= 0; }

/* ---------- derivados de PORTAIS e GRANDES ---------- */
const PRIO_W = { alta:0, media:1, baixa:2 };
const isRemoto = p => /remot/i.test((p.country||"")+" "+(p.note||""));
const prioOf = p => p.prio && PRIO_W.hasOwnProperty(p.prio) ? p.prio : (p.origem==="email" ? "media" : "baixa");
const MORTA_RE = /VAGA EXPIRADA|SEM VAGAS|NÃO EXISTE|NÃO APLICAR|não está mais|não aparece mais|saiu do ar|estúdio fechado|liquida/i;
const isMorta = p => MORTA_RE.test(p.note||"") && !isApplied(p);
const A_MAO_RE = /(?:^|[\s(,;.])[aà]\s+m[ãa]o(?![a-zç])/i;
const GRANDE_MAO_RE = /[àa]\s+m[ãa]o em \d/i;
const CHAR_RE = /character|personagem|creature|criatura|vis dev|visual development|groom/i;
const isPersonagem = p => CHAR_RE.test((p.name||"")+" "+(p.note||"").slice(0,200));
function alertaDoGrande(g){
  const n = (g && g[4]) || "";
  if(/alerta[^.]{0,80}(ativo|ativa|criado)/i.test(n) || /coberta pelo cadastro/i.test(n)) return "ativo";
  const i = n.search(/alerta de vaga/i); if(i < 0) return "indefinido";
  const t = n.slice(i);
  if(/bloquead|captcha|datadome/i.test(t)) return "bloqueado";
  if(/n[ãa]o existe|sem alerta|n[ãa]o deu/i.test(t)) return "inexistente";
  return "indefinido";
}
const feitoGrande = g => !!g[5] || !!applied[g[2]];
function pendencias(){
  const abertos = PORTAIS.filter(p=>!isApplied(p) && !isMorta(p));
  return { abertos,
    aMao: abertos.filter(p=>A_MAO_RE.test(p.note||"")),
    altas: abertos.filter(p=>prioOf(p)==="alta"),
    pedidas: abertos.filter(p=>p.origem==="email"),
    remotas: abertos.filter(isRemoto),
    alertaBloq: GRANDES.filter(g=>alertaDoGrande(g)==="bloqueado"),
    grandeMao: GRANDES.filter(g=>GRANDE_MAO_RE.test(g[4]||"") && !feitoGrande(g)) };
}
function candPortal(){
  const pf = PORTAIS.filter(isApplied).length;
  const nomes = new Set(PORTAIS.filter(isApplied).map(p=>normName(p.name)));
  const gs = GRANDES.filter(g=>feitoGrande(g) && !nomes.has(normName(g[0]))).length;
  return pf + gs;
}

/* ---------- tooltip ---------- */
const tooltip = $("#tooltip");
function bindTips(scope){
  (scope || document).querySelectorAll("[data-tip]").forEach(el=>{
    el.addEventListener("mousemove", ev=>{
      tooltip.innerHTML = el.getAttribute("data-tip"); tooltip.style.display = "block";
      const w = tooltip.offsetWidth || 120;
      tooltip.style.left = Math.min(ev.clientX+14, window.innerWidth-w-8)+"px"; tooltip.style.top = (ev.clientY+14)+"px";
    });
    el.addEventListener("mouseleave", ()=> tooltip.style.display = "none");
  });
}

/* ---------- hoje: placar, 14 dias, agenda ---------- */
function dailyRow(iso){ return DAILY.find(d=>d[0]===iso); }
function renderPlacar(){
  const dia = UPDATED;
  const r = dailyRow(dia) || [dia,0,0,0,0];
  const forms = r[3]||0, chars = r[4]||0, emails = r[1]||0, resp = r[2]||0;
  const mf = META_DIA.formularios, mc = META_DIA.personagem;
  const pf = Math.min(100, Math.round(100*forms/mf)), pc = Math.min(100, Math.round(100*chars/mc));
  const bateu = forms>=mf && chars>=mc;
  const semana = DAILY.filter(d=>d[0]>=addDays(dia,-6) && d[0]<=dia);
  const wf = semana.reduce((a,d)=>a+(d[3]||0),0), wc = semana.reduce((a,d)=>a+(d[4]||0),0);
  $("#placar").innerHTML =
    '<div class="titulo"><h3>Meta do dia</h3><span class="dia">'+fmtBR(dia)+' · '+diaSem(dia)+(dia!==hojeISO()?' · último registro':'')+'</span></div>'
    + '<div class="meta">'
    + '<div class="num">'+forms+'<small>/'+mf+'</small></div><div><div class="rot">formulários confirmados</div><div class="barra'+(forms>=mf?" ok":"")+'"><i style="width:'+pf+'%"></i></div></div>'
    + '<div class="num">'+chars+'<small>/'+mc+'</small></div><div><div class="rot">de personagem</div><div class="barra'+(chars>=mc?" ok":"")+'"><i style="width:'+pc+'%"></i></div></div>'
    + '<div class="estado">'+(bateu ? '<b>Meta batida</b> ☺️ ' : '<b>Faltam '+Math.max(0,mf-forms)+'</b> para a meta'+(chars<mc?', '+(mc-chars)+' de personagem':'')+'. ')
    + emails+' email'+(emails===1?'':'s')+' e '+resp+' resposta'+(resp===1?'':'s')+' humana'+(resp===1?'':'s')+' no dia · semana: <b>'+wf+'</b> formulários, '+wc+' de personagem</div>'
    + '</div>';
}
function addDays(iso, n){ const d = new Date(iso+"T12:00:00Z"); d.setUTCDate(d.getUTCDate()+n); return d.toISOString().slice(0,10); }
function renderSemana(){
  const fim = UPDATED, dias = [];
  for(let i=13;i>=0;i--) dias.push(addDays(fim,-i));
  const rows = dias.map(d => dailyRow(d) || [d,0,0,0,0]);
  const maxV = Math.max(META_DIA.formularios+2, ...rows.map(r=>r[3]||0), ...rows.map(r=>r[2]||0));
  const W=360, H=120, padB=22, padT=10, padL=22, slot=(W-padL-4)/14, bw=Math.min(18, slot*0.62);
  const y = v => padT + (H-padT-padB)*(1 - v/maxV);
  const acc = css("--accent"), accSoft = css("--accent-soft"), teal = css("--teal"), line = css("--line-2");
  let s = '<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Formulários por dia nos últimos 14 dias">';
  const ym = y(META_DIA.formularios);
  s += '<line x1="'+padL+'" x2="'+W+'" y1="'+ym+'" y2="'+ym+'" stroke="'+line+'" stroke-dasharray="3 3"/>';
  s += '<text x="'+(W-2)+'" y="'+(ym-3)+'" text-anchor="end" font-size="10" fill="'+css("--muted")+'">meta '+META_DIA.formularios+'</text>';
  rows.forEach((r,i)=>{
    const cx = padL + slot*i + slot/2, f=r[3]||0, c=r[4]||0, resp=r[2]||0;
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(f)+'" width="'+bw+'" height="'+(y(0)-y(f))+'" rx="3" fill="'+acc+'" opacity=".35"><title>'+fmtBR(r[0])+': '+f+' formulários</title></rect>';
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(c)+'" width="'+bw+'" height="'+(y(0)-y(c))+'" rx="3" fill="'+acc+'"><title>'+fmtBR(r[0])+': '+c+' de personagem</title></rect>';
    if(resp) s += '<circle cx="'+cx+'" cy="'+y(resp)+'" r="3" fill="'+teal+'"><title>'+fmtBR(r[0])+': '+resp+' respostas humanas</title></circle>';
    if(i%2===1) s += '<text x="'+cx+'" y="'+(H-6)+'" text-anchor="middle" font-size="10">'+fmtBR(r[0]).slice(0,2)+'</text>';
  });
  s += '</svg>';
  $("#semanaChart").innerHTML = s;
  $("#semanaLeg").innerHTML = '<span><i class="dot" style="background:'+acc+'"></i>personagem</span><span><i class="dot" style="background:'+acc+';opacity:.35"></i>outros formulários</span><span><i class="dot" style="background:'+teal+';border-radius:50%"></i>respostas humanas</span>';
}
function renderAgenda(){
  const agora = Date.now();
  const itens = (typeof AGENDA !== "undefined" ? AGENDA : []).slice()
    .filter(a => new Date(a[0].length>10 ? a[0] : a[0]+"T23:59:00Z") - agora > -6*3600e3)
    .sort((a,b)=> a[0] < b[0] ? -1 : 1).slice(0,4);
  $("#agendaList").innerHTML = itens.length ? '<ul>'+itens.map(([iso,tit,txt,link])=>{
    const d = new Date(iso.length>10 ? iso : iso+"T12:00:00Z");
    const hora = iso.length>10 ? d.toLocaleTimeString("pt-BR",{hour:"2-digit",minute:"2-digit",timeZone:"America/Recife"}) : "";
    return '<li><div class="data"><b>'+String(d.getUTCDate()).padStart(2,"0")+'</b><span>'+SEMANA[iso.length>10 ? new Date(d.toLocaleString("en-US",{timeZone:"America/Recife"})).getDay() : d.getUTCDay()]+'</span></div>'
      + '<div><div class="tit">'+(hora?hora+' · ':'')+esc(tit)+'</div><div class="txt">'+esc(txt)+(link?' <a href="'+esc(link)+'" target="_blank" rel="noopener">abrir ↗</a>':'')+'</div></div></li>';
  }).join("")+'</ul>' : '<p class="vazio">Nada marcado. A próxima entrevista aparece aqui assim que o estúdio confirmar.</p>';
}

/* ---------- tiles ---------- */
function renderTiles(){
  const c = counts(), p = pendencias();
  const CAND_PORTAL = candPortal(), CAND_TOTAL = ENVIOS + CAND_PORTAL;
  const rate = c.delivered ? Math.round(100*c.resp/c.delivered) : 0;
  const soVoce = p.aMao.length + p.alertaBloq.length + p.grandeMao.length;
  const formsTotal = DAILY.reduce((a,d)=>a+(d[3]||0),0), charTotal = DAILY.reduce((a,d)=>a+(d[4]||0),0);
  const grandesFeitos = GRANDES.filter(feitoGrande).length;
  $("#tiles").innerHTML = [
    ["🎯", CAND_TOTAL, "Candidaturas no total", ENVIOS+" por email · "+CAND_PORTAL+" por formulário"],
    ["📝", formsTotal, "Formulários confirmados", charTotal+" de personagem, contados dia a dia"],
    ["💬", c.resp, "Respostas humanas", rate+"% dos emails entregues · "+c.aberto+" em aberto", c.aberto>0],
    ["🤝", c.ent, "Entrevistas", c.off+(c.off===1?" oferta":" ofertas"), c.ent>0],
    ["🖐️", soVoce, "Só você pode fazer", p.aMao.length+" à mão · "+p.alertaBloq.length+" alertas com captcha · "+p.grandeMao.length+" portais fechados"],
    ["🏆", grandesFeitos, "Grandes com candidatura", "de "+GRANDES.length+" na lista"],
    ["🏢", ESTUDIOS_EMAIL, "Estúdios por email", c.bounce+" bounces · "+SEGUNDAS_VIAS+" segundas vias"],
    ["👤", PESSOAS.length, "Pessoas com nome", PESSOAS.filter(x=>x.email).length+" com endereço publicado"]
  ].map(([ic,n,l,d,up])=>'<div class="tile"><div class="h"><span>'+ic+'</span>'+esc(l)+'</div><div class="n">'+n+'</div><div class="d'+(up?" up":"")+'">'+esc(d)+'</div></div>').join("");
  $("#numBadge").textContent = CAND_TOTAL+" candidaturas";
}

/* ---------- na sua mao ---------- */
function abrirSecao(id, filtro){
  const el = document.getElementById(id);
  if(el && el.tagName === "DETAILS"){ el.open = true; salvarSecao(id, true); }
  if(id === "portais" && filtro !== undefined){ portalFiltro = filtro; renderPortais(); }
}
function renderAcoes(){
  const c = counts(), p = pendencias(), items = [];
  const faltaEnviar = DOSSIES.filter(d=>d[4]);
  if(c.aberto > 0) items.push(["urgente","🔥","<b>"+c.aberto+" estúdio"+(c.aberto>1?"s":"")+" respondeu"+(c.aberto>1?"ram":"")+"</b> e a conversa ainda está sem sequência","#conversas"]);
  if(faltaEnviar.length > 0) items.push(["urgente","📋","<b>"+faltaEnviar.length+" formulário"+(faltaEnviar.length>1?"s prontos":" pronto")+" para colar</b>, começando por "+esc(faltaEnviar[0][0])+": só falta você enviar","#dossies"]);
  if(p.altas.length > 0) items.push(["urgente","🎯","<b>"+p.altas.length+" vaga"+(p.altas.length>1?"s quentes":" quente")+" sem candidatura</b>, começando por "+esc(p.altas[0].name.split(/ - | \(/)[0]),"#portais","alta"]);
  if(p.aMao.length > 0) items.push(["atencao","🖐️","<b>"+p.aMao.length+" candidaturas só à mão</b>: captcha de desafio, conta com senha ou portal que não abre para a automação","#portais","mao"]);
  if(p.grandeMao.length > 0) items.push(["atencao","🏆","<b>"+p.grandeMao.length+" portais de estúdio grande só abrem na sua mão</b> ("+p.grandeMao.map(g=>esc(g[0].split(/[,:(]/)[0].trim())).join(", ")+")","#grandes"]);
  if(p.alertaBloq.length > 0) items.push(["atencao","🔔","<b>"+p.alertaBloq.length+" alertas de vaga travados no captcha</b> ("+p.alertaBloq.map(g=>esc(g[0].replace(/\s+Studios$/,""))).join(", ")+"): dois minutos cada","#grandes"]);
  if(p.pedidas.length > 0) items.push(["atencao","📝","<b>"+p.pedidas.length+" "+(p.pedidas.length>1?"estúdios pediram":"estúdio pediu")+" candidatura por formulário</b> na resposta ao seu email","#portais","abertas"]);
  if(c.drafts > 0) items.push(["info","✉️","<b>"+c.drafts+" rascunho"+(c.drafts>1?"s":"")+"</b> no Gmail esperando o Apps Script (enviarRascunhos)","#estudios"]);
  const devidos = STUDIOS.filter(followUpDevido);
  if(devidos.length > 0) items.push(["info","⏰","<b>Follow-up vencido</b> em "+devidos.length+" estúdio"+(devidos.length>1?"s":"")+" sem resposta; o Comunicador manda o lembrete de 7 dias às 11h05","#estudios"]);
  if(items.length===0) items.push(["boa","✅","<b>Tudo em dia.</b> Nada pendente na sua mão agora",""]);
  const PESO = {urgente:0, atencao:1, info:2, boa:3};
  items.sort((a,b)=>PESO[a[0]]-PESO[b[0]]);
  $("#acoesList").innerHTML = items.map(([cls,ic,txt,href,filtro])=>
    '<a class="acao '+cls+'" href="'+(href||"#hoje")+'"'+(filtro!==undefined?' data-filtro="'+filtro+'"':'')+' data-alvo="'+(href||"").slice(1)+'"><span class="ic">'+ic+'</span><span>'+txt+'</span><span class="go">ver →</span></a>').join("");
  $("#acoesList").querySelectorAll(".acao").forEach(a=>a.addEventListener("click", ()=>abrirSecao(a.dataset.alvo, a.dataset.filtro)));
  const urg = items.filter(i=>i[0]==="urgente").length;
  $("#acoesBadge").textContent = urg ? urg+" urgente"+(urg>1?"s":"") : items[0][0]==="boa" ? "em dia" : items.length+" itens";
  $("#nAcoes").textContent = urg || "";
}

/* ---------- conversas ---------- */
function renderConversas(){
  const vivos = CONTACTED.filter(s=>["respondeu","conversa","entrevista","oferta"].includes(stageKnown(s)));
  const ORD = {oferta:0, entrevista:1, conversa:2, respondeu:3};
  vivos.sort((a,b)=>ORD[stageKnown(a)]-ORD[stageKnown(b)] || b.batch-a.batch);
  const rec = CONTACTED.filter(s=>stageKnown(s)==="recusado").length;
  $("#conversasList").innerHTML = vivos.length ? vivos.map(s=>{
    const st = stageKnown(s);
    return '<div class="c"><div class="n">'+esc(s.name.split(" (")[0])+'</div><div class="p">'+esc(s.country)+' · <a href="mailto:'+esc(s.email)+'">'+esc(s.email)+'</a></div>'
      + '<div class="e"><span class="pill '+STAGE_PILL[st]+'">'+STAGE_LABEL[st]+'</span> <span class="pill mute">carta de '+fmtBR(dataDoLote(s.batch))+'</span></div></div>';
  }).join("") : '<p class="hint">Nenhuma conversa aberta agora. As respostas humanas aparecem aqui quando o Comunicador as registra.</p>';
  $("#convBadge").textContent = vivos.length+" aberta"+(vivos.length===1?"":"s")+" · "+rec+" recusa"+(rec===1?"":"s");
  $("#nConv").textContent = vivos.length || "";
}

/* ---------- novidades ---------- */
const NOV_META = { viva:["🎉","Em andamento"], vaga:["🔥","Vaga quente"], porta:["📝","Candidatura"], nao:["✕","Sem sequência"], alerta:["⚠️","Regra ou correção"], envio:["📤","Envios"] };
let novFilter = "", novLimite = 20;
function renderNovidades(){
  const sel = NOVIDADES.filter(n=>!novFilter || n[1]===novFilter).slice().sort((a,b)=> a[0] < b[0] ? 1 : a[0] > b[0] ? -1 : 0);
  const mostra = sel.slice(0, novLimite);
  let ultimoDia = "", html = "";
  mostra.forEach(([data,tipo,tit,txt,link])=>{
    if(data !== ultimoDia){ html += '<div class="dia-sep">'+fmtBR(data)+' · '+diaSem(data)+(data===UPDATED?' · hoje':'')+'</div>'; ultimoDia = data; }
    const [ic,tag] = NOV_META[tipo] || NOV_META.porta;
    html += '<article class="post nv-'+esc(tipo)+'" tabindex="0"><div class="pmeta"><span>'+ic+'</span><span class="pcat">'+tag+'</span>'+(data===UPDATED?'<span class="pnovo">novo</span>':'')+'</div>'
      + '<h4 class="ptit">'+esc(tit)+'</h4><p class="ptxt">'+esc(txt)+'</p>'
      + '<div class="pfoot">'+(link?'<a href="'+esc(link)+'" target="_blank" rel="noopener">abrir link oficial →</a> · ':'')+'toque para ler inteiro</div></article>';
  });
  $("#novList").innerHTML = html || '<p class="hint">Nada nessa categoria ainda.</p>';
  $("#novList").querySelectorAll(".post").forEach(el=>{
    const abre = ev => { if(ev.target.tagName!=="A") el.classList.toggle("open"); };
    el.addEventListener("click", abre);
    el.addEventListener("keydown", ev=>{ if(ev.key==="Enter"||ev.key===" "){ ev.preventDefault(); abre(ev); }});
  });
  $("#novMais").style.display = sel.length > novLimite ? "" : "none";
  $("#novMais").textContent = "mostrar mais ("+Math.max(0, sel.length-novLimite)+" restantes)";
  const hoje = NOVIDADES.filter(n=>n[0]===UPDATED).length;
  $("#novBadge").textContent = (hoje ? hoje+(hoje===1?" nova hoje · ":" novas hoje · ") : "")+NOVIDADES.length+" no total";
  $("#nNov").textContent = hoje || "";
  const chips = [["","Tudo",NOVIDADES.length], ...Object.keys(NOV_META).map(k=>[k,NOV_META[k][0]+" "+NOV_META[k][1],NOVIDADES.filter(n=>n[1]===k).length])].filter(([k,,n])=>k===""||n>0);
  $("#novChips").innerHTML = chips.map(([val,label,n])=>'<button class="chipbtn'+(novFilter===val?" on":"")+'" data-n="'+val+'" type="button">'+esc(label)+'<span class="n">'+n+'</span></button>').join("");
  $("#novChips").querySelectorAll("button").forEach(b=>b.addEventListener("click", ()=>{ novFilter = b.dataset.n; novLimite = 20; renderNovidades(); }));
}

/* ---------- formularios e portais ---------- */
let portalFiltro = "", portalLimite = 40;
const PORTAL_BALDES = [
  ["",         "De pé",            p => !isMorta(p)],
  ["abertas",  "Sem candidatura",  p => !isApplied(p) && !isMorta(p)],
  ["personagem","🎭 Personagem",    p => !isApplied(p) && !isMorta(p) && isPersonagem(p)],
  ["alta",     "🔥 Quente",        p => !isApplied(p) && !isMorta(p) && prioOf(p)==="alta"],
  ["mao",      "🖐️ Só à mão",      p => !isApplied(p) && !isMorta(p) && A_MAO_RE.test(p.note||"")],
  ["remota",   "🌐 Remota",        p => !isApplied(p) && !isMorta(p) && isRemoto(p)],
  ["feitas",   "✓ Feitas",         p => isApplied(p)],
  ["mortas",   "⨯ Encerradas",     p => isMorta(p)]
];
const baldeDoPortal = k => (PORTAL_BALDES.find(b=>b[0]===k) || PORTAL_BALDES[0])[2];
function notaHtml(texto, limite){
  const longa = (texto||"").length > (limite||180);
  return '<div class="nota"><span class="ncorpo">'+esc(texto)+'</span>'+(longa?'<button class="morebtn nmais" type="button">ler a nota inteira</button>':'')+'</div>';
}
function bindNotas(scope){
  scope.querySelectorAll(".nmais").forEach(b=>b.addEventListener("click", ()=>{
    const nota = b.closest(".nota"); nota.classList.toggle("aberta");
    b.textContent = nota.classList.contains("aberta") ? "recolher" : "ler a nota inteira";
  }));
}
function renderPortais(){
  const q = ($("#portalQ").value||"").trim().toLowerCase();
  const mortas = PORTAIS.filter(isMorta);
  const rows = PORTAIS.filter(baldeDoPortal(portalFiltro)).filter(p=>!q || [p.name,p.country,p.note].some(t=>String(t||"").toLowerCase().includes(q))).sort((a,b)=>{
    const pa = isApplied(a)?1:0, pb = isApplied(b)?1:0; if(pa!==pb) return pa-pb;
    const wa = PRIO_W[prioOf(a)], wb = PRIO_W[prioOf(b)]; if(wa!==wb) return wa-wb;
    const ra = isRemoto(a)?0:1, rb = isRemoto(b)?0:1; if(ra!==rb) return ra-rb;
    if(a.origem!==b.origem) return a.origem==="email" ? -1 : 1;
    return a.name.localeCompare(b.name);
  });
  const mostra = rows.slice(0, portalLimite);
  $("#portalRows").innerHTML = mostra.map(p=>{
    const done = isApplied(p), prio = prioOf(p), morta = isMorta(p);
    const tags = [];
    if(p.done) tags.push('<span class="pill good">✓ confirmada</span>'); else if(done) tags.push('<span class="pill good">✓ marcada</span>');
    if(!done && !morta) tags.push(prio==="alta" ? '<span class="pill acc">🔥 quente</span>' : prio==="media" ? '<span class="pill warn">média</span>' : '<span class="pill mute">baixa</span>');
    if(!done && isPersonagem(p)) tags.push('<span class="pill blue">🎭 personagem</span>');
    if(!done && A_MAO_RE.test(p.note||"")) tags.push('<span class="pill warn">🖐️ à mão</span>');
    if(isRemoto(p)) tags.push('<span class="pill blue">🌐 remoto</span>');
    if(p.origem==="email") tags.push('<span class="pill warn">pediram por email</span>');
    if(morta) tags.push('<span class="pill crit">encerrada</span>');
    return '<div class="linha '+(done?"feita":morta?"morta":"prio-"+prio)+'">'
      + '<input type="checkbox" data-url="'+esc(p.url)+'"'+(done?" checked":"")+(p.done?" disabled":"")+' aria-label="Marcar '+esc(p.name)+' como aplicada">'
      + '<div><div class="nome">'+esc(p.name)+'</div><div class="meta-l">'+esc(p.country)+'</div><div class="tags">'+tags.join(" ")+'</div></div>'
      + '<div class="acoes-l"><a href="'+esc(p.url)+'" target="_blank" rel="noopener">abrir ↗</a></div>'
      + notaHtml(p.note)+'</div>';
  }).join("") || '<p class="hint">Nada nesta situação agora.</p>';
  bindNotas($("#portalRows"));
  $("#portalMais").style.display = rows.length > portalLimite ? "" : "none";
  $("#portalMais").textContent = "mostrar mais ("+Math.max(0, rows.length-portalLimite)+" restantes)";
  $("#portalChips").innerHTML = PORTAL_BALDES.map(([k,label,teste])=>'<button class="chipbtn'+(portalFiltro===k?" on":"")+'" data-b="'+k+'" type="button">'+esc(label)+'<span class="n">'+PORTAIS.filter(teste).length+'</span></button>').join("");
  $("#portalChips").querySelectorAll("button").forEach(b=>b.addEventListener("click", ()=>{ portalFiltro = b.dataset.b; portalLimite = 40; renderPortais(); }));
  $("#portalRows").querySelectorAll("input[type=checkbox]").forEach(cb=>cb.addEventListener("change", ()=>{
    if(cb.checked) applied[cb.dataset.url] = true; else delete applied[cb.dataset.url];
    saveApplied(); cb.closest(".linha").classList.toggle("feita", cb.checked); portalResumo(); renderAcoes(); renderTiles();
  }));
  portalResumo(mortas.length);
}
function segbar(alvo, legAlvo, segs, unidade){
  const usados = segs.filter(s=>s[1]>0), total = usados.reduce((a,s)=>a+s[1],0) || 1;
  $(alvo).innerHTML = usados.map(([l,v,c])=>'<i style="width:'+(100*v/total)+'%;background:'+c+'" data-tip="<b>'+esc(l)+'</b>'+v+' '+esc(unidade)+'"></i>').join("");
  $(legAlvo).innerHTML = segs.map(([l,v,c])=>'<span><i class="dot" style="background:'+c+'"></i>'+esc(l)+' <b>'+v+'</b></span>').join("");
  bindTips($(alvo));
}
function portalResumo(mortasCount){
  const p = pendencias(), doneCount = PORTAIS.filter(isApplied).length;
  const mortas = typeof mortasCount==="number" ? mortasCount : PORTAIS.filter(isMorta).length;
  const manuais = p.aMao.length, pers = PORTAIS.filter(baldeDoPortal("personagem")).length;
  segbar("#portalBarra","#portalBarraLegend",[["Feitas",doneCount,css("--good")],["Abertas, só à mão",manuais,css("--warn")],["Abertas para a automação",p.abertos.length-manuais,css("--blue")],["Encerradas",mortas,css("--line-2")]],"rotas");
  $("#portalBadge").textContent = doneCount+" feitas · "+p.abertos.length+" abertas · "+pers+" de personagem";
  $("#nPort").textContent = pers || "";
  $("#portalHint").innerHTML = "<b>"+p.abertos.length+" portas abertas</b>, "+pers+" delas de personagem e "+manuais+" que só você consegue enviar (captcha, conta ou portal fechado para a automação). "
    + p.pedidas.length+" "+(p.pedidas.length===1?"pedido feito por email":"pedidos feitos por email")+". As "+mortas+" encerradas ficam fora da lista até você pedir. Marque o que enviar; o selo verde vem quando a automação vê a confirmação.";
}

/* ---------- estudios grandes ---------- */
function renderGrandes(){
  const rows = GRANDES.map(([name,sede,url,via,note,done])=>({name,sede,url,via,note,done:!!done}));
  const feito = g => g.done || !!applied[g.url];
  rows.sort((a,b)=>(feito(a)?1:0)-(feito(b)?1:0) || a.name.localeCompare(b.name));
  const VIA = { ats:'<span class="pill mute">portal/ATS</span>', form:'<span class="pill good">aceita portfólio sem vaga</span>', email:'<span class="pill warn">email</span>' };
  const AL = { ativo:'<span class="pill good">🔔 alerta ativo</span>', bloqueado:'<span class="pill warn">🔔 alerta travado no captcha</span>', inexistente:'<span class="pill mute">sem alerta no portal</span>', indefinido:'' };
  $("#grandeRows").innerHTML = rows.map(g=>{
    const done = feito(g), al = alertaDoGrande([g.name,g.sede,g.url,g.via,g.note]);
    return '<div class="linha'+(done?" feita":"")+'"><input type="checkbox" data-url="'+esc(g.url)+'"'+(done?" checked":"")+(g.done?" disabled":"")+' aria-label="Marcar '+esc(g.name)+'">'
      + '<div><div class="nome">'+esc(g.name)+'</div><div class="meta-l">'+esc(g.sede)+'</div><div class="tags">'+(g.done?'<span class="pill good">✓ enviado</span> ':'')+(VIA[g.via]||VIA.ats)+' '+(AL[al]||'')+'</div></div>'
      + '<div class="acoes-l"><a href="'+esc(g.url)+'" target="_blank" rel="noopener">carreiras ↗</a></div>'+notaHtml(g.note)+'</div>';
  }).join("");
  bindNotas($("#grandeRows"));
  const feitos = rows.filter(feito).length, al = k => GRANDES.filter(g=>alertaDoGrande(g)===k).length;
  segbar("#grandeAlerta","#grandeAlertaLegend",[["Alerta ativo",al("ativo"),css("--good")],["Travado no captcha",al("bloqueado"),css("--warn")],["Portal sem alerta",al("inexistente"),css("--blue")],["Sem informação",al("indefinido"),css("--line-2")]],"estúdios");
  $("#grandeBadge").textContent = feitos+" de "+GRANDES.length+" com candidatura";
  $("#grandeHint").innerHTML = "<b>"+feitos+" dos "+GRANDES.length+" já receberam candidatura</b> e "+GRANDES.filter(g=>g[3]==="form").length+" aceitam portfólio sem vaga aberta. Quase nenhum aceita email: a entrega aqui é o link certo e o alerta de vaga.";
  $("#grandeRows").querySelectorAll("input[type=checkbox]").forEach(cb=>cb.addEventListener("change", ()=>{
    if(cb.checked) applied[cb.dataset.url] = true; else delete applied[cb.dataset.url];
    saveApplied(); renderGrandes(); renderAcoes(); renderTiles();
  }));
}

/* ---------- numeros ---------- */
function renderFormsChart(){
  const rows = DAILY.filter(d=>(d[3]||0)>0 || d[0]>="2026-09-01").slice(-28);
  const maxV = Math.max(META_DIA.formularios+2, ...rows.map(r=>r[3]||0));
  const W=520, H=170, padB=24, padT=12, padL=28, slot=(W-padL-6)/Math.max(rows.length,1), bw=Math.min(16, slot*0.66);
  const y = v => padT + (H-padT-padB)*(1 - v/maxV), acc = css("--accent");
  let s = '<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Formulários confirmados por dia">';
  [0, Math.round(maxV/2), maxV].forEach(t=>{ s += '<line x1="'+padL+'" x2="'+W+'" y1="'+y(t)+'" y2="'+y(t)+'" stroke="'+css("--line")+'"/><text x="'+(padL-4)+'" y="'+(y(t)+4)+'" text-anchor="end" font-size="10">'+t+'</text>'; });
  const ym = y(META_DIA.formularios);
  s += '<line x1="'+padL+'" x2="'+W+'" y1="'+ym+'" y2="'+ym+'" stroke="'+css("--crit")+'" stroke-dasharray="4 3" opacity=".7"/>';
  rows.forEach((r,i)=>{
    const cx = padL + slot*i + slot/2, f=r[3]||0, c=r[4]||0;
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(f)+'" width="'+bw+'" height="'+(y(0)-y(f))+'" rx="3" fill="'+acc+'" opacity=".35"><title>'+fmtBR(r[0])+': '+f+' formulários, '+c+' de personagem</title></rect>';
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(c)+'" width="'+bw+'" height="'+(y(0)-y(c))+'" rx="3" fill="'+acc+'"/>';
    if(rows.length<=14 || i%3===0) s += '<text x="'+cx+'" y="'+(H-8)+'" text-anchor="middle" font-size="10">'+fmtBR(r[0])+'</text>';
  });
  s += '</svg>';
  $("#formsChart").innerHTML = s;
  $("#formsLeg").innerHTML = '<span><i class="dot" style="background:'+acc+'"></i>personagem</span><span><i class="dot" style="background:'+acc+';opacity:.35"></i>outros</span><span><i class="dot" style="background:'+css("--crit")+'"></i>meta de '+META_DIA.formularios+'</span>';
}
function renderMailChart(){
  const rows = DAILY.slice(-28);
  const maxV = Math.max(10, ...rows.map(r=>Math.max(r[1]||0, r[2]||0)));
  const W=520, H=170, padB=24, padT=12, padL=34, slot=(W-padL-6)/Math.max(rows.length,1), bw=Math.min(16, slot*0.66);
  const y = v => padT + (H-padT-padB)*(1 - v/maxV), blue = css("--blue"), teal = css("--teal");
  let s = '<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Emails e respostas por dia">';
  [0, Math.round(maxV/2), maxV].forEach(t=>{ s += '<line x1="'+padL+'" x2="'+W+'" y1="'+y(t)+'" y2="'+y(t)+'" stroke="'+css("--line")+'"/><text x="'+(padL-4)+'" y="'+(y(t)+4)+'" text-anchor="end" font-size="10">'+t+'</text>'; });
  rows.forEach((r,i)=>{
    const cx = padL + slot*i + slot/2, e=r[1]||0, h=r[2]||0;
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(e)+'" width="'+bw+'" height="'+(y(0)-y(e))+'" rx="3" fill="'+blue+'" opacity=".55"><title>'+fmtBR(r[0])+': '+e+' emails, '+h+' respostas humanas</title></rect>';
    s += '<rect x="'+(cx-bw/2)+'" y="'+y(h)+'" width="'+bw+'" height="'+(y(0)-y(h))+'" rx="3" fill="'+teal+'"/>';
    if(rows.length<=14 || i%3===0) s += '<text x="'+cx+'" y="'+(H-8)+'" text-anchor="middle" font-size="10">'+fmtBR(r[0])+'</text>';
  });
  s += '</svg>';
  $("#mailChart").innerHTML = s;
  $("#mailLeg").innerHTML = '<span><i class="dot" style="background:'+blue+';opacity:.55"></i>emails enviados</span><span><i class="dot" style="background:'+teal+'"></i>respostas humanas</span>';
}
function renderFunnel(){
  const c = counts();
  const steps = [["Emails enviados", ENVIOS],["Entregues", c.delivered],["Respostas", c.resp],["Em conversa", c.conv],["Entrevistas", c.ent],["Ofertas", c.off]];
  const W=460, rowH=32, padL=110, padR=50, H=steps.length*rowH+6, max=ENVIOS||1, acc = css("--accent");
  let s = '<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Funil do email">';
  steps.forEach(([l,v],i)=>{
    const y=i*rowH+6, bw=Math.max(v>0?4:0,(W-padL-padR)*v/max), pct = i===0 ? "" : " ("+Math.round(100*v/max)+"%)";
    s += '<text x="'+(padL-8)+'" y="'+(y+18)+'" text-anchor="end">'+esc(l)+'</text><rect x="'+padL+'" y="'+y+'" width="'+bw+'" height="24" rx="6" fill="'+acc+'" opacity="'+(1-i*0.12)+'"/><text x="'+(padL+bw+6)+'" y="'+(y+17)+'" font-weight="600">'+v+pct+'</text>';
  });
  $("#funnel").innerHTML = s+'</svg>';
}
function renderStatusBar(){
  const c = counts();
  segbar("#statusbar","#statusLegend",[["Aguardando resposta",c.aguard,css("--blue")],["Conversa aberta",c.conv,css("--good")],["Recusa",c.rec,css("--crit")],["Bounce",c.bounce,css("--warn")],["Rascunho",c.drafts,css("--line-2")]],"emails");
}
function renderPaises(){
  const byC = {}, rotulo = {}, vistos = new Set();
  // "Suecia" e "Suécia" sao o mesmo pais: agrupa pela forma sem acento e mostra o rotulo mais comum
  const pais = t => String(t||"").split(/[;(,]/)[0].trim().replace(/^\s*(EUA|USA|Estados Unidos)\b.*/,"EUA") || "?";
  const chave = t => t.toLowerCase().normalize("NFD").replace(/[^a-z ]/g,"");
  const soma = t => { const k = chave(t); byC[k]=(byC[k]||0)+1; rotulo[k]=rotulo[k]||{}; rotulo[k][t]=(rotulo[k][t]||0)+1; };
  STUDIOS.forEach(s=>{ const k = s.email.trim().toLowerCase(); if(vistos.has(k)) return; vistos.add(k); soma(pais(s.country)); });
  PORTAIS.filter(isApplied).forEach(p=>{ const k = normName(p.name); if(vistos.has(k)) return; vistos.add(k); soma(pais(p.country)); });
  const rows = Object.entries(byC).sort((a,b)=>b[1]-a[1]).slice(0,16).map(([k,v])=>[Object.entries(rotulo[k]).sort((a,b)=>b[1]-a[1])[0][0], v]);
  const W=1000, rowH=24, padL=150, padR=40, H=rows.length*rowH+8, max=(rows[0]||[0,1])[1], teal = css("--teal");
  let s = '<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Estúdios por país">';
  rows.forEach(([l,v],i)=>{ const y=i*rowH+5, bw=(W-padL-padR)*v/max;
    s += '<text x="'+(padL-8)+'" y="'+(y+14)+'" text-anchor="end">'+esc(l)+'</text><rect x="'+padL+'" y="'+y+'" width="'+bw+'" height="16" rx="4" fill="'+teal+'"/><text x="'+(padL+bw+6)+'" y="'+(y+13)+'" font-weight="600">'+v+'</text>'; });
  $("#paises").innerHTML = s+'</svg>';
}

/* ---------- pessoas (Joe) ---------- */
const CONF_ROTULO = { alta:"alta", media:"média", "sem-email":"sem email" };
const CONF_PILL = { alta:"good", media:"warn", "sem-email":"mute" };
let joeFiltro = "todas", joeLimite = 30;
function sitPill(s){
  const t = String(s||"").toLowerCase();
  if(t.startsWith("enviado")) return '<span class="pill good">✓ '+esc(s.slice(0,40))+'</span>';
  if(t === "bounce") return '<span class="pill crit">✕ não chegou</span>';
  if(t.startsWith("rascunho") || /^r-?\d{6,}/.test(t)) return '<span class="pill blue">rascunho pronto</span>';
  if(t.startsWith("pendente")) return '<span class="pill warn">carta a escrever</span>';
  if(t.startsWith("segurad")) return '<span class="pill mute">segurada</span>';
  const curto = String(s||"sem via"); return '<span class="pill mute" title="'+esc(curto)+'">'+esc(curto.length>30 ? curto.slice(0,28)+"…" : curto)+'</span>';
}
function renderJoe(){
  const total = PESSOAS.length, por = c => PESSOAS.filter(p=>p.confianca===c).length;
  const comEmail = PESSOAS.filter(p=>p.email).length, estudios = new Set(PESSOAS.map(p=>p.estudio)).size;
  $("#joeTotalEnvios").textContent = ENVIOS; $("#joeComNome").textContent = ESTUDIOS_PESSOA;
  $("#joeBadge").textContent = total ? total+" pessoas · "+comEmail+" com email · "+estudios+" estúdios" : "ainda sem rodada";
  $("#nJoe").textContent = total || "";
  $("#joeTiles").innerHTML = [["👤",total,"Pessoas capturadas",estudios+" estúdios alcançados por nome"],["✉️",comEmail,"Com endereço",por("alta")+" publicados · "+por("media")+" por padrão"],["🔑",PADROES.length,"Padrões de domínio","provados por endereços reais"],["📭",por("sem-email"),"Sem endereço ainda","guardados até surgir a via"]]
    .map(([ic,n,l,d])=>'<div class="tile"><div class="h"><span>'+ic+'</span>'+esc(l)+'</div><div class="n">'+n+'</div><div class="d">'+esc(d)+'</div></div>').join("");
  const chips = [["todas","Todas",total],["alta","Confiança alta",por("alta")],["media","Confiança média",por("media")],["sem-email","Sem email",por("sem-email")]];
  $("#joeChips").innerHTML = chips.filter(c=>c[2]||c[0]==="todas").map(([k,l,n])=>'<button class="chipbtn'+(joeFiltro===k?" on":"")+'" data-joe="'+k+'" type="button">'+esc(l)+'<span class="n">'+n+'</span></button>').join("");
  $("#joeChips").querySelectorAll("button").forEach(b=>b.addEventListener("click", ()=>{ joeFiltro = b.dataset.joe; joeLimite = 30; renderJoe(); }));
  const lista = (joeFiltro==="todas" ? PESSOAS : PESSOAS.filter(p=>p.confianca===joeFiltro)).slice().sort((a,b)=> (b.data||"").localeCompare(a.data||""));
  $("#joeRows").innerHTML = lista.length ? lista.slice(0,joeLimite).map(p=>'<div class="linha sem-check"><div><div class="nome">'+esc(p.pessoa)+' <span style="color:var(--muted);font-weight:400">· '+esc(p.cargo)+'</span></div><div class="meta-l">'+esc(p.estudio)+' · '+esc(p.pais)+(p.data?' · '+fmtBR(p.data):'')+'</div>'
      + '<div class="tags">'+sitPill(p.situacao)+' <span class="pill '+(CONF_PILL[p.confianca]||"mute")+'">'+esc(CONF_ROTULO[p.confianca]||p.confianca)+'</span></div></div>'
      + '<div class="acoes-l">'+(p.email?'<a href="mailto:'+esc(p.email)+'">'+esc(p.email)+'</a>':'<span class="hint" style="margin:0">sem endereço</span>')+'</div>'
      + notaHtml("De onde saiu: "+p.fonte, 140)+'</div>').join("") : '<p class="hint">Nenhuma pessoa nesta faixa ainda.</p>';
  bindNotas($("#joeRows"));
  $("#joeMais").style.display = lista.length > joeLimite ? "" : "none";
  $("#joeMais").textContent = "mostrar mais ("+Math.max(0,lista.length-joeLimite)+" restantes)";
  $("#joePadroes").innerHTML = PADROES.length ? '<table class="tabela"><thead><tr><th>Domínio</th><th>Formato</th><th>Provado por</th></tr></thead><tbody>'+PADROES.map(p=>'<tr><td><b>'+esc(p.dominio)+'</b></td><td><code>'+esc(p.formato)+'</code></td><td style="color:var(--muted)">'+esc(p.prova)+'</td></tr>').join("")+'</tbody></table>' : '<p class="hint">Nenhum padrão provado ainda.</p>';
  const ESTADO = { rodando:["🔄","info","rodando agora"], proximo:["⏭️","atencao","próximo"], regra:["📌","boa","regra fixa"] };
  $("#joePassos").innerHTML = JOE_PASSOS.map(([t,d,e])=>{ const [ic,cls,rot] = ESTADO[e] || ESTADO.proximo; return '<div class="acao '+cls+'"><span class="ic">'+ic+'</span><span><b>'+esc(t)+'</b> <span class="pill mute">'+rot+'</span><div class="hint" style="margin:3px 0 0">'+esc(d)+'</div></span></div>'; }).join("");
}

/* ---------- prospeccao ---------- */
function renderProspec(){
  const ordem = {alta:0, media:1, baixa:2};
  const fora = PROSPECTOS.filter(r=>r[5]==="fora").sort((a,b)=>a[0].localeCompare(b[0]));
  const rows = PROSPECTOS.filter(r=>r[5]!=="fora").sort((a,b)=>((ordem[a[5]]??3)-(ordem[b[5]]??3)) || ((a[3]?0:1)-(b[3]?0:1)) || a[0].localeCompare(b[0]));
  const comEmail = rows.filter(r=>r[3]).length;
  $("#prospecBadge").textContent = rows.length ? rows.length+" para aplicar" : "vazio";
  $("#prospecHint").innerHTML = rows.length ? "Estúdios garimpados em diretório e curados à mão: <b>"+rows.length+"</b> que valem candidatura, <b>"+comEmail+"</b> com email verificado. Ainda não contatados; todos aparecem no seletor do Kit." : "Nada aqui ainda.";
  $("#prospecRows").innerHTML = rows.map(([nome,local,site,email,nota,prio])=>'<div class="linha sem-check prio-'+esc(prio)+'"><div><div class="nome">'+esc(nome)+'</div><div class="meta-l">'+esc(local)+'</div><div class="tags">'+(prio==="alta"?'<span class="pill acc">🔥 alta</span>':prio==="media"?'<span class="pill warn">média</span>':'<span class="pill mute">baixa</span>')+'</div></div>'
    + '<div class="acoes-l">'+(email?'<a href="mailto:'+esc(email)+'">'+esc(email)+'</a>':'<span class="hint" style="margin:0">sem email público</span>')+(site?'<a href="'+esc(site)+'" target="_blank" rel="noopener">site ↗</a>':'')+'</div>'+notaHtml(nota)+'</div>').join("");
  bindNotas($("#prospecRows"));
  $("#prospecFora").innerHTML = fora.length ? '<details style="margin-top:12px"><summary class="hint" style="cursor:pointer">Descartados na checagem ('+fora.length+'), só registro</summary><ul class="hint" style="margin:8px 0 0; padding-left:18px; line-height:1.7">'+fora.map(r=>'<li><b>'+esc(r[0])+'</b> ('+esc(r[1])+'): '+esc(r[4])+'</li>').join("")+'</ul></details>' : "";
}

/* ---------- kit ---------- */
function portaLetter(nome, role){
  const studio = nome.replace(/\s*\([^)]*\)\s*/g," ").replace(/\s*\/.*$/,"").trim();
  const alvo = role ? "the "+role+" opening" : "the opening you currently have posted";
  return "Dear "+studio+" team,\n\nI'm writing about "+alvo+", and I'll be straight about why: it is the closest open door I found, and my discipline is character art. I'm a Senior 3D Character Artist and visual development artist with 10+ years in stylized characters.\n\nOn The Wingfeather Saga at Angel Studios I modeled and hand-painted characters for Season 1. For almost five years I've been with E-Line Media in Arizona, US, taking Endstar's hero characters from first sculpt to engine. I also do character grooming in Houdini. My portfolio at artstation.com/viniciuscavalcanti holds more than 45 projects with over 60 characters across many titles, and my personal work keeps the same bar.\n\nIf character art and visual development sit with a different team at "+studio+", I would be grateful if you could pass my portfolio to whoever leads it, and keep me on file for when an opening comes up. If the posted role is open to a senior artist coming from the character side, I'd be glad to talk about that as well.\n\nI've worked fully remote with a US studio for almost five years, so a distributed team is my normal working mode. I'm open to relocating; my academic background (honors laurea, postgraduate specialization, master's in progress, IELTS, publications) makes a strong visa case.\n\nBest,\nVini Cavalcanti";
}
function portaRole(note){ const m = /VAGAS?:\s*([^;.]{3,60})/.exec(note||""); return m ? m[1].trim().replace(/\s+/g," ") : ""; }
function portaPendentes(){
  const out = [], FORA = ["respondeu","entrevista","oferta","recusado"];
  const vivos = new Set(STUDIOS.filter(s=>FORA.includes(stageKnown(s))).map(s=>normName(s.name)));
  PORTAIS.forEach(p=>{
    if(isApplied(p) || vivos.has(normName(p.name)) || /NÃO APLICAR|SEM VAGAS ABERTAS|VAGA EXPIRADA/i.test(p.note||"")) return;
    const role = portaRole(p.note); if(role && CHAR_RE.test(role)) return;
    out.push([p.name, role]);
  });
  GRANDES.forEach(g=>{ if(feitoGrande(g) || /NÃO APLICAR/i.test(g[4]||"")) return; out.push([g[0], ""]); });
  const vistos = new Set();
  return out.filter(([n])=>{ const k=n.toLowerCase(); if(vistos.has(k)) return false; vistos.add(k); return true; }).sort((a,b)=>a[0].localeCompare(b[0]));
}
function kitGroups(){
  const pend = portaPendentes();
  return KIT.concat([["🚪 Porta de entrada · "+pend.length+" formulários ainda não enviados", [["Versão curta (campo pequeno)", PORTA_CURTA]].concat(pend.map(([n,role])=>[n+(role?" · "+role:""), portaLetter(n, role)]))]]);
}
let KIT_GROUPS = KIT;
const kitStudioName = () => { try { return localStorage.getItem(KIT_STUDIO_KEY) || ""; } catch(e){ return ""; } };
const kitText = raw => { const s = kitStudioName(); return s ? raw.split("{STUDIO}").join(s) : raw; };
function setupKitStudio(){
  const sel = $("#kitStudio");
  const pend = PORTAIS.filter(p=>!isApplied(p)).map(p=>p.name), done = PORTAIS.filter(p=>isApplied(p)).map(p=>p.name);
  const jaTem = n => pend.includes(n) || done.includes(n);
  const grandesPend = GRANDES.filter(g=>!feitoGrande(g)).map(g=>g[0]).filter(n=>!jaTem(n)), grandesFeitos = GRANDES.filter(feitoGrande).map(g=>g[0]).filter(n=>!jaTem(n));
  const cobertos = new Set([...pend, ...done, ...grandesPend, ...grandesFeitos]);
  const ordemP = {alta:0, media:1, baixa:2};
  const prospec = PROSPECTOS.filter(r=>r[5]!=="fora" && !cobertos.has(r[0])).sort((a,b)=>((ordemP[a[5]]??3)-(ordemP[b[5]]??3)) || a[0].localeCompare(b[0])).map(r=>r[0]);
  prospec.forEach(n=>cobertos.add(n));
  const others = CONTACTED.map(s=>s.name).filter(n=>!cobertos.has(n)).sort((a,b)=>a.localeCompare(b));
  const opt = n=>'<option value="'+n.replace(/"/g,"&quot;")+'">'+esc(n)+'</option>';
  const grupo = (l,a) => a.length ? '<optgroup label="'+l+'">'+a.map(opt).join("")+'</optgroup>' : "";
  sel.innerHTML = '<option value="">— escolha o estúdio —</option>'+grupo("🏆 Estúdios grandes (a fazer)",grandesPend)+grupo("🗺️ Prospecção",prospec)+grupo("Portais pendentes",pend)+grupo("🏆 Estúdios grandes (feitos)",grandesFeitos)+grupo("Portais aplicados",done)+grupo("Outros estúdios contatados",others);
  sel.value = kitStudioName();
  sel.addEventListener("change",()=>{ try { localStorage.setItem(KIT_STUDIO_KEY, sel.value); } catch(e){} renderKit(); });
}
function copiar(txt, b){
  const ok = () => { b.textContent="Copiado ✓"; b.classList.add("ok"); setTimeout(()=>{ b.textContent="Copiar"; b.classList.remove("ok"); },1500); };
  try { navigator.clipboard.writeText(txt).then(ok, ()=>{ const t=document.createElement("textarea"); t.value=txt; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); ok(); }); } catch(e){ ok(); }
}
function renderKit(){
  const s = kitStudioName();
  $("#kitStudioHint").innerHTML = s ? 'Textos com <code>{STUDIO}</code> saem como <b>'+esc(s)+'</b>.' : 'Escolha o estúdio para trocar <code>{STUDIO}</code> automaticamente.';
  const wrap = $("#kitList"), open = [].map.call(wrap.querySelectorAll("details"), d=>d.open);
  KIT_GROUPS = kitGroups();
  wrap.innerHTML = KIT_GROUPS.map(([g,items],gi)=>'<details class="kit-group"'+((open.length?open[gi]:gi===0)?" open":"")+'><summary>'+esc(g)+'</summary>'+items.map(([l,v],i)=>{
    const t = kitText(v), long = t.length>220;
    return '<div class="kit-item"><div class="kl">'+esc(l)+'</div><div class="kv'+(long?" clamped":"")+'" id="kv-'+gi+'-'+i+'">'+esc(t)+'</div><div class="kbtns"><button class="copybtn" data-g="'+gi+'" data-i="'+i+'" type="button">Copiar</button>'+(long?'<button class="morebtn" data-t="kv-'+gi+'-'+i+'" type="button">expandir</button>':'')+'</div></div>';
  }).join("")+'</details>').join("");
  wrap.querySelectorAll(".copybtn").forEach(b=>b.addEventListener("click", ()=>copiar(kitText(KIT_GROUPS[+b.dataset.g][1][+b.dataset.i][1]), b)));
  wrap.querySelectorAll(".morebtn").forEach(b=>b.addEventListener("click", ()=>{ const kv=document.getElementById(b.dataset.t); kv.classList.toggle("open"); b.textContent = kv.classList.contains("open") ? "recolher" : "expandir"; }));
}

/* ---------- preenchedor ---------- */
function renderPreenchedor(){
  const btn = $("#pfGerar"), cop = $("#pfCopiar"), msg = $("#pfMsg"), saida = $("#pfSaida"), tel = $("#pfTel");
  let href = "";
  btn.onclick = () => {
    const n = (tel.value||"").replace(/\D/g,"");
    if(!PREENCHEDOR_SRC){ msg.textContent = "código do preenchedor não foi injetado; rode node automacao/gera-preenchedor.mjs"; return; }
    if(n.length < 8){ msg.textContent = "digite o telefone só com dígitos, sem o código do país"; return; }
    href = "javascript:" + encodeURIComponent(PREENCHEDOR_SRC.replace("@@TELEFONE@@", n));
    saida.innerHTML = '<p><a id="pfLink" href="'+href.replace(/"/g,"&quot;")+'" class="btn" style="background:var(--accent);color:#fff;border-color:transparent;font-weight:600">Preencher candidatura</a></p><p class="hint">Arraste o botão para a barra de favoritos, ou use Copiar e cole no endereço de um favorito novo.</p>';
    cop.style.display = ""; msg.textContent = "pronto, com o número embutido";
  };
  cop.onclick = () => { if(!href) return; try{ navigator.clipboard.writeText(href).then(()=>{ msg.textContent = "copiado"; }); } catch(e){ msg.textContent = "não consegui copiar; selecione o link e copie à mão"; } };
}

/* ---------- dossies ---------- */
function renderDossies(){
  const wrap = $("#dossieList"), falta = DOSSIES.filter(d=>d[4]).length;
  $("#dossieBadge").textContent = DOSSIES.length+" vagas"+(falta?" · "+falta+" na sua mão":"");
  const pendente = DOSSIES.findIndex(d=>d[4]);
  wrap.innerHTML = DOSSIES.map(([studio,role,url,items,faltaEnviar],di)=>'<details class="kit-group"'+(di===(pendente>=0?pendente:0)?" open":"")+'><summary>'+(faltaEnviar?'<span class="pill crit">falta enviar</span> ':'')+esc(studio)+' <span style="color:var(--muted); font-weight:400">· '+esc(role)+'</span></summary>'
    + '<div class="kit-item"><div class="kl">Onde aplicar</div><div class="kv"><a href="'+esc(url)+'" target="_blank" rel="noopener">abrir a vaga ↗</a></div><div class="kbtns"></div></div>'
    + items.map(([l,v],i)=>{ const long = v.length>220; return '<div class="kit-item"><div class="kl">'+esc(l)+'</div><div class="kv'+(long?" clamped":"")+'" id="dv-'+di+'-'+i+'">'+esc(v)+'</div><div class="kbtns"><button class="copybtn dcopy" data-d="'+di+'" data-i="'+i+'" type="button">Copiar</button>'+(long?'<button class="morebtn" data-t="dv-'+di+'-'+i+'" type="button">expandir</button>':'')+'</div></div>'; }).join("")+'</details>').join("");
  wrap.querySelectorAll(".dcopy").forEach(b=>b.addEventListener("click", ()=>copiar(DOSSIES[+b.dataset.d][3][+b.dataset.i][1], b)));
  wrap.querySelectorAll(".morebtn").forEach(b=>b.addEventListener("click", ()=>{ const kv=document.getElementById(b.dataset.t); if(!kv) return; kv.classList.toggle("open"); b.textContent = kv.classList.contains("open") ? "recolher" : "expandir"; }));
}

/* ---------- estudios por email ---------- */
let chipFilter = "", rowsLimite = 50;
function followUp(s){
  if(s.delivery==="rascunho" || s.delivery==="bounce") return "";
  const st = stageKnown(s); if(st!=="aguardando") return "";
  if(FOLLOWUP_PRONTO.has(s.email)) return "follow-up 02/09";
  const due = followUpVence(s), days = Math.ceil((due - Date.now())/864e5);
  return days<=0 ? "follow-up devido desde "+fmtBR(due.toISOString()) : "follow-up em "+days+"d";
}
function renderChips(){
  const countBy = st => STUDIOS.filter(s=>stageKnown(s)===st).length;
  const chips = [["","Todos",STUDIOS.length], ...STAGES.map(st=>[st,STAGE_LABEL[st],countBy(st)])];
  $("#stageChips").innerHTML = chips.map(([val,label,n])=>'<button class="chipbtn'+(chipFilter===val?" on":"")+'" data-f="'+val+'" type="button">'+esc(label)+'<span class="n">'+n+'</span></button>').join("");
  $("#stageChips").querySelectorAll("button").forEach(b=>b.addEventListener("click", ()=>{ chipFilter = b.dataset.f; rowsLimite = 50; renderChips(); renderRows(); }));
}
function renderRows(){
  const q = ($("#q").value||"").trim().toLowerCase();
  const rows = STUDIOS.filter(s=>(!q || [s.name,s.country,s.email].some(t=>t.toLowerCase().includes(q))) && (!chipFilter || stageKnown(s)===chipFilter));
  $("#rows").innerHTML = rows.slice(0,rowsLimite).map(s=>{
    const d = DELIV[s.delivery] || DELIV.ok, st = stageKnown(s), fu = followUp(s);
    const opts = STAGES.map(x=>'<option value="'+x+'"'+(st===x?" selected":"")+'>'+STAGE_LABEL[x]+'</option>').join("");
    return '<div class="linha sem-check"><div><div class="nome">'+esc(s.name)+'</div><div class="meta-l">'+esc(s.country)+' · <a href="mailto:'+esc(s.email)+'">'+esc(s.email)+'</a> · '+(s.batch===0?"pré-campanha":"lote "+s.batch)+' de '+fmtBR(dataDoLote(s.batch))+'</div>'
      + '<div class="tags"><span class="pill mute" style="color:var('+d.color+')">'+esc(d.label)+'</span>'+(fu?' <span class="pill mute">'+esc(fu)+'</span>':'')+'</div></div>'
      + '<div class="acoes-l"><select data-email="'+esc(s.email)+'" aria-label="Andamento de '+esc(s.name)+'">'+opts+'</select></div></div>';
  }).join("") || '<p class="hint">Nenhum estúdio encontrado.</p>';
  $("#rows").querySelectorAll("select").forEach(sel=>sel.addEventListener("change", ()=>{
    progress[sel.dataset.email] = sel.value; if(sel.value==="aguardando") delete progress[sel.dataset.email];
    saveProgress(); renderAll();
  }));
  $("#rowsMais").style.display = rows.length > rowsLimite ? "" : "none";
  $("#rowsMais").textContent = "mostrar mais ("+Math.max(0,rows.length-rowsLimite)+" restantes)";
  $("#tableTitle").textContent = STUDIOS.length+" emails · "+ESTUDIOS_EMAIL+" estúdios";
}

/* ---------- secoes dobraveis, tema, rodape ---------- */
function secoesSalvas(){ try { return JSON.parse(localStorage.getItem(SEC_KEY) || "{}") || {}; } catch(e){ return {}; } }
function salvarSecao(id, aberta){ const s = secoesSalvas(); s[id] = aberta; try { localStorage.setItem(SEC_KEY, JSON.stringify(s)); } catch(e){} }
function setupSecoes(){
  const salvo = secoesSalvas();
  document.querySelectorAll("details.sec").forEach(d=>{
    if(salvo.hasOwnProperty(d.id)) d.open = !!salvo[d.id];
    d.addEventListener("toggle", ()=>salvarSecao(d.id, d.open));
  });
  document.querySelectorAll('.menu a[href^="#"]').forEach(a=>a.addEventListener("click", ()=>abrirSecao(a.getAttribute("href").slice(1))));
}
$("#themeBtn").addEventListener("click", ()=>{
  const root = document.documentElement;
  const dark = root.dataset.theme==="dark" || (!root.dataset.theme && window.matchMedia("(prefers-color-scheme: dark)").matches);
  root.dataset.theme = dark ? "light" : "dark";
  try { localStorage.setItem("campanha-theme", root.dataset.theme); } catch(e){}
  renderAll();
});
try { const t = localStorage.getItem("campanha-theme"); if(t) document.documentElement.dataset.theme = t; } catch(e){}
window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", ()=>renderAll());
$("#q").addEventListener("input", ()=>{ rowsLimite = 50; renderRows(); });
$("#portalQ").addEventListener("input", ()=>{ portalLimite = 40; renderPortais(); });
$("#novMais").addEventListener("click", ()=>{ novLimite += 30; renderNovidades(); });
$("#portalMais").addEventListener("click", ()=>{ portalLimite += 40; renderPortais(); });
$("#joeMais").addEventListener("click", ()=>{ joeLimite += 30; renderJoe(); });
$("#rowsMais").addEventListener("click", ()=>{ rowsLimite += 50; renderRows(); });
$("#exportBtn").addEventListener("click", ()=>{
  const head = "estudio,pais,email,lote,entrega,andamento";
  const lines = STUDIOS.map(s=>[s.name,s.country,s.email,s.batch,(DELIV[s.delivery]||DELIV.ok).label,STAGE_LABEL[stageKnown(s)]].map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(","));
  const blob = new Blob(["﻿"+[head,...lines].join("\n")], {type:"text/csv;charset=utf-8"});
  const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "campanha-status.csv"; a.click(); URL.revokeObjectURL(a.href);
});
$("#resetBtn").addEventListener("click", ()=>{ if(window.confirm("Limpar todas as marcações de andamento?")){ progress={}; saveProgress(); renderAll(); } });

function renderAll(){
  renderPlacar(); renderSemana(); renderAgenda(); renderTiles(); renderAcoes(); renderConversas(); renderNovidades();
  renderPortais(); renderGrandes(); renderFormsChart(); renderMailChart(); renderFunnel(); renderStatusBar(); renderPaises();
  renderJoe(); renderProspec(); renderKit(); renderDossies(); renderChips(); renderRows();
}
$("#updated").innerHTML = "dados de "+fmtBR(UPDATED)+" · <b>publicado "+esc(BUILD)+"</b>";
(function(){
  const CP = candPortal();
  $("#rodapeNums").textContent = (ENVIOS+CP)+" candidaturas no total: "+ENVIOS+" cartas por email para "+ESTUDIOS_EMAIL+" endereços ("+EMAILS_PRE+" na leva pré-campanha e "+EMAILS_CAMPANHA+" de 26/08 em diante) e "+CP+" por portal e formulário"
    + (EMAILS_LOG !== ENVIOS ? "; o log diário soma "+EMAILS_LOG+" emails porque conta follow-ups e respostas" : "")+".";
})();
if (ALERTA) { $("#alertaMsg").textContent = ALERTA; $("#alerta").hidden = false; }
if ((Date.now() - new Date(UPDATED+"T12:00:00Z")) > 2*864e5) {
  $("#alertaMsg").textContent = "o painel não é atualizado desde "+fmtBR(UPDATED)+". A rotina diária pode ter parado."+(ALERTA ? " "+ALERTA : "");
  $("#alerta").hidden = false;
}
setupKitStudio(); renderPreenchedor(); setupSecoes(); renderAll();
