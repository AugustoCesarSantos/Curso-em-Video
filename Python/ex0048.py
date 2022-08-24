# Faca um programa que caulcule a soma entre todos os
# numeros ímpares que sao múltiplos de tres e que se
# encontrem no intervalo de 1 ate 500

s = 0
for n in range (1,500+1):
    impar= n%2
    if impar == 1:
        if (n%3)==0:
            print(n)
            s= s+n
print('O somatorio de todos os valores ímpares e \n'
      'multiplos de 3 no intervalo de 1 a 500 é {}.'.format(s))
print('FIM')

print('================Resulcao Guanabara ==================')

soma = 0 #acumulador
cont = 0 # contador
for c in range (1,501,3):
    if c % 3 ==0:
        soma = soma + c # ou soma += c
        cont = cont + c #ou cont += c
print('A Soma de todos os {} valores solicitados é {}.'.format(cont,soma))

