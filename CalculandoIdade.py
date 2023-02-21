ida = int(input("Informe a idade do atleta: "))
 
if ida < 5:
    print ("NÃO TEM IDADE PARA SER ATLETA")
elif ida >= 5 and ida  <= 7:
    print ("INFANTIL A")
elif ida >= 8 and ida <= 10:
    print ("INFANTIL B")
elif ida >= 11 and ida <= 13:
    print ("JUVENIL A")
elif ida >= 14 and ida  <= 17:
    print ("JUVENIL B")
else :
    print ("SÊNIOR")