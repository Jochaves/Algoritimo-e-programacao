# A função valorPagamento, que você irá escrever, recebe por parâmetro o valor da prestação e o número de dias em atraso, calcula e retorna o valor a ser pago. O cálculo do valor a ser pago é feito da seguinte forma:
#- Para pagamentos sem dias de atraso, cobrar o valor da prestação,
#- Quando houver atraso, cobrar 3% de multa e juros de 0,1% por dia de atraso.

def valorPagamento(valor, dias):
    
if dias==0:
        
 return valor
    
else:
        
 valor+= valor*0.03 + dias*0.001*valor
       
 return valor
