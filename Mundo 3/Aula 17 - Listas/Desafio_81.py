'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
print(f"{' DESAFIO 81 ':=^100}")

numeros = []

while True:
    numeros.append(int(input("Digite um número: ")))
    menu = " "
    while menu not in "SN":
        menu = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("ok....")
        break

print(f"Foram digitados {len(numeros)} números.")

numeros.sort(reverse=True)
print(f"A sua lista em ordem decrescente é {numeros}.")

if 5 in numeros:
    print("O número 5 está na lista!")
else:
    print("O número 5 não existe nessa lista!")

print("="*100)
