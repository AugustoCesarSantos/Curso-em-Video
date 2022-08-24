# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou nao continuar.
# No final mostrar:
# A) quantas pessoas tem amis de 18 anos.
# B) Quantos homnes foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

S= N= masculino = feminino = idade2 = menina = idade = 0
sexo = continuar = ''
while True:
    print('-' * 35)
    print('     CADASTRE UMA PESSOA')
    print('-' * 35)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade <=20:
        menina +=1
    print('-'*35)
    if idade > 18:
        idade2 +=1
    continuar= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        S=1
    elif continuar == 'N':
        N=1
        print('')
        print('========== FIM DO PROGRAMA =========')
        print(f'Total de pessoas com mais de 18 anos: {idade2}')
        print(f'Ao todo temos {masculino} homens cadastrados')
        print(f'E temos {menina} mulher(es) com menos de 20 anos.')
        break

#############################################################
print('RESOLUCAO GUANABARA')
tot18 = totM = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        tot18+=1
    if sexo == 'M':
        totM +=1
    if sexo == 'F' and idade <20:
        totM20 +=1
    resp= ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totM} homens cadastrados')
print(f'E temos {totM20} mulher(es) com menos de 20 anos.')