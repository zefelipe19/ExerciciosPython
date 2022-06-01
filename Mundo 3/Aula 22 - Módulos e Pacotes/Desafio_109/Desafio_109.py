'''Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''
from cabecalho import cabecalho, fim
import moeda
cabecalho("DESAFIO 109")

num = float(input("digite um valor: "))
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}.")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}.")
print(f"{moeda.moeda(num)} aumentando 10% é {moeda.aumenta(num, True)}.")
print(f"{moeda.moeda(num)} diminuindo 10% é {moeda.diminui(num, True)}.")

fim("=")
