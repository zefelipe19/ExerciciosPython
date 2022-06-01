'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
print(f"{' DESAFIO 84 ':=^100}")

pessoas = []
dados = []
pesado = leve = 0

while True:
    print("-="*35)
    dados.append(str(input("Digite o nome: ")).strip().title())
    dados.append(float(input("Digite o peso: Kg ")))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    menu = " "
    while menu not in "SN":
        menu = str(input("Continua? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("Ok...")
        break

print(f"Foram cadastrados {len(pessoas)} pessoa(s).")
print(f"O maior peso cadastrado foi {pesado}. Sendo de: ", end="")

for i in pessoas:
    if i[1] == pesado:
        print(f"[{i[0]}] ", end="")
print()

print(f"O menor peso cadastrado foi {leve}. Sendo de: ", end="")

for i in pessoas:
    if i[1] == leve:
        print(f"[{i[0]}] ", end="")
print()

print("="*100)
