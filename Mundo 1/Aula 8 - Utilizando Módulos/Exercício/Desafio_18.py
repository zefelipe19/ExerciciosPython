from math import sin, cos, tan, radians

print("="*19, "DESAFIO 18", "="*19)

print("Calculadora de Seno, Cosseno e Tangente")
num = float(input("Digite o valor do ângulo que deseja ver o SENO, COSSENO e a TANGENTE: "))
seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))

print("Com o valor de {}. \nTemos o SENO de {:.2f} \nCOSSENO {:.2f} \nTANGENTE {:.2f}.".format(num, seno, cosseno, tangente))

print("="*50)
