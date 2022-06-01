'''Funções podem e ou precisam possuir certas variáveis, essas variáveis normalmente são variáveis "locais" isto é
uma variável local só pode ser visivel em um certo bloco: Ex:'''
def linha():
    print("-"*30)
def funcao_ex(b):
    b += 4 # Dentro dessa função temos algumas variáveis, essas são variáveis locais
    c = 2 # So existem dentro dessa função(bloco)
    print(f"A dentro vale {a}.")
    linha()
    print(f"B dentro vale {b}.")
    linha()
    print(f"C dentro vale {c}.")


a = 5 # esta veriável ela tem o escopo global, pois está fora de qualquer bloco que possa existir no programa
funcao_ex(a)
linha()
print(f"A fora vale {a}.")

'''Quando estamos criando uma função as vezes precisamos que certos valores recebam alguma resposta, para isso usamos o comando
"return", esse comando serve para que um função possa alocar o seu resultado em alguma variável ou até mesmo na propria função EX:'''
linha()
def soma(a = 0, b = 0, c = 0):
    s = a + b + c
    #print(s) # nesse exemplo quando chamamos a função ela apenas restornará um print, então caso precisemos fazer o uso varias vezes 
             # essa função pode ser que seja um incomodo coloca-las em um único print.
             # Por isso ao invés de usar esse formato podemos usar o "return" para que a resposta dessa função seja colocada em uma variável EX:
    return(s)# Assim podemos clocar varios resultados dessa função em um único print

r1 = soma(5, 7, 9)
r2 = soma(7, 3)
r3 = soma(8)

print(f"O resultado é {r1}, {r2}, {r3}.")
