'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
print("{:=^100}".format(" DESAFIO 69 "))
homens = maior = menos = 0
while True:
    idade = 0
    menu = sexo = " "
    print("-"*50)
    idade = int(input("Digite a idade de uma pessoa: "))
    sexo = str(input("E o sexo: [M/F] ")).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input("Resposta Inválida! Digite Novamente: [M/F] ")).strip().upper()[0]

    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        menos += 1
    if idade >= 18:
        maior += 1

    print("-"*50)
    menu = str(input("Deseja adicionar mais alguem? [S/N] ")).strip().upper()[0]
    while menu not in "SN":
        menu = str(input("Resposta Inválida! Digite Novamente [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("Ok..")
        print("Programa finalizado!!")
        break
print(f"{maior} pessoas tem mais de 18 anos; \n{menos} melheres com menos de 20 anos; \n{homens} homens cadastrados!")
print("FIM")
print("="*100)
