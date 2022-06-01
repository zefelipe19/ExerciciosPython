'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
from time import sleep
print(f"{' DESAFIO 95 ':=^100}")

dado = {}
gols = []
jogadores = []
totalGols = 0

while True:
    dado.clear()
    gols.clear()
    dado['nome'] = str(input("Qual o nome do jogador: ")).strip().title()
    partidas = int(input(f"Quantas partidas {dado['nome']} jogou: "))
    for c in range (0, partidas):
        gols.append(int(input(f"Quantos gols {dado['nome']} fez na {c + 1}ª partida? ")))
    dado['gols'] = gols[:]
    totalGols = sum(gols[:])
    dado['total'] = totalGols
    jogadores.append(dado.copy())
    
    menu = str(input("Continua? [S/N] ")).strip().upper()[0]
    while menu not in "SN":
        print("Erro!")
        menu = str(input("Continua? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("OK...")
        sleep(0.5)
        break
print("-="*20)
print("No. ", end="")
for i in dado.keys():
    print(f"{i:<15}", end="")
print()
print("-"*40)
for k, v in enumerate(jogadores):
    print(f"{k:<3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-"*40)
while True:
    busca = int(input("De que jogador que ver os dados? (999 Para): "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"Erro! O jogador {busca}, não existe!")
    else:
        print(f"  -- DADOS DO JOGADOR {jogadores[busca]['nome']} --")
        for i, v in enumerate(jogadores[busca]['gols']):
            print(f" -- No jogo {i+1} fez {v} gols.")
print(" << FIM >>")
print('='*100)
