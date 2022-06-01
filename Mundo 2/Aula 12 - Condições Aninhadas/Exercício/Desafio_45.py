'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep

print("{:=^100}".format(" DESAFIO 45 "))
item = ("PEDRA", "PAPEL", "TESOURA")
pc = randint(0, 2)
print("{:=^100}".format("JOGO PEDRA, PAPEL E TESOURA!"))
print("Hora de escolher...")
player = int(input("[0] PEDRA\n[1] PAPEL\n[2] TESOURA \n=> "))
print("-="*50)

print("PREPARAR!!!!!")
sleep(1)
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(0.5)

print("-="*50)
print("O COMPUTADOR escolheu {}".format(item[pc]))
print("O JOGADOR escolheu {}".format(item[player]))
print("-="*50)
if pc == 0:  # PC escolheu PEDRA
    if player == 0:
        print("DEU EMPATE!")
    elif player == 1:
        print("Jogador VENCEU!")
    elif player == 2:
        print("O Computador VENCEU!")
    else:
        print("Comando Inválido!")
elif pc == 1:  # PC escolheu PAPEL
    if player == 0:
        print("O Computador VENCEU!")
    elif player == 1:
        print("DEU EMPATE!")
    elif player == 2:
        print("O Jogador VENCEU!")
    else:
        print("Jogada Inválida!")
elif pc == 2:  # PC escolheu TESOURA
    if player == 0:
        print("Jogador VENCEU!")
    elif player == 1:
        print("O Computador VENCEU!")
    elif player == 2:
        print("DEU EMPATE!")
    else:
        print("Jogada Inválida!")
print("="*100)
