# Faca um algoritimo que leia o preco de um produto e mostre seu novo preco com 5% de desconto.

print (' ======== Exercício 12 ========')
print ('Promocao 5% desconto')
n=float(input('Para adquirir um desconto automático de 5%, por favor digite o valor do produto: R$'))
d=(n*0.05)
#vf=n-d
print ('O valor final do produto com o desconto é R$ {:.2f}'.format(n-d))
print ('O seu desconto foi de: R$ {:.2f}'.format (d))