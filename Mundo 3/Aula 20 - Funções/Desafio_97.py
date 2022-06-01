'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:escreva('Olá, Mundo!') Saída: 
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~'''
print(f"{' DESAFIO 97 ':=^100}")

def escreva(txt):
    l = len(txt) + 4
    print("~" * l)
    print(f"  {txt}")
    print("~" * l)

escreva("Hello, World!")

print("="*100)
