'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print("{:=^100}".format(" DESAFIO 61 "))
print(" Progressão Aritimética v2 ")
primeiro = int(input("Digite o número que deseja ver a sua PA: "))
razao = int(input("Agora a razão do número: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end= "")
    termo += razao
    cont += 1
print("FIM")
print("="*100)
