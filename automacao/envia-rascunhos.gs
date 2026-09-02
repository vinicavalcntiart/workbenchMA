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
  Logger.log(rascunhos.length + " rascunhos da campanha encontrados");
  let n = 0;
  for (const d of rascunhos) {
    if (n >= MAX_POR_EXECUCAO) break;
    const m = d.getMessage();
    const para = m.getTo();
    if (!para) continue;
    const html = m.getBody() + "<br><br>-- <br>" + sig;
    if (SIMULAR) { Logger.log("enviaria para " + para); n++; continue; }
    d.update(para, ASSUNTO, m.getPlainBody(), { htmlBody: html, attachments: files, name: "Vini Cavalcanti" });
    d.send();
    n++;
    Logger.log("enviado para " + para);
    Utilities.sleep(PAUSA_MS);
  }
  Logger.log(n + " processados nesta execução" + (SIMULAR ? " (simulação)" : ""));
}
