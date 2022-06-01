'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
print("{:=^100}".format("DESAFIO 52"))
num = int(input("Digite o número que deseja: "))
div = 0
for c in range (1, num + 1):
    if num % c == 0:
        print("\033[31m", end= "")
        div += 1
    else:
        print("\033[m", end= "")
    print("{}".format(c), end=" ")
print("\033[m")
print("O número {}, foi dividido por {} números.".format(num, div))
if div == 2:
    print("Então esse é um número PRIMO!")
else:
    print("Então esse NÃO é um número PRIMO!")
print("="*100)
