'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''
import random, time
print(f"{' DESAFIO 88 ':=^100}")
print("-="*20)
print(f"{'Mega Sena':^40}")
print("-="*20)

apostas = []
dados = []

print("-"*40)
num = int(input("Digite quantos jogos você quer gerar: "))
for c in range(0, num):
    cont = 0
    while True:
        n = random.randint(1, 60)
        if n not in dados:
            dados.append(n)
            cont += 1
        if cont == 6:
            break
    dados.sort()
    apostas.append(dados[:])
    dados.clear()

for i, n in enumerate(apostas):
    print(f"{i + 1}º Jogo {n}")
    print("-"*40)
    time.sleep(0.5)

print()
print("="*100)
