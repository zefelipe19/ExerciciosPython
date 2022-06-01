'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores.'''
print(f"{' DESAFIO 106':=^100}")

def manual():
    while True:
        print("\033[1;32m")
        menu = str(input("Deseja ver o manual de: ")).lower().strip()
        if menu == "fim":
            break
        l = len(menu) + 24
        print('\033[1;35m')
        print("~"*l)
        print(f"Mostrando o Manual de '{menu}'. ")
        print("~"*l)
        help(menu)

manual()

print("\033[m")
print("="*100)
