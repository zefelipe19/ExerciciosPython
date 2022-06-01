from math import floor, ceil, trunc

print("="*19, "DESAFIO 16", "="*19)
print("Arrendondador de números reais.")
real = float(input("Digite aqui o número que deseja converter. "))

print("O número {}, arrendondado para baixo fica {:.2f}. ".format(real, floor(real)))
print("e arredondado para cima fica {:.2f}, e apenas a porção inteira é {}. ".format(ceil(real), trunc(real)))

print("="*50)
