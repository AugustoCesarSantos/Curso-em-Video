# Crie um programa que leia um numero interio e mostre na tela se ele é PAR ou IMPAR.

num= int(input('Digite um numero: '))
par= num%2
if par == 0:
    print('O número {} é um número PAR.'.format(num))
else:
    print('O numero {} é um número IMPAR.'.format(num))

