'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
print(f"{' DESAFIO 91 ':=^100}")

jogadores = {}

for c in range(0, 4):
    jogadores[f"Jogador {c + 1}"] = randint(1, 6)

for k, v in jogadores.items():
    print(f"O {k} jogou o dado e tirou {v}")
    sleep(0.5)

print("-="*30)
print("Ranking de jogadores")

cont = 1
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f"O {i}, está em {cont}º lugar, tirou {jogadores[i]}.")
    cont += 1
    sleep(0.5)    

print("="*100)
