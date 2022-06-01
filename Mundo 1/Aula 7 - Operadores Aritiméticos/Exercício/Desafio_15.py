print("=================== DESAFIO 15 ===================")
print("calculadora de Aluguel de Carro")
andado = float(input("Quantos Quilômetros(Km) foram rodados? "))
dias = int(input("E por quantos dias foi usado? "))
pagar = dias * 60 + andado * 0.15

print("O valor total a se pagar por {} dias usados e {} Km rodados é: {:.2f} R$.".format(dias, andado, pagar))

print("="*50)
