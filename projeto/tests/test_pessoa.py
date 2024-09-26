import pytest
from projeto.models.pessoa import Pessoa

# Boas práticas de programação.

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 22)
    return pessoa

def test_pessoa_valida(pessoa_valida):
    pessoa_valida.nome == "Marta"
    pessoa_valida.idade == 23

# def test_type_pessoa_valida(pessoa_valida):
#     type(pessoa_valida.nome) is str == True
#     type(pessoa_valida.idade) is int == True

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22

def test_pessoa_idade_negativa_retorna_mensagem():        
    with pytest.raises(ValueError, match="A idade não pode ser negativa."):
        Pessoa("Marta", -22)

def test_pessoa_idade_excedente_retorna_mensagem():
    with pytest.raises(ValueError, match="Ninguém é tão velho."):
        Pessoa("Marta", 130)