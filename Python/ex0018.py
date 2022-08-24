#faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
print (' ======== Exerício 18 =========')
print (' Cálculo de um Coseno, Semno e tangente de um angulo qualquer')

x = float (input ('Digite um angulo qualquer: '))
print (' O seno do angulo digitado é: {:.3f}'.format(math.sin(x)))
print (' O seu coseno  é : {:.3f}.'.format(math.cos(x)))
print ('E sua tangente é: {:.3f}'.format (math.tan(x)))

