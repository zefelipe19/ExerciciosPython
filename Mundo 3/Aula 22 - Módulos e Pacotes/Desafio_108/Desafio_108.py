'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''
from cabecalho import cabecalho, fim
import moeda
cabecalho("DESAFIO 108")

num = float(input("digite um valor: "))
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.")
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.")
print(f"{moeda.moeda(num)} aumentando 10% é {moeda.moeda(moeda.aumenta(num))}.")
print(f"{moeda.moeda(num)} diminuindo 10% é {moeda.moeda(moeda.diminui(num))}.")

fim("=")
