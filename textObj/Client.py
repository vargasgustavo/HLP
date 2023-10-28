from ClassPessoa import Pessoa

p = Pessoa

def cadastro():
    print("+---------------------+")
    p.setcod(input("| Digite seu código:"))
    p.setnome(input("| Digite seu nome:"))
    p.setemail(input("| Digite seu email:"))
    p.setcelular(input("| Digite seu celular:"))
    p.setRG(input("| Digite seu RG:"))
    p.setCPF(input("| Digite seu CPF:"))
    p.setcep(input("| Digite seu cep:"))
    p.setrua(input("| Digite seu rua:"))
    p.setbairro(input("| Digite seu bairro:"))
    p.setcidade(input("| Digite seu cidade:"))
    p.setestado(input("| Digite seu estado:"))
    print("+---------------------+")

def ler():
    print("+----------------------------------------------+")
    print(f'| Cod: {p.getCod()}                            |')
    print(f'| Nome: {p.getNome()}                          |')
    print(f'| Email: {p.getEmail()}                        |')
    print(f'| Celular: {p.getCelular()}                    |')
    print(f'| RG: {p.getRG()}                              |')
    print(f'| CFP: {p.getCPF()}                            |')
    print(f'| Cep: {p.getCep()}                            |')
    print(f'| Rua: {p.getRua()}                            |')
    print(f'| Bairro: {p.getBairro()}                      |')
    print(f'| Cidade: {p.getCidade()}                      |')
    print(f'| Estado: {p.getEstado()}                      |')
    print("+----------------------------------------------+")
