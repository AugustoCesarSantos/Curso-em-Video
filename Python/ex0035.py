# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

print('Para saber se a medida de 3 retas podem formar um triangulo, favor insira 3 medidas.')
a = float(input('Insira o primeiro medida/lado do triangulo: '))
b = float(input('Insira o segundo medida/lado do triangulo: '))
c = float(input('Insira o terceiro medida/lado do triangulo: '))
if a < (b+c) and b < (a+c) and c < (a+b):
    print('Sim, essas medidas podem formar um triangulo')
else:
    print('Nao, essas medidas nao podem formar um triangulo')
