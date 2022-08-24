import math

print (' ======== Exerício 18 =========')
print (' Cálculo de um Cosseno, Seno e Tangente de um angulo qualquer. ')

x = float (input ('Digite um angulo qualquer: '))
SENO = math.sin((math.radians(x)))
COSSENO = math.cos(math.radians(x))
TANGENTE = math.tan(math.radians(x))
print('O SENO do angulo {:.0} é {:.2f}.'.format(x,SENO))
print('O COSSENO do andgulo {:.0} é {:.2f}.'.format(x,COSSENO))
print('A TANGENTE do angulo {} é {:.2f}.'.format(x,TANGENTE))


#solucao do guanabara