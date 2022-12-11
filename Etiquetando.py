preco = float(input('Preço normal da etiqueta:'))
cod = int(input('Código (1 a 4): '))
if cod==1:
    valor = preco*0.90
    print('A vista em dinheiro ou débito, recebe 10%% de desconto: R$ %.2f' %valor)
elif cod==2:
    valor = preco*0.95
    print('A vista em dinheiro ou débito, recebe 5%% de desconto: R$ %.2f' %valor)
elif cod==3:
    valor = preco/2
    print('E 2 vezes, preço normal de etiqueta sem juros. \nValor de parcela: R$ %.2f' %valor)
elif cod==4:
    valor = preco*1.10/3
    print('E 3 vezes, preço normal de etiqueta mais juros de 10%%. \nValor de parcela: R$ %.2f' %valor)
else:
    print('Código inválido')