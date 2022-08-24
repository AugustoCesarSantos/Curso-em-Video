# Crie um programa que leia duas notas de um aluno e calucule sua media.
# Mostrando uma mensagem no final de acordo com a media atingida:
# - Media abaixo de 5.0 : Reprovado
# - Media entre 5.0 e 6.9: Recuperacao
# - Media acima de 7.0 ou superior : Aprovado.

print('\033[1;32m=\033[m'*65)
print('\033[7;30;42m           CALCULO DE MÉDIA FINAL         \033[m')
print('\033[1;32m=\033[m'*65)
print()

print('Para saber o resultado da sua média final insira as suas notas.')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2
print(media)

if media < 5:
    print('\033[1;41mSua Média Final é de {:.1f} e voce está REPROVADO!\033[m'.format(media))

elif media >= 5 and media < 7:
    print('\033[1;43mSua Média Final é de {:.1f} e voce está EM RECUPERACAO!\033[m'.format(media))

elif media >=7:
    print('\033[1;42mSua Média Final é de {:.1f} e voce está APROVADO! Parabéns!\033[m'.format(media))