'''Além de manipular as listas adicionando novos elementos, também podemos adicionar listas dentro de ouras listas
podendo serem manipuladas com um comando "enumerate(nome_da_lista)", com esse comando podemos manipular a lista com um "for in"
nomeando um indicie, e elemento. Exemplo:'''

produtos = [["produto1", 100], ["produto2", 80], ["produto3", 55.99]]

for indicie, elemento in enumerate(produtos):
    print(f"indicies: {indicie}, {elemento}")

'''Com esse exemplo, podemos navegar pelos indicies dentro da lista "produtos", e tambem navegar pelas listas dentro de "produtos."
Exemplo:'''

print(f"O preço do produto2 é {produtos[1][1]}")
