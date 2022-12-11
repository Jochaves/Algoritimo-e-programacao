#Estrutura condicional encadeada 

n1 = float (input ("Digite a nota 1:"))
n2 = float (input ("Digite a nota 2:"))
n3 = float (input ("Digite a nota 3:"))
media = (n1+n2+n3)/3 
print ("Média = %.1f" %media)
if media>=0 and media<3:
    print ("Reprovado")
elif media < 7:
    print ("Exame")
    print ("Você precisa tirar nota %.1f para ser aprovado" %(12-media))
else:
    print ("Aprovado")