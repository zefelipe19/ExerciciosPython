'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for.'''
print("{:=^100}".format("DESAFIO 49"))
print("TABOADA 2.0")
menu = int(input('''Escolha a opção desejada:
[1] Adição
[2] Multiplicação
=> '''))
print("-="*25)
if menu == 1:
    n = int(input("Digite o Número que dejesa ver a taboada: => "))
    for c in range (1,11):
        print("{} + {} = {}".format(n, c, n + c))

elif menu == 2:
    n = int(input("Digite o Número que dejesa ver a taboada: => "))
    for c in range (1, 11):
        print("{} x {} = {}".format(n, c, n * c))
else:
    print("comando inválido")
print("-="*25)
print("="*100)