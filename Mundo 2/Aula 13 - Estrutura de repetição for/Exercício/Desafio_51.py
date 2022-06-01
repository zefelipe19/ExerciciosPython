'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''
print("{:=^100}".format("DESAFIO 51"))
print("Progressão Aritimetica.")
primeiro = int(input("Digite o valor do PRIMEIRO termo da PA: "))
razao = int(input("Agora digite a RAZÃO da PA: "))
decimo = primeiro + (10 -1) * razao
for c in range (primeiro, decimo + razao, razao):
    print("{}".format(c), end = " -> ")
print("Fim")
print("="*100)
