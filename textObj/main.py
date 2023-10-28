from ClassPessoa import Pessoa
from Client import cadastro, ler

p = Pessoa

opc = 1
while opc != 0:
    print("+--------------------+")
    print("|CADASTRO DE CLIENTES|")
    print("+--------------------+")
    print("|    1 - CADASTRO    |")
    print("|    2 - LEITURA     |")
    print("|    0 - FIM         |")
    print("+--------------------+\n")

    opc = int(input("Opção: "))

    if opc == 1:
        cadastro()
    if opc == 2:
        ler()
print("FIM")
