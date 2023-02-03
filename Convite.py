#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar, nesta ordem:

#a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.

#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

#Observe que as quantidades calculadas a serem vendidas devem ser um número inteiro; portanto, o resultado da quantidade de convites deve ser arredondado para cima, usando a função matemática apropriada em Python.



import math

#entrada de dados
custo = float(input("Gasto total do evento: "))
ingresso  = float(input("Valor de cada ingesso: "))

#Processamento
qingressos = math.ceil(custo / ingresso)
lucro = math.ceil((custo + custo *0.23) / ingresso)

#saída 
print(f"A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado: {qingressos}")
print(f"A quantidade de convites que devem ser vendidos para ter o lucro de 23% e : {lucro}")
