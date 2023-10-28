# set() atribuir | get() obter

class Pessoa:
    _nome = ""
    def __init__(self):
        print("Eu sou o construtor")

    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

p = Pessoa()
p.setNome("Carlos")
print(f'Nome: {p.getNome()}')

class Aluno(Pessoa):
    _curso = ""
    def setCurso(self, curso):
        self._curso = curso

    def getCurso(self):
        return self._curso
    
al = Aluno()
al.setNome("Gustavo")
al.setCurso("Computação")
print(f'O aluno {al.getNome()} está cursando {al.getCurso()}!')
