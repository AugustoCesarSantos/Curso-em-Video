# Escreva um programa para aprovar um emprestimo bancario para compra de uma casa
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestacao mensal sabendo qie ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

print('\033[1;34m=\033[m'*65)
print('\033[1;30;43m    PRGRAMA DE EMPRÉSTIMO IMOBILIARIO CAIXA ECONOMICA FEDERAL    \033[m')
print('\033[1;34m=\033[m'*65)
print()

valor = float(input('Qual é o valor do imóvel que deseja comprar: R$ '))
salario = float(input('Qual é o valor do seu salário mensal: R$ '))
tempo= int(input('Em quantos anos pretende pagar o valor do emprestimo: '))
prestacao = valor/(tempo*12)
parte = salario *30/100
if prestacao <= parte:
    print('Parabéns o seu Financiamento foi aprovado! ')
    print('Sua prestacao mensal será de R$ {:.2f}.'.format(prestacao))
else:
    print('A prestacao R${:.2f} excede 30% do seu salário R$ {:.2f}. O seu financiamento NAO foi aprovado!'.format(prestacao,parte))
