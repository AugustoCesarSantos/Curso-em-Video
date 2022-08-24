# o mesmo proifessor do exercisio anterior  queer sortear a ordem de apresentacao de trabalhos dos alunos.
# faca um programa que leia o nome dos quatro alunos e e mostre a ordem sorteada.

import random
print(' ========= Exercicio 20 ==========')
print ('Agora vamos ajudar o professor X a criar uma lista de alunos e escolher uma ordem para apresentacao dos projetos.')
aluno1 = input( 'Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do secundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
#random.shuffle([aluno1, aluno2, aluno3, aluno4])
#print('O aluno sorteado para apagar o quadro foi {}.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
print ('A ordem de apresentacao será {}.'.format(random.sample([aluno1, aluno2, aluno3, aluno4], k=4)))
