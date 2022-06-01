'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha.'''
print(f"{' DESAFIO 87 ':=^100}")

matrizV2 = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
totSoma = somaColuna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matrizV2[linha][coluna] = int(input(f"Digite um número para a posição {linha, coluna}: "))
        if matrizV2[linha][coluna] % 2 == 0:
            totSoma += matrizV2[linha][coluna]

print("-="*25)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matrizV2[linha][coluna]:^5}]", end="")
    print()

print("-="*25)

print(f"A soma de todos os valores pares da matriz é: {totSoma}.")

for linha in range(0, 3):
    somaColuna += matrizV2[linha][2]
print(f"A soma de todos os valores da 3ª coluna é: {somaColuna}.")

for coluna in range(0, 3):
    if coluna == 0:
        maior = matrizV2[1][coluna]
    elif matrizV2[1][coluna] > maior:
        maior = matrizV2[1][coluna]
print(f"O maior valor da segunda linha é: {maior}.")

print("="*100)
