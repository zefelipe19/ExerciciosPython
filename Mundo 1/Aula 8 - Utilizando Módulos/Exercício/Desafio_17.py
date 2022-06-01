from math import hypot

print("="*19, "DESAFIO 17" "="*19)
print("calculadora de Hipotenuza.")
cat1 = float(input("Digite o comprimento do cateto oposto: "))
cat2 = float(input("Agora digite o comprimento do cateto adjasente: "))
hip = hypot(cat1, cat2)

print("O valor da hipotenuza de um triângulo retangulo com catetos de {} e {} respectivamente é {:.2f}.".format(cat1, cat2, hip))

print("="*50)
