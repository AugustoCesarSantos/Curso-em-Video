# Crie um programa que leia varios numeros interios pelo teclado.
# O programa so vai parar quando o usuário digitar o valor 999, que é a condicao de parada
#no final mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando a flag

num = 0
cont = 1
soma=0
a=0
num = int (input('Insira um numero: '))
a=num
while num != 999:
    num = int(input('Digite outro numero: '))
    cont = (cont+1)
    soma  += num
print('exit')
print('O somatório dos numeros digitados foi de {}.'.format (soma-999+a))
print('O total de numeros digitados foi de {}.'.format(cont-1))


print('-'*30)
print('REsolucao guanabara')
print('-'*30)

num = cont = soma = 0
num = int(input(' Digite um numero [999 para parar]: '))
while num != 999:
    soma +=num
    cont += 1
    num = int(input(' Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))
