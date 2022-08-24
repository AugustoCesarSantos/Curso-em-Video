n = 0
while n != 999:
    n = int (input('Digite um numero: '))

#com gambiarra
n = s= 0
while n != 999:
    n = int (input('Digite um numero: '))
    s+=1
s-=999 #gambiarra
print('A soma vale {}.'.format(s))

#sem gambiarra e com o BREAk
n=s=0
while True:
    n = int (input('Digite um numero: '))
    if n == 999:
        break
    s +=1
print('A soma  vale {}.'.format(s))
print(f'A soma vale {s}') # nova pforma de print


