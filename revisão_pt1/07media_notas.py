def mediaNotas():
    return (n1 + n2) / 2

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
mediaNotas()

if mediaNotas() >= 6:
    print(f'Sua média com as notas {n1} e {n2} foi: {mediaNotas()}')
else:
    print(f'Sua media foi: {mediaNotas()} estude mais!')
