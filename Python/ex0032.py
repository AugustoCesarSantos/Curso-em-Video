#crie um programa que leia um ano qualquer e mostre se ele é um ano bissexto.

print()
ano= int (input('Digite um ano para saber se ele é bissexto: '))
bis= ano %4
bis2= ano%100
bis3 = ano%400
if bis ==0 and bis2>0 :
    print ('O ano {} É um ano Bissexto.' .format(ano))
elif bis>=0 and bis3 ==0:
    print('O ano {} É um ano Bissexto.' .format(ano))
else:
    print('O ano {} NAO É um ano Bissexto.' .format(ano))

print('*'*40)
print('Resolucao Guanabara')
print('*'*40)

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if  ano ==0:
    ano= date.today().year
if ano% 4 == 0 and  ano% 100!=0 or ano%400 ==0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NAO é BISSEXTO.' .format(ano))








