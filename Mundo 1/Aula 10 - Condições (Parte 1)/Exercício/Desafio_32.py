import datetime
print("="*19, "DESAFIO 32", "="*19)
print("Analizador de ano....")
ano = int(input("Que ano você gostaria de analizar? (tecle '0' para ver o ano atual): "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} É BISSEXTO e tem 366 dias.".format(ano))
else:
    print("O ano de {} NÃO É BISSEXTO ou seja não tem 366 dias e sim 365.".format(ano))

print("Obrigado....")
print("="*50)
