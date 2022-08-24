# crie um programa que leia quanto dinheiro a pessoa tem na carteira e diga quantos dollares uma pessoa
# tem na carteira e quantos dollares ela pode comprar.
#considere US$ 1.00 = R$ 3.27

print (' ========= Exercício 10  ===========')
print (' Exchange money ')
r=float(input('Insira a quantidade de reais que possui em sua carteira: '))
#d=r/3.27
print ('Com este valor, voce conseguirá comprar US$ {:.2f}.'.format(r/3.27))