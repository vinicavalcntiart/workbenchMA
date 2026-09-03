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
    Logger.log("COTA ZERADA. Nada foi enviado e nenhum rascunho se perdeu. A cota do "
      + "Apps Script vira no começo do dia no fuso do Pacífico, que é por volta das 4h "
      + "da manhã em Recife, então amanhã cedo ela já estará cheia. Rode a função cota() "
      + "antes de enviar para ver com quanto você está trabalhando.");
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
    const html = limparLinks(m.getBody()) + "<br><br>-- <br>" + sig;
    const texto = limparLinks(m.getPlainBody());
    if (SIMULAR) { Logger.log("enviaria para " + para); n++; continue; }
    d.update(para, ASSUNTO, texto, { htmlBody: html, attachments: files, name: "Vini Cavalcanti" });
    d.send();
    n++;
    Logger.log("enviado para " + para);
    Utilities.sleep(PAUSA_MS);
  }
  Logger.log(n + " processados nesta execução" + (SIMULAR ? " (simulação)" : ""));
}
