with open('colC.txt','r',encoding='utf-8') as f:
    input_text = f.read()

print('=======================')

A=input_text.split('\n')
for i in range(len(A)):
    a = A[i]
    if len(a)>0 and a[-1]==',':
        print(i+1, A[i])
