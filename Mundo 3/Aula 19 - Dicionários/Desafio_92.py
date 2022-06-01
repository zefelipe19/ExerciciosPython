'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.'''
import datetime
print(f"{' DESADFIO 92 ':=^100}")

pessoa = {}
for c in range(1):
    pessoa['nome'] = str(input("Digite o nome: ")).title()
    pessoa['ano de nascimento'] = int(input("Digite o ano de nascimento: "))
    pessoa['ctps'] = int(input("Digite o número da CTPS (0 se não tiver): "))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input("Digite o ano de contratação: "))
    pessoa['salário'] = float(input("Digite o valor do salário: R$ "))
    idade = datetime.date.today().year - pessoa["ano de nascimento"]
    pessoa['aposentadoria'] = pessoa["contratação"] + 35 - pessoa["ano de nascimento"]

print("-=-"*18)
for k, v in pessoa.items():
    print(f" --- {k}, tem o valor de {v}")

print("="*100)
