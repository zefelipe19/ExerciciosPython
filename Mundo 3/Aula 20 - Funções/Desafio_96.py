'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
print(f"{' DESAFIO 96 ':=^100}")

def area(l, c):
    s = l * c
    print(f"O calculo de uma area {l}m x {c}m é {s}m²")


def titulo(msg):
    l = len(msg)
    print("-" * l)
    print(msg)
    print("-" * l)

titulo("Calculo de Terreno!")

l = float(input("Digite a largura (m): "))
c = float(input("Agora digite o comprimento (m): "))
area(l, c)
