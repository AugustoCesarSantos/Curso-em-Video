# faca um programa que leia o peso de cinco pessoas.
# no final, mostre qual foi o maior e o menor peso lidos.


maior = 0
menor = 0

for p in range (1,6):
    peso = float(input('Peso da pessoa {}: '.format(p)))
    if p==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor =peso
print('O maior peso foi de {}kg.'.format(maior))
print('O menor peso foi de {}kg.'.format(menor))

'''
s=0
b=0
c=1
for c in range (5):
    peso = float(input('Pessoa {}.Qual é o seu peso?: '.format(c+1)))
    maior +=peso
    menor = peso
print('O maior peso é {}.'.format(c))
'''