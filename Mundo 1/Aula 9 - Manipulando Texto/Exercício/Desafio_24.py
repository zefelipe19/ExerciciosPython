print("="*19, "DESAFIO 24", "="*19)
nome = str(input("Qual é o nome da cidade que você mora? ")).strip()
print("Analizando.... ")
print("A cidade {} começa com 'Santo'? {}".format(nome, nome[:5].lower() == "santo"))

print("="*50)
