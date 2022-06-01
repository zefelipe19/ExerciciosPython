'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
print(f"{' DESAFIO 101':=^100}")

def voto(a):
    from datetime import date
    hoje = date.today().year
    idade = a
    v = hoje - idade
    if 18 > v > 16 or v > 70:
        return f"Com {v} anos o voto é OPCIONAL."
    elif v < 16:
        return f"Com {v} anos NÃO PODE VOTAR."
    else:
        return f"Com {v} anos o voto é OBRIGATÓRIO."


idade = int(input("Em que ano você nasceu? "))
print(voto(idade))

print("="*100)
