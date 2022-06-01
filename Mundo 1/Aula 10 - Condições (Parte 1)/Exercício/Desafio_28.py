import random, time
print("="*19, "DESAFIO 28", "="*19)
pergunta = str(input("Vamos jogar um jogo? ")).strip().lower()
if pergunta == "sim":
    print("Muito Bem....")
    computador = random.randint(0, 5)
    print("Estou pensando em um número entre 0 e 5....")
    jogador = int(input("Pode me dizer qual é? "))
    print("Uhm....")
    time.sleep(2)
    if jogador == computador:
        print("Muito Bem ! Você acertou o número que eu pensei foi {}.".format(computador))
    else:
        print("Que pena... O número que eu pensei foi {} e não {}.".format(computador, jogador))
else:
    print("Tudo bem....")
    time.sleep(1)
    print("Até Mais...")
print("="*50)
