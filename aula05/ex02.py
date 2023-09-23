def area(a, b):
    return (a * b) / 2

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
res = area(base, altura)
print(f'A area do triângulo de base {base} e altura {altura} é {res}')
