# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#Para salarios superiores a R$1250,00 calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%

salario = float(input('Para saber quanto será o seu aumento, digite o valor do seu salário atual: R$ '))
if salario > 1250:
    print('O seu aumento foi de 10% (R$ {:.2f}) e seu novo salario sera R${:.2f}'.format((salario*10/100), (salario*10/100) + salario))
elif salario <= 1250:
    print('O seu aumento foi de 15% (R$ {:.2f}) e seu novo salario sera de R${:.2f}'.format((salario*15/100),(salario*15/100) + salario))

print('*'*40)
print('Resolucao Guanabara')
print('*'*40)

salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario* 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))