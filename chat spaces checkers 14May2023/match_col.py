'''
import sys
try:
    look_for = sys.argv[1]
except IndexError:
    look_for = ','
'''

with open('colC.txt','r',encoding='utf-8') as f:
    colC = f.read()

with open('colD.txt','r',encoding='utf-8') as f:
    colD = f.read()

C=colC.split('\n')
D=colD.split('\n')
lenC=len(C)
lenD=len(D)
print('Length of column C =', lenC, '\nLength of column D =', lenD)

print('=================================')
print('Checking for punctuation mismatch')
print('=================================')

'''
591  python3 colCD.py .
  592  python3 colCD.py ,
  593  python3 colCD.py ?
  594  python3 colCD.py \(
  595  python3 colCD.py \)
  596  python3 colCD.py \
'''
for look_for in [',','.','?','(',')']:
    print('===============',look_for,'===============')

    if lenC==lenD:
        for i in range(lenC):
            x = [i, C[i].count(look_for), D[i].count(look_for)]
            if x[1]!=x[2]:
                print(i+1, (x[1],x[2]), (x[1]-x[2], C[i].count('[/]')), C[i])
    else:
        print("Column lengths do not match. Exiting...")

#exit()

print('===================================')
print('Checking for mismatch in space count')
print('===================================')

look_for = ' '

for i in range(lenC):
    x = [i, C[i].count(look_for), D[i].count(look_for)]
    if (x[1]!=x[2]) and ("[/]" not in C[i]) and ("[*]" not in D[i]):
        print(i+1, (x[1],x[2],x[1]-x[2]), C[i])

a = input('\nPress ENTER to show repeating/error elements...')
print('===================================')
print('Checking for errors in repeating/error elements')
print('===================================')

#pain = ['[/]','[*]']

#B=[c.replace('<','#').replace('>','#').split('#')[1] for c in C]
#A=[len(b.split(' ')) for b in B]

E = []

for i in range(lenC):
    x = [i, C[i].count(look_for), D[i].count(look_for)]
    if (x[1]!=x[2]) and (("[/]" in C[i]) or ("[*]" in D[i])):
        E.append((i+1, (x[1],x[2],x[1]-x[2]), (C[i].count('[/]'), D[i].count('[*]')), C[i]))

B=[str(e).replace('<','#').replace('>','#').split('#')[1] for e in E]
A=[len(b.split(' ')) for b in B]
lenE = len(E)
for i in range(lenE):
    if not(A[i]==E[i][1][2]):
        print(A[i],E[i][1][2],A[i]==E[i][1][2],':',E[i])
