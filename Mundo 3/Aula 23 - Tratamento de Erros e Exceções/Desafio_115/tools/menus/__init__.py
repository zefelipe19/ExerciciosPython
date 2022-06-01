def tituloPrin(msg):
    print("\033[1m")
    print("-" * 40)
    print(f"{msg.center(40)}")
    print("-" * 40)
    print("\033[m")


cores = {
    "red" : "\033[1;31m",
    "green" : "\033[1;32m",
    "blue" : "\033[1;36m",
    "clear" : "\033[m"
}

def linha(msg, color="clear"):
    print(cores[color], f"{msg}", cores["clear"])


def menuLinha(msg):
    print("\033[1m")
    print("-" * 40)
    print(f"{msg.center(40)}")
    print("-" * 40)
    print("\033[1m")