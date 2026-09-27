import sys,re,html,subprocess
for h in sys.argv[1:]:
    try:
        t=subprocess.run(['curl','-sSL','-m','18','-A','Mozilla/5.0 Chrome/128.0',f'https://{h}/careers'],capture_output=True,timeout=25).stdout.decode('utf-8','ignore')
    except Exception: print('###',h,'FALHA'); continue
    t2=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',t,flags=re.S)
    x=re.sub(r'<[^>]+>',' ',t2); x=html.unescape(x); x=re.sub(r'\s+',' ',x)
    disc=re.findall(r'(?i)(character|creature|sculpt|groom|texture|surfac|look ?dev|modell?er|modell?ing|3d artist|visual dev)',x)
    campos=[]
    for m in re.finditer(r'<(input|textarea|select)([^>]*)>',t):
        a=m.group(2); nm=re.search(r'name=[\'\"]([^\'\"]+)',a); ty=re.search(r'type=[\'\"]([^\'\"]+)',a)
        if nm and not re.match(r'_wpcf7|s$|csrf',nm.group(1)): campos.append(nm.group(1)+':'+(ty.group(1) if ty else 'ta'))
    print('###',h,'| len',len(x),'| disciplina:',sorted(set(d.lower() for d in disc))[:6])
    print('   TXT:',x[:260])
    print('   CAMPOS:',', '.join(campos[:14]))
