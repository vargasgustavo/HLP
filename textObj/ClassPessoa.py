class Pessoa:
    def __init__(self, cod: int, nome: str, email: str, celular: int, RG: int, CPF: int, cep: int, rua: str, bairro: str, cidade: str, estado: str):
        self._cod = cod
        self._nome = nome
        self._email = email
        self._celular = celular
        self._RG = RG
        self._CPF = CPF
        self._cep = cep
        self._rua = rua
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado

    def getCod(self):
        return self._cod

    def getNome(self):
        return self._nome
    
    def getEmail(self):
        return self._email
    
    def getCelular(self):
        return self._celular
    
    def getRG(self):
        return self._RG
    
    def getCPF(self):
        return self._CPF
    
    def getCep(self):
        return self._cep
    
    def getRua(self):
        return self._rua
    
    def getBairro(self):
        return self._bairro
    
    def getCidade(self):
        return self._cidade
    
    def getEstado(self):
        return self._estado

# p = Pessoa()
# p.setCodNome("Carlos")
# print("Cod: ", p.getCod())
# print("Nome: ", p.getNome())
