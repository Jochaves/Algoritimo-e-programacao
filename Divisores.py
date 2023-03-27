#Elabore um programa em Python que leia um número inteiro e positivo, calcule e apresente os divisores deste número, separados por um espaço em branco.
#O valor de entrada dever ser validado, pois o programa somente aceitará números positivos. Caso o valor de entrada esteja fora do intervalo, o programa emitirá a mensagem VALOR INVÁLIDO e solicitará a entrada deste dado até que ela seja válida.
#A saída de dados serão os divisores do número de entrada, apresentados um ao lado do outro, separados por um espaço, conforme caso de teste.


while True:
 num = int(input())
 if num <= 0:
     print("VALOR INVÁLIDO")
 else:
     break

divisores = []
for i in range(1, num+1):
    if num % i == 0:
       divisores.append(i)

print(*divisores)  
