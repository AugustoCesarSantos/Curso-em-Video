# Crie um programa que  leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras mnaisc ulas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar espacos)
# Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo:')
print('O nome digitado foi: {}'.format(nome))
print('O nome digitado com todas maiusculas fica: {}'.format(nome.upper()))
print('O nome digitado com todas as letras minusculas: {}'.format(nome.lower()))
print('A quantidade de caracteres do nome digitado é: {}'.format(len(nome)))
nome1= nome.replace(' ','')
print('A quantidade de caracteres do nome digitado sem o espaco entre os nomes é: {}'.format(len(nome1)))
nome2=(nome.split())
print('O seu primeiro nome é {} e tem {} letras.'.format((nome2[0]),len(nome2[0])))

