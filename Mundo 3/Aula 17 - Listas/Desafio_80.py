'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
print(f"{' DESAFIO 80 ':=^100}")

lista = []

for c in range(0, 5):
    n = int(input("Digite um número: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
        posicao += 1

print(lista)
print("="*100)
