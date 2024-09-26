import pytest
from projeto.models.pessoa import Pessoa

# Boas práticas de programação.

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 22)
    return pessoa

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Pessoa(22, 22)
        
def test_pessoa_idade_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A idade deve ser um número inteiro."):
        Pessoa("Marta", "22")

def test_pessoa_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio."):
        Pessoa("", 22)

def test_pessoa_nome_valida(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22

def test_pessoa_idade_negativa_retorna_mensagem():        
    with pytest.raises(ValueError, match="A idade não pode ser negativa."):
        Pessoa("Marta", -22)

def test_pessoa_idade_excedente_retorna_mensagem():
    with pytest.raises(ValueError, match="Ninguém é tão velho."):
        Pessoa("Marta", 130)