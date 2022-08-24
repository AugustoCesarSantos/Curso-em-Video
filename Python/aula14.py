

for c in range (1,10): # comparacao do for e o while
    print(c)
print('End')

d = 1
while d < 10: # compracao do for e while
    print(d)
    d +=1
print('End2')

for c in range (1,5):# comparacao de contagem for and while, neste cqso o for precisa do valor inicial e final
    n = int(input('digite um valor: '))
print('End3')

n=1
while n!= 0: #enquanto o n for diferente de zero continue
    n = int (input('Digite um valor: '))
print('End4')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str (input('Deseja continuar [S/N]: ').upper())
print('End5')


t=1
par = impar = 0
while t !=0:
    t= int(input('Digite um valor: '))
    if t !=0:
        if t %2 == 0:
            par+=1
        else:
            impar +=1
print('Voce digitou {} numeros pares e {} numeros impares.'.format(par,impar))
print('End6')
