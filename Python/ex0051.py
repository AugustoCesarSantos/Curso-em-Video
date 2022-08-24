# Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa progressao.

print('Para construir uma PA, digite o termo e a razao.')

n=int(input('Digite o primeiro termo: '))
b=int(input('Digite a razao: '))

for c in range (10):
    pa = n * b
    pb = (pa*pa*c)
print('PA= {}'.format(pb))

print(' ============= RESOLUCAO GUANABARA =================')
primeiro = int(input('Primeiro termo: '))
razao= int (input('Razao: '))
decimo= primeiro + (10-1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(' {}'.format(c), end='-> ')
print('Acabou')


















