'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from cabecalho import cabecalho, fim
import moeda
cabecalho("DESAFIO 107")

num = float(input("digite um valor: "))
print(f"A metade de {num} é {moeda.metade(num)}.")
print(f"O dobro de {num} é {moeda.dobro(num)}.")
print(f"{num} aumentando 10% é {moeda.aumenta(num)}.")
print(f"{num} diminuindo 10% é {moeda.diminui(num)}.")

fim("=")
