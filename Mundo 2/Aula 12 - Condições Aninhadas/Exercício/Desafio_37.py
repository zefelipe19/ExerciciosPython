'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
cores = {
    "limpo": "\033[m",
    "red": "\033[1;30;41m",
    "blue": "\033[1;30;44m",
    "green": "\033[1;30;42m"

}
print("-=-"*19, "DESAFIO 37", "-=-"*19)
print("Conversor de número inteiro...")
num = int(input("Digite o número INTEIRO que deseja converter: "))
print("Digite qual o formato para converter \n{}[1] para Binário \n{}[2] para Octal \n{}[3] para Hexadecimal{}".format(
    cores["green"], cores["blue"], cores["red"], cores["limpo"]))
user = str(input("Digite sua escolha: ")).strip()
if user == "1":
    binary = bin(num)
    print("{}O número inteiro {}, convertido para binário é {}".format(cores["green"], num, binary[2:]))
elif user == "2":
    octal = oct(num)
    print("{}O número inteiro {}, convertido para octal é {}".format(cores["blue"], num, octal[2:]))
elif user == "3":
    hexa = hex(num)
    print("{}O número inteiro {}, convertido para Hexadecimal é {}".format(cores["red"], num, hexa[2:]))
else:
    print("Opção invalida")
print(cores["limpo"])
print("Fim do programa")

print("-=-"*42)
