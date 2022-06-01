'''Exercício Python 48: Faça um programa que calcule a soma 
entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
print("{:=^100}".format("DESAFIO 48"))
soma = 0
cont = 0
for mum in range (1, 501, 2):
    if mum % 3 == 0:
        cont = cont + 1
        soma = soma + mum
print("As somas de todos os {} valores, é igual à: {}.".format(cont, soma))
print("="*100)
