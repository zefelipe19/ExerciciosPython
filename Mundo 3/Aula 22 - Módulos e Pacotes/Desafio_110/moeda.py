def metade(num=0, formato=False):
    meta = num // 2
    return meta if formato is False else moeda(meta)


def dobro(num=0, formato=False):
    dob = num * 2
    return dob if formato is False else moeda(dob)


def aumenta(num=0, a=0, formato=False):
    n = num
    s = n + (n * (a // 100))
    return s if formato is False else moeda(s)


def diminui(num=0, d=0, formato=False):
    n = num
    p = d
    s = n - (n * (p // 100))
    return s if formato is False else moeda(s)

def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")


def resumo(num, a=0, d=0):
    print("-"*50)
    print("RESUMO".center(50))
    print("-"*50)
    print(f"Peço analizado: \t\t\t{moeda(num)}")
    print(f"A metade de {moeda(num)}, é: \t\t{metade(num, True)}")
    print(f"O Dobro de {moeda(num)}, é: \t\t{dobro(num, True)}")
    print(f"O Preço de {moeda(num)}, com {a}% é: \t{aumenta(num, a, True)}")
    print(f"O Preço de {moeda(num)}, menos {d}% é: \t{diminui(num, d, True)}")
    print("-"*50)