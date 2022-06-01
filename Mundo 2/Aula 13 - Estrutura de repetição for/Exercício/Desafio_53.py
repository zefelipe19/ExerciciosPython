'''Exercício Python 53: Crie um programa que leia uma frase 
qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
print("{:=^100}".format(" DESAFIO 53 "))
print("{:=^100}".format(" Analisador de Palíndromos "))
palavra = str(input("Digite a palavra/fraze que deseja: ")).strip().upper()
fatia = palavra.split()
junto = "".join(fatia)
inverso = ""
for pali in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[pali]
print("Escrevendo {} ao contrário é {}.".format(junto, inverso))
if inverso == junto:
    print("Temos um Palíndro!")
else:
    print("Isso não é um palindormo!")
print("="*100)
