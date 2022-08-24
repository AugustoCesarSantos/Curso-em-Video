# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar [2] multiplicar [3] maior [4] novos numeros [5] sair do programa
# seu programa deverá realizar a operacao solicitada em cada caso.
from time import sleep

a = 0
b = 0
menu = 0
print('-=-' * 30)
print('Hello! Para utilizar o programa, sao necessarios dois numeros inteiros.')
print('-=-' * 30)
a = int (input('Digite o primeiro numero: '))
b = int (input('Digite o segundo numero: '))
print('-=-' * 30)

while menu != 5:
    menu = int (input('O que voce gostaria de fazer?\n'
        '   [1] Somar\n'
        '   [2] Multiplicar\n'
        '   [3] Maior\n'
        '   [4] Novos números\n'
        '   [5] Sair do programa\n'
      'Digite sua opcao: '))
    if menu == 1:
        soma = a + b
        print('O resultado da soma entre {} + {} é {}.'.format(a,b,soma))
        print('-=-' * 30)
    if menu == 2:
        multi= a*b
        print('O resultado da multiplicacao entre {} x {} é {}.'.format(a,b,multi))
        print('-=-' * 30)
    if menu == 3:
        if a>b :
            print('O maior número entren {} e {} é o número {}.'.format(a,b,a))
            print('-=-' * 30)
        else:
            print('O maior número entren {} e {} é o número {}. '.format(a,b,b))
            print('-=-' * 30)
    if menu ==4:
        print('Reiniciando para insercao de novos números.')
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        print('-=-' * 30)
    if menu >5 or menu==0:
        print ('Valores inválidos, inicie novamente.')
        print('-=-' * 30)

print('Programa ecerrando...')
sleep(2)
print('Fim')