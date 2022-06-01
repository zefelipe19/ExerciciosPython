'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print("{:=^100}".format(" DESAFIO 70 "))
print("="*50)
print("{:^50}".format(" BANCO DA MACIOTA "))
print("="*50)
valor = int(input("Digite o valor que deseja sacar: R$ "))
montante = valor
nota = 50
numNotas = 0
while True:
    if montante >= nota:
        montante -= nota
        numNotas += 1
    else:
        if numNotas > 0:
            print(f"Você receberá {numNotas} notas de R$ {nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        numNotas = 0
        if montante == 0:
            break
print("="*100)
