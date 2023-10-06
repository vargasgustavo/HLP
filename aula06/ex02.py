dec = int(input("Digite um valor inteiro: "))
bin = []
while dec >= 2:
    resto = dec % 2
    dec = dec // 2
    bin.append(resto)
bin.append(dec)
binStr = ""
for i in range(len(bin) - 1, -1, -1):
    binStr += str(bin[i])
print(f'Valor em binário: {binStr}')
