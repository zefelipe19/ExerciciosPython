'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
print("{:=^100}".format(" DESAFIO 60 "))
print("{:=^100}".format(" Calculadora Fatorial "))
num = int(input("Digite o número que deseja ver seu calculo fatorial: "))
cont = num
fatorial = 1
print("Calculando {}! => ".format(num), end= "")
#while cont > 0: # Estura de repetição com while 
for c in range (num, 0, -1): # A mesma estrutura usando o 'for' 
    print("{}".format(cont), end= "")
    if cont > 1:
        print(" x ", end= "")
    else:
        print(" = ", end= "")
    fatorial *= cont
    cont -= 1
print(fatorial)
print("="*100)