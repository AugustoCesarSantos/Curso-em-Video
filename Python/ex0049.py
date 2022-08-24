# Refaca o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher
# so que faca utilizando um laco for.


n=int(input('Digite um numero para saber sua tabuada: '))
for tab in range (n,n+1):
    print ('{} x 1 = {}'.format (tab,n*1))
    print ('{} x 2 = {}'.format (tab,n*2))
    print ('{} x 3 = {}'.format (tab,n*3))
    print ('{} x 4 = {}'.format (tab,n*4))
    print ('{} x 5 = {}'. format (tab,n*5))
    print ('{} x 6 = {}'.format (tab,n*6))
    print ('{} x 7 = {}'.format (tab,n*7))
    print ('{} x 8 = {}'.format (tab,n*8))
    print ('{} x 9 = {}'.format (tab,n*9))
    print ('{} x 10= {}'.format (tab,n*10))

print('======== RESOLUCAO GUANABARA ============')
n=int(input('Digite um numero para saber sua tabuada: '))
for c in range (1, 11):
    print ('{} x {} = {}'.format (n,c,n*c))
