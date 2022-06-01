print("="*19, "DESAFIO 35", "="*19)
print("-=-"*50)
print("Analizador de Triângulos.")
print("-=-"*50)
r1 = float(input("Digite o comprimento do primeiro seguimento: "))
r2 = float(input("Digite o comprimento do segundo seguimento: "))
r3 = float(input("Digite o comprimento do terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Um triângulo com as medidas acima PODE EXISTIR.")
else:
    print("Um triângulo com as medidas acima NÃO PODE EXISTIR.")
print("="*50)
