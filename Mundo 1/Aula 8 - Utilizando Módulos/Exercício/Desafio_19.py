from random import choice

print("="*19, "DESAFIO 19", "="*19)
print("Roleta russa de alunos. kkkkkkk")

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Agora do segundo aluno: ")
a3 = input("Terceiro: ")
a4 = input("Quarto: ")

lista = [a1, a2, a3, a4]

#lista = ["Felipe", "Fernanda", "Ronaldo", "Paula"]

escolhido = choice(lista)

print("O aluno escolhido foi {}.".format(escolhido))

print("="*50)
