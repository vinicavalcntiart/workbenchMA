// Envia os rascunhos da campanha com a assinatura do Gmail e os anexos (CV e carta).
// Roda dentro da SUA conta Google, no Apps Script (script.google.com), sem proxy e sem token.
//
// COMO USAR (uma vez):
// 1. Abra https://script.google.com, "Novo projeto", cole este arquivo inteiro.
// 2. No menu da esquerda, "Serviços" (+), adicione "Gmail API" (fica como serviço avançado "Gmail").
// 3. Confira PASTA_DRIVE_ID (pasta do Drive com Vini_Cavalcanti_CV.pdf e Vini_Cavalcanti_Cover_Letter.pdf).
// 4. Com SIMULAR = true, rode a função enviarRascunhos e autorize; o log só lista o que seria enviado.
// 5. Troque SIMULAR para false e rode de novo. Cada execução envia até MAX_POR_EXECUCAO; rode mais vezes se sobrar.
//
// O que ele faz com cada rascunho da campanha (assunto fixo abaixo):
// - pega o HTML do rascunho, acrescenta a assinatura que você usa (a marcada como padrão em Configurações > Assinatura),
// - anexa os dois PDFs, envia e o rascunho sai da caixa de rascunhos.
// Ele NÃO mexe em rascunhos com outro assunto.
//
// DUAS FUNÇÕES, DUAS COTAS DIFERENTES, e é isso que dá a saída para o teto de 100 por dia:
//   prepararRascunhos()  -> completa o rascunho com assinatura e anexos e NÃO envia nada.
//                           Gasta a cota de leitura e escrita do Gmail, que é enorme. Depois é
//                           só disparar pela interface do Gmail, que tem teto próprio e maior.
//   enviarRascunhos()    -> completa E envia. Gasta a cota de ENVIO, a que trava em 100 nesta conta.
// Se a cota de envio estiver zerada, use a primeira e mande à mão.

const ASSUNTO = "Senior Character Artist · Wingfeather Saga credit · stylized + grooming";
const PASTA_DRIVE_ID = "1A3lzDurErp2bHh9s8jbEW7TLMnswxmi8";
const NOMES_ANEXOS = ["Vini_Cavalcanti_CV.pdf", "Vini_Cavalcanti_Cover_Letter.pdf"];
const MAX_POR_EXECUCAO = 40;   // execução do Apps Script dura no máximo 6 minutos
const PAUSA_MS = 1500;         // pausa entre envios
const SIMULAR = true;          // true = só lista no log; false = envia de verdade

// ARMADILHA DO LINK, resolvida aqui em 03/09/2026.
// O compositor do Gmail reescreve TODO link ao gravar o rascunho, virando
// https://www.google.com/url?q=<destino>&source=gmail&ust=...  Isso acontece na API,
// não por copiar link de thread nenhuma, então não dá para evitar na hora de escrever
// o rascunho: o jeito é desfazer a reescrita aqui, imediatamente antes de enviar.
// Num email frio o link embrulhado parece rastreador de spam, e no corpo em texto puro
// a URL gigante aparece inteira.
function limparLinks(texto) {
  if (!texto) return texto;
  return texto.replace(/https?:\/\/(?:www\.)?google\.com\/url\?[^\s"'<>]*/gi, function (todo) {
    var m = /[?&](?:amp;)?q=([^&\s"'<>]+)/i.exec(todo);
    if (!m) return todo;
    var destino = m[1].replace(/&amp;/g, "&");
    try { destino = decodeURIComponent(destino); } catch (e) {}
    // O Gmail às vezes devolve o destino rebaixado para http e sem www. Nos
    // domínios do Vini isso fica feio no corpo em texto puro, então volta ao
    // endereço canônico. Só nos domínios dele: reescrever link de terceiro seria
    // mexer em coisa que não é nossa.
    destino = destino
      .replace(/^http:\/\/(?:www\.)?artstation\.com\//i, "https://www.artstation.com/")
      .replace(/^http:\/\/(?:www\.)?linkedin\.com\//i, "https://www.linkedin.com/")
      .replace(/^http:\/\/(?:www\.)?vinicavalcanti\.com/i, "https://vinicavalcanti.com");
    return destino;
  });
}

/* Diz quanta cota de envio a conta tem AGORA. Rode esta função sozinha no editor e
 * leia o número no registro de execução. Ela não envia nada.
 *
 * Como ler o número, porque ele identifica a conta melhor que qualquer suposição:
 *   perto de 100  -> a conta está no teto baixo do Apps Script. Isso vale para Gmail
 *                    comum, para Workspace Individual e para Workspace em teste ou
 *                    recém-criado, que o Google segura por reputação de envio.
 *   perto de 1500 -> Workspace pago normal, e a cota é folgada de verdade.
 * O teto do Apps Script é diferente do teto do Gmail: email mandado à mão pelo site,
 * ou por conector, gasta o do Gmail e não gasta o do script. Só o que o script dispara
 * gasta este aqui.
 */
function cota() {
  const n = MailApp.getRemainingDailyQuota();
  Logger.log("Cota de envio restante agora: " + n);
  Logger.log(n >= 1000 ? "Workspace pago com cota folgada."
    : "Conta no teto baixo (cerca de 100 por dia). Divida os lotes ou envie em dois dias.");
  return n;
}

/* DIAGNÓSTICO DA COTA, escrito em 06/09 porque a conta é Workspace PAGO e mesmo assim o
 * teto lido é de cerca de 100 por dia, e ninguém entendia o motivo.
 *
 * A chave é que a cota do Apps Script NÃO segue o domínio nem o plano pago: ela segue a
 * CONTA QUE EXECUTA O SCRIPT. Se este arquivo mora no Drive de uma conta @gmail.com comum
 * e só manda COMO contact@vinicavalcanti.art através de um alias de envio, o teto é o da
 * conta comum, 100 por dia, por mais que o domínio tenha Workspace pago. É a explicação
 * mais provável e esta função a confirma ou a descarta em uma execução.
 *
 * Rode esta função sozinha, no editor, e leia o registro. Ela não envia nada.
 * COMO LER:
 *   usuário efetivo termina em @gmail.com  -> é isso. O script roda na conta comum. A
 *       correção é copiar o script para o Drive da conta do Workspace e rodar de lá.
 *   usuário efetivo é @vinicavalcanti.art e a cota ainda vem perto de 100 -> não é conta
 *       errada. Aí sobram duas causas, nesta ordem: assinatura Workspace INDIVIDUAL, que é
 *       paga mas o Apps Script trata como conta comum; ou Workspace em teste ou recém
 *       criado, que o Google segura por reputação até o plano firmar.
 *   cota perto de 1500 -> não há limite nenhum a contornar, e o gargalo é outro.
 */
function diagnostico() {
  Logger.log("Conta que EXECUTA o script (é a dona da cota): " + Session.getEffectiveUser().getEmail());
  try {
    Logger.log("Conta ativa na sessão: " + Session.getActiveUser().getEmail());
  } catch (e) {
    Logger.log("Conta ativa na sessão: não foi possível ler (" + e + ")");
  }
  Logger.log("Cota de envio restante agora: " + MailApp.getRemainingDailyQuota());
  const aliases = GmailApp.getAliases();
  Logger.log("Endereços que esta conta pode usar como remetente: " + (aliases.length ? aliases.join(", ") : "nenhum alias, só o endereço principal"));
  Logger.log("Rascunhos da campanha nesta caixa: " + GmailApp.getDrafts().filter(d => d.getMessage().getSubject() === ASSUNTO).length);
  Logger.log("LEIA: se a conta que executa terminar em @gmail.com, o teto de 100 é dela e o Workspace pago do domínio não conta.");
}

// Confere, sem enviar nada, se sobrou algum link embrulhado nos rascunhos da campanha.
function conferirLinks() {
  const rascunhos = GmailApp.getDrafts().filter(d => d.getMessage().getSubject() === ASSUNTO);
  let sujos = 0;
  for (const d of rascunhos) {
    const m = d.getMessage();
    const bruto = m.getBody() + " " + m.getPlainBody();
    if (/google\.com\/url/i.test(bruto)) { sujos++; Logger.log("AINDA EMBRULHADO: " + m.getTo()); }
    if (/google\.com\/url/i.test(limparLinks(bruto))) Logger.log("LIMPEZA FALHOU: " + m.getTo());
  }
  Logger.log(rascunhos.length + " rascunhos, " + sujos + " com link embrulhado (a limpeza corrige no envio)");
}

/* CONFERE TODO RASCUNHO DA CAIXA, sem enviar nada, e diz o que está fora do padrão.
 *
 * Por que ela varre TODOS e não só os do assunto da campanha: o conferirLinks() acima
 * filtra por ASSUNTO, e por isso ele é cego justamente para o pior defeito possível, que
 * é o rascunho com o assunto ERRADO. Rascunho com assunto errado não é só feio: o
 * prepararRascunhos() e o enviarRascunhos() acham os rascunhos POR ESSE ASSUNTO LITERAL,
 * então um assunto trocado deixa a carta invisível para o envio e ela nunca sai. Foi o que
 * aconteceu em 07/09 com a carta do No Ghost, que estava pronta e fora da esteira.
 *
 * Rode sozinha no editor e leia o registro de execução. Ela não altera e não envia nada.
 */
function conferirRascunhos() {
  const LINKS = [
    ["ArtStation", /artstation\.com\/viniciuscavalcanti/i],
    ["LinkedIn", /linkedin\.com\/in\/vinicavalcnti/i],
    ["site", /vinicavalcanti\.com/i]
  ];
  // Pedir tempo em carta fria custa mais que a recusa, e a regra da campanha proíbe.
  const PEDIDO_DE_TEMPO = /\b(a call|a chat|a meeting|coffee|fifteen minutes|twenty minutes|15 minutes|20 minutes|chance to talk|hop on a call|your time)\b/i;
  const PROIBIDO = [
    ["a palavra Brazil", /\bbrazil\b/i],
    ["travessão", /—/],
    ["'I hope this finds you well'", /hope this (email )?finds you well/i],
    ["assinatura como Vinicius", /\bvinicius\b/i],
    ["htmlBody escapado", /&lt;(p|a|br|b)\b/i]
  ];
  const rascunhos = GmailApp.getDrafts();
  let comProblema = 0;
  for (const d of rascunhos) {
    const m = d.getMessage();
    const para = m.getTo();
    const assunto = m.getSubject();
    const html = m.getBody() || "";
    const texto = m.getPlainBody() || "";
    const tudo = html + " " + texto;
    const faltas = [];

    if (assunto !== ASSUNTO) {
      faltas.push("ASSUNTO FORA DO PADRÃO, o envio NUNCA vai achar este rascunho. Está: \"" + assunto + "\"");
    }
    for (const [nome, re] of LINKS) {
      if (!re.test(tudo)) faltas.push("falta o link do " + nome);
    }
    if (PEDIDO_DE_TEMPO.test(tudo)) faltas.push("pede tempo ou conversa, e o fechamento certo é pedir direção");
    for (const [nome, re] of PROIBIDO) {
      if (re.test(tudo)) faltas.push("contém " + nome);
    }
    if (!texto.trim()) faltas.push("sem corpo em texto puro");
    if (!html.trim()) faltas.push("sem corpo em HTML");
    if (/google\.com\/url/i.test(limparLinks(tudo))) faltas.push("link embrulhado que a limpeza NÃO desfaz");

    if (faltas.length) {
      comProblema++;
      Logger.log("PROBLEMA em " + para + ": " + faltas.join(" | "));
    }
  }
  Logger.log(rascunhos.length + " rascunhos na caixa, " + comProblema + " com problema.");
  if (!comProblema) Logger.log("Todos no padrão. Pode rodar o prepararRascunhos.");
  return comProblema;
}

function assinatura() {
  // Usa a assinatura padrão da conta (a "n"). Se quiser outra, marque-a como padrão no Gmail antes de rodar.
  const contas = Gmail.Users.Settings.SendAs.list("me").sendAs || [];
  const conta = contas.find(c => c.isPrimary) || contas[0];
  if (!conta || !conta.signature) throw new Error("Nenhuma assinatura padrão encontrada nas configurações do Gmail.");
  return conta.signature;
}

function anexos() {
  const pasta = DriveApp.getFolderById(PASTA_DRIVE_ID);
  return NOMES_ANEXOS.map(nome => {
    const it = pasta.getFilesByName(nome);
    if (!it.hasNext()) throw new Error("Não achei no Drive: " + nome);
    return it.next().getAs("application/pdf");
  });
}

// Passo de teste: manda UM email para você mesmo com a assinatura e os dois anexos. Não toca nos rascunhos.
function enviarTeste() {
  const eu = Session.getActiveUser().getEmail();
  const html = "<p>Teste do envio automático da campanha.</p><p>Se a assinatura abaixo e os dois PDFs anexados estiverem certos, o script está pronto.</p>"
             + "<br><br>-- <br>" + assinatura();
  GmailApp.sendEmail(eu, "TESTE campanha: assinatura e anexos", "Teste do envio automático da campanha.", { htmlBody: html, attachments: anexos(), name: "Vini Cavalcanti" });
  Logger.log("teste enviado para " + eu);
}

/* PREPARA os rascunhos sem enviar NENHUM, ideia do Vini em 06/09 e ela resolve o teto de 100.
 *
 * POR QUE FUNCIONA: o Apps Script tem DUAS cotas diferentes e independentes. Enviar email gasta
 * a cota de envio, que nesta conta é de 100 por janela de 24 horas. Ler e ESCREVER rascunho gasta
 * outra cota, a de leitura e escrita do Gmail, que é de dezenas de milhares por dia e nunca chegou
 * perto do limite nesta campanha. Como o enviarRascunhos() já fazia d.update() e só depois d.send(),
 * basta ficar com a primeira metade: o rascunho sai daqui COMPLETO, com assinatura, os dois PDFs
 * anexados e os links já desembrulhados, e o disparo passa a ser feito à mão pelo Gmail.
 *
 * O QUE MUDA NA PRÁTICA: o envio pela interface do Gmail tem teto próprio e muito maior que o do
 * script, então os 75 rascunhos deixam de esbarrar no limite. O preço é clicar em enviar um por um.
 *
 * RODAR DE NOVO É SEGURO: rascunho que já tem os dois anexos é pulado, senão a assinatura entraria
 * duas vezes no corpo.
 *
 * O QUE ELA NÃO RESOLVE, e continua valendo: disparar tudo de uma vez, de um domínio jovem, é o que
 * arrisca a reputação. Mande em levas, não os 75 de uma sentada.
 */
function prepararRascunhos() {
  const sig = assinatura();
  const files = anexos();
  const rascunhos = GmailApp.getDrafts().filter(d => d.getMessage().getSubject() === ASSUNTO);
  Logger.log(rascunhos.length + " rascunhos da campanha encontrados. Esta função NÃO envia nada.");
  let feitos = 0, pulados = 0;
  for (const d of rascunhos) {
    if (feitos >= MAX_POR_EXECUCAO) {
      Logger.log("PAREI NO LIMITE DA EXECUÇÃO: " + (rascunhos.length - feitos - pulados)
        + " ficaram para a próxima rodada. Não é erro, é o limite de 6 minutos do Apps Script.");
      break;
    }
    const m = d.getMessage();
    const para = m.getTo();
    if (!para) { pulados++; continue; }
    if (m.getAttachments().length >= NOMES_ANEXOS.length) { pulados++; continue; }
    const html = limparLinks(m.getBody()) + "<br><br>-- <br>" + sig;
    const texto = limparLinks(m.getPlainBody());
    d.update(para, ASSUNTO, texto, { htmlBody: html, attachments: files, name: "Vini Cavalcanti" });
    feitos++;
    Logger.log("pronto para enviar à mão: " + para);
  }
  Logger.log(feitos + " rascunhos completados com assinatura e anexos, " + pulados
    + " pulados por já estarem prontos ou sem destinatário. Cota de envio gasta: ZERO.");
  Logger.log("Agora abra o Gmail, confira o primeiro e dispare pela interface, em levas.");
}

function enviarRascunhos() {
  const sig = assinatura();
  const files = anexos();
  const rascunhos = GmailApp.getDrafts().filter(d => d.getMessage().getSubject() === ASSUNTO);
  // Cota diária do Gmail. Em 03/09 uma execução estourou no meio e morreu com
  // "Service invoked too many times for one day: email", deixando o Vini sem saber
  // quantos tinham saído. Perguntar antes é barato e transforma o estouro num aviso.
  const sobra = MailApp.getRemainingDailyQuota();
  Logger.log(rascunhos.length + " rascunhos da campanha encontrados · cota restante hoje: " + sobra);
  if (sobra <= 0) {
    // Sobre QUANDO ela volta: a documentação do Google fala em período de 24 horas sem
    // cravar a hora do corte, e existe relato tanto de virada em horário fixo quanto de
    // janela móvel contada do primeiro envio. Como não dá para afirmar qual é, esta
    // mensagem não promete horário: manda conferir, que custa dois segundos e não erra.
    Logger.log("COTA ZERADA. Nada foi enviado e nenhum rascunho se perdeu. Ela volta "
      + "dentro de 24 horas. Em vez de adivinhar a hora, rode a função cota() antes de "
      + "tentar de novo: ela diz o número exato e não envia nada.");
    return;
  }
  let n = 0;
  for (const d of rascunhos) {
    if (n >= MAX_POR_EXECUCAO) break;
    if (n >= sobra) {
      Logger.log("PAREI NA COTA: " + n + " enviados, " + (rascunhos.length - n)
        + " ficaram para a próxima execução. Não é erro.");
      break;
    }
    const m = d.getMessage();
    const para = m.getTo();
    if (!para) continue;
    if (SIMULAR) { Logger.log("enviaria para " + para); n++; continue; }
    // RASCUNHO JA PREPARADO NAO SE PREPARA DE NOVO, senao a assinatura entra DUAS VEZES no corpo.
    // Isso passou a importar em 06/09, quando o prepararRascunhos() nasceu: dali em diante existe
    // rascunho que ja chega aqui completo, e reaplicar o update duplicaria a assinatura.
    // POR QUE ESTE ENVIO NAO USA d.update() SEGUIDO DE d.send(), e o motivo foi MEDIDO em
    // 07/09 numa carta que ja tinha saido: o d.update() GRAVA o rascunho de novo, e e na
    // gravacao que o compositor do Gmail reembrulha todo link em google.com/url. Ou seja,
    // limpar o texto e logo depois gravar DESFAZ a limpeza, e o d.send() manda a versao
    // reembrulhada. A carta da Cosmico saiu as 01h08 com os tres links embrulhados apesar
    // de o limparLinks ter rodado, e foi assim que o defeito apareceu.
    //
    // A correcao e nao passar mais pela gravacao: monta o corpo limpo e manda direto pelo
    // GmailApp.sendEmail, que compoe a mensagem final sem o embrulho, e so depois apaga o
    // rascunho. Vale tambem para o rascunho que ja vinha preparado, porque ele foi
    // preparado pelo mesmo update e portanto tambem esta embrulhado.
    const jaPreparado = m.getAttachments().length >= NOMES_ANEXOS.length;
    const html = limparLinks(m.getBody()) + (jaPreparado ? "" : "<br><br>-- <br>" + sig);
    const texto = limparLinks(m.getPlainBody());
    if (/google\.com\/url/i.test(html + texto)) {
      Logger.log("NAO ENVIEI para " + para + ": sobrou link embrulhado que a limpeza nao desfez. Confira a mao.");
      continue;
    }
    GmailApp.sendEmail(para, ASSUNTO, texto, {
      htmlBody: html,
      attachments: jaPreparado ? m.getAttachments() : files,
      name: "Vini Cavalcanti"
    });
    d.deleteDraft();
    n++;
    Logger.log("enviado com link limpo para " + para + (jaPreparado ? " (ja vinha preparado)" : ""));
    Utilities.sleep(PAUSA_MS);
  }
  Logger.log(n + " processados nesta execução" + (SIMULAR ? " (simulação)" : ""));
}


/* ============================================================================
 * ENVIA OS RASCUNHOS DE ASSUNTO PRÓPRIO
 *
 * POR QUE ESTA FUNÇÃO EXISTE, medido em 11/09 às 23h20:
 * Sobraram três cartas presas na caixa desde 10/09, e não por esquecimento. O
 * enviarRascunhos() acha os rascunhos por `getSubject() === ASSUNTO`, ou seja
 * pelo assunto EXATO da campanha. Estas três têm assunto próprio DE PROPÓSITO,
 * porque a própria casa manda usar um:
 *
 *   - UFX Studios      "Jobs · Senior Character Artist · ..."  (a página pede "Jobs" no assunto)
 *   - HandyGames       "Application as 2D/3D Game Artist (Mid-level/Senior)"
 *   - Keytoon          "Oferta empleo Modelador"               (o texto do anúncio pede este)
 *
 * O conferirRascunhos() já avisava disto ("ASSUNTO FORA DO PADRÃO, o envio NUNCA
 * vai achar este rascunho"), mas não havia como enviá-las. Ficavam escritas,
 * corretas e invisíveis. Duas delas citam vaga aberta pelo nome.
 *
 * POR QUE A LISTA DE PERMISSÃO, e ela não é burocracia:
 * Filtrar por "assunto diferente do padrão" pegaria QUALQUER rascunho da caixa,
 * inclusive email pessoal do Vini. Uma função de disparo que varre o que não
 * reconhece é um acidente esperando a vez. Então ela só envia para endereço que
 * está escrito aqui embaixo, um a um, e ignora todo o resto sem reclamar.
 *
 * O assunto de cada uma é PRESERVADO: é o assunto que a casa pediu, e trocá-lo
 * pelo padrão da campanha desmontaria a única razão de a carta ser diferente.
 *
 * O resto é igual ao enviarRascunhos(): limpa o link, NÃO regrava o rascunho
 * (regravar reembrulha o link em google.com/url, medido em 07/09 na Cosmico),
 * respeita a cota e apaga o rascunho só depois que o envio saiu.
 * ========================================================================== */

const ASSUNTO_PROPRIO_PERMITIDOS = [
  "vfx_hr@ufxstudios.com",       // UFX Studios, Bruxelas
  "jobs@thqnordicmobile.com",    // HandyGames / THQ Nordic Mobile, Giebelstadt
  "info@keytoon.com",            // Keytoon, Madri
  "careers@lightfoxgames.com"    // Lightfox Games, Vancouver: Senior 3D Artist
];

function enviarAssuntoProprio() {
  const sig = assinatura();
  const files = anexos();
  const permitidos = ASSUNTO_PROPRIO_PERMITIDOS.map(e => e.toLowerCase().trim());

  const rascunhos = GmailApp.getDrafts().filter(function (d) {
    const m = d.getMessage();
    if (m.getSubject() === ASSUNTO) return false;          // essas são do enviarRascunhos()
    const para = (m.getTo() || "").toLowerCase();
    return permitidos.some(e => para.indexOf(e) !== -1);
  });

  const sobra = MailApp.getRemainingDailyQuota();
  Logger.log(rascunhos.length + " rascunhos de assunto próprio encontrados · cota restante hoje: " + sobra);
  if (!rascunhos.length) {
    Logger.log("Nada a enviar. Se você esperava alguma, confira se o destinatário está em "
      + "ASSUNTO_PROPRIO_PERMITIDOS: fora da lista, a função ignora de propósito.");
    return;
  }
  if (sobra <= 0) {
    Logger.log("COTA ZERADA. Nada foi enviado e nenhum rascunho se perdeu. Rode cota() antes de tentar de novo.");
    return;
  }

  let n = 0;
  for (const d of rascunhos) {
    if (n >= MAX_POR_EXECUCAO) break;
    if (n >= sobra) {
      Logger.log("PAREI NA COTA: " + n + " enviados, " + (rascunhos.length - n) + " ficaram para a próxima. Não é erro.");
      break;
    }
    const m = d.getMessage();
    const para = m.getTo();
    const assuntoDela = m.getSubject();          // o assunto que a CASA pediu, preservado
    if (!para || !assuntoDela) continue;
    if (SIMULAR) { Logger.log("enviaria para " + para + " com assunto \"" + assuntoDela + "\""); n++; continue; }

    const jaPreparado = m.getAttachments().length >= NOMES_ANEXOS.length;
    const html = limparLinks(m.getBody()) + (jaPreparado ? "" : "<br><br>-- <br>" + sig);
    const texto = limparLinks(m.getPlainBody());
    if (/google\.com\/url/i.test(html + texto)) {
      Logger.log("NAO ENVIEI para " + para + ": sobrou link embrulhado que a limpeza nao desfez. Confira a mao.");
      continue;
    }
    GmailApp.sendEmail(para, assuntoDela, texto, {
      htmlBody: html,
      attachments: jaPreparado ? m.getAttachments() : files,
      name: "Vini Cavalcanti"
    });
    d.deleteDraft();
    n++;
    Logger.log("enviado com link limpo para " + para + " · assunto \"" + assuntoDela + "\""
      + (jaPreparado ? " (ja vinha preparado)" : ""));
    Utilities.sleep(PAUSA_MS);
  }
  Logger.log(n + " processados nesta execução" + (SIMULAR ? " (simulação)" : ""));
}
