frase = 'Curso em Video Python'
# fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Analise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# trasnformacao
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# DIVISAO
print(frase.split())

# juncao
print('-'.join(['Curso', 'em', 'Video', 'Python']))