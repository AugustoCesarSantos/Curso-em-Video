# Crie um programa que faca o computador jogar JOKENPOO com voce
# Pedra, papel e tesoura

from random import randint
from time import sleep

print('\033[1;34m=\033[m'*65)
print('\033[7;38;44m     \U0000270A \U0000270C \U0001F44B    JOKENPOO GAME    \U0000270A \U0000270C \U0001F44B      \033[m')
print('\033[1;34m=\033[m'*65)
print()
computador = randint(1, 3)
print('Ola! vamos jogar JOKENPOO? \U0000270A \U0000270C \U0001F44B')
player = int(input('''Escolha a sua opcao: 
    [ 1 ] PEDRA \U0000270A 
    [ 2 ] PAPEL \U0001F44B 
    [ 3 ] TESOURA \U0000270C 
Digite aqui qual foi a sua opcao: '''))
print('Conte até 3...')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!')
if computador == 1 and player == 1:
    print(''' Oh nao! Deu empate!
    Eu escolhi PEDRA \U0000270A e voce também PEDRA \U0000270A. Vamos jogar novamente?''')
elif computador == 1 and player == 2:
    print('''Parabéns! Voce GANHOU! 
    Eu escolhi PEDRA \U0000270A e voce PAPEL \U0001F44B. Vamos jogar novamente?''')
elif computador == 1 and player == 3:
    print('''Haha! Eu GANHEI! 
    Eu escolhi PEDRA \U0000270A e voce TESOURA \U0000270C. Vamos jogar novamente?''')
elif computador == 2 and player == 2:
    print('''Oh nao! Deu empate! 
    Eu escolhi PAPEL \U0001F44B e voce também PAPEL \U0001F44B. Vamos jogar novamente?''')
elif computador == 2 and player == 3:
    print('''Parabéns! Voce GANHOU! 
    Eu escolhi PAPEL \U0001F44B e voce TESOURA \U0000270C. Vamos jogar novamente?''')
elif computador == 2 and player == 1:
    print('''Haha! Eu GANHEI! 
    Eu escolhi PAPEL \U0001F44B e voce PEDRA \U0000270A. Vamos jogar novamente?''')
elif computador == 3 and player == 3:
    print('''Oh nao! Deu empate! 
    Eu escolhi TESOURA \U0000270C e voce também TESOURA \U0000270C. Vamos jogar novamente?''')
elif computador == 3 and player == 1:
    print('''Parabéns! Voce GANHOU! 
    Eu escolhi TESOURA \U0000270C e voce PEDRA \U0000270A. Vamos jogar novamente?''')
elif computador == 3 and player == 2:
    print('''Haha! Eu GANHEI! 
    Eu escolhi TESOURA \U0000270C e voce PAPEL \U0001F44B. Vamos jogar novamente?''')
else:
    print('Opcao invalida, tente novamente.')


print(' ============================== RESOLUCAO GUANABARA ==============================')
from time import sleep
from random import randint
items = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qula é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!')
print('-='*11)
print('Computador jogou {}.'.format(items[computador]))
print('Jogador jogou {}.'.format(items[jogador]))
print('-='*11)
if computador == 0: # pc jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1 : # pc jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # pc jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
