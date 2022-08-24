# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
# - O primeiro valor é mario
# - O segundo valor é maior
# - Nao existe valor maior os dois sao iguais

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a>b:
    print('O primeiro numero {} é maior que o segundo {}.'.format(a,b))
elif b > a:
    print('O segundo numero {} é maior que o primeiro {}.'.format(b,a))
else:
    print('Nao existe valor maior, os dois nummeros sao iguais.')