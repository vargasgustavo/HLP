def soma(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x / y

def calcula(calculadora):
    calculadora = input("Escolha o tipo de cálculo: ")
    if calculadora == "+":
        soma()
        print(f"A soma de {x} e {y} é {soma}")
    elif calculadora == "-":
        subtracao()
        print(f"A diferença entre {x} e {y} é {subtracao}")
    elif calculadora == "*":
        multiplicacao()
        print(f"O produto de {x} e {y} é {multiplicacao}")
    elif calculadora == "/":
        divisao()
        print(f"A divisão entre {x} e {y} é {divisao}")

x = float(input("\nDigite o valor de x: "))

y = float(input("\nDigite o valor de y: "))

print("\n             Tipos de cálculo             \n")
print("              --> +  -  *  /                ")
print("\n##########################################\n")
calcula()
