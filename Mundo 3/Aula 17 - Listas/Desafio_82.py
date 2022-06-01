'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
print(f"{' DESAFIO 82 ':=^100}")

lista = []
par = []
impar = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    menu = " "
    while menu not in "NS":
        menu = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("OK....")
        break

print(f"A sua lista é essa {lista}.")
print(f"Os números pares são esses: {par}.")
print(f"Os números impares são esses: {impar}.")
print("="*100)
