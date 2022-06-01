'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print("{:=^100}".format(" DESAFIO 62 "))
print("Progressão Aritmetica v3")
num = int(input("Digite o número que deseja ver sua PA: "))
razao = int(input("E qual será a razão? "))
termo = num
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print("{} -> ".format(termo), end= "")
        termo += razao
        cont += 1
    print("...")
    mais = int(input("Quer ver mais termos? (tecle '0' para terminar) -> "))
    print("PA terminada com {} termos.".format(tot))
print("="*100)
