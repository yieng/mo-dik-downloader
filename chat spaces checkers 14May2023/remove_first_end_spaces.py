with open('colC.txt','r',encoding='utf-8') as f:
    colC = f.read()

with open('colD.txt','r',encoding='utf-8') as f:
    colD = f.read()

C=colC.split('\n')
D=colD.split('\n')
lenC=len(C)
lenD=len(D)

C0 = ["".join(c.rstrip().lstrip()) for c in C]
D0 = ["".join(d.rstrip().lstrip()) for d in D]

with open('colC.txt','w',encoding='utf-8') as f:
    for i in range(lenC):
        f.write(C0[i]+'\n')

with open('colD.txt','w',encoding='utf-8') as f:
    for i in range(lenD):
        f.write(D0[i]+'\n')
