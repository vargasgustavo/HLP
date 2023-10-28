from ClassPessoa import Pessoa

p = Pessoa

def cadastro():
    print("+---------------------+")
    p._cod = input("| Digite seu código:")
    p._nome = input("| Digite seu nome:")
    p._email = input("| Digite seu email:")
    p._celular = input("| Digite seu celular:")
    p._RG = input("| Digite seu RG:")
    p._CPF = input("| Digite seu CPF:")
    p._cep = input("| Digite seu cep:")
    p._rua = input("| Digite seu rua:")
    p._bairro = input("| Digite seu bairro:")
    p._cidade = input("| Digite seu cidade:")
    p._estado = input("| Digite seu estado:")
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
