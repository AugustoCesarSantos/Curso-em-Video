cores = dict(palmeiras='\033[7;32m,', flamengo='\033[7;31m', gremio='\033[7;34m', amarelo='\033[7;33m', limpa='\033[m')

print ('{}====== Exercicio 04 ======={}'.format(cores['palmeiras'],cores['limpa']))

n= input('{}Por favor, digite algo:{}'.format(cores['amarelo'],cores['limpa']))
print('{}                                                       {}'.format(cores['flamengo'],cores['limpa']))
print('Classe do conteudo digitado:',type (n))
print('Conteudo é letra:',n.isalpha())
print('Conteudo é um nuhmero: ',n.isnumeric())
print('Conteudo é alfanumérico:',n.isalnum())
print('Conteudo é um digito:', n.isdigit())
print('Conteudo esta em letras minusculas:',n.islower())
print('Conteúdo é um decimal:',n.isdecimal())
print('Conteudo é um identificador:',n.isidentifier())
print('O conteudo é numerico: ',n.isnumeric())
print('O conteudo é imprimível: ',n.isprintable())
print('O conteúdo é um espaco: ' ,n.isspace())
print('O conteudo é um titulo: ',n.istitle())
print('O conteudo esta em letras maiusculas: ',n.isupper())