'''Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
print("{:=^100}".format(" DESAFIO 72 "))
numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num > 0 and num <= 20:
        print(f"Você digitou o número {numeros[num]}.")
    else:
        print("Comando inválido! Tente novamente...")
    menu = " "
    while menu not in "SN":
        menu = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("ok")
        break
print("="*100)
