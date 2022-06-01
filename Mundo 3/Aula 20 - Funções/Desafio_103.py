'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''
print(f"{' DESAFIO 103':=^100}")

def ficha(nome="<Desconhecido>", gols=0):
    n = nome
    print(f"O jogador {n}, fez {gols} no campeonato.")


nome = str(input("Digite o nome do jogador: "))
gols = str(input(f"Quantos gols {nome} fez? "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gols=gols)
else:
    ficha(nome, gols)

print("="*100)
