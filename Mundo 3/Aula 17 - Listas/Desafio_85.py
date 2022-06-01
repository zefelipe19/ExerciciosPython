'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores 
numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
print(f"{' DESAFIO 85 ':=^100}")

lista = [[], []]
num = 0

for c in range(0, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"Os números pares são: {sorted(lista[0])}.")
print(f"Os números impares são: {sorted(lista[1])}.")

print("="*100)
