# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome= str(input('Digite seu nome completo: ')).strip()
silva= nome.upper()
print ('Existe o nome/sobrenome Silva no seu nome?', 'SILVA' in silva)

print(
)

#solucao do guanabara
nome=str (input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('silva'in nome.lower()))
