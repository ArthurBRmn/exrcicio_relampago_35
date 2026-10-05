class Voo:
    def __init__(self):
        self.__origem = ""
        self.__distancia = 0
        self.__destino = 0
        self.__data = 0

    def get_origem(self):
        return self.__origem

    def set_origem(self, origem):
        self.__origem = origem

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def calcularPreco(self):
        pass

class VooDomestico(Voo):
    def __init__(self):
        super().__init__()
        self.__fatorPreco = 0

    def Get_fatorPreco(self):
        return self.__fatorPreco

    def set_fatorPreco(self, fatorPreco):
        self.__fatorPreco = fatorPreco

    def calcularPreco(self):
        return self.get_distancia() * self.__fatorPreco

class VooInternacional(Voo):

    def __init__(self):
        super().__init__()
        self.__fatorPreco = 0
        self.__taxa_conversao = 0

    def Get_fatorPreco(self):
        return self.__fatorPreco

    def set_fatorPreco(self, fatorPreco):
        self.__fatorPreco = fatorPreco

    def get_taxa_conversao(self):
        return self.__taxa_conversao

    def set_taxa_conversao(self, taxa_conversao):
        self.__taxa_conversao = taxa_conversao

    def calcularPreco(self):
        return self.get_distancia() * self.__fatorPreco * self.__taxa_conversao


