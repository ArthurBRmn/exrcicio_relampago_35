class Produto:

    def __init__ (self):
        self.__nome = ''
        self.__preco = 0
        self.__tipo = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def calcularPreco(self):
        pass

class ProdutoEletronico(Produto):
    def __init__(self):
        pass

    def calcularPreco(self):
        return  self.get_preco() - (self.get_preco() * 10 / 100)

class ProdutoRoupa(Produto):
    def __init__(self):
        pass

    def calcularPreco(self):
        return self.get_preco() - (self.get_preco() * 20 / 100)

class ProdutoLivro(Produto):
    def __init__(self):
        pass

    def calcularPreco(self):
        return self.get_preco() - (self.get_preco() * 5 / 100)


