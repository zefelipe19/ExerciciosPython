'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''
from time import sleep
aula = " DESAFIO 67 "
print(f"{aula:=^100}")
num = cont = 0
print("Tabuada 3.0")
while True:
    num = int(input("Digite o número que deseja ver a sua taboada: "))
    if num < 0:
        print("Você digitou um número negativo....")
        sleep(0.5)
        print("Encerrando programa.....")
        sleep(0.2)
        break
    print("=-"*25)
    while cont < 10:
        cont += 1
        produto = num * cont
        print(f"{num} x {cont:>2} = {produto}")
    cont = 0
print("Fim")
print("="*100)
