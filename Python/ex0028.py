# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir
#qual foi o numero escolhido pelo computador
# O programa devera escrever na tela se o usuario venceu ou perdeu.

import random
print('Ola! vamos jogar um jogo de advinhacao?\n'
      'Desafio voce a advinhar o numero que estoou pensando...\n'
      'O numero que pensei esta entre 0 e 5')
num1 = random.randint (0,5)
num2= int(input('Agora insira o numero que voce acha que eu pensei entre 0 e 5: '))
if num2 == num1:
    print('Uau voce é mesmo bom nisso! Acertou parabéns!')
else:
    print('Voce errou! Eu ganhei! PC wins! Eu sou o melhor! Loser L!!!')
print('O meu numero foi: {}.'.format(num1))
print('E o seu numero foi: {}'.format(num2))

print(' ###################### SOLUCAO GUANABARA ####################')

from random import randint
from time import sleep

computador = randint(0,5) # faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? : ')) #Jogador tenta advinhar
print('PROCESSANDO ...')
sleep(3)
if  jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))