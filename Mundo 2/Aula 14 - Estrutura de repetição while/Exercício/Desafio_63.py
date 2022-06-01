'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''
print("{:=^100}".format(" DESAFIO 63 "))
t1 = 0
t2 = 1
cont = 3
num = int(input("Digite quantas casas da Sequência de Fibonacci, deseja ver: "))
while cont <= num:
    t3 = t1 + t2
    print("{} -> ".format(t3), end= "")
    cont += 1
    t1 = t2
    t2 = t3
print("Fim")
print("="*100)
