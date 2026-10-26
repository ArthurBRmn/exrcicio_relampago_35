from codigo.uniacademia_20262_exercicio_relampago_supresa_pi import *

def test_deve_retornar_nome_escolaridade_professor():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    professor = Professor()
    professor.set_escolaridade(escolaridade)
    assert professor.get_nome_escolaridade() == "Doutorado"

def test_deve_retornar_pessoa_sem_escolaridade():
    professor = Professor()
    assert professor.get_nome_escolaridade() == "Pessoa sem escolaridade"

def test_deve_retornar_nome_estado_cidade():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    assert cidade.get_nome_estado() == "RJ"

def test_deve_retornar_cidade_sem_estado():
    cidade = Cidade()
    assert cidade.get_nome_estado() == "Cidade sem estado"

def test_deve_retornar_nome_estado_naturalidade_aluno():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    aluno = Aluno()
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "RJ"

def test_deve_retornar_aluno_sem_estado_naturalidade():
    aluno = Aluno()
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem estado naturalidade"

def test_a_escolaridade_de_um_professor():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    professor = Professor()
    professor.set_escolaridade(escolaridade)
    assert professor.get_nome_escolaridade() == "Doutorado"

def test_b_escolaridade_do_coordenador_de_um_curso():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Mestrado")
    coordenador = Professor()
    coordenador.set_escolaridade(escolaridade)
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_nome_escolaridade_coordenador() == "Mestrado"

def test_c_escolaridade_do_diretor_de_uma_escola():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    diretor = Professor()
    diretor.set_escolaridade(escolaridade)
    escola = Escola()
    escola.set_diretor(diretor)
    assert escola.get_nome_escolaridade_diretor() == "Doutorado"

def test_d_estado_de_naturalidade_de_um_aluno():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    aluno = Aluno()
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "RJ"

def test_e_cidade_de_naturalidade_de_um_professor():
    cidade = Cidade()
    cidade.set_nome("Juiz de Fora")
    professor = Professor()
    professor.set_naturalidade(cidade)
    assert professor.get_naturalidade().get_nome() == "Juiz de Fora"

def test_f_estado_em_que_um_aluno_estuda():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade()
    cidade.set_estado(estado)
    escola = Escola()
    escola.set_cidade(cidade)
    aluno = Aluno()
    aluno.set_escola(escola)
    assert aluno.get_nome_estado_escola() == "MG"

def test_g_tipo_de_ensino_do_curso_em_que_professor_foi_contratado():
    tipo_ensino = TipoEnsino()
    tipo_ensino.set_nome("Ensino superior")
    curso = Curso()
    curso.set_tipo_ensino(tipo_ensino)
    professor = Professor()
    professor.set_curso_contratacao(curso)
    assert professor.get_curso_contratacao().get_nome_tipo_ensino() == "Ensino superior"

def test_h_coordenador_do_curso_de_um_aluno():
    coordenador = Professor()
    curso = Curso()
    curso.set_coordenador(coordenador)
    aluno = Aluno()
    aluno.set_curso(curso)
    assert aluno.get_nome_escolaridade_coordenador_curso() == "Pessoa sem escolaridade"
    assert aluno.get_curso().get_coordenador() is coordenador

def test_i_diretor_de_um_professor():
    diretor = Professor()
    escola = Escola()
    escola.set_diretor(diretor)
    professor = Professor()
    professor.set_escola(escola)
    assert professor.get_escola().get_diretor() is diretor

def test_j_coordenador_de_um_professor():
    coordenador = Professor()
    curso = Curso()
    curso.set_coordenador(coordenador)
    coordenador.set_curso_coordenacao(curso)
    assert coordenador.get_curso_coordenacao().get_coordenador() is coordenador
