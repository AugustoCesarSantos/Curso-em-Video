
# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunta ao usuario qual sera o valor a ser sacado
# (num inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS. Considere que o caixa possui cedulas de R$ 50, 20, 10 e 1.

from time import sleep

print('='*50)
print('                  BANCO BOSTAú')
print('='*50)

cinquenta = valor = cinquenta2 = cinquenta3= vinte = dez = um= total = 0
s = ''

while True:
    valor = int(input('Que valor voce quer sacar? R$ '))
    if valor > 9999:
        print('Limite para saque R$ 9999,00. favor insira um valor menor.')
    if valor <9999:
        # divir valor por casa decimal
        u = valor // 1 % 10
        d = valor // 10 % 10
        c = valor // 100 % 10
        m = valor // 1000 % 10
        #notas de 50 para centena e milhar
        if c>0:
            cinquenta = (c/50)*100
        if m>0:
            cinquenta2 = (m/50)*1000
        cinquenta3 = cinquenta + cinquenta2
        # notas de 20, 10
        if d ==1:
            dez = d
        elif d ==2:
            vinte = 1
        elif d ==3:
            dez = 1
            vinte = 1
        elif d ==4:
            vinte = 2
        elif d ==5:
            vinte =2
            dez =1
        elif d ==6:
            vinte = 3
        elif d ==7:
            vinte =3
            dez =1
        elif d ==8:
            vinte =4
        elif d ==9:
            vinte =4
            dez =1
        # notas de 1
        um = u
        print('========= NOTAS ===========')
        print(f'NOTA DE 1:  {um}')
        print(f'NOTA DE 10: {dez}')
        print(f'NOTA DE 20: {vinte}')
        print(f'NOTA DE 50: {cinquenta3:.0f}')
        print('='*50)
    s = (str(input('Deseja finalizar a Operacao? [S/N]: '))).strip().upper()[0]
    print('=' * 50)
    if s == 'S':
        break

print('Finalizando ...')
sleep(2)
print('Operacao Finalizada.')
print('Retire o seu cartao e nao esqueca do dinheiro.')
print('O BANCO BOSTAú agradece sua visita, tenha um bom dia e volte sempre!')



#############################################################
print(' ')
print('RESOLUCAO GUANABARA')
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 50
totced= 0
while True:
    if total >=ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Toral de {totced} cedeulas de R$ {ced}.')
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total ==0:
            break
print('='*30)
print('Volte sempre ao Banco CEV e tenha um bom dia !')
