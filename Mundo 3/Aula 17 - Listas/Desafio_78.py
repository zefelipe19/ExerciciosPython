'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
print(f"{' DESAFIO 78 ':=^100}")

num = []
maior = menor = 0

for c in range (0, 5):
    num.append(int(input(f"Digite um número, para a posição {c}: ")))
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
    
print(f"Você digitou os numeros: {num}.")
print(f"O maior número digitado foi: {maior}. Na(s) posição(ões): ", end= " ")

for i, v in enumerate(num):
    if v == maior:
        print(f"{i}...", end= " ")

print()
print(f"O menor número digitado foi: {menor}. Na(s) posição(ões): ", end= "")

for i, v in enumerate(num):
    if v == menor:
        print(f"{i}...", end= " ")

print()
print("="*100)
