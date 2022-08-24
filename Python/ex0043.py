# Desenvolva uma logica que leia o peso e a altura de uma pessoa.
# calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 : Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 ate 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Morbida

print('\033[1;34m=\033[m'*65)
print('\033[7;38;44m          CALCULADORA DE IMC - ÍNDICE DE MASSA CORPORAL          \033[m')
print('\033[1;34m=\033[m'*65)
print()

print('Para calcular o seu IMC precisamos de alguns dados. Favor insira o seu PESO e ALTURA.')
peso = float(input('PESO (Kg): '))
altura = float(input('ALTURA (metros): '))
imc = peso/ (altura * altura) # ou peso/ (altura **2)
if imc <= 18.5:
    print('O seu IMC é {:.1f}. Voce esta abaixo do PESO! Precisas comer melhor!'.format(imc))
elif imc >=18.5 and imc <25:
    print('O seu IMC é {:.1f}. Parabéns, voce está no peso IDEAL. Continue assim!'.format(imc))
elif imc >=25 and imc <30:
    print('O seu IMC é {:.1f}. O seu estado é de SOBREPESO! Precisa ter atencao a sua dieta!'.format(imc))
elif imc >=30.01 and imc <40:
    print('O seu IMC é {:.1f}. O seu estado é de OBESIDADE!\n '
          'Precisa ter atencao a sua dieta e precisas fazer exercicio regularmente para melhorar o seu peso!\n'
          'Sua vida pode estar em RISCO!'.format(imc))
elif imc >=40:
    print('O seu IMC é {:.1f}. O seu estado é de OBESIDADE MORBIDA!\n'
          'Precisas ter atencao imediata e procurar ajuda medica! \n'
          'A sua saúde está em RISCO!'.format(imc))


