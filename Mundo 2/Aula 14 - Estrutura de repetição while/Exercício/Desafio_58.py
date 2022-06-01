'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print("{:=^100}".format(" DESAFIO 58 "))
print("Adivinhe o número que estou pensando...")
cont = 1
pc = randint(1, 10)
user = int(input("Em que número estou pensando? => "))
while user != pc:
    if user > pc:
        print("É menos.... ", end="")
    else:
        print("É mais.... ", end= "")
    user = int(input("Tente novamente! => "))
    cont += 1
print("Parabéns você acertou, o eu estava pensando no número {}.".format(pc))
print("você precisou de {} tentativas para acertar!".format(cont))

print("="*100)
