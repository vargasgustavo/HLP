def promovido(dinheiro):
    return dinheiro * 1.7

d = float(input("Digite seu salário: "))
res = promovido(d)
print(f'Seu salário foi de {d} R$ para {res} R$')