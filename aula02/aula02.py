def media():
    media = (n1 + n2) / 2
    if (media >= 6):
        print(f"\nO aluno {nome} de ra {ra}, foi aprovado com media {media}!\n")
    else:
        print(f"\nO aluno {nome} de ra {ra}, foi reprovado com media {media}!\n")
# Fim da função

ra = input("Qual o ra do aluno: ")
nome = input("Qual o nome: ")
n1 = float(input("Nota da primeira prova: "))
n2 = float(input("Nota da segunda prova: "))
media()
print("Boas férias!")
