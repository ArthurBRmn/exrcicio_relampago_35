from codigo.sistema_pedido import *

def teste_disconto_eletronico ():
    produto_eletronico = ProdutoEletronico()
    produto_eletronico.set_preco(100)
    assert produto_eletronico.calcularPreco() == 90

def teste_disconto_roupa ():
    produto_roupa = ProdutoRoupa()
    produto_roupa.set_preco(100)
    assert produto_roupa.calcularPreco() == 80

def teste_disconto_livro ():
    produto_livro = ProdutoLivro()
    produto_livro.set_preco(100)
    assert produto_livro.calcularPreco() == 95