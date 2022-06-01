print("="*19, "DESAFIO 26", "="*19)
print("Contador de Letras 'A'.")
a = str(input("Digite qualquer coisa: ")).strip().lower()
print("A letra 'A' aparece {} vezes.".format(a.lower().count("a")))
print("A letra 'A' aparece pela primeira vez na posição {}.".format(a.find("a") + 1))
print("A letra 'A' aparece por ultimo na posição {}.".format(a.rfind("a") + 1))
print("Sem contar os espaços entre as palavras \nA letra 'A' aparece por ultimo na posição {}.".format(a.rfind("a") + 1 - a.count(" ")))

print("="*50)
