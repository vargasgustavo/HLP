def parImp():
    return num % 2 == 0

num = int(input("Digite um valor inteiro: "))

if parImp() == 0:
    print(f'O valor {num} é ímpar!')
else:
    print(f'O valor {num} é par!')
