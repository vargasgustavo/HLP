def modulo(v):
    if v < 0:
        v = v * -1
    return v

valor = 3
print("|",valor,"| =", modulo(valor))
valor = -3
print("|",valor,"| =", modulo(valor))

valor = int(input("Digite um inteiro: "))
print("|",valor,"| =", modulo(valor))
