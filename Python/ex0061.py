# Refaca o Desafio 051. Lendo o primeiro termo e a razao de uma PA.
# mostrando 10 primeiros termos da progressao usando a estrutura While.

print('*='*15)
print('        Gerador de PA')
print('*='*15)

primeiro = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razáo da sua PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} ->'.format(termo),end='')
    termo +=razao
    cont +=1
print('Fim')

