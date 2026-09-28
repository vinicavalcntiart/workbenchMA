exec(open('test_2clumps.py').read().split("S = {}")[0])
S = {}
S['A1.0 (so grande)']                 = build([(CL, {'Guide Distance':0.08})])
S['B1.0 (so pequeno)']                = build([(CL, {'Guide Distance':0.02})])
S['A1.0 > B1.0 OFF']                  = build([(CL, {'Guide Distance':0.08}), (CL, {'Guide Distance':0.02,'Seed':7,'Existing Guide Map':False})])
S['A0.5 > B1.0 OFF']                  = build([(CL, {'Guide Distance':0.08,'Factor':0.5}), (CL, {'Guide Distance':0.02,'Seed':7,'Existing Guide Map':False})])
S['A0.5 > B0.7 OFF']                  = build([(CL, {'Guide Distance':0.08,'Factor':0.5}), (CL, {'Guide Distance':0.02,'Seed':7,'Factor':0.7,'Existing Guide Map':False})])
S['B1.0 > A0.5 OFF (pequeno antes)']  = build([(CL, {'Guide Distance':0.02}), (CL, {'Guide Distance':0.08,'Seed':7,'Factor':0.5,'Existing Guide Map':False})])
S['B0.7 > A0.5 OFF']                  = build([(CL, {'Guide Distance':0.02,'Factor':0.7}), (CL, {'Guide Distance':0.08,'Seed':7,'Factor':0.5,'Existing Guide Map':False})])
S['A0.5 > B1.0 ON (padrao)']          = build([(CL, {'Guide Distance':0.08,'Factor':0.5}), (CL, {'Guide Distance':0.02,'Seed':7,'Existing Guide Map':True})])
print(f"{'cenario':36s} {'grupos r=5mm':>13s} {'grupos r=3cm':>13s}")
for k,ng in S.items():
    tips,_ = evalpos(ng)
    print(f"{k:36s} {nclumps(tips,0.005):13d} {nclumps(tips,0.03):13d}")
