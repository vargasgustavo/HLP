def acres(valor):
    valor = valor * 1.7
    return valor

valor = float(input("Digite um valor: "))

print(f'Valor original: {valor}, valor com acréscimo: {acres(valor)}')
