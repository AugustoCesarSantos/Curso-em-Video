#TESTES DE CORES
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')
print('\033[30mTeste\033[m')

#TESTES DE CORES PALMEIRAS
print('\033[0;30;41mOla Mundo!\033[m')

print('\033[7;30;42mPalmeiras, o maior campeao do Brasil!')
print('\033[7;32;40mPalmeiras, o maior campeao do Brasil!\033[m')
print('\033[1;32;40mPalmeiras, o maior campeao do Brasil!\033[m')
print('\033[1;30;47mPalmeiras, o maior campeao do Brasil!\033[m')
print ('\033[0;33;44mOla Mundo! \033[m')

print('\033[1;31;43mOla Mundo!\033[m')


#COM VARIAVEIS
a=3
b=5
print('Os valores  sao \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))


#SEGUNDO FORMA DE COLOCAR CORES
nome = 'Augusto'
print('Ola, muito prazer em te conhecer, {}{}{}!' .format('\033[4;34m', nome, '\033[m'))

#TERCEIRO FORMA COM UMA LISTA
nome= 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'
         }
print('Ola muito prazer em te conhecer, {}{}{}!!!'.format(cores ['pretoebranco'], nome, cores ['limpa']))