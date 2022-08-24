#Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# + Se ele ainca vai se alistar ao serivo militar
# + Se é a hora de alistar
# + Se ja passou do tempo de alistamento
# seu programa também deverá mostrar o tempo qque falta ou que passou do prazo.

from datetime import datetime

print('\033[1;32m=\033[m'*65)
print('\033[7;30;42m       MINISTÉRIO DA DEFESA - SERVICO DE ALISTAMENTO MILITAR     \033[m')
print('\033[1;32m=\033[m'*65)
print()

dia = (input('Insira sua data de nascimento no formato __/__/__ : '))

dob = datetime.strptime(dia,'%d/%m/%Y').date()
hoje = (datetime.today().date())

alistamento = ((hoje-dob).days//365)
print('Voce tem {:.0f} anos de idade.'.format(alistamento))

if alistamento == 18:
    print('De acordo com sua idade {}, está na hora de realizar o Alistamento Militar Obrigatório!'.format(alistamento))
    print('Procure o Servico Militar mais proximo de sua residencia!')
elif alistamento >18:
    print('De acordo com sua idade {} anos, voce passou do tempo hábil para realizar o Alistamento Militar Obrigatório.'.format(alistamento))
    print('Voce ultrapassou o prazo em {:.0f} ano(s).'.format(alistamento-18))
    print('Procure o Servico Militar mais proximo de sua residencia com urgencia para regularizar a sua situacao!')
elif alistamento <18:
    print('De acordo com sua idade {} anos, voce ainda é muito novo para o Alistamento Militar Obrigatorio.'.format(alistamento))
    print('Ainda faltam {:.0f} ano(s) para que voce possa realizar o Alistamento Militar.'.format(18-alistamento))



print(' ============================== RESOLUCAO GUANABARA ==============================')

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(' Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))

if  idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade> 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))










