# Refaca o DESAFIO 035 dos triangulos. acrescentando o recurso de mostrar que tipo de triangulo sera fromado:
# Eaquilatero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('Para saber se a medida de 3 retas podem formar um triangulo, favor insira 3 medidas.')
a = float(input('Insira o primeiro medida/lado do triangulo: '))
b = float(input('Insira o segundo medida/lado do triangulo: '))
c = float(input('Insira o terceiro medida/lado do triangulo: '))
if a < (b+c) and b < (a+c) and c < (a+b):
    print('Sim, essas medidas podem formar um triangulo')
    if a==b==c:
        print('O tipo de triangulo a ser formado será o EQUILÁTERO, onde todos os lados sao iguais.')

    elif a == b or a ==c or b==c:
        print('O tipo de triangulo a ser formado será o ISÓCELES, onde apenas dois lados sao iguais.')

    else:
        print('O tipo de triangulo a ser formado sera o ESCALENO, onde todos os lados sao diferentes.')
else:
    print('Nao, essas medidas nao podem formar um triangulo')
