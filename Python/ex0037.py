# Escreva um programa que leia um numero inteiro qualquer e peca para o
# usuario escolher qual sera a base de conversao:
# 1 . Para binario
# 2. Para Octal
# 3. Para hexadecimal

import math
from time import sleep

print('\033[1;34m=\033[m'*65)
print('\033[1;30;43m        CALCULADORA DE CONVERSAO BINARIA, OCTAL E HEXADECIMAL    \033[m')
print('\033[1;34m=\033[m'*65)
print()



decimal = int (input('Digite um numero inteiro para converte-lo de Decimal para Binario, Octal ou Hexadecimal: '))
menu = int(input('Menu de selecao:\n'
                 'Pressione 1 para conversao Binária\n'
                 'pressione 2 para conversao Octagonal\n'
                 'Pressione 3 para conversao Hexadecimal\n'))
print()
print('PROCESSANDO ...')
sleep(2)

if menu == 1:
    print('A conversao do número Decimal {} para base Binaria é {}.'. format(decimal,bin(decimal)[2:]))
elif menu == 2:
    print('A conversao do número Decimal {} para base Octagonal é {}.'.format(decimal,oct(decimal)[2:]))
elif menu == 3:
    print('A conversao do número Decimal {} para base Hexadecimal é {}.'.format(decimal,hex(decimal)[2:]))
else:
    print('Opcao Inválida, inicie novamente.')
