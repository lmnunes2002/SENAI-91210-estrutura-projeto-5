class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)

    def verificar_idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        
        if valor >= 130:
            raise ValueError("Ninguém é tão velho.")
        
        self.idade = valor
        return self.idade

    def _verificar_idade(self, valor):
        self.__verificar_idade_negativa(valor)
        self.__verificar_idade_acima_130(valor)

        self.idade = valor
        return self.idade

    def __verificar_idade_negativa(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        
    def __verificar_idade_acima_130(self, valor):
        if valor >= 130:
            raise ValueError("Ninguém é tão velho.")