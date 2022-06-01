'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
print("{:=^100}".format(" DESAFIO 59 "))
v1 = int(input("Digite o primeiro valor! => "))
v2 = int(input("Digite o segundo valor! => "))
menu = 0
while menu != 5:
    print("-="*25)
    menu = int(input('''O que você deseja fazer?
    [1] somar
    [2] multiplicar
    [3] saber qual o maior
    [4] novos valores
    [5] sair....
    => '''))
    if menu == 1:
        soma = v1 + v2
        print("{} + {} = {}".format(v1, v2, soma))
    elif menu == 2:
        mult = v1 * v2
        print("{} x {} = {}".format(v1, v2, mult))
    elif menu == 3:
        maior = v1
        if v2 > maior:
            print("O maior valor é {}".format(v2))
        else:
            print("O maior valor é {}".format(v1))
    elif menu == 4:
        v1 = int(input("Digite o novo valor! => "))
        v2 = int(input("Digite o novo segundo valor => "))
    elif menu == 5:
        print("OK")
    elif menu == 69:
        print("Hum..... ")
        sleep(1)
        print("Safado!")
        sleep(1)
    else:
        print("Comando inválido!")
print("Fechando....")
sleep(0.5)
print("FIM!!!")
print("="*100)
