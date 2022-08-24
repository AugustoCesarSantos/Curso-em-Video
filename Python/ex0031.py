# desenvolva um programa que pergunte a distancia de uma viagem em km
#Calcule o preco da passagem, cobrando R$0,50 por km para viagens de até 200km
# e R$0,45 para viagens mais longas.
print()
print(' **** TICKET MACHINE ****')
print()
viagem = float(input('Para saber o preco do bilhete de onibus, insira a quantidade de KM que ira percorrer: '))
if viagem <= 200:
    print('O valor do bilhete é de R${:.2f}. Boa viagem!'.format(viagem *0.50))
else:
    print('O valor do bilhete é de R${:.2f}. Boa viagem!'.format(viagem*0.45))


print( '*' *35)
print('Resulcao Guanabara forma simplicada if else')

distancia = float  (input('Qual e a distancia de sua viagem: '))
print('Voce esta prestes a completar uma viagem de {}km.'.format(distancia))
preco = distancia *0.50 if distancia <=200 else distancia * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(preco))
