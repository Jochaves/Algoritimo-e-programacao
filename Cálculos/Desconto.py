#Faça um algoritimo que leia o preço de um produto e mostre o novo preço, com 15% de desconto.


preço= float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 15 / 100)
print('O produto que custavs R${}, na promoçãocom desconto de 15% vai custar R${}'.format(preço, novo))