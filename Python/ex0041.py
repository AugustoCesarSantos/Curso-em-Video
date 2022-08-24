# A Confederacao Nacional de Natacao precisa de um programa que leia
# o ano de nascimento de um atleta e mostre a sua categoria, de acorodo com sua idade:
# Ate 9 anos= Mirim
# Ate 14 anos = Infantil
# Ate 19 anos = Junior
#Ate 20 anos = Senior
# Acima = Master

from datetime import date

print('\033[1;34m=\033[m'*65)
print('\033[7;38;44m              CONFEDERACAO NACIONAL DE NATACAO              \033[m')
print('\033[1;34m=\033[m'*65)
print()


atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(' Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))

print()

if  idade <= 9:
    print('A sua idade é {} anos e sua categoria é MIRIM'.format(idade))

elif idade <=14:
    print('A sua idade é de {} anos e sua categoria é INFANTIL'. format(idade))

elif idade <=19:
    print('A sua idade é de {} anos e sua categoria é JUNIOR'. format(idade))

elif idade == 20:
    print('A sua idade é de {} anos e sua categoria é SENIOR.'.format(idade))

elif idade >= 21:
    print('A sua idade é de {} anos e sua categoria é MASTER.'.format(idade))
print ('Boas bracadas!')
