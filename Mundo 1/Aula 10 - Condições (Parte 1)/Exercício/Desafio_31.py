print("="*19, "DESAFIO 31", "="*19)
print("Calculadora de preço de viagem...")
viagem = float(input("Qual é a distância da viagem? "))
if viagem <= 200.00:
     preco1 = viagem * 0.50
     print("O valor da passagem fica em: R$ {:.2f}.".format(preco1))
else:
    preco2 = viagem * 0.45
    print("A distância dessa viagem exede o valor limite normal... \nPortanto o preço por Km será reduzido.")
    print("Preço da viagem será cobrado R$ 0.45 por Km, sendo o total de R$ {:.2f}.".format(preco2))
print("="*50)
