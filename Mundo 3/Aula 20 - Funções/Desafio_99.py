'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
print(f"{' DESAFIO 99 ':=^100}")
def linha():
    print("-"*40)
def maior(*num):
    m = cont = 0
    print(f"Foram passados {len(num)} valor(es).")
    print("Analizando os números: ", end="")
    for c in num:
        if cont == 0:
            m = c
        elif c > m:
            m = c
        cont += 1
        print(f"{c}", end= ' ', flush=True)
        sleep(0.3)
    print()
    print(f"O maior número é {m}")

linha()
maior(0, 5, 9, 6, 7, 2, 9, 0)
linha()
maior(4, 5, 7)
linha()
maior(5)

print("=" * 100)
