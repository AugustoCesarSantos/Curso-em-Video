# Faca um programa que leia 3 numeros mostre  qual é o maior e qual é o menor.

num1 = int(input('Insita o primeiro número: '))
num2 = int(input('Insira o segundo numero: '))
num3 = int(input('Insita o terceiro numero: '))
if  num1 > num2 and num1 >num3:
    print('O maior número é {}.'.format(num1))
elif num2 >num1 and num2 > num3:
    print(('O maior numero é {}.'.format(num2)))
elif num3 >num1 and num3 >num2:
    print(('O maior numero é {}.'.format(num3)))

if  num1 < num2 and num1 <num3:
    print('O menor número é {}.'.format(num1))
elif num2 <num1 and num2 < num3:
    print(('O manor numero é {}.'.format(num2)))
elif num3 <num1 and num3 <num2:
    print(('O menor numero é {}.'.format(num3)))

print('*'*40)
print('Resolucao Guanabara')
print('*'*40)

a = int(input('Primeiro valor: '))
b = int(input('Primeiro valor: '))
c = int(input('Primeiro valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = a
if b > a and b > c:
    maior= b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
