'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''
cor = {
    "clear" : "\033[m",
    "red" : "\033[1;30;41m",
    "green" : "\033[1;30;42m",
    "yellow" : "\033[1;30;43m",
    "gray" : "\033[1;30;47m"
}
print("-=-"*19, "DESAFIO 43", "-=-"*19)
print("Calculadora de IMC")
peso = float(input("Digite seu peso Kg: "))
altura = float(input("Digite sua altura em metros, (Ex: 1.56): "))
imc = peso / (altura ** 2)
print("O seu IMC é de {:.1f}, Você está: ".format(imc))
if imc < 18.5:
    print("{}ABAIXO DO PESO, CUIDADO!{}".format(cor["red"], cor["clear"]))
elif 18.5 < imc < 25:
    print("{}NO PESO IDEAL, PARABÉNS!{}".format(cor["green"], cor["clear"]))
elif 25 < imc < 30:
    print("{}COM SOBREPESO! Cuidado....{}".format(cor["yellow"], cor["clear"]))
elif 30 < imc < 40:
    print("{}COM OBESIDADE!, CUIDADO...{} Procure um médico.".format(cor["red"], cor['clear']))
else:
    print("{}COM OBESIDADE MÓRBIDA. PROCURE UM MÉDICO URGENTE!!!!!!{}".format(cor["gray"], cor["clear"]))

print("FIM")
print("-=-"*50)
