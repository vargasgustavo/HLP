'''if 10 > 2:
    print("Dez eh maior!")
else:
    print("Dez eh menor!")
    print("Somente serei impresso se for falso")
print("Eu sempre serei impresso")'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

if media < 6:
    print("Voce quer fazer a sub? (s/n)")
    if 's':
        sub = float(input("Digite a nota da sub: "))
        