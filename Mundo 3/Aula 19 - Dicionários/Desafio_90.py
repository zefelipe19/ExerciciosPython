'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
print(f"{' DESAFIO 90 ':=^100}")

aluno = {
    "nome" : str(input("Digite o nome do aluno: ")),
    "media" : float(input("Digite a média: ")),
}

if aluno["media"] >= 7:
    aluno["estado"] = "Aprovado"
elif 5 < aluno["media"] < 7:
    aluno["estado"] = "Recuperação"
else:
    aluno["estado"] = "Reprovado"

print("-="*30)

for k, v in aluno.items():
    print(f" - {k} é igual a {v}.")

print("FIM")
print("="*100)
