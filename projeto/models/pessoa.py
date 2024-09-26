class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = self._verificar_nome(nome)
        self.idade = self._verificar_idade(idade)

    # def verificar_idade(self, valor):
    #     if valor < 0:
    #         raise ValueError("A idade não pode ser negativa.")
        
    #     if valor >= 130:
    #         raise ValueError("Ninguém é tão velho.")
        
    #     self.idade = valor
    #     return self.idade

    # Método para verificação.
    def _verificar_nome(self, valor):
        self.__verificar_nome_tipo_invalido(valor)

        self.nome = valor
        return self.nome
    
    # Método para verificação.
    def _verificar_idade(self, valor):
        self.__verificar_idade_tipo_invalido(valor)
        self.__verificar_idade_negativa(valor)
        self.__verificar_idade_acima_130(valor)

        self.idade = valor
        return self.idade
    
    # Método auxiliar.
    def __verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
    
    # Método auxiliar.
    def __verificar_idade_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("A idade deve ser um número inteiro.")

    # Método auxiliar.
    def __verificar_idade_negativa(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")

    # Método auxiliar.    
    def __verificar_idade_acima_130(self, valor):
        if valor >= 130:
            raise ValueError("Ninguém é tão velho.")