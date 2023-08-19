# def converte():
#     conve = km * 0.621371
#     print(f"\nA distância que digitou equivale a {conve} milhas\n")

# km = float(input("\nDigite a distância: "))
# converte()

def maior():
    if n1 > n2:
        maior = n1
    if n2 > n1:
        maior = n2

def calcMedia(n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        print("PARABÉNS")
        print(f"Aprovado com media {media}!")
    else:
        print(f"Reprovado com media {media}!")
        print(f"Quer fazer a sub (s/n)?\n")
        sub = input("")
        while sub == 's':
            n3 = float(input("Nota da sub: "))


n1 = float(input("Nota da primeira prova: "))
n2 = float(input("Nota da segunda prova: "))
