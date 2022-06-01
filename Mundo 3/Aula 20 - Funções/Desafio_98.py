'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
print(f"{' DESAFIO 98 ':=^100}")
def titulo(t):
    l = len(t) + 4
    print("-" * l)
    print(f"  {t}")
    print("-" * l)
def contador(i, f, p):
    print(f"Contando de {i} até {f} de {p} em {p}")
    if i > f:
        if p > 0:
            for c in range(i, f - 1, -p):
                print(f"{c}", end=" ", flush=True)
                sleep(0.2)
        elif p == 0:
            for c in range(i, f - 1, -1):
                print(f"{c}", end=" ", flush=True)
                sleep(0.2)
        elif p < 0:
            p = p * -1
            for c in range(i, f - 1, -p):
                print(f"{c}", end=" ", flush=True)
                sleep(0.2)
    else:
        if p == 0:
            for c in range(i, f + 1, 1):
                print(f"{c}", end= " ", flush=True)
                sleep(0.2)
        else:
            for c in range(i, f + 1, p):
                print(f"{c}", end=" ", flush=True)
                sleep(0.2)
    print("FIM!")

titulo("Contagem Progressiva")
contador(1, 10, 1)

titulo("contagem Regressiva")
contador(10, 0, 2)

titulo("Contagem Personalizada")
inicio = int(input("Digite o número de inicio da contagem: "))
fim = int(input("Digite o número do fim da contagem: "))
passo = int(input("E qual é o passo: "))

contador(inicio, fim, passo)

print("=" * 100)
