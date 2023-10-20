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
    f = open("aggenda.db", "a")
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
        print("|%-30s|%20s|%20s|"%(nome, idade, altura))
    print()
    temp = input("Tecle enter para continuar")
    f.close()
