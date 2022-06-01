'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime
print("-=-"*19, "DESFIO 39", "-=-"*19)
print("Serviço militar obrigatorio")
print("-=-"*50)
print("Qual seu gênero")
print("Digite 'M' para 'Masculino' e 'F' para 'Feminino'.")
menu = str(input("")).strip().upper()
if menu == "F":
    print("Você não é obrigada a servir o serviço militar obrigatório!")
    user = str(input("Deseja servir mesmo assim ? Tecle 'S' para 'SIM' e 'N' para 'NÃo'. ")).strip().upper()
    if user == "S":
        idade = int(input("Digite o ano que você nasceu: "))
        hoje = datetime.date.today().year
        servico = hoje - idade
        if servico == 18:
            print("Você já pode se alistar!")
        elif servico > 18:
            print("Você já passou do ano de se alistar!")
        elif servico < 18:
            print("Você ainda não possui idade para se alistar!")
        else:
            print("Essa não é uma resposta valida!")
elif menu == "M":
    idade = int(input("Digite o ano que você nasceu: "))
    hoje = datetime.date.today().year
    servico = hoje - idade
    if servico == 18:
        print("Você já pode se alistar, procure um posto de reserva na sua cidade e aliste-se!")
    elif servico > 18:
        print("Você ja passou do tempo de se alistar! ja fazem {} Ano(s), se você não se alistou ainda procure um posto de reseva e o faça!".format(servico - 18))
    elif servico < 18:
        print("Tenha calma! Você ainda não pode se alistar ainda te falta {} Ano(s).".format(18 - servico))
    else:
        print("Essa não é uma resposta valida!")
else:
    print("Essa resposta não é valida!")
print("-=-"*50)
