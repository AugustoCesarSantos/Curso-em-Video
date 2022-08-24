# Crie um programa que leia o ano de nascimento de sete pessoas.
# no final mostre quantas pessoas ainda nao atingiram a mai
# oridade (21) e quantas ja.

from datetime import date

atual= date.today().year
s=0
b=0
for c in range (7):
    nasc = int(input('Ano de nascimento: '))
    idade = atual-nasc
    if idade >= 21:
        s = s+1
    elif idade <21:
        b = b+1
maior=s
menor=b
print('Maior de idade {}'.format(maior))
print('Menor de idade {}'. format(menor))

