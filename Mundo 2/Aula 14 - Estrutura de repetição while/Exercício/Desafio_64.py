'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
print("{:=^100}".format(" DESAFIO 64 "))
print("Testador de Paciencia v1")
num = int(input("Digite o um número, (Digite '999', para parar): "))
valor = 0
cont = 0
while num != 999:
    valor += num
    cont += 1
    num = int(input("Digite outro, (Digite '999', para parar): "))
print("Você digitou {} valores, somando todos ele é {}.".format(cont, valor))
print("="*100)