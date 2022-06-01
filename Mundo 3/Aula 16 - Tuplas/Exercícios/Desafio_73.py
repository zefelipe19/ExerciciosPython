'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
print("{:=^100}".format(" DESAFIO 73 "))
times = (
    "Corinthians", "Santos", "Avaí", "América-MG", "Bragantino", "São Paulo", "Atlético-MG",
    "Botafogo", "Internacional", "Coritiba", "Cuiabá", "Atletico-PR", "Palmeiras", "Flamengo",
    "Fluminence", "Goiás", "Ceará", "Juventude", "Atlético-GO", "Fortaleza"
)
print("--"*50)
print(f"Os Top 5 times são {times[0:5]}")
print("--"*50)
print(f"OS 4 ultimos são {times[-4:]}")
print("--"*50)
print(sorted(times))
print("--"*50)
print(f"O time Flamengo está em {times.index('Flamengo') + 1}º lugar.")
print("="*100)
