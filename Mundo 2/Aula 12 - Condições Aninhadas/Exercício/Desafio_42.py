'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
print("-=-"*19, "DESAFIO 42", "-=-"*19)
print("Testador de triângulos")
l1 = float(input("Digite o comprimento do PRIMEIRO lado: "))
l2 = float(input("Digite o comprimento do SEGUNDO lado: "))
l3 = float(input("Digite o comprimento do TECEIRO lado: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Esse  triângulo pode existir!")
    if l1 == l2 == l3:
        print("E o triângulo será um Triângulo Equilátero!")
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print("E o triângulo será um Triângulo Isósceles!")
    elif l1 != l2 != l3:
        print("E o triângulo será um Triângulo Escaleno!")
else:
    print("Esse triângulo NÃO pode existir!")
print("-=-"*19)
