''' crie um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posicao ela aparece  a primeira vez
- Em que posicao ela aparece a ultima vez  '''

frase= input('Digite uma frase: ').strip()
frase2= (frase.upper ())
print('A quantidade de vezes que a letra A aparece na frase é: {}'.format (frase2.count ('A')))
print('A posicao em que ela aparece a primeira vez é: {}'.format(frase2.find('A')+1))
print('A posicao em que ela aparece pela ultima vez é: {}'.format(frase2.rfind('A')+1))


#solucao do Guanabara
print(

)

frase = str (input('digite uma frase: ')).strip().upper()
print('A letra A apararece {} vezes na frase.'.format(frase.count ('A')))
print('A primeira letra A foi encontrada na posicao {}.'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}.'.format(frase.rfind('A')+1))


