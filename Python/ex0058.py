# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 a 10.
# So que agora o jogador vai tentar advinhar ate acertar.
# mostrando no final quantos palpites foram necesarios para vencer.

from random import randint
from time import sleep

jogador = 0
tentativas = 1

computador = randint(0,10) # faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar...')
print('-=-' * 20)

while jogador != computador: #faz um loop ate p jogador acertar
    jogador = int(input('Em que numero eu pensei? : ')) #Jogador tenta advinhar
    print('PROCESSANDO ...')
    sleep(0.5) #contador de tempo
    if jogador >=11: # se o jogador colocar um numero fora do range, faz ele jogar again
        print('Valor incorreto, somente entre 0 e 10, tente novamente!')
        print('')
    if  jogador == computador: # compara o numero se for vencedor
        print('PARABENS! Voce conseguiu me vencer!')
        print('')
    else: # compara situacao onde pc e jog sao dif.
        print('GANHEI! Tente novamente!')
        print('')
        tentativas +=1 # contador de tentativas
print('Eu pensei no número {}.'.format(computador))
print('Voce precisou de {} tentativas para me vencer!'.format(tentativas))
print('Fim')



print(' ========================= Resolucao Guanabara =====================')


from random import randint
computador2 = randint( 0,10)
print('Sou seu computador ... Acabei de pensar em um numero entre 0 e 10.')
print('Será que vc concesegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador2 = int(input('Qual é o seu palpite?: '))
    palpites +=1
    if jogador2 == computador:
        acertou = True
    else:
        if jogador2 < computador2:
            print('Mais... tente mais uma vez.')
        elif jogador2 > computador:
            print('Menos ... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))







