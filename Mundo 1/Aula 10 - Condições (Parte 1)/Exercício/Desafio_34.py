print("="*19, "DESAFIO 34", "="*19)
print("Atualizador de Salários.")
salario = float(input("Digite o valor do seu salário: R$ "))
if salario > 1250:
    aumento = salario + salario * 0.10
    print("Seu salário sendo de R$ {:.2f} recebeu um aumento de 10%, sendo agora de R${:.2f}.".format(salario, aumento))
else:
    aumento = salario + salario * 0.15
    print("Seu Salário sendo de R$ {:.2f} \nvocê receberá 15% de aumento sendo agora R$ {:.2f}.".format(salario, aumento))
print("="*50)
