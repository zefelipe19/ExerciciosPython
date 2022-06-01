'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
print("{:=^100}".format(" DESAFIO 57 "))
genero = str(input("Informe seu gênero: [M/F] => ")).strip().upper()[0]
while genero not in "MF":
    genero = str(input("Dados inválidos, Por Favor digite novamente! => ")).strip().upper()[0]
print("Dados registrados com sucesso!!!!")
print("="*100)
