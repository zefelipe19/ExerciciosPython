'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
print(f"{' DESAFIO 89 ':=^100}")

alunos = []

while True:
    nome = str(input("Digite o nome do Aluno: ")).strip().title()
    nota1 = float(input("Digite a Nota 1 do Aluno: "))
    nota2 = float(input("Digite a Nota 2 do Aluno: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    menu = str(input("Deseja adicionar mais um aluno? [S/N] ")).strip().upper()[0]
    if menu in "N":
        print("Ok....")
        break
print("=-"*10)
print(f"{'No.':<3} {'Nome':<10}{'Média':>4}")
print("-"*17)
for i, a in enumerate(alunos):
    print(f"{i:<3} {a[0]:<10} {a[2]:>4.1f}")
while True:
    menu = int(input("Digite o número do aluno que deseja ver as notas: [999 para encerrar!] "))
    if menu == 999:
        print("OK...")
        break
    if menu <= len(alunos) - 1:
        print(f"As Notas do Aluno: {alunos[menu][0]}, são {alunos[menu][1]}")
print("FIM")
print("="*100)
