preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto: '))

valor = preco - (preco * desconto/100 )

print('Valor a pagar: ', valor)