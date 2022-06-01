'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
print(f"{' DESAFIO 93 ':=^100}")

jogador = {}
gols = []

jogador['Nome'] = str(input("Digite o nome do jogador: ")).title().strip()
num = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range (0,num):
    gols.append(int(input(f"Quantos gols {jogador['Nome']} fez na partida {c + 1}? ")))
jogador['Partidas'] = num
jogador['Gols'] = gols[:]

tot = sum(gols)

jogador['Total de Gols'] = tot

print("-="*30)

print(jogador)

print("-="*30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor de {v}.")

print("-="*30)

for i, v in enumerate(jogador["Gols"]):
    print(f"Na partida {i + 1}ª, {jogador['Nome']} fez {v} gol(s).")
print(f"Fazendo {jogador['Total de Gols']} gol(s) no fim do campeonato.")
print("="*100)
