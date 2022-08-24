''' Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
Ex: Ana Maria de Barros Souza
primeiro = Ana
ultimo = Souza'''

nome= input('Digite seu nome completo: ')
nome2=nome.title()
dividido = nome2.split()
print('Primeiro Nome = {}'.format(dividido[0]))
print('Ultimo Nome = {}'.format(dividido [-1]))

print(
    )
#Resolucao Guanabara
n = str(input('Digite seu nome completo: ')).strip()
nome= n.split()
print('Ola! Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))