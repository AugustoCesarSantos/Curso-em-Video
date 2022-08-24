# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Santo".

cidade=input('Diga o nome de uma cidade qulquer:')
nome = (cidade.strip().split())
santo= (nome[0])
santo= (cidade.upper ())
print ('A nome da cisade digitada comeca com Santo:','SANTO'in santo)

print(
    )

#correcao do guanabara
cid=str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')