'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
num = (
    int(input("Digite um número: ")), int(input("Digite um número: ")), 
    int(input("Digite um número: ")), int(input("Digite um número: ")), 
)
print(f"O número 9 aparece {num.count(9)} vezes")
if 3 in num:
    print(f"O número 3 foi digitado na {num.index(3) + 1}ª posição")
else:
    print("Não existe o número 3 no bloco")
print("Os números pares são: ", end= "")
for c in num:
    if c % 2 == 0:
        print(f'{c} ', end= "")
    elif c % 2 == 1:
        print("", end= "")