print("="*19, "DESAFIO 30", "="*19)
print("-=-"*10, "É IMPAR OU PAR?", "-=-"*10)

n = int(input("Digite um número: "))
r = n % 2
if r == 1:
    print("O número {} é IMPAR !!!".format(n))
else:
    print("O número {} é PAR !!!".format(n))
    
print("="*50)
