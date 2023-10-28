class Pessoa:  
    _cod = ""
    def setCod(self, cod):
        self._cod = cod
                
    _nome = ""
    def setNome(self, nome):
        self._nome = nome
                    
    _email = ""
    def setEmail(self, email):
        self._email = email
                    
    _celular = ""
    def setCelular(self, celular):
        self._celular = celular
                    
    _rg = ""
    def setRG(self, rg):
        self._rg = rg
                
    _cpf = ""
    def setCPF(self, cpf):
        self._cpf = cpf
                
    _cep = ""
    def setCep(self, cep):
        self._cep = cep
                
    _rua = ""
    def setRua(self, rua):
        self._rua = rua
    
    _bairro = ""
    def setBairro(self, bairro):
        self._bairro = bairro
                
    _cidade = ""
    def setCidade(self, cidade):
        self._cidade = cidade

    _estado = ""
    def setEstado(self, estado):
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
        return self._rg
    
    def getCPF(self):
        return self._cpf
    
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
