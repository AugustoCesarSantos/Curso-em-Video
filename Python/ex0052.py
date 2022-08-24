# Faca um programa que leia um numero inteiro e
# diga se ele é ou nao um numero primo.
#resolucao Guanabara
tot=0
p = int(input(' Digite um numero inteiro para saber se ele é um numero primo: '))
for c in range (1,p+1):
    if p % c == 0:
        print('\033[1;32m',end= ' ')
        tot  +=1
    else:
        print('\033[31m', end= ' ')
    print(c,end= ' ')
print('\n\033[mO número {} é divisivel por {} números.'.format(p,tot))
if tot == 2:
    print('Portanto o {} É UM NÚMERO PRIMO.'.format(p))
else:
    print('Portanto o {} NAO É UM NÚMERO PRIMO.'.format(p))

