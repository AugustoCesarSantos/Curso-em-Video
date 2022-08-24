a = input ('Escreva algo:')

print (
    f'''
    O tipo primitivo é {type(a)}
    é numero:  {a.isnumeric()}
    é alfabetico: {a.isalnum()}
    é alfanumérico? {a.isalnum()} 
    é maiuscula? {a.isupper()}
    é minuscula? {a.islower()}
    é capitalizada? {a.istitle()}
    ''')
















