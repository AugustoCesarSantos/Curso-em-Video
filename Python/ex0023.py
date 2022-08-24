# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separadamente

# ex: digite um numero: 1834
# Unidades: 4
# Dezenas: 3
# Centenas: 8
#milhar: 1
# faca o programa como string e matematicamente

num= input ('Digite um numero qualuer entre 0 a 9999:')
print('Unidades: {}'.format(num[3]))
print('Dezenas:  {}'.format(num[2]))
print('Centenas: {}'.format(num[1]))

print('Milhares: {}'.format(num[0]))

#matematicamente
print()

num = int(input('Insira um numero: '))
u = num// 1%10
d = num// 10 % 10
c = num//100 % 10
m = num// 1000% 10
print(' Analizando o numero: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezana:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))