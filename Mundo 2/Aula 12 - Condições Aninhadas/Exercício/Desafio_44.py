'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
print("-=-"*19, "DESAFIO 45", "-=-"*19)
preco = float(input("Informe o preço do produto: R$ "))
menu = str(input("Selecione o metodo de pagamento: \n[1] À Vista(Dinheiro/Cheque). \n[2] À Vista(Cartão). \n[3] Cartão(Parcelado).\n")).strip()
if menu == "1":
    valor = preco * 0.10
    desconto = preco - valor
    print("O valor final a pagar com dinheiro ou cheque será: R$ {:.2f}".format(desconto))
elif menu == "2":
    valor = preco * 0.05
    desconto = preco - valor
    print("O valor final a pagar à vista no cartão será: R$ {:.2f}".format(desconto))
elif menu == "3":
    menu2 = int(input("Digite o número de parcelas: "))
    if menu2 == 2:
        valor = preco / 2
        print("O valor da prestação em 2x é R$ {:.2f}".format(valor))
    elif menu2 > 2:
        valor = preco / menu2
        juros = (valor + (valor * 0.20)) * menu2
        prestacao = juros / menu2
        print("Em {}x, o valor final será de R$ {:.2f}, com o valor de cada prestação sendo de R$ {:.2f}.".format(menu2, juros, prestacao))
else:
    print("{}Codígo invalido!{}".format("\033[1;30;31m", "\033[m"))
print("-=-"*50)
