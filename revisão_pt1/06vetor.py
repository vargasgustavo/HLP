i = 0
VET = 1000
lista = []
while i < VET:
    valor = int(input("Digite um numero "))
    i += 1
    lista.append(valor)
print(lista)

soma = sum(lista)
menor = min(lista)
maior = max(lista)
media = soma / VET
print("Somatoria", soma)
print("Maior elemento", maior)
print("Menor elemento", menor)
print("Media", media)
