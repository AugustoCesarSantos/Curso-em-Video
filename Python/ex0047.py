# crie um programa que mostre na tela todod os numeroes pares
# no intervalo entre 1 e 50.

print('No intervalo de 1 a 50 estes sao os números pares:')
for n in range (1,50+1):
    par= n%2
    if par == 0:
        print(n)

# OU

for b in range (0,50+1,2):
    print(b)
print('Fim')


print('================= RESOLUCAO GUANABARA =====================')

for n in range (1,51):
    if n%2==0:
        print(n, end=' ')

# ou pois utiliza menos memoria no pc

for n in range (2, 51, 2):
    print(n, end=' ')
print('Acabou')


