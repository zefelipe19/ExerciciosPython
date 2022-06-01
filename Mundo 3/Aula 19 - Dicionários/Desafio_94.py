'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
from time import sleep
print(f"{' DESAFIO 94 ':=^100}")

grupo = []
pessoa = {}
totIdade = 0
mulheres = []
maior = []

while True:
    pessoa['nome'] = str(input("Nome: ")).strip().title()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print("Erro!, Por Favor digite apenas 'M' para 'Masculino ou 'F' para 'Feminino'.")
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == "M":
        pessoa['sexo'] = "Masculino"
    if sexo == "F":
        pessoa["sexo"] = "Femino"
    
    pessoa['idade'] = int(input("Idade: "))
    
    grupo.append(pessoa.copy())
    totIdade += pessoa["idade"]
    if sexo == "F":
        mulheres.append(pessoa["nome"][:])
    pessoa.clear()

    menu = str(input("Deseja adcionar mais alguem? [S/N] ")).strip().upper()[0]
    while menu not in "NS":
        print("Erro! Por Favor digite apenas 'S' para 'SIM' e 'N' para 'NÃO'.")
        menu = str(input("Deseja adcionar mais alguem? [S/N] ")).strip().upper()[0]
    if menu == "N":
        print("Certo, FINALIZANDO.....")
        sleep(0.5)
        break
print('-='*30)

mediaIdade = totIdade / len(grupo)

print(f"O número de pessoa(s) cadastrado(s) foi {len(grupo)}.")
print(f"A média de idade foi de {mediaIdade:5.2f} anos")
if mulheres == []:
    print("Não foi cadastrada nenhuma mulher.")
else:
    print(f"As mulheres cadastradas foram: {mulheres}.")

#print(grupo)

for i, v in enumerate(grupo):
    if v["idade"] > mediaIdade:
        maior.append(v["nome"])
print(f"A pessoas com idade maior que {mediaIdade}: {maior}")

print("="*100)
