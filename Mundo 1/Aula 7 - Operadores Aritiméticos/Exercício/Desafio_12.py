print("=================== DESAFIO 12 ===================")

preco = int(input("Qual o valor do produto? "))
desconto = int(input("E qual é o valor do desconto? "))
descontoEmPorcentagem = desconto / 100
precoFinal = preco * descontoEmPorcentagem

print("O preço inicial do produto é de {}R$ e com o desconto o preço final fica {}R$.".format(preco, precoFinal))

print("=" * 50)
