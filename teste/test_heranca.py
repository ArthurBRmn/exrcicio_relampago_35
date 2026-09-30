from codigo.heranca import *

def test_deve_retornar_matricula_aluno():
    aluno = Aluno()
    aluno.set_matricula(123)
    assert aluno.get_matricula() == 123

def test_deve_retornar_titulacao_professor():
    professor = Professor()
    professor.set_titulacao("Doutorado")
    assert professor.get_titulacao() == "Doutorado"

def test_deve_retornar_nome_pessoa():
    pessoa = Pessoa()
    pessoa.set_nome("Marco")
    assert pessoa.get_nome() == "Marco"

def test_deve_retornar_nome_aluno():
    aluno = Aluno()
    aluno.set_nome("Sara")
    assert aluno.get_nome() == "Sara"

def test_deve_retornar_nome_professor():
    professor = Professor()
    professor.set_nome("Ana")
    assert professor.get_nome() == "Ana"