with open('colD.txt','r',encoding='utf-8') as f:
    input_text = f.read()

print('=======================')

A=input_text.replace('\n',' ').split(' ')
for a in A:
    if "|" not in a and a not in [',','.','?']:
        print(a)
