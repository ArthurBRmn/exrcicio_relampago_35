from codigo.conta_bancaria import *

def test_calcular_saque_conta_corrente():
    conta = ContaCorrente()
    conta.set_saldo(1000)
    conta.sacar(100)
    assert conta.get_saldo() == 900

def test_calcular_saque_conta_poupanca():
    conta = ContaPoupanca()
    conta.set_saldo(1000)
    conta.sacar(200)
    assert conta.get_saldo() == 800

def test_calcular_taxa_deposito():
    conta = ContaCorrente()
    conta.set_saldo(1000)
    conta.set_taxa_manutencao(20)
    conta.depositar(100)
    assert conta.get_saldo() == 1080

def test_calcular_taxa_juros():
    conta = ContaPoupanca()
    conta.set_taxa_juros(2)
    conta.set_saldo(1000)
    conta.calcular_juros()
    assert conta.get_saldo() == 1020

