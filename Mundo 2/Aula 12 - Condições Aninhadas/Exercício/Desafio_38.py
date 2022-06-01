'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''
cores = {
    "clear" : "\033[m",
    "blue" : "\033[1;30;42m",
    "red" : "\033[1;30;41m"
}
print("-=-"*19, "DESAFIO 38", "-=-"*19)
print("Comparador de números...")
a = float(input("{}Digite o primeiro número: {}".format(cores["blue"], cores["clear"])))
b = float(input("{}Agora digite o segundo número: {}".format(cores["red"], cores["clear"])))
print("-=-"*20)
if a > b:
    print("{}O Primeiro valor, o número {} é o maior!{}".format(cores["blue"], a, cores["clear"]))
elif b > a:
    print("{}O Segundo valor, o número {} é o maior!{}".format(cores["red"], b, cores["clear"]))
elif a == b:
    print("Não existe um número maior, ambos são o mesmo!")
