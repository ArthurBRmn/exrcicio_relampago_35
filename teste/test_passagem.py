from codigo.passagem04 import *

def test_voo_domestico():
    voo_domestico = VooDomestico()
    voo_domestico.set_distancia(1000)
    voo_domestico.set_fatorPreco(10)
    assert voo_domestico.calcularPreco() == 10000

def test_voo_internacional():
    voo_internacional = VooInternacional()
    voo_internacional.set_distancia(10000)
    voo_internacional.set_fatorPreco(10)
    voo_internacional.set_taxa_conversao(1)
    assert voo_internacional.calcularPreco() == 100000