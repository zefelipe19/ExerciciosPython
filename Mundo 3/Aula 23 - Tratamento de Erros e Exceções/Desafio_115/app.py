# Desafio_115 Criando um banco de dados simples com menu interativo.
from tools import menus
from tools import imput_menu
from time import sleep

menus.tituloPrin("Gestão de Clientes")
dadosClientes = "clientes.txt"

while True:
    print("\033[1m", "-" * 39, "\033[m")
    menus.linha("1. Ver Clientes Cadastrados", "blue")
    menus.linha("2. Cadastrar Novo cliente", "green")
    menus.linha("3. Fechar Programa" , "red")
    print()
    n = imput_menu.leiaInt("\033[1mTecle um número correspondente no menu: \033[m")

    if n == 1:
        menus.menuLinha(f"{'Mostrando Clientes'}")
        imput_menu.leiaArquivo(dadosClientes)
        sleep(0.5)

    elif n == 2:
        menus.menuLinha(f"{'Adcionando Clientes'}")
        imput_menu.escrevaArquivo(dadosClientes)
        sleep(0.5)

    elif n == 3:
        menus.menuLinha(f"{'Fechando Programa... Até Mais!'}")
        sleep(0.5)
        break
