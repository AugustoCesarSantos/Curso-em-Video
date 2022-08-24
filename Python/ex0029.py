  #Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h. mostre uma menssagem dizendo que ele foi multado.
#a multa vai custar  R$7,00 por cada km acima do limite

import emoji
#(emoji.emojize(use_aliases=True))
print()
print(emoji.emojize(' :warning: ****** :oncoming_automobile: RADAR DE VELOCIDADE :oncoming_automobile: ****** :warning:'))
print(emoji.emojize(':warning:  :construction: Obras na estrada! Reduza sua velocidade para 80KM/H, ou será multado!:construction:  :warning:'))
velocidade = int (input(' Qual a velocidade do Veículo?: '))
print('O veiculo passou pelo radar a {}KM/H.'.format(velocidade))
multa=(velocidade-80)*7
if velocidade >80:
    print('O veículo excedeu o limite de velocidade e está MULTADO!!!')
    print('O valor de sua multa é de R${},00'.format(multa))
else:
    print('Obrigado por cumprir a lei e obedecer a velocidade permitida!')


# nao estou fazendo nada somente para o gajo nao me encher o saco, estou com os fones de ouvido.

print('=-=' *30)
print('========= Resolucao Guanabara ==========')
print('=-=' *30)

velocidade = float (input('Qual é a velovidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    multa =  (velocidade - 80)*7
    print('Voce deve pagar uma multa de R$ {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija  com seguranca!')
