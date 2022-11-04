#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar: 
# a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado. 
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.  

 
custo_total = float(input("Gasto total do evento: "))
valor_ingresso  = float(input("Valor de cada ingesso: "))
quantidade_ingressos = int(custo_total // valor_ingresso)
lucro = int((custo_total + custo_total * 0.23) // valor_ingresso)
print("Quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado: {}".format(quantidade_ingressos))
print("quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%: {}".format(lucro))