# A função valorPagamento, que você irá escrever, recebe o parâmetro ou valor da prestação e o valor de dias em atraso, calcula e retorna o número ou valor a ser pago. O cálculo do valor a ser pago é feito da seguinte forma:
#- Para pagamentos sem dias de atraso, cobrar o valor da prestação,
#- Quando atraso, cobrar 3% de multa e juros de 0,1% por dia de atraso.

def valorPagamento(valor, dias):
    juros = 0
    if dias == 0:
        return valor
    else:
        juros = 0.1 * dias

        return valor + ((3 * valor)/100) + juros 

total = 0
cont = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    cont += 1

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)