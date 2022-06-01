'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print("{:=^100}".format(" DESAFIO 68 "))
print("-="*20)
print("Vamos jogar PAR ou ÍMPAR")
print("=-"*20)
v = 0
while True:
    player = int(input("Digite o número que deseja jogar: "))
    pc = randint(0, 10)
    total = player + pc
    menu = " "
    while menu not in "PI":
        menu = str(input("Você escolhe PAr ou IMPAR? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {player}, e o computador jogou {pc}, o Total é {total},", end="")
    if total % 2 == 0:
        print(" é PAR")
    else:
        print(" é IMPAR")
    if menu == "P":
        if total % 2 == 0:
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif menu == "I":
        if total % 2 == 0:
            print("você perdeu!")
            break
        else:
            print("Você ganhou!")
            v += 1
print(f"GAME OVER!!!! Você venceu {v} vezes!")
print("="*100)
