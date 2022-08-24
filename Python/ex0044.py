# elabore um programa que calcule o valor a ser pago por um profuto considerando
# o seu preco normal e a condicao de pagamento
# A VISTA EM DINHEIRO/ CHEQUE: 10% DE DESCONTO
# A VISTA NO CARTAO: 5% DE DESCONTO
# EM ATE 2X NO CARTAO: PRECO NORMAL
# 3X OU MAIS NO CARTAO: 20% DE JUROS

print('\033[1;34m=\033[m'*65)
print('\033[1;32;41m              CREDIÁRIO CASAS BAHIA               \033[m')
print('\033[1;34m=\033[m'*65)
print()

print('Para saner todas as condicoes disponiveis de CREDIÁRIO insira o valor do produto e a forma de pagamento.')

valor = float(input('Qual é o Valor do produto: R$ '))
pagamento = int(input('FORMAS DE PAGAMENTO \n'
             '1. A VISTA EM DINHEIRO OU CHEQUE \n'
             '2. A VISTA NO CARTAO \n'
             '3. EM ATÉ 2X NO CARTAO \n'
             '4. 3X OU MAIS NO CARTAO \n'
             'Escolha sua forma de pagmento 1, 2, 3 ou 4: '))
if pagamento == 1:
    print('Pagando a Vista em Dinheiro ou Cheque, voce ganha 10% de desconto.\n'
          'O valor final do produto será de R$ {:.2f}.'.format(valor-(valor*10/100)))
elif pagamento == 2:
    print('Pagando a Vista no Cartao, voce ganha 5% de desconto. \n'
          'O valor final do produto será de R$ {:.2f}.'.format(valor-(valor*5/100)))
elif pagamento ==3:
    print('Pagando em até 2x no Cartao, voce nao tem direio a desconto. \n'
          'O valor final do produto será de R$ {:.2f}.'.format(valor))
elif pagamento == 4:
    print('Pagando em até 3x ou mais vezes no Cartao, voce terá um acrescimo de 20% de juros sobre o valor do produto. \n'
          'O valor final do produto será de R$ {:.2f}.'.format(valor+(valor*20/100)))


print(' ============================== RESOLUCAO GUANABARA ==============================')

print ('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preco das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/ cheque
[ 2 ] a vista cartao 
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual é a sua opcao? '))
if opcao ==1:
    total = preco - (preco*10/100)
elif opcao == 2:
    total = preco - (preco*5/100)
elif opcao ==3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int (input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f}.'.format(totparc,parcela))
else:
    total = preco
    print('Opcao de pagamento inválida, tente novamte.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no fianl.'.format (preco, total))
