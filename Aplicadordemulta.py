#Faça um programa em Python para mostrar um alerta de multa quando a velocidade de um carro estiver 
#acima do permitido (50 km/h)

vel = float(input("informe a velocidade: "))
if(vel > 50):
    print("você será multado")
else:
    print("você não será multado")

print("fim.")