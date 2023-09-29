def mod(num):
    if num < 0:
        num = num * -1
    return num

num = int(input("Digite um valor inteiro: "))

print(f'|{num}| = |{mod(num)}|')
