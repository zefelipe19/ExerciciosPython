'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(num): 
    while True:
        try:
            a = int(input(num))
        except:
            print("\033[1;31m", "Erro, Digite um número inteiro!", "\033[m")
            continue
        else:
            return a


def leiaFloat(num):
    while True:
        try:
            a = float(input(num))
        except (ValueError, TypeError) as erro:
            print("\033[1;31m", f"O erro foi {erro.__class__}", "\033[m")
            continue
        except KeyboardInterrupt:
            print("Usuário interrompeu o programa.")
        else:
            return a


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número inteiro {n}")

b = leiaFloat("Digite um número: ")
print(f"Você acabou de digitar o número decimal {b:.1f}")
