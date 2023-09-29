def areaTri(base, altura):
    return base * altura / 2

base = float(input("Base: "))
altura = float(input("Altura: "))

print(f'O triângulo de base {base} e altura {altura} tem sua área valendo {areaTri(base, altura)}')
