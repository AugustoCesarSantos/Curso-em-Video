# Faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peca a digitacao novamente até ter um valor correto.


sexo= ''
while sexo != 'M' and sexo != 'F': #enquanto o n for diferente de zero continue
    sexo = str(input('Ola para efeito de pesquisas, qual é o seu sexo? (M/F): ').strip().upper())
    if sexo != 'M' and sexo != 'F':
        print('Formato inválido ou resposta errada.')
print('Obrigado.')

print(' ================== REsolucao Guanabara ==================')
sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor invalido., Por favor, informe o seu sexo (M/F): ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

