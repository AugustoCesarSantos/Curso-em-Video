# Faca um programa que mostra a tabuada  de varios números, um de cada vez, para  cada valor
#digitado pelo usuario. O programa será i n terrompido quando o numero solicitado for negativo.
n=0
while True:
    print('-'*45)
    n= int (input('Quer ver a tabuada de qual valor? '))
    print('-'*45)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break  
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n * c))


