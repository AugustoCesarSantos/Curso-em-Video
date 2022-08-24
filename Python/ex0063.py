# Escreva um programa que leia um numero qualuer
# e mostre na tela os n primeiros elementos de uma sequencia fibonacci

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int (input('Qauntos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print('{} -> {}'.format(t1,t2 ),end='')
cont = 3
while cont <=n:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 =t2
    t2=t3
    cont +=1
print('FIM')