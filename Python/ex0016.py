# crie  um programa que mostre um numero real pelo teclado e mostre na tela a sua porcao inteira
# Ex: digite  um numero: 6.127
# O numero 6.127 tem a parte inteira 6.

# print (' ====== Exercicio 16 ====== ')
#num = float(input(' Digite um numero real com 3 casas decimais depois da virgula: '))
#print ('O numero digitado foi {}.'.format(int(num)))

import math
num = float (input ('Write a number with 3 decimal places after the point: '))
inteiro = math.trunc(num)
print ('A porcao inteira do numero {} é {}.'. format(num,inteiro))

