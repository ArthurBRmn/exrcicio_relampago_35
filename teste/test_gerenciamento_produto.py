from codigo.gerenciamneto_produto import *

def test_calcular_produto_eletronico():
    produto_eletronico = ProdutoEletronico()
    produto_eletronico.set_preco(100)
    produto_eletronico.set_quantidade(10)
    assert produto_eletronico.calcular_preco() == 1000

    produto_eletronico.set_unitario(3)
    assert produto_eletronico.vender_quantidade() == 7

def test_calcular_roupa():
    produto_roupa = ProdutoRoupa()
    produto_roupa.set_preco(100)
    produto_roupa.set_quantidade(10)
    produto_roupa.set_unitario(3)
    produto_roupa.set_desconto(10)
    assert produto_roupa.calcular_preco() == 270

    assert produto_roupa.vender_quantidade() == 7

def test_calcular_produto_alimento():
    produto_alimento = ProdutoAlimento()
    produto_alimento.set_preco(10)
    produto_alimento.set_quantidade(10)
    produto_alimento.set_unitario(4)
    assert produto_alimento.calcular_preco() == 40

    assert produto_alimento.vender_quantidade() == 6  