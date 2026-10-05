from codigo.sistema_pagamento02 import *

def test_deve_calcular_salario_funcionario_comum():
    funcionario = FuncionarioComum()
    funcionario.set_salario_mensal(1000.0)
    assert funcionario.calcular_pagamento() == 1000.0

def test_deve_calcular_salario_funcionario_gerente():
    funcionario = Gerente()
    funcionario.set_salario_mensal(1000.0)
    funcionario.set_bonus_fixo(200.0)
    assert funcionario.calcular_pagamento() == 1200.0

def test_deve_calcular_salario_funcionario_diretor():
    funcionario = Diretor()
    funcionario.set_salario_mensal(1000.0)
    funcionario.set_lucro_empresa(100000.0)
    funcionario.set_participacao_lucros(2.0)
    assert funcionario.calcular_pagamento() == 3000.0