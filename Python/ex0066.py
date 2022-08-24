#Crie um programa que leia v]arios numeros pelo teclado. O programa  so vai parar quando  o usuario
# digitar 999  que é a condicao de parada. No final mostre quantos numeros forma digitados
# e qual foi a soma entre eles (desconsiderando o flag)

acum=n=cont= 0

while True:
    n = int(input('Digite um numero: '))
    if n== 999:
        break
    acum +=1
    cont +=n
print(f'O total de numeros digitados foi de {acum} e a soma dos números  foi de {cont}.')