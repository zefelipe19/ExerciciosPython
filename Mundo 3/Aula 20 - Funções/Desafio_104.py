'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
á função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')'''
print(f"{' DESAFIO 104':=^100}")

def leiaInt(num):
    a = input(str(num))
    while True:
        if a.isnumeric():
            return a
            break
        else:
            print("\033[;31m", "Erro, Digite um número inteiro!", "\033[m")
            a = input(str(num))


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
print("="*100)
