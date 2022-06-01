'''As funções em python são codígos usados para efetuar certas operações como a função "print" ela serve para mostrar uma certa
informação na tela, podemos também cria funções personalizadas usamos a função "def" para criar uma função personalizada. EX:'''
def funcaoEX(msg): # Dentro dos parenses podemos declarar um parâmetro, nesse ex o parametro é "msg" para que eu saiba que é uma mensagem.
    l = len(msg)
    print("-" * l)
    print(f"{msg}")
    print("-" * l) # Quando criamos uma função precisamos deixar 2 linhas em branco do nosso proxímo codigo.


funcaoEX("Olá, Mundo") # A fraze escrita dentro dos parênteses vai substituir o parâmetro "msg" criado anteriormente.
