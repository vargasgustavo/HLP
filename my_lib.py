def cpftext(cpf):
    if len(cpf) != 14:
        return False
    cpf = cpf[0:3]+cpf[4:7]+cpf[8:11]+cpf[14:14]
    soma = 0
    i = 1
    for n in cpf[:9]:
        soma += int(n) * i
        i += 1
    resto1 = soma % 11
    if resto1 == 10:
        resto1 = 0
    
    soma = 0
    i = 1
    for n in cpf[1:10]:
        soma += int(n) * i
        i += 1
    resto2 = soma % 11
    if resto2 == 10:
        resto2 = 0
    resto1 = (resto1 * 10) + resto2
    resto2 = (int(cpf[9])*10) + int (cpf[10])
    if resto1 == resto2:
        return True
    else:
        return False

print(cpftext("457.354.898-01"))
