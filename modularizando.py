def atualizar_preco(valor):
    porcentagem = valor + (valor * 10/100)
    print( '{:.2f}' .format (porcentagem))


def taxa(valor):
    porcentagem = (valor + (valor * 10/100)) * 2.5/100
    print( '{:.2f}' .format (porcentagem))


def main():

    valor = float(input('Entrar o valor do produto: '))

    atualizar_preco(valor)
    taxa(valor)

main()