# Melhore o Desafio 061, perguntando para o usuario se ele quer
# mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrat 0 termos.
'''
print('*='*15)
print('        Gerador de PA')
print('*='*15)

primeiro = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razáo da sua PA: '))
termo = primeiro
cont = 1
cont0=1
novoterm=cont0
while novoterm != 0:
    while cont <=10:
        print('{} ->'.format(termo),end='')
        termo +=razao
        cont +=1
    print('')
    print('\nVoce gostaria de ver mais quantos termos dessa PA?')
    novoterm=(int(input('Se sim, digite quantos termos a mais quer ver, se nao digite 0: ')))
    while novoterm <= (''+1) :
        print('{} ->'.format(termo), end='')
    termo += razao

print('Fim')

while cont0 !=0:
    while cont <= novoterm:
        
'''

print('*='*15)
print('        Gerador de PA')
print('*='*15)

primeiro = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razáo da sua PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total+ mais
    while cont <=total:
        print('{} ->'.format(termo),end='')
        termo +=razao
        cont +=1
    print('Pausa')
    mais = int (input('Quantos termos voce quer mostrar mais? '))

