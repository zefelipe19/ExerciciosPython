print("="*19, "DESAFIO 23", "="*19)
print("Separador de casas númericas...")

num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print("A Unidade é {}. \nA Dezena é {}. \nA Centena é {}. \nA 12Unidade de Milhar é {}.".format(u, d, c, um))

print("="*50)
