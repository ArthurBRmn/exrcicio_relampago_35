from codigo.formageometrica01 import *

def test_retornar_raio_circulo():
    circulo = Circulo()
    circulo.set_raio(5)
    assert circulo.get_raio() == 5

def test_calcular_area_circulo():
    circulo = Circulo()
    circulo.set_raio(5)
    assert circulo.calcular_area() == 78.5

#-----------------------------------------------

def retornar_altura_retangulo():
    retangulo = Retangulo()
    retangulo.set_altura(2)
    assert retangulo.get_altura() == 2

def retornar_base_retangulo():
    retangulo = Retangulo()
    retangulo.set_base(2)
    assert retangulo.get_base() == 2

def test_calcular_area_retangulo():
    retangulo = Retangulo()
    retangulo.set_altura(2)
    retangulo.set_base(2)
    assert retangulo.calcular_area() == 4
