'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
print(f"{' DESAFIO 102':=^100}")

def fatorial(n, show=False):
    '''Parametro: "n" é o número que deseja fazer o calculo fatorial
    show: Coloca-se "True" se desejar ver o calculo por escrito
    return: é o valor que vai ser atribuido a função'''
    cont = n
    f = 1
    while cont != 0:
        if show == True:
            print(f"{cont}", end="")
            if cont > 1:
                print(" x ", end="")
            if cont == 1:
                print(" = ", end="")
        f *= cont
        cont -= 1
    return f


print(fatorial(12, True))
print("="*100)
