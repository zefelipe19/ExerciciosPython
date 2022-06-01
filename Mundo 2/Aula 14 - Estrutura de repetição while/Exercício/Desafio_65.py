'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
print("{:=^100}".format(" DESAFIO 66 "))
print("Calculador de médias.")
num = 0
cont = 0
soma = 0
menu = "S"
maior = menor = 0
while menu in "S":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    menu = str(input("Deseja Continuar? [S/N] ")).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print("~"*25)
print("Você Digitou {} valores, a soma de tudo é {} e a média é {}.".format(cont, soma, media))
print("O maior número digitado foi {} e o menor foi {}.".format(maior, menor))
print("="*100)
