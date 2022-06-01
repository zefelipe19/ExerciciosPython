def metade(num=0, formato=False):
    meta = num // 2
    return meta if formato is False else moeda(meta)


def dobro(num=0, formato=False):
    dob = num * 2
    return dob if formato is False else moeda(dob)


def aumenta(num=0, formato=False):
    a = num
    s = a + (a * 0.10)
    return s if formato is False else moeda(s)


def diminui(num=0, formato=False):
    a = num
    s = a - (a * 0.10)
    return s if formato is False else moeda(s)

def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")