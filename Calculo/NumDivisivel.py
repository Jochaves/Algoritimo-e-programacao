#O programa deve receber um número inteiro, digitado pelo usuário, e apresentar uma mensagem: 

#- se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: O número é divisível por 3 e 5. 

#- se o número que o usuário digitou não for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: O número não é divisível por 3 e 5. 


numX = int(input("Qual é o número em mente por você?: "))

if (numX % 3) == 0 and (numX % 5) == 0:

   print("O número que você digitou é (",numX,") e sim, ele É divisível por três e cinco ao mesmo tempo.")

else:

   print("O número que você digitou é (",numX,") e não, ele NÃO é divisível por três e cinco ao mesmo tempo.")