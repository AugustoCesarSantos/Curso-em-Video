from datetime import date
from time import sleep
aniversariante = str(input('Digite o seu nome completo: ').strip().upper())
print('PROCESSANDO ...')
sleep(3)
if aniversariante == 'THIAGO SCHETTINI MARI' or aniversariante == 'THIAGO MARI':
    print('Ola meu amigo, tudo bem? ')
    print('Parabéns meu amigo {}! Hoje {} é seu aniversário, desejo-te tudo de bom. Forte abraco.'.format(aniversariante, date.today()))
else:
    print('Espere o seu aniversário para ganhar parabéns!')
print('Tenha um dia abencoado!')