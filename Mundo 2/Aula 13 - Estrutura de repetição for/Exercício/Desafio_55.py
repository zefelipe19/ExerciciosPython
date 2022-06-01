'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''
print("{:=^100}".format(" DESAFIO 55 "))
pesado = 0
leve = 0
for c in range (1, 6):
    peso = float(input("Digite o peso (Kg) da {}º pessoa: ".format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print("O maior peso apresentado foi {} Kg \nE o menor peso apresentado foi {} Kg.".format(pesado, leve))
print("="*100)
