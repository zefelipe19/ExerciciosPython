print("="*19, "DESAFIO 29", "="*19)
print("Analizador de Multa....")
velocidade = int(input("Qual é a velocidade? "))

if velocidade > 80:
    print("ATENÇÃO!!! \nVocê foi multado \nA velocidade maxíma permitida é 80Km/h")
    multa = (velocidade - 80) * 7
    print("O valor da multa a pagar é {:.2f} R$.".format(multa))

print("Está tudo bem...")

print("Fim.....")
print("="*50)
