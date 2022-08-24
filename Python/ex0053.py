#Crie um programa que leia uma frase qualquer e diga se ela é um polindroma.
# desconsiderando os espacos
#ex. APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma Frase: ')).upper().strip()
separa = frase.split()
junto = ''.join(separa)
inverso = junto[::-1]
print('O inverso da frase {} é {}.'.format(frase,inverso))
if junto == inverso:
    print('A frase é um Palindromo')
else:
    print('A frase nao é um Palindromo')


print('=========== Resolucao Huanbara ===========')

frase = str(input('Digite uma Frase: ')).upper().strip()
separa = frase.split()
junto = ''.join(separa)
inverso = ''
for letra  in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso da frase {} é {}.'.format(junto,inverso))
if junto == inverso:
    print('A frase é um Palindromo')
else:
    print('A frase nao é um Palindromo')
























