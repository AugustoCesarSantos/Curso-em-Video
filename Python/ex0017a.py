#faca um programa que leia  o comprimento do cateto oposto e do cateto adjacente  de um triangulo retangulo.
# calcule e mostre o comprimento da hipotenusa.
# o quadrado da hipoitesnusa é igual a soma do quadrado dos catetos

from math import hypot
print (' ======== Exerício =========')
print (' Caulo da hipotenusa')
from math import hypot
catopo = float (input (' Digite o comprimento do cateto oposto:'))
catadj = float (input (' Digite o comprimento do cateto adjacente: '))
print (' O comprimento da hipotenusa é {:.2f}.'.format(hypot(catopo,catadj)))



