import os

def retira_enter(x):
    tam = len(x) - 1
    x = x[:tam]
    return x

def cadastro():
    os.system("cls")
    print("Cadastro")
    print()
    nome = input("Nome: ")
    idade = input("Idade: ")
    altura = input("Altura: ")
    f = open("agenda.db", "a")
    f.write(nome + "\n")
    f.write(idade + "\n")
    f.write(altura + "\n")
    f.close()

def listagem():
    os.system("cls")
    print("Listagem")
    f = open("agenda.db", "r")
    print()
    while True:
        nome = f.readline()
        nome = retira_enter(nome)
        if nome == "":
            break
        idade = f.readline()
        idade = retira_enter(idade)
        altura = f.readline()
        altura = retira_enter(altura)
        print("|%-30s|%-5s|%-5s|"%(nome, idade, altura))
    print()
    temp = input("Tecle enter para continuar")
    f.close()

op = 1
while op != 0:
    os.system("cls")
    print()
    print("1 - Cadastro")
    print("2 - Listar")
    print("0 - Fim")
    op = int(input("Opção: "))
    if op == 1:
        cadastro()
    if op == 2:
        listagem()

print("Fim")
