'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o'''
print("{:=^100}".format("DESAFIO 50"))
soma = 0
cont = 0
for c in range (0, 6):
    n = int(input("=> "))
    if n % 2 ==0:
        soma = soma + n
        cont = cont + 1
print("A soma de todos pares ({}) é os valores é {}".format(cont, soma))
print("="*100)
