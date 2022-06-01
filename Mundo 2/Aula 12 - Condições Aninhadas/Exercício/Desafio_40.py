"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""
colores = {
    "clear" : "\033[m",
    "red" : "\033[1;30;41m",
    "yellow" : "\033[1;30;43m",
    "green" : "\033[1;30;42m"
}
print("-=-"*19, "DESAFIO 40", "-=-"*19)
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Agora digite a segunda nota: "))
media = (n1 + n2) / 2
if media < 5.0:
    print("A média foi de {:.1f} , o aluno foi {}REPROVADO!{}".format(media, colores["red"], colores["clear"]))
elif media >= 5.0 and media <= 6.9:
    print("A média foi de {:.1f} , o aluno está de {}RECUPERAÇÂO!{}".format(media, colores["yellow"], colores["clear"]))
elif media >= 7.0:
    print("A média foi de {:.1f} , o aluno está {}APROVADO!{}".format(media, colores["green"], colores["clear"]))
else:
    print("Esta resposta não é valida")

print("-=-"*50)
