/* Preenchedor de formulário de candidatura, para rodar NO NAVEGADOR DO VINI.
 *
 * POR QUE ISSO EXISTE. O livro-caixa do Half Breaks já provou qual é a causa raiz
 * dos formulários travados, e ela não é o formulário: é a REDE. O SmartRecruiters
 * escreveu na tela, com o IP no texto, que a recusa vem de "automated (bot) activity
 * on your network", e o reCAPTCHA invisível do Greenhouse e do Eightfold pontua a
 * sessão pelo mesmo motivo. Nenhuma esperteza de preenchimento resolve isso, porque
 * o problema acontece DEPOIS do preenchimento, no último clique.
 *
 * A saída inteligente não é driblar o porteiro, é trocar quem bate na porta. Este
 * arquivo faz o trabalho chato (preencher trinta campos) acontecer dentro do
 * navegador do Vini, no IP dele, com ele presente. Não existe engano nenhum: quem
 * envia é ele, quem revisa é ele, e o script nunca clica em enviar.
 *
 * COMO VIRA BOOKMARKLET. O painel tem um gerador que pega este código, troca o
 * marcador de telefone (arroba arroba TELEFONE arroba arroba, logo abaixo) pelo
 * número dele e devolve um link javascript: para arrastar até a barra de favoritos.
 * O número NÃO está aqui porque este repositório é público; ele só existe dentro do
 * favorito, no computador dele. O marcador aparece UMA vez no arquivo inteiro, de
 * propósito: na primeira versão ele também aparecia neste comentário, e a troca caiu
 * no comentário em vez de cair no código, deixando o favorito sem número.
 *
 * O QUE ELE FAZ, em ordem:
 * 1. varre todo input, textarea e select da página, inclusive dentro de iframe de
 *    mesma origem;
 * 2. monta o "rótulo real" de cada campo juntando label, aria-label, placeholder,
 *    name e id, porque nenhum ATS usa os mesmos dois;
 * 3. casa esse rótulo com a tabela de respostas e escreve o valor com o setter
 *    nativo, disparando input e change, que é o único jeito de React e Vue
 *    registrarem o que foi digitado;
 * 4. em <select> de verdade, escolhe a opção pelo texto;
 * 5. no fim abre um painel com três listas: o que preencheu, o que NÃO conseguiu e
 *    qual é a resposta certa para cada um, e o que ele decidiu não tocar.
 *
 * O QUE ELE NÃO FAZ, de propósito:
 * - não clica em enviar, nunca;
 * - não mexe em anexo (o navegador não deixa, e nem deveria);
 * - não tenta resolver captcha de espécie nenhuma;
 * - não finge combobox: campo que é lista customizada ele aponta no painel para o
 *   Vini escolher, porque clicar às cegas em lista de dois níveis foi exatamente o
 *   bug que escolheu "Andorra" como país do telefone em 04/09.
 */
(function () {
  var TEL = '@@TELEFONE@@';

  var R = [
    { k: 'Nome',            v: 'Vini',        re: /(first|given|fore)[\s_-]*name|primeiro nome|prénom|vorname/i },
    { k: 'Sobrenome',       v: 'Cavalcanti',  re: /(last|family|sur)[\s_-]*name|sobrenome|nom de famille|nachname/i },
    { k: 'Nome completo',   v: 'Vini Cavalcanti', re: /full[\s_-]*name|nome completo/i, attr: /(^|_)(full)?name$/i },
    { k: 'Email',           v: 'contact@vinicavalcanti.art', re: /e-?mail|correo/i },
    { k: 'Telefone',        v: TEL,           re: /phone|telefone|mobile|téléphone|celular|tel$/i },
    { k: 'Cidade',          v: 'Olinda',      re: /^city$|city\b|cidade|ville|localidade/i },
    { k: 'Estado',          v: 'Pernambuco',  re: /state|province|região|estado/i },
    { k: 'País',            v: 'Brazil',      re: /country|país|pays|land$/i },
    { k: 'Cidade e país',   v: 'Olinda, Pernambuco, Brazil', re: /location|where are you based|current location|localiza/i },
    { k: 'LinkedIn',        v: 'https://www.linkedin.com/in/vinicavalcnti/', re: /linked ?in/i },
    { k: 'Portfólio',       v: 'https://www.artstation.com/viniciuscavalcanti', re: /portfolio|artstation|reel|demo ?reel|portfólio/i },
    { k: 'Site pessoal',    v: 'https://vinicavalcanti.com', re: /website|personal site|other work|any other|site pessoal|url$/i },
    { k: 'Empresa atual',   v: 'E-Line Media', re: /current (employer|company)|most recent (employer|company)|empresa atual/i },
    { k: 'Cargo atual',     v: 'Senior 3D Character Artist', re: /current (title|role|position)|job title|cargo/i },
    { k: 'Anos de experiência', v: '10', re: /years of (professional )?experience|anos de experi|how many years/i },
    { k: 'Aviso prévio',    v: 'A standard transition period with my current studio; glad to align dates in the process.', re: /notice period|availability|start date|disponibil/i },
    { k: 'Salário atual',   v: 'Confidential under the NDA of my current contract; happy to discuss ranges during the process.', re: /current (salary|compensation)|salário atual/i },
    { k: 'Pretensão',       v: 'Open to aligning with your band for the role; if the range is posted, I am comfortable at the lower end of it.', re: /salary expectation|expected (salary|compensation)|desired (salary|compensation)|pretens/i },
    { k: 'Por que aqui',    v: 'I am a senior 3D character artist with a credit on The Wingfeather Saga, working in stylized characters with a focus on grooming and look. My portfolio holds more than 45 projects with over 60 characters across many titles, and my personal projects are some of the strongest pieces in it.', re: /cover letter|why do you|tell us about|additional information|anything else|message|comments/i }
  ];

  /* Perguntas de sim ou não, e a resposta que a campanha dá SEMPRE. Nenhuma delas
     é dourada: autorização de trabalho é a pergunta eliminatória e a resposta é a
     verdade, "não tenho e preciso de patrocínio". */
  var SN = [
    { k: 'Autorizado a trabalhar (EUA/Canadá/país da vaga)', a: 'No',  re: /legally authoriz|authorized to work|right to work|eligible to work|work authorization|permis de travail/i },
    { k: 'Precisa de patrocínio de visto',                   a: 'Yes', re: /sponsorship|sponsor|visa support|patrocín/i },
    { k: 'Aceita realocar',                                  a: 'Yes', re: /relocat|willing to move|mudar de país/i },
    { k: 'Aceita presencial ou híbrido',                     a: 'Yes', re: /on-?site|in office|hybrid|commut|presencial/i },
    { k: 'Já trabalhou aqui antes',                          a: 'No',  re: /previously (worked|employed)|former employee|ever worked (for|at)/i },
    { k: 'Tem parente na empresa',                           a: 'No',  re: /relative|family member|friends? (who )?work/i },
    { k: 'Experiência em jogos',                             a: 'Yes', re: /games? industry|experience in games/i },
    { k: 'Idade, etnia, gênero, deficiência, veterano',      a: 'Prefer not to say', re: /gender|ethnic|race|disabilit|veteran|hispanic|latino|sexual orientation|age range|pronoun/i }
  ];

  var feito = [], falta = [], pulado = [], caixas = 0, campos_totais = 0;

  function texto(el) {
    var t = [];
    if (el.id) {
      var l = document.querySelector('label[for="' + CSS.escape(el.id) + '"]');
      if (l) t.push(l.innerText);
    }
    var lp = el.closest('label'); if (lp) t.push(lp.innerText);
    var grp = el.closest('fieldset, [role=group], .field, [class*="field"], [data-automation-id]');
    if (grp) {
      var lg = grp.querySelector('legend, label, .label, [class*="label"]');
      if (lg && !lg.contains(el)) t.push(lg.innerText);
    }
    ['aria-label', 'placeholder', 'name', 'id', 'data-automation-id'].forEach(function (a) {
      var v = el.getAttribute(a); if (v) t.push(v.replace(/[_\-]+/g, ' '));
    });
    return t.join(' | ').replace(/\s+/g, ' ').slice(0, 300);
  }

  /* Casamento exato por atributo. Existe porque o rótulo composto ("Full name |
     name | input") nunca casa com uma âncora ^...$, e foi assim que o Lever, cujo
     campo se chama simplesmente "name", ficou sem o nome preenchido no primeiro
     teste. Quando a regra traz .attr, ela vale se name OU id baterem exatamente. */
  function casaAttr(el, rule) {
    if (!rule.attr) return false;
    return rule.attr.test(el.getAttribute('name') || '') || rule.attr.test(el.id || '');
  }
  function casa(el, rot, rule) {
    return casaAttr(el, rule) || rule.re.test(rot);
  }

  /* React e Vue ignoram el.value = x. O caminho que funciona é o setter nativo do
     prototype, seguido de input e change. Isso não é truque de bot: é o que o
     próprio navegador faz quando alguém digita. */
  function escreve(el, val) {
    var proto = el instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
    var set = Object.getOwnPropertyDescriptor(proto, 'value');
    if (set && set.set) set.set.call(el, val); else el.value = val;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    el.dispatchEvent(new Event('blur', { bubbles: true }));
  }

  function marca(el, cor) {
    el.style.outline = '2px solid ' + cor;
    el.style.outlineOffset = '1px';
  }

  function selecionaOpcao(sel, alvo) {
    var alvos = alvo === 'Prefer not to say'
      ? [/prefer not/i, /decline/i, /do not wish/i, /não desejo/i]
      : [new RegExp('^\\s*' + alvo + '\\b', 'i')];
    for (var i = 0; i < sel.options.length; i++) {
      var txt = sel.options[i].text;
      for (var j = 0; j < alvos.length; j++) {
        if (alvos[j].test(txt)) {
          sel.selectedIndex = i;
          sel.dispatchEvent(new Event('input', { bubbles: true }));
          sel.dispatchEvent(new Event('change', { bubbles: true }));
          return txt.trim();
        }
      }
    }
    return null;
  }

  function trataRadio(nome, rot, resp, campos) {
    var alvo = resp === 'Prefer not to say' ? /prefer not|decline|do not wish/i : new RegExp('^\\s*' + resp + '\\b', 'i');
    for (var i = 0; i < campos.length; i++) {
      var r = campos[i];
      if (r.type !== 'radio' || r.name !== nome) continue;
      var lab = texto(r);
      if (alvo.test(lab)) {
        r.click();
        return lab.split('|')[0].trim();
      }
    }
    return null;
  }

  function docs() {
    var lista = [document];
    document.querySelectorAll('iframe').forEach(function (f) {
      try { if (f.contentDocument) lista.push(f.contentDocument); } catch (e) { /* outra origem, deixa quieto */ }
    });
    return lista;
  }

  docs().forEach(function (doc) {
    var campos = [].slice.call(doc.querySelectorAll('input, textarea, select'));
    campos_totais += campos.length;
    var radiosFeitos = {};

    campos.forEach(function (el) {
      if (el.type === 'file' || el.type === 'hidden' || el.type === 'submit' || el.type === 'button') return;
      /* Caixa de marcar fica INTEIRA com ele. Duas razões: as de "como soube da
         vaga" são muitas e a escolha é dele, e as de consentimento e termos ninguém
         marca no lugar de outra pessoa. No primeiro teste elas ainda entupiram o
         painel aparecendo como "já preenchido", porque o value de um checkbox é o
         valor da opção e não o que o usuário marcou. */
      if (el.type === 'checkbox') { caixas++; return; }
      if (el.closest('#vc-painel')) return;
      if (el.disabled || el.readOnly) return;
      if (el.offsetParent === null && el.type !== 'radio') return;

      var rot = texto(el);
      if (!rot) return;

      /* rádio: resolve o grupo inteiro de uma vez */
      if (el.type === 'radio') {
        if (radiosFeitos[el.name]) return;
        var grupoRot = rot + ' ' + (el.closest('fieldset, [role=radiogroup], .field') || {}).innerText;
        for (var s = 0; s < SN.length; s++) {
          if (SN[s].re.test(grupoRot)) {
            radiosFeitos[el.name] = 1;
            var esc = trataRadio(el.name, grupoRot, SN[s].a, campos);
            if (esc) { feito.push([SN[s].k, esc]); marca(el, '#2e7d32'); }
            else falta.push([SN[s].k, 'responder ' + SN[s].a]);
            return;
          }
        }
        return;
      }

      if (el.tagName === 'SELECT') {
        if (el.selectedIndex > 0 && el.value) { pulado.push([rot.split('|')[0].trim(), 'já preenchido']); return; }
        for (var s2 = 0; s2 < SN.length; s2++) {
          if (SN[s2].re.test(rot)) {
            var t = selecionaOpcao(el, SN[s2].a);
            if (t) { feito.push([SN[s2].k, t]); marca(el, '#2e7d32'); }
            else { falta.push([SN[s2].k, 'escolher ' + SN[s2].a]); marca(el, '#c62828'); }
            return;
          }
        }
        for (var r2 = 0; r2 < R.length; r2++) {
          if (casa(el, rot, R[r2])) {
            var t2 = selecionaOpcao(el, R[r2].v);
            if (t2) { feito.push([R[r2].k, t2]); marca(el, '#2e7d32'); }
            else { falta.push([R[r2].k, R[r2].v]); marca(el, '#c62828'); }
            return;
          }
        }
        return;
      }

      if (el.value && el.value.trim()) { pulado.push([rot.split('|')[0].trim(), 'já preenchido']); return; }

      for (var s3 = 0; s3 < SN.length; s3++) {
        if (SN[s3].re.test(rot)) { escreve(el, SN[s3].a); feito.push([SN[s3].k, SN[s3].a]); marca(el, '#2e7d32'); return; }
      }
      for (var r3 = 0; r3 < R.length; r3++) {
        if (casa(el, rot, R[r3])) {
          if (R[r3].k === 'Telefone' && (!TEL || TEL.charAt(0) === '@')) {
            falta.push(['Telefone', 'o favorito foi gerado sem número; refaça no painel']);
            marca(el, '#c62828'); return;
          }
          escreve(el, R[r3].v);
          feito.push([R[r3].k, R[r3].v.length > 70 ? R[r3].v.slice(0, 70) + '...' : R[r3].v]);
          marca(el, '#2e7d32');
          return;
        }
      }
    });

    /* combobox customizado (Workday, Eightfold, react-select): não se clica às cegas.
       Aponta e deixa a escolha com quem está olhando a tela. */
    doc.querySelectorAll('[role=combobox], [class*="select__control"], button[aria-haspopup="listbox"]').forEach(function (c) {
      if (c.offsetParent === null) return;
      var rot = (c.closest('[data-automation-id], .field, [class*="field"]') || c).innerText.replace(/\s+/g, ' ').slice(0, 90);
      if (!rot) return;
      var achou = null;
      SN.concat(R.map(function (x) { return { k: x.k, a: x.v, re: x.re }; })).forEach(function (rule) {
        if (!achou && rule.re.test(rot)) achou = rule;
      });
      if (achou) { falta.push([rot, 'lista: escolher ' + (achou.a.length > 50 ? achou.a.slice(0, 50) + '...' : achou.a)]); marca(c, '#ef6c00'); }
    });
  });

  /* O Greenhouse (e outros) desenham o mesmo formulário duas vezes, uma para tela
     larga e outra para celular, e o painel saía com cada linha repetida. Preencher
     as duas cópias está certo; relatar as duas, não. */
  function unico(lista) {
    var visto = {}, saida = [];
    lista.forEach(function (p) {
      var ch = p[0] + '\u0000' + p[1];
      if (!visto[ch]) { visto[ch] = 1; saida.push(p); }
    });
    return saida;
  }
  feito = unico(feito); falta = unico(falta); pulado = unico(pulado);

  var old = document.getElementById('vc-painel'); if (old) old.remove();
  function bloco(titulo, itens, cor) {
    if (!itens.length) return '';
    return '<div style="margin:10px 0"><b style="color:' + cor + '">' + titulo + ' (' + itens.length + ')</b><ul style="margin:4px 0 0 16px;padding:0">' +
      itens.map(function (p) { return '<li style="margin:2px 0"><b>' + p[0] + ':</b> ' + String(p[1]).replace(/</g, '&lt;') + '</li>'; }).join('') + '</ul></div>';
  }
  var p = document.createElement('div');
  p.id = 'vc-painel';
  p.style.cssText = 'position:fixed;top:12px;right:12px;z-index:2147483647;width:390px;max-height:82vh;overflow:auto;background:#fff;color:#111;border:1px solid #999;border-radius:10px;box-shadow:0 8px 30px rgba(0,0,0,.35);padding:14px;font:13px/1.45 system-ui,sans-serif';
  p.innerHTML =
    '<div style="display:flex;justify-content:space-between;align-items:center"><b>Preenchido. Revise e envie você.</b>' +
    '<button id="vc-x" style="border:0;background:#eee;border-radius:6px;padding:3px 9px;cursor:pointer">fechar</button></div>' +
    '<div style="margin-top:6px;color:#555">O script não clica em enviar e não anexa arquivo. Anexe o CV e a carta à mão.</div>' +
    (feito.length === 0 && falta.length === 0
      ? '<div style="margin:10px 0;padding:9px;background:#fff3cd;border-radius:7px;color:#7a5c00"><b>Não achei formulário nesta página.</b> Foram vistos ' + campos_totais + ' campos. Em muitos ATS o formulário só existe depois de clicar em <b>Apply</b>, ou ele abre em outra aba. Clique em Apply, espere carregar e acione o favorito de novo.</div>'
      : '') +
    bloco('Preenchido', feito, '#2e7d32') +
    bloco('Falta você fazer', falta, '#c62828') +
    bloco('Não toquei, já tinha valor', pulado, '#777') +
    (caixas ? '<div style="margin:8px 0;color:#777">' + caixas + ' caixas de marcar deixadas para você, incluindo consentimento, termos e "como ficou sabendo da vaga".</div>' : '');
  document.body.appendChild(p);
  document.getElementById('vc-x').onclick = function () { p.remove(); };
})();
