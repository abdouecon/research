import re, json, sys, os
SRC='../tables/'
def strip_macros(cell):
    c=cell.strip()
    c=re.sub(r'\\cellcolor\{[^}]*\}','',c)
    # unwrap \gradXxx{...}
    m=re.match(r'^\\grad\w+\{\s*(.*?)\s*\}$',c)
    if m: c=m.group(1)
    return c.strip()
def parse(fname):
    rows=[]
    txt=open(SRC+fname).read()
    # remove comment lines
    lines=[l for l in txt.split('\n') if not l.lstrip().startswith('%')]
    body='\n'.join(lines)
    # rows start with (CODE)& or with Medicare
    for raw in re.split(r'\\\\',body):
        r=raw.strip()
        r=re.sub(r'\\hline|\\toprule|\\bottomrule','',r).strip()
        m=re.match(r'^\((\w+(?:\.\d)?)\)\s*&(.*)$',r,re.S) or re.match(r'^(Medicare Part [AB])\s*&(.*)$',r,re.S)
        if not m: continue
        code=m.group(1); rest=m.group(2)
        cells=[strip_macros(x) for x in rest.split('&')]
        rows.append([code]+[re.sub(r'\s+',' ',x) for x in cells])
    return rows
if __name__=='__main__':
    for f in sys.argv[1:]:
        for r in parse(f): print(r)
