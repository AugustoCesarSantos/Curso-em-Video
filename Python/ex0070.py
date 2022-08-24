# Crie um programa que leia o nome e o preco de varios produtos.
# O programa deverá perguntqar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato

produto = produto2 = continua = ''
total = caro= preco = comparador = maior =menor = 0

print('-'*51)
print('            LOJA SUPER BARATAO TABAJARA         ')
print('-'*51)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    continua = str (input('Deseja continuar a compra? [S/N] ')).strip().upper()[0]
    print('-' * 51)
    #total
    total += preco
    #maior que mil
    if preco > 1000:
        caro +=1
    #menor preco/produto
    comparador = preco
    if preco < comparador:
        menor = preco
        produto2 = produto

    if continua == 'N':
        print('-' * 17,'FIM DO PROGRAMA','-'*17)
        print(f'O total da compra foi R$ {total:.2f}.')
        print(f'Temos {caro} produtos custando mais de R$ 1000.00')
        print(f'O produto mais barato foi {produto2} que custa R$ {menor:.2f}')
        break


#############################################################
print(' ')
print('RESOLUCAO GUANABARA')

total= totmil = menor = cont= 0
barato = ' '
while True:
    produto = str (input('Nome do Produto: '))
    preco = float (input ('Preco: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil +=1
    if cont ==1: # ou if cont  ==1  or preco < menor:
        menor = preco
        barato = produto
    else: # se usar o Ou nao precisa usar esse Else
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if  resp == 'N':
        break
print('-' * 17, 'FIM DO PROGRAMA', '-' * 17)
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
