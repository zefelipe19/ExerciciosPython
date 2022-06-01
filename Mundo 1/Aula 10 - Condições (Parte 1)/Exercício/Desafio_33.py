print("="*19, "DESAFIO 33", "="*19)
print("Qual é o número maior? ")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o teceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("-"*50)
print("Entre os valores {}, {}, e {}.".format(a, b, c,))
print("-"*50)
print("O menor valor digitado foi {}.".format(menor))
print("E o maior valor digitado é {}.".format(maior))
print("="*50)
