'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
import datetime
print("-=-"*19, "DESAFIO 41", "-=-"*19)
print("Confederação Nacional de Natação")
ano = int(input("Digite o ano em que o participante nasceu: "))
hoje = datetime.date.today().year
idade = hoje - ano
if idade <= 9:
    print("O participante tem {} anos, é da categoria 'MIRIM'.".format(idade))
elif 9 < idade <= 14:
    print("O participante tem {} anos, é da categoria 'INFANTIL'.".format(idade))
elif idade <= 19:
    print("O participante tem {} anos, é da categoria 'JÚNIOR'.".format(idade))
elif idade <= 25:
    print("O participante tem {} anos, é da categoria 'SÊNIOR'.".format(idade))
elif idade > 25:
    print("O participante tem {} anos, é da categoria 'MASTER'.".format(idade))
else:
    print("Essa resposta não é valida")
print("-=-"*19)
