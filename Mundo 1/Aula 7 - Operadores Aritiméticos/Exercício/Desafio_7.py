print("=================== DESAFIO 7 ===================")

print("================ Calculadora de media. ================")

nome = input("Qual é o nome do(a) Aluno(a): ")
n1 = float(input("Digite a nota do primeiro semestre: "))
n2 = float(input("digite a nota do segundo semestre: "))
media = (n1 + n2) / 2

print("A media entre as notas {} e {} do aluno {}, é {:.2f}.".format(n1, n2, nome, media))
