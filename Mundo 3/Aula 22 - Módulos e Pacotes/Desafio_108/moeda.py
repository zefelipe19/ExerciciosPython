def metade(num=0):
    meta = num // 2
    return meta


def dobro(num=0):
    dob = num * 2
    return dob


def aumenta(num=0):
    a = num
    s = a + (a * 0.10)
    return s


def diminui(num=0):
    a = num
    s = a - (a * 0.10)
    return s

def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")