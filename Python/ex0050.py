# desenolva um programa que leia seis nuemros inteiros e mostre a
# soma apenas daqueles que forem pares.
# Se o valor digitado for impar desconsidere-o.

s=0
for c in range (0,6):
    n=int(input('Digite um valor: '))
    if n%2 ==0:
        s=s+n
print('O somatorio de todos os números pares foi {}, os ímpares foram desconsiderados.'.format(s))
print('FIM')

print('========== RESOLUCAO GUANBARA ==========')
soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite o {} valor: '. format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {}  números PARES e a a soma foi de {}.'.format(cont,soma))
