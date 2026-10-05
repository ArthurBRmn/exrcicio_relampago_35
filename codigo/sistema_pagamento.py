class Funcionario:
    def __init__(self):
        self.__salario_mensal = 0.0
    def get_salario_mensal(self):
        return self.__salario_mensal
    def set_salario_mensal(self, salario_mensal):
        self.__salario_mensal = salario_mensal
    def calcular_pagamento(self):
        pass

class FuncionarioComum(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
    def calcular_pagamento(self):
        return self.get_salario_mensal()

class Gerente(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.__bonus_fixo = 0.0
    def get_bonus_fixo(self):
        return self.__bonus_fixo
    def set_bonus_fixo(self, bonus_fixo):
        self.__bonus_fixo = bonus_fixo
    def calcular_pagamento(self):
        return self.get_salario_mensal() + self.__bonus_fixo

class Diretor(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.__lucro_empresa = 0.0
        self.__participacao_lucros = 0.0
    def get_lucro_empresa(self):
        return self.__lucro_empresa
    def set_lucro_empresa(self, lucro_empresa):
        self.__lucro_empresa = lucro_empresa
    def get_participacao_lucros(self):
        return self.__participacao_lucros
    def set_participacao_lucros(self, participacao_lucros):
        self.__participacao_lucros = participacao_lucros
    def calcular_pagamento(self):
        participacao = self.__lucro_empresa * (self.__participacao_lucros / 100)
        return self.get_salario_mensal() + participacao
