'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print("{:=^100}".format(" DESAFIO 76 "))
lanches = (
    "Coxinha", 1.50,
    "Enrroladinho", 2.0,
    "Esfirra", 2.50,
    "Risole", 2.50,
    "Empada", 2.0,
    "Bolo", 3.0
)
print(f"{' Cardapio ':-^58}")
for comida in range (0, len(lanches)):
    if comida % 2 == 0:
        print(f"{lanches[comida]:.<50}", end= "")
    else:
        print(f"R${lanches[comida]:>5.2f}")
print("-"*58)
print("="*100)
