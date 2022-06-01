'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
cores = {
    "fundo":"\033[;;40m",
    "limpo":"\033[m",
    "verde":"\033[1;30;42m",
    "vermelho":"\033[1;30;41m",

}
print(cores["fundo"])
print("-=-"*19, "DESAFIO 36", "-=-"*19)
valorCasa = float(input("Digite o valor da casa que deseja comprar: R$ "))
salario = float(input("Agora digite o valor do salário: R$ "))
tempoAno = int(input("Em quantos anos será pago: "))
tempoMes = tempoAno * 12
prestacao = valorCasa // tempoMes
maximo = salario * 0.30
print("Com tempo de {} anos, são {} prestações com um valor de R$ {:.2f}".format(tempoAno, tempoMes, prestacao))
confirmacao = str(input("Deseja continuar? \nPressione 'S' para 'Sim' \nPressione 'N' para 'Não'\n")).strip().upper()
if confirmacao == "S":
    if prestacao > maximo:
        print("{}O seu financiamento NÃO FOI APROVADO.{}".format(cores["vermelho"], cores["fundo"]))
    else:
        print("{}Parábens seu finaciamento foi APROVADO.{}".format(cores["verde"], cores["fundo"]))
elif confirmacao == "N":
    print("Até mais!!!1")
print("Tenha um bom dia!!!!")

print("-=-"*42)
