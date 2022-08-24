# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# no final mostre:
# A media de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos


somaidade = 0
maioridadehomem = 0
nomevelho = ''
media = 0
mulher20 = 0


for p in range (1,5):
    print('----------------------------')
    print('Pessoa {}'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ').strip().upper())
    somaidade +=idade
    if p == 1 and sexo == 'M':          # ou if p ==1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade> maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade<20:
        mulher20 +=1

print()
media = somaidade/4
menina = mulher20
print('A media de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho,maioridadehomem))
print(('A quantidade de mulheres com menos de 20 anos é de {}'.format(menina)))

