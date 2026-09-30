class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):

    def __init__(self):
        self.__base = 0
        self.__altura = 0

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    def calcular_area(self):
        return self.__altura * self.__base

    def calcular_perimetro(self):
        return 2 * (self.__altura + self.__base)

class Circulo(FormaGeometrica):

    def __init__(self):
        self.__raio = 0

    def get_raio(self):
        return self.__raio

    def set_raio(self, raio):
        self.__raio = raio

    def calcular_area(self):
        return 3.14 * self.__raio * self.__raio

    def calcular_perimetro(self):
        return 2 * 3.14 * self.__raio