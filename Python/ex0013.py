# Faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

print (' ====== Exercício 13 ======')
print('aumento salarial 15%')

s=float(input(' Digite o salario do funcionario para lhe dar 15% de aumento: R$ '))
ns=s*(15/100)
print ('O nobvo salario do funcionario será de R$ {:.2f}'.format (s+ns))
print ('O aumento foi de R$ {:.2f}'.format (ns))