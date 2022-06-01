'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
print(f"{' DESAFIO 100 ':=^100}")

def sorteia(lista):
    for c in range(0, 5):
        n = randint(0, 20)
        lista.append(n)
    print(lista)


def somaPar(lista):
    par = 0
    for i in lista:
        if i % 2 ==0:
            par += i
    print(par)

num = []
sorteia(num)
somaPar(num)
print("=" * 100)
