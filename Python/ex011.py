# Faca um programa que leia a largura e a altura de uma parede em metros.
# calcule a sua área e a quantidade de tinta necesaria para pintá-la. sabendo que cada litro de tinta pinta uma area de 2mº

print (' =======  Exercicio 11 =======')
print ('Caluladora de tinta')

l=float(input('Insira a largura da parede em metros: '))
a=float(input('Agora, insira a altura da parede: '))
ar=l*a

print('Voce ira precisar de {:.1f} litros de tinta para pintar esta area de {:.2f} metros quadrados.'.format (ar/2,ar))

