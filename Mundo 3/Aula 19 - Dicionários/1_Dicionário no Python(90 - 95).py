'''Os dicionários, funcionam de forma muito parecida com as listas, porem, diferente das listas onde os indicies são apontados por apenas números.
as listas podem usar "keys" para indexar os conteúdos "valores ou values", sendo assim em uma lista a string "Felipe" ela seria indexada a um número,
em um dicionário essa string pode ser adicionada a uma "key" chamada "nome: ".'''

# values, são os valores indexados a uma "key"
# keys, são os indicies do dicionário
# items, são todos os items que estão em uma lista
# Exemplo:

pessoa = {"nome": "Felipe", "idade": 19, "sexo": "M"}
print(f"O {pessoa['nome']} tem {pessoa['idade']} anos.")

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print("-="*30)
 # Podemos também adicionar dicionários a uma lista EX:

locadora = [
    {
    "filme" : "Star Wars",
    "ano" : "1977",
    "diretor" : "George Lucas"
    },
    {
    "filme" : "Avengers",
    "ano" : "2012",
    "diretor" : "Joss Whedon"
    },
    {
    "filme" : "Matrix",
    "ano" : "1999",
    "diretor" : "Wachowski"
    }
]

print(locadora[1]["filme"])
print("-="*30)

for c in locadora:
    print(c)

