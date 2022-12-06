#Escreva um programa em Python que leia dois números distintos e apresente o quadrado do maior número.

import math 
print('Digite 2 números')
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

if n1>n2:
    quadrado = math.pow(n1,2)
else:
    quadrado = math.pow(n2,2)
print('Quadrado do maior:', quadrado)