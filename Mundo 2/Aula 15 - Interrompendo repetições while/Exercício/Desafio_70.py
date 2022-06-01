'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
print("{:=^100}".format(" DESAFIO 70 "))
print("{:-^100}".format(" MERCADINHO BARATINHO "))
total = caro = cont = barato = 0
baratoNome = " "
while True:
    print("-"*100)
    produto = str(input("Digite o nome do produto: ")).strip().upper()
    preco = float(input("O valor do produto R$: "))
    cont += 1
    
    if cont == 1:
        baratoNome = produto
        barato = preco
    elif preco < barato:
        baratoNome = produto
        barato = preco
    elif preco > 1000:
        caro += 1
    total += preco

    continua = " "
    while continua not in "SN":
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continua == "N":
        print("OK....\nEncerrando.......")
        break
print(f"Total a pagar R${total:.2f}; \nSão {caro} mais caros que R$ 1000.00; \nO produto mais barato é {baratoNome}.")
print("="*100)
