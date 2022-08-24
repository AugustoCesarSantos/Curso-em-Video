# Faca um programa que jogue PAR ou IMPAR com o PC. O jogo sera
#interrompido quando o jogador PERDER.
#MOStrando o total de vitorias consectivas que ele conquistou no final do jogo.

from random import randint

jogador=pc= tentativas= jgcondicao = soma = resultado =0
condicao= variante = ''

print('=-' * 40)
print('     VAMOS JOGAR PAR OU ÍMPAR?')
print('=-' * 40)
while True:
    jogador= int(input('Diga um valor: '))
    condicao = str (input('Par ou Impar? [P/I] ')).strip().upper()[0]
    if condicao == 'P':
        jgcondicao=1
    elif condicao == 'I':
        jgcondicao=2
    elif condicao != 'P' and condicao !='I':
        print('Condicao Invalida, digite novamente.')
    pc = randint(0,10)

    soma = jogador+pc
    resultado = (jogador+pc)%2
    if resultado == 0:
        variante = ('Par')
    elif resultado >0:
        variante = ('Impar')

    print('-' * 40)
    print(f'Voce jogou {jogador} e o computador {pc}. O total de {soma} DEU {variante}. ')
    print('-' * 40)

    if jgcondicao ==1 and resultado == 0:
        print('Voce VECEU!')
        print('Vamos jogar novamente...')
        print('=-' * 40)
        tentativas +=1
    elif jgcondicao == 2 and resultado >0 :
        print('Voce VECEU!')
        print('Vamos jogar novamente...')
        print('=-' * 40)
        tentativas +=1
    elif jgcondicao == 1 and resultado >0:
        print('Voce PERDEU!')
        print('=-' * 40)
        print(f'GAME OVER! Voce venceu {tentativas} vezes.')
        break
    elif jgcondicao ==2 and resultado==0:
        print('Voce PERDEU!')
        print('=-' * 40)
        print(f'GAME OVER! Voce venceu {tentativas} vezes.')
        break



################################################################################

print('Solcucao Guanabara')

from random import randint
v=0
while True:
    jogador = int(input('Diga um numero: '))
    computador = randint(0,10)
    total = jogador+computador
    tipo =  ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print(f'Voce Jogou {jogador} e o computador {computador}. Total de {total}.')
    print('Deu PAR.' if total%2==0 else 'Deu Impar.')
    if tipo == 'P':
        if total %2 ==0 :
            print('Voce venceu.')
            v+=1
        else:
            print('Voce Perdeu')
            break
    if tipo == 'I':
        if total %2 ==1 :
            print('Voce venceu.')
            v+=1
        else:
            print('Voce Perdeu')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER. Voce venceu {v} vezes.')