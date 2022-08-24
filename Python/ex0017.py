#faca um programa que leia  o comprimento do cateto oposto e do cateto adjacente  de um triangulo retangulo.
# calcule e mostre o comprimento da hipotenusa.
# o quadrado da hipoitesnusa é igual a soma do quadrado dos catetos


print (' ======== Exerício =========')
print (' Caulo da hipotenusa')
catopo = float (input (' Digite o comprimento do cateto oposto:'))
catadj = float (input (' Digite o comprimento do cateto adjacente: '))
x = (catopo**2)
y= (catadj**2)
hipo=((x+y)**(1/2))
print (' O comprimento da hipotenusa é {:.2f}.'.format(hipo))



