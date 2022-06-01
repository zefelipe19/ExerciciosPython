'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
print(f"{' DESAFIO 77 ':=^100}")
palavras = (
    "LIVRO",
    "ESTUDAR",
    "CASAMENTO",
    "FELICIDADE",
    "FILHOS"
)
for palavra in palavras:
    print(f"\nNa palavra {palavra} temos: ", end= "")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=' ')
print("\n")
print("="*100)
