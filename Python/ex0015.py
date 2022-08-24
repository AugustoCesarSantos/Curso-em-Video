# eSCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE
# DE DIAS PELOS QUAIS ELE FOI ALUGADO.
# CALCULE O PRECO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

print('======== Exercicio 15 ========')
print(' Rent-a-car')
print(' Para saber o valor da sua fatura por favor insira os dados a seguir.')
dias = int(input('     *Total de DIAS de aluguel: '))
km = float(input('     *Total de KM percorridos: '))
vkm = km*0.15
vdias= dias*60

print(' O valor final da fatura é de R$ {:.2f}. Para um carro alugado {} dias que rodou {}KM. '.format(vkm+vdias, dias, km, ))

