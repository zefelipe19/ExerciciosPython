def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print("\033[1;31m", "Erro! Por Favor digite um número inteiro válido.", "\033[m")
            continue
        if n not in (1, 2, 3):
            print("\033[1;31m", "Erro! Por Favor digite um comando válido!", "\033[m")
            continue
        else:
            return n


def leiaArquivo(arquivoNome):
    try:
        with open (arquivoNome, 'rt') as arquivoLeitura:
            for v in arquivoLeitura:
                print(v)
    except:
        print("Tivemos um erro ao ler o arquivo :(")
    finally:
        arquivoLeitura.close()



def escrevaArquivo(arquivoNome):
    try:
        nome = str(input("Digite o nome: ")).strip().title()
        email = str(input("Digite o email: ")).strip()
        with open ("clientes.txt", "a") as arquivoEscrita:
            arquivoEscrita.write(f"{nome}")
            arquivoEscrita.write(f"\t\t{email}")
            arquivoEscrita.write("\n")
    except:
        print("Tivemos um erro ao fazer o registro :(")
    finally:
        arquivoEscrita.close()