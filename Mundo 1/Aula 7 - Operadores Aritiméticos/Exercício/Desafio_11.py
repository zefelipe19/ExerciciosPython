print("=================== DESAFIO 11 ===================")

print("Calculadora de litros de tinta.")

altura = float(input("Quantos metros de altura tem essa parede? "))
largura = float(input("E quantos metros de largura tem essa parede? "))
area = largura * altura
litros = area / 2

print("Com as medidas de {}m de Altura e {}m de Largura, a Área dessa parde possuí {}m2.".format(
    altura, largura, area))
print("Então para pinta-la você precisará de {}L de tinta.".format(litros))

print("="*50)
