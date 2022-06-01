'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
print("{:=^100}".format(" DESAFIO 74 "))
numeros = (
    randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    )
for n in numeros:
    print(f'{n} ', end= "")
print("\n{}".format("-"*15))
print(f"O maior número é {max(numeros)}.")
print(f"O menor número é {min(numeros)}.")
print("="*100)
