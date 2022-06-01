'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
print(f"{' DESAFIO 83 ':=^100}")

expressao = str(input("Digite uma expressão que use parênteses: "))
checagem = []

for simb in expressao:
    if simb == "(":
        checagem.append("(")
    elif simb == ")":
        if len(checagem) > 0:
            checagem.pop()
        else:
            checagem.append(")")
            break
if len(checagem) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão não é valida!")

print("="*100)
