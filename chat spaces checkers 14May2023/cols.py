# input

with open('CD.txt','r',encoding='utf-8') as f:
    cols = f.readlines()

# (actions) + underscores

a = '†'
col0 = []
for i in range(len(cols)):
    c0 = cols[i]
    for y in ['(',')']:
        c0=c0.replace(y,a+y+a)
    c1=c0.split(a)
    for i in range(len(c1)):
        if c1[i-1]=='(' and c1[i+1]==')':
            c1[i] = c1[i].replace(' ','_')
    c2 = ''.join(c1)
    col0.append(c2)
cols = col0

colC = []
colD = []
for x in cols:
    colC.append(x.split('\t')[0]+'\n')
    colD.append(x.split('\t')[1])

# output

with open('colC.txt','w',encoding='utf-8') as f:
    for x in colC:
        f.write(x)

with open('colD.txt','w',encoding='utf-8') as f:
    for x in colD:
        f.write(x)
    f.write('\n')
