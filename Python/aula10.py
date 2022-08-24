#Condicoes
tempo = int(input('Qauntos anos tem o seu carro?'))
if  tempo<=3:
    print('carro novo')
else:
    print('Carro velho')
print('====Fim====')

#condicoes simplificadas
tempo = int (input('Quantos anos tem o seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('===FIM===')


#estrutura de condicional simples somente com o if
nome= str (input('Qual e o seu nome? '))
if nome == 'Gustavo':
    print('Que nome feio voce tem!')
print('')

#estrutura de concicional composta quanto contem if e else
nome= str (input('Qual e o seu nome? '))
if nome == 'Gustavo':
    print('Que nome feio voce tem!')
else:
    print('Seu nome é tao nomal!')
print(' Bom dia, {}!'.format(nome))
print('')

#exercicio da media
nota1= float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('Sua media foi de {:.2f}.'.format(media))
if  media >= 6:
    print('Voce obteve uma boa media danado! PARABENS!')
else:
    print('Sua media foi baixa, estude mais filha da puta!')

# condicao simplificada
print('PARABÉNS' if media >=7 else 'Estude mais seu vagabundo filho da puta!' )