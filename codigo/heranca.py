class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__cpf = 0
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__matricula = 0
        self.__escola_segundo_grau = ""
    def get_matricula(self):
        return self.__matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def get_escola_segundo_grau(self):
        return self.__escola_segundo_grau
    def set_escola_segundo_grau(self, escola_segundo_grau):
        self.__escola_segundo_grau = escola_segundo_grau

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__titulacao = ""
    def get_titulacao(self):
        return self.__titulacao
    def set_titulacao(self, titulacao):
        self.__titulacao = titulacao

