class Produto:
    def __init__(self):
        self.__nome = ""
        self.__preco = 0.0
        self.__unitario = 0
        self.__quantidade = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_unitario(self):
        return self.__unitario

    def set_unitario(self, unitario):
        self.__unitario = unitario

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def calcular_preco(self):
        pass

    def vender_quantidade(self):
        pass

class ProdutoEletronico(Produto):
    def __init__(self):
        Produto.__init__(self)

    def vender_quantidade(self):
        if self.get_quantidade() >= self.get_unitario():
            self.set_quantidade(self.get_quantidade() - self.get_unitario())
            return self.get_quantidade()

        else:
            return self.get_quantidade()


    def calcular_preco(self):
        return self.get_preco() * self.get_quantidade()

class ProdutoRoupa(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.__desconto = 0

    def get_desconto(self):
        return self.__desconto

    def set_desconto(self, desconto):
        self.__desconto = desconto

    def vender_quantidade(self):
        if self.get_quantidade() >= self.get_unitario():
            self.set_quantidade(self.get_quantidade() - self.get_unitario())
            return self.get_quantidade()

        else:
            return self.get_quantidade()

    def calcular_preco(self):
        return (self.get_preco() - self.get_desconto()) * self.get_unitario()

class ProdutoAlimento(Produto):
    def __init__(self):
        Produto.__init__(self)

    def vender_quantidade(self):
        if self.get_quantidade() >= self.get_unitario():
            self.set_quantidade(self.get_quantidade() - self.get_unitario())
            return self.get_quantidade()

        else:
            return self.get_quantidade()

    def calcular_preco(self):
        return self.get_preco() * self.get_unitario()