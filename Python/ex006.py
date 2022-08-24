from math import s

print (' ======= Exerício 06 ========')

n1= int (input ('Digite um valor: '))
n2 = n1*2
n3 = n1*3
n4 = n1**(1/2)
#print ('O dobro do numero digitado é {}, o seu triplo é {} e a sua Raiz Quadrada é {}'.format (n2,n3,n4))

print ('O dobro de {} é {}. \nO triplo é {}. \nE sua raiz quadrada é {:.2f}.'.format (n1,(n1*2),(n1*3),(n1**(1/2))))#n, pow (n, (1/2)))
