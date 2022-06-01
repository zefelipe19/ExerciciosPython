'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
print("{:=^100}".format(" DESAFIO 54 "))
maiores = 0
menores = 0
hoje = date.today().year
for c in range (1, 8):
    data = int(input("Digite a data de nascimento da {}º pessoa: ".format(c)))
    if hoje - data >= 18:
        maiores += 1
    elif hoje - data < 18:
        menores += 1
print("O número de pessoas maiores de idade é {}, e menores é {}.".format(maiores, menores))
print("="*100)
