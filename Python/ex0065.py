# Crie um programa que leia varios numeros inteiros pelo teclado. no fianl da execucao.
# mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
#o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
saida = ''
num = acum= cont = maior = menor =  0

while saida != 'N':
    num = int(input(' Digite um numero: '))
    saida = str(input('     Deseja continuar [S/N]: ')).upper().strip()[0]
    cont +=1
    acum +=num
    if acum ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor :
            menor = num
media = acum/cont
print('Voce digitou {} numeros e a  media dos valores digitados foi {}.'.format(cont,media))
print ('O maior numero é {} e o menor numero é {}.'.format(maior,menor))