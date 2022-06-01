'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
print(f"{' DESAFIO 79 ':=^100}")

lista = []
cont = 0
menu = ""

while True:
    print("-"*50)
    cont += 1
    n = int(input(f"Digite o {cont}ª número para ser adcionado a lista: "))
    if n not in lista:
        lista.append(n)
        print(f"O núemro {n} foi adicionado com sucesso!")
    else:
        print(f"O número {n} já existe!")
    print("-" * 50)
    menu = str(input("Deseja continuar? [S/N] => ")).strip().upper()[0]
    while menu not in "SN":
        menu = str(input("Comando inválido, Tente Novamente! [S/N] => ")).strip().upper()[0]
    if menu == "N":
        print("Ok....")
        break
print("-"*50)
print(f"A sua lista ficou assim: {lista}.")
print(f"A sua lista em ordem fica: {sorted(lista)}.")

print("="*100)
