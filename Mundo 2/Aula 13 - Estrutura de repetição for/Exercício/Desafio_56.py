'''Exercício Python 56: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
print("{:=^100}".format(" DESAFIO 56 "))
somaIdade = 0
mediaIdade = 0
idadeHVelho = 0
homemVelho = ""
mulherJovem = 0

for c in range (1, 5):
    print("---- {}ª PESSOA ----".format(c))
    nome = str(input("Nome: ").strip().upper())
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M / F]: ")).strip().upper()
    somaIdade += idade
    if c == 1 and sexo == "M":
        idadeHVelho = idade
        homemVelho = nome
    if sexo == "M" and idadeHVelho < idade:
        idadeHVelho = idade
        homemVelho = nome
    if sexo == "F" and idade < 20:
        mulherJovem += 1

mediaIdade = somaIdade / 4
print("A média de idade do grupo é {:.1f} anos".format(mediaIdade))
print("O homem mais velho se chama {}, e tem {} Anos.".format(homemVelho, idadeHVelho))
print("Existem {} Mulheres com menos de 20 anos.".format(mulherJovem))
print("="*100)
