# crie um programa em que um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
print (' ========== Exercicio 19 ==========')
print (' Vamos ajudar o nosso Professor X com as tarefas da sala de aula.')
aluno1 = input( 'Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do secundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
#luckyone= random.choice([aluno1, aluno2,aluno3, aluno4])
print('O aluno sorteado para apagar o quadro foi {}.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))